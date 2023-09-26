#Lista de aprovados

def achar_elemento(elem, arr):
    achou = False

    for i in range(len(arr)):
        if arr[i] == elem:
            achou = True
    return achou

candidatos = ["Lucas", "Roger", "Renato", "Yuri", "William"]

print("Bem vindo candidato!")
nome = input("Procure seu nome na lista de aprovados: ")

if achar_elemento(nome, candidatos):
    print("Parabéns, você foi aprovado " + nome)
else:
    print("Seu nome não foi encontrado " + nome)