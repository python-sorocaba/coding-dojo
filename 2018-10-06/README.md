# HASHADIQ - Hash

Neste problema, pede-se para armazenar, gerenciar e buscar por indivíduos definidos por um identificador único (inteiro) e pelas seguintes informações:

- Primeiro nome
- Último nome
- Data de nascimento
- Telefone

## Entrada

A entrada será feita por `add`, `del`, `info` e `query` descritos abaixo...

### add

O comando `add` recebe e armazena todos dados do individuo, e retorna erro se já existir individuo com mesmo identificador.

Sintaxe:
```
add <id> <first_name> <last_name> <birtday> <phone_number>
```

Saídas previstas:
- Caso de sucesso: Comando não retorna nada, apenas adiciona;
- Caso de erro: Exibe erro na quando a inserção de individuo tem um identificador duplicado (já cadastrado anteriormente).

### del

O comando `del` remove todos dados relacionados a um determinado identificador, e retorna erro se não existir individuo com o identificador fornecido.

Sintaxe:
```
del <id>
```

Saídas previstas:
- Caso de sucesso: Comando não retorna nada, apenas deleta;
- Caso de erro: Exibe erro caso o identificador solicitado não exista.

### info

O comando `info` imprime todos dados de um determinado identificador, e retorna erro se não existir individuo com o identificador fornecido.

Sintaxe:
```
info <id>
```

Saídas previstas:
- Caso de sucesso: Imprime todos os dados de um determinado identificador;
- Caso de erro: Exibe erro caso o identificador solicitado não exista.

### query

O comando `query` realiza uma busca nos indivíduos cadastrados. Conforme as seguintes tags de busca:

- fn: Primeiro nome
- ln: Ultimo nome
- bd: Data de nascimento
- pn: Telefone

Sintaxe:
```
query (<tag>:<valor>)+
```

Saídas previstas:
- Caso de sucesso: Retorna todos os identificadores (somente os ids) que respeitem os critérios da busca na ordem crescente;
- Caso de erro: Retorna uma linha vazia (quando nenhum identificador foi encontrado).

### exit

A execução é encerrada com o comando `exit`.

Sintaxe:
```
exit
```

# Exemplos

```
>>> add 123 Roberto Nascimento 01/01/1960 +55-21-0190-0190
>>> add 123 Joao Souza 11/10/2000 103-99
ID 123 ja cadastrado.
>>> add 09 Andre Matias 01/01/1970 +55-21-0190-0190
>>> add 222 Diogo Fraga 01/06/1967 +55-21-0190-0190
>>> add 99 Seu Barbosa 01/01/1960 +55-21-0190-0190
>>> add 100 Seu Beirada 01/01/1960 +55-21-9999-9999
>>> add 155 Andre Fortunato 02/01/1962 +55-21-0190-0190
>>> query bd:01/01/1960
99 100 123
>>> query bd:01/01/1960 fn:Seu
99 100
>>> query bd:01/01/1960 fn:Seu pn:+55-21-9999-9999
100
>>> info 100
Seu Beirada 01/01/1960 +55-21-9999-9999
>>> del 99
>>> info 99
ID 99 nao existente.
>>> del 99
ID 99 nao existente.
>>> query fn:XXX

>>> query bd:01/01/1960 fn:Seu
100
>>> exit
Bye bye!
```

# Dicas para manter sua sanidade mental

- Não tenha pressa, faça teste por teste, faça comando por comando, veja se funciona, depois passe para a implementação do próximo (baby steps!);
- Não se preocupe com entradas inválidas, respeite os exemplos e informe valores nos mesmos formatos demonstrados;
- Usem dicionários, não paga nada!
- Não é necessário persistir o dado! Podemos trabalhar com as informações em memória!

# Referência

- [HASHADIQ - Hash](https://br.spoj.com/problems/HASHADIQ/)
