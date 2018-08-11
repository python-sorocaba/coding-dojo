
def is_prime_number(number):
    if number == 1:
        return False
    elif number == 0:
        return False
    elif number < 0:
        return False
    elif number % 2 == 0 and number != 2:
        return False
    elif number % 10 == 5 and number > 5:
        return False
    elif number % 1 == 0 and number % number == 0:
        return True


def char_to_number(char):
    if char.isupper():
        return ord(char) - 38

    return ord(char) - 96


def sum_word(word):
    result = 0
    for char in word:
        result += char_to_number(char)
    return result


def is_word_prime(word):
    word_value = sum_word(word)
    return is_prime_number(word_value)
