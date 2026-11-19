# Sistema de Apoio à Gestão de Conteúdo Automotivo

Projeto acadêmico da disciplina **Engenharia de Software II — CSI410**, Universidade Federal de Ouro Preto (UFOP).

| | |
|---|---|
| **Integrantes** | Bruno José Souza e Pablo Gonçalves Barbosa |
| **Cliente principal** | Administrador de uma página de conteúdo automotivo |
| **Canal de publicação do cliente** | Instagram |

## Sobre o projeto

Sistema para auxiliar o administrador de uma página de conteúdo automotivo a **organizar, acompanhar e planejar** suas atividades editoriais: ideias, fotos e vídeos, etapas de produção, agenda de publicações, solicitações de eventos e oportunidades de parceria.

**Problema:** o administrador faz sozinho todo o processo (captar, organizar, editar e publicar). Os materiais ficam na galeria do celular e são publicados na ordem em que chegam, sem planejamento. Após eventos grandes surgem mais de 30 fotos, além de vídeos, e o volume de pendências acumula.

**Prioridade da primeira versão (definida pelo cliente):** uma **agenda de organização de conteúdos e datas de publicação**.

## Status

- Etapa atual: primeiro incremento implementado (MVP) e documentação atualizada.
- Stack: Python, Flask e SQLite. Cinco módulos implementados (conteúdo, produção, agenda, eventos e oportunidades, acesso) com 27 testes automatizados.
- Falta: avaliação do primeiro incremento com o cliente (veja [`docs/10-pendencias.md`](docs/10-pendencias.md)).
- Requisitos, regras e prioridades marcados como "pendentes" aguardam validação com o cliente (veja [`docs/10-pendencias.md`](docs/10-pendencias.md) e as *Issues* do repositório).

## Documentação

| # | Documento |
|---|---|
| 01 | [Plano do projeto e visão do produto](docs/01-plano-do-projeto.md) |
| 02 | [Histórias de usuário](docs/02-historias-de-usuario.md) |
| 03 | [Regras de negócio](docs/03-regras-de-negocio.md) |
| 04 | [Cenários de qualidade](docs/04-cenarios-de-qualidade.md) |
| 05 | [Entrevistas e atas de contato](docs/05-entrevistas-e-atas.md) |
| 06 | [Matriz de riscos](docs/06-matriz-de-riscos.md) |
| 07 | [Módulos, segredos e regras de dependência](docs/07-modulos-e-dependencias.md) |
| 08 | [Padrão de projeto: Strategy](docs/08-padrao-strategy.md) |
| 09 | [Registro de mudanças](docs/09-registro-de-mudancas.md) |
| 10 | [Pendências e dúvidas para o cliente](docs/10-pendencias.md) |
| 11 | [Registro de etapa e retrospectiva](docs/11-retrospectiva.md) |
| 12 | [Declaração de contribuição e uso de IA](docs/12-contribuicao-e-uso-de-ia.md) |
| 13 | [Registro de correções e atualizações](docs/13-registro-de-correcoes.md) |
| 14 | [Implementação: arquitetura do código, rotas e execução](docs/14-implementacao.md) |
| ADR-001 | [Organização modular do sistema](docs/adr/ADR-001-organizacao-modular.md) |
| ADR-002 | [Stack: Python, Flask e SQLite](docs/adr/ADR-002-stack-python-flask-sqlite.md) |
| ADR-003 | [Materiais como referências (sem upload)](docs/adr/ADR-003-materiais-por-referencia.md) |

## Como contribuir (equipe)

1. Cada tarefa deve ter uma *Issue*.
2. Crie uma *branch* a partir da `main` (ex.: `feature/agenda`).
3. Abra um *Pull Request* e peça revisão do outro integrante antes do *merge*.

## Como executar o sistema

```
pip install -r requirements.txt
python criar_admin.py   # uma vez: cria o administrador
python run.py           # abre em http://127.0.0.1:5000
python -m pytest        # testes
python backup.py        # cópia de segurança do banco
```
