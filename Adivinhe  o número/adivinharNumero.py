from random import randint
from time import sleep


def tamanho(txt):
    tam = len(txt)
    print('-' * tam)
    print(f'{txt}')
    print('-' * tam)
    print()


msg = 'Adivinhe o número de 1 a 100 que estou pensando!'
tamanho(msg)
sleep(0.5)
rand_num = randint(1, 100)
numero = 0
tentativas = 0

while numero is not rand_num:
    try:
        numero = int(input('Escolha um número: '))
        tentativas += 1
        if numero > rand_num:
            print(f'QUASE! É uma valor menor que {numero}.')
        elif numero < rand_num:
            print(f'QUASE! É uma valor maior que {numero}.')
        else:
            print()
            print('Processando...')
            sleep(1.5)
            print(f'Parabéns!! Você acertou em {tentativas} tentativas.')
    except ValueError as e:
        sleep(0.7)
        print(f'\033[31mVocê não digitou um número! {e} \033[m')
        print()