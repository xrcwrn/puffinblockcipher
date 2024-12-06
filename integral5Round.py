from Puffin import key_schedule, sbox_substitution, apply_permutation, reverse_sbox_substitution, P64


def generate_plaintexts(fixed_byte, varying_position, num_texts=256):
    """Generate a set of plaintexts where one byte varies and others are fixed."""
    plaintexts = []
    for i in range(num_texts):
        pt = bytearray([fixed_byte] * 8)  # Start with all fixed bytes
        pt[varying_position] = i  # Vary one byte
        plaintexts.append(bytes(pt))
    return plaintexts

def integral_attack(master_key):
    """Perform a 5-round integral attack on the PUFFIN cipher."""
    fixed_byte = 0xAA  # Arbitrary fixed value
    varying_position = 0  # Vary the first byte
    plaintexts = generate_plaintexts(fixed_byte, varying_position)

    # Encrypt all plaintexts
    subkeys = key_schedule(master_key)
    intermediate_states = []
    for pt in plaintexts:
        block = int.from_bytes(pt, byteorder="big")
        state = block
        state ^= subkeys[0]  # Initial key addition
        for round_num in range(4):  # Encrypt for 4 rounds
            state = sbox_substitution(state)
            state ^= subkeys[round_num + 1]
            state = apply_permutation(state, P64)
        intermediate_states.append(state)  # Collect states after 4 rounds

    # Analyze patterns in intermediate states
    xor_results = [0] * 8
    for state in intermediate_states:
        for i in range(8):
            byte = (state >> (8 * i)) & 0xFF
            xor_results[i] ^= byte

    # Print XOR results to identify balanced bytes
    print(f"XOR Results After 4 Rounds: {xor_results}")

    # Attempt to recover 5th round key
    potential_keys = []
    for guess_key in range(256):  # Brute-force 8 bits of key
        xor_test = 0
        for state in intermediate_states:
            test_state = state ^ (guess_key << 56)  # Apply guessed key to most significant byte
            test_state = reverse_sbox_substitution(test_state)  # Reverse substitution
            byte = (test_state >> 56) & 0xFF
            xor_test ^= byte
        if xor_test == 0:  # Balanced byte confirms key guess
            potential_keys.append(guess_key)

    print(f"Potential 5th Round Key Candidates: {potential_keys}")

# Test the attack
if __name__ == "__main__":
    master_key = 0x0123456789ABCDEF0123456789ABCDEF
    integral_attack(master_key)
