import argparse
import os.path
import sys

from methods import caesar_rotate, caesar_bruteforce


PROG = "python caesar.py"
DESCRIPTION = "Caesar cipher command-line tool"
USAGE = f"{PROG} [OPTION]... [FILE or TEXT]..."
EPILOG = """
Example of usage:
    python caesar.py --key KEY <file>
    python caesar.py --key KEY "cipher or plaintext"
    python caesar.py --bruteforce <file>
    python caesar.py --bruteforce "cipher text"
    
"""


def main():
    parser = argparse.ArgumentParser(
        prog=PROG,
        formatter_class=argparse.RawTextHelpFormatter,
        usage=USAGE,
        epilog=EPILOG
    )

    parser.add_argument("input", nargs='?', help="text or file")
    parser.add_argument("--key", type=int, help="shift value for encryption/decryption")
    parser.add_argument("--bruteforce", action="store_true", help="bruteforce decryption")

    args = parser.parse_args()

    if args.input and os.path.isfile(args.input):
        with open(args.input, 'r') as f:
            text = f.read()
    else:
        text = args.input or sys.stdin.read()

    if args.key is not None:
        caesar_rotate(text, args.key)
    if args.bruteforce:
        caesar_bruteforce(text)



if __name__ == "__main__":
    main()