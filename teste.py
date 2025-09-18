transformador = [+,-,*,/]
try:
    n = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    opc = int(input('0 = +\n1 = -\n2 = *\n3 = /\nDigite aque o numero: '))
except:
    print('caramba mn como tu e tao burro')
    
if n == 0 and n2 == 0 and opc == 4: print('ANIAMAL TU NAO CONSEGUE DIVIDIR 0 BURRO')

for i in range(0, 3, 1):
    if i == opc:
        a = transformador[i]
        print(f'O resultado e {n a n2}')
