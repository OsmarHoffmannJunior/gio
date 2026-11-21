# Data Model: Quiz, inteligência e tracking (003)

Rev. 1b, 21/11/2026. Complementa `../001-sistema-unidades/data-model.md` e `../002-area-cliente/data-model.md`. Mesmas convenções: `marca_id` em toda tabela de negócio, RLS por `atribuicao`, PII cifrada e fora de analytics, API-first (princípio XIV proposto).

## Quiz
- **quiz** (novo): id, marca_id, origem[rede|unidade], unidade_id?, modelo_quiz_id?, nome, objetivo[recomendar|conhecer_interesses|reativar|pesquisa], finalidade_texto_legal_id → texto_legal (002), status[rascunho|aguardando|aprovado|publicado|pausado|arquivado], versao_publicada_id?, criado_por, aprovacao_id? → aprovacao (001).
- **modelo_quiz** (novo): id, marca_id, nome, campos_livres[], escopos_permitidos, versao, ativo.
- **quiz_versao** (novo, imutável após publicar): id, quiz_id, numero, grafo_json (perguntas, opções, arestas), regras_recomendacao_json, textos_resultado_json, publicada_em.
- **pergunta** (novo, dentro da versão): id, quiz_versao_id, chave, tipo[unica|multipla|escala|imagem|faixa_etaria|cidade|texto_curto], texto, obrigatoria, ordem, sensivel_bloqueada bool (validador).
- **opcao** (novo): id, pergunta_id, chave, texto, imagem?, ordem, pontos_json{procedimento_id|categoria_id: pontos}, atributo_barreira?[preco|dor|tempo|medo_resultado|distancia].
- **aresta** (novo): quiz_versao_id, de_pergunta_id, condicao_json (opções), para_pergunta_id ou fim.
- **resposta_quiz** (novo): id, quiz_versao_id, marca_id, unidade_origem_id?, campanha_id?, canal[landing|area_cliente|link|qr|campanha], anon_id?, cliente_id?, iniciado_em, concluido_em?, ultima_pergunta_chave, resultado_json (procedimentos e pontos), consentimento_personalizacao bool (no momento), utm_json, cidade_ibge? (declarada ou da unidade), faixa_etaria?.
- **resposta_item** (novo): resposta_quiz_id, pergunta_chave, opcoes_chaves[], valor_escala?, texto? (curto, sem PII; validador de PII antes de gravar).
- **interesse_cliente** (002+): origem ganha `quiz`; `peso_inicial`, `decai_em_dias` (padrão 180 para meia-vida), `resposta_quiz_id?`.
- **barreira_cliente** (novo): cliente_id, tipo, origem[quiz|atendimento], atualizado_em.
- Agregados (sem PII): **agg_quiz_dia**(quiz_versao_id, dia, unidade_id, cidade_ibge, faixa_etaria, pergunta_chave, opcao_chave, contagem).

## Inteligência e fontes externas
- **fonte_externa** (novo): id, chave[ibge_localidades|ibge_censo_idade|ibge_pib|ibge_pop|pof|inmet_estacao|inmet_normais|inmet_avisos|open_meteo|feriados|calendario|trends|gbp_performance|places|search_console], dono_id, licenca, custo_texto, url_doc, frequencia, granularidade, ativa bool, ultima_coleta_em, ultimo_status.
- **municipio** (novo, referência IBGE): codigo_ibge, nome, uf, microrregiao, regiao_imediata, lat, lng, estacao_inmet_proxima?.
- **serie_municipio** (novo): codigo_ibge, data (ou ano/mes), variavel[pop_total|pop_faixa_sexo|pib|pib_pc|temp_media|temp_max|chuva|uv_max|normal_temp|normal_chuva|trends_indice], dimensao_json? (faixa, sexo, termo), valor, fonte_id, coletado_em. Índice por (variavel, codigo_ibge, data).
- **calendario_comercial** (novo): id, marca_id, data_inicio, data_fim, nome, tipo[feriado|data_comercial|estacao|evento_local], escopo[nacional|uf|municipio], uf?, codigo_ibge?, fonte.
- **gbp_metrica_dia** (novo; só com acesso concedido pela unidade): unidade_id, dia, impressoes_busca, impressoes_maps, rotas, ligacoes, cliques_site.
- **concorrente_local** (novo; só se D11 permitir): unidade_id, place_id, nome, categoria, distancia_m, nota, avaliacoes, lido_em.
- **regra_insight** (001+): tipos novos `sazonal_clima`, `demanda_quiz`, `penetracao_baixa`, `concorrencia`, `tracking_quebrado`, `utm_invalida`; `acao_sugerida_json` com `modelo_campanha_id` e unidades.
- **avaliacao_regra** (novo): regra_id, insight_id, acao[usada|descartada|ignorada], resultado_json, ts.

## Tracking
- **plano_medicao** (novo): id, marca_id?, pergunta_negocio, kpis[], eventos[], dono_id, versao.
- **evento_definicao** (novo, o dicionário): id, nome (objeto_acao), descricao, gatilho, origem[navegador|servidor|app], status[proposto|aprovado|ativo|obsoleto], dono_id, versao, mapeamentos_json{ga4, meta, google_ads, tiktok}, criado_em.
- **evento_propriedade** (novo): evento_definicao_id, nome, tipo[string|int|decimal|bool|enum|timestamp], obrigatoria, enum_valores[]?, descricao, pii_proibida bool (sempre true).
- **versao_dicionario** (novo): id, numero (semver), changelog, aprovado_por, publicado_em, json_schema_url.
- **evento** (001+, vira **evento_bruto**): event_id (único), event_name, schema_versao, marca_id, ambiente, plataforma, ts_cliente, ts_servidor, anon_id?, sessao_id, cliente_hash?, unidade_id?, template?, variante_id?, campanha_id?, quiz_id?, pagina_tipo, url_sem_query, utm_json, click_ids_json (gclid, gbraid, wbraid, fbclid, ttclid; só servidor), consentimento_json, props_json. Particionada por dia.
- **evento_invalido** (novo): recebido_em, payload_redigido, motivo, event_name?, schema_versao?.
- **identidade** (novo): marca_id, anon_id, cliente_id, ligado_em, metodo[cadastro|login]. Fora do alcance de analytics.
- **sessao** (novo, derivada): sessao_id, anon_id, inicio, fim, origem_json, unidade_id_primeira, paginas, eventos.
- **link_rastreado** (novo): id, marca_id, unidade_id?, campanha_id?, quiz_id?, url_destino, utm_source, utm_medium, utm_campaign, utm_content?, utm_term?, codigo_curto, dono_id, criado_em.
- **lista_utm** (novo): tipo[source|medium], valor, descricao, ativo.
- **destino** (novo): id, marca_id, escopo[rede|unidade], unidade_id?, tipo[ga4|google_ads|meta|tiktok|gsc|coletor], identificador (validado por tipo), segredo_ref? (cofre), consentimento_exigido[], status[rascunho|aguardando|ativo|suspenso], aprovado_por?, peso_estimado_kb?, criado_em.
- **envio_destino** (novo): event_id, destino_id, status[enviado|aceito|rejeitado|descartado_consentimento], resposta_resumo, tentativas, ts. Retenção curta.
- **alerta_tracking** (novo): id, tipo[queda_volume|pico|unidade_sem_conversao|invalidos|pii|utm], escopo, detalhes_json, status, ts.
- **verificacao_gsc** (novo): unidade_id?, tipo[prefixo_rede|meta_tag_unidade|dominio_proprio], propriedade_url, conteudo_meta?, status, verificado_em.
- **politica_campo** (001+): chaves novas `tag.ga4_unidade`, `tag.gsc_meta`, `tag.google_ads_unidade`, `tag.meta_pixel_unidade`, `tag.tiktok_unidade`, `tag.script_livre` (sempre T para unidade).

## Wiki (001+)
- **trilha** ganha tipo `medicao_tags`; **artigo** usa `video_url`, `perfis_alvo[]`, e ganha `versao_interface`, `revisar bool`, `revisar_motivo?` (marcado quando evento_definicao, destino ou tela mudam).

## Dicionário inicial (v0.1, proposta)
Propriedades obrigatórias da FR-219 valem para todos. Mapeamento para destinos entre parênteses.

| Evento | Origem | Propriedades específicas | Destinos |
|---|---|---|---|
| pagina_visualizada | navegador | pagina_tipo, unidade_id? | GA4 page_view |
| unidade_visualizada | navegador | unidade_id, template, variante_id | GA4 |
| catalogo_procedimento_visualizado | navegador | procedimento_id, unidade_id? | GA4 view_item |
| whatsapp_clicado | navegador | unidade_id, posicao | GA4; Meta Contact |
| telefone_clicado | navegador | unidade_id, posicao | GA4 |
| rota_clicada | navegador | unidade_id | GA4 |
| lead_iniciado | servidor | unidade_id, formulario, procedimento_id? | GA4 generate_lead (secundária); Meta Lead |
| agendamento_concluido | servidor | unidade_id, tipo[avaliacao|sessao], id_intencao, origem | GA4 conversão principal; Ads principal; Meta Schedule; TikTok |
| agendamento_remarcado | servidor | unidade_id | GA4 |
| agendamento_cancelado | servidor | unidade_id, motivo | GA4 |
| atendimento_compareceu | servidor (DocBiz) | unidade_id, tipo | Ads offline; Meta CAPI |
| cliente_cadastrado | servidor | metodo, unidade_preferida_id? | GA4 sign_up; Meta CompleteRegistration |
| cliente_logado | servidor | metodo | GA4 login |
| consentimento_alterado | servidor | finalidade, canal?, acao | coletor apenas |
| quiz_visualizado | navegador | quiz_id, versao | GA4 |
| quiz_iniciado | navegador | quiz_id, versao, canal | GA4 |
| quiz_pergunta_respondida | navegador | quiz_id, pergunta_chave, indice | coletor apenas (alto volume) |
| quiz_concluido | servidor | quiz_id, versao, procedimentos_recomendados[] | GA4 |
| quiz_resultado_salvo | servidor | quiz_id | GA4 |
| oferta_visualizada | navegador | promocao_id ou campanha_id | GA4 view_promotion |
| oferta_clicada | navegador | promocao_id ou campanha_id | GA4 select_promotion |
| pedido_criado | servidor | pedido_id, valor, unidade_id | GA4 begin_checkout |
| pagamento_aprovado | servidor (webhook) | pedido_id, valor, metodo, unidade_id | GA4 purchase; Ads; Meta Purchase; TikTok |
| pedido_estornado | servidor | pedido_id, valor | GA4 refund |
| sessao_realizada | servidor (DocBiz) | pacote_id, numero | coletor apenas |
| avaliacao_enviada | servidor | nps, unidade_id | coletor apenas |
| campanha_mensagem_entregue / _aberta / _clicada | servidor | campanha_id, canal | coletor apenas |
| link_rastreado_acessado | servidor | codigo_curto | coletor apenas |
