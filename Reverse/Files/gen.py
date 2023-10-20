def encrypte_c(text):
    encrypted_text = ''
    key1 = 0b1101101
    key2 = 5

    for char in text:
        encrypted_char = ord(char) ^ key1
        encrypted_char = (encrypted_char << key2) | (encrypted_char >> (8 - key2))
        encrypted_char = (encrypted_char + 42) % 256
        binary_representation = bin(encrypted_char)[2:]
        binary_representation = binary_representation.zfill(8)
        inverted_binary = ''.join('1' if bit == '0' else '0' for bit in binary_representation)
        encrypted_text += inverted_binary + ' '

    return encrypted_text



'''
Fonction de chiffrement du flag.
'''