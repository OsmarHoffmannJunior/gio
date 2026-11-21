# Data Model: Área do Cliente (002)

Rev. 1c, 21/11/2026 (integração com a 003: origem quiz, objetivo quiz, funções quiz_unidade e tags_unidade). Complementa `../001-sistema-unidades/data-model.md`. Convenções da 001 valem aqui: toda tabela de negócio tem `marca_id` (e `unidade_id` quando couber), RLS por `atribuicao` para perfis internos, PII cifrada por campo e mascarada por padrão, auditoria append only.

## Princípio de arquitetura: API-first
- Uma API versionada (`/v1`), REST com contrato OpenAPI, usada pelo site da área do cliente, pelos painéis da 001 e pelo app futuro. Nada de regra de negócio só no front.
- Dois públicos de autenticação: **clientes** (pool próprio, OIDC com PKCE, tokens curtos e refresh rotativo) e **usuários internos** (pool da 001, 2FA). Escopos OAuth separados: `cliente:*` só enxerga recursos do próprio `cliente_id`.
- Webhooks de entrada (DocBiz, gateway, Meta/WhatsApp, e-mail) e de saída (Salesforce, BI) passam por fila com idempotência (`chave_idempotencia`) e reprocessamento.
- Eventos de domínio (`cliente_cadastrado`, `consentimento_alterado`, `agendamento_confirmado`, `pedido_pago`, `sessao_realizada`, `campanha_enviada`...) num barramento interno; analytics recebe só `cliente_hash`, nunca PII (princípio III e VII).
- IDs públicos opacos (UUID v7), nunca hash de e-mail na URL.

## Legenda de relação com a 001
- (001) entidade que já existe e é reutilizada.
- (001+) entidade da 001 que ganha campos (detalhe em `impacto-na-001.md`).
- (novo) entidade criada nesta spec.

## Identidade e perfil
- **cliente** (novo): id, marca_id, status[pendente_verificacao|ativo|bloqueado|em_exclusao|anonimizado], nome, nome_social?, email (cifrado, único por marca), email_verificado_em, celular (cifrado, único por marca), celular_verificado_em, data_nascimento? (cifrado), maior_idade_declarada_em, cpf? (cifrado, só na compra), genero?, cidade_ibge, uf, cep?, unidade_preferida_id? → unidade (001), origem_cadastro_json{canal, utm_*, campanha_id?, unidade_id?, lead_id?}, como_conheceu[google|instagram|indicacao|passou_na_frente|tv_radio|outro], como_conheceu_texto?, completude, idioma, criado_em, ultimo_acesso_em.
- **cliente_identidade** (novo): cliente_id, provedor[email_otp|whatsapp_otp|link_magico|google|apple|senha|passkey], sujeito_externo, criado_em, ultimo_uso_em. (Senha com hash forte; passkey com credencial pública.)
- **sessao_cliente** (novo): id, cliente_id, dispositivo, plataforma[web|ios|android], ip, criado_em, expira_em, revogada_em.
- **codigo_verificacao** (novo): id, destino_hash, canal[email|whatsapp|sms], finalidade[cadastro|login|troca_contato], tentativas, expira_em (curto, só para controle; apagado após uso).
- **endereco_cliente** (novo, fase 2): cliente_id, tipo[cobranca], cep, logradouro..., cifrado.
- **dependente** (novo, fase 3): id, responsavel_cliente_id, nome, data_nascimento, parentesco, consentimento_responsavel_id.
- **cliente_vinculo_unidade** (novo): cliente_id, unidade_id, tipo[preferida|agendou|comprou|atendido|campanha], primeiro_em, ultimo_em. Base da regra "unidade só vê clientes vinculados".
- **cliente_vinculo_docbiz** (novo): cliente_id, unidade_id, id_paciente_docbiz, vinculado_em, metodo[cpf|email|celular|manual]. 
- **lead** (001+): ganha `cliente_id?`; ao verificar o contato, lead e cliente se ligam.

## Consentimento e privacidade
- **texto_legal** (novo): id, marca_id, tipo[termos|privacidade|marketing|personalizacao|compartilhar_unidade|imagem|saude|regulamento], versao, corpo, material bool, publicado_em.
- **consentimento** (001+): passa a ter `titular_tipo[lead|cliente]`, `titular_id`, `finalidade`, `canal?[email|whatsapp|sms|push]`, `texto_legal_id`, `acao[concedido|revogado]`, `origem[site|app|unidade|importacao]`, ip, user_agent, ts. Histórico imutável; o estado atual é a última linha por finalidade e canal.
- **preferencia_contato** (novo): cliente_id, canal, faixa_inicio, faixa_fim, frequencia_max_semana, valido bool (bounce ou número inválido).
- **pedido_titular** (001+): ganha `cliente_id?` e tipo `revisao_decisao_automatizada`.
- **politica_retencao** (001): novas entidades cliente, pedido, notificacao, campanha_envio.

## Interesses
- **categoria_interesse** (novo): id, marca_id, nome, ordem (categorias de estética, sem condições médicas).
- **interesse_cliente** (novo): cliente_id, procedimento_id? ou categoria_id?, origem[declarado|inferido|quiz], peso, atualizado_em. Inferido só com consentimento de personalização.

## Catálogo, ofertas e preço
- **procedimento** (001+, hoje `tratamento`): ganha descricao_aprovada, beneficios, indicacao, contraindicacoes_gerais, sessoes_tipicas, intervalo_dias, duracao_min, cuidados_pre, cuidados_pos, idade_minima, imagens, visibilidade_preco_padrao[oculto|logado|promocao|publico], preco_sugerido?, preco_teto?, preco_piso? (ver D1), compravel_online bool, ativo.
- **produto** (novo, opcional): id, marca_id, nome, tipo[home_care|vale|kit], sku, preco_sugerido. Para campanhas que vinculam produtos.
- **modelo_pacote** (novo): id, marca_id, procedimento_id, sessoes, validade_dias, intervalo_min_dias, regras_cancelamento_texto_legal_id, transferivel bool.
- **oferta_unidade** (novo, substitui `unidade_tratamento` da 001 com mais campos): id, unidade_id, procedimento_id, ativa, duracao_local_min?, preco?, visibilidade_preco, compravel_online, texto_local?, destaque bool, status_aprovacao, versao.
- **pacote_unidade** (novo): id, unidade_id, modelo_pacote_id, preco, parcelas_max, sem_juros_ate, ativo.

## Promoções
- **modelo_promocao** (001+): ganha tipo[avaliacao_gratuita|sessao_bonus|percentual|preco_fixo|brinde|combo], campos_livres[], regulamento_template, exige_aprovacao_unidade bool, escopos_permitidos.
- **promocao** (001+): ganha origem[rede|unidade], adesao[obrigatoria|opcional], procedimentos[], pacotes[], preco_de?, preco_por?, limite_usos?, usos, regulamento_texto_legal_id, alcance_json, status[rascunho|aguardando|aprovada|no_ar|pausada|encerrada|reprovada].
- **adesao_promocao** (novo): promocao_id, unidade_id, status[aderiu|recusou|pendente], por_id, ts.

## Controle da rede (US17)
- **funcao_controlada** (novo, catálogo do sistema): chave[precos|procedimentos_locais|pacotes_locais|promocoes|campanhas_clientes|canal_email|canal_whatsapp|canal_push|canal_area_cliente|avisos_regionais|ver_base_clientes|exportar_clientes|quiz_unidade|tags_unidade], descricao, padrao='bloqueado'.
- **liberacao** (novo): id, marca_id, funcao_chave, escopo_tipo[rede|regional|unidade], escopo_id?, estado[bloqueado|liberado|liberado_com_aprovacao], autor_id, motivo, inicio, fim?, ts. Herança unidade > regional > rede; sem linha = bloqueado.
- **limite_envio** (novo): id, marca_id, escopo_tipo, escopo_id?, campanhas_por_periodo, mensagens_por_periodo, periodo[semana|mes], orcamento_whatsapp_centavos?, freq_max_cliente_semana, janela_inicio, janela_fim, dias_bloqueados[], alcance_max_tipo[propria_unidade|raio|cidades|uf], raio_km?, cidades_ibge[]?, ufs[]?, autor_id, ts.
- **teto_alcance** (constante do sistema, como `teto_nivel` da 001): perfil de unidade nunca alcança "base nacional"; aplicado por constraint e RLS.
- **consumo_cota** (novo): escopo_tipo, escopo_id, periodo_ref, campanhas_usadas, mensagens_usadas, gasto_whatsapp_centavos.
- **pedido_liberacao** (novo): id, unidade_id, funcao_chave, justificativa, ticket_id → ticket (001), status.

## Mural de avisos internos (US18)
- **aviso** (novo): id, marca_id, autor_id, categoria[novidade|promocao_rede|comunicado|treinamento|prazo|sistema], prioridade[normal|alta|urgente], titulo, corpo, anexos[], artigo_id? → artigo (001), promocao_id?, campanha_id?, exige_confirmacao bool, prazo_confirmacao?, fixado bool, fixado_ate?, inicio, fim?, publico_json{unidades[], regionais[], filtros{uf, modulo_ligado, template...}, perfis[]}, canais[mural|sino|email|whatsapp_interno], status[rascunho|agendado|publicado|expirado|arquivado].
- **aviso_destinatario** (novo): aviso_id, usuario_id, unidade_id?, entregue_em, aberto_em?, confirmado_em?, lembretes_enviados.
- **notificacao** (001+): novo tipo `aviso`.

## Campanhas e segmentos (US8, US19, US20)
- **segmento** (novo): id, marca_id, dono_escopo_tipo, dono_escopo_id, nome, regras_json{interesses, faixa_etaria, cidades, raio, unidades, historico{comprou, sessao, inativo_dias, pacote_restante, nps}}, dinamico bool, ultima_contagem, contado_em. A API devolve só contagens a perfis de unidade.
- **modelo_campanha** (novo): id, marca_id, objetivo[agendar_avaliacao|vender_pacote|reativar|aniversario|lancamento|renovacao|quiz|outro], nome, canais[], conteudos_json por canal, campos_livres[], cta_padrao, arte_url, template_whatsapp_id?, regras_json, escopos_permitidos, aprovacao_obrigatoria bool, versao, ativo.
- **campanha** (novo): id, marca_id, origem[rede|unidade], unidade_id?, criador_id, modelo_campanha_id, objetivo, segmento_id ou segmento_json, alcance_json{ufs, cidades, raio, unidades}, procedimentos[], pacotes[], produtos[], promocao_id?, canais[], conteudo_json, cta_url, utm_json, inicio, fim, disparo[unico|agendado|recorrente], gatilho?[aniversario|inativo|pacote_acabando|pos_sessao], agendado_para?, previa_json{elegiveis_por_canal, excluidos{consentimento, frequencia, conflito, teto}, custo_estimado}, status[rascunho|aguardando|aprovada|reprovada|agendada|enviando|no_ar|pausada|encerrada], aprovacao_id? → aprovacao (001), replicada_de_id?, passo_assistente.
- **campanha_envio** (novo): id, campanha_id, cliente_id, canal, status[programado|descartado_frequencia|descartado_consentimento|enviado|entregue|falhou|aberto|clicado|opt_out], motivo_descartado?, id_provedor, ts por status. Base das métricas; retenção curta para a linha nominal, agregados permanentes.
- **cartao_area_cliente** (novo): campanha_id ou promocao_id, cliente_id?, segmento_id?, inicio, fim, exibicoes, cliques (vitrine "Ofertas para você" e "Perto de você").
- **regra_frequencia** (novo): marca_id, max_semana, max_mes, prioridade_ordem[rede, unidade_preferida, proxima], janela.
- **atribuicao_conversao** (novo): id, campanha_id, cliente_hash, tipo[cadastro|agendamento|comparecimento|venda], ref_id, valor_centavos?, modelo[ultimo_clique_7d|ultimo_clique_30d], ts.
- **metrica_campanha_dia** (novo, agregada): campanha_id, unidade_id, canal, dia, enviados, entregues, aberturas, cliques, cadastros, agendamentos, comparecimentos, vendas, valor_vendas, custo.
- **replicacao** (novo): id, campanha_origem_id, autor_id, destinos_json, modo[publicar|propor], resultados_json{unidade_id: campanha_id|erro}, ts.

## Agendamento
- **agendamento** (novo; a fonte da verdade é a DocBiz): id, marca_id, unidade_id, cliente_id, dependente_id?, procedimento_id, tipo[avaliacao|sessao|retorno], pacote_id?, inicio, fim, profissional_ref?, sala_ref?, status[reservado_temporario|solicitado|confirmado|remarcado|cancelado_cliente|cancelado_unidade|compareceu|faltou], id_docbiz?, origem[site|app|unidade|call_center|campanha], campanha_id?, remarcacoes, cancelado_motivo?, lead_id?, sincronizado_em.
- **politica_agenda** (novo): escopo_tipo, escopo_id, antecedencia_min_h, remarcar_ate_h, max_remarcacoes, cancelar_ate_h, no_show_regras_json, sinal_exigido_apos_faltas?.
- **lembrete** (novo): agendamento_id, canal, quando, status, resposta[confirmou|remarcar|cancelar]?.
- **lista_espera** (novo, fase 2): cliente_id, unidade_id, procedimento_id, faixas_json, criado_em, avisado_em?.

## Pedidos, pagamentos, pacotes e sessões
- **pedido** (novo): id, marca_id, unidade_vendedora_id, cliente_id, itens[] (pedido_item), subtotal, desconto, total, promocao_id?, campanha_id?, regulamento_texto_legal_id, status[aguardando_pagamento|pago|cancelado|estornado|parcial_estornado|expirado], arrependimento_ate, canal[site|app|unidade], criado_em.
- **pedido_item** (novo): pedido_id, tipo[pacote|sessao_avulsa|produto|vale], ref_id, qtd, preco_unit.
- **pagamento** (novo): id, pedido_id, gateway, metodo[pix|cartao|carteira], parcelas, valor, status[pendente|autorizado|pago|recusado|estornado|chargeback], id_gateway, split_json{unidade, rede}, pago_em, webhook_recebido_em.
- **conta_recebimento** (novo): unidade_id, gateway, subconta_id, kyc_status, ativo. (Dados bancários ficam no gateway, não na plataforma.)
- **documento_fiscal** (novo): pedido_id, tipo[recibo|nfse], numero, emissor_cnpj, url_pdf, status, emitido_em.
- **estorno** (novo): pagamento_id, valor, motivo[arrependimento|cancelamento|chargeback|outro], status, ts.
- **pacote** (novo): id, cliente_id, unidade_id, pedido_id? (nulo se vendido na DocBiz), modelo_pacote_id, procedimento_id, area?, sessoes_contratadas, sessoes_realizadas, sessoes_agendadas, validade_ate, status[ativo|concluido|expirado|cancelado|transferido], id_docbiz?, sincronizado_em.
- **sessao** (novo): id, pacote_id, agendamento_id?, numero, status[prevista|agendada|realizada|faltou|cancelada], realizada_em?, unidade_id, profissional_ref?, id_docbiz?.
- **transferencia_pacote** (novo, fase 2): pacote_id, de_unidade_id, para_unidade_id, aceite_origem, aceite_destino, regra_financeira, status.

## Relacionamento
- **avaliacao** (novo): id, cliente_id, unidade_id, agendamento_id ou sessao_id, nota_nps 0 a 10, comentario?, convidado_google_em, clicou_google bool, caso_recuperacao_id? → ticket (001), ts. Sem incentivo e sem filtro por nota no convite ao Google.
- **notificacao_cliente** (novo): id, cliente_id, tipo[transacional|relacionamento|marketing], template_id, canal[area|email|whatsapp|sms|push], status, lida_em?, campanha_id?, ref_entidade.
- **template_mensagem** (novo): id, marca_id, chave, canal, categoria_meta?[marketing|utility|authentication], corpo, variaveis[], aprovado_meta_em?, versao.
- **dispositivo_push** (novo, app): cliente_id, plataforma, token, ativo.
- **ticket** (001+): `origem` ganha `cliente`; `cliente_id?`; canal[area|whatsapp|email].
- **artigo** (001+): `publico` já tem `cliente`; usado na ajuda da área do cliente.

## Relações principais
```
marca 1..N unidade (001)
marca 1..N cliente 1..N cliente_vinculo_unidade N..1 unidade
cliente 1..N consentimento N..1 texto_legal
cliente 1..N interesse_cliente N..1 procedimento|categoria_interesse
procedimento 1..N oferta_unidade N..1 unidade
procedimento 1..N modelo_pacote 1..N pacote_unidade N..1 unidade
cliente 1..N agendamento N..1 unidade ; agendamento 0..1 sessao
cliente 1..N pedido 1..N pedido_item ; pedido 1..N pagamento ; pedido 1..N documento_fiscal
cliente 1..N pacote 1..N sessao
modelo_campanha 1..N campanha 1..N campanha_envio N..1 cliente
campanha N..1 segmento ; campanha 0..1 promocao ; campanha 0..1 aprovacao (001)
liberacao / limite_envio por escopo (rede, regional (001), unidade)
aviso 1..N aviso_destinatario N..1 usuario (001)
lead (001) 0..1 cliente
```

## Novos módulos no RBAC (para `perfil_permissao.modulo` da 001)
`clientes`, `ofertas_precos`, `promocoes`, `campanhas_clientes`, `avisos`, `controles_rede`, `vendas_pacotes`, `nps`, `financeiro_cliente`, `performance`. As ações V, E, A, P, X, D seguem a 001; o que a unidade efetivamente pode fazer é a interseção de RBAC x `liberacao` x `limite_envio`.

## Recursos principais da API (rascunho)
- Cliente: `POST /v1/auth/otp`, `POST /v1/auth/verify`, `GET/PATCH /v1/me`, `GET/PUT /v1/me/consentimentos`, `GET/PUT /v1/me/interesses`, `POST /v1/me/privacidade/pedidos`, `GET /v1/me/agendamentos`, `POST /v1/agendamentos`, `GET /v1/unidades/{id}/disponibilidade`, `GET /v1/me/pacotes`, `POST /v1/pedidos`, `POST /v1/pedidos/{id}/pagamentos`, `GET /v1/me/ofertas`, `POST /v1/avaliacoes`, `GET /v1/me/notificacoes`.
- Interno: `/v1/admin/clientes`, `/segmentos/{id}/contagem`, `/campanhas` (+ `/previa`, `/enviar-aprovacao`, `/replicar`), `/modelos-campanha`, `/avisos` (+ `/relatorio-leitura`), `/controles/liberacoes`, `/controles/limites`, `/performance/*`, `/ofertas`, `/promocoes`, `/financeiro/repasses`.
- Webhooks de entrada: `/v1/webhooks/docbiz`, `/gateway`, `/whatsapp`, `/email`.
