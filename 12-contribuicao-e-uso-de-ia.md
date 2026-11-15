# 12 — Declaração de contribuição e uso de IA

## Declaração de contribuição
| Integrante | Principais contribuições | Responsável por | Participação estimada |
|---|---|---|---|
| Bruno José Souza | Levantamento de requisitos, contato e entrevista com o cliente, documentação, identificação do problema, histórias de usuário e regras de negócio | Levantamento, documentação, histórias e regras | 50% |
| Pablo Gonçalves Barbosa | Levantamento de requisitos, acompanhamento da entrevista, registro das informações, documentação e colaboração na solução | Apoio ao levantamento, documentação, histórias e regras | 50% |

> Os percentuais são proposta inicial de divisão igualitária, **não** medição comprovada. Confirmem antes de assinar. Assinaturas físicas ficam fora do repositório.

## Declaração de uso de IA
Houve uso de ferramentas de IA generativa na documentação do projeto (organização, estruturação, revisão e elaboração de textos, templates, matriz de riscos e retrospectiva). A declaração anterior cita **ChatGPT (GPT-6)**.

> **Atualização necessária (CORR-002):** a declaração original cita apenas o ChatGPT, mas o grupo também utilizou o **Gemini**. Antes da entrega, incluam a ferramenta na tabela abaixo, com **versão/modelo** e **finalidade** reais.

| Ferramenta e versão | Finalidade | Parte do trabalho |
|---|---|---|
| ChatGPT — modelo GPT-6 | Organização, estruturação, revisão e elaboração de textos | Documentação, requisitos, matriz de riscos, retrospectiva, templates |
| Gemini — versão a informar | A informar pelos integrantes | A informar pelos integrantes |

> Se outras ferramentas de IA também ajudaram (por exemplo, na organização destes arquivos do repositório), declarem-nas da mesma forma.

**O que NÃO foi feito com IA:** entrevista com o cliente, observação da rotina, decisões finais dos integrantes, validação dos requisitos com o cliente, implementação do sistema e comprovação de resultados.

**Responsabilidade humana:** todas as decisões intelectuais, conceituais, argumentativas e interpretativas, incluindo decisões de projeto/arquitetura e escolha de casos de teste, são dos autores. Todo o conteúdo deve ser revisado criticamente pelos integrantes, que assumem a responsabilidade ética, acadêmica e intelectual pelo trabalho.

## Itens reutilizados (ADR-001)
| Item | Uso | Licença | Alternativas | Motivo |
|---|---|---|---|---|
| GitHub (web) | Hospedagem do repositório e controle de versão | Termos de uso da plataforma | GitLab, Bitbucket | Organização e compartilhamento do código |
| Git | Controle de versão | GNU GPL v2 | Outros VCS | Acompanhar alterações e integrar contribuições |
| ChatGPT (GPT-6) | Apoio à documentação | Serviço proprietário da OpenAI | Elaboração manual e outras IAs | Estruturação e revisão textual |

Bibliotecas, frameworks e serviços ainda não identificados não devem ser declarados como reutilizados.

## Itens reutilizados na implementação
Preencham a coluna de versão com o resultado de `python --version` e `pip show flask werkzeug pytest`.

| Item | Uso | Licença | Alternativas consideradas | Motivo |
|---|---|---|---|---|
| Python (versão a informar) | Linguagem do sistema | Licença PSF | Node.js, Java | Simplicidade e testes rápidos |
| Flask (versão a informar) | Servidor web e API | BSD-3-Clause | Django, FastAPI | Leve e adequado ao porte do projeto |
| Werkzeug (instalado com o Flask) | Hash de senha e utilitários | BSD-3-Clause | bcrypt/argon2 | Já vem com o Flask |
| SQLite (módulo `sqlite3` do Python) | Banco de dados | Domínio público | PostgreSQL, MySQL | Sem servidor; arquivo único; um administrador |
| pytest (versão a informar) | Testes automatizados | MIT | unittest | Escrita simples dos testes |
