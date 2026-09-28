# Career Tracker — protótipo

Projeto de estudo em Python para acompanhar a evolução de um programa de candidaturas a vagas. A versão atual recebe empresa e status, valida as entradas e exibe a candidatura no terminal.

> Estado do projeto: `v0.0.2-prototype` — validação de empresa, prática de 28/09/2026. Ainda não há armazenamento de candidaturas.

## O que funciona nesta versão

- Solicita o nome da empresa e o status da candidatura.
- Rejeita empresa vazia ou composta apenas por espaços em branco.
- Valida a empresa antes de verificar o status.
- Aceita `enviada`, `entrevista` e `recusada`; a entrada do status é convertida para minúsculas.
- Exibe a candidatura somente quando empresa e status são válidos.
- Exibe `Empresa invalida.` ou `Status invalido.` conforme a validação que falhou.
- Mantém validação e exibição organizadas em módulos Python.

## Como executar

É necessário ter Python 3 instalado. Na pasta do repositório:

```bash
cd career_tracker
python3 main.py
```

No Windows, o comando pode ser `python main.py`. Não há dependências externas nem configuração de banco de dados.

Exemplo de uso:

```text
Qual empresa você candidatou: Acme

Opções de status: enviada, entrevista, recusada

Qual status da candidatura: enviada
Empresa: Acme | Status: Enviada
```

Com empresa `Acme` e status `pendente`, a saída é `Status invalido.`. Com empresa vazia ou apenas espaços, a saída é `Empresa invalida.`.

## Evolução e versão anterior

| Versão | Marco | Onde consultar |
| --- | --- | --- |
| `v0.0.1-prototype` | Esboço original: entrada de empresa, validação de status e exibição | [Código e README originais](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/302f336d9bad881d148e4f9ebde75057ddf67b95) |
| `v0.0.2-prototype` | Exercícios 4 e 5: validação de empresa e integração no fluxo principal | Código atual e [registro da prática](docs/2026-09-28-validacao-empresa.md) |

A versão anterior completa está preservada na branch [`historico/v0.0.1-prototype`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.1-prototype), com código, README e imagem originais. Os commits anteriores permanecem no histórico.

- [Histórico de mudanças](CHANGELOG.md)
- [README original preservado](https://github.com/LuKeT-Dev-Py/career-tracker-python/blob/302f336d9bad881d148e4f9ebde75057ddf67b95/README.md)
- [Imagem da execução original](https://github.com/LuKeT-Dev-Py/career-tracker-python/blob/302f336d9bad881d148e4f9ebde75057ddf67b95/docs/demonstracao.png) — registro da primeira versão, não da atualização atual.

## Limitações conhecidas

- A candidatura é apenas exibida: nenhum histórico é salvo ou consultado depois que o programa termina.
- `strip()` é usado para verificar se a empresa está preenchida; não altera o valor de `empresa` que será exibido.
- O status é convertido para minúsculas, mas espaços extras não são removidos: ` enviada ` é rejeitado.
- O programa pede uma candidatura por execução e não permite atualização da situação de uma vaga.
- A exibição usa `capitalize()`, que altera as demais letras do nome para minúsculas.
- A validação da empresa verifica apenas se há conteúdo; não verifica a existência real da empresa.

## Próximos passos planejados

- Ampliar o tratamento de erros e a normalização dos dados inseridos.
- Registrar e consultar várias candidaturas.
- Atualizar a situação das vagas.
- Persistir o histórico em PostgreSQL quando a aplicação estiver pronta para isso.

Esses itens são planos; não fazem parte das funcionalidades implementadas.

## Estrutura

```text
career_tracker/
├── main.py
├── candidaturas/
│   ├── __init__.py
│   └── operacoes.py
└── validacoes/
    ├── __init__.py
    ├── empresa.py
    └── status.py
```

Projeto de estudo em desenvolvimento. Cada atualização registra uma etapa do aprendizado.
