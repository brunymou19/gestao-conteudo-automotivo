# 08 — Ficha de padrão de projeto: Strategy

**Categoria:** comportamental · **Responsáveis:** Bruno José Souza e Pablo Gonçalves Barbosa
**Situação na Etapa 3:** ☒ Ainda não implementado — padrão **proposto para avaliação**.

## Problema neste sistema
O sistema recebe conteúdos e solicitações de tipos diferentes (publicações espontâneas, divulgação antecipada de eventos, cobertura de encontros, oportunidades de parceria), cada um podendo exigir critérios diferentes de priorização. É preciso poder alterar esses critérios sem mexer no resto do sistema.

## Por que este padrão
Strategy encapsula comportamentos intercambiáveis e permite escolher qual usar conforme a necessidade — aqui, diferentes critérios de priorização.

## Alternativa sem o padrão
Concentrar a priorização em uma única estrutura de `if/else`. É mais simples no início, mas dificulta a manutenção quando critérios mudam ou crescem.

## Custo
- Estruturas adicionais para representar as estratégias
- Mais classes/componentes
- Necessidade de entender como a estratégia é selecionada
- Possível complexidade desnecessária se a priorização for muito simples

## Participantes

| Papel | Classe/módulo | Observação |
|---|---|---|
| Contexto | Módulo de Gerenciamento de Conteúdo | Usa a estratégia selecionada |
| Interface da estratégia | Estratégia de Priorização | Operação comum de priorização |
| Estratégia concreta 1 | Priorização por urgência | Prazos e proximidade de eventos |
| Estratégia concreta 2 | Priorização por compromisso | Solicitações e compromissos assumidos |

## Como será testado
Testes com diferentes situações de conteúdo e solicitações, verificando se a estratégia selecionada aplica os critérios esperados e se alterar uma estratégia não afeta as demais.

## Motivo da situação atual
A aplicação depende de confirmar que o sistema realmente precisará de diferentes estratégias de priorização. A decisão será revisada durante o desenvolvimento para não adicionar complexidade sem necessidade.
