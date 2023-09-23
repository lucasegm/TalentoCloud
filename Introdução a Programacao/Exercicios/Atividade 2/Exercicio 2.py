rodas = int(input("Quantas rodas tem o veículo que deseja dirigir? "))

if rodas <= 3:
    print("Se inscreva para a Habilitação A.")
else:
    pessoas = int(input("Quantas pessoas acomodam o veículo? "))
    
    if pessoas <= 8:
        peso = float(input("Qual o peso do veículo? "))
        
        if peso <= 3500:
            print("Se inscreva para a Habilitação B")
        elif peso < 6000:
            print("Se inscreva para a Habilitação C")
        else:
            print("Se inscreva para a Habilitação E")
    else:
        print("Se inscreva para a Habilitação D")