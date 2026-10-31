# Career Tracker

Aplicação de terminal em Python para organizar candidaturas a vagas. Permite cadastrar empresa, cargo e status, consultar os registros e editar a candidatura escolhida.

É meu projeto principal de estudo. Nele pratico validação de entradas, organização em módulos, manipulação de listas e dicionários, arquivos JSON e testes com `unittest`.

**Estado atual:** protótipo com cadastro de duas candidaturas por execução, edição contínua e gravação em JSON.

> O programa principal ainda inicia com uma lista vazia. Ao concluir dois novos cadastros, substitui o JSON da execução anterior. A leitura já existe em um script separado; recuperar os registros automaticamente ao abrir o programa é a próxima integração.

## Funcionalidades

- Cadastrar duas candidaturas com empresa, cargo e um dos status `enviada`, `entrevista` ou `recusada`.
- Listar registros e editar empresa, cargo ou status de uma candidatura selecionada.
- Rejeitar campos vazios, status inválidos e seleções inexistentes ou não numéricas.
- Remover espaços das extremidades e normalizar o status para minúsculas.
- Mostrar o total de candidaturas e de entrevistas após o cadastro inicial.
- Salvar o cadastro e as edições em JSON com UTF-8.
- Conferir um JSON em script separado, com mensagens para arquivo ausente, conteúdo inválido ou lista vazia.

## Como executar

Requer **Python 3.12 ou superior** e Git para clonar. Usa somente a biblioteca padrão, sem dependências externas. A sintaxe de f-strings utilizada na conferência exige [Python 3.12](https://docs.python.org/3.12/whatsnew/3.12.html#pep-701-syntactic-formalization-of-f-strings).

No Linux ou macOS:

```bash
git clone https://github.com/LuKeT-Dev-Py/career-tracker-python.git
cd career-tracker-python/career_tracker
python3 main.py
```

No Windows, dentro da mesma pasta, use `py main.py` ou `python main.py`, conforme a instalação. Confira se o interpretador é 3.12 ou superior.

1. Cadastre duas candidaturas.
2. Digite `1` ou `2` para escolher qual deseja editar.
3. Informe o campo por extenso: `empresa`, `cargo` ou `status`.
4. Digite o novo valor e confira a listagem.
5. Para encerrar, use `Ctrl+C`; o protótipo ainda pode mostrar `KeyboardInterrupt`.

### Exemplo de uso

Cadastre os dados fictícios abaixo:

| Número | Empresa | Cargo | Status |
| --- | --- | --- | --- |
| 1 | Acme | Dev Python | enviada |
| 2 | Beta | Estágio | entrevista |

O resumo inicial informa duas candidaturas e uma em entrevista. Para mudar o status da segunda:

```text
Qual candidatura deseja alterar: 2
Qual valor deseja alterar?: status
Qual status da candidatura: enviada
```

Na nova listagem:

```text
Candidatura: 1
Empresa: Acme | Cargo: Dev Python | Status: Enviada
Candidatura: 2
Empresa: Beta | Cargo: Estágio | Status: Enviada
```

A primeira candidatura permanece intacta, e o arquivo de treino recebe a alteração. O resumo de entrevistas ainda é calculado somente após o cadastro inicial.

## Arquivos JSON

| Fluxo | Arquivo | Localização |
| --- | --- | --- |
| Gravação pelo programa principal | `candidaturas_treino.json` | Pasta atual do terminal. |
| Leitura pelo script de conferência | `candidaturas_laboratorio.json` | Pasta `career_tracker`, definida em `configuracoes.py`. |

Os arquivos são gerados durante o uso e não acompanham o repositório. Para demonstrar a leitura com os dados cadastrados, encerre o principal e, dentro de `career_tracker`, execute no Linux ou macOS:

```bash
cp -i candidaturas_treino.json candidaturas_laboratorio.json
python3 conferir_carregamento.py
```

No Windows, copie o arquivo pelo explorador, renomeie a cópia para `candidaturas_laboratorio.json` e execute `py conferir_carregamento.py`.

A cópia é uma preparação manual para a demonstração. A conferência mostra totais e registros, trata arquivo ausente e JSON malformado e aceita `[]` como lista vazia válida.

## Teste automatizado

Dentro de `career_tracker`:

```bash
python3 -m unittest -v teste
```

No Windows: `py -m unittest -v teste`.

Há **um teste incluído**, em [teste.py](career_tracker/teste.py), que verifica se `resumir_candidaturas([])` retorna `{"total": 0, "entrevistas": 0}`. Ele não cobre o cadastro interativo, as edições ou a persistência.

## Onde ler o código

| Arquivo | Responsabilidade |
| --- | --- |
| [main.py](career_tracker/main.py) | Cadastro, resumo inicial, seleção, edição e chamadas de gravação. |
| [operacoes.py](career_tracker/candidaturas/operacoes.py) | Operações sobre candidaturas, leitura/gravação JSON e contagens. |
| [empresa.py](career_tracker/validacoes/empresa.py) e [status.py](career_tracker/validacoes/status.py) | Limpeza e validação das entradas. |
| [conferir_carregamento.py](career_tracker/conferir_carregamento.py) | Leitura e apresentação do arquivo de laboratório. |
| [configuracoes.py](career_tracker/configuracoes.py) | Caminho do arquivo usado na conferência. |
| [modulos.py](career_tracker/modulos.py) | Importações utilizadas pelo principal. |

Cada candidatura é um dicionário com `empresa`, `cargo` e `status`. A seleção exibida começa em 1; `indice = alteracao - 1` converte a escolha para o índice da lista.

## Limitações e próximos passos

A prioridade é completar o ciclo de salvar, encerrar, reabrir e recuperar os mesmos registros. Isso exige unificar arquivo e caminho, carregar os dados no início e tratar falhas de leitura/gravação no fluxo principal.

Também faltam validação da estrutura do JSON carregado, atualização do resumo após edições, saída por menu, quantidade variável de cadastros e exclusão. Um JSON interpretável com campos ausentes ainda pode causar erro na conferência.

## Evolução do projeto

O marco `v0.0.6-prototype` registra a integração parcial de JSON em 21/10/2026. O teste de lista vazia está incluído no código atual.

- [CHANGELOG](CHANGELOG.md): versões e histórico.
- [Registro técnico de JSON](docs/2026-10-21-json-parcial.md): cenários de verificação e limitações do marco.
- [Documentação anterior preservada](docs/readme-anterior-2026-10-31.md): histórico detalhado, versões anteriores e decisões.

Os exemplos desta apresentação e o teste incluído foram conferidos em Python 3.12.14. As verificações históricas estão identificadas nos registros técnicos.
