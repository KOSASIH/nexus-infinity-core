from qen import QuantumEntanglementNetwork
from qen_utils.quantum_key_distribution import QuantumKeyDistribution
from qen_utils.entanglement_swapping import EntanglementSwapping

class NexusInfinity:
    def __init__(self):
        self.qen = QuantumEntanglementNetwork()
        self.qkd = QuantumKeyDistribution(self.qen)
        self.es = EntanglementSwapping(self.qen)

    def create_node(self, name):
        node = Node(name)
        self.qen.add_node(node)
        return node

    def create_edge(self, node1, node2):
        edge = Edge(node1, node2)
        self.qen.add_edge(edge)
        return edge

    def entangle_nodes(self, node1, node2):
        self.qen.entangle_nodes(node1, node2)

    def generate_key(self, node1, node2):
        return self.qkd.generate_key(node1, node2)

    def get_shared_key(self, node1, node2):
        return self.qkd.get_shared_key(node1, node2)

    def swap_entanglement(self, node1, node2, node3):
        return self.es.swap_entanglement(node1, node2, node3)

    def extend_entanglement(self, node1, node2, node3):
        return self.es.extend_entanglement(node1, node2, node3)

# Example usage:
ni = NexusInfinity()
node1 = ni.create_node("Node 1")
node2 = ni.create_node("Node 2")
node3 = ni.create_node("Node 3")
edge1 = ni.create_edge(node1, node2)
edge2 = ni.create_edge(node2, node3)
ni.entangle_nodes(node1, node2)
key = ni.generate_key(node1, node2)
print("Shared secret key:", key)
ni.swap_entanglement(node1, node2, node3)
print("Entanglement swapped between Node 1 and Node 3")
