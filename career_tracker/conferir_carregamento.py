from candidaturas.operacoes import carregar_candidaturas, exibir_candidatura, contar_entrevistas

caminho = 'candidaturas_laboratorio.json'
try:
    candidaturas_recuperadas = carregar_candidaturas(caminho)
except FileNotFoundError:
    print('O arquivo não existe.')
else:
    em_entrevista2 = contar_entrevistas(candidaturas_recuperadas)
    print('')
    print(f'Total de candidaturas: {len(candidaturas_recuperadas)}')
    print(f'Candidaturas em entrevista: {em_entrevista2}\n')
    for n in candidaturas_recuperadas:
        exibir_candidatura(n['empresa'], n['status'], n['cargo'])