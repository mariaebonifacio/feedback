from flask import Flask, render_template, request, redirect, session
import mysql.connector
import datetime
from data.conexao import Conexao
from model.control_mensagem import Mensagem 
from model.control_usuario import Usuario


app = Flask(__name__)

app.secret_key = "maria123"

# Aqui vão as minhas rotas.

# ROTA PARA A PÁGINA INICIAL ------------------------------------
@app.route("/comentario")
def pagina_principal():
    if "usuario" in session:
        mensagens = Mensagem.recuperar_mensagens()
        return render_template("index.html", mensagens = mensagens)
    else:
        return redirect ("/login")


# ROTA PARA A PÁGINA DE CADASTRAR MENSAGEM -------------------------
@app.route("/post/mensagem", methods = ["POST"])
def post_mensagem():
    
    # Peguei as informações vindas do formulário
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    # Cadastrando a mensagem usando a classe Mensagem
    Mensagem.cadastrar_mensagem(usuario, mensagem)

    # Redireciona para o index
    return redirect("/comentario")


# DELETAR MENSAGENS ----------------------------------
@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagens(codigo)
    return redirect("/comentario")


# adicionar curtidas ------------------------------------
@app.route("/put/mensagens/adicionar/curtida/<codigo>")
def adicionar_curtidas(codigo):
    Mensagem.adicionar_curtidas(codigo)

    return redirect("/comentario")


# adicionar dislike ------------------------------------
@app.route("/put/mensagens/adicionar/dislike/<codigo>")
def adicionar_dislike(codigo):
    Mensagem.adicionar_dislike(codigo)

    return redirect("/comentario")


# página inicial ------------------------------------------------------------------------------------------------------------
@app.route("/")
def cadastro_usuario():
    #Recuperar usuario
    usuarios = Usuario.recuperar_usuario()

    return render_template("cadastrarUsuario.html", usuarios = usuarios)


# cadastrar usuário ----------------------------------------------------------------------------------------------------------
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


# PAGINA DE LOGIN -----------------------------------------------------------------------------------------------------------
@app.route("/pagina_login")
def pagina_login():
    return render_template("pagina_login.html")


# VERIFICAÇÃ DE LOGIN -----------------------------------------------------------------------------------------------------
@app.route("/post/logar", methods = ["POST"])
def post_logar():

    login = request.form.get("login")
    senha = request.form.get("senha")
    esta_logado = Usuario.logar(login,senha)

    if esta_logado:
        return redirect("/comentario")
    else:
        return redirect("/login")



# Login ------------------------------------------------------------------------------



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)