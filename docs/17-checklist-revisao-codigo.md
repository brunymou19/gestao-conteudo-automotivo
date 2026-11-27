# Template 18 — Checklist de revisão de código

Uso: aplicar a cada pull request. Abaixo constam (1) o checklist e (2) o registro dos PRs. A coluna "Verificado" só recebe ✔ quando há evidência; o que não foi possível verificar está marcado como pendente.

## Revisão do estado atual do código (26/11/2026, `main`) — feita pelo assistente, a ser confirmada pelos integrantes
Não é a revisão de um PR; é uma verificação do código existente.

### Arquitetura
| Item | Situação | Evidência |
|---|---|---|
| O código está no módulo certo | Parcial | Regras de cada módulo estão em `app/<módulo>/service.py` |
| Não cria dependência proibida | **Parcial** | Imports: agenda → produção; eventos → conteúdo e agenda (permitidos). Mas Produção grava na tabela `conteudo`; Agenda faz JOIN em `conteudo`; Eventos lê `categoria`. Acesso direto a tabelas de outro módulo |
| O segredo de cada módulo continua escondido | Parcial | O segredo "estados" está em Produção; as consultas SQL cruzadas expõem a estrutura de tabelas |
| Segue os ADRs | ✔ | ADR-001, 002 e 003 refletidos no código |

### Projeto
| Item | Situação | Evidência |
|---|---|---|
| Nomes vêm do domínio do cliente | ✔ | conteúdo, agenda, evento, oportunidade, material, editoria |
| Responsabilidade clara por função | ✔ | Funções curtas (maior arquivo de módulo: 93 linhas) |
| Sem duplicação evidente de regras | Parcial | A listagem de agenda repete a regra de "finalizado" em consultas diferentes |
| Padrões implementados conforme as fichas | **Não se aplica** | Nenhum padrão implementado (Template 16) |

### Testes
| Item | Situação | Evidência |
|---|---|---|
| Existe teste para a regra criada | ✔ | 27 testes; cobertura de linhas 91% (pytest-cov, ambiente do assistente) |
| Contemplam partições, limites e erros | **Parcial** | Lacunas listadas em `15-plano-de-testes.md` (formato de data e hora, senha com 7 e 8 caracteres, hoje/ontem) |
| Independentes e repetíveis | ✔ | Banco temporário por teste (`tmp_path`) |
| Não dependem de relógio, rede ou produção | Parcial | Sem rede; `atrasado` usa `date.today()` com datas fixas de 2020; `sugestoes` recebe a data como parâmetro |
| Dublês usados adequadamente | Não se aplica | Nenhum dublê; SQLite temporário real |
| O pipeline passou | **Não verificável** | Não há pipeline |

### Higiene
| Item | Situação | Evidência |
|---|---|---|
| PR pequeno e com descrição | **Não** para o PR #18 | 58 arquivos alterados (reorganização); descrição presente |
| Sem senhas, chaves ou dados reais | ✔ | Chave da sessão por variável `SECRET_KEY` ou gerada em execução; senhas só em hash; `.gitignore` exclui `*.db` e `backups/` |
| Sem código comentado ou morto | ✔ | Busca por código comentado não encontrou ocorrências |

## Registro para o relatório de qualidade
| PR | Autor | Revisor | Problema encontrado na revisão | Resolvido? |
|---|---|---|---|---|
| #18 `copia-seguranca` → `main` (merge em 18/11/2026) | Bruno José Souza (merge) — conferir autor do PR | **Não evidenciado** | **Pendente.** Não foi possível ler os comentários do PR (API bloqueada); conferir a aba Conversation | **Pendente** |

Nenhuma revisão foi simulada. Para os próximos PRs, o revisor deve ser o outro integrante, e os problemas devem ser registrados aqui.
