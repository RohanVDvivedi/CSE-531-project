import grpc
import branch_pb2
import branch_pb2_grpc
import time
import json

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
        print("Customer: " + str(self.id))
        event_processed = []

        for event in self.events :
            self.logical_clock += 1
            curr_message_logical_clock = self.logical_clock
            if event["interface"] == "query" :
                response = self.stub.Query(branch_pb2.Request(customer_request_id = int(event["customer-request-id"]), logical_clock = curr_message_logical_clock))
            elif event["interface"] == "withdraw":
                response = self.stub.Withdraw(branch_pb2.Request(customer_request_id = int(event["customer-request-id"]), logical_clock = curr_message_logical_clock, money = event["money"]))
            elif event["interface"] == "deposit":
                response = self.stub.Deposit(branch_pb2.Request(customer_request_id = int(event["customer-request-id"]), logical_clock = curr_message_logical_clock, money = event["money"]))
            event_processed.append({"customer_request_id" : int(event["customer-request-id"]), "logical_clock" : self.logical_clock, "interface": event["interface"], "comment": "event_sent from customer" + str(self.id)})
            self.logical_clock = max(self.logical_clock, response.logical_clock) + 1
            self.recvMsg.append(response)

        results_json = json.dumps(event_processed)

        print(results_json)

def run(id, events) :
    c = Customer(id, events)
    c.executeEvents()

if __name__ == "__main__" :
    run(1, [{"id": 1, "interface": "query"}, {"id": 2, "interface": "deposit", "money" : 170}, {"id": 3, "interface": "withdraw", "money" : 70}, {"id": 4, "interface": "query"}])