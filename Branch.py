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
        # the list of process IDs of the branches
        # the list of Client stubs to communicate with the branches
        self.channels = list()
        self.stubList = list()
        self.branches = list()
        for branch in branches :
            if branch == self.id :
                continue
            self.branches.append(branch)
            self.channels.append(grpc.insecure_channel("localhost:" + str(50000 + branch)))
            self.stubList.append(branch_pb2_grpc.BranchStub(self.channels[-1]))
        # logical clock
        self.logical_clock = 0
        self.logical_clock_lock = Lock()
        self.event_processed = []

    def __del__(self) :
        for c in self.channels :
            c.close()
    
    def advance_and_get_logical_clock(self, recv_logical_clock = None) :
        with self.logical_clock_lock:
            if recv_logical_clock == None :
                self.logical_clock += 1
            else :
                self.logical_clock = max(self.logical_clock, recv_logical_clock) + 1
            curr_logical_clock = self.logical_clock
        return curr_logical_clock


    # TODO: students are expected to process requests from both Client and Branch
    def Query(self, request, context):
        recv_time = self.advance_and_get_logical_clock(request.logical_clock)
        self.event_processed.append({"customer-request-id": request.customer_request_id, "logical_clock": recv_time, "interface": "query", "comment":"event_recv from customer " + str(self.id)})
        balance = self.balance
        send_time = self.advance_and_get_logical_clock()
        return branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = send_time, balance = balance)
    
    def Withdraw(self, request, context):
        recv_time = self.advance_and_get_logical_clock(request.logical_clock)
        self.event_processed.append({"customer-request-id": request.customer_request_id, "logical_clock": recv_time, "interface": "withdraw", "comment":"event_recv from customer " + str(self.id)})
        self.balance -= request.money
        for branch_id, branch in zip(self.branches, self.stubList) :
            send_time = self.advance_and_get_logical_clock()
            self.event_processed.append({"customer-request-id": request.customer_request_id, "logical_clock": send_time, "interface": "propogate_withdraw", "comment":"event_sent to branch " + str(branch_id)})
            resp = branch.Propogate_Withdraw(branch_pb2.Request(customer_request_id = request.customer_request_id, from_branch_id = self.id, logical_clock = send_time))
            recv_time = self.advance_and_get_logical_clock(resp.logical_clock)
        send_time = self.advance_and_get_logical_clock()
        return branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = send_time, success = True)
    
    def Deposit(self, request, context):
        recv_time = self.advance_and_get_logical_clock(request.logical_clock)
        self.event_processed.append({"customer-request-id": request.customer_request_id, "logical_clock": recv_time, "interface": "deposit", "comment":"event_recv from customer " + str(self.id)})
        self.balance += request.money
        for branch_id, branch in zip(self.branches, self.stubList) :
            send_time = self.advance_and_get_logical_clock()
            self.event_processed.append({"customer-request-id": request.customer_request_id, "logical_clock": send_time, "interface": "propogate_deposit", "comment":"event_sent to branch " + str(branch_id)})
            resp = branch.Propogate_Deposit(branch_pb2.Request(customer_request_id = request.customer_request_id, from_branch_id = self.id, logical_clock = send_time))
            recv_time = self.advance_and_get_logical_clock(resp.logical_clock)
        send_time = self.advance_and_get_logical_clock()
        return branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = send_time, success = True)
    
    def Propogate_Withdraw(self, request, context):
        recv_time = self.advance_and_get_logical_clock(request.logical_clock)
        self.event_processed.append({"customer-request-id": request.customer_request_id, "logical_clock": recv_time, "interface": "propogate_withdraw", "comment":"event_recv from branch " + str(request.from_branch_id)})
        self.balance -= request.money
        send_time = self.advance_and_get_logical_clock()
        return branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = send_time, success = True)
    
    def Propogate_Deposit(self, request, context):
        recv_time =self.advance_and_get_logical_clock(request.logical_clock)
        self.event_processed.append({"customer-request-id": request.customer_request_id, "logical_clock": recv_time, "interface": "propogate_deposit", "comment":"event_recv from branch " + str(request.from_branch_id)})
        self.balance += request.money
        send_time = self.advance_and_get_logical_clock()
        return branch_pb2.Response(customer_request_id = request.customer_request_id, logical_clock = send_time, success = True)

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