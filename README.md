# Career Tracker

Projeto de estudo em Python para acompanhar candidaturas a vagas pelo terminal e registrar minha evolução em programação. O programa recebe o nome da empresa e o status, prepara essas entradas, verifica se são válidas e exibe a candidatura.

**Versão atual:** `v0.0.3-prototype`, registrada em 02/10/2026. O projeto recebe uma candidatura por execução e ainda não salva os dados.

## Funcionalidades implementadas

- Entrada do nome da empresa e do status pelo terminal.
- Remoção de espaços em branco nas extremidades do nome da empresa com `limpar_empresa()`.
- Normalização do status com `normalizar_status()`: remoção de espaços nas extremidades e conversão para minúsculas.
- Rejeição de empresa vazia ou composta apenas por espaços em branco.
- Validação dos status `enviada`, `entrevista` e `recusada`.
- Validação da empresa antes do status, com `if`/`elif`/`else`.
- Mensagens `Empresa inválida.` e `Status inválido.` para entradas rejeitadas.
- Exibição da candidatura somente quando os dois campos são válidos.
- Separação das funções de validação, limpeza e exibição em módulos Python.

## Como executar

É necessário ter Python 3 instalado. Não há dependências externas nem configuração de banco de dados.

```bash
git clone https://github.com/LuKeT-Dev-Py/career-tracker-python.git
cd career-tracker-python/career_tracker
python3 main.py
```

Se você já baixou o projeto, entre na pasta `career_tracker` e execute `python3 main.py`. No Windows, o comando pode ser `python main.py` ou `py main.py`.

## Exemplo de uso

```text
Qual empresa você candidatou: Acme

Opções de status: enviada, entrevista, recusada

Qual status da candidatura: ENVIADA
Empresa: Acme | Status: Enviada
```

Entradas como `"  Acme  "` e `" EnTrEvIsTa "` resultam em `Empresa: Acme | Status: Entrevista`. Os espaços nas extremidades são removidos antes da validação e da exibição.

| Empresa | Status | Saída final |
| --- | --- | --- |
| `"Acme"` | `"enviada"` | `Empresa: Acme \| Status: Enviada` |
| `"  Acme  "` | `" enviada "` | `Empresa: Acme \| Status: Enviada` |
| `""` | `"enviada"` | `Empresa inválida.` |
| `"   "` | `"pendente"` | `Empresa inválida.` |
| `"Acme"` | `"pendente"` | `Status inválido.` |

O programa solicita os dois campos antes de validar. Quando ambos estão inválidos, a mensagem da empresa tem prioridade.

## Organização do código

| Arquivo | Responsabilidade |
| --- | --- |
| `career_tracker/main.py` | Coletar as entradas, chamar a limpeza e a normalização, validar e escolher a saída. |
| `career_tracker/validacoes/empresa.py` | `limpar_empresa(nome)` remove espaços nas extremidades; `empresa_preenchida(nome)` retorna se há conteúdo. |
| `career_tracker/validacoes/status.py` | `normalizar_status(texto)` prepara o texto; `validar_status(status)` verifica se ele pertence à tupla de status permitidos. |
| `career_tracker/candidaturas/operacoes.py` | `exibir_candidatura(empresa, status)` imprime os dados com `capitalize()`. |
| `career_tracker/validacoes/__init__.py` e `career_tracker/candidaturas/__init__.py` | Identificar os diretórios como pacotes Python regulares. |

`validar_status()` espera receber o texto já normalizado. A chamada a `normalizar_status()` acontece no programa principal. As funções de limpeza retornam novas strings, e `main.py` atribui esses resultados às variáveis usadas depois.

## Evolução do projeto

| Versão | Registro | Etapa | Código e documentação preservados |
| --- | --- | --- | --- |
| `v0.0.1-prototype` | 24/09/2026 | Entrada pelo terminal, validação de status e exibição em módulos. | [Primeira versão completa](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/302f336d9bad881d148e4f9ebde75057ddf67b95) e branch [`historico/v0.0.1-prototype`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.1-prototype). |
| `v0.0.2-prototype` | 28/09/2026 | Exercícios 4 e 5: validação de empresa e integração no fluxo principal. | [Versão completa](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/53d5d972f688c8e726a503bd8505a98105176579), branch [`historico/v0.0.2-prototype`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.2-prototype) e [registro da prática](docs/2026-09-28-validacao-empresa.md). |
| `v0.0.3-prototype` | 02/10/2026 | Limpeza do nome da empresa, normalização do status e condições com `if`/`elif`/`else`. | Código atual e [registro técnico desta etapa](docs/2026-10-02-normalizacao-entradas.md). |

O [CHANGELOG](CHANGELOG.md) detalha as mudanças. Cada atualização acrescenta commits ao histórico, sem reescrever os registros anteriores. A estrutura desta etapa separa a inclusão das funções, a integração no terminal e a documentação, usando os tipos `feat`, `refactor` e `docs`.

O [README original](https://github.com/LuKeT-Dev-Py/career-tracker-python/blob/302f336d9bad881d148e4f9ebde75057ddf67b95/README.md), o [README da v0.0.2](https://github.com/LuKeT-Dev-Py/career-tracker-python/blob/53d5d972f688c8e726a503bd8505a98105176579/README.md) e a [imagem da primeira execução](docs/demonstracao.png) continuam disponíveis. A imagem é um registro da primeira versão.

## Verificação desta etapa

Foram executados localmente 8 casos das funções de limpeza e normalização e 17 casos do programa completo. Todos passaram, incluindo entradas com espaços, tabulações, letras maiúsculas, empresa vazia e status inválido. Os resultados estão no [registro da atualização](docs/2026-10-02-normalizacao-entradas.md#verificação-executada).

Essas verificações foram executadas pelo assistente sobre o código enviado pelo autor. Não são uma suíte automatizada incluída no repositório nem novos exercícios respondidos pelo autor.

## Limitações conhecidas

- Os dados são exibidos e descartados quando o programa termina; não há persistência nem consulta de histórico.
- Há uma candidatura por execução, sem menu, repetição, edição ou exclusão.
- `strip()` remove espaços em branco nas extremidades; espaços internos permanecem. `"en viada"` continua sendo um status inválido.
- `capitalize()` muda as demais letras para minúsculas: `"IBM"` aparece como `"Ibm"`, e `"Acme Labs"` como `"Acme labs"`.
- A validação da empresa verifica apenas se o texto está preenchido, sem confirmar a existência da empresa.
- As funções recebem strings, como as retornadas por `input()`; não há tratamento de tipos diferentes ou da interrupção da entrada.

## Próximos passos planejados

- Ampliar o tratamento de erros e revisar a apresentação dos nomes das empresas.
- Registrar e consultar várias candidaturas.
- Atualizar a situação das vagas.
- Persistir o histórico em PostgreSQL quando a aplicação estiver pronta para isso.

Esses itens são planos e ainda não estão implementados. As atualizações acompanham os conceitos praticados durante o estudo de Python.
