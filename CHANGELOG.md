# Histórico de evolução

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
