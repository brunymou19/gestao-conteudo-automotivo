# Template 20 — Plano de testes de desenvolvimento e de release

Posição: 26/11/2026. Tecnologia: Python 3, Flask, SQLite, pytest. "Executado" só aparece onde houve execução real.

## Testes de desenvolvimento — Etapa 3
| Nível | O que é testado | Técnica e ferramenta | Dublês usados | Responsável |
|---|---|---|---|---|
| Unidade | Regras dos serviços chamadas diretamente: sugestões por regra semanal, senha curta e duplicada, regra semanal inválida | pytest, caixa-preta | Nenhum; SQLite temporário real | Bruno e Pablo (divisão por teste a registrar) |
| Integração | Rotas HTTP com banco, login e módulos juntos (agenda + produção + eventos + conteúdo) | pytest + cliente de teste do Flask | Nenhum; banco em `tmp_path`; sem rede | Bruno e Pablo |
| Sistema (opcional) | Não realizado em navegador ou celular | — | — | Pendente |
| Critérios de aceitação | Critérios de H01–H07 em `02-historias-de-usuario.md`; ainda não executados como roteiro | Roteiro manual (testes de release RT01–RT14) | — | Pendente |

Distribuição dos 27 testes: `test_app.py` 9; `test_acesso.py` 8; `test_novos.py` 10.

## Partições e valores-limite (regras que existem no projeto)
| Regra | Partições (representante) | Valores-limite testados | Testes | Lacunas (testes não escritos) |
|---|---|---|---|---|
| RN01 estados | Estado válido (`em_edicao`); inválido (`xyz`) | — | `test_estado_invalido_e_valido`, `test_registra_ideia_com_estado_inicial` | Conteúdo inexistente (404); cada um dos 6 estados |
| RN03 limite diário | 0–1 no dia: sem aviso; 2 no dia: o 3º gera aviso; modo bloqueio | 2 existentes (3º agendamento): avisa; bloqueia no modo configurado | `test_limite_diario_apenas_avisa`, `test_limite_diario_bloqueia_quando_configurado` (respostas 200, 200, 400) | O 2º agendamento sem aviso não é afirmado; reagendar o mesmo conteúdo não conta duas vezes |
| Horário de publicação | Horário livre; horário ocupado no mesmo dia; formato inválido | Mesmo horário recusado | `test_mesmo_horario_rejeitado` | `00:00`, `23:59`, `24:00`, data inválida, hora vazia |
| RN04 atrasado | Data passada e não finalizado; passada e finalizado; hoje ou futura | Data antiga (2020) | `test_atrasado_na_agenda`, `test_evento_passado_aceito_e_atrasado` | Data = hoje; ontem; item publicado |
| RN09 finalizado | Estado `publicado`; `encerrado` | `publicado` recusado | `test_conteudo_finalizado_nao_agenda` | `encerrado` |
| RN02 eventos | Tipo válido; inválido; data passada | Tipo `x` recusado; data passada aceita | `test_evento_fluxo_completo`, `test_evento_passado_aceito_e_atrasado` | Prazo com formato inválido; nome e solicitante vazios |
| RN08 oportunidades | Canal válido; canal inválido; situação válida e inválida | `fax`, `?` recusados | `test_oportunidade` | Contato e proposta vazios |
| RN07 materiais | Tipo válido (`foto`); inválido (`zip`) | `zip` recusado | `test_material_por_referencia` | Referência vazia; conteúdo inexistente |
| RN06 categorias | Nome novo; duplicado | Duplicada recusada; 12 iniciais | `test_categoria_duplicada`, `test_12_categorias_iniciais` | Nome vazio |
| RN10 regra semanal | Dia 0–6 válido; fora do intervalo | Dia 9 recusado; sugestão some após agendar | `test_regra_semanal_gera_sugestao_ate_agendar`, `test_regra_invalida` | Dias −1, 0, 6 e 7 |
| Acesso (C05) | Senha com menos de 8; 8 ou mais; usuário existente; credenciais corretas ou não | Senha `curta` recusada | `test_senha_curta_e_usuario_duplicado`, `test_senha_certa_libera`, `test_senha_errada_negada` e outros | Senhas de 7 e 8 caracteres |

**Cobertura de linhas:** 91% (pytest-cov, ambiente do assistente). Cobertura de linhas não prova cobertura dos requisitos; as lacunas acima mostram o que ainda falta. Próximo passo sugerido: escrever os testes de limite listados (Issue a criar).

## Ciclos de TDD
| Regra | Integrante | Commit do teste | Commit da implementação | Algum teste mudou o projeto? |
|---|---|---|---|---|
| Todas | — | **Sem evidência** | **Sem evidência** | — |

O histórico do repositório não mostra testes escritos antes da implementação: os testes foram enviados nos mesmos commits do código ("Implementa MVP da agenda editorial", "Implementa login do administrador", "Completa MVP"). **Não houve TDD comprovado**, e nenhum ciclo foi reconstruído. Para os próximos testes de limite, o grupo pode aplicar TDD de verdade e registrar os dois commits.

## Testes de release — Etapa 4 (planejados; nenhum executado)
Regra do professor: cada história deve ser testada por um integrante que não a implementou. Como o histórico não mostra quem implementou cada módulo, "Executado por" está **a definir**.

| ID | História, regra ou cenário | Técnica | Critério ou medida | Executado por | Situação | Data |
|---|---|---|---|---|---|---|
| RT01 | H01 registrar ideia | Partições (título vazio / válido; com e sem editoria) | Registra com estado "ideia"; título vazio recusado | A definir | Pendente | — |
| RT02 | H02, RN01 estados | Partições | Percorre os 6 estados; estado inexistente recusado | A definir | Pendente | — |
| RT03 | H03, RN03 limite diário | Valor-limite (1, 2 e 3 publicações no dia) | Sem aviso até 2; aviso no 3º; mesmo horário recusado | A definir | Pendente | — |
| RT04 | H03 reorganizar agenda | Exploratório (celular e computador) | Data muda mantendo a hora; no celular o campo de data funciona | A definir | Pendente | — |
| RT05 | H04, RN04 atrasados | Valor-limite (ontem, hoje, amanhã) | Só item vencido e não finalizado aparece como atrasado | A definir | Pendente | — |
| RT06 | H05, RN02 eventos | Partições (3 tipos; data passada) | Evento gera conteúdo e é agendado; data passada aceita | A definir | Pendente | — |
| RT07 | H06, RN08 oportunidades | Partições (canais, situações) | Registro e mudança de situação corretos | A definir | Pendente | — |
| RT08 | H07, RN07 materiais | Partições (tipos; referência vazia) | Referência adicionada e removida; sem upload | A definir | Pendente | — |
| RT09 | RN10 regra semanal | Valor-limite (dias 0, 6 e 7) | Sugestão aparece e some ao agendar | A definir | Pendente | — |
| RT10 | C05 segurança | Caixa-preta, valor-limite (senha de 7 e 8) | Sem login = acesso negado; senha de 7 recusada, de 8 aceita | A definir | Pendente | — |
| RT11 | C04 confiabilidade | Reiniciar o servidor e conferir dados; executar `backup.py` | Dados persistem; cópia criada em `backups/` | A definir | Pendente | — |
| RT12 | C02 usabilidade | Teste com o cliente no celular | Registrar um conteúdo e ver seu estado sem ajuda em até 2 min (limite **proposto**) | Cliente com a equipe | Pendente | — |
| RT13 | C03 desempenho | Carga com 1.000 conteúdos | Consultas de agenda e pendentes em até 500 ms (limite **proposto**) | A definir | Pendente (medição preliminar abaixo) | — |
| RT14 | C01 modificabilidade | Mudança M15 (Template 22) | Mudança contida no módulo de Agenda | A definir | Pendente | — |

## Suíte completa de regressão
- **Comando:** `python -m pytest` (na raiz do repositório)
- **Número de testes:** 27
- **Resultado:** 27 passaram
- **Data e local da execução:** 26/11/2026, ambiente do assistente (cópia da `main`, commit 5281449). **A execução no computador do grupo ainda deve ser registrada.**

## Cenários de qualidade medidos
| Cenário | Medida exigida | Valor obtido |
|---|---|---|
| C01 modificabilidade | Mudança com impacto controlado (ver Template 22) | Não medido (mudança não implementada) |
| C02 usabilidade | Tarefa concluída sem ajuda em tempo definido com o cliente (limite proposto) | Não medido |
| C03 desempenho | Consulta em tempo adequado, mesmo com mais registros; limite **proposto:** 500 ms com 1.000 conteúdos | Medição preliminar no ambiente do assistente (1.000 conteúdos, 600 agendamentos, cliente de teste do Flask, mediana de 5 execuções): agenda 2 ms; pendentes 1 ms; conteúdos 9 ms; sugestões 0 ms. Repetir na máquina do grupo |
| C04 confiabilidade | Dados persistem após reinício | Não medido |
| C05 segurança | Acesso restrito a quem fez login | Verificado pelos testes de acesso (8 testes), sem teste de intrusão |

## Fichas de teste de release (principais)
**RT03 — H03 / RN03 / valor-limite.** Pré-condição: administrador logado; três conteúdos criados com dados fictícios. Passos: agendar o 1º em 01/12/2026 às 10:00; o 2º às 11:00; o 3º às 12:00. Esperado: sem aviso nos dois primeiros; aviso "já há 2 publicações" no terceiro; um 4º conteúdo às 10:00 é recusado. Obtido: ___.

**RT04 — H03 / reorganizar.** Pré-condição: um conteúdo agendado em 01/12/2026 às 10:00. Passos: no celular, usar o campo de data do item para escolher 05/12/2026; no computador, arrastar o item para outro dia. Esperado: data muda, hora permanece 10:00. Obtido: ___.

**RT06 — H05 / RN02 eventos.** Pré-condição: administrador logado. Passos: registrar evento "Encontro de teste" (tipo divulgação antecipada, data e prazo futuros, solicitante fictício); clicar em "Agendar publicação". Esperado: surge o conteúdo "Evento: Encontro de teste" na editoria "Agenda automotiva", com estado "agendado". Obtido: ___.

**RT11 — C04.** Pré-condição: banco com ao menos um conteúdo. Passos: parar e iniciar o servidor; conferir os dados; executar `python backup.py`. Esperado: dados permanecem e aparece um arquivo em `backups/`. Obtido: ___.
