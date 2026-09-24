from validacoes.status import validar_status
from candidaturas.operacoes import exibir_candidatura


status_validos = ('Opções de status: enviada, entrevista, recusada \n')
empresa = input('Qual empresa você candidatou: ')
print('')
print(status_validos)
status = input('Qual status da candidatura: ').lower()

if validar_status(status):
    exibir_candidatura(empresa, status)
else:
    print('Erro')
