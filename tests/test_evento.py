import unittest
from models.evento import Evento

class TestEvento(unittest.TestCase):

    def test_criar_evento(self):
        evento =  Evento(
            "Festival de Música", 100, "20/10/2026")
        self.assertEqual(
            evento.nome, "Festival de Música")
        self.assertEqual(
            evento.vagas, 100)
        
    def test_evento_nao_lotado(self):
        evento =  Evento(
                "Festival de Música", 100, "20/10/2026")
        self.assertFalse(evento.lotado())

    def test_evento_lotado(self):
        evento =  Evento(
                "Festival de Música", 0, "20/10/2026")
        self.assertTrue(evento.lotado())

    def teste_status_hoje(self):
        evento = Evento("Show", 10, "19/10/2026")
        self.assertEqual(evento.status(), "hoje")

    def teste_status_agendado(self):
        evento = Evento("Show", 10, "20/10/2026")
        self.assertEqual(evento.status(), "agendado")

    def teste_status_realizado(self):
        evento = Evento("Show", 10, "18/10/2026")
        self.assertEqual(evento.status(), "realizado")