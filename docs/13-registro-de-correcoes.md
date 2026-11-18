# 13 — Registro de correções e atualizações (errata)

Este documento funciona como o "comitê de atualização/correção" do projeto: reúne, em um só lugar, os erros encontrados na documentação e as atualizações necessárias. Cada item tem número, data de registro, documentos afetados e situação. Novas correções devem ser adicionadas ao final, sem apagar as anteriores.

**Responsáveis:** Bruno José Souza e Pablo Gonçalves Barbosa
**Como usar:** ao encontrar um erro, abra uma *Issue* com o rótulo `correcao` e acrescente uma linha neste registro.

---

## CORR-001 — Data da Ata de Contato nº 01 (alinhamento inicial)

- **Data do registro:** 15/11/2026
- **Documentos afetados:** Ata nº 01 e Registro de entrevista (primeiro contato) — ver [05](05-entrevistas-e-atas.md)
- **O que estava escrito:** "Data: 29/11".
- **Problema:** a entrevista principal (segundo contato) ocorreu em **02/11/2026**. O primeiro contato não poderia ser posterior a ela, então a data original continha um erro de digitação.
- **Correção:** o primeiro contato, por grupo de WhatsApp, ocorreu em **29/10**. A entrevista principal permanece em **02/11/2026**.
- **Situação:** Corrigido neste repositório. Pendente: corrigir também o arquivo original (PDF/Word) que será entregue ao professor.

## CORR-002 — Declaração de uso de IA (documento 12)

- **Data do registro:** 15/11/2026
- **Documentos afetados:** Declaração de uso de IA — ver [12](12-contribuicao-e-uso-de-ia.md)
- **O que estava escrito:** a declaração cita apenas o **ChatGPT (GPT-6)**.
- **Problema:** o grupo também utilizou o **Gemini**, que não constava na declaração.
- **Atualização necessária:** incluir o Gemini na declaração, informando versão/modelo, finalidade e parte do trabalho em que foi usado, além de manter os limites do uso (o que não foi feito com IA).
- **Situação:** Em andamento. Falta informar a versão do Gemini e a finalidade exata.

---

# Atualizações

## ATU-001 — Respostas às 12 dúvidas incorporadas
- **Data:** 15/11/2026
- **Origem:** informações repassadas pela equipe; a confirmação formal com o cliente ocorrerá na avaliação do primeiro incremento.
- **Documentos atualizados:** [02](02-historias-de-usuario.md), [03](03-regras-de-negocio.md), [09](09-registro-de-mudancas.md), [10](10-pendencias.md).

## ATU-002 — Implementação do primeiro incremento e atualização de status
- **Data:** 15/11/2026
- **Mudança:** MVP implementado (cinco módulos, 27 testes). ADR-001 passou a **Aceito**; criadas ADR-002 (stack) e ADR-003 (materiais por referência); atualizados os documentos [04](04-cenarios-de-qualidade.md), [07](07-modulos-e-dependencias.md), [08](08-padrao-strategy.md), [12](12-contribuicao-e-uso-de-ia.md) e criado [14](14-implementacao.md).
- **Situação:** concluída. Strategy e priorização automática seguem **não implementados**.
