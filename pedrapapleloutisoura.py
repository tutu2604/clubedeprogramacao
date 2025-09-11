#tralalelo tralala esteve aq...
import random

dinheiro = 100

def cara_ou_coroa():
    global dinheiro
    opc = ['pedra', 'papel', 'tesoura']
    numero = random.randint(0,2)
    try:
        numero2 = str(input('Pedra, Papel ou Tisoura\nEssa partida vale 5 rs\nDigite aq: '))
    except:
        print('Coloca um numero valido lx')

    if numero2 == 'papel' and opc[numero] == 'pedra' or numero2 == 'papel' and opc[numero] == 'pedra' or numero2 == 'pedra' and opc[numero] == 'tisoura':
        print(f'Vc ganhou verme {opc[numero]}\n')
        dinheiro += 5
        print(dinheiro)
        cara_ou_coroa()
    elif numero2 == opc[numero]:
        print(f'Empate {opc[numero]}\n')
        cara_ou_coroa()
    else:
        print(f'Vc perdeu lx {opc[numero]}\n')
        dinheiro -= 5
        print(dinheiro)
        cara_ou_coroa()

cara_ou_coroa()
