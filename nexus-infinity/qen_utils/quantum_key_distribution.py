import random
from qen import QuantumEntanglementNetwork

class QuantumKeyDistribution:
    def __init__(self, qen):
        self.qen = qen
        self.keys = {}

    def generate_key(self, node1, node2):
        # Simulate quantum key distribution between two nodes
        qubit1 = random.choice([-1, 1])  # Simulate random qubit value
        qubit2 = qubit1  # Assume perfect entanglement
        self.qen.transmit_qubit(node1, node2, qubit1)
        measurement1 = self.qen.measure_qubit(node1, qubit1)
        measurement2 = self.qen.measure_qubit(node2, qubit2)
        if measurement1 == measurement2:
            key = qubit1  # Shared secret key
            self.keys[(node1.id, node2.id)] = key
            return key
        else:
            raise ValueError("Key distribution failed")

    def get_shared_key(self, node1, node2):
        return self.keys.get((node1.id, node2.id))

# Example usage:
qen = QuantumEntanglementNetwork()
node1 = Node("Node 1")
node2 = Node("Node 2")
qen.add_node(node1)
qen.add_node(node2)
edge = Edge(node1, node2)
qen.add_edge(edge)
qen.entangle_nodes(node1, node2)
qkd = QuantumKeyDistribution(qen)
key = qkd.generate_key(node1, node2)
print("Shared secret key:", key)
