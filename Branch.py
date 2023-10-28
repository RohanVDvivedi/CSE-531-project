import grpc
import branch_pb2
import branch_pb2_grpc
from concurrent import futures
from threading import Lock
import signal

class Branch(branch_pb2_grpc.BranchServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
        # lock to protect balance
        self.balanceLock = Lock()
        # the list of process IDs of the branches
        self.branches = branches
        # the list of Client stubs to communicate with the branches
        self.channels = list()
        self.stubList = list()
        for branch in branches :
            if branch == self.id :
                continue
            self.channels.append(grpc.insecure_channel("localhost:" + str(50000 + branch)))
            self.stubList.append(branch_pb2_grpc.BranchStub(self.channels[-1]))
        # logical clock
        self.logical_clock = 0

    def __del__(self) :
        for c in self.channels :
            c.close()

    # TODO: students are expected to process requests from both Client and Branch
    def Query(self, request, context):
        print("Branch Query: " + str(self.id))
        with self.balanceLock:
            balance = self.balance
            # compute recv time stamp
            self.logical_clock = max(self.logical_clock, request.logical_clock) + 1
            # compute send time stamp
            self.logical_clock += 1
            response = branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = self.logical_clock, balance = balance)
        return response
    
    def Withdraw(self, request, context):
        print("Branch Withdraw: " + str(self.id))
        with self.balanceLock:
            self.balance -= request.money
            # compute recv timestamp
            self.logical_clock = max(self.logical_clock, request.logical_clock) + 1
            for branch in self.stubList :
                # compute send timestamp
                self.logical_clock += 1
                resp = branch.Propogate_Withdraw(branch_pb2.Request(customer_request_id = request.customer_request_id, logical_clock = self.logical_clock))
                # compute recv timestamp
                self.logical_clock = max(self.logical_clock, resp.logical_clock) + 1
            # compute send timestamp
            self.logical_clock += 1
            response = branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = self.logical_clock, success = True)
        return response
    
    def Deposit(self, request, context):
        print("Branch Deposit: " + str(self.id))
        with self.balanceLock:
            print("+Branch Deposit: " + str(self.id))
            self.balance += request.money
            # compute recv timestamp
            self.logical_clock = max(self.logical_clock, request.logical_clock) + 1
            for branch in self.stubList :
                # compute send timestamp
                self.logical_clock += 1
                resp = branch.Propogate_Deposit(branch_pb2.Request(customer_request_id = request.customer_request_id, logical_clock = self.logical_clock))
                # compute recv timestamp
                self.logical_clock = max(self.logical_clock, resp.logical_clock) + 1
            # compute send timestamp
            self.logical_clock += 1
            response = branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = self.logical_clock, success = True)
        return response
    
    def Propogate_Withdraw(self, request, context):
        with self.balanceLock:
            self.balance -= request.money
            # compute recv timestamp
            self.logical_clock = max(self.logical_clock, request.logical_clock) + 1
            # compute send timestamp
            self.logical_clock += 1
            response = branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = self.logical_clock, success = True)
        return response
    
    def Propogate_Deposit(self, request, context):
        with self.balanceLock:
            self.balance += request.money
            # compute recv timestamp
            self.logical_clock = max(self.logical_clock, request.logical_clock) + 1
            # compute send timestamp
            self.logical_clock += 1
            response = branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = self.logical_clock, success = True)
        return response

def serve_stop(server, b) :
    server.stop(None)
    del b

def serve(id, balance, branches) :
    b = Branch(id, balance, branches)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers = 5))
    branch_pb2_grpc.add_BranchServicer_to_server(b, server)
    server.add_insecure_port("localhost:" + str(50000 + b.id))
    server.start()
    signal.signal(signal.SIGINT, lambda sig, frame : serve_stop(server, b))
    signal.pause()

if __name__ == "__main__" :
    serve(1, 500, [1])