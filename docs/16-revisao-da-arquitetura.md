# Template 17 — Folha de revisão da arquitetura e resposta às revisões

## Parte A — Folha do revisor (revisão individual de Bruno José Souza)
**Projeto revisado:** LocoMat. **Revisor:** Bruno José Souza.

Esta folha usa apenas o que foi informado sobre a revisão. O texto original (frases, justificativas e sugestões) **não está no repositório nem nesta conversa**; Bruno deve transcrevê-lo nos campos abaixo.

| Aspecto revisado | O que foi analisado (conforme informado) | Texto da revisão |
|---|---|---|
| Cenário C01 | Usabilidade | A transcrever |
| Cenário C04 | Rastreabilidade | A transcrever |
| Decisões | ADR-003 e ADR-004 | A transcrever |
| Risco | Concorrência nas reservas | A transcrever |
| Ponto de sensibilidade | Módulo histórico | A transcrever |
| Trade-offs | Monolito modular e histórico somente de acréscimo | A transcrever |
| Segredo do módulo | Módulo acesso | A transcrever |
| Dificuldade | Expansão para várias atléticas | A transcrever |
| Ponto forte | Consistência transacional do histórico | A transcrever |

Não foi feita uma segunda revisão. Se o professor pedir outra revisão individual, o grupo deve informar qual projeto revisar.

## Parte B — Resposta às revisões (grupo revisado: Sistema de Apoio à Gestão de Conteúdo Automotivo)
Nenhuma revisão recebida de outros grupos foi encontrada nos documentos, nas conversas ou no repositório. **Esta parte está pendente.** A revisão feita por Bruno no LocoMat não é uma revisão recebida pelo nosso grupo.

| Revisor | Ponto levantado | Decisão (incorporado / descartado / adiado) | Justificativa ou ajuste feito |
|---|---|---|---|
| A preencher | A preencher | A preencher | A preencher |

**O que o grupo levou das revisões para as próximas etapas:** a preencher após receber as revisões no fórum.

## Pontos de atenção da arquitetura atual (autoanálise, para o grupo considerar ao responder revisões)
- Acoplamento por tabela: Agenda e Eventos leem ou gravam tabelas de outros módulos (detalhes em `17-checklist-revisao-codigo.md`).
- Estados e situações provisórios (oportunidades, tipos de evento).
- Padrão de projeto ainda não implementado (`08-padrao-strategy.md`).
