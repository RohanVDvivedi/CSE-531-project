import grpc
import branch_pb2
import branch_pb2_grpc

class Branch(branch_pb2_grpc.BranchServicer):

    def __init__(self, id, balance, branches):
        # unique ID of the Branch
        self.id = id
        # replica of the Branch's balance
        self.balance = balance
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
    
    def Withdraw(self, request, context):
        self.recvMsg.append(request)
    
    def Deposit(self, request, context):
        self.recvMsg.append(request)
    
    def Propogate_Withdraw(self, request, context):
        self.recvMsg.append(request)
    
    def Propogate_Deposit(self, request, context):
        self.recvMsg.append(request)