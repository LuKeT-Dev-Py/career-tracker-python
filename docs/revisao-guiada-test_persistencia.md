# Revisão guiada de test_persistencia.py

## Situação registrada em 27/11/2026

**A revisão integral da suíte ainda não tem confirmação de conclusão.** Há avanços posteriores ao planejamento: o autor implementou com orientação um teste de resumo e registrou sua execução dos sete testes em 24/11. Em 27/11, o código recebeu também um teste de limites da seleção.

Esses registros não comprovam, por si só, a leitura detalhada de todos os cenários. As verificações do assistente estão identificadas separadamente no [guia dos testes](TESTES.md).

## Origem e participação da IA

Os seis testes iniciais de persistência foram acrescentados pelo assistente na atualização de 03/11/2026, no [commit e851996](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/e851996796d1500a02c6471bf24cbeae7cdca8b0). A suíte inicial não foi escrita originalmente pelo autor. Os testes posteriores de resumo e seleção são contribuições que devem ser consideradas individualmente, conforme o histórico.

O autor já estudou a base de `unittest` e informou conseguir acompanhar o fluxo, reservando tempo para a leitura detalhada. O histórico mantém o reconhecimento de suas implementações e das contribuições do assistente, sem declarar autoria integral ou domínio independente de todo o código.

## Planejamento original de 06/11/2026

O período de 09 a 13/11/2026 foi reservado para a análise guiada, começando na segunda-feira. A distribuição abaixo é um registro histórico do plano original, não uma declaração de conclusão ou um cronograma futuro. Naquele planejamento, a leitura substituiria o exercício 6, com os exercícios 1 a 5 e o miniprojeto semanal mantidos; isso não define a rotina atual de prática.

| Dia previsto | Foco | O que acompanhar na leitura |
| --- | --- | --- |
| Segunda, 09/11 | Organização e preparação | Identificar a classe de testes, o `setUp()`, os diretórios temporários, a cópia dos arquivos e a limpeza ao final. |
| Terça, 10/11 | Entradas e execuções automáticas | Acompanhar `rodar()`, as entradas fornecidas ao programa, o subprocesso, o diretório de execução e a captura das saídas. |
| Quarta, 11/11 | Cadastro, edição e recuperação | Relacionar as sessões aos dados esperados, às comparações e à conferência do JSON salvo. |
| Quinta, 12/11 | Cenários inválidos e preservação | Entender as entradas inválidas, a conferência do arquivo anterior e a simulação de falha na gravação. |
| Sexta, 13/11 | Explicação e execução | Revisar as próprias explicações, ajustar o necessário e executar a suíte, registrando resultados e dúvidas. |

A ordem acompanha a compreensão. Uma etapa pode exigir mais tempo, e um resultado `OK` ou a passagem de uma data não encerra automaticamente a revisão.

## Como acompanhar os próximos avanços

Registrar com palavras próprias o que foi entendido, as dúvidas restantes e quais cenários foram executados pessoalmente. Identificar o responsável e o resultado observado em cada execução, mantendo separados os registros do assistente e do autor.

Para registrar a conclusão, o autor precisa conseguir explicar a preparação, as entradas, os resultados esperados e a preservação dos arquivos, além de executar os testes e compreender o alcance das verificações. O teste de uma lista vazia do antigo `teste.py` pertence ao histórico; o comando atual utiliza somente `test_persistencia.py`.

Dentro de `career_tracker`, execute:

```bash
python3 -B -m unittest -v test_persistencia
```

As execuções já registradas estão no [guia dos testes](TESTES.md#registros-de-execução). Uma nova execução ou etapa de estudo deve ser registrada com sua data e resultado, sem presumir a compreensão de toda a suíte.

[Voltar ao README](../README.md#uso-de-ia-e-acompanhamento-dos-testes)
