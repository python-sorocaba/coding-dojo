# Cheque por Extenso

Apesar de o volume de cheques emitidos tenha diminuído drasticamente nos últimos anos, principalmente devido a popularização dos cartões de crédito e débito, eles ainda são utilizados em muitas compras, especialmente a de valores altos. E para auxiliar no seu preenchimento, vários estabelecimentos possuem máquinas que dado o valor da compra, preenchem o cheque com o seu valor por extenso.

Desenvolva um programa que dado um valor monetário, seja retornado o valor em reais por extenso.

# Exemplos

- 15415,16 -> quinze mil quatrocentos e quinze reais e dezesseis centavos
- 0,05 -> cinco centavos
- 2,25 -> dois reais e vinte e cinco centavos

# Dica para manter a sanidade mental

Não devemos nos preocupar (a priori):

- Números inválidos
    - Letras
    - Números com ponto ao invés de vírgula)
    - Números com mais de 2 dígitos após a vírgula. Ex: 1,956
    - Números inteiros (sem uso de vírgula). Ex: 10
- Números muito grandes (na casa dos milhões, trilhões e etc)

Vamos sempre nos preocupar com números no formato: XXXXX,XX

Posteriormente a gente se preocupa com os outros (se der tempo) :wink:

# Referência

- [DojoPuzzles.com - Cheque por Extenso](http://dojopuzzles.com/problemas/exibe/cheque-por-extenso/)
- [Escrever números por extenso](http://www.languagesandnumbers.com/como-contar-em-portugues-brasil/pt/por-bra/)
