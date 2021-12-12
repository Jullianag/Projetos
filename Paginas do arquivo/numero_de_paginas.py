from PySimpleGUI import PySimpleGUI as sg
import PyPDF2
import os


class PaginasPdf:
    def __init__(self):
        sg.theme('Reddit')

        layout = [
            [sg.Text('Quantas páginas tem o seu PDF?')],
            [sg.Input(key='caminho'), sg.FileBrowse('procurar', key='botao')],
            [sg.Button('mostrar')],
            [sg.Output(key='texto', size=30)],
            [sg.Button('limpar'), sg.Button('sair')],
        ]

        self.janela = sg.Window('Páginas', layout)

    def start_window(self):
        try:
            while True:
                eventos, valores = self.janela.read()
                botao = valores['botao']

                # caso o usuário feche o programa
                if eventos == sg.WIN_CLOSED or eventos == 'sair':
                    break
                elif eventos == 'mostrar':
                    with open(botao, 'rb') as arquivo_pdf:
                        leitor = PyPDF2.PdfFileReader(arquivo_pdf)
                        num_paginas = leitor.getNumPages()
                        print(f'Este arquivo tem {num_paginas} páginas.')

                elif eventos == 'limpar':
                    tela = ''
                    self.janela.find_element('texto').Update(tela)
                    self.janela.find_element('caminho').Update(tela)

        except TypeError as e:
            print()


wn = PaginasPdf()
wn.start_window()