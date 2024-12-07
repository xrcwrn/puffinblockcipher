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

## Differential Propogation
```
Initial Difference (Delta_0): 0xf00000000

Pair 1: P1 = 0x7d43ef51340d764d, P2 = 0x7d43ef5e340d764d

--- Round 1 ---
After S-box: Difference = 0xc00000000
Active S-boxes: [8]
  S-box 8: Active bits = b2, b3
Probability for Round 1: 0.250000
After Key XOR: Difference = 0xc00000000
After Permutation: Difference = 0x200000000000080
Bit Propagation Mapping:
  From S-box 8:
    b2 -> S14(b2)
    b0 -> S2(b0)

--- Round 2 ---
After S-box: Difference = 0x800000000000060
Active S-boxes: [1, 14]
  S-box 1: Active bits = b1, b2
  S-box 14: Active bits = b3
Probability for Round 2: 0.062500
After Key XOR: Difference = 0x800000000000060
After Permutation: Difference = 0x4000204
Bit Propagation Mapping:
  From S-box 1:
    b3 -> S6(b3)
    b2 -> S2(b2)
  From S-box 14:
    b3 -> S0(b3)

--- Round 3 ---
After S-box: Difference = 0xf000b03
Active S-boxes: [0, 2, 6]
  S-box 0: Active bits = b0, b1
  S-box 2: Active bits = b0, b1, b3
  S-box 6: Active bits = b0, b1, b2, b3
Probability for Round 3: 0.015625
After Key XOR: Difference = 0xf000b03
After Permutation: Difference = 0x1008000041001162
Bit Propagation Mapping:
  From S-box 0:
    b1 -> S3(b1)
    b2 -> S0(b2)
  From S-box 2:
    b1 -> S6(b1)
    b3 -> S1(b3)
    b1 -> S15(b1)
  From S-box 6:
    b1 -> S2(b1)
    b0 -> S13(b0)
    b2 -> S1(b2)
    b3 -> S7(b3)

--- Round 4 ---
After S-box: Difference = 0xb00f00003a003d8d
Active S-boxes: [0, 1, 2, 3, 6, 7, 12, 15]
  S-box 0: Active bits = b0, b2, b3
  S-box 1: Active bits = b3
  S-box 2: Active bits = b0, b2, b3
  S-box 3: Active bits = b0, b1
  S-box 6: Active bits = b1, b3
  S-box 7: Active bits = b0, b1
  S-box 12: Active bits = b0, b1, b2, b3
  S-box 15: Active bits = b0, b1, b3
Probability for Round 4: 0.000015
After Key XOR: Difference = 0xb00f00003a003d8d

=== Differential Attack Complete ===
Total Probability of 4 Rounds: 0.000000003725
```
## Differential Attack 4 Round
Testing Key Guess: 0b100

Testing Key Guess: 0b101

Testing Key Guess: 0b110

Testing Key Guess: 0b111

Testing Key Guess: 0b1000

Testing Key Guess: 0b1001

Testing Key Guess: 0b1010

Testing Key Guess: 0b1011

Testing Key Guess: 0b1100

Testing Key Guess: 0b1101
Matched Key: 0b1101

=== Found Key: 0b1101 ===


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
Designed for resource-constrained environments such as IoT, RFID, and embedded systems.

Provides confidentiality and integrity for real-time message exchanges.

Easily implemented on resource-limited platforms like smart cards and wearables.

We developed a secure chat application using PUFFIN.
![image](https://github.com/user-attachments/assets/0b138b07-87cb-43c8-973e-1b47723c0e50)
