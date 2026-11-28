"""
Caesar Cipher
-------------
"""

import string
ALPHABET = string.ascii_uppercase


def encrypt(text: str, shift: int) -> str:
    """Encrypt text using a Caesarcipher."""
    result = []
    shift = shift % 26
    for char in text.upper():
        if char in ALPHABET:
            new_index = (ALPHABET.index(char) + shift) % 26
            result.append(ALPHABET[new_index])
        else:
            result.append(char)
    return " ".join(result)

def decrypt(text: str, shift: int) -> str:
    """Decrypt text that was encrypted with the given Caesar shift."""
    return encrypt(text, -shift)
