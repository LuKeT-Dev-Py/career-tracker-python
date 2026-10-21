from candidaturas.operacoes import carregar_candidaturas, exibir_candidatura, contar_entrevistas
import json
from configuracoes import CAMINHO_CONFERENCIA

try:
    candidaturas_recuperadas = carregar_candidaturas(CAMINHO_CONFERENCIA)
except FileNotFoundError:
    print(f'Arquivo não encontrado: {CAMINHO_CONFERENCIA}')
    print('Confira se o arquivo existe no caminho informado acima.')
except json.JSONDecodeError:
    print(f'Arquivo: {CAMINHO_CONFERENCIA}')
    print('O arquivo está vazio ou contém JSON inválido.')
    print('Confira o conteúdo antes de tentar novamente.')
else:
    em_entrevista2 = contar_entrevistas(candidaturas_recuperadas)
    print('')
    print(f'Total de candidaturas: {len(candidaturas_recuperadas)}')
    print(f'Candidaturas em entrevista: {em_entrevista2}\n')
    for n in candidaturas_recuperadas:
        exibir_candidatura(n['empresa'], n['status'], n['cargo'])