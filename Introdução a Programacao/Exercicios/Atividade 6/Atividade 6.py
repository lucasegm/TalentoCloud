def obter_idade_atual(ano_nascimento):
    ano_atual = 2022
    idade = ano_atual - ano_nascimento
    return idade

def main():
    while True:
        nome = input("Digite seu nome completo: ")
        if nome.isalpha():
            break
        else:
            print("Nome inválido. Insira apenas letras.")

    while True:
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Ano de nascimento fora do intervalo válido.")
        except ValueError:
            print("Ano de nascimento inválido. Insira um número válido.")

    idade = obter_idade_atual(ano_nascimento)
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")

if __name__ == "__main__":
    main()