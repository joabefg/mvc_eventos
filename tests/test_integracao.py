import unittest
import sqlite3
from models.evento import Evento

class TestIntegracaoEvento(unittest.TestCase):
    def setUp(self):
        self.conexao = sqlite3.connect(":memory:")
        cursor = self.conexao.cursor()
        cursor.execute("""
                CREATE TABLE IF NOT EXISTS evento (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    vagas INTEGER NOT NULL,
                    data DATE NOT NULL
                )
            """)
        self.conexao.commit()
        cursor.close()
        self.evento_base = Evento(
            "Show",100,"25/11/2026")

    def test_cadastro_evento(self):
        self.conexao.close()
        self.evento_base = None