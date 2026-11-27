# Template 19 — Registro de mudanças

Preserva os registros M01–M10 e acrescenta M11–M15. Datas reais quando constam em commits; "26/11/2026" indica registro feito nesta atualização.

| ID | Data | Itens afetados | Origem | Mudança | Impacto estimado | Decisão e justificativa |
|---|---|---|---|---|---|---|
| M01 | A definir | H03, RN03, C02 | Entrevista com o cliente | Priorizar a agenda de publicações como funcionalidade central da primeira versão | Alto | **Aceita** como prioridade inicial; implementada |
| M02 | A definir | H05, H06, RN02, RN04 | Entrevista com o cliente | Diferenciar solicitações de divulgação antecipada das de cobertura durante ou após o evento | Médio | **Aceita**; implementada como tipos de evento |
| M03 | A definir | H03, RN03, C02 | Informações do cliente | Considerar o limite de até 2 publicações por dia em horários diferentes | Médio | **Aceita**; ponto pendente resolvido por M07 |
| M04 | A definir | H01, H02, H07, RN07 | Observação da rotina e entrevista | Atenção ao registro e acompanhamento de fotos, vídeos e materiais | Alto | **Aceita**; ponto pendente resolvido por M08 |
| M05 | A definir | H03, H04, H05, H06, RN04, RN05 | Análise dos requisitos | Detalhar os critérios de priorização | Médio | **Adiada** até validar os critérios com o cliente (permanece adiada) |
| M06 | 15/11/2026 | RN01, H02 | Respostas à dúvida 3 (informadas pela equipe) | Estados confirmados: ideia, em edição, pronto, agendado, publicado, encerrado | Médio | **Aceita**; implementada |
| M07 | 15/11/2026 | RN03, H03 | Respostas às dúvidas 1 e 2 | O limite de 2/dia apenas avisa; sem intervalo mínimo; mesmo horário recusado | Médio | **Aceita**; implementada |
| M08 | 15/11/2026 | RN07, H07, ADR-003 | Resposta à dúvida 8 | Materiais apenas como referências, sem upload | Alto | **Aceita**; implementada |
| M09 | 15/11/2026 | H03, H04, RN10 | Respostas às dúvidas 7 e 12 | Agenda reorganizável e sugestões por regra semanal | Médio | **Aceita**; implementada |
| M10 | 15/11/2026 | RN06, C01 | Resposta à dúvida 6 | Cadastro das 12 editorias iniciais | Baixo | **Aceita**; implementada |
| M11 | 15/11/2026 | H03, RN09 | Equipe (decisão técnica na implementação) | Criar RN09: conteúdo publicado ou encerrado não pode ser agendado | Baixo | **Aceita**; implementada e testada |
| M12 | 15/11/2026 | ADR-001, ADR-002, ADR-003 | Equipe | ADR-001 passa de Proposto a Aceito; criadas ADR-002 (stack) e ADR-003 (materiais por referência) | Médio | **Aceita**; documentada |
| M13 | 15/11/2026 | H01–H07 | Equipe | Incluir critérios de aceitação nas histórias de usuário | Baixo | **Aceita**; a confirmar com o cliente |
| M14 | 15/11/2026 | H05, H06, RN02, RN08 | Equipe | Definir valores provisórios: situações das oportunidades (nova, em conversa, aceita, recusada, concluída) e tipos de evento | Médio | **Aceita provisoriamente**; confirmar com o cliente |
| M15 | 26/11/2026 | H03, RN03, C01 | Proposta da equipe a partir da dúvida 2 (hoje não há intervalo mínimo); interesse do cliente a confirmar | Intervalo mínimo configurável entre publicações no mesmo dia | Baixo (previsto; ver Template 22) | **Proposta — decisão do grupo pendente.** Candidata à mudança da Etapa 4 |

**Mudança escolhida para a Etapa 4:** ainda não há escolha formal. A recomendação é M15 (justificada em `18-analise-de-impacto.md`).
