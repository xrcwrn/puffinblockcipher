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
    """Apply P64 permutation."""
    result = 0
    for i, pos in enumerate(perm):
        if data & (1 << (pos - 1)):
            result |= (1 << i)
    return result

def sbox_substitution(data):
    """Apply S-box substitution."""
    substituted = 0
    for i in range(16):  # 64 bits = 16 × 4-bit nibbles
        nibble = (data >> (4 * i)) & 0xF
        substituted |= S_BOX[nibble] << (4 * i)
    return substituted

def reverse_sbox_substitution(data):
    """Reverse the S-box substitution."""
    inverse_sbox = [S_BOX.index(i) for i in range(16)]
    reversed_data = 0
    for i in range(16):
        nibble = (data >> (4 * i)) & 0xF
        reversed_data |= inverse_sbox[nibble] << (4 * i)
    return reversed_data

def key_schedule(master_key):
    """Generate keys for 4 rounds."""
    subkeys = []
    for round_num in range(4):
        subkeys.append((master_key >> (16 * round_num)) & 0xFFFFFFFFFFFFFFFF)
    return subkeys

def differential_attack(master_key, delta_0, num_pairs=100):
    """Perform the differential attack and guess the third round key."""
    # Generate subkeys
    subkeys = key_schedule(master_key)
    print("\n=== Differential Attack ===")
    print(f"Master Key: {hex(master_key)}")
    print(f"Subkeys (First 4 Rounds): {[hex(k) for k in subkeys]}")

    # Step 1: Generate plaintext pairs
    plaintext_pairs = [
        generate_random_plaintext_pair(delta_0) for _ in range(num_pairs)
    ]

    # Step 2: Perform encryption for 3 rounds
    round_differences = []
    for plaintext1, plaintext2 in plaintext_pairs:
        block1, block2 = plaintext1, plaintext2
        for round_num in range(3):
            # S-box substitution
            block1 = sbox_substitution(block1)
            block2 = sbox_substitution(block2)

            # XOR with round key
            block1 ^= subkeys[round_num]
            block2 ^= subkeys[round_num]

            # Permutation
            if round_num < 2:  # No permutation in the last round
                block1 = apply_permutation(block1, P64)
                block2 = apply_permutation(block2, P64)

        # Compute the XOR difference at the end of 3 rounds
        round_diff = block1 ^ block2
        round_differences.append(round_diff)

    # Step 3: Guess third round key
    guessed_key_candidates = []
    for candidate in range(2**16):  # Limit to 16-bit key guesses for feasibility
        success = True
        for i, (plaintext1, plaintext2) in enumerate(plaintext_pairs):
            # Reverse partial encryption for round 3
            block1, block2 = plaintext1, plaintext2

            # Encrypt for 2 rounds
            for round_num in range(2):
                block1 = sbox_substitution(block1)
                block2 = sbox_substitution(block2)

                block1 ^= subkeys[round_num]
                block2 ^= subkeys[round_num]

                if round_num == 0:
                    block1 = apply_permutation(block1, P64)
                    block2 = apply_permutation(block2, P64)

            # Apply candidate key for round 3
            block1 ^= candidate
            block2 ^= candidate

            # Check if the difference matches
            if (block1 ^ block2) != round_differences[i]:
                success = False
                break

        if success:
            guessed_key_candidates.append(candidate)

    # Step 4: Output results
    print("\n=== Key Guessing Results ===")
    print(f"Guessed Third Round Key Candidates: {[hex(k) for k in guessed_key_candidates]}")
    print(f"Actual Third Round Key: {hex(subkeys[2])}")

# Helper Functions
def generate_random_plaintext_pair(delta_0):
    """Generate a random plaintext pair with a given XOR difference."""
    plaintext1 = random.getrandbits(64)
    plaintext2 = plaintext1 ^ delta_0
    return plaintext1, plaintext2

# Run the attack
master_key = 0x012a113456789DEF  # Example master key
delta_0 = 0x0000000F0000000F  # Example input difference
differential_attack(master_key, delta_0)

