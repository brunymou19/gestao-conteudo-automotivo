# ADR-003 — Materiais como referências (sem upload)

- **Status:** Aceito · **Data:** 15/11/2026 · **Responsáveis:** Bruno José Souza e Pablo Gonçalves Barbosa
- **Relacionados:** H07, RN07, C04, M04, M08

## Contexto
O cliente trabalha pelo celular, guarda fotos e vídeos na galeria e informou que **não haverá upload pelo celular**. Também apontou os materiais como a informação mais prejudicial de se perder.

## Alternativas
1. **Guardar só referências** (nome do arquivo, pasta ou link) — + simples, + sem consumo de espaço e sem risco de upload grande · − o sistema não garante que o arquivo continua existindo.
2. **Upload dos arquivos para o sistema** — + materiais centralizados · − descartado pelo cliente; exige armazenamento, limites de tamanho e mais segurança.

## Decisão
Cada conteúdo guarda uma lista de referências com tipo (foto, vídeo ou outro). O sistema não armazena os arquivos.

## Consequências
- **Melhora:** simplicidade e rapidez; o banco continua pequeno.
- **Piora (trade-off):** o arquivo em si continua só no celular do cliente; o `backup.py` protege os registros (referências, datas, eventos), mas **não os arquivos**.
- **Mais difícil de mudar depois:** adotar upload no futuro exigirá nova tabela de arquivos e armazenamento.

## Como verificar
Testes de adicionar, listar e remover referências, e recusa de tipo inválido.
