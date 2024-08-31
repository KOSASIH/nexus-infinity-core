import numpy as np
from scipy.linalg import expm
from qiskit import QuantumCircuit, execute
from qiskit.providers.aer import AerSimulator
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

class QKD:
    """
    Quantum Key Distribution (QKD) for secure key exchange.

    Attributes:
    -----------
    qen : QEN
        Quantum Entanglement Network (QEN) instance.
    alice_node : str
        Alice's node identifier.
    bob_node : str
        Bob's node identifier.
    shared_secret : str
        Shared secret key.
    """

    def __init__(self, qen, alice_node, bob_node):
        self.qen = qen
        self.alice_node = alice_node
        self.bob_node = bob_node
        self.shared_secret = ''

    def encode_qubit(self, bit):
        """
        Encode a classical bit onto a qubit.

        Parameters:
        -----------
        bit : int
            Classical bit (0 or 1).

        Returns:
        -------
        qc : QuantumCircuit
            Quantum circuit encoding the classical bit.
        """
        qc = QuantumCircuit(1)
        if bit == 1:
            qc.x(0)
        return qc

    def decode_qubit(self, qc):
        """
        Decode a qubit to retrieve the classical bit.

        Parameters:
        -----------
        qc : QuantumCircuit
            Quantum circuit encoding the qubit.

        Returns:
        -------
        bit : int
            Classical bit (0 or 1).
        """
        job = execute(qc, self.qen.simulator)
        result = job.result()
        measurement = result.get_counts()
        bit = 0 if measurement['0'] > measurement['1'] else 1
        return bit

    def bb84_protocol(self):
        """
        Implement the BB84 protocol for QKD.

        Returns:
        -------
        shared_secret : str
            Shared secret key.
        """
        # Alice prepares and sends qubits to Bob
        alice_bits = np.random.randint(2, size=256)  # 256-bit key
        alice_qubits = [self.encode_qubit(bit) for bit in alice_bits]
        self.qen.teleport_qubit(self.alice_node, self.bob_node, alice_qubits)

        # Bob measures the qubits
        bob_measurements = [self.decode_qubit(qc) for qc in alice_qubits]

        # Alice and Bob publicly compare their bases
        alice_bases = np.random.randint(2, size=256)  # 256-bit key
        bob_bases = np.random.randint(2, size=256)  # 256-bit key
        alice_bases_public = alice_bases.copy()
        bob_bases_public = bob_bases.copy()

        # Alice and Bob discard mismatched bases
        alice_bits_filtered = [alice_bits[i] for i in range(256) if alice_bases[i] == bob_bases[i]]
        bob_measurements_filtered = [bob_measurements[i] for i in range(256) if alice_bases[i] == bob_bases[i]]

        # Alice and Bob generate the shared secret key
        shared_secret = ''
        for i in range(len(alice_bits_filtered)):
            shared_secret += str(alice_bits_filtered[i] ^ bob_measurements_filtered[i])

        self.shared_secret = shared_secret
        return shared_secret

    def hkdf_key_derivation(self, shared_secret):
        """
        Derive a cryptographic key from the shared secret using HKDF.

        Parameters:
        -----------
        shared_secret : str
            Shared secret key.

        Returns:
        -------
        key : bytes
            Derived cryptographic key.
        """
        salt = b'qkd-salt'
        info = b'qkd-key-derivation'
        hkdf = HKDF(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            info=info
        )
        key = hkdf.derive(shared_secret.encode())
        return key
