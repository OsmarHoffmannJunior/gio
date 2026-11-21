# Impacto da 003 nas specs 001 e 002 e na constituição

Rev. 1b, 21/11/2026. **A 001 não foi alterada** (a rodada 2 de telas está editando). Na 002 fiz só os ajustes mínimos listados no fim, registrados no cabeçalho de cada arquivo.

## Constituição (soma à proposta 1.3.0 da 002)
1. **Novo princípio XVII. Medição é contrato.** Todo evento existe primeiro no dicionário versionado, com dono, schema e mapeamento de destinos; nenhum evento, tag ou destino vai a produção sem QA e aprovação. Um único carregador e um único banner de consentimento por marca; nenhum script livre de unidade.
2. **Princípio III:** acrescentar "conversões são enviadas aos destinos de anúncio pelo servidor, com o mesmo `event_id` do navegador para deduplicar".
3. **Princípio VII:** acrescentar "respostas de quiz só entram em segmentação com consentimento de personalização; perguntas de saúde bloqueadas até o princípio XV mudar".
4. **Princípio IX:** acrescentar "o orçamento de performance vale com as tags ligadas".
5. **Princípio X:** acrescentar "toda recomendação automática mostra fonte, regra e amostra".
6. **Princípio XI:** acrescentar "tags, destinos e verificação do Search Console são estrutura da rede; a unidade só preenche campos tipados liberados".

## Spec 001
- **FR-009 (eventos padronizados):** passa a apontar para o dicionário da 003 (FR-217 a FR-219). Renomear para o padrão `objeto_acao` em pt-BR: `view_unidade` > `unidade_visualizada`, `clique_whatsapp` > `whatsapp_clicado`, `clique_telefone` > `telefone_clicado`, `clique_rota` > `rota_clicada`, `compareceu offline` > `atendimento_compareceu`. `lead_iniciado` e `agendamento_concluido` continuam.
- **FR-025 (fim de scripts por unidade):** mantém; acrescentar "tags da unidade só por campos tipados do gerenciador (003, FR-231 a FR-235)".
- **FR-028 (insights):** tipos novos `sazonal_clima`, `demanda_quiz`, `penetracao_baixa`, `concorrencia`, `tracking_quebrado`, `utm_invalida`.
- **US14 e FR-027 (Wiki):** nova trilha "Medição e tags" com artigos por perfil e **vídeo explicativo por artigo** (003, US23 e FR-238). Entregável futuro, na fase de lançamento da Wiki às unidades e antes de abrir o gerenciador de tags às unidades. Artigos ganham `versao_interface` e marcação automática "revisar".
- **dados-ficha.md e aba SEO da ficha:** nova seção "Tags e medição" (GA4 próprio, `api_secret`, meta tag do Search Console, Google Ads, Meta, TikTok), com status de aprovação.
- **politica-campos.md:** novas chaves `tag.ga4_unidade`, `tag.gsc_meta`, `tag.google_ads_unidade`, `tag.meta_pixel_unidade`, `tag.tiktok_unidade` (T por padrão, EA por escopo) e `tag.script_livre` (sempre T para unidade).
- **rbac.md:** módulos novos "Quiz", "Inteligência", "Tracking e tags"; R-SEO (ou o dono do tracking) com V E A P em Tracking e tags; R-MKT com V E A P em Quiz; R-AG com V em dicionário e agregados; unidade com V E em Quiz (se liberado) e E nos campos de tags liberados.
- **data-model.md:** `evento` vira `evento_bruto` com as propriedades obrigatórias da FR-219; entram `evento_definicao`, `versao_dicionario`, `destino`, `envio_destino`, `link_rastreado`, `verificacao_gsc` e as tabelas de fontes externas (ver `data-model.md` da 003).
- **telas.md:** aba SEO da ficha com "Tags e medição" (T11); menu da rede com "Tracking" (T01 a T10) e "Inteligência" (I01 a I07).
- **plan.md:** a fase 0 já prevê a limpeza de tracking no site atual; a fase 1 ganha coletor próprio, loader único, banner e dicionário v1; a Wiki ganha o guia em vídeo; custos de server-side ficam fora (recomendação E usa o stack existente).

## Spec 002
- **Campanhas (US19):** novo objetivo "conhecer interesses (quiz)", com o quiz como conteúdo.
- **Interesses (FR-111):** origem `quiz` com peso e decaimento.
- **Central de privacidade (US3):** item "minhas respostas de quiz" para ver e apagar.
- **Atribuição (FR-121, FR-160):** os números vêm do coletor da 003 com o mesmo modelo.
- **Controles da rede (FR-142):** nova função controlada `quiz_unidade` e `tags_unidade`, padrão bloqueado.

### Ajustes feitos na 002 nesta rodada (registrados)
- `002-area-cliente/spec.md`: status rev. 1c; nota em US19 sobre objetivo quiz; FR-142 inclui `quiz_unidade` e `tags_unidade`.
- `002-area-cliente/data-model.md`: `interesse_cliente.origem` ganha `quiz`; `modelo_campanha.objetivo` ganha `quiz`; `funcao_controlada` ganha `quiz_unidade` e `tags_unidade`.
