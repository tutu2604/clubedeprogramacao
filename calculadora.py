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
        
    print('ANIAMAL TU NAO CONSEGUE DIVIDIR 0 BURRO')
calculadora()
