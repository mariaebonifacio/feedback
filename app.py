from flask import Flask, render_template, request, redirect
import mysql.connector
import datetime
from data.conexao import Conexao
from model.control_mensagem import Mensagem 

app = Flask(__name__)

# Aqui vão as minhas rotas.

# ROTA PARA A PÁGINA INICIAL ------------------------------------
@app.route("/")
def pagina_principal():
    mensagens = Mensagem.recuperar_mensagens()
    return render_template("index.html", mensagens = mensagens)


# ROTA PARA A PÁGINA DE CADASTRAR MENSAGEM -------------------------
@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    
    # Peguei as informações vindas do formulário
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    # Cadastrando a mensagem usando a classe Mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)

    # Redireciona para o index
    return redirect("/")

# DELETAR MENSAGENS ----------------------------------

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagens(codigo)
    return redirect("/")

# adicionar curtidas ------------------------------------

@app.route("/put/mensagens/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    
    return redirect("/")

app.run(debug=True)

# dislike -----------------------------------------------

