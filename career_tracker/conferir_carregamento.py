from candidaturas.operacoes import carregar_candidaturas, exibir_candidatura, contar_entrevistas, resumir_candidaturas
import json
from configuracoes import CAMINHO_CONFERENCIA

def executar_conferencia():
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
        resumo = resumir_candidaturas(candidaturas_recuperadas)
        print('')
        if resumo['total'] == 0:
            print('Nenhuma candidatura cadastrada.')
            
        print(f'Total de candidaturas: {resumo['total']}')
        print(f'Candidaturas em entrevista: {resumo['entrevistas']}\n')
        for n in candidaturas_recuperadas:
            exibir_candidatura(n['empresa'], n['status'], n['cargo'])
            
if __name__ == "__main__":
    executar_conferencia()