# Script Description
This script retrieves the state value of Ethereum smart contract functions over a specified number of previous blocks and stores the results in a CSV file. The retrieved state values are then reversed to be in chronological order.

## Prerequisites
- Python 3.6 or higher
- `web3`, `python-dotenv`, `tqdm`, and `requests` Python packages

To set up the required environment variables for the script, create a new file in the root directory of your project called .env. Inside this file, set the following two variables:

`RPC_URL`: The URL of the Ethereum node to use for the Web3 provider. This can be the URL of a local node, a remote node, or a node provided by a third-party service. For example, if you are using Infura, the URL will look something like https://mainnet.infura.io/v3/<your-infura-project-id>.

`ETHERSCAN_API_KEY`: An API key for Etherscan.io. You can obtain an API key by creating an account on the Etherscan website and following the instructions provided.

Make sure to save the .env file in the root directory of your project, as the load_dotenv() function in the script expects to find the file in this location.

## Installation
1. Clone the repository or download the script
2. Install the required Python packages using `pip install -r requirements.txt`
3. Set the required environment variables in a `.env` file:
    - `RPC_URL`: URL for the Ethereum node to use for Web3 provider
    - `ETHERSCAN_API_KEY`: API key for Etherscan.io to retrieve the contract ABI

## Usage
python3 script.py <contract_address> <function_names> <number_of_blocks>

- `contract_address`: Ethereum smart contract address to retrieve state values from
- `function_names`: Space-separated list of smart contract function names to retrieve state values for
- `number_of_blocks`: Number of previous blocks to retrieve state values for

The script will output a CSV file with the state values of the specified smart contract functions over the specified number of previous blocks. The CSV file will be named based on the current timestamp, the contract address, the function names, and the number of blocks.

## Example
python3 script.py 0x5B38Da6a701c568545dCfcB03FcB875f56beddC4 balanceOf totalSupply 10

This will retrieve the `balanceOf` and `totalSupply` state values for the smart contract with address `0x5B38Da6a701c568545dCfcB03FcB875f56beddC4` over the previous 10 blocks and store the results in a CSV file.
