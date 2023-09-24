import json
import multiprocessing as mp
import time
import os
import signal

import Branch
import Customer

input_file = open('input.json')
input_params = json.load(input_file)
input_file.close()

branches = []

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

customer_pids = []
for customer in input_params :
    if customer["type"] == "customer" :
        p = mp.Process(target = Customer.run,  args = (int(customer["id"]), customer["events"]))
        p.start()
        customer_pids.append(p)

# let the proceessing and message passing occur
time.sleep(10)

# join all customers and branches

for customer_pid in customer_pids :
    customer_pid.join()

for branch_pid in branch_pids :
    os.kill(branch_pid.pid, signal.SIGINT)
    branch_pid.join()