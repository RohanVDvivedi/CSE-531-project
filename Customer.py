import grpc
import branch_pb2
import branch_pb2_grpc

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

    def __del__(self) :
        self.channel.close()

    # TODO: students are expected to create the Customer stub
    def createStub(self):
        self.channel = grpc.insecure_channel("localhost:" + str(50000 + self.id))
        return branch_pb2_grpc.BranchStub(self.channel)

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        results = []

        for event in self.events :
            if event["interface"] == "query" :
                response = self.stub.Query(branch_pb2.Request())
            elif event["interface"] == "withdraw":
                response = self.stub.Withdraw(branch_pb2.Request(money = event["money"]))
            elif event["interface"] == "deposit":
                response = self.stub.Deposit(branch_pb2.Request(money = event["money"]))
            self.recvMsg.append(response)

        return results

def run(id, events, result_queue) :
    c = Customer(id, events)
    result_queue.put(c.executeEvents())