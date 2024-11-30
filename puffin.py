# PUFFIN Cipher 

# Constants
S_BOX = [0xD, 0x7, 0x3, 0x2, 0x9, 0xA, 0xC, 0x1, 0xF, 0x4, 0x5, 0xE, 0x6, 0x0, 0xB, 0x8]
P64 = [
    13, 2, 60, 50, 51, 27, 10, 36, 25, 7, 32, 61, 1, 49, 47, 19,
    34, 53, 16, 22, 57, 20, 48, 41, 9, 52, 6, 31, 62, 30, 28, 11,
    37, 17, 58, 8, 33, 44, 46, 59, 24, 55, 63, 38, 56, 39, 15, 23,
    14, 4, 5, 26, 18, 54, 42, 45, 21, 35, 40, 3, 12, 29, 43, 64
]
P128 = [
    22, 121, 126, 110, 79, 81, 116, 55, 113, 21, 29, 20, 56, 76, 41, 112,
    45, 109, 95, 87, 94, 44, 68, 8, 115, 69, 6, 75, 83, 5, 54, 70,
    23, 61, 106, 103, 85, 124, 111, 52, 119, 32, 100, 17, 15, 34, 128, 91,
    58, 99, 120, 67, 31, 98, 53, 71, 92, 25, 38, 93, 65, 2, 37, 28,
    24, 82, 88, 14, 96, 118, 1, 9, 125, 27, 127, 18, 4, 10, 102, 7,
    35, 105, 48, 63, 30, 77, 72, 50, 108, 73, 12, 19, 107, 11, 26, 84,
    47, 97, 117, 49, 46, 33, 16, 42, 39, 57, 114, 62, 123, 101, 80, 13,
    51, 122, 64, 89, 43, 60, 40, 3, 86, 90, 59, 74, 78, 104, 36, 66
]

# Helper Functions
def apply_permutation(data, perm):
    """Apply a bit permutation."""
    result = 0
    for i, pos in enumerate(perm):
        if data & (1 << (pos - 1)):
            result |= (1 << i)
    return result

def sbox_substitution(data):
    substituted = 0
    for i in range(16):
        nibble = (data >> (4 * i)) & 0xF
        substituted |= S_BOX[nibble] << (4 * i)
    return substituted

def reverse_sbox_substitution(data):
    inverse_sbox = [S_BOX.index(i) for i in range(16)]
    reversed_data = 0
    for i in range(16):
        nibble = (data >> (4 * i)) & 0xF
        reversed_data |= inverse_sbox[nibble] << (4 * i)
    return reversed_data

def key_schedule(master_key, reverse=False):
    subkeys = []
    key = apply_permutation(master_key, P128)
    for round_num in range(32):
        if round_num % 4 != 1 and round_num % 4 != 4:
            key ^= (1 << 0) | (1 << 1) | (1 << 2) | (1 << 4)
        subkey = key & ((1 << 64) - 1)
        subkeys.append(subkey)
        key = apply_permutation(key, P128)
    return subkeys[::-1] if reverse else subkeys

def encryption(plaintext, master_key):
    subkeys = key_schedule(master_key)
    state = plaintext
    for round_num in range(32):
        state = sbox_substitution(state)
        state ^= subkeys[round_num]
        state = apply_permutation(state, P64)
    return state

def decryption(ciphertext, master_key):
    subkeys = key_schedule(master_key, reverse=True)
    state = ciphertext
    for round_num in range(32):
        state = apply_permutation(state, P64)
        state ^= subkeys[round_num]
        state = reverse_sbox_substitution(state)
    return state

# String and Number Handling
def string_to_int(text):
    # Ensure the string is long enough to fit into the 64-bit integer space
    byte_length = len(text.encode())
    return int.from_bytes(text.encode(), byteorder='big'), byte_length

def int_to_string(value, byte_length):
    return value.to_bytes(byte_length, byteorder='big').decode(errors='ignore')

# Updated Test Functionality
def test_puffin():
    plaintext = "PUFFIN"
    master_key = 0x0123456789ABCDEF0123456789ABCDEF

    # Convert string to integer for encryption and get its byte length
    plaintext_int, byte_length = string_to_int(plaintext)

    # Encrypt the plaintext
    ciphertext = encryption(plaintext_int, master_key)

    # Decrypt the ciphertext
    decrypted_int = decryption(ciphertext, master_key)

    # Convert decrypted integer back to string
    decrypted_text = int_to_string(decrypted_int, byte_length)

    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext (Hex): {hex(ciphertext)}")
    print(f"Decrypted Text: {decrypted_text}")

    
# Run the test
test_puffin()
