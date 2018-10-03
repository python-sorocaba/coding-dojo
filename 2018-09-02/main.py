
def number_to_text(number):
    unit = {
        0: 'sem valor real',
        1: 'um real',
        2: 'dois reais',
        3: 'três reais',
        4: 'quatro reais',
        5: 'cinco reais',
        6: 'seis reais',
        7: 'sete reais',
        8: 'oito reais',
        9: 'nove reais',
    }
    tens = {
        10: 'dez reais',
        11: 'onze reais',
        12: 'doze reais',
        13: 'treze reais',
        14: 'quatorze reais',
        15: 'quinze reais',
        16: 'dezesseis reais',
        17: 'dezessete reais',
        18: 'dezoito reais',
        19: 'dezenove reais',
    }
    deca = {
        20: 'vinte',
        30: 'trinta',
        40: 'quarenta',
        50: 'cinquenta',
        60: 'sessenta',
        70: 'setenta',
        80: 'oitenta',
        90: 'noventa',
    }

    if number < 10:
        return unit[number]

    elif number < 20:
        return tens[number]

    elif number < 100:
        return deca[number]
