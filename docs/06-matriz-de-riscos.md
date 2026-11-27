# Template 10 — Matriz de riscos

Posição: 26/11/2026. Probabilidade e impacto: B (baixa), M (média), A (alta). Estratégia: evitar, minimizar ou plano de contingência. Situação: ativo, materializado ou encerrado. Responsáveis: Bruno José Souza e Pablo Gonçalves Barbosa (divisão por risco a confirmar).

| ID | Risco | Prob. | Imp. | Estratégia e ação | Gatilho | Resp. | Situação |
|---|---|---|---|---|---|---|---|
| R01 | Acúmulo de conteúdos pendentes de edição | M | A | **Minimizar.** Agenda, estados e lista de pendentes implementados; falta validar o uso com o cliente | Muitas fotos e vídeos aguardando edição após eventos | Bruno e Pablo | Ativo |
| R02 | Atrasos nas publicações e perda de oportunidades | M | A | **Minimizar.** Agenda com atrasados, eventos com prazo e sugestões por regra semanal implementados | Pedido recebido perto da data do evento; conteúdo importante sem data | Bruno e Pablo | Ativo |
| R03 | Requisitos incompletos ou interpretados incorretamente | M | A | **Minimizar.** Respostas às 12 dúvidas incorporadas; confirmar com o cliente as respostas e os valores provisórios (situações das oportunidades, tipos de evento) | Divergência entre o sistema e o que o cliente espera | Bruno e Pablo | Ativo |
| R04 | Alterações frequentes de escopo | M | M | **Minimizar.** Mudanças registradas (M01–M15); manter fora do escopo Instagram automático, editor de imagens e IA | Pedido de nova funcionalidade | Bruno e Pablo | Ativo |
| R05 | Dificuldades de integração e organização do código | M | A | **Minimizar.** Branch e pull request para alterações; mensagens de commit descritivas | Arquivos duplicados, versões conflitantes, erro após integrar | Bruno e Pablo | **Materializado** (reorganizado em 18/11/2026; risco residual ativo) |
| R06 | Alterações entram na main sem revisão e sem execução automática dos testes (não há pipeline) | M | M | **Minimizar.** Exigir PR com revisão do outro integrante; configurar GitHub Actions executando `python -m pytest` | Commit direto na main; teste falhando sem ninguém perceber | Bruno e Pablo | Ativo |
| R07 | Interface não validada em celular real (uso principal do cliente) | M | A | **Minimizar.** Testar a tela em celular e na avaliação do primeiro incremento; arrastar na agenda pode não funcionar em toque (há campo de data como alternativa) | Cliente não consegue usar a agenda pelo celular | Bruno e Pablo | Ativo |
| R08 | Perda de registros (banco SQLite local e backup manual) | M | A | **Minimizar.** Executar `backup.py` periodicamente. **Contingência:** restaurar a cópia mais recente. Os arquivos de foto e vídeo ficam só no celular do cliente | Falha do computador; exclusão do arquivo do banco | Bruno e Pablo | Ativo |
| R09 | Exposição de informações do cliente no repositório público | A | A | **Plano de contingência.** O cliente pediu que seu nome não seja divulgado. O nome foi removido dos arquivos na entrega do Incremento 1 (substituído por "cliente (administrador da página)"), mas permanece no histórico antigo do Git | Nome do cliente visível a terceiros | Bruno e Pablo | **Materializado** (removido dos arquivos; permanece no histórico) |
| R10 | Inconsistência entre declarações (uso de IA, contribuição) e o histórico real | M | A | **Evitar.** Declarar todas as ferramentas e finalidades; conferir commits e PRs antes de assinar | Declaração diferente do que ocorreu | Bruno e Pablo | Ativo |

## Histórico de revisões

| Data | Risco | O que mudou | Por quê |
|---|---|---|---|
| A definir (versão inicial) | R01–R05 | Criação dos cinco riscos com a classificação original (R01 A/A; R02, R03, R05 M/A; R04 M/M) | Primeira versão da matriz (ver histórico anterior) |
| 26/11/2026 (proposta de revisão, a confirmar pelo grupo) | R01 | Probabilidade A → M | Agenda, estados e pendentes implementados (testes passam); sem validação do cliente |
| 26/11/2026 (idem) | R02 | Ação atualizada; classificação mantida | Atrasados, prazos de eventos e sugestões implementados |
| 26/11/2026 (idem) | R03 | Ação atualizada; classificação mantida | 12 respostas incorporadas, mas há valores provisórios e falta a avaliação do cliente |
| 26/11/2026 (idem) | R04 | Ação atualizada | Mudanças M06–M14 registradas |
| 18/11/2026 | R05 | Situação: ativo → materializado | Uploads manuais deixaram arquivos duplicados e versões antigas em `app/`; corrigido pelo PR #18 |
| Data do merge do PR de documentação (preencher) | R09 | Nome removido dos arquivos do repositório | Pedido do cliente de não divulgar o nome |
| 26/11/2026 (proposta) | R06–R10 | Riscos novos | Ausência de pipeline e de revisão; tela não testada em celular; backup manual; nome do cliente no repositório; consistência das declarações |

Datas de revisões anteriores à de 26/11/2026 que não constam em registro do repositório permanecem "a definir".
