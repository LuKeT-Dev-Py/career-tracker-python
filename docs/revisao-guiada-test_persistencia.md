# Revisão guiada de test_persistencia.py

**Estado: leitura detalhada pendente.** Planejamento registrado em 06/11/2026 para a semana de 09 a 13/11/2026, com início na segunda-feira, 09/11.

## Origem e participação da IA

O arquivo `career_tracker/test_persistencia.py` foi elaborado com auxílio de IA e acrescentado pelo assistente durante a atualização de 03/11/2026, no [commit `e851996796d1500a02c6471bf24cbeae7cdca8b0`](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/e851996796d1500a02c6471bf24cbeae7cdca8b0). Essa suíte não foi escrita originalmente pelo autor do projeto. A atribuição não se estende automaticamente a `teste.py` ou a outros arquivos.

As verificações executadas pelo assistente na publicação estão identificadas no README. Elas devem ser diferenciadas dos testes efetivamente executados e confirmados pelo autor. O histórico mantém o reconhecimento das implementações do autor e das contribuições do assistente; não representa autoria integral ou domínio independente de todo o código.

O autor já estudou a base de `unittest` e consegue acompanhar o fluxo, mas ainda precisa fazer a leitura detalhada desta suíte. Este documento registra o plano de estudo, sem declarar essa revisão concluída.

## Plano de leitura

Durante essa semana, a análise substitui apenas o **exercício 6** da prática diária. Os exercícios 1–5 e o miniprojeto semanal continuam normalmente.

| Dia previsto | Foco | O que acompanhar na leitura |
| --- | --- | --- |
| Segunda, 09/11 | Organização e preparação | Identificar a classe de testes, o `setUp()`, os diretórios temporários, a cópia dos arquivos e a limpeza ao final. |
| Terça, 10/11 | Entradas e execuções automáticas | Acompanhar a função `rodar()`, as entradas fornecidas ao programa, o subprocesso, o diretório de execução e a captura de saídas. |
| Quarta, 11/11 | Cadastro, edição e recuperação | Relacionar as sessões do programa aos dados esperados, às comparações e à conferência do JSON salvo. |
| Quinta, 12/11 | Cenários inválidos e preservação | Entender o que cada entrada inválida verifica, como o arquivo anterior é conferido e como a falha de gravação é simulada. |
| Sexta, 13/11 | Explicação e execução | Revisar as próprias explicações, ajustar o necessário e executar a suíte, registrando o resultado e as dúvidas restantes. |

A ordem acompanha a compreensão, não apenas o calendário. Uma etapa pode precisar de mais tempo. Chegar ao dia previsto ou obter `OK` não encerra automaticamente a revisão.

## Como registrar o progresso

Ao avançar, registrar com palavras próprias o que foi entendido, quais dúvidas permanecem e quais cenários foram executados pessoalmente. Identificar cada execução pelo responsável e pelo resultado observado, mantendo separados os registros do assistente e do autor.

A leitura detalhada continuará pendente até que o autor consiga explicar a preparação, as entradas, os resultados esperados e a preservação dos arquivos, além de executar os testes e compreender o alcance de suas verificações.

Comando previsto para a etapa de execução, dentro de `career_tracker`:

```bash
python3 -m unittest -v teste test_persistencia
```

O comando está documentado para o estudo futuro. Esta atualização de documentação não registra uma nova execução nem uma confirmação do autor.

[Voltar ao README](../README.md#uso-de-ia-e-revisão-dos-testes)
