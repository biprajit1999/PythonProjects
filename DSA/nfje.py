from sympy import mod_inverse
import math


def multiplicative_cypher(text, mode, key):
    char_dict = {}
    cipher_message = ''
    for i in range(26):
        char_dict[chr(ord('a') + i)] = i
    key_list = list(char_dict.keys())
    inv_char_dict = dict(zip(char_dict.values(), char_dict.keys()))

    if mode == 'encrypt':
        if math.gcd(26, key) == 1:
            for char in text:
                if char in key_list:
                    new_index = (char_dict[char] * key) % 26
                    cipher_message = cipher_message + inv_char_dict[new_index]
                else:
                    cipher_message = cipher_message + char
        else:
            print('invalid key selected')

        return cipher_message.upper()

    if mode == 'decrypt':
        mult_inv = mod_inverse(key, 26)
        for char in text:
            if char in key_list:
                new_index = (char_dict[char] * mult_inv) % 26
                cipher_message = cipher_message + inv_char_dict[new_index]
            else:
                cipher_message = cipher_message + char

    return cipher_message.lower()


txt = str(input("Enter plain text: "))
txt = txt.lower()
key = int(input("Enter key: "))
mode = str(input("encrypt/decrypt: "))
encrypt_message = multiplicative_cypher(txt, mode, key)
print(encrypt_message)