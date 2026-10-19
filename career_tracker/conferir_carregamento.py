from candidaturas.operacoes import carregar_candidaturas, exibir_candidatura, contar_entrevistas
import json

caminho = 'candidaturas_laboratorio.json'
try:
    candidaturas_recuperadas = carregar_candidaturas(caminho)
except FileNotFoundError:
    print(f'Arquivo não encontrado: {caminho}')
    print('Confira o nome do arquivo e a pasta de execução do terminal.')
except json.JSONDecodeError:
    print(f'Arquivo: {caminho}')
    print('O arquivo está vazio ou contém JSON inválido.')
    print('Confira o conteúdo antes de tentar novamente.')
else:
    em_entrevista2 = contar_entrevistas(candidaturas_recuperadas)
    print('')
    print(f'Total de candidaturas: {len(candidaturas_recuperadas)}')
    print(f'Candidaturas em entrevista: {em_entrevista2}\n')
    for n in candidaturas_recuperadas:
        exibir_candidatura(n['empresa'], n['status'], n['cargo'])