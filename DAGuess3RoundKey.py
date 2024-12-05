import random
from Puffin import key_schedule, sbox_substitution, apply_permutation, reverse_sbox_substitution, P64

def print_subkeys(subkeys):
    """
    Print all 33 subkeys in hexadecimal format.
    """
    print("\nGenerated Subkeys:")
    for i, subkey in enumerate(subkeys):
        print(f"K{i}: {hex(subkey)}")

def generate_random_plaintext_pair(delta_0):
    """Generate a random plaintext pair with a given XOR difference."""
    plaintext1 = random.getrandbits(64)
    plaintext2 = plaintext1 ^ delta_0
    return plaintext1, plaintext2

def compute_difference(block1, block2):
    """Compute the XOR difference between two blocks."""
    return block1 ^ block2

def guess_third_round_key(master_key, delta_0, num_pairs=100):
    """Perform a differential attack to guess the third-round key."""
    subkeys = key_schedule(master_key)  # Generate subkeys

    print("\n=== Differential Attack to Guess Third-Round Key ===")
    print(f"Master Key: {hex(master_key)}")
    print_subkeys(subkeys)

    # Step 1: Generate plaintext pairs with known difference
    plaintext_pairs = [generate_random_plaintext_pair(delta_0) for _ in range(num_pairs)]

    # Step 2: Encrypt for 3 rounds and record differences
    round_differences = []
    for plaintext1, plaintext2 in plaintext_pairs:
        block1, block2 = plaintext1, plaintext2

        # Apply 3 rounds of encryption
        for round_num in range(3):
            block1 = sbox_substitution(block1)
            block2 = sbox_substitution(block2)
            block1 ^= subkeys[round_num]
            block2 ^= subkeys[round_num]
            if round_num < 2:  # Apply permutation in the first 2 rounds
                block1 = apply_permutation(block1, P64)
                block2 = apply_permutation(block2, P64)

        # Record the round difference after 3 rounds
        round_diff = compute_difference(block1, block2)
        round_differences.append(round_diff)

    # Step 3: Guess the third-round key
    guessed_keys = []
    for candidate in range(2**64):  # Search over the full 64-bit key space
        valid_candidate = True
        for i, (plaintext1, plaintext2) in enumerate(plaintext_pairs):
            block1, block2 = plaintext1, plaintext2

            # Reverse encryption for the first 2 rounds
            for round_num in range(2):
                if round_num == 1:
                    block1 = apply_permutation(block1, P64)
                    block2 = apply_permutation(block2, P64)
                block1 ^= subkeys[round_num]
                block2 ^= subkeys[round_num]
                block1 = reverse_sbox_substitution(block1)
                block2 = reverse_sbox_substitution(block2)

            # Apply candidate key for round 3
            block1 ^= candidate
            block2 ^= candidate
            block1 = reverse_sbox_substitution(block1)
            block2 = reverse_sbox_substitution(block2)

            # Validate the difference
            if (block1 ^ block2) != delta_0:
                valid_candidate = False
                break

        if valid_candidate:
            guessed_keys.append(candidate)

    print("\n=== Key Guessing Results ===")
    if guessed_keys:
        print(f"Guessed Third-Round Key Candidates: {[hex(k) for k in guessed_keys]}")
    else:
        print("No valid third-round key candidates found.")
    print(f"Actual Third-Round Key: {hex(subkeys[2])}")

# Run the attack
if __name__ == "__main__":
    master_key = 0x0123456789ABCDEF  # Example master key
    delta_0 = 0x0000000F0000000F  # Example input difference
    guess_third_round_key(master_key, delta_0)
