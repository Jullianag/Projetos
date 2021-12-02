from time import sleep

print('O cão é o melhor amigo do homem.')
sleep(1.0)


perguntas = {
    '1° Pergunta': {
        'pergunta': 'Que raça tem aspecto leonino, '
                    'com pelagem abundante e espessa, orelhas separadas '
                    'e língua azulada?',

        'Resposta': {
            'a': 'Lasha Apso',
            'b': 'Husky Siberiano',
            'c': 'Chow Chow',
            'd': 'Pequinês',
        },
        'resposta_correta': 'c',
    },
    '2° Pergunta': {
        'pergunta': 'O cão Snoopy foi inspirado em qual raça de cachorro?',

        'Resposta': {
            'a': 'Cocker Spainel',
            'b': 'Dogue Alemão',
            'c': 'Beagle',
            'd': 'Yorkshire',
        },
        'resposta_correta': 'c',
    },
    '3° Pergunta': {
            'pergunta': 'Marley, do livro e filme (Marley e Eu), é um legítimo:',

            'Resposta': {
                'a': 'Labrador',
                'b': 'Pit Bull',
                'c': 'Bull Terrier',
                'd': 'Pinscher',
            },
            'resposta_correta': 'a',
        },
}
print()

resp_correta = 0

for pk, pv in perguntas.items():
    print(f'{pk}: \n{pv["pergunta"]}')
    sleep(1.0)

    print()
    for ok, ov in pv['Resposta'].items():
        print(f'{ok}. {ov}')

    resp_usuario = str(input('\nSua resposta: ')).strip().lower()
    sleep(0.6)
    print()

    if resp_usuario == pv['resposta_correta']:
        print('\033[1;32mResposta Correta!\033[m')
        resp_correta += 1
        sleep(0.6)

    else:
        print('\033[1;31mResposta Errada!\033[m')
        sleep(0.6)

print()

quantidade_perguntas = len(perguntas)
porcentagem = resp_correta / quantidade_perguntas * 100

print('RESULTADO FINAL')
print(f'Total de acertos: {resp_correta}')
print(f'Você obteve {porcentagem:.2f}% de acertos.')