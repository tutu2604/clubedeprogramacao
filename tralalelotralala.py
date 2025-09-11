#tralalelo tralala esteve aq...

import random

dinheiro = 100

def cara_ou_coroa():
    global dinheiro
    opc = ['cara', 'coroa']
    numero = random.randint(0,1)
    try:
        numero2 = str(input('Escolha cara ou coroa\nEssa partida vale 5 rs\nDigite aq: '))
    except:
        print('Coloca um numero valido lx')
    
    if numero2 == opc[numero]:
        print('Parabens vc ganhou verme\n')
        dinheiro += 5
        print(f'{dinheiro}\n')
        cara_ou_coroa()
    else:
        print('Vc perdeu lx\n')
        dinheiro -= 5
        print(f'{dinheiro}\n')
        cara_ou_coroa()

cara_ou_coroa()
