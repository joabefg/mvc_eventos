from flask import Flask
from controllers.evento_controller import cadastrar

# Instancia a API
app = Flask(__name__)

# Cria a rota /evento
@app.route("/evento", methods=["GET","POST"])
def cadastrar_eventos():
    return cadastrar()

# Sobe o servidor
if __name__ == "__main__":
    app.run(debug=True)