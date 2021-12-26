from PySimpleGUI import PySimpleGUI as sg
import projeto_catalogo


class TabelaSQL:
    def __init__(self):

        layout1 = [
            [sg.Text(('Cadastro de eletrônicos'), pad=(130, 1))],
            [sg.Text((''), pad=(130, 1))],
            [sg.Text('Nome:'), sg.Input(key='nome', size=(20, 1), pad=(10, 1))],
            [sg.Text('Marca:'), sg.Input(key='marca', size=(20, 1), pad=(9, 1))],
            [sg.Text('Valor:'), sg.Input(key='valor', size=(20, 1), pad=(15, 1))],
            [sg.Text('id:'), sg.Input(key='id', size=(20, 1), pad=(35, 1))],
            [sg.Text('Resultado: ', pad=(5, 10))],
            [sg.Output(key='texto', size=(50, 15))],
            [sg.Button('Inserir'), sg.Button('Limpar'), sg.Button('Atualizar'), sg.Button('Excluir'),
             sg.Button('Listar'), sg.Button('Sair')]
        ]

        self.janela = sg.Window('Tabela Eletrônicos', layout1)

    def start_window(self):
        try:
            while True:
                eventos, valores = self.janela.read()

                nome = valores['nome']
                marca = valores['marca']
                valor = valores['valor']
                id = valores['id']

                # caso o usuário feche o programa
                if eventos == sg.WIN_CLOSED or eventos == 'Sair':
                    break
                elif eventos == 'Inserir':
                    projeto_catalogo.inserir(nome, marca, valor)
                    print(f'O produto "{nome}" foi inserido!')

                elif eventos == 'Atualizar':
                    projeto_catalogo.atualizar(nome, valor, marca, id)
                    print('Produto atualizado!')

                elif eventos == 'Excluir':
                    projeto_catalogo.excluir(id)
                    print(f'Produto excluído!')

                elif eventos == 'Listar':
                    print('Id   Produto    Marca   Valor')
                    print()
                    projeto_catalogo.listar()

                elif eventos == 'Limpar':
                    tela = ''
                    self.janela.find_element('texto').Update(tela)
                    self.janela.find_element('nome').Update(tela)
                    self.janela.find_element('marca').Update(tela)
                    self.janela.find_element('valor').Update(tela)
                    self.janela.find_element('id').Update(tela)

        except TypeError as e:
            print()


jn = TabelaSQL()
jn.start_window()