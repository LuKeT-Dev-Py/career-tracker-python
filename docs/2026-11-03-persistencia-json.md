# Persistência de candidaturas no programa principal

Registro da versão **v0.1.0**, publicada em 03/11/2026.

## O que mudou desde a v0.0.6

Na [versão anterior](2026-10-21-json-parcial.md), o principal gravava o JSON, mas iniciava com a lista vazia. A leitura dependia de outro script e de um arquivo de laboratório. Ao concluir novos cadastros, o programa podia substituir os registros da sessão anterior.

O [commit do autor que integra a leitura](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/08b596261e097046938a4b205a218402bee566b9) concluiu o fluxo principal: recuperar os dados ao abrir, cadastrar sem perder os anteriores, continuar sem cadastrar e gravar as edições no mesmo arquivo. O caminho é definido a partir da pasta do programa. O resumo de candidaturas foi extraído para uma função e recebeu um teste de lista vazia nos commits que antecederam a integração.

| Situação | Comportamento na v0.1.0 |
| --- | --- |
| Primeiro uso, sem arquivo | Abre o menu para iniciar um cadastro. |
| Reabertura com dados válidos | Mostra os registros e a contagem de entrevistas. |
| Escolha de cadastrar | Acrescenta uma candidatura e salva a lista. |
| Edição válida | Grava o novo valor no registro selecionado. |
| Arquivo vazio, inválido ou com estrutura incorreta | Informa o problema e preserva o arquivo original. |
| Falha ao substituir o JSON | Informa que a alteração não foi salva. O arquivo anterior permanece. |

## Ajustes feitos na publicação

A comparação confirmou que os 20 arquivos úteis do ZIP eram idênticos aos da branch principal antes da publicação. O pacote local também continha metadados do Git e caches Python, que ficaram fora da atualização. Os JSONs de uso local passaram a ser ignorados pelo Git. O teste do autor em `teste.py` foi preservado.

Durante a revisão, um registro sem `status` ainda causava um erro ao montar o resumo. A leitura agora exige uma lista de objetos com empresa, cargo e status válidos antes que o programa use os dados. O principal também informa erros de arquivo e grava cada alteração em um arquivo temporário antes de substituir a versão anterior. A opção `0` encerra a sessão pela tela de edição.

## Como foi verificado

Em Python 3.12.14, o teste do autor e seis testes adicionais da publicação passaram. A verificação principal executou três sessões independentes em um diretório diferente da pasta do código: cadastrou a primeira candidatura, adicionou uma segunda e editou empresa, cargo e status da primeira, depois reabriu sem cadastrar. Foram conferidos a listagem, a contagem de entrevistas e os registros do JSON.

Também foram verificados o primeiro uso sem arquivo, o carregamento de `[]`, a rejeição de opções inválidas, arquivos malformados ou com estrutura incorreta e uma falha simulada na substituição do arquivo. Nesses casos, o teste confere que o conteúdo anterior não é sobrescrito. Os testes criam dados fictícios em diretórios temporários.

A versão fecha o ciclo de persistência local desta etapa. O menu ainda cadastra uma nova vaga por sessão, e o resumo é atualizado quando o programa é reaberto. Filtros e exclusão ficam para uma próxima versão.
