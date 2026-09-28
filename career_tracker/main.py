from validacoes.status import validar_status
from validacoes.empresa import empresa_preenchida
from candidaturas.operacoes import exibir_candidatura


status_validos = ('Opções de status: enviada, entrevista, recusada \n')
empresa = input('Qual empresa você candidatou: ')
print('')
print(status_validos)
status = input('Qual status da candidatura: ').lower()

if empresa_preenchida(empresa):
    if validar_status(status):
        exibir_candidatura(empresa, status)
    else:
        print('Status invalido.')
else:
    print('Empresa invalida.')
