# Projeto: Evitando o 13º Andar

Este é um projeto simples que consiste em imprimir os números de 1 a 20, representando os andares de um hotel, mas evitando o número 13, devido à superstição do dono do hotel.

#### Exemplo 1: Utilizando o laço for
Neste exemplo, usamos um laço for para iterar de 1 a 20 e imprimir os números dos andares do hotel, pulando o 13.

```python
numero = 21
for i in range(20):
    numero = numero - 1
    if numero == 13:
        continue
    print(numero)
```

#### Exemplo 2: Utilizando o laço while
Neste segundo exemplo, utilizamos um laço while para alcançar o mesmo resultado, ou seja, imprimir os números de 1 a 20, excluindo o número 13.

```python
i = 21
while i > 1:
    i = i - 1
    if i == 13:
        continue
    print(i)
```

#### Exemplo 3: Utilizando outro laço while
No terceiro exemplo, também usamos um laço while para resolver o problema, mantendo a lógica de imprimir os números dos andares, excluindo o 13.

```python
i = 20
while True:
    if i != 13:
        print(i)
    i -= 1
    if i < 1:
        break
```

Estes três exemplos demonstram diferentes maneiras de atingir o mesmo objetivo de evitar o 13º andar ao imprimir os números de 1 a 20, sendo uma aplicação prática de estruturas de repetição em Python. Além disso, os números são impressos em ordem decrescente, conforme solicitado no desafio.
