def menu():
    try:
        menuu = int(input('1 = Algebra\n2 = Geometria\n3 = sair :(\nDigite aqui: '))
    except:
        print('O felo da puta escreve certo burro verme lixo horrivel')
    
    if menuu == 1:
        calculadora()
    elif menuu == 2:
        Geometria()

def calculadora():
    try:
        n = int(input('Numero 1: '))
        n2 = int(input('Numero 2: '))
        opc = int(input('0 = +\n1 = -\n2 = *\n3 = /\n4 = **\n5 = **0.5\nDigite aque o numero: '))
    except:
        print('caramba mn como tu e tao burro')
        
    if not (n == 0 or n2 == 0 and opc == 3):
        if opc == 0:
            print(n + n2)
        elif opc == 1:
            print(n - n2)
        elif opc == 2:
            print(n * n2)
        elif opc == 3:
            print(n / n2)
        elif opc == 4:
            print(n ** n2)
        elif opc == 5:
            print(n **0.5)
        dnv = str(input('Tu q dnv(s/n): '))
        if dnv == 's':
            calculadora()
        else:
            menu()
        
    print('ANIAMAL TU NAO CONSEGUE DIVIDIR 0 BURRO')

def Geometria():
    try:
        ops = int(input('1 = quadrado\n2 = retangulo\n3 = triangulo\n4 = circulo\n5 = trapezio\nDigite aq: '))
    except:
        print('Boa verme lixo')
        
    if ops == 1:
        b = int(input('Numero base: '))
        print(f'O resulado é {b * b}')
    elif ops == 2:
        b = int(input('Numero base: '))
        h = int(input('Numero altura: '))
        print(f'O resulado é {b * h}')
    elif ops == 3:
        b = int(input('Numero base: '))
        h = int(input('Numero altura: '))
        print(f'O resulado é {b * h / 2}')
    elif ops == 4:
        r = int(input('Numero do raio: '))
        print(f'O resulado é {(3.14*r)**2}')
    elif ops == 5:
        b = int(input('Numero base menor: '))
        bM = int(input('Numero base maior: '))
        h = int(input('Numero altura: '))
        print(f'O resulado é {(b + bM) * h / 2}')
    dnv = str(input('Quer dnv (s/n): '))
    if dnv == 's':
        Geometria()
    else:
        menu()

menu()
