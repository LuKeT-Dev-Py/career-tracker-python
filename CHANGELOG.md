# Histórico de evolução

## v0.0.4-wip: 07/10/2026

**Versão parcial. Está prevista para 08/10/2026 a publicação da versão completa das funcionalidades que ficaram em aberto nesta etapa, conforme o planejamento informado pelo autor.**

### Implementado no cadastro e na listagem

- Campo cargo, com remoção de espaços nas extremidades e repetição da pergunta quando vazio.
- Cadastro de duas candidaturas por execução, definido no código.
- Lista de dicionários com empresa, cargo e status, mantida somente na memória do programa.
- Novas tentativas para entradas inválidas de empresa e status.
- Exibição do cargo junto de empresa e status e listagem numerada na entrada do fluxo de edição.
- Tratamento de `ValueError` na conversão do número da candidatura para inteiro.

### Em desenvolvimento

- Edição de empresa com problemas no índice e na posição do bloco de atualização.
- Edição de cargo e status com marcadores `# Proximo` e `...`.
- Validação da faixa do número da candidatura e comparação do campo status.
- Rejeição de campos inválidos antes de qualquer atualização, revisão do contador e definição da saída do fluxo.

### Documentação e análise

- README explica o estado parcial, as funcionalidades disponíveis, os erros conhecidos e a publicação completa prevista para 08/10/2026.
- [Registro técnico da etapa](docs/2026-10-07-cadastro-memoria-edicao-parcial.md) inclui comparação com a v0.0.3, explicações dos conceitos, 12 cenários verificados e critérios para a continuação.
- As verificações confirmaram o cadastro e reproduziram os problemas da edição, incluindo alteração do registro errado e `IndexError`. A comparação com `is` gera `SyntaxWarning`. A edição não é apresentada como concluída.

### Preservado

- Código enviado pelo autor em `career_tracker(4)(1).zip`, sem correção da lógica nesta publicação.
- Versão anterior completa na branch `historico/v0.0.3-prototype` e no [commit anterior](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/acbe8e93f87165fcee5a6ea1877c718cb45b8bac).
- Versões v0.0.1 e v0.0.2, READMEs anteriores, imagem original, registros de estudo e histórico de commits.
- Seções anteriores deste CHANGELOG, mantidas como registro das versões anteriores.

Não há persistência entre execuções. A previsão de conclusão refere-se às pendências desta etapa, não aos planos de banco de dados e outros recursos futuros.

## v0.0.3-prototype: 02/10/2026

Normalização de entradas e organização das condições, conforme o código enviado pelo autor em `career_tracker(3).zip`.

### Adicionado

- `limpar_empresa(nome)` em `validacoes/empresa.py`, com `nome.strip()`.
- `normalizar_status(texto)` em `validacoes/status.py`, com `texto.strip().lower()`.
- [Registro técnico da etapa](docs/2026-10-02-normalizacao-entradas.md), com explicações, comparação entre versões, estrutura dos commits e resultados das verificações.

### Alterado

- `main.py` atribui os valores limpos e normalizados antes de validar e exibir.
- Status com espaços em branco nas extremidades passam a ser aceitos quando correspondem a `enviada`, `entrevista` ou `recusada` após a normalização.
- A limpeza da empresa passa a afetar também o valor exibido.
- Condições aninhadas substituídas por `if not`/`elif not`/`else`, mantendo a prioridade da validação da empresa.
- Mensagens com acentos: `Empresa inválida.` e `Status inválido.`.
- README atualizado para a versão atual, com funcionalidades, execução, estrutura, evolução e limitações.

### Preservado

- `v0.0.2-prototype` completa na branch `historico/v0.0.2-prototype` e no [commit anterior](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/53d5d972f688c8e726a503bd8505a98105176579).
- `v0.0.1-prototype`, documentação dos exercícios 4 e 5, imagem original e todos os commits anteriores.
- Regra dos três status permitidos, rejeição de empresa vazia e lógica de exibição com `capitalize()`.
- As seções anteriores deste CHANGELOG, mantidas como registro daquelas versões.

### Verificação e limites

O assistente executou 8 casos das funções novas e 17 do programa completo. Os 25 casos passaram; os 17 cenários de execução também foram comparados com a versão anterior. A sintaxe dos arquivos Python foi verificada. A matriz está no registro técnico; essas verificações não representam exercícios adicionais do autor nem uma suíte de testes incluída no repositório.

Os caches `__pycache__` e `.pyc` do ZIP não foram publicados. O programa ainda recebe uma candidatura por execução, sem persistência, menu ou edição. A exibição continua alterando a capitalização de nomes como `IBM` para `Ibm`.

## v0.0.2-prototype — 28/09/2026

Prática de validação de entradas, exercícios 4 e 5.

### Adicionado

- `validacoes/empresa.py` com `empresa_preenchida(nome)`, usando `bool(nome.strip())`.
- Registro dos exercícios, análise técnica e resultados da verificação em [docs/2026-09-28-validacao-empresa.md](docs/2026-09-28-validacao-empresa.md).

### Alterado

- `main.py` verifica a empresa antes do status e só exibe a candidatura quando ambas as validações passam.
- A mensagem genérica `Erro` foi substituída por `Empresa invalida.` ou `Status invalido.`.
- README atualizado para descrever as funcionalidades e limitações atuais.

### Preservado

- Versão anterior completa na branch `historico/v0.0.1-prototype` e no [commit original](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/302f336d9bad881d148e4f9ebde75057ddf67b95).
- [README da primeira versão](https://github.com/LuKeT-Dev-Py/career-tracker-python/blob/302f336d9bad881d148e4f9ebde75057ddf67b95/README.md), mantido sem alterações.
- Validador de status, função de exibição, arquivos `__init__.py`, imagem original e demais arquivos anteriores.
- Histórico de commits, sem reescrita.

### Verificação

Executados localmente 5 casos da função de validação e 10 casos do programa completo. Todos passaram. A matriz de resultados está no registro da prática. As verificações desta atualização foram executadas pelo assistente; não representam novos exercícios respondidos pelo autor.

## v0.0.1-prototype — 24/09/2026

Primeira versão publicada, preservada como registro de aprendizado.

- Entrada de empresa e status pelo terminal.
- Status aceitos: `enviada`, `entrevista` e `recusada`.
- Conversão da entrada do status para minúsculas.
- Exibição da candidatura válida; mensagem `Erro` para status inválido.
- Separação em módulos de validação e exibição.
- Empresa vazia ainda era aceita; não havia persistência.

Consulte o [README original](https://github.com/LuKeT-Dev-Py/career-tracker-python/blob/302f336d9bad881d148e4f9ebde75057ddf67b95/README.md) para todas as informações daquela versão.
