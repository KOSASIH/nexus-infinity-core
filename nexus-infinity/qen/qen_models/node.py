class Node:
    def __init__(self, name):
        self.id = name
        self.entangled_nodes = []
        self.measurements = []

    def receive_qubit(self, qubit):
        # Simulate reception of a qubit on a node
        self.measurements.append((qubit, None))  # Store qubit for later measurement

    def __str__(self):
        return "Node {}".format(self.id)

# Example usage:
node = Node("Node 1")
print("Node:", node)
