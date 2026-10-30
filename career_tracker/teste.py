import unittest
from candidaturas.operacoes import resumir_candidaturas

class TestResumoCandidaturas(unittest.TestCase):
    def test_lista_vazia(self):
        obtido = resumir_candidaturas([])
        esperado = {"total": 0, "entrevistas": 0}
        self.assertEqual(obtido, esperado)

