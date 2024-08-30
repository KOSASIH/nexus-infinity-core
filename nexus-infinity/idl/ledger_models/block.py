import hashlib

class Block:
    def __init__(self, previous_hash, transactions, miner_address):
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.miner_address = miner_address
        self.timestamp = int(datetime.datetime.now().timestamp())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        string_to_hash = "{}{}{}{}".format(self.previous_hash, self.transactions, self.miner_address, self.timestamp)
        return hashlib.sha256(string_to_hash.encode()).hexdigest()

    def __str__(self):
        return "Block {} - Hash: {}".format(self.timestamp, self.hash)

# Example usage:
block = Block("previous_hash", [Transaction("Alice", "Bob", 10)], "Alice")
print("Block:", block)
