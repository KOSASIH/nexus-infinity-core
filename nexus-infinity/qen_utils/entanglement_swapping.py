from qen import QuantumEntanglementNetwork
from qen_models.node import Node

class EntanglementSwapping:
    def __init__(self, qen):
        self.qen = qen

    def swap_entanglement(self, node1, node2, node3):
        # Simulate entanglement swapping between three nodes
        if node1 in node2.entangled_nodes and node2 in node3.entangled_nodes:
            node1.entangled_nodes.append(node3)
            node3.entangled_nodes.append(node1)
            return True
        else:
            raise ValueError("Nodes are not entangled")

    def extend_entanglement(self, node1, node2, node3):
        # Simulate extending entanglement between three nodes
        if node1 in node2.entangled_nodes:
            self.qen.entangle_nodes(node2, node3)
            return True
        else:
            raise ValueError("Nodes are not entangled")

# Example usage:
qen = QuantumEntanglementNetwork()
node1 = Node("Node 1")
node2 = Node("Node 2")
node3 = Node("Node 3")
qen.add_node(node1)
qen.add_node(node2)
qen.add_node(node3)
edge1 = Edge(node1, node2)
edge2 = Edge(node2, node3)
qen.add_edge(edge1)
qen.add_edge(edge2)
qen.entangle_nodes(node1, node2)
es = EntanglementSwapping(qen)
es.swap_entanglement(node1, node2, node3)
print("Entanglement swapped between Node 1 and Node 3")
