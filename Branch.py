import grpc
import branch_pb2
import branch_pb2_grpc
from concurrent import futures
from threading import Lock

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
        self.stubList = list()
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # iterate the processID of the branches

        # TODO: students are expected to store the processID of the branches
        pass

    # TODO: students are expected to process requests from both Client and Branch
    def Query(self, request, context):
        self.recvMsg.append(request)
        print("query")
        print(request)
        with self.balanceLock:
            balance = self.balance
        return branch_pb2.Response(balance = balance)
    
    def Withdraw(self, request, context):
        self.recvMsg.append(request)
        print("withdraw")
        print(request)
        with self.balanceLock:
            self.balance -= request.money
        return branch_pb2.Response(success = True)
    
    def Deposit(self, request, context):
        self.recvMsg.append(request)
        print("deposit")
        print(request)
        with self.balanceLock:
            self.balance += request.money
        return branch_pb2.Response(success = True)
    
    def Propogate_Withdraw(self, request, context):
        self.recvMsg.append(request)
        print("propogate_withdraw")
        print(request)
        with self.balanceLock:
            self.balance -= request.money
        return branch_pb2.Response(success = True)
    
    def Propogate_Deposit(self, request, context):
        self.recvMsg.append(request)
        print("propogate_deposit")
        print(request)
        with self.balanceLock:
            self.balance += request.money
        return branch_pb2.Response(success = True)
    
b = Branch(1, 500, [1])

server = grpc.server(futures.ThreadPoolExecutor(max_workers = 5))
branch_pb2_grpc.add_BranchServicer_to_server(b, server)
server.add_insecure_port("localhost:5000" + str(b.id))
server.start()
server.wait_for_termination()