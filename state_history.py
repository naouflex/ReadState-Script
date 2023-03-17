import csv
import argparse
from web3 import Web3
from dotenv import load_dotenv
import os
import time
import requests
from tqdm import tqdm

# Load environment variables from .env file
load_dotenv()

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('contract', type=str, help='Contract address')
parser.add_argument('functions', type=str, nargs='+', help='Function names')
parser.add_argument('blocks', type=int, help='Number of previous blocks to retrieve state value for')

# Parse arguments
args = parser.parse_args()

# Initialize Web3 provider and contract instance
provider = Web3(Web3.HTTPProvider(os.getenv('RPC_URL')))
# Get the ABI from etherscan.io using contract address
ABI = requests.get(f"https://api.etherscan.io/api?module=contract&action=getabi&address={args.contract}&apikey={os.getenv('ETHERSCAN_API_KEY')}").json()['result']
contract = provider.eth.contract(address=args.contract, abi=ABI)

# Retrieve block number of most recent block
block_num = provider.eth.block_number

# Initialize list to store state values over time
state_values = {function: [] for function in args.functions}

# Set up progress bar
pbar = tqdm(total=args.blocks*len(args.functions))

# Loop through previous blocks and retrieve state value for each block
for i in range(args.blocks):
    # Calculate block number to retrieve state value for
    block_to_check = block_num - i
    
    for function in args.functions:
        pbar.set_description(f"Checking block {block_to_check} for {function}")
        # Retrieve state value from contract function call
        state_value = contract.functions[function]().call(block_identifier=block_to_check)/1e18
        
        # Add state value to list
        state_values[function].append(state_value)
        
        # Update progress bar
        pbar.update(1)

# Close progress bar
pbar.close()

# Reverse order of state values list to put them in chronological order
for function in args.functions:
    state_values[function].reverse()

# Generate filename based on current timestamp
filename = f"{int(time.time())}_{args.contract}_{'_'.join(args.functions)}_{args.blocks}.csv"

# Write state values to CSV
with open(filename, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Block'] + args.functions)
    for i in range(args.blocks):
        row = [block_num - i]
        for function in args.functions:
            row.append(state_values[function][i])
        writer.writerow(row)
