#!/usr/bin/env python3                                                                                                      

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

# Given IV
iv = bytearray.fromhex("ffeeddccbbaa00112233445566778899")
# Given Plaintext
plainText = "Welcome to UWE"
# Given Ciphertext (Hex)
given_cipher_hex = bytearray.fromhex("05e620629887d1cbb6a400a6a01b22fa")

# Load the text file
textFile = open("WordList.txt", "r")

# Loop for brute forcing and length maintaining
for key in textFile.read().splitlines():
    if len(key) < 16:
       key = key.ljust(16, '*')
    elif len(key) == 16:
       key = key
    else:
       key = key.ljust(24, '*')

    # Encrypt the message
    cipher = AES.new(key=bytearray(key, encoding='utf-8'), mode=AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(plainText.encode('utf-8'), AES.block_size))

    derived_cipher_hex = ciphertext
    if (given_cipher_hex == derived_cipher_hex):
        print("The key is: ",(key))
        break
    else:
        print("Checking: ",(key))
        continue