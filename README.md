# PUFFIN Block Cipher
PUFFIN is a lightweight block cipher designed for efficient encryption and decryption operations, particularly in resource-constrained environments like embedded systems, IoT devices, and smart cards. Below is a summary of its key features and properties:

### Key Features
Block Size: 64 bits
Key Size: 128 bits
Rounds: 32 rounds (encryption and decryption)
Structure: Substitution-Permutation Network (SPN)
Design Goals: Security, efficiency, and suitability for lightweight applications





## PUFFIN block diagram
<img src="https://github.com/user-attachments/assets/8a4e30ef-d721-41dd-83d8-fd38d5dd4ce7" width="500">

 ## S-box Mapping (in Hexadecimal)
![image](https://github.com/user-attachments/assets/594937c9-aac0-4489-8321-ae2f83298823)


## Difference Distribution Table (DDT) 
```
from sage.crypto.sbox import SBox
S = SBox(13,7, 3, 2, 9, 10, 12, 1, 15, 4, 5, 14, 6, 0, 11, 8)
S.difference_distribution_table()
```

<img src="https://github.com/user-attachments/assets/4c8eeed9-1513-4c16-a054-af003a94d46d" width="500">

## Differential Branch Number
```
from sage.crypto.sbox import SBox
S = SBox(13,7, 3, 2, 9, 10, 12, 1, 15, 4, 5, 14, 6, 0, 11, 8)
S.differential_branch_number()
```


The differential Branch Number of PUFFIN is 2

## Differential Uniformity
```
from sage.crypto.sbox import SBox
S = SBox(13,7, 3, 2, 9, 10, 12, 1, 15, 4, 5, 14, 6, 0, 11, 8)
S.maximal_difference_probability_absolute()
```
The Differential Uniformity is 4

 ## Linear Approximation Table (LAT)
 ```
from sage.crypto.sbox import SBox
S = SBox(13,7, 3, 2, 9, 10, 12, 1, 15, 4, 5, 14, 6, 0, 11, 8)
S.linear_approximation_table()

```
<img src="https://github.com/user-attachments/assets/8915a7f1-333c-4a82-bbb9-af686e6904e9" width="500">

## Differential attack
```
=== Differential Attack ===
Master Key: 0x123456789abcdef
Initial Difference (Delta_0): 0xf0000000f

Pair 1:
P1: 0x155215efaaad7358, P2: 0x155215e0aaad7357

--- Round 1 ---
After S-box: B1 = 0x7aa37ab8555012af, B2 = 0x7aa37abd555012a1, Difference = 0x50000000e
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b1, b2, b3
  S-box 9: Active bits = b0, b2
After Key XOR: B1 = 0xdca340b811d05ab9, B2 = 0xdca340bd11d05ab7
After Permutation: B1 = 0xb526dd89040079cd, B2 = 0xbf24dd99040079cf
Round 1 Difference: 0xa02001000000002

--- Round 2 ---
After S-box: B1 = 0xea3c00f4d9dd1460, B2 = 0xe8390044d9dd1468, Difference = 0x20500b000000008
Active S-boxes in Round 2 After S-box: [1, 10, 13, 15]
  S-box 1: Active bits = b3
  S-box 10: Active bits = b0, b1, b3
  S-box 13: Active bits = b0, b2
  S-box 15: Active bits = b1
After Key XOR: B1 = 0xdaa994f8f9ec3440, B2 = 0xd8ac9448f9ec3448
After Permutation: B1 = 0xe4a1bd05ea68af85, B2 = 0xe0a3b500ea688f95
Round 2 Difference: 0x402080500002010

--- Round 3 ---
After S-box: B1 = 0xb957e0dab5cf58fa, B2 = 0xbd52eaddb5cff84a, Difference = 0x4050a070000a0b0
Active S-boxes in Round 3 After S-box: [2, 4, 9, 11, 13, 15]
  S-box 2: Active bits = b0, b1, b3
  S-box 4: Active bits = b1, b3
  S-box 9: Active bits = b0, b1, b2
  S-box 11: Active bits = b1, b3
  S-box 13: Active bits = b0, b2
  S-box 15: Active bits = b2
After Key XOR: B1 = 0xa9396898b0c64afc, B2 = 0xad3c629fb0c6ea4c
After Permutation: B1 = 0xbc36c1693612e6c4, B2 = 0xbe73c1d13217c6d4
Round 3 Difference: 0x24500b804052010

--- Round 4 ---
After S-box: B1 = 0xe62c67c42c73bc69, B2 = 0xeb12670723716c09, Difference = 0xd3e00c30f02d060
Active S-boxes in Round 4 After S-box: [2, 4, 5, 7, 9, 10, 13, 14, 15]
  S-box 2: Active bits = b1, b2
  S-box 4: Active bits = b0, b2, b3
  S-box 5: Active bits = b1
  S-box 7: Active bits = b0, b1, b2, b3
  S-box 9: Active bits = b0, b1
  S-box 10: Active bits = b2, b3
  S-box 13: Active bits = b1, b2, b3
  S-box 14: Active bits = b0, b1
  S-box 15: Active bits = b0, b2, b3
After Key XOR: B1 = 0xc42c4b767c11b5d0, B2 = 0xc9124bb5731365b0
Round 4 Difference: 0xd3e00c30f02d060

Pair 2:
P1: 0xd19e933ccb241d96, P2: 0xd19e9333cb241d99

--- Round 1 ---
After S-box: B1 = 0x74b42266e39704c, B2 = 0x74b42226e397044, Difference = 0x400000008
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b3
  S-box 9: Active bits = b2
After Key XOR: B1 = 0xa14b78262ab9385a, B2 = 0xa14b78222ab93852
After Permutation: B1 = 0x938f0b627239620b, B2 = 0x918d0b627239620b
Round 1 Difference: 0x202000000000000

--- Round 2 ---
After S-box: B1 = 0x42f8dec31324c3de, B2 = 0x47f0dec31324c3de, Difference = 0x508000000000000
Active S-boxes in Round 2 After S-box: [13, 15]
  S-box 13: Active bits = b3
  S-box 15: Active bits = b0, b2
After Key XOR: B1 = 0x726d4acf3315e3fe, B2 = 0x77654acf3315e3fe
After Permutation: B1 = 0x2f6f663e3705ebd2, B2 = 0x2f6f66be3515ebd2
Round 2 Difference: 0x8002100000

--- Round 3 ---
After S-box: B1 = 0x38c8cc2b21dabe03, B2 = 0x38c8cceb2a7abe03, Difference = 0xc00ba00000
Active S-boxes in Round 3 After S-box: [6, 7, 10]
  S-box 6: Active bits = b1, b3
  S-box 7: Active bits = b0, b1, b3
  S-box 10: Active bits = b2, b3
After Key XOR: B1 = 0x28a6446924d3ac05, B2 = 0x28a644a92f73ac05
After Permutation: B1 = 0x5931b912b00450bc, B2 = 0x5d399812f00c51bc
Round 3 Difference: 0x408210040080100

--- Round 4 ---
After S-box: B1 = 0xa427e473edd9ade6, B2 = 0xa0244f738dd6a7e6, Difference = 0x403ab00600f0a00
Active S-boxes in Round 4 After S-box: [3, 5, 8, 11, 12, 13, 15]
  S-box 3: Active bits = b1, b3
  S-box 5: Active bits = b0, b1, b2, b3
  S-box 8: Active bits = b1, b2
  S-box 11: Active bits = b0, b1, b3
  S-box 12: Active bits = b1, b3
  S-box 13: Active bits = b0, b1
  S-box 15: Active bits = b2
After Key XOR: B1 = 0x8627c8c1bdbba45f, B2 = 0x822463c1ddb4ae5f
Round 4 Difference: 0x403ab00600f0a00

Pair 3:
P1: 0x73a9afb79fe3833d, P2: 0x73a9afb89fe38332

--- Round 1 ---
After S-box: B1 = 0x125458e148b2f220, B2 = 0x125458ef48b2f223, Difference = 0xe00000003
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b0, b1
  S-box 9: Active bits = b1, b2, b3
After Key XOR: B1 = 0xb45462e10c32ba36, B2 = 0xb45462ef0c32ba35
After Permutation: B1 = 0x9d552ad0540e4873, B2 = 0x9f552ad0540f58f1
Round 1 Difference: 0x200000000011082

--- Round 2 ---
After S-box: B1 = 0x40aa350da9db9f12, B2 = 0x48aa350da9d8af87, Difference = 0x800000000033095
Active S-boxes in Round 2 After S-box: [1, 2, 4, 5, 15]
  S-box 1: Active bits = b0, b2
  S-box 2: Active bits = b0, b3
  S-box 4: Active bits = b0, b1
  S-box 5: Active bits = b0, b1
  S-box 15: Active bits = b3
After Key XOR: B1 = 0x703fa10189eabf32, B2 = 0x783fa10189e98fa7
After Permutation: B1 = 0x10358550d7ee2d5b, B2 = 0x1820855ad7ee3d5e
Round 2 Difference: 0x815000a00001005

--- Round 3 ---
After S-box: B1 = 0x7d2afaad01bb30ae, B2 = 0x7f3dfaa501bb20ab, Difference = 0x217000800001005
Active S-boxes in Round 3 After S-box: [1, 4, 9, 13, 14, 15]
  S-box 1: Active bits = b0, b2
  S-box 4: Active bits = b0
  S-box 9: Active bits = b3
  S-box 13: Active bits = b0, b1, b2
  S-box 14: Active bits = b0
  S-box 15: Active bits = b1
After Key XOR: B1 = 0x6d4472ef04b222a8, B2 = 0x6f5372e704b232ad
After Permutation: B1 = 0x7d32fd8141940f4, B2 = 0xfd32fdc141b706d
Round 3 Difference: 0x800000400023099

--- Round 4 ---
After S-box: B1 = 0xd102380f79749d89, B2 = 0xd8023806797e1dc0, Difference = 0x9000009000a8049
Active S-boxes in Round 4 After S-box: [1, 2, 4, 5, 9, 15]
  S-box 1: Active bits = b0, b3
  S-box 2: Active bits = b2
  S-box 4: Active bits = b3
  S-box 5: Active bits = b1, b3
  S-box 9: Active bits = b0, b3
  S-box 15: Active bits = b0, b3
After Key XOR: B1 = 0xf30214bd29169430, B2 = 0xfa0214b4291c1479
Round 4 Difference: 0x9000009000a8049

Pair 4:
P1: 0xff51865569fcd208, P2: 0xff51865a69fcd207

--- Round 1 ---
After S-box: B1 = 0x88a7fcaac48603df, B2 = 0x88a7fca5c48603d1, Difference = 0xf0000000e
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b1, b2, b3
  S-box 9: Active bits = b0, b1, b2, b3
After Key XOR: B1 = 0x2ea7c6aa80064bc9, B2 = 0x2ea7c6a580064bc7
After Permutation: B1 = 0x5472588c1141f6dc, B2 = 0x5e70589c1140f65e
Round 1 Difference: 0xa02001000010082

--- Round 2 ---
After S-box: B1 = 0xa913aff677978c06, B2 = 0xab1daf46779d8cab, Difference = 0x20e00b0000a00ad
Active S-boxes in Round 2 After S-box: [1, 2, 5, 10, 13, 15]
  S-box 1: Active bits = b0, b2, b3
  S-box 2: Active bits = b1, b3
  S-box 5: Active bits = b1, b3
  S-box 10: Active bits = b0, b1, b3
  S-box 13: Active bits = b1, b2, b3
  S-box 15: Active bits = b1
After Key XOR: B1 = 0x99863bfa57a6ac26, B2 = 0x9b883b4a57acac8b
After Permutation: B1 = 0xbcd939618c9d89be, B2 = 0xb0cb316c8abd99a6
Round 2 Difference: 0xc12080d06201018

--- Round 3 ---
After S-box: B1 = 0xe60424c7f640f4eb, B2 = 0xed6e27c6f5e0445c, Difference = 0xb6a030103a0b0b7
Active S-boxes in Round 3 After S-box: [1, 2, 4, 6, 7, 9, 11, 13, 14, 15]
  S-box 1: Active bits = b0, b1, b2
  S-box 2: Active bits = b0, b1, b3
  S-box 4: Active bits = b0, b1, b3
  S-box 6: Active bits = b1, b3
  S-box 7: Active bits = b0, b1
  S-box 9: Active bits = b0
  S-box 11: Active bits = b0, b1
  S-box 13: Active bits = b1, b3
  S-box 14: Active bits = b1, b2
  S-box 15: Active bits = b0, b1, b3
After Key XOR: B1 = 0xf66aac85f349e6ed, B2 = 0xfd00af84f0e9565a
After Permutation: B1 = 0xee2bc6febe641f48, B2 = 0xe646c5e2b8f80e47
Round 3 Difference: 0x86d031c069c110f

--- Round 4 ---
After S-box: B1 = 0xbb3e6c8bebc9789f, B2 = 0xbc9c6ab3ef8fdb91, Difference = 0x7a206380446a30e
Active S-boxes in Round 4 After S-box: [1, 3, 4, 5, 6, 7, 9, 10, 11, 13, 14, 15]
  S-box 1: Active bits = b1, b2, b3
  S-box 3: Active bits = b0, b1
  S-box 4: Active bits = b1, b3
  S-box 5: Active bits = b1, b2
  S-box 6: Active bits = b2
  S-box 7: Active bits = b2
  S-box 9: Active bits = b3
  S-box 10: Active bits = b0, b1
  S-box 11: Active bits = b1, b2
  S-box 13: Active bits = b1
  S-box 14: Active bits = b1, b3
  S-box 15: Active bits = b0, b1, b2
After Key XOR: B1 = 0x993e4039bbab7126, B2 = 0x9e9c4601bfedd228
Round 4 Difference: 0x7a206380446a30e

Pair 5:
P1: 0xd6ffe91e2253ec84, P2: 0xd6ffe9112253ec8b

--- Round 1 ---
After S-box: B1 = 0xc88b47b33a2b6f9, B2 = 0xc88b47733a2b6fe, Difference = 0xc00000007
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b0, b1, b2
  S-box 9: Active bits = b2, b3
After Key XOR: B1 = 0xaa888e7b7722feef, B2 = 0xaa888e777722fee8
After Permutation: B1 = 0xf85b783dbe4d13e7, B2 = 0xf25b783dbe4d0365
Round 1 Difference: 0xa00000000001082

--- Round 2 ---
After S-box: B1 = 0x8fae1f20eb9072b1, B2 = 0x83ae1f20eb90d2ca, Difference = 0xc0000000000a07b
Active S-boxes in Round 2 After S-box: [1, 2, 4, 15]
  S-box 1: Active bits = b0, b1, b3
  S-box 2: Active bits = b0, b1, b2
  S-box 4: Active bits = b1, b3
  S-box 15: Active bits = b2, b3
After Key XOR: B1 = 0xbf3b8b2ccba15291, B2 = 0xb33b8b2ccba1f2ea
After Permutation: B1 = 0x826c49ae5ada3dcd, B2 = 0x826b492e5ede2fcb
Round 2 Difference: 0x7008004041206

--- Round 3 ---
After S-box: B1 = 0xf3c6945ba5052060, B2 = 0xf3ce943bab0b386e, Difference = 0x800600e0e180e
Active S-boxes in Round 3 After S-box: [1, 3, 4, 5, 7, 10, 13]
  S-box 1: Active bits = b1, b2, b3
  S-box 3: Active bits = b3
  S-box 4: Active bits = b0
  S-box 5: Active bits = b1, b2, b3
  S-box 7: Active bits = b1, b2, b3
  S-box 10: Active bits = b1, b2
  S-box 13: Active bits = b3
After Key XOR: B1 = 0xe3a81c19a00c3266, B2 = 0xe3a01c79ae022a68
After Permutation: B1 = 0xc8a11435363086c3, B2 = 0xd0bb3c35741006e0
Round 3 Difference: 0x181a280042208023

--- Round 4 ---
After S-box: B1 = 0x6f57792a2c2dfc62, B2 = 0xdee262a197ddcbd, Difference = 0x62b95f00355020df
Active S-boxes in Round 4 After S-box: [1, 2, 4, 6, 7, 8, 11, 12, 13, 14, 15, 16]
  S-box 1: Active bits = b0, b1, b2, b3
  S-box 2: Active bits = b0, b2, b3
  S-box 4: Active bits = b1
  S-box 6: Active bits = b0, b2
  S-box 7: Active bits = b0, b2
  S-box 8: Active bits = b0, b1
  S-box 11: Active bits = b0, b1, b2, b3
  S-box 12: Active bits = b0, b2
  S-box 13: Active bits = b0, b3
  S-box 14: Active bits = b0, b1, b3
  S-box 15: Active bits = b1
  S-box 16: Active bits = b1, b2
After Key XOR: B1 = 0x4d5755987c4ff5db, B2 = 0x2fee0a98491fd504
Round 4 Difference: 0x62b95f00355020df

Pair 6:
P1: 0x6c9fdc8cd5a4e8f6, P2: 0x6c9fdc83d5a4e8f9

--- Round 1 ---
After S-box: B1 = 0xc64806f60a59bf8c, B2 = 0xc64806f20a59bf84, Difference = 0x400000008
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b3
  S-box 9: Active bits = b2
After Key XOR: B1 = 0x60483cf64ed9f79a, B2 = 0x60483cf24ed9f792
After Permutation: B1 = 0x478fef6bdb250063, B2 = 0x458def6bdb250063
Round 1 Difference: 0x202000000000000

--- Round 2 ---
After S-box: B1 = 0x91f8b8ce0e3addc2, B2 = 0x9af0b8ce0e3addc2, Difference = 0xb08000000000000
Active S-boxes in Round 2 After S-box: [13, 15]
  S-box 13: Active bits = b3
  S-box 15: Active bits = b0, b1, b3
After Key XOR: B1 = 0xa16d2cc22e0bfde2, B2 = 0xaa652cc22e0bfde2
After Permutation: B1 = 0xd439626af7352233, B2 = 0xd439626ef5252237
Round 2 Difference: 0x402100004

--- Round 3 ---
After S-box: B1 = 0x924c3c5812a3322, B2 = 0x924c3cb8a3a3321, Difference = 0xe0b100003
Active S-boxes in Round 3 After S-box: [1, 6, 7, 9]
  S-box 1: Active bits = b0, b1
  S-box 6: Active bits = b0
  S-box 7: Active bits = b0, b1, b3
  S-box 9: Active bits = b1, b2, b3
After Key XOR: B1 = 0x194a4b8784232124, B2 = 0x194a4b898f332127
After Permutation: B1 = 0xe51023207994c2c, B2 = 0xd59023247985dae
Round 3 Difference: 0x308000040011182

--- Round 4 ---
After S-box: B1 = 0xdba7d323d1449636, B2 = 0xd0a4d323914fa05b, Difference = 0xb030000400b366d
Active S-boxes in Round 4 After S-box: [1, 2, 3, 4, 5, 8, 13, 15]
  S-box 1: Active bits = b0, b2, b3
  S-box 2: Active bits = b1, b2
  S-box 3: Active bits = b1, b2
  S-box 4: Active bits = b0, b1
  S-box 5: Active bits = b0, b1, b3
  S-box 8: Active bits = b2
  S-box 13: Active bits = b0, b1
  S-box 15: Active bits = b0, b1, b3
After Key XOR: B1 = 0xf9a7ff9181269f8f, B2 = 0xf2a4ff91c12da9e2
Round 4 Difference: 0xb030000400b366d

Pair 7:
P1: 0x11d868f29181b14d, P2: 0x11d868fd9181b142

--- Round 1 ---
After S-box: B1 = 0x770fcf8347f7e790, B2 = 0x770fcf8047f7e793, Difference = 0x300000003
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b0, b1
  S-box 9: Active bits = b0, b1
After Key XOR: B1 = 0xd10ff5830377af86, B2 = 0xd10ff5800377af85
After Permutation: B1 = 0xdd99845a83dde95a, B2 = 0xdd99844a83dcf958
Round 1 Difference: 0x1000011002

--- Round 2 ---
After S-box: B1 = 0x44f9a5f200b4a5, B2 = 0x44f995f20684af, Difference = 0x300006300a
Active S-boxes in Round 2 After S-box: [1, 4, 5, 10]
  S-box 1: Active bits = b1, b3
  S-box 4: Active bits = b0, b1
  S-box 5: Active bits = b1, b2
  S-box 10: Active bits = b0, b1
After Key XOR: B1 = 0x30d16da9d2319485, B2 = 0x30d16d99d237a48f
After Permutation: B1 = 0x6d081a7a988e7c81, B2 = 0x6d1b127b988efc82
Round 2 Difference: 0x13080100008003

--- Round 3 ---
After S-box: B1 = 0xc0df75154ffb16f7, B2 = 0xc07e731e4ffb86f3, Difference = 0xa1060b00009004
Active S-boxes in Round 3 After S-box: [1, 4, 9, 11, 13, 14]
  S-box 1: Active bits = b2
  S-box 4: Active bits = b0, b3
  S-box 9: Active bits = b0, b1, b3
  S-box 11: Active bits = b1, b2
  S-box 13: Active bits = b0
  S-box 14: Active bits = b1, b3
After Key XOR: B1 = 0xd0b1fd574af204f1, B2 = 0xd010fb5c4af294f5
After Permutation: B1 = 0xc3bcb579cccb7a00, B2 = 0x8bdca569ccce5a81
Round 3 Difference: 0x4860101000052081

--- Round 4 ---
After S-box: B1 = 0x62e6ea14666e15dd, B2 = 0xfe065ac4666ba5f7, Difference = 0x9ce0b0d00005b02a
Active S-boxes in Round 4 After S-box: [1, 2, 4, 5, 10, 12, 14, 15, 16]
  S-box 1: Active bits = b1, b3
  S-box 2: Active bits = b1
  S-box 4: Active bits = b0, b1, b3
  S-box 5: Active bits = b0, b2
  S-box 10: Active bits = b0, b2, b3
  S-box 12: Active bits = b0, b1, b3
  S-box 14: Active bits = b1, b2, b3
  S-box 15: Active bits = b2, b3
  S-box 16: Active bits = b0, b3
After Key XOR: B1 = 0x40e6c6a6360c1c64, B2 = 0xdc0676763609ac4e
Round 4 Difference: 0x9ce0b0d00005b02a

Pair 8:
P1: 0xf39c43c0b89b6aef, P2: 0xf39c43cfb89b6ae0

--- Round 1 ---
After S-box: B1 = 0x8246926def4ec5b8, B2 = 0x82469268ef4ec5bd, Difference = 0x500000005
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b0, b2
  S-box 9: Active bits = b0, b2
After Key XOR: B1 = 0x2446a86dabce8dae, B2 = 0x2446a868abce8dab
After Permutation: B1 = 0x1a1aabf8f564859a, B2 = 0x101aabe8f564959a
Round 1 Difference: 0xa00001000001000

--- Round 2 ---
After S-box: B1 = 0x75755e8f8ac9fa45, B2 = 0x7d755ebf8ac94a45, Difference = 0x80000300000b000
Active S-boxes in Round 2 After S-box: [4, 10, 15]
  S-box 4: Active bits = b0, b1, b3
  S-box 10: Active bits = b0, b1
  S-box 15: Active bits = b3
After Key XOR: B1 = 0x45e0ca83aaf8da65, B2 = 0x4de0cab3aaf86a65
After Permutation: B1 = 0x1d68d7b0647d5641, B2 = 0x1d69dfb164795644
Round 2 Difference: 0x1080100040005

--- Round 3 ---
After S-box: B1 = 0x70cf01edc910ac97, B2 = 0x70c408e7c914ac99, Difference = 0xb090a0004000e
Active S-boxes in Round 3 After S-box: [1, 5, 9, 11, 13]
  S-box 1: Active bits = b1, b2, b3
  S-box 5: Active bits = b2
  S-box 9: Active bits = b1, b3
  S-box 11: Active bits = b0, b3
  S-box 13: Active bits = b0, b1, b3
After Key XOR: B1 = 0x60a189afcc19be91, B2 = 0x60aa80a5cc1dbe9f
After Permutation: B1 = 0x17251c3ad8e534e1, B2 = 0x1f271c1ada64946b
Round 3 Difference: 0x80200200281a08a

--- Round 4 ---
After S-box: B1 = 0x713a76250fba29b7, B2 = 0x7831767505c949ce, Difference = 0x90b00500a736079
Active S-boxes in Round 4 After S-box: [1, 2, 4, 5, 6, 7, 10, 13, 15]
  S-box 1: Active bits = b0, b3
  S-box 2: Active bits = b0, b1, b2
  S-box 4: Active bits = b1, b2
  S-box 5: Active bits = b0, b1
  S-box 6: Active bits = b0, b1, b2
  S-box 7: Active bits = b1, b3
  S-box 10: Active bits = b0, b2
  S-box 13: Active bits = b0, b1, b3
  S-box 15: Active bits = b0, b3
After Key XOR: B1 = 0x533a5a975fd8200e, B2 = 0x5a315ac755ab4077
Round 4 Difference: 0x90b00500a736079

Pair 9:
P1: 0x135c19b2a8a35640, P2: 0x135c19bda8a3564f

--- Round 1 ---
After S-box: B1 = 0x72a674e35f52ac9d, B2 = 0x72a674e05f52ac98, Difference = 0x300000005
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b0, b2
  S-box 9: Active bits = b0, b1
After Key XOR: B1 = 0xd4a64ee31bd2e48b, B2 = 0xd4a64ee01bd2e48e
After Permutation: B1 = 0xe57bfdb8c005591a, B2 = 0xed7bfda8c004491a
Round 1 Difference: 0x800001000011000

--- Round 2 ---
After S-box: B1 = 0xba1e80ef6ddaa475, B2 = 0xb01e805f6dd99475, Difference = 0xa0000b000033000
Active S-boxes in Round 2 After S-box: [4, 5, 10, 15]
  S-box 4: Active bits = b0, b1
  S-box 5: Active bits = b0, b1
  S-box 10: Active bits = b0, b1, b3
  S-box 15: Active bits = b1, b3
After Key XOR: B1 = 0x8a8b14e34deb8455, B2 = 0x808b14534de8b455
After Permutation: B1 = 0xcc94b916ca2d332c, B2 = 0xc885b111ca2d3329
Round 2 Difference: 0x411080700000005

--- Round 3 ---
After S-box: B1 = 0x6649e47c65302236, B2 = 0x6ffae77765302234, Difference = 0x9b3030b00000002
Active S-boxes in Round 3 After S-box: [1, 9, 11, 13, 14, 15]
  S-box 1: Active bits = b1
  S-box 9: Active bits = b0, b1, b3
  S-box 11: Active bits = b0, b1
  S-box 13: Active bits = b0, b1
  S-box 14: Active bits = b0, b1, b3
  S-box 15: Active bits = b0, b3
After Key XOR: B1 = 0x76276c3e60393030, B2 = 0x7f946f3560393032
After Permutation: B1 = 0x43250ce73c296899, B2 = 0x43451cf73cba4817
Round 3 Difference: 0x6010100093208e

--- Round 4 ---
After S-box: B1 = 0x923ad6b12634cf44, B2 = 0x929a768126e59f71, Difference = 0xa0a03000d15035
Active S-boxes in Round 4 After S-box: [1, 2, 4, 5, 6, 10, 12, 14]
  S-box 1: Active bits = b0, b2
  S-box 2: Active bits = b0, b1
  S-box 4: Active bits = b0, b2
  S-box 5: Active bits = b0
  S-box 6: Active bits = b0, b2, b3
  S-box 10: Active bits = b0, b1
  S-box 12: Active bits = b1, b3
  S-box 14: Active bits = b1, b3
After Key XOR: B1 = 0xb03afa037656c6fd, B2 = 0xb09a5a33768796c8
Round 4 Difference: 0xa0a03000d15035

Pair 10:
P1: 0x6513ccd48b2a82a, P2: 0x6513cc248b2a825

--- Round 1 ---
After S-box: B1 = 0xdca726609fe35f35, B2 = 0xdca726639fe35f3a, Difference = 0x30000000f
Active S-boxes in Round 1 After S-box: [1, 9]
  S-box 1: Active bits = b0, b1, b2, b3
  S-box 9: Active bits = b0, b1
After Key XOR: B1 = 0x7aa71c60db631723, B2 = 0x7aa71c63db63172c
After Permutation: B1 = 0x60b8bc26dd083d5f, B2 = 0x68babc36dd092d5d
Round 1 Difference: 0x802001000011002

--- Round 2 ---
After S-box: B1 = 0xcdefe63c00df20a8, B2 = 0xcfe5e62c00d430a0, Difference = 0x20a0010000b1008
Active S-boxes in Round 2 After S-box: [1, 4, 5, 10, 13, 15]
  S-box 1: Active bits = b3
  S-box 4: Active bits = b0
  S-box 5: Active bits = b0, b1, b3
  S-box 10: Active bits = b0
  S-box 13: Active bits = b1, b3
  S-box 15: Active bits = b1
After Key XOR: B1 = 0xfd7a723020ee0088, B2 = 0xff70722020e51080
After Permutation: B1 = 0x80f28fc9323ac80c, B2 = 0x80e08fce301ac805
Round 2 Difference: 0x12000702200009

--- Round 3 ---
After S-box: B1 = 0xfd83f86423256fd6, B2 = 0xfdbdf86b2d756fda, Difference = 0x3e000f0e50000c
Active S-boxes in Round 3 After S-box: [1, 6, 7, 9, 13, 14]
  S-box 1: Active bits = b2, b3
  S-box 6: Active bits = b0, b2
  S-box 7: Active bits = b1, b2, b3
  S-box 9: Active bits = b0, b1, b2, b3
  S-box 13: Active bits = b1, b2, b3
  S-box 14: Active bits = b0, b1
After Key XOR: B1 = 0xeded7026262c7dd0, B2 = 0xedd37029287c7ddc
After Permutation: B1 = 0x92ad5ec8b339e235, B2 = 0x9987ded8f13ae28d
Round 3 Difference: 0xb2a8010420300b8

--- Round 4 ---
After S-box: B1 = 0x4350ab6fe224b32a, B2 = 0x44f10b0f8725b3f0, Difference = 0x7a1a060650100da
Active S-boxes in Round 4 After S-box: [1, 2, 5, 7, 8, 10, 12, 13, 14, 15]
  S-box 1: Active bits = b1, b3
  S-box 2: Active bits = b0, b2, b3
  S-box 5: Active bits = b0
  S-box 7: Active bits = b0, b2
  S-box 8: Active bits = b1, b2
  S-box 10: Active bits = b1, b2
  S-box 12: Active bits = b1, b3
  S-box 13: Active bits = b0
  S-box 14: Active bits = b1, b3
  S-box 15: Active bits = b0, b1, b2
After Key XOR: B1 = 0x615087ddb246ba93, B2 = 0x66f127bdd747ba49
Round 4 Difference: 0x7a1a060650100da

=== Differential Attack Complete ===
```
## Automated Cryptanalysis  Mixed-Integer Linear Programming (MILP)
```
gurobi_cl puffin_milp.lp
```
![image](https://github.com/user-attachments/assets/e43cb609-c434-4190-89d3-07dfe2a872fe)



```
gurobi_cl ResultFile=puffin_sol.sol puffin_milp.lp
```
![image](https://github.com/user-attachments/assets/16e86cc2-fc4c-473e-9939-9700805571f9)



## Software Application
![image](https://github.com/user-attachments/assets/0b138b07-87cb-43c8-973e-1b47723c0e50)
