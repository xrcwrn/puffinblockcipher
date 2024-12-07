import random
from Puffin import key_schedule, sbox_substitution, reverse_sbox_substitution, apply_permutation

def validate_permutation_table(permutation_table):
    """
    Validate and adjust the permutation table to exclude invalid entries.
    Args:
        permutation_table (list): Permutation table to validate.
    Returns:
        list: Validated permutation table.
    """
    valid_table = [idx for idx in permutation_table if 0 <= idx < 64]
    if len(valid_table) != len(permutation_table):
        print(f"Invalid entries in permutation table have been excluded: {permutation_table}")
    return valid_table

def inverse_permutation(block, permutation_table):
    """
    Perform the inverse permutation on a 64-bit block using the given permutation table.
    Args:
        block (int): 64-bit block to permute.
        permutation_table (list): Permutation table.
    Returns:
        int: Permuted block.
    """
    permutation_table = validate_permutation_table(permutation_table)

    inverse_table = [0] * 64
    for i, perm in enumerate(permutation_table):
        inverse_table[perm] = i  # Build the inverse permutation table

    result = 0
    for i in range(64):
        if (block >> i) & 1:  # If the bit at position i is set
            result |= (1 << inverse_table[i])  # Set the corresponding bit in the result
    return result

def generate_random_plaintext_pair(delta_0):
    """Generate a random plaintext pair with a given XOR difference."""
    plaintext1 = random.getrandbits(64)
    plaintext2 = plaintext1 ^ delta_0
    return plaintext1, plaintext2

def compute_difference(block1, block2):
    """Compute the XOR difference between two blocks."""
    return block1 ^ block2

def differential_attack(master_key, delta_0, num_pairs=1000, key_range=(0, 2**16)):
    """
    Perform a differential attack focusing on the last 4 bits at round 4.
    Guesses keys in the specified key_range.
    """
    # Ensure P64 is valid
    from Puffin import P64
    P64 = validate_permutation_table(P64)

    subkeys = key_schedule(master_key)
    print(f"Master Key: {hex(master_key)}")
    print(f"Initial Difference (Delta_0): {hex(delta_0)}")

    # Step 1: Generate plaintext pairs and compute differences
    round4_differences = []
    round3_expected_differences = []
    for _ in range(num_pairs):
        plaintext1, plaintext2 = generate_random_plaintext_pair(delta_0)

        # Encrypt plaintexts through 4 rounds
        block1, block2 = plaintext1, plaintext2
        for round_num in range(4):
            # Substitution
            block1 = sbox_substitution(block1)
            block2 = sbox_substitution(block2)

            # Key addition
            block1 ^= subkeys[round_num]
            block2 ^= subkeys[round_num]

            # Permutation (skip in last round)
            if round_num < 3:
                block1 = apply_permutation(block1, P64)
                block2 = apply_permutation(block2, P64)

        # Store round 4 difference and the expected difference for level 3
        round4_diff = compute_difference(block1, block2)
        round4_differences.append(round4_diff)
        # Save the last 4 bits of the expected difference for level 3
        round3_expected_differences.append((round4_diff & 0xF))  # Extract last 4 bits

    # Step 2: Key Guessing
    print(f"Testing keys in range: {key_range}")
    for guessed_key in range(*key_range):  # Iterate over specified key range
        print(f"\nTesting Key Guess: {bin(guessed_key)}")

        # Step 3: Inverse operations for each pair
        for pair_idx in range(num_pairs):
            round4_diff = round4_differences[pair_idx]
            expected_diff = round3_expected_differences[pair_idx]

            # Extract last 4 bits from round 4 difference
            round4_last4 = round4_diff & 0xF

            # Inverse operations to move to round 3
            round3_level = inverse_permutation(round4_last4, P64)  # Inverse permutation
            round3_level ^= guessed_key  # XOR with guessed key
            round3_level = reverse_sbox_substitution(round3_level)  # Inverse S-Box

            # Compute difference at level 3 (last 4 bits)
            computed_diff = round3_level & 0xF

            # Match with expected difference
            if computed_diff == expected_diff:
                print(f"Matched Key: {bin(guessed_key)}")
                return guessed_key  # Stop after finding the first valid key

    print("\nNo matching keys found in the specified range.")
    return None

# Main Execution
if __name__ == "__main__":
    master_key = 0x0123456789ABCDEF  # Example master key
    delta_0 = 0xF000000000000000  # Example input difference
    key_range = (0, 2**16)  # Adjust range for practical computation (16-bit range)
    found_key = differential_attack(master_key, delta_0, key_range=key_range)

    if found_key is not None:
        print(f"\n=== Found Key: {bin(found_key)} ===")
    else:
        print("\n=== No Key Found ===")
