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
        # logical clock
        self.logical_clock = 0

    def __del__(self) :
        self.channel.close()

    # TODO: students are expected to create the Customer stub
    def createStub(self):
        self.channel = grpc.insecure_channel("localhost:" + str(50000 + self.id))
        return branch_pb2_grpc.BranchStub(self.channel)

    # TODO: students are expected to send out the events to the Bank
    def executeEvents(self):
        event_processed = []

        for event in self.events :
            self.logical_clock += 1
            event_processed.append({"customer_request_id" : int(event["customer-request-id"]), "logical_clock" : self.logical_clock, "interface": event["interface"], "comment": "event_sent from customer " + str(self.id)})
            curr_message_logical_clock = self.logical_clock
            if event["interface"] == "query" :
                response = self.stub.Query(branch_pb2.Request(customer_request_id = int(event["customer-request-id"]), logical_clock = curr_message_logical_clock))
            elif event["interface"] == "withdraw":
                response = self.stub.Withdraw(branch_pb2.Request(customer_request_id = int(event["customer-request-id"]), logical_clock = curr_message_logical_clock, money = event["money"]))
            elif event["interface"] == "deposit":
                response = self.stub.Deposit(branch_pb2.Request(customer_request_id = int(event["customer-request-id"]), logical_clock = curr_message_logical_clock, money = event["money"]))
            self.logical_clock = max(self.logical_clock, response.logical_clock) + 1
            event_processed.append({"customer_request_id" : int(event["customer-request-id"]), "logical_clock" : self.logical_clock, "interface": event["interface"], "comment": "event_recv from branch " + str(self.id)})
            self.recvMsg.append(response)

        event_processed.sort(key = lambda e : e["logical_clock"])
        return {"id":self.id, "type":"customer", "events": event_processed}

def run(id, events, result_queue) :
    c = Customer(id, events)
    result_queue.put(c.executeEvents())