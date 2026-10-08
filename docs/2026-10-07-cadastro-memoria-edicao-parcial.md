# Evolução de 07/10/2026: cadastro em memória e edição parcial

## Estado e continuação prevista

**Registro parcial: `v0.0.4-wip`. Está prevista para 08/10/2026 a publicação da versão completa das partes que ficaram em aberto nesta etapa, conforme o planejamento informado pelo autor.**

O código vem do arquivo `career_tracker(4)(1).zip` e foi comparado com a `v0.0.3-prototype`, publicada no commit [`acbe8e9`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/acbe8e93f87165fcee5a6ea1877c718cb45b8bac). O autor informou que continuará o trabalho no dia seguinte. A edição de cargo e status, os erros da edição de empresa e a seleção dos registros permanecem em aberto neste registro.

O assistente analisou e verificou o código, preparou a documentação e organizou a publicação. A lógica enviada foi preservada. O marco não é uma versão completa da aplicação nem inclui persistência em banco de dados.

## Mudanças em relação à v0.0.3

| Parte | v0.0.3-prototype | v0.0.4-wip |
| --- | --- | --- |
| Campos | Empresa e status. | Empresa, cargo e status. |
| Cadastro | Uma candidatura por execução. | Duas candidaturas por execução, definidas no código. |
| Entrada inválida | Mostrava a mensagem de erro. | Repete a pergunta de empresa, cargo ou status até receber uma entrada válida. |
| Momento da validação | Coletava empresa e status antes de validar. | Valida a empresa antes de pedir cargo e status. |
| Armazenamento durante a execução | Apenas variáveis de uma candidatura. | Lista de dicionários com as duas candidaturas. |
| Listagem | Exibição de uma candidatura. | Percorre a lista e numera os registros na entrada do fluxo de edição. |
| Edição | Não implementada. | Estrutura parcial, com erros e marcadores de continuação. |
| Dados entre execuções | Não persistidos. | Continuam não persistidos. |

## Como o código atual funciona

### Cadastro e estrutura de dados

O contador `empresas_a_cadastrar` começa em 1, e `while empresas_a_cadastrar <= 2` determina duas rodadas de cadastro. Isso é um limite fixo no código, não uma quantidade escolhida pelo usuário.

A empresa é limpa com `limpar_empresa()` e validada por `empresa_preenchida()`. O cargo recebe `strip()` e precisa ter conteúdo. O status é normalizado com `strip().lower()` e precisa ser `enviada`, `entrevista` ou `recusada`.

Em cada rodada, um novo dicionário é criado com as chaves `empresa`, `cargo` e `status`. As atribuições por chave preenchem esse dicionário. `empresas_cadastradas.append(candidatura)` inclui o registro na lista, que permanece na memória enquanto o processo está ativo. Criar um novo dicionário dentro do laço evita que os dois registros sejam o mesmo objeto.

`for emprise in empresas_cadastradas` percorre os registros. A variável `emprise` recebe um dicionário por vez; suas chaves fornecem os argumentos para `exibir_candidatura(empresa, status, cargo)`. Na edição, `n` começa em 1 para a numeração visível. A listagem aparece após o cadastro e novamente no início do laço de edição.

### Laços e novas tentativas

Os `while` internos mantêm a pergunta do campo atual. Um `continue` volta ao começo do laço mais próximo; ele não reinicia todo o cadastro. Um `break` sai desse laço, permitindo avançar ao próximo campo.

No cargo, a variável começa como `False` e passa a conter a string preenchida. Uma string não vazia é verdadeira em uma condição, e `while not cargo` deixa de repetir a pergunta.

A função `tratar_lista(lista)` retorna `True` quando a lista tem elementos e `False` quando está vazia. No fluxo normal desta versão, o cadastro precisa preencher duas candidaturas antes de chegar à listagem.

### Seleção numérica e tratamento de erro

`int(alteracao)` converte o texto recebido em inteiro. Letras ou outras entradas que não representam inteiros geram `ValueError`; o `except` mostra uma mensagem e repete a pergunta.

Essa conversão confirma o tipo de entrada, mas não confirma que existe uma candidatura com aquele número. A lista de duas candidaturas tem os índices 0 e 1. A numeração exibida ao usuário é 1 e 2. É necessário validar a faixa e converter a numeração de maneira consistente antes de acessar o registro.

## Pendências confirmadas

### Índice da alteração de empresa

O trecho de empresa diminui `alteracao` em 1 para exibir o nome atual, mas aumenta novamente antes da atribuição do novo nome. A gravação acaba usando a numeração exibida como índice da lista.

Nas verificações, escolher a candidatura 1 e o campo empresa alterou o segundo registro. Escolher a candidatura 2 gerou `IndexError` na atribuição. O número 0 também foi aceito e modificou um registro; selecionar 99 gerou `IndexError` ao tentar ler o nome atual.

### Posição do bloco de nova empresa

O `while True` que pergunta a nova empresa está fora de `if valor == 1`. Por isso, é executado também quando o campo escolhido é cargo, status ou um comando inválido. A seleção de cargo alterou a empresa do segundo registro, mantendo o cargo original. Um campo inválido também permitiu essa alteração antes de mostrar `Valor invalido.` e sair do laço.

### Comparação do campo status

A expressão `alteracao is 'status'` verifica se os operandos são o mesmo objeto na memória. Ela não compara o conteúdo dos textos. Strings com o mesmo conteúdo podem ser objetos diferentes, por isso essa comparação pode falhar dependendo de como a string foi criada.

O campo status construído em tempo de execução retornou `False` na verificação da função. Na execução do programa, escolher status também foi rejeitado. O Python emitiu `SyntaxWarning` para essa linha. A continuação deve usar uma comparação de conteúdo para reconhecer o campo.

### Marcadores de cargo e status

Os blocos `if valor == 2` e `if valor == 3` contêm `# Proximo` e `...`. A expressão `...` é o objeto `Ellipsis`; usada sozinha nesse bloco, não implementa uma ação nem atualiza o dicionário. Os campos cargo e status ainda não têm edição implementada.

### Contador e encerramento

`contador = 0` fica dentro do laço de cadastro, então as tentativas inválidas da primeira candidatura são descartadas quando começa a segunda. Em um cenário com dois status inválidos no primeiro cadastro e um no segundo, a saída final mostrou 1.

O contador é impresso depois do laço de edição. Esse laço não tem opção explícita de saída; o caminho atual de campo inválido o interrompe, após executar indevidamente o bloco de empresa. O posicionamento do contador e a forma de terminar a interação ainda precisam de revisão.

### Outros pontos observados

- O `try` em torno de `return False` no validador de status não trata uma operação capaz de gerar `ValueError` naquele trecho.
- `import sys` não é usado no código atual.
- `capitalize()` altera a capitalização dos nomes das empresas; esse comportamento já existia antes.
- Não há validação da existência real da empresa, armazenamento entre execuções, exclusão ou quantidade variável de cadastros.

## Verificações executadas

O assistente verificou 12 cenários em 07/10/2026. O objetivo foi identificar o comportamento real, incluindo os defeitos, e não declarar a edição concluída. As verificações usaram entradas controladas e examinaram a saída e os dicionários em memória. Nos cenários que chegavam a uma nova pergunta, a execução foi interrompida de forma controlada pela ferramenta de verificação. Essa interrupção não é um recurso de saída do programa.

| Cenário | Resultado observado |
| --- | --- |
| Cadastro e listagem de duas candidaturas | Dois dicionários em uma lista; entrada no fluxo de edição após o segundo cadastro. |
| Repetição de entradas inválidas e normalização | Empresa, cargo e status são perguntados novamente; espaços nas extremidades são removidos. |
| Seleção com texto em vez de inteiro | O ValueError da conversão int() é tratado e a pergunta é repetida. |
| Editar empresa da candidatura 1 | Defeito confirmado: altera a empresa da candidatura 2. |
| Editar empresa da candidatura 2 | Defeito confirmado: usa índice 2 em uma lista com índices 0 e 1 e encerra com IndexError. |
| Selecionar candidatura 0 | Defeito confirmado: número fora da faixa aceita e modifica um registro. |
| Selecionar candidatura 99 | Defeito confirmado: falta validar a faixa do número escolhido. |
| Escolher edição de cargo | Defeito confirmado: pergunta por empresa e altera esse campo; cargo permanece igual. |
| Escolher edição de status | Nesta execução, status foi rejeitado pela comparação is; a pergunta e alteração de empresa ocorreram antes do erro. |
| Contagem e campo de edição inválido | Três status inválidos no cadastro, mas contador final é 1; campo inválido ainda permite alterar empresa antes de sair. |
| Lista vazia e lista preenchida | tratar_lista() retorna False para lista vazia e True para lista com conteúdo. |
| Identificação dos campos de edição | empresa e cargo são reconhecidos; status construído em tempo de execução falha pela comparação de identidade is. |

Todos os arquivos Python puderam ser compilados, com `SyntaxWarning` na comparação de status. A sintaxe executável não garante a correção do fluxo. A tabela registra tanto comportamentos funcionais quanto erros reproduzidos. Esses cenários foram executados pelo assistente e não representam novos exercícios respondidos pelo autor nem uma suíte de testes adicionada ao repositório.

## Critérios para conferir a continuação de 08/10/2026

Esta lista serve como roteiro de verificação das pendências, sem apresentar uma implementação pronta:

- Selecionar 1 deve afetar somente o primeiro registro; selecionar 2, somente o segundo.
- Zero, números negativos, valores maiores que a lista e texto não numérico devem ser rejeitados sem alterar dados.
- Escolher empresa deve perguntar e validar somente a empresa; escolher cargo ou status deve atuar somente no respectivo campo.
- Cargo vazio deve permitir nova tentativa, e status fora das três opções deve ser rejeitado antes da atualização.
- Um campo de edição inválido deve mostrar o erro antes de qualquer alteração.
- Após cada alteração válida, a listagem deve refletir o novo valor, preservando os demais campos e registros.
- O escopo do contador e a forma de sair da interação precisam estar definidos e descritos conforme o comportamento implementado.

A publicação da versão completa dessas partes está prevista para 08/10/2026. A previsão é do autor e não transforma as pendências em funcionalidades já disponíveis.

## Commits e preservação do histórico

| Ordem | Mensagem | Escopo |
| --- | --- | --- |
| 1 | `feat(candidaturas): registra cadastro em memoria e edicao parcial` | Código do ZIP, com cargo, duas candidaturas, repetição das entradas e estrutura de edição ainda incompleta. |
| 2 | `docs: explica v0.0.4-wip e continuacao prevista para 08-10` | README completo, CHANGELOG e análise técnica desta etapa, com destaque para a continuação no dia seguinte. |

A `v0.0.3-prototype` permanece completa na branch [`historico/v0.0.3-prototype`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.3-prototype). As versões anteriores e seus READMEs também continuam acessíveis. Os registros de [28/09](2026-09-28-validacao-empresa.md) e [02/10](2026-10-02-normalizacao-entradas.md) foram preservados, e a publicação acrescenta commits sem reescrever o histórico.
