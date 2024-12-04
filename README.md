# PUFFIN Block Cipher
Implementation of PUFFIN block cipher

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
P1: 0xd2086a061c0c8886, P2: 0xd2086a091c0c8889

--- Round 1 ---
After S-box: B1 = 0x3dfc5dc76d6fffc, B2 = 0x3dfc5d476d6fff4
After Key XOR: B1 = 0x2fc80bbff7d3213, B2 = 0x2fc80b3ff7d321b
After Permutation: B1 = 0x252d9a176a6b95f3, B2 = 0x252f9a176a6b9573
Round 1 Difference: 0x2000000000080
Active S-boxes in Round 1: [2, 13]

--- Round 2 ---
After S-box: B1 = 0x3a304571c5ce4a82, B2 = 0x3a384571c5ce4a12
After Key XOR: B1 = 0x3a30445280a9c329, B2 = 0x3a38445280a9c3b9
After Permutation: B1 = 0x40226107152f5c44, B2 = 0x4026610f172f5c44
Round 2 Difference: 0x4000802000000
Active S-boxes in Round 2: [7, 9, 13]

--- Round 3 ---
After S-box: B1 = 0x9d33c7d17a38a699, B2 = 0x9d3cc7d87138a699
After Key XOR: B1 = 0x9d33c7d17b1be3fe, B2 = 0x9d3cc7d8701be3fe
After Permutation: B1 = 0xed7f609b6df66b4e, B2 = 0xed77608b2ff64ad6
Round 3 Difference: 0x8001042002198
Active S-boxes in Round 3: [1, 2, 3, 4, 7, 8, 10, 13]

Pair 2:
P1: 0x7233ef9576416848, P2: 0x7233ef9a76416847

--- Round 1 ---
After S-box: B1 = 0x1322b84a1c97cf9f, B2 = 0x1322b8451c97cf91
After Key XOR: B1 = 0x1201fd2d953c0270, B2 = 0x1201fd22953c027e
After Permutation: B1 = 0x6384087404e8efe0, B2 = 0x6986086404e9ef62
Round 1 Difference: 0xa02001000010082
Active S-boxes in Round 1: [1, 2, 5, 10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0xc2f9df19d9bfb8bd, B2 = 0xc4fcdfc9d9b4b8c3
After Key XOR: B1 = 0xc2f9de3a9cd83116, B2 = 0xc4fcdeea9cd33168
After Permutation: B1 = 0xe9e59f25436364a3, B2 = 0xe5f3bfa2474346b1
Round 2 Difference: 0xc16208704202212
Active S-boxes in Round 2: [1, 2, 3, 4, 6, 7, 9, 10, 12, 13, 14, 15]

--- Round 3 ---
After S-box: B1 = 0xb4ba483a92c2c952, B2 = 0xba82e85391929ce7
After Key XOR: B1 = 0xb4ba483a93e18c35, B2 = 0xba82e85390b1d980
After Permutation: B1 = 0xb82c99a3960f5d88, B2 = 0xb100717f114d4c0d
Round 3 Difference: 0x92ce8dc87421185
Active S-boxes in Round 3: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

Pair 3:
P1: 0xf3ea65b8e2673cb, P2: 0xf3ea6548e2673c4

--- Round 1 ---
After S-box: B1 = 0xd82b5caefb3c126e, B2 = 0xd82b5ca9fb3c1269
After Key XOR: B1 = 0xd90819c97297df81, B2 = 0xd90819ce7297df86
After Permutation: B1 = 0xb598653aab9498c5, B2 = 0xbf98652aab9588c7
Round 1 Difference: 0xa00001000011002
Active S-boxes in Round 1: [1, 4, 5, 10, 15]

--- Round 2 ---
After S-box: B1 = 0xea4fca255e494f6a, B2 = 0xe84fca355e4aff61
After Key XOR: B1 = 0xea4fcb061b2ec6c1, B2 = 0xe84fcb161b2d76ca
After Permutation: B1 = 0xa258462cd2edf35c, B2 = 0xa24b462bd2e9e35f
Round 2 Difference: 0x13000700041003
Active S-boxes in Round 2: [1, 4, 5, 9, 13, 14]

--- Round 3 ---
After S-box: B1 = 0x53af9c3603b082a6, B2 = 0x539e9c3e03b4b2a8
After Key XOR: B1 = 0x53af9c360293c7c1, B2 = 0x539e9c3e0297f7cf
After Permutation: B1 = 0x43b85d2f83553a58, B2 = 0x4b9b5d2f83579adb
Round 3 Difference: 0x82300000002a083
Active S-boxes in Round 3: [1, 2, 4, 5, 13, 14, 15]

Pair 4:
P1: 0xe085680b0f4f53ea, P2: 0xe08568040f4f53e5

--- Round 1 ---
After S-box: B1 = 0xbdfacfded898a2b5, B2 = 0xbdfacfd9d898a2ba
After Key XOR: B1 = 0xbcd98ab951336f5a, B2 = 0xbcd98abe51336f55
After Permutation: B1 = 0xb5575ab39b4a2bc6, B2 = 0xbf555aa39b4b3bc4
Round 1 Difference: 0xa02001000011002
Active S-boxes in Round 1: [1, 4, 5, 10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0xeaa1a5e24e953e6c, B2 = 0xe8aaa5524e9e2e69
After Key XOR: B1 = 0xeaa1a4c10bf2b7c7, B2 = 0xe8aaa4710bf9a7c2
After Permutation: B1 = 0xcd39b55cd14c3347, B2 = 0xc129bd5bd36c034e
Round 2 Difference: 0xc10080702203009
Active S-boxes in Round 2: [1, 4, 6, 7, 9, 11, 14, 15]

--- Round 3 ---
After S-box: B1 = 0x6024eaa607962291, B2 = 0x6734e0ae02c6d29b
After Key XOR: B1 = 0x6024eaa606b567f6, B2 = 0x6734e0ae03e597fc
After Permutation: B1 = 0xf6d4d6a9549c272, B2 = 0xe2e8dce955fc3d1
Round 3 Difference: 0x143c0a4001601a3
Active S-boxes in Round 3: [1, 2, 3, 5, 6, 9, 10, 12, 13, 14, 15]

Pair 5:
P1: 0xdf6b346fa631b5ad, P2: 0xdf6b3460a631b5a2

--- Round 1 ---
After S-box: B1 = 0x8ce29c85c27ea50, B2 = 0x8ce29cd5c27ea53
After Key XOR: B1 = 0x9ed6cafd58c27bf, B2 = 0x9ed6caad58c27bc
After Permutation: B1 = 0x6e271b788f31f5f6, B2 = 0x6c271b688f31e5f4
Round 1 Difference: 0x200001000001002
Active S-boxes in Round 1: [1, 4, 10, 15]

--- Round 2 ---
After S-box: B1 = 0xcb317e1ff8278a8c, B2 = 0xc6317ecff827ba89
After Key XOR: B1 = 0xcb317f3cbd400327, B2 = 0xc6317fecbd403322
After Permutation: B1 = 0xeae08c65659275e6, B2 = 0xe6e1ace4658265e3
Round 2 Difference: 0xc01208100101005
Active S-boxes in Round 2: [1, 4, 6, 9, 10, 12, 13, 15]

--- Round 3 ---
After S-box: B1 = 0xb5bdf6caca431abc, B2 = 0xbcb756b9caf3cab2
After Key XOR: B1 = 0xb5bdf6cacb605fdb, B2 = 0xbcb756b9cbd08fd5
After Permutation: B1 = 0xd4eef0c8db5b7fd3, B2 = 0xddec9999d9067fdc
Round 3 Difference: 0x9026951025d000f
Active S-boxes in Round 3: [1, 5, 6, 7, 9, 10, 11, 12, 13, 15]

Pair 6:
P1: 0x336d48e870fbc52c, P2: 0x336d48e770fbc523

--- Round 1 ---
After S-box: B1 = 0x22c09fbf1d8e6a36, B2 = 0x22c09fb11d8e6a32
After Key XOR: B1 = 0x23e3dad89425a7d9, B2 = 0x23e3dad69425a7dd
After Permutation: B1 = 0x24e7322f915cf6e8, B2 = 0x2ee7322f915df668
Round 1 Difference: 0xa00000000010080
Active S-boxes in Round 1: [2, 5, 15]

--- Round 2 ---
After S-box: B1 = 0x39b1233847a68cbf, B2 = 0x3bb1233847a08ccf
After Key XOR: B1 = 0x39b1221b02c10514, B2 = 0x3bb1221b02c70564
After Permutation: B1 = 0x86c915391132884, B2 = 0x87891579513aa84
Round 2 Difference: 0x14000404008200
Active S-boxes in Round 2: [3, 4, 7, 9, 13, 14]

--- Round 3 ---
After S-box: B1 = 0xdfc647a247723ff9, B2 = 0xdf1f47a14a7255f9
After Key XOR: B1 = 0xdfc647a246517a9e, B2 = 0xdf1f47a14b51109e
After Permutation: B1 = 0xdd4fde8e0891487f, B2 = 0xcd4e8c9e4a92691f
Round 3 Difference: 0x1001521042032160
Active S-boxes in Round 3: [2, 3, 4, 5, 7, 8, 10, 11, 12, 13, 16]

Pair 7:
P1: 0xc5024b06e0ba33e, P2: 0xc5024bf6e0ba331

--- Round 1 ---
After S-box: B1 = 0xd6ad39edcbde522b, B2 = 0xd6ad39e8cbde5227
After Key XOR: B1 = 0xd78e7c8a42759fc4, B2 = 0xd78e7c8f42759fc8
After Permutation: B1 = 0xdd8894ee8b1dcad9, B2 = 0xd78a94fe8b1dcad9
Round 1 Difference: 0xa02001000000000
Active S-boxes in Round 1: [10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0xff49bbfe706504, B2 = 0x1f5498bfe706504
After Key XOR: B1 = 0xff4898bb17ecaf, B2 = 0x1f548a8bb17ecaf
After Permutation: B1 = 0x3d3b522be606f59a, B2 = 0x3d3b5a2ae416f592
Round 2 Difference: 0x80102100008
Active S-boxes in Round 2: [1, 6, 7, 9, 11]

--- Round 3 ---
After S-box: B1 = 0x202ea33ebcdc8a45, B2 = 0x202ea535b97c8a43
After Key XOR: B1 = 0x202ea33ebdffcf22, B2 = 0x202ea535b85fcf24
After Permutation: B1 = 0x3370c943f7ed85fa, B2 = 0x7b30c853f7e48458
Round 3 Difference: 0x48400110000901a2
Active S-boxes in Round 3: [1, 2, 3, 5, 10, 11, 14, 15, 16]

Pair 8:
P1: 0xb11832242d4437dc, P2: 0xb118322b2d4437d3

--- Round 1 ---
After S-box: B1 = 0xe77f233930992106, B2 = 0xe77f233e30992102
After Key XOR: B1 = 0xe65c665eb932ece9, B2 = 0xe65c6659b932eced
After Permutation: B1 = 0xf35366cdf60f5790, B2 = 0xf95366ddf60e5790
Round 1 Difference: 0xa00001000010000
Active S-boxes in Round 1: [5, 10, 15]

--- Round 2 ---
After S-box: B1 = 0x82a2cc608cd8a14d, B2 = 0x84a2cc008cdba14d
After Key XOR: B1 = 0x82a2cd43c9bf28e6, B2 = 0x84a2cd23c9bc28e6
After Permutation: B1 = 0xd931313e4ce9c70a, B2 = 0xd92119b84ce9c70a
Round 2 Difference: 0x10288600000000
Active S-boxes in Round 2: [9, 10, 11, 12, 14]

--- Round 3 ---
After S-box: B1 = 0x427272b96b461d5, B2 = 0x43774ef96b461d5
After Key XOR: B1 = 0x427272b979724b2, B2 = 0x43774ef979724b2
After Permutation: B1 = 0x617d09da8481a5ba, B2 = 0x67bd29da8403e5ba
Round 3 Difference: 0x6c0200000824000
Active S-boxes in Round 3: [4, 5, 6, 12, 14, 15]

Pair 9:
P1: 0x8238e5719309ab49, P2: 0x8238e57e9309ab46

--- Round 1 ---
After S-box: B1 = 0xf32fba1742d45e94, B2 = 0xf32fba1b42d45e9c
After Key XOR: B1 = 0xf20cff70cb7f937b, B2 = 0xf20cff7ccb7f9373
After Permutation: B1 = 0xc1deac675fecdf53, B2 = 0xc3dcac675fecdfd3
Round 1 Difference: 0x202000000000080
Active S-boxes in Round 1: [2, 13, 15]

--- Round 2 ---
After S-box: B1 = 0x670b56c1a8b608a2, B2 = 0x620656c1a8b60802
After Key XOR: B1 = 0x670b57e2edd18109, B2 = 0x620657e2edd181a9
After Permutation: B1 = 0x45c2ad867b957528, B2 = 0x45c2ad0e7d855538
Round 2 Difference: 0x8806102010
Active S-boxes in Round 2: [2, 4, 6, 7, 9, 10]

--- Round 3 ---
After S-box: B1 = 0x9a6350fc1e4a1a3f, B2 = 0x9a6350db10faaa2f
After Key XOR: B1 = 0x9a6350fc1f695f58, B2 = 0x9a6350db11d9ef48
After Permutation: B1 = 0xb6aeea07c1286bed, B2 = 0xb5a3e31781256bcc
Round 3 Difference: 0x30d0910400d0021
Active S-boxes in Round 3: [1, 2, 5, 8, 10, 11, 13, 15]

Pair 10:
P1: 0x115730424e41b185, P2: 0x1157304d4e41b18a

--- Round 1 ---
After S-box: B1 = 0x77a12d939b97e7fa, B2 = 0x77a12d909b97e7f5
After Key XOR: B1 = 0x768268f4123c2a15, B2 = 0x768268f7123c2a1a
After Permutation: B1 = 0x3f0d3ce51028d848, B2 = 0x370f3cf51029c84a
Round 1 Difference: 0x802001000011002
Active S-boxes in Round 1: [1, 4, 5, 10, 13, 15]

--- Round 2 ---
After S-box: B1 = 0x28d026ba7d3f0f9f, B2 = 0x21d8268a7d346f95
After Key XOR: B1 = 0x28d0279938588634, B2 = 0x21d827a93853e63e
After Permutation: B1 = 0x6d449251f4a600c4, B2 = 0x6d57da52f69600c2
Round 2 Difference: 0x13480302300006
Active S-boxes in Round 2: [1, 6, 7, 9, 11, 12, 13, 14]

--- Round 3 ---
After S-box: B1 = 0xc09943a7895cdd69, B2 = 0xc0a105a38c4cdd63
After Key XOR: B1 = 0xc09943a7887f980e, B2 = 0xc0a105a38d6f9804
After Permutation: B1 = 0x9f529c1242afe403, B2 = 0xdc309c1240ada521
Round 3 Difference: 0x4362000002024122
Active S-boxes in Round 3: [1, 2, 3, 4, 5, 7, 13, 14, 15, 16]

=== Differential Attack Complete ===
```
