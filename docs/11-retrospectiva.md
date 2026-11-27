# Template 11 — Registro de etapa, retrospectiva e métricas do processo

**Etapa e período:** Incremento 1 (Etapa 3) — desenvolvimento do primeiro incremento. Período com evidência no repositório: **15/11/2026 a 19/11/2026** (datas dos commits). O período oficial da etapa deve ser conferido com o cronograma do professor.
**Participantes da retrospectiva:** Bruno José Souza e Pablo Gonçalves Barbosa. Este texto é uma proposta redigida a partir das evidências; os dois integrantes devem confirmá-lo ou ajustá-lo.

## Planejado × realizado
| Item planejado | Realizado? | Observação |
|---|---|---|
| Ambiente e estrutura inicial (Python, Flask, SQLite, módulos) | Sim | Cinco módulos em `app/` |
| Agenda editorial (H03, RN03, RN04) | Sim | Implementada e testada; sem validação do cliente |
| Fluxo de produção (H01, H02, RN01) | Sim | Seis estados informados |
| Eventos e oportunidades (H05, H06) | Sim | Situações das oportunidades e tipos de evento são provisórios |
| Materiais (H07, RN07) | Sim | Como referências, sem upload (ADR-003) |
| Login do administrador (C05) | Sim | Básico: sem limite de tentativas e sem HTTPS |
| Testes automatizados | Sim | 27 testes; evidência de TDD não encontrada |
| Padrão Strategy (Template 16) | Não | Nenhum padrão implementado no código |
| Pipeline de integração contínua | Não | Não há `.github/workflows` |
| Revisão de código por pull request | Parcial | Um PR (#18) integrado; revisão não evidenciada |
| Avaliação do primeiro incremento com o cliente | Não | Ata nº 04 pendente |
| Repositório organizado | Sim | Após reorganização em 18/11/2026 |

## Retrospectiva
**O que funcionou (manter):** arquitetura modular com serviços separados (ADR-001); decisões registradas em ADRs; testes automatizados desde o início; uso de Issues e quadro de tarefas; respostas do cliente transformadas em regras e testes; registro de correções (CORR-001, CORR-002).

**O que não funcionou (mudar):** envio de arquivos por upload no navegador gerou arquivos duplicados e versões antigas em `app/` (risco R05 materializado); 5 dos 14 commits têm a mensagem genérica "Add files via upload"; só um PR e nenhum pipeline; nome do cliente ficou em documentos públicos; declarações precisaram ser corrigidas depois (data da ata, uso de IA).

**O que vamos experimentar:** todo trabalho por branch e pull request com revisão do outro integrante; GitHub Actions executando os testes; mensagens de commit descritivas; escrever o teste antes da regra nova (TDD) e registrar os commits; revisar as declarações contra o histórico antes de assinar.

## Mudanças no modo de trabalhar
- **O que mudou:** a reorganização foi feita em branch (`copia-seguranca`) e integrada pelo PR #18 em vez de alterar a `main` diretamente.
- **Por quê:** a bagunça do repositório mostrou o custo de integrar sem revisão.
- **O que ainda não mudou:** não há revisão registrada, pipeline nem TDD; permanecem como ações propostas.

## Riscos
Ver `06-matriz-de-riscos.md`. R01 reduziu de probabilidade (A → M). R05 **materializou** e foi tratado. R09 (nome do cliente no repositório) **materializou** e aguarda correção. Entraram R06 a R10.

## Evidências (obtidas do repositório em 26/11/2026)
- **Commits por integrante:** Bruno José Souza, 10; Pablo Gonçalves Barbosa, 4 (total 14). Os 4 commits do Pablo são envios de documentação em 15/11/2026.
- **Pull requests:** #18 (`copia-seguranca` → `main`), integrado em 18/11/2026 22:03. Autor e revisor não verificados (a consulta à API do GitHub foi bloqueada). Conferir na aba **Pull requests**.
- **Pipeline:** não existe (`.github/workflows` ausente).
- **Atas:** `05-entrevistas-e-atas.md`.
- **Quadro de tarefas:** **anexar print** do quadro em Projects.

## Métricas do processo
| Métrica | Valor | Como foi obtido |
|---|---|---|
| Tarefas concluídas | **Pendente** | Contar os itens em "Done" no quadro de Projects |
| Pull requests integrados | 1 (#18) | `git log --merges` indica um merge de PR; conferir na aba Pull requests |
| Tempo médio até a primeira revisão (h) | **Não calculado** | Exige data de abertura e da primeira revisão do PR; sem revisão registrada |
| Tempo médio até o merge (h) | **Não calculado** | Exige a hora de abertura do PR. Referência parcial: o último commit da branch foi às 20:52 e o merge às 22:03 de 18/11/2026 |
| PRs com pedido de alteração | **Não verificado** | Conferir a aba Conversation do PR #18 |
| Execuções do pipeline com falha | Não se aplica | Não há pipeline |
| Tempo médio para corrigir o pipeline (h) | Não se aplica | Não há pipeline |

## Problema do processo identificado
A integração por upload manual, sem pull request, revisão ou pipeline, deixou o repositório desorganizado e exigiu retrabalho (reorganização de 58 arquivos). Dados: 5 de 14 commits genéricos, 1 PR integrado, 0 execuções de pipeline.

## Melhoria proposta
Exigir pull request com revisão do outro integrante e executar `pytest` no GitHub Actions a cada PR. **Como verificar:** proporção de commits na `main` que vieram de PR; tempo até a primeira revisão; execuções do pipeline com falha.

## Efeito observado
**Pendente.** A melhoria ainda não foi aplicada; não há dados.
