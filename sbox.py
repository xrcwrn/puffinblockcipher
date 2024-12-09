from qiskit import QuantumCircuit

def generate_explicit_sbox_circuit():
    """
    Generate an explicit quantum circuit for the S-Box mapping:
    Input:  0  1  2  3  4  5  6  7  8  9  A  B  C  D  E  F
    Output: D  7  3  2  9  A  C  1  F  4  5  E  6  0  B  8
    """
    qc = QuantumCircuit(8)

    # Input 0 -> Output D
    qc.ccx(0, 1, 4)
    qc.cx(2, 5)
    qc.cx(3, 6)
    qc.cx(4, 7)

    # Input 1 -> Output 7
    qc.cx(0, 4)
    qc.ccx(1, 2, 5)
    qc.cx(3, 6)
    qc.cx(5, 7)

    # Input 2 -> Output 3
    qc.cx(1, 4)
    qc.cx(2, 5)
    qc.cx(4, 7)
    qc.cx(5, 7)

    # Input 3 -> Output 2
    qc.cx(0, 4)
    qc.cx(1, 5)
    qc.cx(5, 7)

    # Input 4 -> Output 9
    qc.ccx(0, 3, 4)
    qc.cx(2, 5)
    qc.cx(6, 7)

    # Input 5 -> Output A
    qc.cx(0, 4)
    qc.cx(3, 5)
    qc.cx(6, 7)

    # Input 6 -> Output C
    qc.cx(1, 4)
    qc.cx(3, 6)
    qc.cx(5, 7)
    qc.cx(6, 7)

    # Input 7 -> Output 1
    qc.ccx(0, 2, 4)
    qc.cx(6, 7)

    # Input 8 -> Output F
    qc.cx(0, 4)
    qc.cx(1, 5)
    qc.cx(2, 6)
    qc.cx(3, 7)

    # Input 9 -> Output 4
    qc.ccx(0, 2, 4)
    qc.cx(5, 7)

    # Input A -> Output 5
    qc.cx(1, 4)
    qc.cx(3, 5)
    qc.cx(6, 7)

    # Input B -> Output E
    qc.cx(2, 4)
    qc.cx(3, 5)
    qc.cx(4, 7)

    # Input C -> Output 6
    qc.cx(0, 4)
    qc.cx(1, 5)
    qc.cx(6, 7)

    # Input D -> Output 0
    qc.cx(0, 4)
    qc.cx(1, 5)

    # Input E -> Output B
    qc.cx(2, 4)
    qc.cx(3, 5)
    qc.cx(6, 7)

    # Input F -> Output 8
    qc.ccx(0, 1, 4)
    qc.cx(2, 5)
    qc.cx(3, 6)

    return qc

# Generate the explicit S-Box circuit
explicit_sbox_circuit = generate_explicit_sbox_circuit()

# Draw the circuit
print(explicit_sbox_circuit.draw('text'))
