# Edição validada e continuidade do fluxo

Registro de 08/10/2026, correspondente à versão `v0.0.5-prototype`.

## Fonte e escopo

O código desta publicação foi enviado pelo autor no arquivo `career_tracker(6).zip`. Seus seis arquivos Python são iguais aos da versão revisada imediatamente antes, `career_tracker(5).zip`, e foram preservados integralmente. A documentação e as verificações descritas aqui foram preparadas pelo assistente.

A etapa entrega cadastro, listagem e edição de candidaturas em memória. Conclui os fluxos de empresa, cargo e status que estavam parciais em 07/10, incluindo seleção correta e novas tentativas. Persistência, menu geral, exclusão e melhorias do contador seguem como pendências ou planos.

## Comparação com a versão parcial de 07/10

| Área | `v0.0.4-wip` | `v0.0.5-prototype` |
| --- | --- | --- |
| Lista vazia | O cadastro começava antes de exibir essa condição inicial. | A abertura informa que nenhuma empresa foi cadastrada. |
| Seleção | Havia conversão para inteiro, sem validação da faixa. | `selecao_valida(numero, quantidade)` aceita apenas números entre 1 e o total de registros. |
| Índice | A atualização podia atingir o segundo registro ao escolher o primeiro ou acessar uma posição inexistente ao escolher o segundo. | `indice = alteracao - 1` converte a numeração exibida para o índice usado na lista. |
| Empresa | O bloco de atualização ficava fora da condição do campo escolhido. | A pergunta e a atualização acontecem dentro do bloco de empresa. |
| Cargo | Existiam marcadores de continuação, sem atualização. | O programa pede, limpa, valida e grava o novo cargo. |
| Status | O identificador do campo usava `is` e a edição estava incompleta. | Usa `==`, normaliza `novo_status`, valida e atualiza somente o registro escolhido. |
| Campo desconhecido | Podia pedir e alterar empresa antes de emitir o aviso. | Informa `Valor invalido.` e volta à seleção sem alterar registros. |
| Continuidade | A edição estava parcial. | Após empresa, cargo ou status válidos, o programa lista o resultado e permite editar novamente. |

As revisões intermediárias de 08/10 também corrigiram a normalização da variável do novo status, a posição do `break` e a orientação da pergunta de campo. Elas fazem parte do caminho até o ZIP final; não são apresentadas como releases independentes.

## Bug explicado pelo autor: número e índice

O autor relatou que, ao escolher uma candidatura, o programa tentava alterar a posição seguinte. A numeração mostrada ao usuário começa em 1, enquanto os índices da lista começam em 0.

| Escolha do usuário | Índice correto | Registro |
| --- | --- | --- |
| `1` | `0` | Primeira candidatura. |
| `2` | `1` | Segunda candidatura. |

Com duas candidaturas, o índice `2` corresponderia a um terceiro registro, inexistente. Usar o número `2` diretamente para acessar a lista poderia gerar `IndexError`.

A correção relatada foi criar uma variável própria:

```python
indice = alteracao - 1
```

Assim, a entrada `2` produz o índice `1`. O autor informou que conferiu essa escolha e conseguiu alterar a segunda candidatura corretamente. A verificação desta publicação também confirmou a edição da segunda candidatura e a preservação da primeira.

Antes dessa conversão, `selecao_valida()` confere a faixa. Portanto, a subtração não transforma uma escolha `0` em um índice negativo válido por acidente.

## Fluxo e responsabilidades

1. `main.py` cria a lista e verifica seu estado vazio com `tratar_lista()`.
2. O cadastro pede os dados de duas candidaturas. Empresa, cargo e status precisam ser válidos antes de `append()` incluir o dicionário.
3. O `for` chama `exibir_candidatura()` para mostrar os registros.
4. Na edição, `int()` converte a escolha. `except ValueError` trata texto não numérico e `selecao_valida()` verifica a faixa.
5. `verificar_alteracao()` recebe o nome do campo e retorna 1, 2 ou 3 para empresa, cargo ou status; um campo desconhecido retorna `False`.
6. O bloco correspondente pede e valida o novo valor antes de atualizar a chave do dicionário selecionado.
7. O laço externo continua, lista os dados atualizados e solicita outra escolha.

Os números retornados por `verificar_alteracao()` pertencem ao controle interno do programa. Na pergunta de campo, o usuário digita palavras. A entrada é preparada com `strip().lower()`.

Na edição de status, `break` encerra o laço de tentativa do novo status. O laço externo continua aberto. Isso permite repetir a edição e conferir os dados na listagem seguinte.

## Verificações executadas

O assistente executou 10 cenários com entradas fornecidas ao programa original, capturando a saída e uma cópia da lista de candidaturas a cada pergunta. As funções importadas e a lógica do aplicativo não foram substituídas.

Após consumir cada sequência, o procedimento pausou a execução na pergunta seguinte. O programa permanece aberto por projeto; essa pausa do procedimento permite conferir o estado final e não representa uma saída implementada no aplicativo.

### Dados usados como base

Salvo o caso de lista vazia e o de entradas inválidas no cadastro, os cenários começam com esta sequência de entradas, uma por pergunta:

```text
Acme
Dev Python
enviada
Beta
Estágio
entrevista
```

Ela produz dois registros: Acme/Dev Python/enviada e Beta/Estágio/entrevista.

### Matriz de resultados

Nas sequências abaixo, cada item entre crases é uma resposta consecutiva. `""` representa Enter sem texto e `"   "` representa somente espaços.

| Cenário | Entradas após o cadastro base | Resultado conferido |
| --- | --- | --- |
| 1. Lista vazia | Nenhuma entrada; pausa na primeira pergunta de empresa. | Aviso `Nenhuma empresa foi cadastrada.` e lista vazia. Passou. |
| 2. Cadastro e listagem | Pausa na primeira seleção. | Dois dicionários distintos e listagem de ambas as candidaturas. Passou. |
| 3. Editar empresa da segunda candidatura | `2`, `empresa`, `""`, `"   "`, ` Gamma ` | Entradas vazias rejeitadas sem alteração; somente empresa da segunda passa a Gamma, com listagem e nova seleção. Passou. |
| 4. Editar cargo da primeira candidatura | `1`, `cargo`, `""`, `"   "`, ` Analista Python ` | Entradas vazias rejeitadas; somente cargo da primeira muda, sem espaços nas extremidades. Passou. |
| 5. Normalizar novo status da primeira | `1`, ` STATUS `, ` RECUSADA ` | Campo reconhecido e status gravado como recusada somente na primeira; nova listagem e seleção. Passou. |
| 6. Selecionar a segunda corretamente | `2`, `status`, `enviada` | Índice 1 usado; somente status da segunda muda. Passou. |
| 7. Seleção inválida | `abc`, `0`, `-1`, `3`, `99`, `2`, `status`, `enviada` | Texto e números fora da faixa rejeitados; registros preservados durante essas tentativas; escolha válida permite editar a segunda. Passou. |
| 8. Campo inexistente | `1`, `outro` | Mensagem de campo inválido; nenhum dado muda e o programa retorna à seleção. Passou. |
| 9. Cadastro e status inválidos | Sequência completa descrita abaixo. | Nenhum registro incompleto é incluído; tentativas de novo status inválido preservam os dois registros. Passou. |
| 10. Alterações consecutivas | `1`, `empresa`, `Gamma`, `2`, `cargo`, `Analista`, `2`, `status`, `enviada`, `1`, `status`, `recusada` | Todos os campos atingem somente seus registros; resultado final listado e fluxo aberto para outra edição. Passou. |

### Sequência do cenário 9

Esta sequência substitui o cadastro base:

```python
[
    "", "   ", " Acme ",
    "", " Dev Python ",
    "pendente", " ENVIADA ",
    "Beta", "Estágio", " entrevista ",
    "1", "status", "", "   ", "pendente", " recusada "
]
```

Empresa e cargo vazios geram nova tentativa. O primeiro status `pendente` é rejeitado antes de incluir o registro. Depois do cadastro, Enter, espaços e `pendente` são rejeitados como novo status sem modificar os dois registros. Apenas ` recusada ` atualiza o status da primeira candidatura, após a normalização.

### Resultado final do cenário 10

| Candidatura | Empresa | Cargo | Status |
| --- | --- | --- | --- |
| 1 | Gamma | Dev Python | recusada |
| 2 | Beta | Analista | enviada |

Os seis arquivos Python foram compilados em Python 3.12 sem avisos de sintaxe. O código desta publicação passou nos 10 cenários descritos; esse resultado se limita aos casos analisados. As verificações não representam uma suíte permanente incluída no repositório nem exercícios adicionais realizados pelo autor.

## Relação com o passo 2 da trilha de estudo

| Critério | Evidência nesta etapa |
| --- | --- |
| Cadastrar duas candidaturas, listar e alterar o status escolhido preservando a outra. | Cenários 2, 5, 6 e 10. |
| Separar funções em módulos e compreender importações e chamadas. | Estrutura dos pacotes e explicação do fluxo no README e neste registro. |
| Validar valor aceito, campo vazio e status inválido sem registrar ou alterar dados inválidos. | Cenários 3, 4 e 9. |
| Reconhecer lista vazia e rejeitar registro inexistente sem encerrar inesperadamente. | Cenários 1 e 7, respeitando o fluxo inicial de dois cadastros. |
| Explicar um bug, sua causa, correção e resultado conferido. | Relato do autor sobre `indice = alteracao - 1` e conferência da segunda candidatura. |

A etapa de cadastro, listagem e edição em memória foi considerada atendida nos cenários revisados e com a explicação apresentada pelo autor. Isso não significa que a aplicação ou a trilha inteira estejam concluídas.

## Limitações mantidas e próximos ajustes

- Os dados ficam somente em memória e desaparecem ao encerrar.
- O fluxo cadastra exatamente duas candidaturas antes da edição.
- Ainda faltam saída pelo menu, exclusão e cadastro de novos registros durante a edição.
- O contador de status inválidos é reiniciado por cadastro e sua impressão fica depois do laço externo sem saída normal.
- A exibição com `capitalize()` muda a capitalização de nomes como IBM.
- `import sys`, o `try` em torno de `return False` e laços redundantes podem ser revisados.

Esses limites estão registrados sem alterar o código do autor nesta publicação. A próxima etapa de estudo é trabalhar a persistência, mantendo melhorias do fluxo como itens de evolução.

## Organização da publicação no GitHub

| Commit | Conteúdo |
| --- | --- |
| `fix(cli): conclui edicao e corrige selecao de candidaturas` | Atualiza o programa e as operações com o código do ZIP, incluindo faixa, índice, edição e continuidade. |
| `docs: registra v0.0.5-prototype e conclusao da edicao em memoria` | Atualiza README e CHANGELOG e acrescenta este registro técnico com evidências e limites. |

O estado parcial de 07/10 está preservado na branch [`historico/v0.0.4-wip`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.4-wip), no [commit original](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/6c4e772cbdb3d15ba458eae8672a06865f669ded) e no [registro daquela etapa](2026-10-07-cadastro-memoria-edicao-parcial.md).

A previsão registrada em 07/10 para continuar a publicação em 08/10 permanece no histórico como planejamento daquela data. Esta nova versão registra o que foi efetivamente entregue: edição dos três campos com seleção validada e continuidade. Contador, saída e persistência seguem descritos como ajustes ou etapas futuras.

Os documentos, a imagem original e as branches anteriores permanecem preservados. A publicação acrescenta commits sem reescrever o histórico. Nenhum cache Python gerado durante a análise é incluído.
