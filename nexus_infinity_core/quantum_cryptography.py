import numpy as np
from qiskit import QuantumCircuit, execute, Aer

class QuantumCryptography:
    """
    Quantum Cryptography for secure communication and data encryption.

    Attributes:
    -----------
    num_qubits : int
        Number of qubits for quantum key distribution.
    """

    def __init__(self, num_qubits):
        self.num_qubits = num_qubits

    def generate_quantum_key(self):
        """
        Generate a quantum key using quantum key distribution.

        Returns:
        -------
        quantum_key : numpy.array
            Generated quantum key.
        """
        qc = QuantumCircuit(self.num_qubits)
        qc.h(range(self.num_qubits))
        qc.measure_all()
        job = execute(qc, backend=Aer.get_backend('qasm_simulator'), shots=1024)
        result = job.result()
        quantum_key = np.array(result.get_counts(qc))
        return quantum_key

    def encrypt_data(self, data, quantum_key):
        """
        Encrypt data using the quantum key.

        Parameters:
        -----------
        data : numpy.array
            Data to encrypt.
        quantum_key : numpy.array
            Quantum key for encryption.

        Returns:
        -------
        encrypted_data : numpy.array
            Encrypted data.
        """
        encrypted_data = np.bitwise_xor(data, quantum_key)
        return encrypted_data

    def decrypt_data(self, encrypted_data, quantum_key):
        """
        Decrypt data using the quantum key.

        Parameters:
        -----------
        encrypted_data : numpy.array
            Encrypted data.
        quantum_key : numpy.array
            Quantum key for decryption.

        Returns:
        -------
        decrypted_data : numpy.array
            Decrypted data.
        """
        decrypted_data = np.bitwise_xor(encrypted_data, quantum_key)
        return decrypted_data
