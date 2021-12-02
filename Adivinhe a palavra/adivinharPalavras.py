from time import sleep

palavraSecreta = 'playstation'
digitadas = []
tentativas = 10

print('Adivinhe a palavra secreta!!\n')

while True:

    if tentativas <= 0:
        print('Você perdeu!!!')
        break

    letra = input('Digite uma letra: ').lower().strip()
    if len(letra) > 1:
        sleep(0.4)
        print('Preciso de apenas UMA letra.')
        continue
    if letra.isdigit():
        sleep(0.4)
        print('Por favor, digite apenas LETRAS.')
        continue

    digitadas.append(letra)

    if letra in palavraSecreta:
        sleep(0.4)
        print(f'\033[1;95mLegal! A letra "{letra}" exite na palavra.\033[m')
        sleep(0.4)
    else:
        sleep(0.4)
        print(f'\033[1;31mA letra "{letra}" digitada não existe na palavra :(\033[m')

    palavra_temporaria = ''

    for letra_secreta in palavraSecreta:
        if letra_secreta in digitadas:
            palavra_temporaria += letra_secreta
        else:
            palavra_temporaria += '_'

    if palavra_temporaria == palavraSecreta:
        sleep(0.4)
        print('\033[1;92mPARABENS! Você encontro a resposta!!!\033[m')
        sleep(0.4)
        print(f'A palavra secreta era "\033[1;93m{palavraSecreta}\033[m".')
        break
    else:
        sleep(0.4)
        print(f'Status da palavra secreta: {palavra_temporaria}')

    if letra not in palavraSecreta:
        tentativas -= 1

    sleep(0.4)
    print(f'Você ainda tem \033[1;96m{tentativas}\033[m chances.')
    print()