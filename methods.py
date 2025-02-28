import string

def caesar_rotate(text, key):
    decrypted = []
    for char in text:
        if char == ' ':
            decrypted.append(char)

        # Skipping non-alphabet chars
        if char not in string.ascii_letters:
            continue

        if char.islower():
            lower_char_index = string.ascii_lowercase.index(char)
            decrypted.append(string.ascii_lowercase[(lower_char_index + key) % 26])
        elif char.isupper():
            upper_char_index = string.ascii_uppercase.index(char)
            decrypted.append(string.ascii_uppercase[(upper_char_index + key) % 26])
        else:
            decrypted.append(char)

    print(''.join(decrypted))


def caesar_bruteforce(ciphertext):
    print("--------------------------------------------------")
    for shift in range(1, 26):
        decrypted = []
        for char in ciphertext:
            if char == ' ':
                decrypted.append(char)

            # Skipping non-alphabet chars
            if char not in string.ascii_letters:
                continue

            if char.islower():
                decrypted.append(string.ascii_lowercase[(string.ascii_lowercase.index(char) + shift) % 26])
            elif char.isupper():
                decrypted.append(string.ascii_uppercase[(string.ascii_uppercase.index(char) + shift) % 26])
            else:
                decrypted.append(char)

        print(f"Shift {shift:2d}: {''.join(decrypted)}")
        print("--------------------------------------------------")
