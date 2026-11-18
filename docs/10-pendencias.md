# 10 — Pendências e dúvidas para o cliente

## Dúvidas respondidas (informações repassadas pela equipe em 15/11/2026)

| # | Pergunta | Resposta | Onde foi aplicada |
|---|---|---|---|
| 1 | Limite de 2/dia: obrigatório ou aviso? | Apenas avisar | RN03, `agenda/service.py` |
| 2 | Intervalo mínimo entre publicações? | Não existe; só impede o mesmo horário | RN03 |
| 3 | Estados do fluxo | Ideia, em edição, pronto, agendado, publicado, encerrado | RN01, `producao/service.py` |
| 4 | Dados de solicitações de eventos | Nome do evento, data, quem pediu, tipo e prazo | H05, módulo Eventos e Oportunidades |
| 5 | Dados de oportunidades | Nome do contato, canal, proposta e condições, situação | H06 |
| 6 | Nomes das editorias | 12 editorias (ver RN06) | Cadastradas por padrão |
| 7 | Agenda só visualiza ou reorganiza? | Permite reorganizar: mudar data e arrastar | H03 |
| 8 | Materiais no sistema ou referências? | Não haverá upload pelo celular; apenas referências | RN07, ADR-003 |
| 9 | O que é mais prejudicial perder? | Os materiais | `backup.py` (cópia do banco) |
| 10 | Se o sistema cair? | Anotar manualmente e lançar depois | Eventos aceitam datas passadas |
| 11 | IA na edição | Não será automatizada; o cliente usa prompt em IA externa | Fora do escopo |
| 12 | Frequência e dias fixos | Ex.: "domingo: encontro da semana"; vira regra de sugestão | RN10 |

## Pendências que continuam
- **Confirmar com o cliente**, na avaliação do primeiro incremento, os valores de situação das oportunidades (provisórios: nova, em conversa, aceita, recusada, concluída) e os nomes dos tipos de evento.
- Quais dias e frequência semanal fixos o cliente quer cadastrar como regras.
- Priorização automática (RN05) e padrão Strategy: decidir se serão necessários.
- Login: limite de tentativas, recuperação de senha e HTTPS para uso fora do computador local.
- Teste da tela em celular real (arrastar pode não funcionar em toque; há campo de data como alternativa).
- Métricas, evidências, datas da matriz de riscos e do registro de mudanças: preencher com dados reais.
