import pytest

from main import (
    is_prime_number, char_to_number, sum_word, is_word_prime
)


def test_one_is_not_prime():
    assert is_prime_number(1) is False


def test_zero_is_not_prime():
    assert is_prime_number(0) is False


def test_two_is_prime():
    assert is_prime_number(2) is True


def test_negative_number_is_not_prime():
    assert is_prime_number(-1) is False


def test_three_number_is_prime():
    assert is_prime_number(3) is True


@pytest.mark.parametrize('number', (4, 6, 10, 232))
def test_even_bigger_than_two_is_not_prime(number):
    assert is_prime_number(number) is False


@pytest.mark.parametrize('number', (15, 25, 55, 555))
def test_number_ending_in_five_bigger_than_five_is_not_prime(number):
    assert is_prime_number(number) is False


@pytest.mark.parametrize('number', (5, 101, 367, 523))
def test_number_is_prime(number):
    assert is_prime_number(number) is True


@pytest.mark.parametrize('number', (4, 6, 10, 232))
def test_number_is_not_prime(number):
    assert is_prime_number(number) is False


@pytest.mark.parametrize('number', (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997))
def test_prime_numbers_below_one_thousand(number):
    assert is_prime_number(number) is True


@pytest.mark.parametrize('char, expected', (
    ('a', 1),
    ('z', 26),
))
def test_lower_a_char_to_number(char, expected):
    assert char_to_number(char) == expected


@pytest.mark.parametrize('char, expected', (
    ('A', 27),
    ('Z', 52),
))
def test_upper_a_char_to_number(char, expected):
    assert char_to_number(char) == expected


@pytest.mark.parametrize('word, expected', (
    ('a', 1),
    ('aa', 2),
    ('aA', 28),
    ('AA', 54),
    ('Aa', 28),
    ('python', 98),
    ('p', 16)
))
def test_sum_word(word, expected):
    assert sum_word(word) == expected


@pytest.mark.parametrize('word, expected', (
    ('b', True),
    ('a', False),
    ('python', False)
))
def test_is_word_prime(word, expected):
    assert is_word_prime(word) is expected
