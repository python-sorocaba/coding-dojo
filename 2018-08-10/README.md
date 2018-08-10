# Palavras Primas

Um número primo é definido se ele possuir exatamente dois divisores: o número um e ele próprio. São exemplos de números primos: 

- 2
- 3
- 5
- 101
- 367
- 523

Neste problema, você deve ler uma palavra composta somente por letras [a-zA-Z]. Cada letra possui um valor específico, a vale 1, b vale 2 e assim por diante, até a letra z que vale 26. Do mesmo modo A vale 27, B vale 28, até a letra Z que vale 52.

Você precisa definir se cada palavra em um conjunto de palavras é prima ou não. Para ela ser prima, a soma dos valores de suas letras deve ser um número primo.

Exercício extraído e adaptado de: [http://dojopuzzles.com/problemas/exibe/palavras-primas/](http://dojopuzzles.com/problemas/exibe/palavras-primas/)

# Reconhecendo um número primo

- É um número natural menos 0 e 1
    - 1 não é um número primo, porque ele tem apenas um divisor que é ele mesmo
    - 0 não é um número primo, pois divisão por 0 não existe
- É um número positivo
- É divisível por 1 e por si mesmo
- Se o número for ímpar, TALVEZ seja primo, porém se for par não é primo, apenas o número 2
    - Todos os outros pares que não são o número 2 possuem pelo menos 3 divisores (1, ele mesmo e 2)
- Um número maior que 5 terminado em 5 não é primo
    - Todos os outros números terminados em 5 possuem pelo menos 3 divisores (1, ele mesmo e 5)

# Dica para manter a sanidade mental

Este exercício pode ser separado facilmente em dois dojos:

- Primeiro Dojo: Deveremos criar 'algo' que identifique se um número é primo ou não;
- Segundo Dojo: Identificar se uma palavra é prima ou não (que demandará pouquíssimo tempo).

... porém tudo depende da velocidade e tempo em que o dojo for realizado.

# Referências

- [Vídeo - NÚMEROS PRIMOS - Com saber se um Número é primo ou não](https://www.youtube.com/watch?v=TjAx7pHgxpo)
- [DojoPuzzles.com](http://dojopuzzles.com/problemas/exibe/palavras-primas/)
- [Números primos](https://www.somatematica.com.br/fundam/primos.php)

