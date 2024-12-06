Plaintext: PUFFIN 1234
Ciphertext (Hex): b86b37c46150a3cb6e5b0287023cf4aa
Decrypted Text: PUFFIN 1234
Master Key: 0x123456789abcdef
Initial Difference (Delta_0): 0xf0000000f

Pair 1: P1 = 0xfc567fb808f53b9, P2 = 0xfc567f4808f53b6

--- Round 1 ---
After S-box: Difference = 0x700000008
Active S-boxes: [0, 8]
  S-box 0: Active bits = b3
  S-box 8: Active bits = b0, b1, b2
After Key XOR: Difference = 0x700000008
After Permutation: Difference = 0x202001000010000
Bit Propagation Mapping:
  From S-box 0:
    b2 -> S12(b2)
  From S-box 8:
    b1 -> S9(b1)
    b1 -> S4(b1)
    b2 -> S14(b2)

--- Round 2 ---
After S-box: Difference = 0xb0b003000060000
Active S-boxes: [4, 9, 12, 14]
  S-box 4: Active bits = b1, b2
  S-box 9: Active bits = b0, b1
  S-box 12: Active bits = b0, b1, b3
  S-box 14: Active bits = b0, b1, b3
After Key XOR: Difference = 0xb0b003000060000
After Permutation: Difference = 0x1008050210a00c
Bit Propagation Mapping:
  From S-box 4:
    b1 -> S13(b1)
    b0 -> S4(b0)
  From S-box 9:
    b1 -> S8(b1)
    b0 -> S11(b0)
  From S-box 12:
    b2 -> S3(b2)
    b0 -> S1(b0)
    b2 -> S6(b2)
  From S-box 14:
    b1 -> S5(b1)
    b3 -> S8(b3)
    b3 -> S0(b3)

--- Round 3 ---
After S-box: Difference = 0xb0030e0e30100f
Active S-boxes: [0, 3, 5, 6, 8, 10, 13]
  S-box 0: Active bits = b0, b1, b2, b3
  S-box 3: Active bits = b0
  S-box 5: Active bits = b0, b1
  S-box 6: Active bits = b1, b2, b3
  S-box 8: Active bits = b1, b2, b3
  S-box 10: Active bits = b0, b1
  S-box 13: Active bits = b0, b1, b3
After Key XOR: Difference = 0xb0030e0e30100f
After Permutation: Difference = 0xb6a1000408b10a3
Bit Propagation Mapping:
  From S-box 0:
    b1 -> S3(b1)
    b2 -> S0(b2)
    b0 -> S15(b0)
    b2 -> S12(b2)
  From S-box 3:
    b1 -> S0(b1)
  From S-box 5:
    b1 -> S14(b1)
    b0 -> S5(b0)
  From S-box 6:
    b0 -> S13(b0)
    b2 -> S1(b2)
    b3 -> S7(b3)
  From S-box 8:
    b1 -> S4(b1)
    b2 -> S14(b2)
    b0 -> S2(b0)
  From S-box 10:
    b0 -> S6(b0)
    b3 -> S13(b3)
  From S-box 13:
    b2 -> S4(b2)
    b2 -> S13(b2)
    b1 -> S11(b1)

--- Round 4 ---
After S-box: Difference = 0x1e8a00040323018
Active S-boxes: [0, 1, 3, 4, 5, 7, 11, 12, 13, 14]
  S-box 0: Active bits = b3
  S-box 1: Active bits = b0
  S-box 3: Active bits = b0, b1
  S-box 4: Active bits = b1
  S-box 5: Active bits = b0, b1
  S-box 7: Active bits = b2
  S-box 11: Active bits = b1, b3
  S-box 12: Active bits = b3
  S-box 13: Active bits = b1, b2, b3
  S-box 14: Active bits = b0
After Key XOR: Difference = 0x1e8a00040323018

=== Differential Attack Complete ===
