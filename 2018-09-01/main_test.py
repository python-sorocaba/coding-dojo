import pytest
from main import ceasar_cipher, create_cipher_map, char_upper_cipher


def test_ceaser_cipher_rot3_phrase():
    phrase = 'a ligeira raposa marrom saltou sobre o cachorro cansado'
    expected_phrase = 'd oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr'
    assert ceasar_cipher(phrase, rot=3) == expected_phrase



@pytest.mark.parametrize('word, rot, expected_word', (
    ('ABC', 3, 'DEF'),
    ('ABC', 4, 'EFG'),
    ('RAFAEL', 3, 'UDIDHO'),
    ('rafael', 3, 'udidho'),
    ('Rafael', 3, 'Udidho'),
    ('ABCDEF', 4, 'EFGHIJ'),
    ('a ligeira', 3, 'd oljhlud')
))
def test_ceaser_cipher(word, rot, expected_word):
    assert ceasar_cipher(word, rot=rot) == expected_word

def test_char_cipher():
    assert char_upper_cipher('A', 3) == 'D'

@pytest.mark.skip
def test_create_cipher_map_abc():
    assert create_cipher_map('ABCD', rot=1) == dict(A='B',B='C',C='D', D='A')
