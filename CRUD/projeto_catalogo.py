import pymysql.cursors
from contextlib import contextmanager


@contextmanager
def conectar():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='eletronicos',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conexao
    finally:
        conexao.close()


def inserir(nome, marca, valor):
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            sql = 'INSERT INTO eletronicos (nome, marca, valor) VALUES (%s, %s, %s)'
            cursor.execute(sql, (nome, marca, valor))
            conexao.commit()
            print('deu certo')


def excluir(id):
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            sql = 'DELETE FROM eletronicos WHERE id=%s'
            cursor.execute(sql, (id,))
            conexao.commit()


def atualizar(nome, valor, marca, id):
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            sql = 'UPDATE eletronicos SET nome=%s, valor=%s, marca=%s WHERE id=%s'
            cursor.execute(sql, (nome, valor, marca, id))
            conexao.commit()


def listar():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute('SELECT * FROM eletronicos ORDER BY id ASC LIMIT 100')
            resultado = cursor.fetchall()

            for linha in resultado:
                print(linha['id'], linha['nome'], linha['marca'], linha['valor'])


listar()