import hashlib

class Transaction:
    def __init__(self, sender_address, recipient_address, amount):
        self.sender_address = sender_address
        self.recipient_address = recipient_address
        self.amount = amount
        self.timestamp = int(datetime.datetime.now().timestamp())
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        string_to_hash = "{}{}{}{}".format(self.sender_address, self.recipient_address, self.amount, self.timestamp)
        return hashlib.sha256(string_to_hash.encode()).hexdigest()

# Example usage:
transaction = Transaction("Alice", "Bob", 10)
print("Transaction hash:", transaction.hash)
