from qiskit import QuantumCircuit

def p64_layer():
    """
    Implements the P64-Layer for a 64-bit permutation based on Table A1.
    """
    # Create a quantum circuit with 64 qubits
    qc = QuantumCircuit(64)

    # P64 permutation table
    p64_table = [
        12, 1, 59, 49, 50, 26, 9, 35,
        24, 6, 31, 60, 0, 48, 46, 18,
        33, 52, 15, 21, 56, 19, 47, 40,
        8, 51, 5, 30, 61, 29, 27, 10,
        36, 16, 57, 7, 32, 43, 45, 58,
        23, 54, 62, 37, 55, 38, 14, 22,
        13, 3, 4, 25, 17, 53, 41, 44,
        20, 34, 39, 2, 11, 28, 42, 63
    ]

    # Apply SWAP gates to perform the permutation
    for i, target in enumerate(p64_table):
        if i < target:  # Avoid redundant swaps
            qc.swap(i, target - 1)  # Adjust for 0-based indexing

    return qc

# Create the P64-Layer circuit
qc = p64_layer()

# Draw the circuit
print(qc.draw('text'))

