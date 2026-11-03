import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

from validacoes.status import validar_status


class EstruturaCandidaturasInvalida(ValueError):
    """O JSON foi lido, mas não representa uma lista de candidaturas."""

def exibir_candidatura(empresa, status, cargo):
    print(f'Empresa: {empresa.capitalize()} | Cargo: {cargo} | Status: {status.capitalize()}')

def tratar_lista(lista):

    if lista:
        return True
    else:
        return False

def verificar_alteracao(alteracao):

    if alteracao == 'empresa':
        return 1
    elif alteracao == 'cargo':
        return 2
    elif alteracao == 'status':
        return 3
    else:
        return False

def selecao_valida(numero, quantidade):
    
    if numero <= quantidade and numero > 0:
        return True
    else:
        return False

def salvar_candidaturas(lista, caminho):
    destino = Path(caminho)
    temporario = None
    try:
        with NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=destino.parent,
            prefix=f".{destino.name}.", suffix=".tmp", delete=False,
        ) as arquivo:
            temporario = Path(arquivo.name)
            json.dump(lista, arquivo, ensure_ascii=False, indent=2)
        # Só substitui a versão anterior depois que a gravação terminou.
        os.replace(temporario, destino)
        temporario = None
    finally:
        if temporario is not None:
            temporario.unlink(missing_ok=True)

def contar_entrevistas(lista):
    contador = 0
    for dic in lista:
        if dic['status'] == 'entrevista':
            contador += 1
        else:
            continue
    return contador

def carregar_candidaturas(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        recuperado = json.load(arquivo)

    if not isinstance(recuperado, list):
        raise EstruturaCandidaturasInvalida("O arquivo deve conter uma lista de candidaturas.")
    for numero, candidatura in enumerate(recuperado, start=1):
        if not isinstance(candidatura, dict):
            raise EstruturaCandidaturasInvalida(f"A candidatura {numero} deve ser um objeto JSON.")
        for campo in ("empresa", "cargo", "status"):
            valor = candidatura.get(campo)
            if not isinstance(valor, str) or not valor.strip():
                raise EstruturaCandidaturasInvalida(
                    f"A candidatura {numero} precisa de um texto válido no campo '{campo}'."
                )
        if not validar_status(candidatura["status"]):
            raise EstruturaCandidaturasInvalida(f"A candidatura {numero} tem um status inválido.")
    return recuperado

def resumir_candidaturas(lista):
    quantia = len(lista)
    entrevistas = contar_entrevistas(lista)
    return {"total": quantia, "entrevistas": entrevistas}
