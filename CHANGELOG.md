# Histórico de evolução

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
