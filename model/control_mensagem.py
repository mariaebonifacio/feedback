from data.conexao import Conexao
import datetime

# 
class Mensagem:
    
    def cadastrar_mensagem(usuario, comentario):
        data_hora = datetime.datetime.today()

        # CADASTRANDO AS INFORMAÇÕES NO BANCO DE DADOS
        # Criando a conexão

        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular o banco de dados
        cursor = conexao.cursor()

        # Criando o SQL que será executado
        sql = """INSERT INTO tb_comentarios
                    (nome, data_hora, comentario)
                    VALUES
                    (%s, %s, %s)"""
        
        valores = (usuario, data_hora, comentario)

        # Executando o comando SQL
        cursor.execute(sql,valores)

        # Confirmo a alteração
        conexao.commit()

        # Fecho a conexão com o Banco
        cursor.close()
        conexao.close()

# ------------------------------------------------------------------------------

    def recuperar_mensagens():
        # Criar conexão
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular o banco de dados
        # Dictionary vai devolver as informações
        cursor = conexao.cursor(dictionary = True)

            # criando o SQL que será executado
        sql = """SELECT nome as usuario,
                            comentario as mensagem,
                            data_hora,
                            cod_comentario as codigo,
                            curtidas
                            FROM tb_comentarios"""
        
        # Executando o comando SQL 
        cursor.execute(sql)

        # Recuperando os dados e guardadndo em uma variável
        resultado = cursor.fetchall()

        # Fecho a conexão com o banco
        conexao.close()
       
        return resultado

# ------------------------------------------------------------------------------------

    def deletar_mensagens(codigo):
       # Criar conexão
        conexao = Conexao.criar_conexao()
        
        cursor = conexao.cursor()
        
        sql = "delete from tb_comentarios where cod_comentario = %s;"
        valores=(codigo,)
       
       # Executando o comando SQL 
        cursor.execute(sql,valores)
        
        # Comitando para gravar as alterações
        conexao.commit()
        
        cursor.close()
        
        # fechando conexão
        conexao.close()
        
# ----------------------------------------------------------
    def adicionar_curtidas(codigo):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()
        
        sql = "UPDATE tb_comentarios SET curtidas = curtidas + 1 WHERE cod_comentario = %s"
        valores = (codigo, )
        
        cursor.execute(sql, valores)
        conexao.commit()
        conexao.close()

    # ----------------------------------------------------------
    def adicionar_dislike(codigo):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()
        
        sql = "UPDATE tb_comentarios SET curtidas = curtidas - 1 WHERE cod_comentario = %s"
        valores = (codigo, )
        
        cursor.execute(sql, valores)
        conexao.commit()
        conexao.close()

    # ----------------------------------------------------------
        
    def recuperar_mensagens(nome):
        # Criar conexão
        conexao = Conexao.criar_conexao()

        # O cursor será responsável por manipular o banco de dados
        # Dictionary vai devolver as informações
        cursor = conexao.cursor(dictionary = True)

            # criando o SQL que será executado
        sql = """SELECT comentario 
                 FROM tb_comentarios 
                 WHERE nome = %s 
                 ORDER BY data_hora 
                 DESC LIMIT 1"""
        
        valores = (nome,)

        # Executando o comando SQL 
        cursor.execute(sql, valores)

        # Recuperando os dados e guardadndo em uma variável
        resultado = cursor.fetchone()

        # Fecho a conexão com o banco
        conexao.close()
       
        return resultado
        