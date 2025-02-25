from flask import Flask
app = Flask(__name__)

# Aqui vão as minhas rotas.

@app.route("/")
def pagina_principal():
    return "SUPER PAGINA PRINCIPAL"

app.run(debug=True)