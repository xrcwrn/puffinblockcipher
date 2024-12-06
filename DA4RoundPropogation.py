import random
from Puffin import encrypt, decrypt, key_schedule, sbox_substitution, apply_permutation, P64

def generate_random_plaintext_pair(delta_0):
    """Generate a random plaintext pair with a given XOR difference."""
    plaintext1 = random.getrandbits(64)
    plaintext2 = plaintext1 ^ delta_0
    return plaintext1, plaintext2

def compute_difference(block1, block2):
    """Compute the XOR difference between two blocks."""
    return block1 ^ block2

def identify_active_bits(nibble1, nibble2):
    """Identify which bits are active (different) between two nibbles."""
    active_bits = []
    diff = nibble1 ^ nibble2
    for bit_position in range(4):  # 4 bits in a nibble
        if (diff >> bit_position) & 1:
            active_bits.append(bit_position)  # Return bit indices as integers
    return active_bits

def trace_bit_propagation(input_diff, permutation):
    """
    Trace how bits propagate through the permutation layer.
    Returns a mapping from input S-box/bit to output S-box/bit.
    """
    propagation_map = {i: [] for i in range(16)}  # Map for 16 S-boxes
    for bit in range(64):
        if (input_diff >> bit) & 1:  # If the bit is active
            target_bit = permutation[bit]  # Get the target bit from the permutation
            input_sbox = bit // 4       # Determine input S-box (0-indexed)
            output_sbox = target_bit // 4  # Determine output S-box (0-indexed)
            input_bit = bit % 4         # Determine bit index within the input S-box
            output_bit = target_bit % 4 # Determine bit index within the output S-box
            propagation_map[input_sbox].append((output_sbox, output_bit))
    return propagation_map

def differential_attack(master_key, delta_0, num_pairs=1):
    """Perform a 4-round differential attack with bit tracking."""
    subkeys = key_schedule(master_key)
    print(f"Master Key: {hex(master_key)}")
    print(f"Initial Difference (Delta_0): {hex(delta_0)}")

    for pair_idx in range(num_pairs):
        plaintext1, plaintext2 = generate_random_plaintext_pair(delta_0)
        print(f"\nPair {pair_idx + 1}: P1 = {hex(plaintext1)}, P2 = {hex(plaintext2)}")

        block1, block2 = plaintext1, plaintext2
        for round_num in range(4):  # Four rounds
            print(f"\n--- Round {round_num + 1} ---")

            # Substitution
            block1 = sbox_substitution(block1)
            block2 = sbox_substitution(block2)
            sbox_diff = compute_difference(block1, block2)

            print(f"After S-box: Difference = {hex(sbox_diff)}")

            # Track active S-boxes and bits
            active_sboxes = []
            sbox_bit_activations = {}
            for i in range(16):  # 16 S-boxes
                nibble1 = (block1 >> (4 * i)) & 0xF
                nibble2 = (block2 >> (4 * i)) & 0xF
                if nibble1 != nibble2:
                    active_sboxes.append(i)
                    active_bits = identify_active_bits(nibble1, nibble2)
                    sbox_bit_activations[i] = active_bits

            print(f"Active S-boxes: {active_sboxes}")
            for sbox, bits in sbox_bit_activations.items():
                active_bits_str = ", ".join([f"b{bit}" for bit in bits])
                print(f"  S-box {sbox}: Active bits = {active_bits_str}")

            # XOR with round key
            block1 ^= subkeys[round_num]
            block2 ^= subkeys[round_num]
            print(f"After Key XOR: Difference = {hex(compute_difference(block1, block2))}")

            # Permutation
            if round_num < 3:  # Skip permutation in the last round
                propagation_map = trace_bit_propagation(
                    compute_difference(block1, block2),
                    P64,
                )
                block1 = apply_permutation(block1, P64)
                block2 = apply_permutation(block2, P64)
                print(f"After Permutation: Difference = {hex(compute_difference(block1, block2))}")

                # Print bit propagation
                print("Bit Propagation Mapping:")
                for inp_sbox, mappings in propagation_map.items():
                    if mappings:  # Only print if there is active propagation
                        print(f"  From S-box {inp_sbox}:")
                        for out_sbox, out_bit in mappings:
                            print(f"    b{out_bit} -> S{out_sbox}(b{out_bit})")

    print("\n=== Differential Attack Complete ===")

# Main Execution
if __name__ == "__main__":
    master_key = 0x0123456789ABCDEF  # Example master key
    delta_0 = 0x0000000F0000000F  # Example input difference
    differential_attack(master_key, delta_0)
