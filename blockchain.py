"""
A simple Blockchain in Python
"""
from flask import Flask, request
import hashlib
import json

class Block:
    
    def __init__(self, previous_block_hash, transaction_list):

        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = f"{' - '.join(transaction_list)} - {previous_block_hash}"
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.generate_genesis_block()

    def generate_genesis_block(self):
        self.chain.append(Block("0", ['Genesis Block']))
    
    def create_block_from_transaction(self, transaction_list):
        previous_block_hash = self.last_block.block_hash
        self.chain.append(Block(previous_block_hash, transaction_list))

    def display_chain(self):
        for i in range(len(self.chain)):
            print(f"Data {i + 1}: {self.chain[i].block_data}")
            print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

    @property
    def last_block(self):
        return self.chain[-1]

app = Flask(__name__)
blockchain = Blockchain()


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    hashes = []
    for block in blockchain.chain:
        chain_data.append(block.block_data)
        hashes.append(block.block_hash)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data,
                       "hash": hashes})



app.run(debug=True, port=8080)
