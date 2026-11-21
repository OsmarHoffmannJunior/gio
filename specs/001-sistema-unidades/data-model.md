# Data Model (resumo)

- **marca**(id, nome, tema_json, dominio_principal, regras_texto_json)
- **unidade**(id, marca_id, slug, nome, status[ativa|inauguracao|inativa], tipo[full|slim], cnpj, id_docbiz, id_crm, cro, telefone, whatsapp, email, cep, uf, cidade, bairro, logradouro, numero, complemento, referencia, lat, lng, inauguracao, permitir_agendamento, template_id, estrategia_canonical[ficha|dominio|redireciona], dominio, completude, grupo_id)
- **horario_funcionamento**(unidade_id, dia, abre, fecha) / **horario_agenda** / **excecao**(data, motivo, global|unidade)
- **foto**(unidade_id, url, tipo[fachada|recepcao|sala|equipe|antes_depois], alt, ordem, status_aprovacao)
- **profissional**(unidade_id, nome, cargo, registro, foto, responsavel_tecnico)
- **tratamento**(id, marca_id, categoria, nome, url_nacional) / **unidade_tratamento**(unidade_id, tratamento_id, destaque, texto_local)
- **faq**(unidade_id, pergunta, resposta, ordem)
- **template**(id, marca_id, nome[A|B|C], blocos_json) / **landing**(unidade_id, template_id, blocos_json, versao, status[rascunho|aguardando|publicada])
- **aprovacao**(id, unidade_id, tipo, diff_json, status, revisor_id)
- **gbp**(unidade_id, place_id, nota, avaliacoes, categoria, site, telefone, sincronizado_em)
- **lead**(id, marca_id, unidade_id, nome, email, telefone, tratamento, status[novo|contatado|agendado|compareceu|nao_compareceu|perdido], fila[unidade|call_center], responsavel_id, sla_vence_em, primeiro_contato_em, id_docbiz, origem_json{canal,utm_*,gclid,fbclid,referrer,landing}, consentimento_id)
- **evento**(id, lead_id?, sessao_id, unidade_id, tipo, url, ts, props_json) (sem PII)
- **consentimento**(id, texto_versao, ip, user_agent, ts, finalidades)
- **ticket**(id, origem[unidade|cliente], unidade_id, categoria, prioridade, status, sla_vence_em, responsavel_id) / **mensagem_ticket**
- **artigo**(id, marca_id, publico[unidade|cliente], titulo, corpo, tags)
- **usuario**(id, nome, email, externo, 2fa_tipo, ultimo_login, expira_em, status) (papel e escopo saem daqui e vão para atribuicao)
- **auditoria**(id, marca_id, unidade_id?, usuario_id, perfil_id, acao[editar|publicar|aprovar|reverter|exportar|ver_pii|override|alterar_perfil|ver_como], entidade, entidade_id, campo?, antes, depois, motivo?, lote_id?, ip, user_agent, ts) (append only)
- **relatorio_salvo**(id, dono_id, filtros_json, formato, agenda_cron, destinatarios)

## Rev. 2 (21/11/2026): RBAC, política de campos, schema base, override
- **regional**(id, marca_id, nome) / **regional_unidade**(regional_id, unidade_id)
- **perfil**(id, marca_id, codigo, nome, nivel[rede|regional|unidade], padrao bool, base_perfil_id?, ativo, criado_por) (padrões: R-ADM, R-MKT, R-SEO, R-COM, R-CC, R-FIN, R-AG, G-REG, U-FRQ, U-GER, U-REC)
- **perfil_permissao**(perfil_id, modulo[ficha|landing|schema_seo|dominio|aprovacoes|leads|relatorios|avaliacoes|suporte|usuarios|auditoria|marca|integracoes], acoes set[ver|editar|aprovar|publicar|exportar|pii], restricao[agr|fila|conteudo|seo|propria]?)
- **teto_nivel**(nivel, modulo, acoes_max) (constante do sistema; impede perfil personalizado acima do teto; Agência nunca com pii)
- **atribuicao**(id, usuario_id, perfil_id, escopo_tipo[rede|regional|unidade], escopo_id?, inicio, fim?, concedido_por) (uma pessoa pode ter várias)
- **politica_campo**(id, marca_id, chave_campo, grupo, tipo[campo|bloco|seo], perfil_id?, estado[T|E|EA|L|O], aprovador_perfil_id?, validadores_json, versao) (perfil nulo = vale para todos os perfis de unidade)
- **schema_base**(id, marca_id, tipo_unidade?, schema_type, categorias_json, same_as_json, parent_org_json, mapeamento_json, ativo, versao)
- **faq_base**(id, marca_id, pergunta, resposta, ordem, ativo)
- **seo_unidade**(unidade_id, title_override?, description_override?, robots, canonical_estrategia, jsonld_gerado, jsonld_valido bool, validado_em) (escrita só por perfil com schema_seo:editar)
- **valor_campo_versao**(id, unidade_id, chave_campo, valor_json, status[rascunho|aguardando|publicado|em_conflito|revertido|despublicado], origem[unidade|rede|sistema], autor_id, motivo?, lote_id?, aprovacao_id?, ts) (histórico por campo e base do reverter)
- **lote_alteracao**(id, marca_id, autor_id, descricao, motivo, filtro_unidades_json, total_unidades, status, ts)
- **promocao**(id, unidade_id, modelo_id, titulo, tratamento_id, condicao, inicio, fim, status) / **modelo_promocao**(id, marca_id, campos_json, regras_json)
- **notificacao**(id, usuario_id, tipo[alteracao_rede|aprovacao|sla|chamado|lote], entidade, entidade_id, resumo, diff_json?, lida_em, canal[sino|email|resumo_diario])
- **contestacao**(id, auditoria_id, unidade_id, autor_id, ticket_id, status)
- Notas:
  - **aprovacao** ganha `aprovador_perfil_id` e a trava "autor diferente do aprovador".
  - **foto** ganha `termo_imagem_url` para antes e depois e para pessoas.
  - **profissional** ganha `consentimento_imagem`.
  - RLS no Postgres usa `atribuicao` para filtrar `unidade_id` e bloquear colunas de PII sem a ação `pii`.

## Rev. 3 (21/11/2026): Wiki, insights, módulos, modelos de ficha, variantes, GBP da unidade, LGPD centralizada
- **artigo** ganha `perfis_alvo[]`, `modulo`, `video_url`, `trilha_id?`, `ordem`, `uteis`, `nao_uteis`; **trilha**(id, marca_id, nome, perfil_alvo, tipo[primeiros_passos|modulo|gbp|novidades]); **checklist_item**(trilha_id, texto, artigo_id) / **checklist_progresso**(unidade_id, checklist_item_id, feito_em, feito_por); **busca_sem_resultado**(termo, perfil, ts)
- **regra_insight**(id, marca_id, tipo[queda|pico|sla|completude|gbp_divergente|campanha], parametros_json, ativa) / **insight**(id, regra_id, escopo_tipo, escopo_id, titulo, numeros_json, fonte, periodo, acao_sugerida, status[novo|visto|resolvido|descartado], ts) / **assinatura_relatorio**(usuario_id, frequencia, tipos[], canal_email)
- **modulo**(chave, nome, descricao, padrao bool) / **modulo_regra**(modulo_chave, escopo_tipo[rede|regional|unidade], escopo_id?, ligado bool, autor_id, ts) (herança: unidade > regional > rede)
- **modelo_ficha**(id, marca_id, nome, status[rascunho|ativo|arquivado], principal bool, base_id?, blocos_json, campos_visiveis_json, versao) / **menu_item**(modelo_id, rotulo, ancora, ordem, visivel, tipo[ancora|link_variante]) ; **unidade.modelo_ficha_id** (nulo = principal)
- **landing_variante**(id, unidade_id, tipo[principal|ab|campanha|servico], nome, slug, template_id, blocos_json, status[rascunho|aguardando|em_teste|no_ar|encerrada], indexavel bool, canonical_para?, trafego_pct?, utm_json?, inicio, fim, vencedora bool) / **metrica_variante**(variante_id, dia, visitas, leads, taxa)
- **gbp_snapshot**(unidade_id, place_id, lido_em, nome, endereco, telefone, site, categoria, horario_json, nota, avaliacoes, sem_resposta) / **divergencia_gbp**(unidade_id, campo, valor_cadastro, valor_gbp, status, artigo_id) (sem escrita no GBP; **gbp** da rev. 1 vira este snapshot)
- **base_legal**(id, marca_id, finalidade[atendimento|marketing|analytics], base[consentimento|legitimo_interesse|execucao_contrato], texto_versao) / **politica_retencao**(marca_id, entidade, prazo_dias, acao[anonimizar|excluir]) / **pedido_titular**(id, marca_id, canal, tipo[acesso|correcao|exclusao|portabilidade|revogacao], titular_hash, unidade_id?, status, prazo_em, responsavel_id, evidencias_json)


## Rev. 3.1 (21/11/2026): contas só por convite
- **convite**: id, email, perfil_id, escopo (rede, regional, unidade), unidade_id, regional_id, criado_por (usuario_id), criado_em, expira_em (72 h), usado_em, reenviado_vezes, status (pendente, aceito, vencido, revogado). Índice único em (email, status=pendente).
- **provisionamento_unidade**: id, unidade_id, etapa (dados, modelo_ficha, modulos, regional, dominio, conta_admin), concluido_por, concluido_em.
- **usuario**: novos campos senha_trocada_em, mfa_ativado_em, origem='convite' (único valor permitido), convite_id.
- Regra: criação de usuario só por aceite de convite válido; o perfil do convite precisa estar entre os perfis liberados para o escopo de quem convidou.

## Rev. 3.2 (21/11/2026): integração das specs 002 e 003
- `tratamento` vira `procedimento` com campos novos (com visão de compatibilidade); `unidade_tratamento` vira `oferta_unidade`.
- `lead` ganha `cliente_id`.
- `consentimento` ganha `titular_tipo`, `titular_id`, `finalidade`, `canal`, `texto_legal_id`, `acao`, `origem`.
- `promocao` e `modelo_promocao` ampliados conforme o `data-model.md` da 002.
- `notificacao` ganha tipo `aviso`; `ticket` ganha `cliente_id` e canal; `pedido_titular` ganha `cliente_id`.
- `perfil_permissao.modulo` ganha os módulos novos (ver `rbac.md`, rev. 3.2).
- `modulo` ganha `area_cliente`, `pagamento_online`, `campanhas_unidade`, `chat_cliente`, `mural_avisos`, `quiz`, `inteligencia`, `tracking_tags`.
- `regra_insight.tipo` ganha `campanha_destaque`, `cota_estourada`, `nps_baixo`, `no_show_alto`, `aviso_pendente`, `sazonal_clima`, `demanda_quiz`, `penetracao_baixa`, `concorrencia`, `tracking_quebrado`, `utm_invalida`.
- `politica_retencao` ganha as entidades da 002.
- `evento` vira `evento_bruto` com as propriedades obrigatórias da FR-219 da 003; entram `evento_definicao`, `versao_dicionario`, `destino`, `envio_destino`, `link_rastreado`, `verificacao_gsc` e as tabelas de fontes externas (ver `data-model.md` da 003).
- Nomes de evento no padrão `objeto_acao`: `unidade_visualizada`, `lead_iniciado`, `agendamento_concluido`, `whatsapp_clicado`, `telefone_clicado`, `rota_clicada`, `atendimento_compareceu`.

## Rev. 3.3 (21/11/2026): auditoria geral
- **auditoria** passa a ser a tabela única da auditoria geral, só de inclusão: id (sequencial), criado_em (servidor), marca_id, escopo[rede|regional|unidade], regional_id?, unidade_id?, usuario_id (ou `sistema`), perfil_id, modulo, tipo[alteracao|dado_pessoal|permissao|tags|campanha|configuracao|exportacao|acesso|aprovacao], acao, entidade, entidade_id, antes (jsonb), depois (jsonb), motivo, status_aprovacao[direto|direto_rede|pendente|aprovado|rejeitado], solicitante_id?, decisor_id?, motivo_decisao?, ip (guardado completo, mascarado na tela), dispositivo (user agent resumido), sessao_id, hash_anterior, hash.
- Regras: sem UPDATE e sem DELETE para qualquer papel do banco (permissão revogada e gatilho que bloqueia); a cadeia `hash = sha256(hash_anterior + registro)` é verificada todo dia; retenção por `politica_retencao` (D14: alterações 5 anos, acessos a dado pessoal 2 anos) com expurgo só por rotina do sistema, que grava o próprio registro de expurgo.
- Índices por criado_em, unidade_id, usuario_id, modulo, tipo e status_aprovacao para os filtros da tela 17. Exportação CSV gera registro `tipo=exportacao`.

