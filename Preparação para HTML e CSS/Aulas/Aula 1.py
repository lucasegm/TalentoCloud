#Arrays é uma forma de armazenar dados, pódendo ser strings, booleanos, int, float, outro array
# Chamamos de Indice o nome dos itens da lista
# Cada item da lista tem uma posição
# -------------------------------
# vendas = [100, 1500, 350, 270, 900]
# produtos = ["tv", "celular", "teclado", "mouse", "tablet"]
# print("Vendas do produto {} foram de {} unidades.".format(produtos[3], vendas[3]))
#---------------------------------------

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

