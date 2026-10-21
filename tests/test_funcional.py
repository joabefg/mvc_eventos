import unittest
from app import app

class TestFuncional(unittest.TestCase):
    def setUp(self):
        self.cliente = app.test_client()

    def test_render_form(self):
        resposta = self.cliente.get("/evento")
        print(resposta.data)
        self.assertEqual(resposta.status_code, 200)

    def test_envio_form(self):
        resposta = self.cliente.post("/evento",
                        data={
                            "nome": "formatura",
                            "vagas": 100,
                            "data": "20/12/2026"})
        self.assertEqual(resposta.status_code, 201)

if __name__ == "__main__":
    unittest.main()