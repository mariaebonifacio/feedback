from flask import Flask, render_template, request, redirect
import mysql.connector
import datetime
from data.conexao import Conexao
from model.control_mensagem import Mensagem 
from model.control_usuario import Usuario

app = Flask(__name__)

# Aqui vão as minhas rotas.

# ROTA PARA A PÁGINA INICIAL ------------------------------------
@app.route("/comentario")
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
def adicionar_curtidas(codigo):
    Mensagem.adicionar_curtidas(codigo)

    return redirect("/")


# adicionar dislike ------------------------------------

@app.route("/put/mensagens/adicionar/dislike/<codigo>")
def adicionar_dislike(codigo):
    Mensagem.adicionar_dislike(codigo)

    return redirect("/")


# CADASTRAR USUÁRIO ---------------------------------------------------
@app.route("/")
def cadastro_usuario():
    #Recuperar usuario
    usuarios = Usuario.recuperar_usuario()

    return render_template("cadastrarUsuario.html", usuarios = usuarios)

@app.route("/post/cadastrarusuario", methods = ["POST"])
def post_usuario():
    # Peguei as informações vinda do usuário
    login = request.form.get("login")
    nome = request.form.get("nome")
    senha = request.form.get("senha")

    # Cadastrando a mensagem usando a classe Mensagem
    Usuario.cadastro_usuario(login, nome, senha)
   
    # Rediriciona para o index
    return redirect("/")

app.run(debug=True)

app.run(debug=True)