def xor_encrypt_decrypt(text, key='K'):
    return ''.join(chr(ord(c) ^ ord(key)) for c in text)
