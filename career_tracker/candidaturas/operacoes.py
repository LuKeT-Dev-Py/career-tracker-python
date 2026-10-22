import json

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
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False, indent=2)

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
    return recuperado

def resumir_candidaturas(lista):
    quantia = len(lista)
    entrevistas = contar_entrevistas(lista)
    return {"total": quantia, "entrevista": entrevistas}