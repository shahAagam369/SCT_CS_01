# Caesar Cipher

A simple Python implementation of the Caesar Cipher encryption and decryption algorithm.

## Description

This program allows users to encrypt and decrypt text using the Caesar Cipher technique, one of the simplest and most widely known encryption techniques. The method is named after Julius Caesar, who used it to communicate with his generals.

The Caesar Cipher works by shifting each letter in the plaintext by a certain number of places down the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on.

## Features

- Encrypt any text message using a custom shift value (1-25)
- Decrypt previously encrypted messages using the same shift value
- Preserves case (uppercase/lowercase) of the original message
- Maintains non-alphabetic characters (spaces, numbers, punctuation) unchanged
- Simple command-line interface for easy interaction

## Requirements

- Python 3.x

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/shahAagam369/caesar-cipher.git
   cd caesar-cipher
   ```

2. No additional libraries are required as the program uses only Python's built-in functions.

## Usage

Run the program using Python:

```
python caesar_cipher.py
```

Follow the on-screen prompts to:
1. Choose between encryption and decryption
2. Enter the message to process
3. Specify the shift value (between 1 and 25)

### Example

```
=== Caesar Cipher Encryption/Decryption Tool ===

Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter your choice (1/2/3): 1
Enter the message to encrypt: Hello World
Enter the shift value (1-25): 3
Encrypted message: Khoor Zruog

Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit

Enter your choice (1/2/3): 2
Enter the message to decrypt: Khoor Zruog
Enter the shift value used for encryption (1-25): 3
Decrypted message: Hello World
```

## How It Works

The Caesar Cipher substitutes each letter in the plaintext with a letter that is a fixed number of positions down the alphabet. The mathematical formula used is:

For encryption: E(x) = (x + n) mod 26
For decryption: D(x) = (x - n) mod 26

Where:
- x is the position of the letter in the alphabet (0-25)
- n is the shift value
- mod 26 ensures the result wraps around the alphabet

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Julius Caesar, for inventing this cipher
- The many cryptography enthusiasts who keep ancient ciphers alive for educational purposes
