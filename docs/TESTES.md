# Testes do Career Tracker

O arquivo [career_tracker/test_persistencia.py](../career_tracker/test_persistencia.py) reúne os testes automatizados da versão atual. A suíte usa `unittest`, da biblioteca padrão, e contém **8 testes em 3 classes**.

## Como executar

A partir da raiz do repositório:

```bash
cd career_tracker
python3 -B -m unittest -v test_persistencia
```

Se você já estiver na pasta `career_tracker`, execute somente a segunda linha. No Windows, use `py -B -m unittest -v test_persistencia` na mesma pasta. O projeto requer Python 3.12 ou superior.

Os testes de integração preparam uma cópia do código e arquivos fictícios em diretórios temporários. A suíte não precisa de um JSON de candidaturas real nem altera o arquivo local do programa.

## Cenários cobertos

| Classe | Quantidade | O que verifica |
| --- | --- | --- |
| `TestPersistencia` | 6 testes | Cadastro, edição e recuperação em novas execuções; primeiro uso sem cadastro; lista vazia válida; arquivos inválidos sem sobrescrita; entradas inválidas sem alteração; falha simulada ao substituir o JSON. |
| `TestResumoCandidaturas` | 1 teste | Resumo de três candidaturas, com uma entrevista e duas vagas da mesma empresa. |
| `TestSelecaoCandidatura` | 1 teste | Com duas candidaturas, as escolhas `0`, `1` e `3` retornam `False`, `True` e `False`. |

Os casos de arquivos inválidos são avaliados por subtestes dentro de um método. Por isso, o total exibido pelo `unittest` é oito testes, mesmo havendo várias entradas verificadas.

Um resultado `OK` confirma as expectativas desses cenários na execução realizada. Ele não significa que todos os comportamentos possíveis estejam cobertos ou que a leitura detalhada da suíte tenha sido concluída.

## Origem e contribuições

- Os seis testes iniciais de `TestPersistencia` foram acrescentados pelo assistente de IA em 03/11/2026, no [commit e851996](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/e851996796d1500a02c6471bf24cbeae7cdca8b0), junto de ajustes do projeto.
- O teste de resumo com empresa repetida foi implementado pelo autor com orientação, conforme seu registro no README e o [commit de 23/11](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/dbdf986510c59a8e0849eacae6984530b83c8162).
- O teste dos limites da seleção foi acrescentado no [commit de 27/11](https://github.com/LuKeT-Dev-Py/career-tracker-python/commit/2d73dc3d3a689ba4bc1974d352d4c66ef7956d20), como evolução posterior da suíte.

Essas contribuições devem ser consideradas individualmente. A origem da suíte inicial não atribui automaticamente à IA todos os testes posteriores, e a presença dos arquivos no repositório não declara domínio independente de todo o código pelo autor.

## Registros de execução

| Data | Responsável | Registro |
| --- | --- | --- |
| 03/11/2026 | Assistente | Sete testes aprovados com Python 3.12.14 na publicação original, cuja composição diferia da atual. |
| 24/11/2026 | Assistente | Sete testes aprovados com Python 3.12.3, conforme o registro anterior do README. |
| 24/11/2026 | Autor | Execução dos sete testes confirmada no README, com `python3 -B -m unittest -v test_persistencia`; o autor informou ter revisado diretamente aquela atualização da seção. |
| 27/11/2026 | Assistente | Oito testes aprovados com Python 3.12.14 sobre o commit `2d73dc3d3a689ba4bc1974d352d4c66ef7956d20`. |

A execução mais recente foi feita nesta revisão de documentação. Também foi conferida a demonstração do README: cadastrar, editar o status, encerrar e reabrir o programa a partir de outra pasta, mantendo o registro e recuperando a entrevista.

Os registros do assistente e do autor não são intercambiáveis. Não há aqui uma confirmação do autor de execução dos oito testes atuais nem de conclusão da análise integral da suíte.

## Acompanhamento de estudo

O [plano de revisão guiada](revisao-guiada-test_persistencia.md) registra a preparação dos testes, entradas automáticas, execuções, cenários de erro e preservação de arquivos. O planejamento original de novembro e os avanços posteriores são mantidos com suas datas. A conclusão depende da compreensão demonstrada pelo autor, sem ser presumida pela passagem do calendário ou por um resultado `OK`.

[Voltar ao README](../README.md#testes)
