nota = int(input("Qual foi a sua nota? "))

if nota < 4:
    print("Reprovado")
elif nota < 7:
    print("Em recuperação")
else:
    print("Aprovado")