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