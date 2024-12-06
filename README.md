# PUFFIN Block Cipher
Implementation of PUFFIN block cipher
![image](https://github.com/user-attachments/assets/8a4e30ef-d721-41dd-83d8-fd38d5dd4ce7)

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
Plaintext: PUFFIN 1234
Ciphertext (Hex): b86b37c46150a3cb6e5b0287023cf4aa
Decrypted Text: PUFFIN 1234

=== Differential Attack ===
Master Key: 0x123456789abcdef
Initial Difference (Delta_0): 0xf0000000f

Pair 1:
P1: 0x1d3e1a3f03fec8fa, P2: 0x1d3e1a3003fec8f5

--- Round 1 ---
After S-box: B1 = 0x702b7528d28b6f85, B2 = 0x702b752dd28b6f8a
After Key XOR: B1 = 0xd62b4f28960b2793, B2 = 0xd62b4f2d960b279c
After Permutation: B1 = 0xe07d0cae83a07cea, B2 = 0xea7f0cbe83a06ce8
Round 1 Difference: 0xa02001000001002
Active S-boxes in Round 1: [1, 4, 10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0xbd10d65bf25d16b5, B2 = 0xb518d6ebf25dc6bf
After Key XOR: B1 = 0x8d854257d26c3695, B2 = 0x858d42e7d26ce69f
After Permutation: B1 = 0xaa4db0998839f455, B2 = 0xae4ff8988a3df452
Round 2 Difference: 0x402480102040007
Active S-boxes in Round 2: [1, 5, 7, 9, 11, 12, 13, 15]

--- Round 3 ---
After S-box: B1 = 0x5590ed44ff2489aa, B2 = 0x5b988f4ff52089a3
After Key XOR: B1 = 0x45fe6506fa2d9bac, B2 = 0x4bf6070df0299ba5
Round 3 Difference: 0xe08620b0a040009
Active S-boxes in Round 3: [1, 5, 7, 9, 11, 12, 13, 15]

Pair 2:
P1: 0xdc231dfdcb1be730, P2: 0xdc231df2cb1be73f

--- Round 1 ---
After S-box: B1 = 0x63270806e7eb12d, B2 = 0x63270836e7eb128
After Key XOR: B1 = 0xa0324a802afef93b, B2 = 0xa0324a832afef93e
After Permutation: B1 = 0x957fc120752ed00b, B2 = 0x9d7fc130752fc00b
Round 1 Difference: 0x800001000011000
Active S-boxes in Round 1: [4, 5, 10, 15]

--- Round 2 ---
After S-box: B1 = 0x4a18673d1a3b0dde, B2 = 0x4018672d1a386dde
After Key XOR: B1 = 0x7a8df3313a0a2dfe, B2 = 0x708df3213a094dfe
After Permutation: B1 = 0x38df1c5df7e06a16, B2 = 0x38ce5c5af7e06a12
Round 2 Difference: 0x11400700000004
Active S-boxes in Round 2: [1, 9, 12, 13, 14]

--- Round 3 ---
After S-box: B1 = 0x2f0876a081bdc57c, B2 = 0x2f6ba6a581bdc573
After Key XOR: B1 = 0x3f66fee284b4d77a, B2 = 0x3f052ee784b4d775
Round 3 Difference: 0x63d0050000000f
Active S-boxes in Round 3: [1, 9, 12, 13, 14]

Pair 3:
P1: 0x22a60b8dafd6413f, P2: 0x22a60b82afd64130

--- Round 1 ---
After S-box: B1 = 0x335cdef0580c9728, B2 = 0x335cdef3580c972d
After Key XOR: B1 = 0x955ce4f01c8cdf3e, B2 = 0x955ce4f31c8cdf3b
After Permutation: B1 = 0xfc066bc1c776c873, B2 = 0xf4066bd1c777d873
Round 1 Difference: 0x800001000011000
Active S-boxes in Round 1: [4, 5, 10, 15]

--- Round 2 ---
After S-box: B1 = 0x86dcce67611c6f12, B2 = 0x89dcce0761110f12
After Key XOR: B1 = 0xb6495a6b412d4f32, B2 = 0xb9495a0b41202f32
After Permutation: B1 = 0x90c46ab69f29e9c2, B2 = 0x90c502309f1969c6
Round 2 Difference: 0x1688600308004
Active S-boxes in Round 2: [1, 4, 6, 9, 10, 11, 12, 13]

--- Round 3 ---
After S-box: B1 = 0x4d69c5ec4834b463, B2 = 0x4d6ad32d4874c46c
After Key XOR: B1 = 0x5d074dae4d3da665, B2 = 0x5d045b6f4d7dd66a
Round 3 Difference: 0x316c10040700f
Active S-boxes in Round 3: [1, 4, 6, 9, 10, 11, 12, 13]

Pair 4:
P1: 0xe0fd4e2fc99a61c3, P2: 0xe0fd4e20c99a61cc

--- Round 1 ---
After S-box: B1 = 0xbd809b386445c762, B2 = 0xbd809b3d6445c766
After Key XOR: B1 = 0x1b80a13820c58f74, B2 = 0x1b80a13d20c58f70
After Permutation: B1 = 0x18049947a5d48ac4, B2 = 0x12049957a5d48ac4
Round 1 Difference: 0xa00001000000000
Active S-boxes in Round 1: [10, 15]

--- Round 2 ---
After S-box: B1 = 0x7fd944915a09f569, B2 = 0x73d944a15a09f569
After Key XOR: B1 = 0x4f4cd09d7a38d549, B2 = 0x434cd0ad7a38d549
After Permutation: B1 = 0x278a4695eb7c5295, B2 = 0x278a4e14eb7c5291
Round 2 Difference: 0x88100000004
Active S-boxes in Round 2: [1, 9, 10, 11]

--- Round 3 ---
After S-box: B1 = 0x31f59c4abe16a34a, B2 = 0x31f59b79be16a347
After Key XOR: B1 = 0x219b1408bb1fb14c, B2 = 0x219b133bbb1fb141
Round 3 Difference: 0x7330000000d
Active S-boxes in Round 3: [1, 9, 10, 11]

Pair 5:
P1: 0xdfd0684ddff42217, P2: 0xdfd06842dff42218

--- Round 1 ---
After S-box: B1 = 0x80dcf9008893371, B2 = 0x80dcf930889337f
After Key XOR: B1 = 0xae0df5904c097b67, B2 = 0xae0df5934c097b69
After Permutation: B1 = 0xdc8140c75fe07277, B2 = 0xd48340d75fe17275
Round 1 Difference: 0x802001000010002
Active S-boxes in Round 1: [1, 5, 10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0x6f79d61a8bd1311, B2 = 0x9f29d01a8b7131a
After Key XOR: B1 = 0x3662096d888c3331, B2 = 0x3967090d8886333a
After Permutation: B1 = 0x2252bb455a09cc9, B2 = 0x23703305590acdf
Round 2 Difference: 0x12288400303016
Active S-boxes in Round 2: [1, 2, 4, 6, 9, 10, 11, 12, 13, 14]

--- Round 3 ---
After S-box: B1 = 0xd33a3ee9aa5d4664, B2 = 0xd321d22daa4d5608
After Key XOR: B1 = 0xc354b6abaf545462, B2 = 0xc34f5a6faf44440e
Round 3 Difference: 0x1becc40010106c
Active S-boxes in Round 3: [1, 2, 4, 6, 9, 10, 11, 12, 13, 14]

Pair 6:
P1: 0x3321bce030ffce56, P2: 0x3321bcef30ffce59

--- Round 1 ---
After S-box: B1 = 0x2237e6bd2d886bac, B2 = 0x2237e6b82d886ba4
After Key XOR: B1 = 0x8437dcbd690823ba, B2 = 0x8437dcb8690823b2
After Permutation: B1 = 0xc6a708b96d6261da, B2 = 0xc4a508a96d6261da
Round 1 Difference: 0x202001000000000
Active S-boxes in Round 1: [10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0x6c51dfe4c0c3c705, B2 = 0x695adf54c0c3c705
After Key XOR: B1 = 0x5cc44be8e0f2e725, B2 = 0x59cf4b58e0f2e725
After Permutation: B1 = 0xd51ffa0ad8c5cd4, B2 = 0x951f721af9c7cdc
Round 2 Difference: 0x400088102102008
Active S-boxes in Round 2: [1, 4, 6, 7, 9, 10, 11, 15]

--- Round 3 ---
After S-box: B1 = 0xd0a7885d50f6a609, B2 = 0xd4a7813758461606
After Key XOR: B1 = 0xc0c9001f55ffb40f, B2 = 0xc4c909755d4f0400
Round 3 Difference: 0x400096a08b0b00f
Active S-boxes in Round 3: [1, 4, 6, 7, 9, 10, 11, 15]

Pair 7:
P1: 0x568208da5122d0bd, P2: 0x568208d55122d0b2

--- Round 1 ---
After S-box: B1 = 0xacf3df05a7330de0, B2 = 0xacf3df0aa7330de3
After Key XOR: B1 = 0xaf3e505e3b345f6, B2 = 0xaf3e50ae3b345f5
After Permutation: B1 = 0x4b3c535eadca670e, B2 = 0x493c534eadcb778c
Round 1 Difference: 0x200001000011082
Active S-boxes in Round 1: [1, 2, 4, 5, 10, 15]

--- Round 2 ---
After S-box: B1 = 0x9e26a2ab5065c1db, B2 = 0x9426a29b506e11f6
After Key XOR: B1 = 0xaeb336a77054e1fb, B2 = 0xa4b33697705f31d6
After Permutation: B1 = 0xe7e7d8dc3d07b20e, B2 = 0xeff590db3923a20b
Round 2 Difference: 0x812480704241005
Active S-boxes in Round 2: [1, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15]

--- Round 3 ---
After S-box: B1 = 0xb1b10f0620d1e3db, B2 = 0xb88a4d0e243253de
After Key XOR: B1 = 0xa1df874425d8f1dd, B2 = 0xa8e4c54c213b41d8
Round 3 Difference: 0x93b420804e3b005
Active S-boxes in Round 3: [1, 4, 5, 6, 7, 9, 11, 12, 13, 14, 15]

Pair 8:
P1: 0x56efc92f7236504e, P2: 0x56efc92072365041

--- Round 1 ---
After S-box: B1 = 0xacb86438132cad9b, B2 = 0xacb8643d132cad97
After Key XOR: B1 = 0xab85e3857ace58d, B2 = 0xab85e3d57ace581
After Permutation: B1 = 0x68eb592d8b2ed1a4, B2 = 0x62e9593d8b2ed1a4
Round 1 Difference: 0xa02001000000000
Active S-boxes in Round 1: [10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0xcfbea430fe3b0759, B2 = 0xc3b4a420fe3b0759
After Key XOR: B1 = 0xff2b303cde0a2779, B2 = 0xf321302cde0a2779
After Permutation: B1 = 0xa2bf0cc5df303eec, B2 = 0xa2bf0c44dd303ee0
Round 2 Difference: 0x810200000c
Active S-boxes in Round 2: [1, 7, 9, 10]

--- Round 3 ---
After S-box: B1 = 0x53e8d66a082d2bb6, B2 = 0x53e8d699002d2bbd
After Key XOR: B1 = 0x43865e280d2439b0, B2 = 0x43865edb052439bb
Round 3 Difference: 0xf30800000b
Active S-boxes in Round 3: [1, 7, 9, 10]

Pair 9:
P1: 0x7f9b10429341f792, P2: 0x7f9b104d9341f79d

--- Round 1 ---
After S-box: B1 = 0x184e7d9342978143, B2 = 0x184e7d9042978140
After Key XOR: B1 = 0xbe4e47930617c955, B2 = 0xbe4e47900617c956
After Permutation: B1 = 0xdd5c42971385da3c, B2 = 0xdd5c42871384ca3e
Round 1 Difference: 0x1000011002
Active S-boxes in Round 1: [1, 4, 5, 10]

--- Round 2 ---
After S-box: B1 = 0xa6934172fa0526, B2 = 0xa693f172f9652b
After Key XOR: B1 = 0x3033074d52cb2506, B2 = 0x303307fd52c8450b
After Permutation: B1 = 0x6a79a11299a2288a, B2 = 0x666ae91199a2388a
Round 2 Difference: 0xc13480300001000
Active S-boxes in Round 2: [4, 9, 11, 12, 13, 14, 15]

--- Round 3 ---
After S-box: B1 = 0xc514577344533ff5, B2 = 0xccc5b47744532ff5
After Key XOR: B1 = 0xd57adf31415a2df3, B2 = 0xdcab3c35415a3df3
Round 3 Difference: 0x9d1e30400001000
Active S-boxes in Round 3: [4, 9, 11, 12, 13, 14, 15]

Pair 10:
P1: 0x66ee138da9099740, P2: 0x66ee1382a909974f

--- Round 1 ---
After S-box: B1 = 0xccbb72f054d4419d, B2 = 0xccbb72f354d44198
After Key XOR: B1 = 0x6abb48f01054098b, B2 = 0x6abb48f31054098e
After Permutation: B1 = 0x3522bc2d1302f00e, B2 = 0x3d22bc3d1303e00e
Round 1 Difference: 0x800001000011000
Active S-boxes in Round 1: [4, 5, 10, 15]

--- Round 2 ---
After S-box: B1 = 0x2a33e63072d38ddb, B2 = 0x2033e62072d2bddb
After Key XOR: B1 = 0x1aa6723c52e2adfb, B2 = 0x10a6722c52e39dfb
After Permutation: B1 = 0x32ff994d8d0c5a9e, B2 = 0x32fe994a8d0c5a9b
Round 2 Difference: 0x1000700000005
Active S-boxes in Round 2: [1, 9, 13]

--- Round 3 ---
After S-box: B1 = 0x23884490f0d6a54b, B2 = 0x238b4495f0d6a54e
After Key XOR: B1 = 0x33e6ccd2f5dfb74d, B2 = 0x33e5ccd7f5dfb748
Round 3 Difference: 0x3000500000005
Active S-boxes in Round 3: [1, 9, 13]

=== Differential Attack Complete ===
```
## Automated Cryptanalysis  Mixed-Integer Linear Programming (MILP)
```
gurobi_cl puffin_milp.lp
```
![image](https://github.com/user-attachments/assets/ed8d4658-8438-4f4b-9c43-a9d0d274f821)


```
gurobi_cl ResultFile=puffin_sol.sol puffin_milp.lp
```
![image](https://github.com/user-attachments/assets/84363fc4-98de-4021-a222-68be4bcbf7ac)


## Software Application
![image](https://github.com/user-attachments/assets/0b138b07-87cb-43c8-973e-1b47723c0e50)
