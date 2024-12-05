import random
from Puffin import encrypt, decrypt, key_schedule, sbox_substitution, apply_permutation, P64  # Import from Puffin.py

def generate_random_plaintext_pair(delta_0):
    """Generate a random plaintext pair with a given XOR difference."""
    plaintext1 = random.getrandbits(64)
    plaintext2 = plaintext1 ^ delta_0
    return plaintext1, plaintext2

def compute_difference(block1, block2):
    """Compute the XOR difference between two blocks."""
    return block1 ^ block2

def differential_attack(master_key, delta_0, num_pairs=10):
    """Perform a 3-round differential attack using functions from Puffin.py."""
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
            if round_num < 2:  # Permutation is skipped in the last round
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
if __name__ == "__main__":
    master_key = 0x0123456789ABCDEF  # Example master key
    delta_0 = 0x0000000F0000000F  # Example input difference
    differential_attack(master_key, delta_0)
