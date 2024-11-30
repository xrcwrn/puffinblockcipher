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

# Updated Encryption and Decryption Functions
def encrypt(data, master_key):
    subkeys = key_schedule(master_key)
    encrypted_data = []

    # Process data in 64-bit (8-byte) blocks
    for i in range(0, len(data), 8):
        block = data[i:i + 8]
        block_int = int.from_bytes(block.ljust(8, b'\x00'), byteorder='big')  # Pad if block is incomplete
        encrypted_block = block_int
        for round_num in range(32):
            encrypted_block = sbox_substitution(encrypted_block)
            encrypted_block ^= subkeys[round_num]
            encrypted_block = apply_permutation(encrypted_block, P64)
        encrypted_data.append(encrypted_block.to_bytes(8, byteorder='big'))
    return b''.join(encrypted_data)

def decrypt(data, master_key):
    subkeys = key_schedule(master_key, reverse=True)
    decrypted_data = bytearray()

    # Process data in 64-bit (8-byte) blocks
    for i in range(0, len(data), 8):
        block = data[i:i + 8]
        block_int = int.from_bytes(block, byteorder='big')
        decrypted_block = block_int
        for round_num in range(32):
            decrypted_block = apply_permutation(decrypted_block, P64)
            decrypted_block ^= subkeys[round_num]
            decrypted_block = reverse_sbox_substitution(decrypted_block)
        decrypted_data.extend(decrypted_block.to_bytes(8, byteorder='big'))
    return decrypted_data.rstrip(b'\x00')  # Remove padding

# Updated Test Functionality 
def test_puffin():
    plaintext = "PUFFIN 1234"
    master_key = 0x0123456789ABCDEF0123456789ABCDEF

    # Convert string to bytes
    plaintext_bytes = plaintext.encode()

    # Encrypt the plaintext
    ciphertext_bytes = encrypt(plaintext_bytes, master_key)

    # Decrypt the ciphertext
    decrypted_bytes = decrypt(ciphertext_bytes, master_key)

    # Convert decrypted bytes back to string
    decrypted_text = decrypted_bytes.decode()

    print(f"Plaintext: {plaintext}")
    print(f"Ciphertext (Hex): {ciphertext_bytes.hex()}")
    print(f"Decrypted Text: {decrypted_text}")

# Run the test
test_puffin()
