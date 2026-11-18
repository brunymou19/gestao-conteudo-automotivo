# ADR-002 — Stack: Python, Flask e SQLite

- **Status:** Aceito · **Data:** 15/11/2026 · **Responsáveis:** Bruno José Souza e Pablo Gonçalves Barbosa
- **Relacionados:** ADR-001, C01, C02, C04, C05

## Contexto
O projeto é acadêmico, tem um único administrador como usuário (usa o celular) e precisa de uma primeira versão funcional em prazo curto. Nenhuma tecnologia estava definida antes; o grupo confirmou Python, Flask e SQLite.

## Alternativas
1. **Python + Flask + SQLite** — + simples e leve, + sem servidor de banco, + fácil de testar e rodar, + combina com a organização modular · − não escala para muitos usuários simultâneos, − o servidor de desenvolvimento não serve para produção.
2. **Django + PostgreSQL** — + recursos prontos (admin, login) · − mais pesado e com mais configuração para o porte do projeto.
3. **Node.js + banco em servidor** — + um só idioma no front e no back · − o grupo não o escolheu e exigiria servidor de banco.

## Decisão
Python com Flask para a API e a página, SQLite como banco, tela em HTML e JavaScript simples, pytest para testes.

## Consequências
- **Melhora:** simplicidade, execução local, testes rápidos, backup copiando um arquivo.
- **Piora (trade-off):** concorrência limitada; para uso real seria preciso servidor de produção e HTTPS.
- **Mais difícil de mudar depois:** trocar de banco exige adaptar as consultas SQL escritas dentro dos módulos.

## Como verificar
Executar `python -m pytest` (27 testes) e subir o sistema com `python run.py`.
