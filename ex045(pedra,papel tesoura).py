#jogo de pedra papel ou tesoura

from time import sleep
from random import randint

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('Suas opções \n [ 0 ] Pedra\n [ 1 ] Papel\n [ 2 ] Tesoura')
jogador = int(input('Qual é a sua jogada? '))
if jogador >= 3:
    print('Digite uma escolha existente!')
else:
    print('-=' * 11)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!')
    sleep(1)
    print(f'Você escolheu {itens[jogador]}\nO computador escolheu {itens[computador]}')
    if computador == 0:
        if jogador == 0:
            print(' EMPATE')
        elif jogador == 1:
            print('VOCÊ GANHOU')
        elif jogador == 2:
            print(' O COMPUTADOR GANHOU')
        else:
            print(' JOGADA INVALIDA')
    if computador == 1:
        if jogador == 0:
            print(' O COMPUTADOR GANHOU')
        elif jogador == 1:
            print(' EMPATE')
        elif jogador == 2:
            print('VOCÊ GANHOU')
        else:
            print(' JOGADA INVALIDA')
    if computador == 2:
         if jogador == 0:
            print('VOCÊ GANHOU')
         elif jogador == 1:
            print(' O COMPUTADOR GANHOU')
         elif jogador == 2:
            print(' EMPATE')
         else:
            print(' JOGADA INVALIDA')
    print('-=' * 16)
input('aperte enter para encerrar!')