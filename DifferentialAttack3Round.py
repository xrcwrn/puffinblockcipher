import random

# Constants
S_BOX = [0xD, 0x7, 0x3, 0x2, 0x9, 0xA, 0xC, 0x1, 0xF, 0x4, 0x5, 0xE, 0x6, 0x0, 0xB, 0x8]
P64 = [
    13, 2, 60, 50, 51, 27, 10, 36, 25, 7, 32, 61, 1, 49, 47, 19,
    34, 53, 16, 22, 57, 20, 48, 41, 9, 52, 6, 31, 62, 30, 28, 11,
    37, 17, 58, 8, 33, 44, 46, 59, 24, 55, 63, 38, 56, 39, 15, 23,
    14, 4, 5, 26, 18, 54, 42, 45, 21, 35, 40, 3, 12, 29, 43, 64
]

# Functions
def apply_permutation(data, perm):
    """Apply a bit-level permutation based on P64."""
    result = 0
    for i, pos in enumerate(perm):
        if data & (1 << (pos - 1)):
            result |= (1 << i)
    return result

def sbox_substitution(data):
    """Apply S-box substitution to all 16 nibbles of the 64-bit block."""
    substituted = 0
    for i in range(16):  # 64 bits = 16 × 4-bit nibbles
        nibble = (data >> (4 * i)) & 0xF
        substituted |= S_BOX[nibble] << (4 * i)
    return substituted

def key_schedule(master_key):
    """Generate 3 round keys from the master key."""
    subkeys = []
    for round_num in range(4):  # 3 rounds + initial key
        subkeys.append((master_key >> (16 * round_num)) & 0xFFFFFFFFFFFFFFFF)
    return subkeys

def generate_random_plaintext_pair(delta_0):
    """Generate two plaintexts with a fixed XOR difference."""
    plaintext1 = random.getrandbits(64)
    plaintext2 = plaintext1 ^ delta_0
    return plaintext1, plaintext2

def compute_difference(block1, block2):
    """Compute the XOR difference between two blocks."""
    return block1 ^ block2

# Differential Attack
def differential_attack(master_key, delta_0, num_pairs=100):
    # Generate subkeys
    subkeys = key_schedule(master_key)

    print("\n=== Differential Attack ===")
    print(f"Master Key: {hex(master_key)}")
    print(f"Initial Difference (Delta_0): {hex(delta_0)}")

    for pair_idx in range(num_pairs):
        # Generate plaintext pair
        plaintext1, plaintext2 = generate_random_plaintext_pair(delta_0)
        print(f"\nPair {pair_idx + 1}:")
        print(f"P1: {hex(plaintext1)}, P2: {hex(plaintext2)}")

        # Encryption process for 3 rounds
        block1, block2 = plaintext1, plaintext2
        for round_num in range(3):
            print(f"\n--- Round {round_num + 1} ---")

            # Substitution
            block1 = sbox_substitution(block1)
            block2 = sbox_substitution(block2)
            print(f"After S-box: B1 = {hex(block1)}, B2 = {hex(block2)}")

            # XOR with round key
            block1 ^= subkeys[round_num]
            block2 ^= subkeys[round_num]
            print(f"After Key XOR: B1 = {hex(block1)}, B2 = {hex(block2)}")

            # Permutation
            block1 = apply_permutation(block1, P64)
            block2 = apply_permutation(block2, P64)
            print(f"After Permutation: B1 = {hex(block1)}, B2 = {hex(block2)}")

            # Compute round difference
            round_diff = compute_difference(block1, block2)
            print(f"Round {round_num + 1} Difference: {hex(round_diff)}")

            # Identify active S-boxes
            active_sboxes = []
            for i in range(16):  # Check all 16 nibbles
                nibble1 = (block1 >> (4 * i)) & 0xF
                nibble2 = (block2 >> (4 * i)) & 0xF
                if nibble1 != nibble2:
                    active_sboxes.append(i + 1)
            print(f"Active S-boxes in Round {round_num + 1}: {active_sboxes}")

    print("\n=== Differential Attack Complete ===")

# Run the attack
master_key = 0x0123456789ABCDEF  # Example master key
delta_0 = 0x0000000F0000000F  # Example input difference
differential_attack(master_key, delta_0)
