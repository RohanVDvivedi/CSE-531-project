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
        for branch in branches :
            if branch == self.id :
                continue
            self.channels.append(grpc.insecure_channel("localhost:" + str(50000 + branch)))
            self.stubList.append(branch_pb2_grpc.BranchStub(self.channels[-1]))

    def __del__(self) :
        for c in self.channels :
            c.close()

    # TODO: students are expected to process requests from both Client and Branch
    def Query(self, request, context):
        balance = self.balance
        return branch_pb2.Response(balance = balance)
    
    def Withdraw(self, request, context):
        self.balance -= request.money
        for branch in self.stubList :
            branch.Propogate_Withdraw(branch_pb2.Request(money = request.money))
        return branch_pb2.Response(success = True)
    
    def Deposit(self, request, context):
        self.balance += request.money
        for branch in self.stubList :
            branch.Propogate_Deposit(branch_pb2.Request(money = request.money))
        return branch_pb2.Response(success = True)
    
    def Propogate_Withdraw(self, request, context):
        self.balance -= request.money
        return branch_pb2.Response(success = True)
    
    def Propogate_Deposit(self, request, context):
        self.balance += request.money
        return branch_pb2.Response(success = True)

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