# Cifra de César

Em criptografia, a Cifra de César, também conhecida como cifra de troca, código de César ou troca de César, é uma das mais simples e conhecidas técnicas de criptografia. É um tipo de cifra de substituição na qual cada letra do texto é substituída por outra, que se apresenta no alfabeto abaixo dela um número fixo de vezes. Por exemplo, com uma troca de três posições, A seria substituído por D, B se tornaria E, e assim por diante. O nome do método é em homenagem a Júlio César, que o usou para se comunicar com os seus generais.

O processo de criptografia de uma cifra de César é frequentemente incorporado como parte de esquemas mais complexos, como a cifra de Vigenère, e continua tendo aplicações modernas, como no sistema ROT13. Como todas as cifras de substituição monoalfabéticas, a cifra de César é facilmente decifrada e na prática não oferece essencialmente nenhuma segurança na comunicação.

Você precisa criar um algoritmo de cifra de césar que suporte diversos rotacionamentos de caracteres para criptografar a sua mensagem.

![cifra-cesar](../images/cifra-cesar.png)

# Exemplos

Com rotação de 3 caracteres:
```
Normal:  ABCDEFGHIJKLMNOPQRSTUVWXYZ
Cifrado: DEFGHIJKLMNOPQRSTUVWXYZABC

Normal:  Rafael
Cifrado: Udidho

Normal:  a ligeira raposa marrom saltou sobre o cachorro cansado
Cifrado: d oljhlud udsrvd pduurp vdowrx vreuh r fdfkruur fdqvdgr
```

Com rotação de 4 caracteres:
```
Normal: ABCDEF
Cifrado: EFGHIJ
```

etc.

# Desafio extra

Este desafio pode ser realizado durante ou fora do dojo de acordo com o tempo disponível que a gente terá ao final da "primeira fase" :wink:.

Crie um algoritmo que por força bruta consiga descriptografar mensagens cifradas, tentando mudar a rotação a cada iteração até encontrar texto legível.

Para automatizar mais ainda a descoberta podemos usar uma lista de palavras de um determinado idioma. Bons exemplos de lista de palavras podem ser vistos abaixo:

- [Random word generator- Python (Stack Overflow)](https://stackoverflow.com/questions/18834636/random-word-generator-python).
- [Dadoware](https://github.com/thoughtworks/dadoware)
- [Faker](https://github.com/joke2k/faker)

# Referências

- [Cifra de César - Wikipédia](https://pt.wikipedia.org/wiki/Cifra_de_C%C3%A9sar)
- [ROT13 - Wikipédia](https://pt.wikipedia.org/wiki/ROT13)
- [Site que "criptografa" mensagens - rot13.com](https://www.rot13.com/)
