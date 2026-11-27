# Template 22 — Análise de impacto da mudança

## Escolha da mudança
O grupo **ainda não escolheu formalmente** a mudança da Etapa 4 (nenhum registro no repositório). **Recomendação: M15 — intervalo mínimo configurável entre publicações no mesmo dia.**

Por que M15:
- Tem relação com uma necessidade real: o cliente já impõe até 2 publicações por dia em horários diferentes (RN03); a dúvida 2 perguntou sobre o intervalo e a resposta atual é "não existe", portanto a regra pode mudar.
- Cabe no escopo e no prazo.
- Avalia o segredo do módulo de Agenda ("controla o planejamento e a organização das publicações").
- Tem critérios objetivos de medida (módulos e arquivos tocados, testes que quebram).

Antes de adotar, o grupo deve confirmar o interesse do cliente e verificar se o catálogo de mudanças da disciplina oferece uma opção equivalente. A escolha final é do grupo.

## Pedido de mudança
- **ID e descrição:** M15 — o sistema deve recusar uma publicação cujo horário esteja a menos de N minutos de outra publicação do mesmo dia. N é configurável; o padrão é 0 (regra desligada, comportamento atual).
- **Origem:** proposta da equipe a partir da dúvida 2; **origem no cliente a confirmar** (hoje o cliente respondeu que não existe intervalo mínimo).
- **Tipo de manutenção:** adição ou modificação de funcionalidade.
- **Cenário de modificabilidade:** C01 (alterar uma regra de organização editorial com impacto controlado).
- **Segredo que deve conter a mudança:** módulo de Agenda e Publicações.
- **Módulo e segredo (Etapa 2):** Agenda e Publicações; segredo: "planejamento e organização das publicações".

## Análise de impacto
Coluna "Previsto" preenchida em **26/11/2026, antes de qualquer implementação** (estimativas do assistente; o grupo deve confirmá-las). "Realizado" e a explicação ficam **pendentes** até a mudança ser implementada.

| Elemento | Previsto | Realizado | Explicação da diferença |
|---|---|---|---|
| Módulos afetados | 1 (Agenda). Eventos e Oportunidades herda o comportamento por chamar `agenda.agendar`, sem alterar código | Pendente | Pendente |
| Arquivos alterados | 4: `app/agenda/service.py`, `tests/test_novos.py` (ou novo arquivo de testes), `docs/03-regras-de-negocio.md`, `docs/09-registro-de-mudancas.md` | Pendente | Pendente |
| Linhas alteradas | Cerca de 15 no código, 35 nos testes e 10 na documentação | Pendente | Pendente |
| Testes existentes que quebram | 0 (padrão 0 minutos; os testes atuais usam horários com 60 minutos de distância ou dias diferentes) | Pendente | Pendente |
| Testes novos | 5: diferença = N−1 recusa; = N aceita; = N+1 aceita; outro dia ignora; N = 0 mantém o comportamento atual | Pendente | Pendente |
| Registros de decisão afetados | Nenhum ADR; a RN03 e o registro M15 são atualizados | Pendente | Pendente |
| Esforço (horas) | 2 a 3 | Pendente | Pendente |
| Como o impacto será medido | `git diff --stat main..<branch>` para arquivos e linhas; `python -m pytest` antes e depois para testes que quebram; contagem dos módulos tocados | Pendente | Pendente |

## Análise final (a responder após implementar)
1. A mudança ficou contida? **Pendente.**
2. A alteração respeitou os segredos e as regras de dependência da Etapa 2? **Pendente.**
3. Quais módulos precisaram ser modificados? **Pendente** (previsão: só Agenda).
4. Houve alterações fora do módulo que deveria conter a mudança? **Pendente.**
5. O que faríamos diferente na Etapa 2 sabendo disso? **Pendente.**

**Pull requests relacionados e comandos usados para medir o impacto:** pendentes.

**Premissas:** a regra considera apenas publicações do mesmo dia; o intervalo é medido em minutos entre horários; o padrão desligado preserva o comportamento atual.
