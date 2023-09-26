# Exercicio 1
def achar_elemento(elem, arr):
    achou = False
# o len é exclusivo do range, a fim de não limitar
    for i in range(len(arr)):
        if arr[i] == elem:
            achou = True

    if(achou == False):
        print("Não encontramos o nome: " + elem)
    else:
        print("Achamos o nome: " + elem)

nome = ["Lucas", "Arturo", "Karen", "Julia"]
achar_elemento("Maran", nome)

