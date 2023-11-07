import json
import multiprocessing as mp
import time
import os
import signal

import Branch
import Customer

input_file = open('input_10.json')
input_params = json.load(input_file)
input_file.close()

branches = []

result_queue = mp.Queue()

for branch in input_params :
    if branch["type"] == "branch" :
        branches.append(int(branch["id"]))

branch_pids = []
for branch in input_params :
    if branch["type"] == "branch" :
        p = mp.Process(target = Branch.serve, args = (int(branch["id"]), int(branch["balance"]), branches, result_queue))
        p.start()
        branch_pids.append(p)

# sleep for a second, let the servers start
time.sleep(1)

# build customer processes
customer_pids = []
for customer in input_params :
    if customer["type"] == "customer" :
        p = mp.Process(target = Customer.run,  args = (int(customer["id"]), customer["customer-requests"], result_queue))
        customer_pids.append(p)

# run customer processes
for customer_pid in customer_pids :
    customer_pid.start()

# join customer processes
for customer_pid in customer_pids :
    customer_pid.join()

# join all branches
for branch_pid in branch_pids :
    os.kill(branch_pid.pid, signal.SIGINT)
    branch_pid.join()

# gather results of all customers and branches
results_customer = []
results_branch = []
for i in range(len(input_params)) :
    r = result_queue.get()
    if(r["type"] == "customer"):
        results_customer.append(r)
    else:
        results_branch.append(r)

all_events = []
for r in results_customer :
    for e in r["events"]:
        _e = dict(e)
        _e["id"] = r["id"]
        all_events.append(_e)
for r in results_branch :
    for e in r["events"]:
        _e = dict(e)
        _e["id"] = r["id"]
        all_events.append(_e)
all_events.sort(key = lambda e : (e["customer-request-id"], e["logical_clock"]))

# sort results_customer by id
results_customer.sort(key = lambda e : e["id"])

# sort results_branch by id
results_branch.sort(key = lambda e : e["id"])

results_customer_json = json.dumps(results_customer, indent = 4)
f = open("customer_output.json", "w")
f.write(results_customer_json)
f.close()

results_branch_json = json.dumps(results_branch, indent = 4)
f = open("branch_output.json", "w")
f.write(results_branch_json)
f.close()

all_events_json = json.dumps(all_events, indent = 4)
f = open("events_output.json", "w")
f.write(all_events_json)
f.close()