# 01 — Plano do projeto e visão do produto

**Disciplina:** Engenharia de Software II — CSI410 · **Instituição:** UFOP
**Integrantes:** Bruno José Souza e Pablo Gonçalves Barbosa
**Cliente principal:** administrador de uma página de conteúdo automotivo

## 1. Visão do produto
Sistema de Apoio à Gestão de Conteúdo Automotivo, para auxiliar o administrador na organização, acompanhamento e planejamento de suas atividades editoriais.

Hoje o administrador cuida sozinho de todas as etapas: identificar oportunidades, obter materiais, editar e publicar. As demandas surgem de forma irregular (veículos encontrados na rua, encontros, eventos, ideias e solicitações externas). Com o crescimento da página aumentaram os materiais recebidos de seguidores, proprietários de veículos e organizadores de eventos. Sem um processo centralizado, é difícil acompanhar pendências, planejar publicações e manter frequência consistente.

A solução centraliza essas informações: registrar ideias, acompanhar a produção, organizar materiais, planejar publicações e controlar solicitações de eventos e oportunidades de parceria.

## 2. Problema identificado
- Produção, edição e publicação concentradas em uma pessoa.
- Conteúdos surgem espontaneamente ou por solicitações via Instagram e e-mail.
- Fotos e vídeos ficam na galeria do celular; edição e publicação seguem a ordem de chegada, sem planejamento editorial.
- Após eventos maiores há mais de 30 fotos, além de vídeos, o que pode superar a capacidade individual e gerar acúmulo.

## 3. Objetivos
**Geral:** desenvolver um sistema que auxilie na gestão do conteúdo automotivo, com mais organização, visibilidade das pendências e controle do planejamento editorial.

**Específicos:**
- Centralizar o registro de ideias e conteúdos.
- Organizar fotos, vídeos e materiais recebidos.
- Acompanhar o andamento da produção e edição.
- Planejar publicações por meio de uma agenda editorial.
- Controlar datas e prazos.
- Registrar e acompanhar solicitações de eventos.
- Organizar oportunidades e parcerias.
- Facilitar a identificação de conteúdos pendentes e atividades prioritárias.
- Permitir a evolução das categorias editoriais e das funcionalidades.

## 4. Stakeholders
- **Cliente principal / usuário principal:** administrador da página.
- **Equipe de desenvolvimento:** Bruno José Souza e Pablo Gonçalves Barbosa.
- **Professor da disciplina:** orientação e avaliação.
- **Outros envolvidos:** organizadores de eventos, proprietários de veículos, seguidores e outros administradores de páginas automotivas (ouvidos como referência complementar, sem substituir a validação do cliente).

## 5. Processo atual de trabalho
O processo começa quando o administrador vê um automóvel interessante ou participa de um encontro/evento. Ele registra as imagens, edita pelo celular e publica no Instagram. Também recebe fotos, vídeos e pedidos de divulgação por mensagens no Instagram e e-mail; esse material de terceiros também pode ser editado e publicado. A organização é feita pela galeria do celular, sem agenda centralizada.

A equipe acompanhou presencialmente um caso real: organização de um pequeno encontro automotivo, divulgação antecipada, realização do encontro, fotos e edição/publicação no mesmo dia.

## 6. Escopo
**Previsto:**
- Cadastro e organização de ideias e conteúdos
- Acompanhamento das etapas de produção
- Associação de fotos, vídeos e outros materiais aos conteúdos
- Organização por categorias editoriais
- Agenda de planejamento de publicações
- Controle de datas e prazos
- Registro e acompanhamento de solicitações de eventos
- Organização de oportunidades e parcerias
- Visualização de conteúdos pendentes e atividades prioritárias

**Fora do escopo inicial:**
- Publicação automática no Instagram
- Editor de imagens completo
- Integração obrigatória com ferramentas de IA
- Gerenciamento de equipe com múltiplos administradores
- Substituição dos aplicativos de edição usados pelo cliente

Esses limites podem ser revistos se o levantamento identificar necessidades relevantes e viáveis.

## 7. Estratégia de levantamento e validação
Três momentos de contato com o cliente:
1. **Levantamento inicial:** entender processo, dificuldades, regras e prioridades.
2. **Avaliação do primeiro incremento:** apresentar protótipo/primeira versão e coletar observações.
3. **Avaliação final:** apresentar a solução, verificar atendimento aos requisitos e registrar aceitação.

O primeiro contato foi online (grupo de WhatsApp). Em **02/11/2026** houve encontro presencial, com aprofundamento do levantamento e observação do processo real.

## 8. Escopo de implementação e prioridades
Prioridade do cliente: melhorar a organização geral do processo e ampliar a capacidade de acompanhar contatos externos e oportunidades. **Primeira versão: agenda de organização de conteúdos e datas de publicação**, para visualizar pendências, organizar o planejamento e reduzir a dependência da galeria do celular. As demais funcionalidades serão priorizadas conforme contribuição a esse objetivo, validação com o cliente e viabilidade técnica/acadêmica.

## 9. Organização da equipe
- **Bruno José Souza:** levantamento de requisitos, condução da entrevista principal e atividades atribuídas à sua parte.
- **Pablo Gonçalves Barbosa:** levantamento de requisitos, registro das informações da entrevista principal e atividades atribuídas à sua parte.
- A distribuição detalhada de histórias e tarefas será definida pela equipe (use o quadro *Projects* do GitHub).

## 10. Riscos e pontos de atenção
- Disponibilidade do cliente para os contatos previstos
- Mudanças de necessidades e prioridades
- Crescimento irregular de materiais recebidos
- Dependência da organização individual do administrador
- Limitações técnicas para integração com serviços externos
- Manter o escopo compatível com o prazo acadêmico
- Validar regras e critérios ainda sem definição definitiva

(Detalhes em [06 — Matriz de riscos](06-matriz-de-riscos.md).)

## 11. Entregas previstas
Plano e visão do produto · Registros de contatos e entrevistas · Levantamento e especificação de requisitos · Histórias de usuário e critérios de aceitação · Regras de negócio · Cenários de qualidade · Definição do escopo dos incrementos · Documentação arquitetural e decisões técnicas · Implementação do sistema · Avaliação e validação final com o cliente.

## 12. Aceite do cliente e consentimento
- **Carta de aceite do cliente (Etapa 1):** assinada pelo cliente em 03/11/26.
- **Termo de consentimento (Etapas 1 e 4):** assinado. Autorizados: anotações, gravação de áudio, transcrição automática por IA, gravação de tela sem rosto, fotografias de ambiente/documentos sem identificar pessoas. **Não** autorizado o uso do nome nos relatórios (cliente identificado apenas pela função).
- Os documentos originais assinados **não** devem ser publicados no repositório (guarde-os fora do GitHub).

> Observação: o termo de consentimento diz que os registros são de acesso restrito ao grupo. Por isso, recomenda-se manter o repositório **privado** (adicionando o professor como colaborador).
