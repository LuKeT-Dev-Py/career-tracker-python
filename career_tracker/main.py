from modulos import *


def gravar_alteracoes(candidaturas):
    try:
        salvar_candidaturas(candidaturas, caminho=CAMINHO_CANDIDATURAS)
    except OSError as erro:
        print(f'Não foi possível salvar a alteração: {erro}')
        raise SystemExit(1) from None


status_validos = ('Opções de status: enviada, entrevista, recusada \n')
empresas_a_cadastrar = 1
empresas_cadastradas = []
try:
    empresas_cadastradas = carregar_candidaturas(CAMINHO_CANDIDATURAS)
except FileNotFoundError:
    print('Nenhum arquivo de candidaturas ainda. Você pode começar um cadastro.')
    empresas_cadastradas = []

except json.JSONDecodeError:
    print(f'Arquivo: {CAMINHO_CANDIDATURAS}')
    print('O arquivo está vazio ou contém JSON inválido.')
    print('Confira o conteúdo antes de tentar novamente.')
    raise SystemExit(1) from None
except (EstruturaCandidaturasInvalida, OSError, UnicodeError) as erro:
    print(f'Não foi possível ler {CAMINHO_CANDIDATURAS}: {erro}')
    raise SystemExit(1) from None
else:
    resumo = resumir_candidaturas(empresas_cadastradas)
    print("\n=== Candidaturas recuperadas ===")
    if resumo['total'] == 0:
        print('Nenhuma candidatura cadastrada.')
            
    print(f'Total de candidaturas: {resumo['total']}')
    print(f'Candidaturas em entrevista: {resumo['entrevistas']}\n')
    for n in empresas_cadastradas:
        exibir_candidatura(n['empresa'], n['status'], n['cargo'])

if not tratar_lista(empresas_cadastradas):
    print('Nenhuma empresa foi cadastrada.')  

menu = ('1 - Cadastrar',
        '0 - Continuar sem cadastrar')
while True:
    print("\n=== Menu ===")
    for opcao in menu:
        print(opcao)

    escolha = input("\nEscolha uma opção: ")
    try:
        escolha = int(escolha)
    except ValueError:
        print('Digite um valor inteiro valido!')
        continue
    if escolha == 1:
        break
    elif escolha == 0:
        if len(empresas_cadastradas) == 0:
            print('Sessão encerrada.')
            raise SystemExit(0)
        else:
            empresas_a_cadastrar = 2
            break
    else:
        print('Digite os valores 1 ou 0')
        continue

while empresas_a_cadastrar <= 1:

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
    gravar_alteracoes(empresas_cadastradas)
    empresas_a_cadastrar += 1

while True:
    print("\n=== Editar candidatura ===")
    n = 1
    for emprise in empresas_cadastradas:
        print(f'Candidatura: {n}')
        exibir_candidatura(emprise['empresa'],emprise['status'],emprise['cargo'])
        n += 1
        
    while True:
        print('0 - Sair')
        alteracao = input('Qual candidatura deseja alterar: ')

        try:
            alteracao = int(alteracao)
            if alteracao == 0:
                print('Sessão encerrada.')
                raise SystemExit(0)
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
                gravar_alteracoes(empresas_cadastradas)
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
            gravar_alteracoes(empresas_cadastradas)
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
                gravar_alteracoes(empresas_cadastradas)
                break

    if not valor:
        print('Valor invalido.')
        continue
