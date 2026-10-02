from validacoes.status import validar_status, normalizar_status
from validacoes.empresa import empresa_preenchida, limpar_empresa
from candidaturas.operacoes import exibir_candidatura
status_validos = ('Opções de status: enviada, entrevista, recusada \n')

empresa = input('Qual empresa você candidatou: ')
print('')
print(status_validos)
status = input('Qual status da candidatura: ')

status = normalizar_status(status)
empresa = limpar_empresa(empresa)

if not empresa_preenchida(empresa):
    print("Empresa inválida.")
elif not validar_status(status):
    print("Status inválido.")
else:
    exibir_candidatura(empresa, status)
