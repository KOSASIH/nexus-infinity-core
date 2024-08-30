import random
from qen_models.node import Node
from qen_models.edge import Edge

class QuantumEntanglementNetwork:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edges.append(edge)

    def entangle_nodes(self, node1, node2):
        # Simulate quantum entanglement between two nodes
        node1.entangled_nodes.append(node2)
        node2.entangled_nodes.append(node1)

    def transmit_qubit(self, node1, node2, qubit):
        # Simulate quantum teleportation between two entangled nodes
        if node1 in node2.entangled_nodes:
            node2.receive_qubit(qubit)
        else:
            raise ValueError("Nodes are not entangled")

    def measure_qubit(self, node, qubit):
        # Simulate measurement of a qubit on a node
        measurement = random.choice([-1, 1])  # Simulate random measurement outcome
        node.measurements.append((qubit, measurement))
        return measurement

    def get_node_by_id(self, node_id):
        for node in self.nodes:
            if node.id == node_id:
                return node
        return None

# Example usage:
qen = QuantumEntanglementNetwork()
node1 = Node("Node 1")
node2 = Node("Node 2")
qen.add_node(node1)
qen.add_node(node2)
edge = Edge(node1, node2)
qen.add_edge(edge)
qen.entangle_nodes(node1, node2)
qubit = random.choice([-1, 1])  # Simulate random qubit value
qen.transmit_qubit(node1, node2, qubit)
measurement = qen.measure_qubit(node2, qubit)
print("Measurement outcome:", measurement)
