from flask import Flask, render_template, request, redirect
import mysql.connector
import datetime

app = Flask(__name__)

# Aqui vão as minhas rotas.

# ROTA PARA A PÁGINA INICIAL
@app.route("/")
def pagina_principal():
    return render_template("index.html")

# ROTA PARA A PÁGINA DE CADASTRAR MENSAGEM
@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    # Peguei as informações vindas do formulário
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")
    data_hora = datetime.datetime.today()

    # CADASTRANDO AS INFORMAÇÕES NO BANCO DE DADOS
    # CIANDO A CONEXÃO
    conexao = mysql.connector.connect( host = "localhost",
                                      port =  3306,
                                      user = "root",
                                      password = "root",
                                      database = "dbFeedback")
    
    # O cursor será responsável por manipular o banco de dados
    cursor = conexao.cursor()

    # criando o SQL que será executado
    sql = """INSERT INTO tb_comentarios
                (nome, data_hora, comentario)
             VALUES
                (%s, %s, %s)"""
    
    valores=(usuario, data_hora, mensagem)

    # Executando o comando SQL 
    cursor.execute(sql, valores)

    # Confirmo a alteração
    conexao.commit()

    # Fecho a conexão com o banco
    cursor.close()
    conexao.close()

    # Redireciona para o index
    return redirect("/")

app.run(debug=True)