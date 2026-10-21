import unittest
from app import app

class TestFuncional(unittest.TestCase):
    def setUp(self):
        self.cliente = app.test_client()

    def test_render_form(self):
        resposta = self.cliente.get("/evento")
        self.assertEqual(resposta.status_code, 200)

unittest.main()