from web3 import Web3

# Initialize Web3 connection
GANACHE_URL = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

if w3.is_connected():
    print("Connected to Ganache blockchain!")
else:
    raise ConnectionError("Failed to connect to the blockchain!")

# Use the first account from Ganache
DEFAULT_ACCOUNT = w3.eth.accounts[0]
w3.eth.default_account = DEFAULT_ACCOUNT

def save_report_to_blockchain(report):
    """
    Save a hashed report to the blockchain.
    """
    report_hash = Web3.keccak(text=report).hex()
    tx_hash = w3.eth.send_transaction({
        'from': w3.eth.default_account,
        'to': w3.eth.accounts[1],  # Example recipient account
        'value': 0,
        'data': report_hash
    })
    return tx_hash.hex()


def verify_report_hash(tx_hash):
    """
    Verify the hash of a report from a blockchain transaction.
    """
    transaction = w3.eth.get_transaction(tx_hash)
    stored_hash = transaction.input
    return stored_hash
