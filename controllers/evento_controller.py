from flask import render_template, request

def cadastrar():
    # acessar /evento
    if request.method == "GET":
        return render_template("formulario.html")
    # enviar o form para /evento
    if request.method == "POST":
        # aqui iria a lógica de salva.
        return {"mensagem": "Criado!"}, 201