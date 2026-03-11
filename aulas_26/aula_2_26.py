def irmas():
    idade = []
    
    for _ in range(3):
        try:
            idade.append(int(input("Qual a idade: ")))
        except ValueError:
            print("Digite apenas numeros")
            return
    
    for irma in idade:
        if irma >= 100 or irma <= 5:
            print("Idade invalida")
            return
        
    idade.remove(max(idade))
    idade.remove(min(idade))
    return idade

resposta = irmas()
print(resposta)
