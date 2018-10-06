import pytest
from main import number_to_text


@pytest.mark.parametrize('number,text', [
    (0, 'sem valor real'),
    (1, 'um real'),
    (2, 'dois reais'),
    (3, 'três reais'),
])
def test_unit_numbers(number, text):
    assert number_to_text(number) == text


@pytest.mark.parametrize('number,text', [
    (10, 'dez reais'),
    (11, 'onze reais'),
    (12, 'doze reais'),
    (13, 'treze reais'),
    (14, 'quatorze reais'),
    (15, 'quinze reais'),
    (16, 'dezesseis reais'),
])
def test_decimals_numbers(number, text):
    assert number_to_text(number) == text

@pytest.mark.parametrize('number,text', [
    (20, 'vinte'),
    (30, 'trinta'),
    (40, 'quarenta'),
    (50, 'cinquenta'),
    (60, 'sessenta'),
    (70, 'setenta'),
    (80, 'oitenta'),
    (90, 'noventa'),
])
def test_deca_numbers(number, text):
    assert number_to_text(number) == text
