alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def ceasar_cipher(word, rot):
    result = ''
    for char in word:
        if char.upper() not in alphabet:
            result += char
            continue
        result += char_upper_cipher(char, rot)
    return result


def char_upper_cipher(char, rot):
    char_upper = char.upper()
    index = alphabet.index(char_upper)
    index_alphabet = (index + rot) % len(alphabet)
    if char.isupper():
        return alphabet[index_alphabet]
    return alphabet[index_alphabet].lower()


def create_cipher_map(alphabet, rot):
    cipher_map = {}

    for index, c in enumerate(alphabet):
        cipher_map[c] = alphabet[(index % len(alphabet)) + rot]

    return cipher_map
