import numpy as np
from itertools import product

# Define the S-Box (PUFFIN S-Box or example values)
SBOX = [
    0x3, 0xF, 0xE, 0x1, 0x0, 0xA, 0x7, 0x4,
    0xC, 0x5, 0x6, 0xB, 0x9, 0xD, 0x2, 0x8
]

# Inverse S-Box
INV_SBOX = [SBOX.index(i) for i in range(len(SBOX))]

# Define PUFFIN tables
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

# Helper functions
def sbox_substitution(matrix):
    """Apply S-Box substitution to each element."""
    return np.vectorize(lambda x: SBOX[x & 0xF])(matrix)

def inverse_sbox_substitution(matrix):
    """Reverse the S-Box substitution."""
    return np.vectorize(lambda x: INV_SBOX[x & 0xF])(matrix)

def permute_matrix(matrix, table):
    """Permute the matrix using TABLE_9."""
    flattened = matrix.flatten()
    permuted = np.zeros_like(flattened)
    for i, row in enumerate(table):
        for j, bit_position in enumerate(row):
            if bit_position < len(flattened):
                permuted[i * len(row) + j] = flattened[bit_position]
    return permuted.reshape(matrix.shape)

def inverse_permute_matrix(matrix, table):
    """Apply the inverse permutation to the matrix using TABLE_9."""
    flattened = matrix.flatten()
    inverse_permuted = np.zeros_like(flattened)
    for i, row in enumerate(table):
        for j, bit_position in enumerate(row):
            if bit_position < len(flattened):
                inverse_permuted[bit_position] = flattened[i * len(row) + j]
    return inverse_permuted.reshape(matrix.shape)

def format_to_matrix(matrix):
    """Print the matrix in a readable format."""
    for row in matrix:
        print("  ".join(f"{x:02X}" for x in row))

# Main PUFFIN encryption
def apply_puffin(input_matrix, rounds=4):
    """Encrypt the input matrix using the PUFFIN algorithm."""
    current_matrix = np.array(input_matrix, dtype=np.uint8)  # Ensure uint8 for bitwise operations

    for round_num in range(1, rounds + 1):
        # Step 1: S-Box Substitution
        current_matrix = sbox_substitution(current_matrix)

        # Step 2: Subkey XOR (using a dummy key, replace with actual key schedule if needed)
        subkey_array = np.full(current_matrix.shape, 0x0F, dtype=np.uint8)  # Example subkey
        current_matrix = np.bitwise_xor(current_matrix, subkey_array)

        # Step 3: Permutation
        current_matrix = permute_matrix(current_matrix, TABLE_9)

    return current_matrix


def integral_attack(input_matrix, rounds=4):
    """Implement the integral attack on the PUFFIN cipher."""
    current_matrix = np.array(input_matrix, dtype=np.uint8)

    # Step 1: Encrypt the matrix with 4 rounds
    print("Encrypting input matrix for 4 rounds...")
    round4cipher = apply_puffin(current_matrix, rounds=rounds)

    print("\nRound 4 Cipher:")
    format_to_matrix(round4cipher)

    # Step 2: Apply inverse permutation of Round 4 (perinv4)
    perinv4 = inverse_permute_matrix(round4cipher, TABLE_9)
    print("\nAfter Inverse Permutation (Round 4) - perinv4:")
    format_to_matrix(perinv4)

    # Step 3: Guess keys for bits 8, 9, 10, 11 (xxxx in 0b00000000xxxx0000)
    print("\nGuessing keys for bits 8, 9, 10, 11...")
    valid_keys = []
    for key_bits in product([0, 1], repeat=4):
        # Construct the 16-bit key with xxxx placed in bits 8-11
        guessed_key = sum((bit << (11 - i)) for i, bit in enumerate(key_bits))  # Place xxxx in positions 8-11
        guessed_key <<= 4  # Align to the format 0b00000000xxxx0000

        # XOR guessed key with perinv4 (keyinv4)
        key_array = np.full(perinv4.shape, guessed_key, dtype=np.uint16)  # Ensure 16-bit keys
        keyinv4 = np.bitwise_xor(perinv4, key_array)
        print(f"\nGuessed Key: {guessed_key:016b} - After XOR (keyinv4):")
        format_to_matrix(keyinv4)

        # Step 4: Apply inverse S-Box to keyinv4 (sboxinv4)
        sboxinv4 = inverse_sbox_substitution(keyinv4)
        print(f"\nAfter Inverse S-Box (sboxinv4):")
        format_to_matrix(sboxinv4)

        # Step 5: Apply inverse permutation on sboxinv4 (Round 3)
        round3inv = inverse_permute_matrix(sboxinv4, TABLE_9)
        print(f"\nAfter Inverse Permutation (Round 3):")
        format_to_matrix(round3inv)

        # Step 6: XOR values at position 2 of each row in sboxinv4
        xor_value = 0
        for row in sboxinv4:
            xor_value ^= row[2]

        print(f"XOR of Position 2: {xor_value:#04X}")

        # Check if XOR value is balanced (equals 0)
        if xor_value == 0:
            print(f"Balanced property satisfied for guessed key: {guessed_key:016b}")
            valid_keys.append(guessed_key)

    # Step 7: Print valid keys
    if valid_keys:
        print("\nValid Keys Found:")
        for key in valid_keys:
            print(f"k2 = {key:016b}")
    else:
        print("\nNo valid keys found.")

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

# Perform the attack
integral_attack(input_matrix, rounds=4)
