from qiskit import QuantumCircuit

def key_scheduler():
    """
    Implements the Key Scheduler for generating subkeys K0, K1, ..., K32
    from a 128-bit master key.
    """
    # Create a quantum circuit with 128 qubits (master key) and 64 output qubits (subkey)
    qc = QuantumCircuit(128 + 64)

    # Define P128 permutation table
    p128_table = [
        127, 126, 125, 124, 123, 122, 121, 120,
        119, 118, 117, 116, 115, 114, 113, 112,
        111, 110, 109, 108, 107, 106, 105, 104,
        103, 102, 101, 100, 99,  98,  97,  96,
        95,  94,  93,  92,  91,  90,  89,  88,
        87,  86,  85,  84,  83,  82,  81,  80,
        79,  78,  77,  76,  75,  74,  73,  72,
        71,  70,  69,  68,  67,  66,  65,  64,
        63,  62,  61,  60,  59,  58,  57,  56,
        55,  54,  53,  52,  51,  50,  49,  48,
        47,  46,  45,  44,  43,  42,  41,  40,
        39,  38,  37,  36,  35,  34,  33,  32,
        31,  30,  29,  28,  27,  26,  25,  24,
        23,  22,  21,  20,  19,  18,  17,  16,
        15,  14,  13,  12,  11,  10,  9,   8,
        7,   6,   5,   4,   3,   2,   1,   0
    ]

    # Define bit inversion positions
    bit_inversion_positions = [1, 2, 3, 5]

    # Define S64 selection table
    s64_table = [
        0, 1, 2, 3, 4, 5, 6, 7,
        8, 9, 10, 11, 12, 13, 14, 15,
        16, 17, 18, 19, 20, 21, 22, 23,
        24, 25, 26, 27, 28, 29, 30, 31,
        32, 33, 34, 35, 36, 37, 38, 39,
        40, 41, 42, 43, 44, 45, 46, 47,
        48, 49, 50, 51, 52, 53, 54, 55,
        56, 57, 58, 59, 60, 61, 62, 63
    ]

    # Step 1: Apply P128 permutation
    for i, target in enumerate(p128_table):
        if i < target:  # Avoid redundant swaps
            qc.swap(i, target)

    # Step 2: Bit inversion
    for position in bit_inversion_positions:
        qc.x(position)  # Apply NOT gate to invert bits

    # Step 3: Select 64 bits for subkey
    for i, target in enumerate(s64_table):
        qc.cx(target, 128 + i)  # Copy selected bit to the subkey register

    # Step 4: Repeat P128 for the next round (if needed)
    for i, target in enumerate(p128_table):
        if i < target:
            qc.swap(i, target)

    return qc

# Create the Key Scheduler circuit
qc = key_scheduler()

# Draw the circuit
print(qc.draw('text'))

