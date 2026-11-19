# 14 — Implementação: arquitetura do código, rotas e execução

## Estrutura
```
app/
  __init__.py                  API Flask, login e rotas
  db.py                        tabelas SQLite
  acesso/service.py            usuário e senha (hash)
  conteudo/service.py          conteúdos, editorias, referências de materiais
  producao/service.py          estados do fluxo
  agenda/service.py            agenda, reorganização, atrasos, regras semanais, sugestões
  eventos_oportunidades/service.py   eventos e oportunidades
  templates/                   index.html e login.html
tests/                         27 testes
run.py · criar_admin.py · backup.py · requirements.txt
```

## Tabelas
`categoria`, `conteudo`, `agendamento` (única por data e hora), `material`, `evento`, `oportunidade`, `regra_semanal`, `usuario`.

## Rotas principais (todas exigem login)
- Conteúdos: `GET/POST /api/conteudos`, `PATCH /api/conteudos/<id>/estado`
- Materiais: `GET/POST /api/conteudos/<id>/materiais`, `DELETE /api/materiais/<id>`
- Editorias e estados: `GET/POST /api/categorias`, `GET /api/estados`
- Agenda: `GET/POST /api/agenda`, `PATCH /api/agenda/<id>`, `GET /api/pendentes`, `GET /api/sugestoes`
- Regras semanais: `GET/PUT /api/regras-semanais`, `DELETE /api/regras-semanais/<dia>`
- Eventos: `GET/POST /api/eventos`, `PATCH /api/eventos/<id>/situacao`, `POST /api/eventos/<id>/agendar`
- Oportunidades: `GET/POST /api/oportunidades`, `PATCH /api/oportunidades/<id>/situacao`
- Acesso: `/login` e `/logout`

## Execução
```
pip install -r requirements.txt
python criar_admin.py
python run.py
python -m pytest
python backup.py
```
Variável opcional `SECRET_KEY` mantém o login válido após reiniciar o servidor.

## Verificação realizada
27 testes automatizados passaram, e o servidor foi iniciado com requisições de login e de todas as rotas de leitura (resposta 200). A tela não foi testada em navegador de celular.

## Limitações conhecidas
- Strategy e priorização automática (RN05) não implementados.
- Situações das oportunidades e nomes dos tipos de evento são provisórios.
- Arrastar na agenda usa o recurso do navegador e pode não funcionar em toque; o campo de data em cada item é a alternativa.
- Login sem limite de tentativas nem recuperação de senha; sem HTTPS.
- O backup copia o banco, não os arquivos de foto e vídeo (ficam no celular do cliente).
- A agenda e os eventos leem a tabela `conteudo` diretamente em algumas consultas.
