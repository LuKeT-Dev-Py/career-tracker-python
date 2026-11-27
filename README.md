# Career Tracker

Aplicação de terminal em Python para organizar candidaturas a vagas. Permite cadastrar empresa, cargo e status, consultar os registros e atualizar uma candidatura conforme o processo seletivo avança. Os dados ficam em um arquivo JSON local e são recuperados na próxima execução.

É meu projeto principal de estudo em Python. Começou com registros em memória e evoluiu para persistência entre sessões, tratamento de erros e testes automatizados. O histórico registra minhas implementações e as contribuições feitas com apoio de IA.

**Em desenvolvimento · Python 3.12+ · JSON · unittest**

## Funcionalidades

- Cadastrar candidaturas com os status `enviada`, `entrevista` ou `recusada`.
- Listar os registros e editar empresa, cargo ou status da candidatura escolhida.
- Recuperar os dados ao abrir e salvar cadastros e edições no mesmo arquivo.
- Mostrar o total de candidaturas e de entrevistas na abertura.
- Rejeitar campos vazios, status inválidos e seleções inexistentes ou não numéricas.
- Informar problemas de leitura e preservar o JSON anterior se a substituição do arquivo falhar.

## Como executar

Requer **Python 3.12 ou superior**. O projeto usa somente a biblioteca padrão, sem instalação de dependências externas.

```bash
git clone https://github.com/LuKeT-Dev-Py/career-tracker-python.git
cd career-tracker-python/career_tracker
python3 main.py
```

No Windows, dentro da mesma pasta, use `py main.py` ou `python main.py`, conforme sua instalação. Confira a versão do interpretador com `py --version` ou `python --version`.

### Navegação no terminal

1. Na abertura, confira os registros recuperados. No primeiro uso, o programa informa que ainda não há arquivo.
2. No primeiro menu, digite `1` para cadastrar uma nova candidatura ou `0` para continuar sem cadastrar. Se não houver registros e você escolher `0`, a sessão é encerrada.
3. No segundo menu, digite `1` para editar ou `0` para encerrar sem editar.
4. Na edição, escolha o número da candidatura e informe o campo por extenso: `empresa`, `cargo` ou `status`.
5. Digite o novo valor. O programa salva a alteração e mostra a listagem atualizada. Na próxima seleção de candidatura, `0` encerra a sessão.

Uma entrada como ` ENTREVISTA ` é normalizada para `entrevista`. Valores inválidos geram uma nova tentativa antes da atualização do registro.

## Demonstração: salvar, encerrar e recuperar

Em uma instalação sem registros, escolha `1` no primeiro menu e cadastre os dados fictícios **Acme / Estágio Python / enviada**. No segundo menu, escolha `1` para editar. Selecione a candidatura `1`, o campo `status` e informe `entrevista`. Saia com `0` na próxima seleção.

Execute `python3 main.py` novamente. A abertura apresenta:

```text
=== Candidaturas recuperadas ===
Total de candidaturas: 1
Candidaturas em entrevista: 1

Empresa: Acme | Cargo: Estágio Python | Status: Entrevista
```

Para apenas consultar e encerrar, escolha `0` nos dois menus. Se optar por cadastrar em uma próxima sessão, o novo registro será acrescentado aos anteriores.

## Armazenamento dos dados

O programa lê e grava `career_tracker/candidaturas_treino.json`. O caminho é definido a partir da pasta do código; iniciar o script de outro diretório não muda o destino. Esse arquivo é local, é criado durante o uso e está no `.gitignore`.

O JSON contém uma lista de objetos com `empresa`, `cargo` e `status`. O conteúdo `[]` é uma lista vazia válida. Arquivos sem conteúdo, malformados ou com registros incompatíveis são recusados antes de qualquer gravação. Para salvar, o programa escreve em um arquivo temporário e depois substitui o anterior.

Se você usava uma versão antiga que gravava em outra pasta, confira a localização e o conteúdo do arquivo antes de copiá-lo para a pasta atual.

## Testes

Dentro da pasta `career_tracker`, execute:

```bash
python3 -B -m unittest -v test_persistencia
```

No Windows: `py -B -m unittest -v test_persistencia`.

A suíte atual tem **8 testes em 3 classes**, cobrindo persistência, resumo e limites da seleção. Nesta revisão de documentação, em **27/11/2026**, o assistente executou os oito testes com Python 3.12.14 e todos passaram. Os testes de integração usam diretórios temporários.

O [guia dos testes](docs/TESTES.md) explica os cenários, a origem das contribuições e os registros de execução. Ele distingue as verificações do assistente das execuções confirmadas pelo autor.

## Organização do código

| Arquivo | Responsabilidade |
| --- | --- |
| [main.py](career_tracker/main.py) | Recuperação inicial, menus, cadastro e edição. |
| [candidaturas/operacoes.py](career_tracker/candidaturas/operacoes.py) | Leitura e gravação JSON, validação da estrutura, seleção e resumo. |
| [configuracoes.py](career_tracker/configuracoes.py) | Caminho do arquivo de candidaturas. |
| [validacoes/](career_tracker/validacoes) | Limpeza da empresa e normalização e validação do status. |
| [modulos.py](career_tracker/modulos.py) | Importações utilizadas pelo programa principal. |
| [test_persistencia.py](career_tracker/test_persistencia.py) | Testes com `unittest`, incluindo execuções do programa em subprocessos. |

## Uso de IA e acompanhamento dos testes

Os seis testes iniciais de persistência foram acrescentados pelo assistente de IA na [publicação de 03/11/2026](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/e851996796d1500a02c6471bf24cbeae7cdca8b0). A IA também auxiliou em ajustes e verificações do projeto. A suíte recebeu depois testes de resumo e seleção, com contribuições registradas no histórico; sua origem não deve ser atribuída integralmente a uma única pessoa.

Já estudei a base de `unittest` e sigo acompanhando o arquivo. Uma execução bem-sucedida não comprova, por si só, a revisão completa da suíte. O [registro da análise guiada](docs/revisao-guiada-test_persistencia.md) mantém o planejamento original e os avanços documentados, sem presumir a conclusão da leitura.

## Escopo e próximos passos

O programa atende ao uso local e individual. Ainda permite cadastrar apenas uma nova candidatura por sessão; para registrar outra, é necessário reabrir. O resumo é calculado na abertura, e a exibição usa `capitalize()`, que pode mudar a capitalização de nomes como `IBM`.

Exclusão, filtros e um menu para vários cadastros na mesma sessão são melhorias futuras. O armazenamento atual é JSON local; não há integração com banco de dados nesta versão.

## Documentação e histórico

- [Índice da documentação](docs/README.md): orientações atuais e registros de evolução.
- [CHANGELOG](CHANGELOG.md): marcos e alterações posteriores.
- [Guia dos testes](docs/TESTES.md): cobertura e evidências de execução.

Autor do projeto: [João Antônio Pires de Campos](https://github.com/LuKeT-Dev-Py).
