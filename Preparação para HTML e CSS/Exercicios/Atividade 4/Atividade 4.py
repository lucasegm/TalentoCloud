print("Bem vindo a nossa loja! Tivemos algumas alterações em nossos produtos!")

lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 
lista_produtos[1], lista_produtos[4] = 'rimel', 'cremes hidratantes'
lista_produtos.pop(7)
lista_produtos.append("gloss")
lista_produtos.append("cilios")
for i in range(len(lista_produtos)):
    print("Venha adquirir os produtos: {}.".format(lista_produtos[i]))
