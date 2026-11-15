# 02 — Histórias de usuário, critérios de aceitação e situação

Situação em 15/11/2026. Os critérios abaixo foram escritos pela equipe e devem ser confirmados com o cliente na avaliação do primeiro incremento.

| ID | História | Critérios de aceitação | Situação |
|---|---|---|---|
| H01 | Registrar ideias de conteúdo | (1) Registrar com título obrigatório, descrição e editoria. (2) O conteúdo nasce no estado "ideia". (3) A editoria pode ser escolhida entre as 12 cadastradas ou criada na tela. | Implementada |
| H02 | Acompanhar produção | (1) Cada conteúdo tem um estado entre ideia, em edição, pronto, agendado, publicado e encerrado. (2) Estado fora da lista é recusado. (3) Agendar muda o estado para "agendado". | Implementada |
| H03 | Planejar publicações (**prioridade da 1ª versão**) | (1) Agendar com data e hora. (2) A agenda lista os próximos 14 dias. (3) Reorganizar mudando a data ou arrastando o item. (4) Avisar (sem bloquear) quando houver mais de 2 no dia. (5) Recusar o mesmo horário. (6) Sugerir dias com conteúdo fixo ainda sem publicação. | Implementada |
| H04 | Controlar prazos | (1) Itens da agenda com data passada e não finalizados aparecem como atrasados. (2) Eventos pendentes com prazo (ou data) vencido aparecem como atrasados. | Implementada |
| H05 | Registrar solicitações de eventos | (1) Registrar nome, data, quem pediu, tipo e prazo. (2) Tipos: divulgação antecipada, cobertura durante, publicação posterior. (3) Aceitar datas passadas (lançar depois). (4) Gerar o conteúdo do evento e agendá-lo. | Implementada |
| H06 | Organizar oportunidades e parcerias | (1) Registrar nome do contato, canal (Instagram, e-mail, outro), proposta e condições. (2) Acompanhar a situação. | Implementada (situações provisórias) |
| H07 | Organizar materiais | (1) Associar a cada conteúdo referências de fotos, vídeos ou outros (nome do arquivo, pasta ou link). (2) Remover referências. (3) Sem upload de arquivos (ver ADR-003). | Implementada |

## Necessidades levantadas na entrevista (rastreabilidade)
1. Organização centralizada → H01, H02, H07.
2. Planejamento de publicações → H03.
3. Acúmulo após eventos (+30 fotos e vídeos) → H02, H07.
4. Produção concentrada em uma pessoa → H02, usabilidade no celular (C02).
5. Solicitações externas e oportunidades → H05, H06.
6. Prazos diferentes para eventos → RN02, H05.
7. Limite de 2 publicações por dia → RN03, H03.
8. Novas categorias editoriais (12) → RN06.
9. Melhorias na edição de imagens / IA → fora do sistema: o cliente usa uma IA externa com prompt.
10. Frequência de publicações → H03 (regras semanais e sugestões).
11. Dependência de contatos externos → C04 (backup) e registro manual posterior.
