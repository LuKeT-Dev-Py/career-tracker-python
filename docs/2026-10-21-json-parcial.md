# Gravação JSON e leitura em conferência separada

Registro de 21/10/2026, versão `v0.0.6-prototype`.

## Resultado da análise

As mudanças são válidas como evolução do projeto de estudo: o programa grava candidaturas em JSON, o módulo de operações oferece leitura, há contagem de entrevistas e um script independente trata arquivo ausente e JSON inválido.

**O `main.py` já utiliza JSON para gravar. A leitura na inicialização ainda não foi integrada.** O principal inicia uma lista vazia e, ao concluir dois novos cadastros, substitui o arquivo de treino existente. A recomendação é publicar este marco com escopo parcial explícito e concluir o ciclo de recuperação antes de anunciar persistência completa no aplicativo.

A análise usou o commit [`233d3aecc7e9aa0ecb1eeef864139c5253f3cf77`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/233d3aecc7e9aa0ecb1eeef864139c5253f3cf77), comparado à publicação anterior [`51c74c3`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/51c74c363daef7df67187d392ac487ac9f75d5d5). Os nove arquivos Python do autor foram preservados; esta publicação atualiza documentação e histórico.

## Mudanças desde a v0.0.5

| Data | Commit do autor | Evolução registrada |
| --- | --- | --- |
| 13/10 | [`b88b71f`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/b88b71fcdd3cd42e94290115866944359242d459) | Implementações dos exercícios sobre dados. |
| 14/10 | [`86cee7f`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/86cee7ffa49433375a5d64fa3787a5ad6cbd1b52) | Contagem de candidaturas e entrevistas e módulo de importações. |
| 15/10 | [`5cf36bf`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/5cf36bf8c78e6c2e10e11c9c6cbf33a3000bfae9) | Leitura de JSON em um script de conferência, para integração posterior ao principal. |
| 16/10 | [`f3284bd`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/f3284bde1216432941f8761d7a8fabc20a179bb4) | Tratamento de arquivo ausente na conferência. |
| 19/10 | [`368ef54`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/368ef54b16694872dee731566414d6c8ba2e4834) | Tratamento de arquivo vazio ou JSON malformado. |
| 21/10 | [`233d3ae`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/233d3aecc7e9aa0ecb1eeef864139c5253f3cf77) | Caminho de conferência baseado na pasta do projeto. |

O código atual acrescenta `salvar_candidaturas()`, `carregar_candidaturas()` e `contar_entrevistas()` a `candidaturas/operacoes.py`, além de `conferir_carregamento.py`, `configuracoes.py` e `modulos.py`. O cadastro e a edição continuam presentes. O `import sys` sem uso e a impressão final inalcançável do contador foram removidos do principal.

## O que cada fluxo faz

### Programa principal

1. Importa as funções por `from modulos import *`.
2. Começa com `empresas_cadastradas = []`.
3. Exige o cadastro de duas candidaturas válidas.
4. Conta os registros e as entrevistas e mostra o resumo inicial.
5. Grava a lista em `candidaturas_treino.json`.
6. Permite editar empresa, cargo ou status e grava a lista novamente após uma atualização válida.
7. Mantém o laço de edição aberto, exibindo a listagem atualizada.

O nome passado a `salvar_candidaturas()` é relativo à pasta atual do terminal. Não existe chamada de `carregar_candidaturas()` no principal. Ter o arquivo no disco ainda não faz o programa reaproveitar seus dados ao reabrir.

### Conferência independente

`configuracoes.py` monta `CAMINHO_CONFERENCIA` com `os.path.dirname(os.path.abspath(__file__))` e o nome `candidaturas_laboratorio.json`.

`conferir_carregamento.py` carrega esse arquivo, trata `FileNotFoundError` e `json.JSONDecodeError` e, em caso de sucesso, mostra as contagens e as candidaturas. O tratamento não abrange a estrutura dos registros, falhas de permissão ou outros erros de leitura.

O arquivo de laboratório não está versionado. Em um clone novo, a mensagem de arquivo ausente é o comportamento esperado até preparar uma amostra. O README explica como copiar manualmente o arquivo de treino para o nome de laboratório para uma demonstração.

### Diferença entre os destinos

| Operação | Nome | Localização |
| --- | --- | --- |
| Gravação pelo principal | `candidaturas_treino.json` | Pasta atual do terminal. |
| Leitura pela conferência | `candidaturas_laboratorio.json` | Pasta de `configuracoes.py`. |

Mudar a pasta atual do terminal não altera o destino da conferência, mas altera o destino da gravação pelo principal. O ajuste de caminho de 21/10 é funcional no script em que foi aplicado; ainda falta estendê-lo ao fluxo principal com um caminho comum.

## Conceitos praticados

- `with open()` e fechamento automático do arquivo.
- Modos `w` para gravar e substituir conteúdo e `r` para ler.
- `json.dump()` e `json.load()` para converter entre dados Python e JSON.
- UTF-8, `ensure_ascii=False` e indentação na gravação.
- Diferença entre um arquivo de zero bytes, JSON malformado e uma lista vazia válida `[]`.
- `try`, `except` e `else` no fluxo de carregamento.
- Contagem de registros por status.
- Caminho do próprio arquivo em comparação à pasta atual do terminal.
- Separação entre uma função disponível em módulo e sua integração ao fluxo de entrada do aplicativo.

## Verificações executadas

O assistente executou **22 cenários: 17 confirmaram funcionalidades e 5 reproduziram limitações**. As entradas foram fornecidas ao programa original, com cópias da lista e do arquivo a cada pergunta. Os dados de teste ficaram em diretórios temporários; o script de conferência foi executado em subprocessos sobre uma cópia do código.

O principal permanece em um laço de edição. O procedimento de verificação pausou a execução na próxima pergunta depois de consumir cada sequência. Essa pausa não é um recurso de saída do aplicativo. Não foram substituídas as funções de gravação ou leitura, e os arquivos Python originais não foram editados.

### Funcionalidades confirmadas

Os cenários do principal usam como base Acme / Dev Python / enviada e Beta / Estágio / entrevista.

| Nº | Cenário | Resultado observado |
| --- | --- | --- |
| 1 | Abertura sem entrada. | Lista vazia, mensagem inicial e nenhum JSON criado antes do cadastro. |
| 2 | Cadastro de duas candidaturas. | Dois registros, resumo de 2 candidaturas e 1 entrevista e JSON igual à lista. |
| 3 | Editar empresa da segunda, tentando antes Enter e espaços. | Novas tentativas sem alteração prematura; valor Gamma gravado somente na segunda. |
| 4 | Editar cargo da primeira, tentando antes Enter e espaços. | Valores vazios rejeitados; Analista Python gravado somente na primeira. |
| 5 | Selecionar a segunda e informar ` STATUS ` e ` ENVIADA `. | Normalização do campo e do status; somente a segunda muda e o JSON acompanha. |
| 6 | Tentar `abc`, `0`, `-1`, `3` e `99` antes de uma escolha válida. | Texto e números fora da faixa recusados, sem alterar lista ou JSON; escolha 2 funciona. |
| 7 | Escolher o campo `outro`. | Campo recusado, sem alterar lista ou JSON; retorno à seleção. |
| 8 | Campos vazios e status `pendente` no cadastro e na edição. | Somente dados válidos são incluídos ou atualizados; tentativas inválidas preservam o estado salvo. |
| 9 | Alterar empresa, cargo e dois status na mesma execução. | Cada alteração afeta o registro escolhido; listagem e JSON refletem o resultado final. |
| 10 | Salvar e recuperar empresa São João e cargo Estágio. | Acentos e dados preservados em UTF-8. |
| 11 | Salvar e recuperar `[]`. | Lista vazia gravada e recuperada corretamente. |
| 12 | Contar listas com zero, uma e duas entrevistas. | Totais 0, 1 e 2, respectivamente. |
| 13 | Conferência com arquivo ausente. | Mensagem orienta o caminho; encerramento sem traceback. |
| 14 | Conferência com arquivo de zero bytes. | `JSONDecodeError` tratado com mensagem. |
| 15 | Conferência com conteúdo `{invalido`. | `JSONDecodeError` tratado com mensagem. |
| 16 | Conferência válida a partir da pasta do projeto e de outra pasta. | Mesmo arquivo localizado e mesma saída: 2 candidaturas, 1 entrevista e dados completos. |
| 17 | Conferência de `[]`. | Total de candidaturas e entrevistas igual a zero. |

### Limitações reproduzidas

| Nº | Situação | Resultado observado | Ajuste sugerido |
| --- | --- | --- | --- |
| 18 | JSON interpretável contendo candidatura sem `status`. | `KeyError` não tratado na contagem. | Validar lista, dicionários, chaves e valores antes de utilizar os dados. |
| 19 | Abrir o principal com JSON de uma execução anterior e cadastrar dois novos registros. | A lista inicia vazia; o conteúdo anterior é substituído pelos novos registros. | Carregar antes do cadastro e preservar os registros recuperados ao salvar. |
| 20 | Comparar gravação do principal com destino da conferência. | Arquivos e regras de caminho diferentes. | Definir um único destino para o fluxo integrado. |
| 21 | Mudar um status para entrevista após o resumo inicial. | A listagem e o JSON mudam; o resumo não é recalculado. | Recalcular as contagens quando forem exibidas após alterações. |
| 22 | Criar um diretório chamado `candidaturas_treino.json` no destino. | `IsADirectoryError` encerra o principal durante a gravação. | Tratar falhas de arquivo e informar quando uma alteração não foi salva. |

O cenário 19 foi conferido com um registro antigo fictício, seguido de nova execução no mesmo diretório. Antes do novo cadastro, o arquivo ainda continha o registro antigo e a lista estava vazia. Ao concluir dois cadastros, o JSON passou a conter somente Acme e Beta.

Os nove arquivos Python foram compilados com Python 3.12.14 sem avisos de sintaxe. Essas verificações são evidências dos cenários analisados, não uma suíte permanente incluída no repositório ou exercícios adicionais atribuídos ao autor.

## Devo esperar o JSON no main.py para publicar?

Vale registrar agora as mudanças implementadas e verificadas. A versão `v0.0.6-prototype` documenta gravação no principal e leitura em conferência independente, com integração pendente. Os seis commits de código do autor continuam compondo esse histórico.

Para uma divulgação centrada em salvar e continuar as candidaturas depois de reabrir o aplicativo, a recomendação é aguardar a leitura na inicialização e os critérios abaixo. A gravação de um arquivo já existe; a continuidade entre sessões ainda precisa ser concluída.

### Prioridade antes de anunciar a persistência concluída

1. Escolher um arquivo e um caminho comuns para salvar e carregar, independentes da pasta atual do terminal.
2. Carregar os registros antes de decidir cadastrar ou editar e permitir consultá-los sem exigir dois cadastros novos.
3. Salvar edições e novos registros preservando os dados recuperados.
4. Tratar arquivo ausente e JSON inválido no principal; um erro de leitura não deve levar à substituição silenciosa do histórico por novos dados.
5. Conferir o ciclo completo: cadastrar e salvar, encerrar, reabrir, listar os mesmos registros, editar, encerrar e recuperar a edição em outra execução.

### Ajustes seguintes

- Conferir a estrutura e os valores dos registros carregados.
- Informar falhas de gravação e o estado dos dados que não puderam ser salvos.
- Atualizar o resumo após alterações de status.
- Criar menu com saída, cadastro flexível e exclusão.
- Revisar `import *`, contador de tentativas, laços redundantes e capitalização dos nomes.

Esses itens descrevem a próxima etapa para o autor implementar. A análise e a publicação não antecipam essa implementação.

## Organização desta publicação

- Novo marco `v0.0.6-prototype` no README e no CHANGELOG.
- README com execução do principal, conferência independente, destinos dos arquivos e limites de recuperação.
- Este registro com comparação, seis commits do autor, evidências e critérios para a integração.
- Preservação da `v0.0.5-prototype` na [branch histórica](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.5-prototype), a partir de seu [commit de publicação](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/51c74c363daef7df67187d392ac487ac9f75d5d5).
- Um novo commit de documentação sobre o código já publicado, sem reescrever os commits do autor ou alterar os nove arquivos Python.

Os registros anteriores, demais branches e imagem original continuam disponíveis. Os JSONs temporários usados nas verificações não fazem parte da publicação.
