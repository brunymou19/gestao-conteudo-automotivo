# 07 — Módulos, segredos e regras de dependência

> Proposta de divisão lógica. **Não** significa que os módulos já estejam implementados.

## Módulos

| # | Módulo | Responsabilidade | Segredo | Interface | Depende de | Protege |
|---|---|---|---|---|---|---|
| 1 | Gerenciamento de Conteúdo | Registrar e organizar ideias, fotos, vídeos e materiais | Dados associados a cada conteúdo | Cadastro, consulta, atualização e organização | Produção; Agenda | C01, C02, RN01 |
| 2 | Produção de Conteúdo | Acompanhar etapas da ideia até a preparação para publicar | Situações e transições do fluxo | Atualização e consulta do estado | Gerenciamento de Conteúdo | C01, RN01 |
| 3 | Agenda e Publicações | Datas de publicação, compromissos e planejamento editorial | Planejamento e organização das publicações | Visualização, cadastro e alteração de datas | Gerenciamento; Produção | C02, RN03 |
| 4 | Eventos e Oportunidades | Solicitações de divulgação, eventos, parcerias e oportunidades | Informações das solicitações externas e compromissos | Cadastro, consulta e acompanhamento | Agenda; Gerenciamento | RN02, RN04, RN05 |
| 5 | Usuário e Acesso | Controle de acesso administrativo | Informações de autenticação e autorização | Autenticação e controle de acesso | Persistência de dados | C05 |

Responsáveis: Bruno José Souza e Pablo Gonçalves Barbosa.

## Regras de dependência
1. **Agenda não acessa detalhes internos de Produção** — usa suas interfaces. *Por quê:* reduzir acoplamento. *Verificação:* revisão de código e análise de dependências.
2. **Eventos e Oportunidades não implementa regras do fluxo de produção.** *Por quê:* cada responsabilidade em seu módulo. *Verificação:* revisão de estrutura e responsabilidades.
3. **Módulos de negócio não dependem de detalhes da interface visual.** *Por quê:* alterar a interface sem mexer nas regras. *Verificação:* revisão de dependências e testes.

## Acoplamentos aceitos
1. Gerenciamento de Conteúdo → Produção: **aceitável** (o acompanhamento depende da etapa de produção; comunicar por interfaces definidas).
2. Agenda → Gerenciamento de Conteúdo: **aceitável** (a agenda associa datas aos conteúdos; preservar ou ajustar interfaces se o módulo mudar).
3. Eventos e Oportunidades → Agenda: **aceitável** (eventos geram compromissos; limitar a dependência às operações necessárias).
