import hashlib
from ledger_models.transaction import Transaction
from ledger_models.block import Block

class InterdimensionalLedger:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.pending_transactions = []
        self.mining_reward = 10

    def create_genesis_block(self):
        return Block("Genesis Block", [], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def mine_pending_transactions(self, miner_address):
        if not self.pending_transactions:
            return False

        new_block = Block(self.get_latest_block().hash, self.pending_transactions, miner_address)
        self.chain.append(new_block)
        self.pending_transactions = []
        return new_block

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

    def get_balance_of_address(self, address):
        balance = 0
        for block in self.chain:
            for transaction in block.transactions:
                if transaction.sender_address == address:
                    balance -= transaction.amount
                elif transaction.recipient_address == address:
                    balance += transaction.amount
        return balance

# Example usage:
ledger = InterdimensionalLedger()
transaction1 = Transaction("Alice", "Bob", 10)
transaction2 = Transaction("Bob", "Charlie", 5)
ledger.add_transaction(transaction1)
ledger.add_transaction(transaction2)
new_block = ledger.mine_pending_transactions("Alice")
print("New block mined:", new_block.hash)
print("Balance of Alice:", ledger.get_balance_of_address("Alice"))
