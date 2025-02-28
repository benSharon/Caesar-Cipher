# Caesar Cipher Command-Line Tool

## Description
This is a command-line tool for encrypting and decrypting text using the Caesar cipher. The tool supports both encryption with a given shift key and brute-force decryption.

## Features
- Encrypt or decrypt text using a shift key
- Perform brute-force decryption by trying all possible shifts
- Accept input as text or from a file

## Installation
Ensure you have Python installed on your system.

Clone the repository or download the files:
```sh
 git clone <repository-url>
 cd <repository-folder>
```

## Usage
Run the script using Python:
```sh
python caesar.py [OPTION]... [FILE or TEXT]...
```

### Options
- `--key <int>`: Specify the shift value for encryption/decryption
- `--bruteforce`: Perform brute-force decryption by trying all possible shifts

### Examples
Encrypt a text file with a shift of 3:
```sh
python caesar.py --key 3 input.txt
```

Decrypt a text using brute force:
```sh
python caesar.py --bruteforce "Khoor Zruog"
```

Encrypt direct text input with a shift of 5:
```sh
python caesar.py --key 5 "Hello World"
```

## Files
- `caesar.py`: Main script handling argument parsing and processing
- `methods.py`: Contains functions for Caesar cipher encryption and brute-force decryption

## Dependencies
This script relies on Python's standard libraries and requires no additional dependencies.

## License
This project is licensed under the MIT License.
