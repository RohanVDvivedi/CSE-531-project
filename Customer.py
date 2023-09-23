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
                response = self.stub.MsgDelivery(branch_pb2.Request(id = event["id"], interface = event["interface"]))
            else:
                response = self.stub.MsgDelivery(branch_pb2.Request(id = event["id"], interface = event["interface"], money = event["money"]))
            self.recvMsg.append(response)
        print(self.recvMsg)

# use customer
c = Customer(1, [{"id": 1, "interface": "query"}])
c.executeEvents()