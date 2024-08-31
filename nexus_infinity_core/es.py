import numpy as np
from scipy.linalg import expm
from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import AerSimulator

class EntanglementSwapper:
    """
    Entanglement Swapper for extending entanglement between nodes.

    Attributes:
    -----------
    qen : QEN
        Quantum Entanglement Network (QEN) instance.
    node1 : str
        First node identifier.
    node2 : str
        Second node identifier.
    intermediate_node : str
        Intermediate node identifier.
    """

    def __init__(self, qen, node1, node2, intermediate_node):
        self.qen = qen
        self.node1 = node1
        self.node2 = node2
        self.intermediate_node = intermediate_node

    def entangle_nodes(self, node1, node2):
        """
        Entangle two nodes using the QEN.

        Parameters:
        -----------
        node1 : str
            First node identifier.
        node2 : str
            Second node identifier.
        """
        self.qen.entangle_nodes(node1, node2)

    def swap_entanglement(self):
        """
        Perform entanglement swapping between two nodes using an intermediate node.

        Returns:
        -------
        entangled_state : numpy.array
            Entangled state between the two nodes.
        """
        # Entangle node1 with intermediate node
        self.entangle_nodes(self.node1, self.intermediate_node)

        # Entangle node2 with intermediate node
        self.entangle_nodes(self.node2, self.intermediate_node)

        # Measure the intermediate node
        measurement = self.qen.measure_entanglement(self.intermediate_node, self.node1)
        measurement ^= self.qen.measure_entanglement(self.intermediate_node, self.node2)

        # Apply corrections to node1 and node2
        if measurement == 1:
            self.qen.nodes[self.node1] = '1' if self.qen.nodes[self.node1] == '0' else '0'
            self.qen.nodes[self.node2] = '1' if self.qen.nodes[self.node2] == '0' else '0'

        # Return the entangled state
        entangled_state = self.qen.entanglements[(self.node1, self.node2)]
        return entangled_state

    def extend_entanglement(self):
        """
        Extend entanglement between two nodes using entanglement swapping.

        Returns:
        -------
        entangled_state : numpy.array
            Entangled state between the two nodes.
        """
        # Perform entanglement swapping
        entangled_state = self.swap_entanglement()

        # Update the QEN with the new entanglement
        self.qen.entanglements[(self.node1, self.node2)] = entangled_state

        return entangled_state
