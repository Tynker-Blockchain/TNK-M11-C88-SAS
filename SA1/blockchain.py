import hashlib
import json
from time import time
from hash import generateHash

class BlockChain():
    def __init__(self):
        self.chain = []

    def addBlock(self, newBlock):
        if(len(self.chain) == 0):
            self.createGenesisBlock()
        newBlock.previousHash = self.chain[-1].currentHash
        newBlock.currentHash = newBlock.calculateHash()
        self.chain.append(newBlock)
    
    def createGenesisBlock(self):
        genesisBlock = Block(0, time(), [], "No Previous Hash Present. Since this is the first block.")
        self.chain.append(genesisBlock)
    
    def printChain(self):
        for block in self.chain:
            print("Block Index", block.index)
            print("Timestamp", block.timestamp)
            print("Transaction", block.transaction)
            print( "Previous Hash",block.previousHash)
            print( "Current Hash",block.currentHash)
            print( "Is Valid Block",block.isValid)

            print("*" * 100 , "\n")

    # Define validateBlock() method that takes a parameter named currenBlock
    def validateBlock(self, currentBlock):

        # Create variable previousBlock and save previous block init using "index of current block-1"
        previousBlock = self.chain[currentBlock.index - 1]
       
        # Checking whether the current block index is greater than previous block index or not
        if(currentBlock.index != previousBlock.index + 1):
            # Return false
            return False
        
        # Calculate hash for previousBlock and store it in previousBlockhash
        previousBlockHash = previousBlock.calculateHash()

        # Checking whether the previous block hash and current block hash is equal or not 
        if(previousBlockHash != currentBlock.previousHash):
            # Return flase
            return False
        # return True
        return True
        
class Block:
    def __init__(self, index, timestamp, transaction, previousHash):
        self.index = index
        self.transaction = transaction
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = self.calculateHash()
        self.isValid = None
       
    def calculateHash(self, timestamp=None):
        if(timestamp == None):
            timestamp = self.timestamp

        blockString = str(self.index) + str(timestamp) + str(self.previousHash) + str(self.transaction)
        return generateHash(blockString)
       
transaction = {
        'sender': 'Satoshi',
        'receiver': 'Mike',
        'amount': '5 ETH'
    }

sender = generateHash(transaction["sender"])
receiver = generateHash(transaction["receiver"])

transaction["sender"] = sender
transaction["receiver"] = receiver

blockData = {
        'index': 1,
        'timestamp': time(),
        'transaction': transaction,
        'previousHash': "No Previous Hash Present. Since this is the first block.",
    }

newBlock = Block(
    blockData["index"], 
    blockData["timestamp"], 
    blockData["transaction"],
    blockData["previousHash"])

chain = BlockChain()
chain.addBlock(newBlock)

# Validating the new block using chain.validateBlock() method
isValid = chain.validateBlock(newBlock)
# Change the validation aatribute i.e isValid for the newBlock to returned value
newBlock.isValid = isValid

chain.printChain()
