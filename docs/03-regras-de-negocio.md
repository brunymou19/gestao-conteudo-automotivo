# 03 — Regras de negócio

| ID | Regra | Situação (15/11/2026) |
|---|---|---|
| RN01 | Todo conteúdo tem um estado: ideia, em edição, pronto, agendado, publicado, encerrado. | Definida e implementada |
| RN02 | Solicitações de evento têm tipo (divulgação antecipada, cobertura durante, publicação posterior), data e prazo. Não há antecedência mínima universal. | Implementada |
| RN03 | Até 2 publicações por dia, em horários diferentes. O sistema **apenas avisa** ao passar do limite; **não há intervalo mínimo**, mas o mesmo horário é recusado. | Definida e implementada |
| RN04 | Conteúdos e eventos têm datas e prazos; o que passou do prazo e segue pendente aparece como atrasado. | Implementada |
| RN05 | Priorização por urgência, proximidade de eventos, compromissos, relevância e disponibilidade de materiais. | **Não implementada** (ainda não há priorização automática; ver ficha do Strategy) |
| RN06 | Conteúdos organizados por editoria, com inclusão de novas. Editorias iniciais: Pelo Caminho, Na pista, Garagem da Comunidade, Agenda automotiva, Entenda sua máquina, Ícones, Que carro é esse, Qual você escolhe, Top 5, E se, Bastidores MPM, Classificados MPM. | Implementada |
| RN07 | Materiais são associados aos conteúdos **como referências** (nome do arquivo, pasta ou link). Não há upload pelo celular. | Definida e implementada |
| RN08 | Cada oportunidade é registrada e avaliada individualmente (contato, canal, proposta, condições, situação). | Implementada |
| RN09 | Conteúdos publicados ou encerrados não podem ser agendados novamente. | Regra técnica adicionada pela equipe |
| RN10 | Conteúdos fixos por dia da semana (ex.: domingo: encontro da semana) geram sugestões na agenda enquanto não houver publicação naquele dia. | Definida com o cliente e implementada |
