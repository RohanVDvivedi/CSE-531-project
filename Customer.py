import grpc
import branch_pb2
import branch_pb2_grpc

class Customer:
    def __init__(self, id, branch_ids, events):
        # unique ID of the Customer
        self.id = id
        # events from the input
        self.events = events
        # a list of received messages used for debugging purpose
        self.recvMsg = list()
        # pointer for the stub
        self.channels = {}
        self.stubs = {}
        for branch_id in branch_ids :
            self.channel[branch_id] = grpc.insecure_channel("localhost:" + str(50000 + branch_id))
            self.stubs[branch_id] =  branch_pb2_grpc.BranchStub(self.channel)

    def __del__(self) :
        for branch_id in self.channels :
            self.channels[branch_id].close()

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        results = []

        for event in self.events :
            if event["interface"] == "query" :
                response = self.stubs[int(event["branch"])].Query(branch_pb2.Request())
            elif event["interface"] == "withdraw":
                response = self.stubs[int(event["branch"])].Withdraw(branch_pb2.Request(money = event["money"]))
            elif event["interface"] == "deposit":
                response = self.stubs[int(event["branch"])].Deposit(branch_pb2.Request(money = event["money"]))

        return results

def run(id, branch_ids, events, result_queue) :
    c = Customer(id, branch_ids, events)
    result_queue.put(c.executeEvents())