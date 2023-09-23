import grpc
import branch_pb2
import branch_pb2_grpc
import time

class Customer:
    def __init__(self, id, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.stub = self.createStub()

    # TODO: students are expected to create the Customer stub
    def createStub(self):
        self.channel = grpc.insecure_channel("localhost:5000" + str(self.id))
        return branch_pb2_grpc.BranchStub(self.channel)

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        for event in self.events :
            response = None
            if event["interface"] == "query" :
                print("querying")
                response = self.stub.Query(branch_pb2.Request())
            elif event["interface"] == "withdraw":
                response = self.stub.Withdraw(branch_pb2.Request(money = event["money"]))
            elif event["interface"] == "deposit":
                response = self.stub.Deposit(branch_pb2.Request(money = event["money"]))
            self.recvMsg.append(response)
        print(self.recvMsg)

def run() :
    c = Customer(1, [{"id": 1, "interface": "query"}, {"id": 2, "interface": "deposit", "money" : 170}, {"id": 3, "interface": "withdraw", "money" : 70}, {"id": 4, "interface": "query"}])
    c.executeEvents()

if __name__ == "__main__" :
    run()