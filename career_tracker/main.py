import sys
from validacoes.status import validar_status, normalizar_status
from validacoes.empresa import empresa_preenchida, limpar_empresa
from candidaturas.operacoes import exibir_candidatura, tratar_lista, verificar_alteracao, selecao_valida
status_validos = ('Opções de status: enviada, entrevista, recusada \n')
empresas_a_cadastrar = 1
empresas_cadastradas = []
if not tratar_lista(empresas_cadastradas):
    print('Nenhuma empresa foi cadastrada.')  

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
            if selecao_valida(alteracao, len(empresas_cadastradas)):
                indice = alteracao - 1
            else:
                print('Digite um valor valido para quantidade de vagas cadastradas.')
                continue
            break
        except ValueError:
            print('Digite um valor inteiro valido.')
            continue
    valores_validos = ['Empresa', 'Cargo', 'Status']
    print(f'Valores validos, {valores_validos}')
    oq_alterar = input('Qual valor deseja alterar?: ').strip().lower()
    valor = verificar_alteracao(oq_alterar)

    if valor == 1:
        print(empresas_cadastradas[indice]['empresa'].capitalize())
        while True:
            nova_empresa = input('Qual empresa deseja por no lugar: ')
            nova_empresa = limpar_empresa(nova_empresa)
            if not empresa_preenchida(nova_empresa):
                print("Empresa inválida. Tente novamente.")
                continue
            else:
                empresas_cadastradas[indice]['empresa'] = nova_empresa
                break

    if valor == 2:
        print(empresas_cadastradas[indice]['cargo'].capitalize())
        while True:
            while True:
                novo_cargo = input('Digite o novo cargo para essa empresa: ').strip()
                if novo_cargo == '':
                    print('Cargo inválido. Tente novamente.')
                    continue
                else:
                    break
            empresas_cadastradas[indice]['cargo'] = novo_cargo
            break            

    if valor == 3:
        while True:
            print(status_validos)
            novo_status = input('Qual status da candidatura: ')
            novo_status = normalizar_status(novo_status)
            
            if not validar_status(novo_status):
                print("Status inválido. Tente novamente.")
                continue
            else:
                empresas_cadastradas[indice]['status'] = novo_status
                break

    if not valor:
        print('Valor invalido.')
        continue

print('')
print(f'Status inválidos informados: {contador}')
