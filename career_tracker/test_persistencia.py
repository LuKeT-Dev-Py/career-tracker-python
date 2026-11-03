import json
from pathlib import Path
import shutil
import subprocess
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch

from candidaturas.operacoes import salvar_candidaturas


class TestPersistencia(unittest.TestCase):
    def setUp(self):
        pasta = TemporaryDirectory()
        self.addCleanup(pasta.cleanup)
        self.raiz = Path(pasta.name)
        self.projeto = self.raiz / "career_tracker"
        origem = Path(__file__).resolve().parent
        for arquivo in origem.rglob("*.py"):
            destino = self.projeto / arquivo.relative_to(origem)
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(arquivo, destino)
        self.arquivo = self.projeto / "candidaturas_treino.json"

    def rodar(self, *entradas):
        return subprocess.run(
            [sys.executable, "-B", "-X", "utf8", str(self.projeto / "main.py")],
            input="\n".join(entradas) + "\n" if entradas else "",
            text=True,
            encoding="utf-8",
            capture_output=True,
            cwd=self.raiz,
            timeout=5,
        )

    def test_cadastro_edicao_e_recuperacao_em_novas_execucoes(self):
        primeira = self.rodar("1", "São João", "Estágio", " ENVIADA ", "0")
        self.assertEqual(primeira.returncode, 0, primeira.stderr)
        self.assertIn("São João", self.arquivo.read_text(encoding="utf-8"))
        self.assertFalse((self.raiz / self.arquivo.name).exists())

        segunda = self.rodar(
            "1", "Beta", "Dev Python", "enviada",
            "1", "empresa", "Acme",
            "1", "cargo", "Estágio Python",
            "1", "status", " Entrevista ", "0",
        )
        self.assertEqual(segunda.returncode, 0, segunda.stderr)
        esperado = [
            {"empresa": "Acme", "cargo": "Estágio Python", "status": "entrevista"},
            {"empresa": "Beta", "cargo": "Dev Python", "status": "enviada"},
        ]
        salvo = self.arquivo.read_bytes()
        self.assertEqual(json.loads(salvo), esperado)

        terceira = self.rodar("0", "0")
        self.assertEqual(terceira.returncode, 0, terceira.stderr)
        self.assertIn("Candidaturas recuperadas", terceira.stdout)
        self.assertIn("Total de candidaturas: 2", terceira.stdout)
        self.assertIn("Candidaturas em entrevista: 1", terceira.stdout)
        self.assertIn("Empresa: Acme | Cargo: Estágio Python | Status: Entrevista", terceira.stdout)
        self.assertEqual(self.arquivo.read_bytes(), salvo)

    def test_primeiro_uso_sem_cadastro_nao_cria_arquivo(self):
        resultado = self.rodar("0")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertFalse(self.arquivo.exists())

    def test_lista_vazia_valida_e_preservada(self):
        self.arquivo.write_bytes(b"[]")
        resultado = self.rodar("0")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Total de candidaturas: 0", resultado.stdout)
        self.assertEqual(self.arquivo.read_bytes(), b"[]")

    def test_arquivo_invalido_encerra_sem_sobrescrever(self):
        casos = (
            (b"", "JSON inválido"),
            (b"{invalido", "JSON inválido"),
            (b"null", "lista de candidaturas"),
            (b"[1]", "objeto JSON"),
            (b'[{"empresa":"Acme","cargo":"Dev"}]', "campo 'status'"),
            (b'[{"empresa":"Acme","cargo":"Dev","status":"outro"}]', "status inválido"),
            (b"\xff", "Não foi possível ler"),
        )
        for conteudo, mensagem in casos:
            with self.subTest(conteudo=conteudo):
                self.arquivo.write_bytes(conteudo)
                resultado = self.rodar()
                self.assertEqual(resultado.returncode, 1)
                self.assertIn(mensagem, resultado.stdout)
                self.assertNotIn("Traceback", resultado.stderr)
                self.assertEqual(self.arquivo.read_bytes(), conteudo)

    def test_entrada_invalida_nao_altera_candidatura(self):
        salvo = b'[{"empresa":"Acme","cargo":"Dev","status":"enviada"}]'
        self.arquivo.write_bytes(salvo)
        resultado = self.rodar("texto", "4", "0", "2", "1", "outro", "0")
        self.assertEqual(resultado.returncode, 0, resultado.stderr)
        self.assertIn("Digite um valor inteiro", resultado.stdout)
        self.assertIn("Valor invalido.", resultado.stdout)
        self.assertEqual(self.arquivo.read_bytes(), salvo)

    def test_falha_na_substituicao_mantem_o_arquivo_anterior(self):
        self.arquivo.write_bytes(b"[]")
        with patch("candidaturas.operacoes.os.replace", side_effect=PermissionError("sem acesso")):
            with self.assertRaises(PermissionError):
                salvar_candidaturas([{"empresa": "Acme"}], self.arquivo)
        self.assertEqual(self.arquivo.read_bytes(), b"[]")
        self.assertFalse(list(self.projeto.glob(".*.tmp")))


if __name__ == "__main__":
    unittest.main()
