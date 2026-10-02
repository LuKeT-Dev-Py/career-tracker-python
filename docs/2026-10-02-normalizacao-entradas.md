# Evolução de 02/10/2026: normalização de entradas

## Origem e escopo

Esta etapa registra o código enviado pelo autor no arquivo `career_tracker(3).zip`, comparado com a `v0.0.2-prototype`, publicada no commit [`53d5d97`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/53d5d972f688c8e726a503bd8505a98105176579).

As mudanças de lógica já estavam no ZIP. O assistente preparou a documentação, verificou o comportamento e organizou a publicação. Não foram adicionados recursos além dos enviados pelo autor. O primeiro ZIP desta conversa, `career_tracker(2).zip`, foi substituído pelo envio mais recente e não foi publicado.

Os arquivos `__pycache__` e `.pyc` do ZIP são caches gerados pelo Python e foram excluídos da publicação. Os arquivos `__init__.py` continuam presentes. A função de exibição mantém a mesma lógica; a linha em branco adicional nesse arquivo não constitui uma funcionalidade nova e não gera um commit próprio.

## Mudanças implementadas

### Limpeza do nome da empresa

```python
def limpar_empresa(nome):
    return nome.strip()
```

`strip()` retorna uma nova string sem espaços em branco nas extremidades, incluindo tabulações e quebras de linha. A string original não é alterada pela função. No programa principal, `empresa = limpar_empresa(empresa)` atribui esse retorno à variável, e o valor limpo é usado na validação e na exibição.

Com `"  Acme  "`, o valor usado passa a ser `"Acme"`. Espaços dentro do nome permanecem: `"Acme  Labs"` continua com dois espaços internos.

`empresa_preenchida(nome)` continua usando `bool(nome.strip())`. Uma string vazia retorna `False`; uma string com conteúdo retorna `True`. Essa validação rejeita também uma entrada formada apenas por espaços em branco.

### Normalização do status

```python
def normalizar_status(texto):
    return texto.strip().lower()
```

As chamadas acontecem da esquerda para a direita: `strip()` remove os espaços nas extremidades e `lower()` converte o resultado para minúsculas. Assim, `" EnTrEvIsTa "` se torna `"entrevista"`.

`validar_status(status)` mantém a mesma regra: o texto deve pertencer à tupla `('enviada', 'entrevista', 'recusada')`. A normalização não aceita novas situações, não corrige palavras digitadas incorretamente e não remove espaços internos. O validador não normaliza por conta própria; `main.py` faz isso antes de chamá-lo.

A conversão para minúsculas já existia na `v0.0.2`, diretamente no `input()`. Nesta etapa, ela passa a fazer parte de uma função própria, junto com a remoção de espaços nas extremidades.

### Fluxo de validação

```python
status = normalizar_status(status)
empresa = limpar_empresa(empresa)

if not empresa_preenchida(empresa):
    print("Empresa inválida.")
elif not validar_status(status):
    print("Status inválido.")
else:
    exibir_candidatura(empresa, status)
```

O operador `not` inverte o resultado booleano: a condição fica verdadeira quando a validação retorna `False`. O `elif` só é avaliado se o primeiro `if` for falso. O `else` é executado quando nenhuma das condições de erro é verdadeira.

Essa estrutura reduz o aninhamento e mantém a prioridade da empresa. Se os dois campos estiverem inválidos, a saída é `Empresa inválida.` e a validação do status não é chamada. Os dois campos continuam sendo solicitados antes dessas verificações.

As mensagens receberam acentos: `Empresa inválida.` e `Status inválido.`.

## Comparação com a versão anterior

| Situação | v0.0.2-prototype | v0.0.3-prototype |
| --- | --- | --- |
| Empresa `"  Acme  "`, status `"enviada"` | `Empresa:   acme   \| Status: Enviada` | `Empresa: Acme \| Status: Enviada` |
| Empresa `"Acme"`, status `" enviada "` | `Status invalido.` | `Empresa: Acme \| Status: Enviada` |
| Empresa `"Acme"`, status `"ENVIADA"` | Aceito | Continua aceito |
| Empresa vazia, status válido | `Empresa invalida.` | `Empresa inválida.` |
| Empresa válida, status `"pendente"` | `Status invalido.` | `Status inválido.` |
| Dois campos inválidos | Erro de empresa tem prioridade | Prioridade mantida |
| Organização das condições | `if` dentro de outro `if` | `if`/`elif`/`else` |
| Armazenamento das candidaturas | Não implementado | Não implementado |

## Verificação executada

O assistente executou localmente 8 casos das funções novas e 17 casos do programa completo em 02/10/2026. Todos passaram. Nas entradas inválidas, também foi verificado que a candidatura não é exibida. Todas as execuções terminaram sem erro de processo, e os arquivos Python passaram pela verificação de sintaxe.

Os 17 cenários também foram executados sobre a versão publicada anterior para conferir a comparação. Essa contagem de 25 verificações se refere à versão nova. Os casos abaixo são verificações desta atualização, não exercícios adicionais realizados pelo autor nem uma suíte de testes incluída no repositório.

### Funções de limpeza e normalização

| Função | Entrada | Retorno |
| --- | --- | --- |
| `limpar_empresa` | `""` | `""` |
| `limpar_empresa` | `" \t "` | `""` |
| `limpar_empresa` | `"  Acme  "` | `"Acme"` |
| `limpar_empresa` | `"Acme  Labs"` | `"Acme  Labs"` |
| `normalizar_status` | `"ENVIADA"` | `"enviada"` |
| `normalizar_status` | `" \t EnTrEvIsTa \t "` | `"entrevista"` |
| `normalizar_status` | `"   "` | `""` |
| `normalizar_status` | `" en viada "` | `"en viada"` |

### Programa completo

As entradas são representadas entre aspas para tornar os espaços visíveis. `\t` representa uma tabulação.

| Empresa | Status | Saída final |
| --- | --- | --- |
| `"Acme"` | `"enviada"` | `Empresa: Acme \| Status: Enviada` |
| `"Acme"` | `"entrevista"` | `Empresa: Acme \| Status: Entrevista` |
| `"Acme"` | `"recusada"` | `Empresa: Acme \| Status: Recusada` |
| `"Acme"` | `"ENVIADA"` | `Empresa: Acme \| Status: Enviada` |
| `"Acme"` | `" enviada "` | `Empresa: Acme \| Status: Enviada` |
| `"  Acme  "` | `"enviada"` | `Empresa: Acme \| Status: Enviada` |
| `"  ACME  "` | `" EnTrEvIsTa "` | `Empresa: Acme \| Status: Entrevista` |
| `"Acme"` | `"\tRECUSADA\t"` | `Empresa: Acme \| Status: Recusada` |
| `""` | `"enviada"` | `Empresa inválida.` |
| `"   "` | `"enviada"` | `Empresa inválida.` |
| `"\t"` | `"enviada"` | `Empresa inválida.` |
| `""` | `"pendente"` | `Empresa inválida.` |
| `"Acme"` | `"pendente"` | `Status inválido.` |
| `"Acme"` | `" en viada "` | `Status inválido.` |
| `"Acme"` | `""` | `Status inválido.` |
| `"IBM"` | `"enviada"` | `Empresa: Ibm \| Status: Enviada` |
| `"Acme  Labs"` | `"enviada"` | `Empresa: Acme  labs \| Status: Enviada` |

## Organização dos commits

| Ordem | Mensagem | Conteúdo |
| --- | --- | --- |
| 1 | `feat(validacoes): adiciona limpeza de empresa e normalizacao de status` | Funções `limpar_empresa()` e `normalizar_status()` nos módulos existentes. |
| 2 | `refactor(cli): normaliza entradas e simplifica validacao` | Uso das funções antes da validação, condições com `if`/`elif`/`else` e mensagens com acentos. |
| 3 | `docs: registra evolucao para v0.0.3-prototype` | README completo, nova entrada no CHANGELOG e este registro técnico. |

`feat` identifica a inclusão das funções; `refactor` identifica a reorganização do fluxo, incluindo a integração dessas funções; `docs` reúne a documentação. Os corpos dos commits explicam o conteúdo e o motivo de cada etapa. A versão `v0.0.3-prototype` identifica este marco de aprendizado na documentação.

## Preservação das versões e limites

A `v0.0.2` permanece completa na branch [`historico/v0.0.2-prototype`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.2-prototype), incluindo o código, README, CHANGELOG, registro da prática e imagem. A [primeira versão](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.1-prototype) e o [registro dos exercícios 4 e 5](2026-09-28-validacao-empresa.md) continuam disponíveis. A publicação acrescenta commits ao histórico existente.

O programa continua exibindo uma candidatura por execução, sem salvá-la. `capitalize()` ainda altera a capitalização dos nomes: `"IBM"` aparece como `"Ibm"`. Os espaços internos permanecem, a empresa é validada apenas quanto ao preenchimento e não há banco de dados, menu ou edição de candidaturas nesta etapa.
