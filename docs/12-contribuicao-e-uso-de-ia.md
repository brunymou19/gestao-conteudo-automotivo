# Templates 12 e 13 — Declaração de contribuição e declaração de uso de IA

Privacidade: cliente identificado apenas como "cliente (administrador da página)".

# Template 12 — Declaração de contribuição

**Entrega:** Incremento 1 (Etapa 3) · **Data:** preencher com a data do envio

| Integrante | Principais contribuições | Histórias, módulos, ADRs e padrões | Participação estimada |
|---|---|---|---|
| Bruno José Souza | Condução da entrevista principal; documentação; histórias e regras de negócio; commits de implementação (10 commits no repositório); organização do repositório | Levantamento e documentação; módulos e ADRs em conjunto com o colega (divisão por módulo a detalhar) | 50% |
| Pablo Gonçalves Barbosa | Anotações da entrevista principal; registro das informações; documentação (4 commits de envio em 15/11/2026); colaboração na definição da solução | Apoio ao levantamento e à documentação; módulos e ADRs em conjunto (divisão por módulo a detalhar) | 50% |

Total: 100%.

**Observações:** os percentuais de 50%/50% foram confirmados pelos integrantes. A contagem de commits (Bruno 10, Pablo 4) não mede esforço, porque boa parte do trabalho foi feita fora de commits e por envio de arquivos. Se a divisão real por história ou módulo for diferente, ajustar antes de assinar.

Declaramos que as informações acima correspondem à contribuição de cada integrante nesta entrega.

Assinaturas: Bruno José Souza: ______________ · Pablo Gonçalves Barbosa: ______________ (a assinar pelos próprios integrantes)

# Template 13 — Declaração de uso de IA

## Versão curta
Marcar: **( X ) Houve uso de ferramentas de IA generativa nesta entrega.**

| Ferramenta e versão | Finalidade | Parte do trabalho | O que NÃO foi feito com IA |
|---|---|---|---|
| ChatGPT (modelo informado na declaração anterior: GPT-6) | Apoio à organização, estruturação, revisão e elaboração de textos | Documentação inicial do projeto, requisitos, matriz de riscos, retrospectiva e preenchimento de templates | Entrevistas, observação da rotina do cliente, decisões finais, validação dos requisitos, comprovação de resultados |
| Gemini (versão não informada) | **A confirmar pelos autores** | **A confirmar pelos autores** | **A confirmar pelos autores** |
| Claude, da Anthropic (modelo: informado como Claude Sonnet 5.5 pelo próprio assistente; conferir na interface) | Geração e complementação de código (aplicação Flask) e de testes (pytest); elaboração e atualização da documentação do repositório (docs 01–14, ADRs 001–003, atualizações destes templates); análise de requisitos e do repositório; orientação para uso do GitHub | Implementação do primeiro incremento; testes automatizados; documentação; organização do repositório | Entrevistas e observação; decisões finais; validação com o cliente; execução e comprovação dos testes no ambiente do grupo; avaliação do primeiro incremento |

## Versão completa — modelo CRediT-IA (https://periodicos.ufop.br/virtualiajournal/credit-ia)

**Declaração de uso.** Declaramos que houve utilização de ferramentas de Inteligência Artificial na elaboração deste trabalho, conforme detalhado abaixo.

**Ferramentas utilizadas:** ChatGPT (GPT-6, conforme declaração anterior); Gemini (versão não informada); Claude (Anthropic; modelo informado como Claude Sonnet 5.5).

**Finalidade do uso:**
- ( X ) Revisão linguística ou gramatical.
- ( ) Tradução.
- ( ) Transcrição de áudio (não há registro de uso).
- ( X ) Geração ou complementação de código.
- ( X ) Código de testes.
- ( ) Configuração do pipeline (não há pipeline).
- ( X ) Outra: elaboração e organização da documentação, análise de requisitos e do repositório, orientação sobre o uso do GitHub, preenchimento dos templates.

**Etapa e parte do trabalho em que foi utilizada:** levantamento e organização das informações (documentação), especificação (histórias, regras, riscos, ADRs), implementação do primeiro incremento (código e testes), organização do repositório e preenchimento dos templates da disciplina. O uso do Gemini deve ser detalhado pelos autores.

**Limites do uso:** a IA não realizou entrevistas nem observou a rotina do cliente; não tomou as decisões finais em nome dos integrantes; não validou os requisitos com o cliente; não substituiu a participação humana. Os testes foram executados pelo assistente no ambiente dele; a execução no ambiente do grupo e a avaliação com o cliente são do grupo. Não foram usados resultados fictícios de testes, métricas ou atividade do repositório como evidência.

**Declaração de responsabilidade humana.** Declaramos que todas as decisões intelectuais, conceituais, argumentativas e interpretativas do trabalho, incluindo decisões de projeto e arquitetura e a escolha dos casos de teste, são de responsabilidade dos autores. O uso de IA foi instrumental e respeitou as regras da disciplina. Todo o conteúdo foi (ou deverá ser) revisado criticamente pelos integrantes, que assumem plena responsabilidade ética, acadêmica e intelectual pelo trabalho entregue e se comprometem a defendê-lo publicamente.

> Nota: esta declaração inclui o Claude porque o código, os testes e a maior parte da documentação do repositório foram produzidos com o apoio dele. Omitir essa ferramenta tornaria a declaração incompatível com o histórico real.

# Itens reutilizados (ADR-001, ADR-002 e implementação)

| Item e versão | Uso | Licença | Alternativas | Motivo |
|---|---|---|---|---|
| GitHub | Hospedagem e controle de versão | Termos de uso | GitLab, Bitbucket | Compartilhamento do código |
| Git | Controle de versão | GNU GPL v2 | Outros VCS | Histórico de alterações |
| Python (versão a informar com `python --version`) | Linguagem | Licença PSF | Node.js, Java | Simplicidade |
| Flask (versão: `pip show flask`) | API e páginas | BSD-3-Clause | Django, FastAPI | Leve |
| Werkzeug (versão: `pip show werkzeug`) | Hash de senha | BSD-3-Clause | bcrypt | Vem com o Flask |
| SQLite (módulo `sqlite3`) | Banco de dados | Domínio público | PostgreSQL | Arquivo único |
| pytest (versão: `pip show pytest`) | Testes | MIT | unittest | Testes simples |
| ChatGPT, Gemini, Claude | Apoio de IA (ver Template 13) | Serviços proprietários, sujeitos aos termos de cada um | Elaboração manual | Apoio à documentação e ao código |
