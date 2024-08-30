import unittest
from qen import QuantumEntanglementNetwork

class TestQEN(unittest.TestCase):
    def setUp(self):
        self.qen = QuantumEntanglementNetwork()

    def test_add_node(self):
        node = Node("Node 1")
        self.qen.add_node(node)
        self.assertIn(node, self.qen.nodes)

    def test_add_edge(self):
        node1 = Node("Node 1")
        node2 = Node("Node 2")
        edge = Edge(node1, node2)
        self.qen.add_edge(edge)
        self.assertIn(edge, self.qen.edges)

    def test_entangle_nodes(self):
        node1 = Node("Node 1")
        node2 = Node("Node 2")
        self.qen.entangle_nodes(node1, node2)
        self.assertIn(node2, node1.entangled_nodes)

if __name__ == "__main__":
    unittest.main()
