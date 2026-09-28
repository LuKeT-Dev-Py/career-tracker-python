# Evolução de 28/09/2026 — validação de empresa

## Origem desta atualização

Esta etapa aplica os exercícios 4 e 5 registrados em `Pratica_Programacao_Career_Tracker_2026-09-28.md`, fornecido pelo autor, sobre a base `v0.0.1-prototype` do repositório.

A lógica registrada pelo autor foi integrada pelo assistente ao código existente. As explicações e verificações abaixo foram preparadas nesta atualização. Os demais exercícios da prática não geraram mudanças no programa.

## Exercício 4 — empresa preenchida

```python
def empresa_preenchida(nome):
    return bool(nome.strip())
```

A solução está correta para entradas de texto, como as retornadas por `input()`.

1. `nome.strip()` retorna uma nova string sem espaços em branco nas extremidades, incluindo tabulações e quebras de linha. A string original não é alterada.
2. `bool()` converte o resultado em um valor booleano: string vazia resulta em `False`; string com conteúdo resulta em `True`.
3. `return` entrega esse booleano para a condição no programa principal.

Assim, `"Acme"` e `"  Acme  "` são aceitos; `""` e `"   "` são rejeitados. Isso corrige a primeira tentativa registrada na prática, que ainda aceitava vários espaços. A validação não comprova que a empresa existe.

## Exercício 5 — integração no Career Tracker

```python
if empresa_preenchida(empresa):
    if validar_status(status):
        exibir_candidatura(empresa, status)
    else:
        print('Status invalido.')
else:
    print('Empresa invalida.')
```

A integração está correta: a chamada da função retorna o resultado que o `if` testa. O segundo `if` só é executado se a empresa estiver preenchida. A candidatura só é exibida se as duas validações passarem.

O primeiro `else`, dentro do bloco da empresa, pertence à validação do status. O último `else` pertence à validação da empresa. Se ambos os campos estiverem inválidos, a mensagem será `Empresa invalida.`.

O programa ainda coleta os dois campos antes de validar. Validar a empresa primeiro não significa que a pergunta de status será omitida.

## Comparação com a versão anterior

| Situação | v0.0.1-prototype | v0.0.2-prototype |
| --- | --- | --- |
| Empresa vazia e status válido | Exibia a candidatura | Exibe `Empresa invalida.` |
| Empresa só com espaços e status válido | Exibia a candidatura | Exibe `Empresa invalida.` |
| Empresa preenchida e status inválido | Exibia `Erro` | Exibe `Status invalido.` |
| Empresa e status válidos | Exibia a candidatura | Continua exibindo a candidatura |
| Armazenamento das candidaturas | Não implementado | Não implementado |

## Verificação executada nesta atualização

No registro original, a captura demonstrava `Acme` com `pendente` resultando em `Status invalido.`. Os demais casos abaixo foram executados localmente pelo assistente nesta atualização.

A função `empresa_preenchida` passou em 5 casos: `"Acme"`, `"  Acme  "`, `"   "`, `""` e uma tabulação. Os dois primeiros retornaram `True`; os demais retornaram `False`.

O programa completo passou nos seguintes 10 casos:

| Empresa (representação da entrada) | Status | Saída final |
| --- | --- | --- |
| `"Acme"` | `enviada` | `Empresa: Acme \| Status: Enviada` |
| `"Acme"` | `entrevista` | `Empresa: Acme \| Status: Entrevista` |
| `"Acme"` | `recusada` | `Empresa: Acme \| Status: Recusada` |
| `"Acme"` | `ENVIADA` | `Empresa: Acme \| Status: Enviada` |
| `"Acme"` | `pendente` | `Status invalido.` |
| `""` | `enviada` | `Empresa invalida.` |
| `"   "` | `enviada` | `Empresa invalida.` |
| `"   "` | `pendente` | `Empresa invalida.` |
| `"  Acme  "` | `enviada` | `Empresa:   acme   \| Status: Enviada` |
| `"Acme"` | `" enviada "` | `Status invalido.` |

Nos casos inválidos, também foi verificado que a candidatura não é exibida. Todas as execuções terminaram sem erro de processo.

## Limites desta etapa

O uso de `strip()` apenas na validação não remove os espaços do nome exibido. A função de exibição continua usando `capitalize()`; por isso, `"  Acme  "` aparece com espaços e letras minúsculas. O status com espaços nas extremidades continua inválido.

Esses comportamentos existentes foram mantidos para que esta etapa corresponda aos exercícios. Não foram adicionados banco de dados, persistência, múltiplas candidaturas, laços de repetição ou atualização de vagas.

## Como consultar a versão anterior

- [Projeto completo antes desta atualização](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/302f336d9bad881d148e4f9ebde75057ddf67b95)
- [README original preservado](https://github.com/LuKeT-Dev-Py/career-tracker-python/blob/302f336d9bad881d148e4f9ebde75057ddf67b95/README.md)

A atualização acrescenta commits ao histórico existente. O código e as informações da primeira versão continuam acessíveis.
