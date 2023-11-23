import json
import multiprocessing as mp
import time
import os
import signal

import Branch
import Customer

input_file = open('input_big.json')
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
        p = mp.Process(target = Branch.serve, args = (int(branch["id"]), int(branch["balance"]), branches))
        p.start()
        branch_pids.append(p)

# sleep for a second, let the servers start
time.sleep(1)

# build customer processes
customer_pids = []
for customer in input_params :
    if customer["type"] == "customer" :
        p = mp.Process(target = Customer.run,  args = (int(customer["id"]), branches, customer["events"], result_queue))
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

# gather results
results = []
for i in range(len(customer_pids)) :
    results.extend(result_queue.get())

results_json = json.dumps(results, indent = 4)

# write output to file
output_file = open('customer_events.json', "w")
output_file.write(results_json)
output_file.close()