import numpy as np

# Example S-Box (PUFFIN S-Box values can replace this)
SBOX = [
    0x3, 0xF, 0xE, 0x1, 0x0, 0xA, 0x7, 0x4,
    0xC, 0x5, 0x6, 0xB, 0x9, 0xD, 0x2, 0x8
]

# PUFFIN tables
TABLE_8 = [
    [2, 122, 14, 57, 88, 35, 97, 51],
    [56, 62, 99, 69, 45, 70, 93, 50],
    [82, 13, 3, 21, 31, 113, 83, 100],
    [11, 22, 30, 64, 40, 95, 119, 49],
    [44, 53, 111, 121, 28, 80, 29, 120],
    [96, 54, 25, 63, 23, 116, 18, 8],
    [110, 17, 43, 85, 15, 94, 41, 71],
    [1, 90, 117, 123, 37, 47, 42, 38],
]

TABLE_9 = [
    [21, 120, 125, 109, 78, 80, 115, 54],
    [112, 20, 28, 19, 55, 75, 40, 111],
    [44, 108, 94, 86, 93, 43, 67, 7],
    [114, 68, 5, 74, 82, 4, 53, 69],
    [22, 60, 105, 102, 84, 123, 110, 51],
    [118, 31, 99, 16, 14, 33, 127, 90],
    [57, 98, 119, 66, 30, 97, 52, 70],
    [91, 24, 37, 92, 64, 1, 36, 27],
]

# Functions for transformations
def sbox_substitution(matrix):
    """Apply S-Box substitution to each element."""
    return np.vectorize(lambda x: SBOX[x & 0xF])(matrix)

def extract_subkey(state, table):
    """Extract the subkey from the state using TABLE_8."""
    subkey = 0
    for row in table:
        for bit_position in row:
            subkey = (subkey << 1) | ((state >> bit_position) & 1)
    return subkey

def permute_matrix(matrix, table):
    """Permute the matrix using TABLE_9."""
    flattened = matrix.flatten()  # Flatten the matrix for easier indexing
    permuted = np.zeros_like(flattened)  # Create an array for permuted values
    
    for i, row in enumerate(table):
        for j, bit_position in enumerate(row):
            if bit_position < len(flattened):
                permuted[i * len(row) + j] = flattened[bit_position]
    
    return permuted.reshape(matrix.shape)

def invert_matrix_bits(matrix, bit_positions):
    """Invert specific bits in the matrix."""
    for bit in bit_positions:
        matrix = np.bitwise_xor(matrix, (1 << bit))
    return matrix

def check_cell_type(matrix):
    """Classify columns of the matrix as A, C, or B."""
    result = []
    transposed = np.array(matrix).T  # Transpose to process columns
    for column in transposed:
        if sorted(column) == list(range(16)):
            result.append("A")
        elif len(set(column)) == 1:
            result.append("C")
        elif np.bitwise_xor.reduce(column) == 0:
            result.append("B")
        else:
            result.append("U")  # Undefined
    return np.array(result).reshape(4, 4)  # Reshape into 4x4 format

def format_to_matrix(matrix):
    """Print the matrix in readable format."""
    for row in matrix:
        print("  ".join(str(x) for x in row))

# Main PUFFIN algorithm
def apply_puffin(input_matrix, rounds=4):
    """Apply the PUFFIN algorithm with intermediate outputs."""
    current_matrix = np.array(input_matrix, dtype=np.uint8)  # Ensure uint8 for bitwise operations

    for round_num in range(1, rounds + 1):
        print(f"\n--- Round {round_num} ---")

        # Step 1: S-Box Substitution
        current_matrix = sbox_substitution(current_matrix)
        print(f"After S-Box (Round {round_num}):")
        format_to_matrix(current_matrix)

        cell_types = check_cell_type(current_matrix)
        print(f"Cell Types (After S-Box, Round {round_num}):")
        format_to_matrix(cell_types)

        # Step 2: Subkey XOR
        subkey = extract_subkey(0x0123456789ABCDEF0123456789ABCDEF, TABLE_8)  # Example master key
        subkey_array = np.full(current_matrix.shape, subkey, dtype=np.uint8)
        current_matrix = np.bitwise_xor(current_matrix, subkey_array)
        print(f"After XOR with Subkey (Round {round_num}):")
        format_to_matrix(current_matrix)

        cell_types = check_cell_type(current_matrix)
        print(f"Cell Types (After XOR, Round {round_num}):")
        format_to_matrix(cell_types)

        # Step 3: Permutation
        current_matrix = permute_matrix(current_matrix, TABLE_9)
        print(f"After Permutation (Round {round_num}):")
        format_to_matrix(current_matrix)

        cell_types = check_cell_type(current_matrix)
        print(f"Cell Types (After Permutation, Round {round_num}):")
        format_to_matrix(cell_types)

        # Step 4: Bit Inversion
        if round_num not in {2, 5, 6, 8}:
            current_matrix = invert_matrix_bits(current_matrix, [0, 1, 2, 4])
            print(f"After Bit Inversion (Round {round_num}):")
            format_to_matrix(current_matrix)

            cell_types = check_cell_type(current_matrix)
            print(f"Cell Types (After Bit Inversion, Round {round_num}):")
            format_to_matrix(cell_types)

# Input matrix
input_matrix = [
    [0, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [1, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [2, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [3, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [4, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [5, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [6, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [7, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [8, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [9, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [10, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [11, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [12, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [13, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [14, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9],
    [15, 2, 3, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 9]
]

# Apply PUFFIN for 4 rounds
apply_puffin(input_matrix, rounds=4)
