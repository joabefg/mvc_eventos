from datetime import datetime
class Evento:
    def __init__(self, nome, vagas, data):
        self.nome = nome
        self.vagas = vagas
        self.data = datetime.strptime(
            data, "%d/%m/%Y").date()

    def lotado(self):
        return self.vagas == 0

    def status(self): # agendado, realizado, hoje
        hoje = datetime.now().date()
        if hoje < self.data:
            return "agendado"
        elif hoje > self.data:
            return "realizado"
        else:
            return "hoje"

    def salvar(self, conexao):
        cursor = conexao.cursor()
        cursor.execute("""
        INSERT INTO evento (nome, vagas, data)
        VALUES (?,?,?)
        """, (self.nome, self.vagas, self.data))
        conexao.commit()