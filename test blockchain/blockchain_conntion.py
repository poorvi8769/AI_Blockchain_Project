from web3 import Web3

GANACHE_URL = 'http://127.0.0.1:8545'
w3 = Web3(Web3.HTTPProvider(GANACHE_URL))

if w3.is_connected():
    print("Connected to Ganache blockchain!")

    # Use the first two accounts provided by Ganache
    sender = w3.eth.accounts[0]
    recipient = w3.eth.accounts[1]

    # Send a test transaction
    tx_hash = w3.eth.send_transaction({
        'from': sender,
        'to': recipient,
        'value': w3.to_wei(0.1, 'ether'),  # Send 0.1 ETH
    })

    # Wait for transaction receipt
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Transaction successful with hash:", tx_hash.hex())
else:
    print("Failed to connect to the blockchain.")
