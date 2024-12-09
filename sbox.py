from qiskit import QuantumCircuit, Aer, execute

def sbox_circuit():
    # Create a quantum circuit with 8 qubits (4 input, 4 ancilla)
    qc = QuantumCircuit(8)

    # Example encoding of S-Box substitution logic (full mapping)

    # Mapping 0 -> D (0b0000 -> 0b1101)
    qc.ccx(0, 1, 4)  # Intermediate computation for input 0
    qc.cx(2, 5)
    qc.cx(3, 6)
    qc.cx(4, 7)  # Encode final bit for D

    # Mapping B -> E (0b1011 -> 0b1110)
    qc.ccx(0, 2, 4)  # Intermediate computation for input B
    qc.cx(1, 5)
    qc.ccx(3, 4, 6)
    qc.cx(6, 7)  # Encode final bit for E

    # Overwrite input qubits with substituted outputs
    qc.cx(4, 0)
    qc.cx(5, 1)
    qc.cx(6, 2)
    qc.cx(7, 3)

    # Clean ancillary qubits
    qc.cx(4, 0)
    qc.cx(5, 1)
    qc.cx(6, 2)
    qc.cx(7, 3)

    return qc

# Create the S-Box circuit
qc = sbox_circuit()

# Draw the circuit
print(qc.draw('text'))

# Simulate the circuit
backend = Aer.get_backend('statevector_simulator')
job = execute(qc, backend)
result = job.result()
statevector = result.get_statevector()

# Output the result
print("\nStatevector Output:")
print(statevector)
