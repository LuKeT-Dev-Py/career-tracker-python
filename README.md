# Career Tracker

Projeto de estudo em Python para acompanhar candidaturas pelo terminal e registrar minha evolução em programação.

**Versão atual: `v0.0.4-wip`, registrada em 07/10/2026. Esta é uma versão parcial, em desenvolvimento.**

> **Está prevista para amanhã, 08/10/2026, a publicação da versão completa das funcionalidades que ficaram em aberto nesta etapa.** A continuação envolve concluir a edição de cargo e status e corrigir o fluxo de alteração de empresa e seleção de candidaturas. Essa previsão corresponde ao planejamento informado pelo autor em 07/10/2026.
>
> O cadastro e a listagem já funcionam. A edição ainda contém trechos incompletos e erros conhecidos, descritos abaixo. O código publicado registra o estado atual do aprendizado.

## O que funciona nesta etapa

- Cadastro de duas candidaturas por execução, quantidade definida no código.
- Entrada de empresa, cargo e status pelo terminal.
- Repetição da pergunta de empresa quando o nome está vazio ou contém apenas espaços em branco.
- Repetição da pergunta de cargo quando a entrada está vazia após `strip()`.
- Repetição da pergunta de status até receber uma das opções permitidas: `enviada`, `entrevista` ou `recusada`.
- Limpeza dos espaços nas extremidades da empresa e do cargo; normalização do status com `strip().lower()`.
- Armazenamento das candidaturas em uma lista de dicionários durante a execução.
- Exibição de empresa, cargo e status; listagem numerada na entrada do fluxo de edição.
- Tratamento de texto não numérico ao solicitar o número da candidatura, com nova tentativa após `ValueError`.

**O armazenamento é somente na memória do programa.** Os dados não permanecem disponíveis entre execuções e não são gravados em arquivo ou banco de dados.

## O que ainda está em desenvolvimento

| Parte | Estado publicado em 07/10/2026 | Continuação prevista para 08/10/2026 |
| --- | --- | --- |
| Seleção da candidatura | Converte a entrada para inteiro, mas não verifica se o número está entre 1 e o total de candidaturas. | Validar a faixa antes de acessar a lista. |
| Edição de empresa | Existe código para pedir e validar o novo nome, mas o índice e a posição do bloco estão incorretos. | Fazer a alteração atingir somente a candidatura e o campo escolhidos. |
| Edição de cargo | Bloco marcado com `# Proximo` e `...`, sem atualização do cargo. | Implementar e validar a alteração. |
| Edição de status | Bloco marcado com `# Proximo` e `...`; a identificação do campo usa `is`. | Corrigir a comparação e implementar a alteração com validação de status. |
| Campo inválido | A pergunta de nova empresa ainda acontece antes do aviso `Valor invalido.`. | Rejeitar o comando antes de qualquer alteração. |
| Contador de status inválidos | Reinicia a cada candidatura e é exibido apenas depois de sair do fluxo de edição. | Revisar seu escopo e o momento de exibição. |

A versão completa prevista para 08/10/2026 se refere às partes em aberto desta etapa. Persistência em banco de dados e outros planos de longo prazo ainda não fazem parte dela.

## Como executar

É necessário ter Python 3 instalado. Não há dependências externas nem configuração de banco de dados.

```bash
git clone https://github.com/LuKeT-Dev-Py/career-tracker-python.git
cd career-tracker-python/career_tracker
python3 main.py
```

Se você já baixou o projeto, entre na pasta `career_tracker` e execute `python3 main.py`. No Windows, o comando pode ser `python main.py` ou `py main.py`.

O programa pede os dados de duas candidaturas. Ao terminar o cadastro, exibe os registros e entra no fluxo de edição ainda incompleto. Para interromper a execução no terminal, use `Ctrl+C`; ainda não existe uma opção própria de saída.

Para consultar o protótipo anterior à edição parcial, use a branch [`historico/v0.0.3-prototype`](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.3-prototype).

## Exemplo do cadastro e da listagem

Uma sequência de entradas válidas:

| Candidatura | Empresa | Cargo | Status |
| --- | --- | --- | --- |
| 1 | `Acme` | `Dev Python` | `enviada` |
| 2 | `Beta` | `Estágio` | `entrevista` |

Ao entrar no fluxo de edição, a listagem apresenta:

```text
Candidatura: 1
Empresa: Acme | Cargo: Dev Python | Status: Enviada
Candidatura: 2
Empresa: Beta | Cargo: Estágio | Status: Entrevista
```

Empresa, cargo e status inválidos geram mensagens para tentar novamente. A parte de edição não é apresentada como concluída nesta versão.

## Organização e conceitos praticados

| Arquivo | Responsabilidade no código atual |
| --- | --- |
| `career_tracker/main.py` | Coletar e validar os dados com laços, criar os dicionários, preencher a lista, listar as candidaturas e iniciar a edição parcial. |
| `career_tracker/validacoes/empresa.py` | `limpar_empresa(nome)` remove espaços nas extremidades; `empresa_preenchida(nome)` verifica se há conteúdo. |
| `career_tracker/validacoes/status.py` | `normalizar_status(texto)` prepara o texto; `validar_status(status)` verifica os três valores permitidos. |
| `career_tracker/candidaturas/operacoes.py` | `exibir_candidatura(empresa, status, cargo)` exibe os dados; `tratar_lista(lista)` verifica se há elementos; `verificar_alteracao(alteracao)` identifica o campo solicitado, com pendência na comparação de status. |
| Arquivos `__init__.py` | Identificar os diretórios de validações e candidaturas como pacotes Python regulares. |

Cada candidatura é um dicionário com as chaves `empresa`, `cargo` e `status`. Um novo dicionário é criado a cada volta do cadastro e incluído em `empresas_cadastradas` com `append()`. O `for` percorre essa lista para exibir os registros.

Os laços `while` permitem novas tentativas. `continue` inicia a próxima volta do laço em que está, e `break` encerra esse laço. A conversão `int()` permite escolher um registro por número; o `try`/`except ValueError` trata a falha dessa conversão, mas ainda falta validar a faixa do número escolhido.

O [registro técnico desta etapa](docs/2026-10-07-cadastro-memoria-edicao-parcial.md) explica esses conceitos, os problemas encontrados e os critérios para verificar a continuação.

## Problemas conhecidos

- Ao pedir a alteração da empresa da candidatura 1, o código pode atualizar a candidatura 2. Ao selecionar a 2, pode acessar uma posição inexistente e gerar `IndexError`.
- A numeração exibida começa em 1, enquanto os índices da lista começam em 0. A conversão do número escolhido ainda está inconsistente.
- A pergunta de nova empresa está fora do bloco que deveria executá-la somente para esse campo. Escolher cargo, status ou um campo inválido também pode modificar a empresa.
- A expressão `alteracao is 'status'` compara a identidade dos objetos, não o conteúdo das strings. Ela gera `SyntaxWarning` e pode rejeitar o comando `status`.
- A edição de cargo e status ainda não atualiza esses campos; `...` é um marcador de continuação.
- O contador de status inválidos representa apenas as tentativas da última candidatura, pois é reiniciado a cada cadastro.
- O `try` em volta de `return False` no validador de status não captura um erro útil nesse trecho: esse retorno não gera `ValueError`.
- `capitalize()` continua alterando a capitalização dos nomes das empresas: `IBM` aparece como `Ibm`.
- Não há persistência, exclusão, quantidade de cadastros escolhida pelo usuário nem comando explícito de saída.

## Verificação desta publicação

Foram analisados 12 cenários, incluindo cadastro, repetição de entradas, listagem, escolha numérica e edição. Eles confirmaram os comportamentos de cadastro e os defeitos da edição descritos acima. Os arquivos Python têm sintaxe executável, com um `SyntaxWarning` na comparação de status.

Essas verificações foram executadas pelo assistente sobre o código enviado pelo autor. **Elas não significam que a edição está concluída ou que todos os fluxos funcionam.** Os resultados estão no [registro técnico](docs/2026-10-07-cadastro-memoria-edicao-parcial.md#verificações-executadas). A lógica do ZIP foi preservada para registrar esta etapa; as correções ficam para a continuação.

## Histórico de evolução

| Versão | Registro | Etapa | Onde consultar |
| --- | --- | --- | --- |
| `v0.0.1-prototype` | 24/09/2026 | Entrada de empresa e status, validação e exibição em módulos. | [Primeira versão completa](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.1-prototype). |
| `v0.0.2-prototype` | 28/09/2026 | Validação de empresa e integração dos exercícios 4 e 5. | [Versão preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.2-prototype) e [registro da prática](docs/2026-09-28-validacao-empresa.md). |
| `v0.0.3-prototype` | 02/10/2026 | Limpeza de entradas, normalização de status e fluxo com `if`/`elif`/`else`. | [Versão completa preservada](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.3-prototype) e [registro técnico](docs/2026-10-02-normalizacao-entradas.md). |
| `v0.0.4-wip` | 07/10/2026 | Cargo, duas candidaturas em memória, novas tentativas e edição parcial. | Código atual e [registro desta etapa](docs/2026-10-07-cadastro-memoria-edicao-parcial.md). |

A publicação acrescenta commits de código e documentação sem reescrever o histórico. Os READMEs, códigos e demais arquivos das versões anteriores continuam acessíveis pelas branches históricas. O [CHANGELOG](CHANGELOG.md) mantém os registros de todas as etapas. A [imagem de demonstração](docs/demonstracao.png) corresponde à primeira versão.

## Planos após esta etapa

- Ampliar o tratamento de erros e revisar a apresentação dos nomes das empresas.
- Permitir registrar e consultar uma quantidade variável de candidaturas.
- Implementar persistência, com PostgreSQL como possibilidade futura.

Esses itens ainda são planos. A prioridade informada para 08/10/2026 é concluir e corrigir o que ficou em aberto no fluxo atual de edição.
