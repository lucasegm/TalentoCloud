lista_frutas = ['melancia', 'banana', 'pera']
print(lista_frutas)
# Imprimirá: ['melancia', 'banana', 'pera']

lista_frutas[1], lista_frutas[2] = 'morango', 'abacaxi'
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi']
# Uma forma de alterar um indice, é atribuir a posição a outro elemento

lista_frutas = ['melancia', 'morango', 'abacaxi']
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi']
# o .append anexa um elemento a Array
lista_frutas.append('kiwi')
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi', 'kiwi']

lista_frutas = ['melancia', 'morango', 'abacaxi', 'kiwi']
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi', 'kiwi']
# a função .pop retira um elemento da array
lista_frutas.pop()
print(lista_frutas)
# Imprimirá: ['melancia', 'morango', 'abacaxi']