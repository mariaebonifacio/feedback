from data.conexao import Conexao 
from hashlib import sha256
from flask import session

class Usuario:
    def cadastro_usuario(login, nome, senha):
       
        # Criando a conexão com o banco de dados
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor()

        # Criando o sql que será executado
        sql = """INSERT INTO tb_usuarios
                    (login, nome, senha)
                VALUES
                    (%s, %s, %s)"""
               
        valores = (login, nome, senha)
   
        # Executando o comnado sql
        cursor.execute(sql,valores)
   
        # Confirmo a alteração (commit serve para fixar a alteração)
        conexao.commit()
   
        # Fecho a conexao com o banco
        cursor.close()
        conexao.close()
   

    def recuperar_usuario():

        #Criar conexão
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular
        cursor = conexao.cursor(dictionary = True)

        # Criando o sql que será executado
        sql = "SELECT login, nome, senha  FROM tb_usuarios;"

        #Executando o comando sql
        cursor.execute(sql)        

        #Recuperando os dados e jogando em uma varialvel
        resultado = cursor.fetchall()

        #Fecho a conexão (como não ouve alteração não preciso do commit)
        conexao.close()

        return resultado
    
    def logar(login, senha):

        # ele vai criar uma unica lista com nome, usuario e senha

        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()

        sql = """SELECT login, nome FROM tb_usuarios 
                    WHERE login = %s
                    AND binary senha = %s"""
        
        valores = (login, senha)

        cursor.execute(sql,valores)

        # fetchone = ele sempre vai retornar só 1 (por causa da PRIMARY KEY -login)
        resultado = cursor.fetchone

        # if resultado - continuacao proxima aula
        if resultado: 
            session['usuario'] = resultado['login']
            session['nome_usuario'] = resultado['nome']
            return True
        else:
            return False