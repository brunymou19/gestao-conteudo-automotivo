# Template 16 — Fichas de padrão de projeto

Verificação em 26/11/2026: busca no código (`app/`, `tests/`) por Strategy, State e Repository não encontrou nenhuma implementação. **Nenhum padrão de projeto foi implementado até agora.** As fichas abaixo registram o estado real.

## Ficha 1 — Strategy (comportamental)
**Responsáveis:** Bruno José Souza e Pablo Gonçalves Barbosa

**Problema neste sistema:** a RN05 pede priorização de conteúdos, eventos e oportunidades por urgência, proximidade de eventos, compromissos assumidos, relevância e disponibilidade de materiais. Os critérios podem mudar ou variar por tipo de solicitação (RN02 e RN08), e o cliente discutiu uma agenda com conteúdos fixos por dia da semana. Hoje essa priorização **não existe** no código; a agenda ordena apenas por data e hora e sugere dias das regras semanais.

**Por que este padrão:** permite trocar o critério de priorização sem alterar o módulo que o utiliza (cenário C01, modificabilidade).

**Alternativa sem o padrão:** uma função com `if/else` por critério, dentro do módulo de Agenda. É mais simples e suficiente enquanto houver um só critério.

**Custo do padrão:** interface e classes adicionais; necessidade de escolher a estratégia em tempo de execução; risco de complexidade sem necessidade se houver um único critério.

**Como será testado:** testes parametrizados com a mesma lista de itens e cada estratégia, verificando a ordem esperada; teste de que trocar a estratégia não altera o módulo cliente; valores-limite (mesmo prazo, prazo vencido, sem prazo).

| Papel | Classe ou módulo | Observação |
|---|---|---|
| Contexto | Módulo de Agenda e Publicações (proposto; a ficha anterior indicava Gerenciamento de Conteúdo) | Receberia a estratégia selecionada |
| Interface da estratégia | `EstrategiaPriorizacao` (a criar) | Operação comum de ordenação |
| Estratégia concreta 1 | `PorUrgencia` (a criar) | Prazo e proximidade de eventos |
| Estratégia concreta 2 | `PorCompromisso` (a criar) | Solicitações e compromissos assumidos |

**Situação na Etapa 3:** ( X ) Ainda não implementado — padrão proposto. ( ) Implementado como previsto. ( ) Modificado. ( ) Abandonado.
**Motivo:** o primeiro incremento priorizou agenda, eventos, oportunidades, materiais e login. A priorização automática (RN05) não foi implementada, e o cliente não confirmou critérios de priorização (mudança M05 adiada).

## Outros padrões avaliados (não implementados)
- **State (fluxo de produção):** hoje os estados são uma lista simples, sem regras de transição definidas pelo cliente. State só se justifica se houver regras de transição; não foi adotado.
- **Repository (persistência):** os serviços executam SQL diretamente com `sqlite3`. Um Repository reduziria o acoplamento entre módulos e tabelas (ver `17-checklist-revisao-codigo.md`), mas não foi implementado.

## Observação para a entrega
Se o professor exige ao menos um padrão implementado na Etapa 3, a opção mais coerente com os requisitos é implementar o Strategy para a priorização (RN05) ou o Repository para isolar o acesso às tabelas. A decisão e a implementação são do grupo (Issue "Decidir se o padrão Strategy e a priorização automática serão implementados").
