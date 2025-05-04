from web3 import Web3

GANACHE_URL = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

if w3.is_connected():
    print("Connected to Ganache blockchain!")
else:
    print("Failed to connect to the blockchain.")
