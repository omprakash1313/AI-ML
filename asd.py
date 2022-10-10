import sys


def decrypt(cipher, key):
    plain = ""
    for index in range(len(cipher)):
        if cipher[index].isalpha():

            if cipher[index].isupper():
                plain = plain + chr((ord(cipher[index]) - 64 - key) % 26 + 64)

        elif cipher[index].islower():
            plain = plain + chr((ord(cipher[index]) - 96 - key) % 26 + 96)

    else:
        plain = plain + cipher[index]

    return plain

in_filename = sys.argv[1]
key = int(sys.argv[2])
out_filename = sys.argv[3]

with open(in_filename, "r") as f:
    encrypted = f.read()

decrypted = decrypt(encrypted, key)

with open(out_filename, "w+") as f:
    f.write(decrypted)
