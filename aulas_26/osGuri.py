contas = []

def criar_conta():
    nome = input("Nome da conta: ")
    senha = input("Senha: ")

    if procurar(nome):
        print("Conta já existe!")
        return

    conta = {
        "nome": nome,
        "senha": senha,
        "saldo": 0
    }

    contas.append(conta)
    print("Conta criada com sucesso!")

def entrar():
    nome = input("Qual o nome da sua conta: ")
    senha = input("Qual a senha: ")

    for conta in contas:
        if conta["nome"] == nome and conta["senha"] == senha:
            print(f"Bem vindo {nome}")
            conta_logada(nome)
            return

    print("Nome ou senha incorretos!")

def conta_logada(nome):
    while True:
        try:
            executar = int(input(
                "\nO que você quer fazer:\n"
                "1 - Depositar\n"
                "2 - Sacar\n"
                "3 - Ver saldo\n"
                "4 - Sair\n"
            ))
        except ValueError:
            print("Digite apenas números!")
            continue

        if executar == 1:
            depositar(nome)
        elif executar == 2:
            sacar(nome)
        elif executar == 3:
            ver(nome)
        elif executar == 4:
            print("Saindo da conta...")
            break
        else:
            print("Opção inválida!")

def depositar(nome):
    try:
        dinheiro = int(input("Quanto deseja depositar: "))
    except ValueError:
        print("Digite um valor válido!")
        return

    for conta in contas:
        if conta["nome"] == nome:
            conta["saldo"] += dinheiro
            print("Depósito realizado com sucesso!")
            return

def sacar(nome):
    try:
        dinheiro = int(input("Quanto deseja sacar: "))
    except ValueError:
        print("Digite um valor válido!")
        return

    for conta in contas:
        if conta["nome"] == nome:
            if conta["saldo"] >= dinheiro:
                conta["saldo"] -= dinheiro
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
            return

def ver(nome):
    for conta in contas:
        if conta["nome"] == nome:
            print(f"Saldo atual: {conta['saldo']}")
            return

def procurar(nome):
    for conta in contas:
        if conta["nome"] == nome:
            return True
    return False

def menu():
    while True:
        try:
            executar = int(input(
                "\n1 - Criar conta\n"
                "2 - Entrar\n"
                "3 - Sair\n"
            ))
        except ValueError:
            print("Digite apenas números!")
            continue

        if executar == 1:
            criar_conta()
        elif executar == 2:
            entrar()
        elif executar == 3:
            print("Encerrando programa...")
            break
        else:
            print("Opção inválida!")

menu()
