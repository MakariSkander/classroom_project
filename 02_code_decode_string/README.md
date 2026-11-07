# 🔐 Code / Decode String

C++ console program that encodes a text and decodes it back.

## How it works

- **Encoding:** each character is turned into a group of 8 letters. For each bit of the character set to 1, a letter between `a` and `h` (one letter per bit position) is placed in the group. The other positions get a random letter between `i` and `z`. The 8 positions are then shuffled randomly.
- **Decoding:** the program builds a histogram of the letters in each group. If a letter between `a` and `h` is present, the matching bit is set to 1. Bit shifting rebuilds the original character.

## Tech

- C++ (`std::vector`, bit operations)
- Microsoft Visual Studio

## Run

Open `Corriger_session2.sln` in Visual Studio, then build and run (Ctrl + F5).
