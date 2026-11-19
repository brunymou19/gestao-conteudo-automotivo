# 04 — Cenários de qualidade (preliminares)

Ainda precisam de estímulo, ambiente, resposta e **métricas mensuráveis**, além de validação de prioridades com o cliente.

| ID | Atributo | Cenário |
|---|---|---|
| C01 | Modificabilidade | Ao alterar uma regra de organização editorial ou categoria, a equipe deve conseguir fazer a mudança com impacto controlado sobre o sistema. |
| C02 | Usabilidade | O administrador deve registrar um conteúdo e identificar pendências e estado de produção por meio de interface simples e compreensível (uso principal pelo celular). |
| C03 | Desempenho | Consultas à agenda e à lista de pendentes devem responder em tempo adequado, mesmo com o crescimento de registros. |
| C04 | Confiabilidade | Alterações em conteúdos, estados e datas devem ser persistidas corretamente e estar disponíveis em consultas posteriores. |
| C05 | Segurança | O sistema deve proteger informações administrativas e impedir acesso não autorizado a funcionalidades restritas. |

## Informações levantadas relevantes
- Dispositivo principal do cliente: **celular**.
- Maior volume de materiais: após eventos maiores (+30 fotos e alguns vídeos).
- Não há número definido de usuários simultâneos.
- Não foi identificada informação confidencial específica, mas deve haver controle de acesso a dados administrativos e de contatos.
- Disponibilidade aceitável / informações mais críticas em caso de perda: **não definidos** (ver [pendências](10-pendencias.md)).

## Situação dos cenários no primeiro incremento (15/11/2026)
- **C01 Modificabilidade:** estados em um único arquivo, editorias cadastráveis na tela, limite e modo de aviso em constantes. Cumprido de forma básica.
- **C02 Usabilidade:** tela única para celular, com campos simples. Não foi testada em celular real nem medida com o cliente.
- **C03 Desempenho:** não medido; banco SQLite com poucos registros.
- **C04 Confiabilidade:** dados persistidos em SQLite; `backup.py` copia o banco (o cliente apontou os materiais como o mais crítico). Backup é manual.
- **C05 Segurança:** login com senha em hash, sessão por cookie e rotas protegidas. Sem limite de tentativas, recuperação de senha ou HTTPS.
