from PySimpleGUI import PySimpleGUI as sg


class ImcPython:
    def __init__(self):
        sg.theme('LightBrown1')
        layout1 = [
            [sg.Text('Nome:'), sg.Input(key='paciente', size=(20, 1), pad=(29, 1))],
            [sg.Text('Peso (Kg)'), sg.Input(key='peso', size=(20, 1), pad=(10, 1))],
            [sg.Text('Altura (m)'), sg.Input(key='altura', size=(20, 1), pad=(10, 1))],
            [sg.Text('Resultado: ', pad=(5, 10))],
            [sg.Output(key='texto', size=30)],
            [sg.Button('Calcular'), sg.Button('Reiniciar'), sg.Button('Sair')]
        ]

        self.janela = sg.Window('Calculadora de IMC', layout1)

    def calcula_imc(self, peso, altura):

        imc = peso / (altura ** 2)

        if imc <= 18.5:
            return 'Abaixo do peso.'
        elif 18.6 <= imc <= 24.9:
            return 'Peso ideal.'
        elif 25.0 <= imc <= 29.9:
            return 'Levemente acima do peso.'
        elif 30.0 <= imc <= 34.9:
            return 'Obesidade grau I.'
        elif 35.0 <= imc <= 39.9:
            return 'Obesidade grau II.\n(Severa)'
        elif imc >= 40:
            return 'Obesidade grau .\n(Mórbida)'

    def start_window(self):
        try:
            while True:
                eventos, valores = self.janela.read()

                nome = valores['paciente']
                peso = float(valores['peso'])
                altura = float(valores['altura'])
                imc = peso / (altura ** 2)

                # caso o usuário feche o programa
                if eventos == sg.WIN_CLOSED or eventos == 'Sair':
                    break
                elif eventos == 'Calcular':
                    print(f'Paciente: {nome}')
                    print(f'Seu imc é: {imc:.2f}')
                    print('Status: ', self.calcula_imc(peso, altura))

                elif eventos == 'Reiniciar':
                    tela = ''
                    self.janela.find_element('texto').Update(tela)
                    self.janela.find_element('paciente').Update(tela)
                    self.janela.find_element('peso').Update(tela)
                    self.janela.find_element('altura').Update(tela)
        except TypeError as e:
            print()


jn = ImcPython()
jn.start_window()