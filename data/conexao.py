import mysql.connector

class Conexao:

    def criar_conexao():
        
        # QUANDO USAR LOCAL: COLOCAR FALSE, QUANDO NÃO: COLOCAR TRUE.
        if False:
        # CIANDO A CONEXÃO
            conexao = mysql.connector.connect( host = "bdgodofredo-alexstocco-93db.b.aivencloud.com",
                                            port =  27974,
                                            user = "3ds",
                                            password = "banana",
                                            database = "db_feedback")

        else:
            # CIANDO A CONEXÃO
            conexao = mysql.connector.connect( host = "localhost",
                                            port =  3306,
                                            user = "3ds",
                                            password = "banana",
                                            database = "db_feedback")
        return conexao