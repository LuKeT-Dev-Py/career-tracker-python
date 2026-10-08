import sys
from validacoes.status import validar_status, normalizar_status
from validacoes.empresa import empresa_preenchida, limpar_empresa
from candidaturas.operacoes import exibir_candidatura, tratar_lista, verificar_alteracao
status_validos = ('Opções de status: enviada, entrevista, recusada \n')
empresas_a_cadastrar = 1
empresas_cadastradas = []

while empresas_a_cadastrar <= 2:
    while True:
        empresa = input('Qual empresa você candidatou: ')
        empresa = limpar_empresa(empresa)
        if not empresa_preenchida(empresa):
            print("Empresa inválida. Tente novamente.")
            continue
        else:
            break
    cargo = False
    while not cargo:
        q_cargo = input('Qual cargo irá trabalhar: ').strip()
        if q_cargo == '':
            print('Cargo inválido. Tente novamente.')
        else:
            cargo = q_cargo

    contador = 0
    while True:
        print('')
        print(status_validos)
        status = input('Qual status da candidatura: ')
        status = normalizar_status(status)

        if not validar_status(status):
            print("Status inválido. Tente novamente.")
            contador += 1
            continue
        else:
            break
    candidatura = {"empresa": '', "cargo": '', "status": ''}
    candidatura['empresa'] = empresa
    candidatura['cargo'] = cargo
    candidatura['status'] = status
    empresas_cadastradas.append(candidatura)
    empresas_a_cadastrar += 1

if tratar_lista(empresas_cadastradas):
    for emprise in empresas_cadastradas:
        exibir_candidatura(emprise['empresa'],emprise['status'],emprise['cargo'])
else:
    print('Nenhuma empresa foi cadastrada.')

while True:
    n = 1
    for emprise in empresas_cadastradas:
        print(f'Candidatura: {n}')
        exibir_candidatura(emprise['empresa'],emprise['status'],emprise['cargo'])
        n += 1
        
    while True:
        alteracao = input('Qual candidatura deseja alterar: ')
        try:
            alteracao = int(alteracao)
            break
        except ValueError:
            print('Digite um valor inteiro valido.')
            continue

    print('Valores validos, Empresa, Cargo, Status')
    oq_alterar = input('Qual valor deseja alterar?: ').strip().lower()
    valor = verificar_alteracao(oq_alterar)

    if valor == 1:
        alteracao -= 1
        print(empresas_cadastradas[alteracao]['empresa'].capitalize())
        alteracao += 1
    while True:
        nova_empresa = input('Qual empresa deseja por no lugar: ')
        nova_empresa = limpar_empresa(nova_empresa)
        if not empresa_preenchida(nova_empresa):
            print("Empresa inválida. Tente novamente.")
            continue
        else:
            empresas_cadastradas[alteracao]['empresa'] = nova_empresa
            break

    if valor == 2:
        # Proximo
        ...
    if valor == 3:
        # Proximo
        ...
    if not valor:
        # Proximo
        print('Valor invalido.')
        break

print('')
print(f'Status inválidos informados: {contador}')
