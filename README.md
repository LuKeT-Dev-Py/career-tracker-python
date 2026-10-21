# Career Tracker

Projeto de estudo em Python para acompanhar candidaturas pelo terminal e registrar minha evolução em programação.

**Versão atual: `v0.0.6-prototype`, registrada em 21/10/2026.** O programa cadastra duas candidaturas, permite editar seus campos e grava os dados em JSON após o cadastro e as alterações. Um script separado lê um arquivo de laboratório e mostra os registros e as contagens.

**A recuperação automática ao abrir o programa ainda está pendente.** O `main.py` começa com uma lista vazia e sobrescreve `candidaturas_treino.json` depois de dois novos cadastros. O arquivo fica no disco, mas seus registros ainda não são reaproveitados pelo fluxo principal na próxima execução.

## O que funciona

- Cadastro de duas candidaturas por execução, com empresa, cargo e status.
- Mensagem inicial de lista vazia e listagem numerada dos registros.
- Edição de empresa, cargo e status somente na candidatura escolhida.
- Validação de empresa e cargo vazios, status inválido, escolha não numérica e número fora da faixa.
- Limpeza dos espaços nas extremidades; normalização de status com `strip().lower()`.
- Status aceitos: `enviada`, `entrevista` e `recusada`.
- Continuidade da edição e nova listagem depois de uma alteração válida.
- Gravação em `candidaturas_treino.json` ao concluir os dois cadastros e após editar qualquer um dos três campos.
- Serialização e leitura JSON com UTF-8, preservando acentos.
- Resumo do total de candidaturas e das que estão em entrevista, exibido após o cadastro inicial.
- Conferência de um JSON em script independente, incluindo tratamento de arquivo ausente e JSON vazio ou malformado.
- Caminho de conferência baseado na pasta do script, funcionando mesmo quando a pasta atual do terminal muda.

O projeto usa somente a biblioteca padrão do Python. Ainda não há banco de dados, exclusão, menu geral, quantidade variável de cadastros ou comando próprio de saída.

## Estado da integração JSON

| Parte | Situação atual |
| --- | --- |
| Salvar pelo `main.py` | Implementado depois do cadastro e de edições válidas. |
| Função `carregar_candidaturas()` | Implementada e utilizada no script de conferência. |
| Carregar ao abrir `main.py` | Pendente; a lista começa vazia em toda execução. |
| Arquivo salvo pelo programa | `candidaturas_treino.json`, relativo à pasta atual do terminal. |
| Arquivo lido pela conferência | `candidaturas_laboratorio.json`, ao lado de `configuracoes.py`. |
| Caminho compartilhado entre gravação e leitura | Pendente; os dois fluxos ainda usam nomes e regras de localização diferentes. |
| Validação da estrutura carregada | Pendente; JSON interpretável não garante uma lista de candidaturas com os campos esperados. |

Os dois arquivos pertencem a fluxos separados de estudo. A conferência não recupera automaticamente o arquivo gravado pelo `main.py`.

## Como executar

É necessário ter Python 3 instalado. A revisão desta versão foi executada com Python 3.12.14.

```bash
git clone https://github.com/LuKeT-Dev-Py/career-tracker-python.git
cd career-tracker-python/career_tracker
python3 main.py
```

No Windows, conforme a instalação, use `python main.py` ou `py main.py` dentro da pasta `career_tracker`.

### Usar o programa principal

1. Preencha empresa, cargo e status de duas candidaturas.
2. Confira a listagem e o resumo inicial. O programa grava `candidaturas_treino.json` na pasta atual do terminal.
3. Digite `1` ou `2` para selecionar a candidatura que deseja alterar.
4. Digite o campo por extenso: `empresa`, `cargo` ou `status`.
5. Informe um novo valor válido. O programa atualiza somente o registro escolhido, grava o JSON e mostra a nova listagem.
6. Para interromper o laço de edição, use `Ctrl+C`. A interrupção pode mostrar `KeyboardInterrupt`.

Ao executar os comandos acima, a pasta atual será `career_tracker`, e o arquivo será criado nela. Executar o mesmo script a partir de outra pasta muda o local da gravação. A configuração de caminho absoluto ainda se aplica somente à conferência.

**Nesta versão, iniciar outra execução e concluir dois novos cadastros substitui o conteúdo anterior do arquivo de treino.** A próxima etapa é carregar e preservar os registros existentes antes de cadastrar ou editar.

### Conferir um arquivo JSON separadamente

```bash
python3 conferir_carregamento.py
```

O script procura `candidaturas_laboratorio.json` na pasta do projeto. Esse arquivo não está incluído no repositório; sua ausência gera uma mensagem com o caminho esperado.

Para conferir uma cópia dos dados de treino no Linux, primeiro interrompa o `main.py` com `Ctrl+C`. Dentro da pasta `career_tracker`, use:

```bash
cp -i candidaturas_treino.json candidaturas_laboratorio.json
python3 conferir_carregamento.py
```

O `-i` pede confirmação se o arquivo de laboratório já existir. No Windows, você pode fazer essa cópia pelo explorador de arquivos, com o mesmo nome de destino. Essa preparação manual serve à demonstração e ainda não conecta a leitura ao fluxo principal.

Com um arquivo válido, a conferência exibe o total de candidaturas, a quantidade em entrevista e os dados de cada registro. Arquivo de zero bytes e JSON malformado geram a mensagem de JSON inválido. O conteúdo `[]` é JSON válido e mostra totais iguais a zero.

## Exemplo

Cadastre:

| Candidatura | Empresa | Cargo | Status |
| --- | --- | --- | --- |
| 1 | Acme | Dev Python | enviada |
| 2 | Beta | Estágio | entrevista |

O resumo inicial informa duas candidaturas e uma em entrevista. Para alterar o status da segunda:

```text
Qual candidatura deseja alterar: 2
Qual valor deseja alterar?: status
Qual status da candidatura: enviada
```

A próxima listagem apresenta:

```text
Candidatura: 1
Empresa: Acme | Cargo: Dev Python | Status: Enviada
Candidatura: 2
Empresa: Beta | Cargo: Estágio | Status: Enviada
```

O arquivo de treino passa a conter os dois registros com esses valores. A primeira candidatura permanece intacta. O resumo de entrevistas é calculado apenas após o cadastro inicial; ele ainda não é recalculado após as edições.

## Organização do código

| Arquivo | Responsabilidade |
| --- | --- |
| `career_tracker/main.py` | Cadastro, validação, listagem, resumo inicial, edição e chamadas de gravação JSON. |
| `career_tracker/modulos.py` | Reunir as importações utilizadas pelo arquivo principal. |
| `career_tracker/candidaturas/operacoes.py` | Exibição, seleção, identificação do campo, gravação, leitura e contagem de entrevistas. |
| `career_tracker/conferir_carregamento.py` | Ler o arquivo de laboratório, tratar ausência e JSON inválido e exibir os dados recuperados. |
| `career_tracker/configuracoes.py` | Definir `CAMINHO_CONFERENCIA` a partir da pasta do próprio arquivo com `os.path`. |
| `career_tracker/validacoes/empresa.py` | Limpar espaços e conferir o preenchimento da empresa. |
| `career_tracker/validacoes/status.py` | Normalizar o status e conferir os três valores aceitos. |
| Arquivos `__init__.py` | Identificar os pacotes Python regulares. |

Cada candidatura é um dicionário com as chaves `empresa`, `cargo` e `status`. A lista `empresas_cadastradas` reúne esses dicionários. A seleção apresentada começa em 1 e é convertida para o índice da lista com `indice = alteracao - 1`.

`salvar_candidaturas(lista, caminho)` usa `open()` em modo `w` e `json.dump()` com `ensure_ascii=False` e `indent=2`. O modo de escrita substitui o conteúdo do arquivo. `carregar_candidaturas(caminho)` usa o modo `r` e `json.load()`, retornando o conteúdo interpretado.

O principal usa `from modulos import *`. Essa centralização foi registrada como parte da evolução; importações explícitas podem facilitar a leitura da origem de cada função em uma revisão futura.

## Verificação e problemas conhecidos

O assistente analisou o código do commit [`233d3ae`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/233d3aecc7e9aa0ecb1eeef864139c5253f3cf77). Foram executados **22 cenários: 17 confirmaram funcionalidades e 5 reproduziram limitações**. Os nove arquivos Python foram compilados sem avisos de sintaxe.

As limitações reproduzidas foram:

1. JSON válido com uma candidatura sem a chave `status` gera `KeyError` não tratado na conferência.
2. O principal não recupera o JSON existente e o sobrescreve depois de dois novos cadastros.
3. Principal e conferência usam arquivos diferentes, e somente a conferência tem caminho baseado na pasta do script.
4. O resumo de entrevistas não é recalculado depois de editar o status.
5. Falhas na gravação não são tratadas pelo principal; um diretório com o nome do arquivo causa `IsADirectoryError`.

Também continuam pendentes a saída por menu, o limite de dois cadastros, a apresentação de empresas com `capitalize()` e a simplificação de trechos redundantes. O contador de tentativas inválidas ainda é reiniciado por cadastro e não é exibido.

O [registro técnico de 21/10](docs/2026-10-21-json-parcial.md) contém a matriz dos cenários, o histórico das mudanças e os critérios para concluir a recuperação no principal. As verificações usaram arquivos temporários e o código original, sem alterar a lógica do autor. Não constituem uma suíte permanente incluída no projeto.

## Histórico de evolução

| Versão | Data | Etapa | Referência |
| --- | --- | --- | --- |
| `v0.0.1-prototype` | 24/09/2026 | Entrada de empresa e status, validação e exibição em módulos. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.1-prototype). |
| `v0.0.2-prototype` | 28/09/2026 | Validação de empresa e exercícios 4 e 5. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.2-prototype) e [registro](docs/2026-09-28-validacao-empresa.md). |
| `v0.0.3-prototype` | 02/10/2026 | Limpeza e normalização de entradas. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.3-prototype) e [registro](docs/2026-10-02-normalizacao-entradas.md). |
| `v0.0.4-wip` | 07/10/2026 | Cargo, duas candidaturas e edição parcial. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.4-wip) e [registro](docs/2026-10-07-cadastro-memoria-edicao-parcial.md). |
| `v0.0.5-prototype` | 08/10/2026 | Edição validada dos três campos em memória. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.5-prototype) e [registro](docs/2026-10-08-edicao-validada.md). |
| `v0.0.6-prototype` | 21/10/2026 | Gravação JSON no principal, contagens e leitura em script separado. | Código atual e [registro desta revisão](docs/2026-10-21-json-parcial.md). |

O [CHANGELOG](CHANGELOG.md) mantém os registros anteriores. Os commits de código entre 13 e 21/10 foram feitos pelo autor e preservados nesta publicação. A [imagem de demonstração](docs/demonstracao.png) continua correspondendo à primeira versão.

## Próxima etapa: recuperar e preservar os dados

- Unificar o arquivo e o caminho utilizados para salvar e carregar.
- Carregar as candidaturas ao iniciar, antes de decidir cadastrar ou editar.
- Recuperar os registros sem exigir dois novos cadastros e manter os anteriores ao salvar novas alterações.
- Tratar arquivo ausente, JSON inválido e erros de gravação no fluxo principal.
- Validar a estrutura carregada e atualizar o resumo quando os dados mudarem.
- Conferir o ciclo: cadastrar, salvar, encerrar, reabrir, listar os mesmos registros, editar, encerrar e reabrir novamente.

A gravação e a leitura separada já justificam este marco de estudo. A conclusão da persistência no fluxo principal depende de verificar o ciclo acima. Menu, exclusão e banco de dados permanecem evoluções futuras.
