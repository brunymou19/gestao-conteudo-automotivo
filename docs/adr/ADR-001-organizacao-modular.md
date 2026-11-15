# ADR-001 — Organização modular do sistema

- **Status:** Proposto *(a equipe deve confirmar antes de marcar como Aceito)*
- **Data:** a definir
- **Responsáveis:** Bruno José Souza e Pablo Gonçalves Barbosa
- **Relacionados:** C01 Modificabilidade, C02 Usabilidade, RN01 Fluxo de produção, RN03 Limite de publicações

## Contexto
O sistema registra materiais, acompanha etapas de produção e planeja publicações, com responsabilidades distintas (conteúdos, agenda, eventos, oportunidades). Organizá-las em partes bem definidas facilita mudanças futuras, reduz acoplamento e permite adicionar recursos sem comprometer o todo.

## Alternativas
**1. Sistema em módulos** — + separação de responsabilidades, + facilidade de alteração, + melhor organização, + evolução independente · − exige planejamento, − definir interfaces, − mais arquivos.

**2. Sem separação clara** — + estrutura inicial simples, + pouco planejamento · − acoplamento, − difícil localizar/modificar, − risco de mudanças afetarem partes não relacionadas.

**3. Microsserviços** — + independência, + escalabilidade, + tecnologias distintas · − complexidade, − comunicação entre serviços, − custo de configuração, − exagero para o porte inicial.

## Decisão
Arquitetura **modular**, com funcionalidades organizadas por responsabilidade, sem adotar inicialmente microsserviços.

## Consequências
- **Melhora:** organização e manutenção, separação de responsabilidades, evolução, testabilidade por parte.
- **Piora (trade-off):** planejar a estrutura dos módulos; cuidado com dependências e interfaces; leve aumento de complexidade inicial.
- **Mais difícil de mudar depois:** estrutura e interfaces entre módulos podem exigir ajustes se o sistema crescer.

## Como verificar
Revisão da estrutura do código, análise de dependências entre módulos e testes individuais das funcionalidades; avaliar se mudar um módulo exige mudanças desnecessárias nos outros.

Veja também: [módulos e dependências](../07-modulos-e-dependencias.md).
