import mysql.connector

class Conexao:

    def criar_conexao():
        # CIANDO A CONEXÃO
        conexao = mysql.connector.connect( host = "localhost",
                                        port =  3306,
                                        user = "root",
                                        password = "root",
                                        database = "dbFeedback")
        return conexao