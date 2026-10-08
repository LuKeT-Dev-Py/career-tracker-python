# Career Tracker

Projeto de estudo em Python para acompanhar candidaturas pelo terminal e registrar minha evolução em programação.

**Versão atual: `v0.0.5-prototype`, publicada em 08/10/2026.** O protótipo cadastra duas candidaturas, lista os registros e permite editar empresa, cargo e status da candidatura escolhida. Após uma alteração, mostra os dados atualizados e continua aberto para outra edição.

Os dados ficam em uma lista de dicionários durante a execução. **Ao encerrar o programa, os cadastros são perdidos.** A persistência é uma próxima etapa do projeto.

## Funcionalidades disponíveis

- Aviso de lista vazia antes do primeiro cadastro.
- Cadastro de duas candidaturas por execução, com empresa, cargo e status.
- Listagem numerada dos registros.
- Seleção por número, com validação entre 1 e a quantidade cadastrada.
- Tratamento de texto não numérico na seleção, com nova tentativa após `ValueError`.
- Edição de empresa, cargo ou status somente na candidatura escolhida.
- Rejeição de empresa e cargo vazios ou compostos apenas por espaços.
- Aceitação dos status `enviada`, `entrevista` e `recusada`, com normalização de espaços nas extremidades e maiúsculas/minúsculas.
- Novas tentativas para entradas inválidas antes de cadastrar ou atualizar um registro.
- Rejeição de campo de edição desconhecido sem alterar os dados.
- Nova listagem e continuidade da edição depois de uma alteração válida.

A quantidade de cadastros é definida no código. O fluxo começa pelo cadastro e depois entra na edição; ainda não há um menu geral para cadastrar mais registros, excluir ou sair.

## Como executar

É necessário ter Python 3 instalado. O projeto usa apenas a biblioteca padrão, sem dependências externas ou configuração de banco de dados. Esta publicação foi verificada com Python 3.12.

```bash
git clone https://github.com/LuKeT-Dev-Py/career-tracker-python.git
cd career-tracker-python/career_tracker
python3 main.py
```

No Windows, conforme a instalação, use `python main.py` ou `py main.py` dentro da pasta `career_tracker`.

### Como usar

1. Informe empresa, cargo e status da primeira candidatura.
2. Repita o cadastro para a segunda candidatura.
3. Confira a listagem e digite `1` ou `2` para escolher qual registro editar.
4. Na pergunta sobre o campo, digite `empresa`, `cargo` ou `status`. Essa pergunta aceita palavras, não os números dos campos.
5. Informe um novo valor válido. O programa mostra a listagem atualizada e volta à seleção.
6. Para interromper a execução no terminal, use `Ctrl+C`. Ainda não há um comando próprio de saída; essa interrupção pode mostrar `KeyboardInterrupt`.

## Exemplo de uso

Cadastre estes dados:

| Candidatura | Empresa | Cargo | Status |
| --- | --- | --- | --- |
| 1 | `Acme` | `Dev Python` | `enviada` |
| 2 | `Beta` | `Estágio` | `entrevista` |

Depois, informe:

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

Somente o status da segunda candidatura muda. Empresa, cargo e todos os dados da primeira permanecem iguais. Uma entrada como ` ENTREVISTA ` também é aceita como `entrevista`; `pendente` é rejeitada e gera uma nova pergunta.

## Organização do código

| Arquivo | Responsabilidade |
| --- | --- |
| `career_tracker/main.py` | Conduzir as perguntas, validar entradas, criar os registros, listar e atualizar o campo escolhido. |
| `career_tracker/validacoes/empresa.py` | Remover espaços nas extremidades com `limpar_empresa()` e verificar conteúdo com `empresa_preenchida()`. |
| `career_tracker/validacoes/status.py` | Preparar o texto com `normalizar_status()` e conferir os três valores permitidos com `validar_status()`. |
| `career_tracker/candidaturas/operacoes.py` | Exibir a candidatura, verificar se a lista tem elementos, identificar o campo de edição e validar o número escolhido. |
| Arquivos `__init__.py` | Identificar os diretórios de validações e candidaturas como pacotes Python regulares. |

O arquivo principal importa as funções dos módulos e as chama durante o fluxo. Por exemplo, `normalizar_status()` prepara uma entrada antes de `validar_status()` conferir seu conteúdo; `selecao_valida()` verifica o número antes de acessar a lista.

Cada candidatura é um dicionário com três chaves:

```python
{"empresa": "Acme", "cargo": "Dev Python", "status": "enviada"}
```

Os dicionários são incluídos na lista `empresas_cadastradas` com `append()`. O `for` percorre a lista para exibir os registros. A edição atualiza uma chave do dicionário na posição selecionada.

## Conceitos praticados

- Funções, parâmetros, retornos e importação entre módulos.
- Listas e dicionários para organizar os dados em memória.
- Laços `while` para novas tentativas e `for` para a listagem.
- Condições para decidir qual campo alterar.
- `strip()` e `lower()` para preparar as entradas.
- Conversão com `int()` e tratamento de `ValueError`.
- Validação de faixa antes de acessar uma lista.
- Diferença entre a numeração apresentada ao usuário e os índices do Python.
- Uso de `continue` para repetir uma tentativa e `break` para encerrar o laço correspondente.

O [registro técnico de 08/10](docs/2026-10-08-edicao-validada.md) explica a correção do índice relatada pelo autor, as mudanças em relação à versão parcial e as verificações desta publicação.

## Verificação desta versão

O assistente executou 10 cenários sobre o código enviado pelo autor, incluindo cadastro, lista vazia, edição de todos os campos, seleção da segunda candidatura, entradas inválidas e alterações consecutivas. **Os 10 cenários passaram.** Os seis arquivos Python também foram compilados sem avisos de sintaxe.

As verificações conferiram os dados e a saída do programa, incluindo a preservação da candidatura não selecionada. Como o fluxo de edição permanece aberto, o procedimento de verificação pausou a execução na próxima pergunta depois de consumir as entradas previstas. Essa pausa pertence à verificação e não é uma opção de saída do aplicativo.

Os casos, entradas e resultados estão no [registro técnico](docs/2026-10-08-edicao-validada.md#verificações-executadas). Eles documentam os cenários analisados; não constituem uma suíte permanente de testes incluída no repositório nem exercícios adicionais realizados pelo autor.

## Limitações e ajustes futuros

| Item | Situação atual |
| --- | --- |
| Persistência | Os cadastros desaparecem ao encerrar a execução. Não há arquivo ou banco de dados. |
| Quantidade de registros | O cadastro inicial é limitado a duas candidaturas pelo código. |
| Operações | Cadastro, listagem e edição disponíveis; exclusão ainda não implementada. |
| Saída | O laço de edição continua aberto e depende de uma interrupção no terminal. |
| Capitalização | `capitalize()` na exibição transforma nomes como `IBM` em `Ibm`. |
| Contador de status inválidos | Reinicia a cada cadastro e sua exibição fica depois do laço de edição, sem ser alcançada no fluxo normal. |
| Organização | Há `import sys` sem uso, um `try` redundante no validador de status e laços que podem ser simplificados. |

A mensagem de lista vazia aparece na abertura, antes dos cadastros. Não há uma opção de consulta independente com zero registros nem um caminho de edição antes de cadastrar.

## Histórico de evolução

| Versão | Data | Etapa | Onde consultar |
| --- | --- | --- | --- |
| `v0.0.1-prototype` | 24/09/2026 | Entrada de empresa e status, validação e exibição em módulos. | [Primeira versão](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.1-prototype). |
| `v0.0.2-prototype` | 28/09/2026 | Validação de empresa e integração dos exercícios 4 e 5. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.2-prototype) e [registro da prática](docs/2026-09-28-validacao-empresa.md). |
| `v0.0.3-prototype` | 02/10/2026 | Limpeza de entradas, normalização de status e organização das condições. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.3-prototype) e [registro técnico](docs/2026-10-02-normalizacao-entradas.md). |
| `v0.0.4-wip` | 07/10/2026 | Cargo, duas candidaturas em memória e edição parcial. | [Estado parcial preservado](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.4-wip) e [análise da etapa](docs/2026-10-07-cadastro-memoria-edicao-parcial.md). |
| `v0.0.5-prototype` | 08/10/2026 | Edição de empresa, cargo e status, seleção validada e continuidade do fluxo. | Código atual e [registro desta publicação](docs/2026-10-08-edicao-validada.md). |

O [CHANGELOG](CHANGELOG.md) registra as mudanças de cada etapa. Os commits e as branches históricas preservam os códigos, READMEs e demais arquivos das versões anteriores. A [imagem de demonstração](docs/demonstracao.png) corresponde à primeira versão.

## Próximos passos

- Implementar armazenamento que permita recuperar as candidaturas depois de fechar e reabrir o programa.
- Criar um menu com saída e quantidade variável de cadastros.
- Revisar contador, capitalização e trechos redundantes.
- Estudar a integração com banco de dados; PostgreSQL permanece uma possibilidade futura.

Esses recursos ainda são planos. A versão atual registra a conclusão do fluxo de cadastro, listagem e edição em memória desta etapa de estudo.
