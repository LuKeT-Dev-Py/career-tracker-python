# Career Tracker

Career Tracker é um programa de terminal em Python para acompanhar candidaturas a vagas. Você registra a empresa, o cargo e o status, consulta o que já cadastrou e atualiza cada candidatura conforme o processo avança.

**Versão v0.1.0 · 03/11/2026.** O programa agora recupera as candidaturas ao abrir e salva alterações no mesmo arquivo JSON. Dá para encerrar, voltar mais tarde e continuar de onde parou.

É meu projeto principal de estudo em Python. Comecei com uma lista que durava só durante a execução e evoluí o programa até recuperar os registros de uma sessão para outra. Usei o projeto para praticar organização em módulos, validação de entradas, tratamento de erros, leitura e gravação de arquivos e testes com `unittest`.

## Como executar

Use **Python 3.12 ou superior**. O programa usa apenas a biblioteca padrão.

```bash
git clone https://github.com/LuKeT-Dev-Py/career-tracker-python.git
cd career-tracker-python/career_tracker
python3 main.py
```

No Windows, dentro da mesma pasta, use `py main.py` ou `python main.py`, conforme sua instalação.

1. Ao abrir, o programa mostra as candidaturas recuperadas e quantas estão em entrevista. No primeiro uso, ele informa que ainda não há arquivo.
2. Digite `1` para cadastrar uma candidatura. Informe empresa, cargo e um dos status: `enviada`, `entrevista` ou `recusada`. Também é possível escolher `0` para continuar com os dados que já existem.
3. Na tela de edição, digite o número da candidatura e o campo que deseja alterar: `empresa`, `cargo` ou `status`.
4. Digite `0` na tela de edição para encerrar. Cadastros e edições válidas são salvos no momento da alteração.

O programa pede novamente quando a empresa ou o cargo está vazio, o status não é aceito ou o número da candidatura não existe. Espaços nas extremidades são removidos, e um status como ` ENTREVISTA ` é aceito como `entrevista`.

## Experimente salvar e recuperar

Cadastre uma empresa fictícia chamada **Acme**, com o cargo **Estágio Python** e o status **enviada**. Na edição, escolha a candidatura `1`, informe o campo `status` e mude para `entrevista`. Saia com `0` e execute `python3 main.py` novamente. A abertura deve mostrar:

```text
=== Candidaturas recuperadas ===
Total de candidaturas: 1
Candidaturas em entrevista: 1

Empresa: Acme | Cargo: Estágio Python | Status: Entrevista
```

Ao escolher `0` no menu inicial, você segue para a edição sem cadastrar outra vaga. Se escolher cadastrar em uma próxima sessão, o novo registro é acrescentado aos anteriores.

## Onde ficam os dados

O programa principal lê e grava `career_tracker/candidaturas_treino.json`. O caminho parte da pasta do código, por isso executar o programa em outro diretório não cria uma segunda cópia por engano. Os dados ficam no computador e esse arquivo é ignorado pelo Git.

Cada candidatura guarda três campos:

```json
{
  "empresa": "Acme",
  "cargo": "Estágio Python",
  "status": "entrevista"
}
```

O arquivo inteiro contém uma lista desses registros. O conteúdo `[]` é uma lista vazia válida. Um arquivo sem conteúdo, com JSON malformado ou com registros incompletos faz o programa avisar e encerrar, preservando o arquivo para conferência. Ao salvar, o programa escreve primeiro em um arquivo temporário e só depois substitui o JSON anterior.

Se uma versão antiga gravou seus dados em outra pasta, localize o arquivo antigo antes de iniciar novos cadastros. Para reutilizá-lo, coloque uma cópia de `candidaturas_treino.json` ao lado de `main.py`, conferindo se já existe um arquivo nesse local.

## Organização do código

| Arquivo | Responsabilidade |
| --- | --- |
| [main.py](career_tracker/main.py) | Abre os dados salvos, conduz o cadastro e a edição e chama a gravação. |
| [candidaturas/operacoes.py](career_tracker/candidaturas/operacoes.py) | Lê, valida e grava JSON. Também exibe, seleciona e resume candidaturas. |
| [configuracoes.py](career_tracker/configuracoes.py) | Define os caminhos dos arquivos de dados. |
| [validacoes/](career_tracker/validacoes) | Confere o preenchimento da empresa e normaliza e valida o status. |
| [modulos.py](career_tracker/modulos.py) | Reúne as importações usadas pelo programa principal. |
| [conferir_carregamento.py](career_tracker/conferir_carregamento.py) | Lê um arquivo de laboratório e mostra o resumo. Registra a etapa em que pratiquei a leitura antes de integrar ao principal. |

O script de conferência continua disponível para estudo. Por padrão, ele lê `candidaturas_laboratorio.json` ao lado de `main.py`. Esse arquivo é opcional e separado dos dados do programa. Para experimentar, crie ali um JSON com `[]` e execute `python3 conferir_carregamento.py`.

## Testes

Dentro da pasta `career_tracker`, execute:

```bash
python3 -m unittest -v teste test_persistencia
```

No Windows, você pode usar `py -m unittest -v teste test_persistencia`.

Na publicação de 03/11/2026, **o assistente executou 7 testes com Python 3.12.14**. O arquivo `teste.py` verifica o resumo de uma lista vazia; `test_persistencia.py` cobre cadastro e edição em sessões distintas, recuperação dos dados, arquivos inválidos, entradas rejeitadas e preservação do JSON anterior em uma falha de gravação simulada. Esses resultados se referem à verificação do assistente naquela publicação. Execuções realizadas e confirmadas por mim devem ser identificadas separadamente.

## Uso de IA e revisão dos testes

A IA auxiliou na elaboração da suíte `career_tracker/test_persistencia.py` e nas verificações do projeto. Esse arquivo foi acrescentado pelo assistente em 03/11/2026, no [commit `e851996`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/e851996796d1500a02c6471bf24cbeae7cdca8b0), e não foi escrito originalmente por mim. Essa atribuição se refere a essa suíte; a origem dos demais testes deve ser considerada individualmente. O histórico preserva as implementações que desenvolvi e as contribuições do assistente.

Já estudei a base de `unittest` e consigo acompanhar o fluxo, mas a leitura detalhada desse arquivo ainda está pendente. Reservei a semana de **09 a 13/11/2026**, começando na segunda-feira, para uma [análise guiada](docs/revisao-guiada-test_persistencia.md) no lugar do exercício 6 da prática diária. Os exercícios 1–5 e o miniprojeto semanal continuam normalmente.

A revisão avançará conforme minha compreensão. A data prevista e um resultado `OK` na execução, por si só, não significam que concluí a leitura ou compreendi todos os cenários.

## Escopo e histórico

O Career Tracker é um programa local para uso individual. Nesta versão, é possível cadastrar uma nova candidatura por sessão e editar as existentes; para cadastrar outra, reabra o programa. O resumo é calculado na abertura. Exclusão, filtros e um menu para registrar várias candidaturas na mesma sessão ficam para evoluções futuras.

- [CHANGELOG](CHANGELOG.md): mudanças de cada versão.
- [Registro da v0.1.0](docs/2026-11-03-persistencia-json.md): comparação com o protótipo, decisões e resultados da verificação.
- [v0.0.6-prototype](https://github.com/LuKeT-Dev-Py/career-tracker-python/tree/historico/v0.0.6-prototype): etapa em que o principal gravava em JSON e a leitura era feita em um script separado.
- [Documentação anterior](docs/readme-anterior-2026-10-31.md): registro das etapas anteriores.
