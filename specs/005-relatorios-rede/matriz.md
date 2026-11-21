# Matriz: fonte x métrica x spec de origem x status

**Spec**: `005-relatorios-rede` · **Data**: 21/11/2026

Situação: **Já capturado** = a plataforma (specs 001 a 004) já gera o dado; **Integração** = depende de API externa ou da DocBiz; **Depende da Salus** = número que só a Salus tem (metas, orçamento, vendas, custos); **Fase 2** = entra com a fase 2 da área do cliente. Avaliações aparecem como Integração porque dependem do acesso às Business Profile APIs (spec 004), embora o modelo de dados já exista.

| Fonte | Métrica | Spec de origem | Tela no hub | Situação |
|---|---|---|---|---|
| Plataforma: leads | Leads por dia, unidade, UF, regional | 001 (lead, US4/US5) | 13, 91, 96 | Já capturado |
| Plataforma: leads | Origem do lead (UTM, gclid, fbclid, ctwa_clid) e fonte agrupada | 001 (origem_json), 003 (evento_bruto) | 13, 90, 91 | Já capturado |
| Plataforma: leads | Ponto de entrada: formulário, quiz, WhatsApp, telefone rastreado | 001, 003 (link_rastreado) | 91, 93 | Já capturado |
| Plataforma: leads | Procedimento de interesse | 001 (lead), 003 (resposta_quiz) | 91, 93 | Já capturado |
| Plataforma: leads | Status no funil (novo, contato, agendado, perdido) e taxa de contato | 001 (lead.status, fila) | 13, 91 | Já capturado |
| Plataforma: leads | Tempo do 1º contato, SLA cumprido, faixas de tempo x agendamento | 001 (primeiro_contato_em, SLA) | 92 | Já capturado |
| Plataforma: leads | Dia e hora de chegada (mapa de calor) | 001 (lead.criado_em) | 92 | Já capturado |
| Plataforma: leads | Quem atendeu: unidade ou call center | 001 (fila, responsável) | 92 | Já capturado |
| Plataforma: leads | Motivo de perda | 001 (campo novo, obrigatório ao perder) | 91 | Já capturado |
| Plataforma: leads | Lead que já é cliente | 001 + 002 (cliente) | 91 | Já capturado |
| Plataforma: unidades | Unidades ativas, regional, UF, cidade, marca, plano | 001 (unidade, RBAC) | filtros, 96 | Já capturado |
| Plataforma: unidades | Completude da ficha | 001 (completude) | 94, 96 | Já capturado |
| Plataforma: unidades | Índice de conversão, ranking, quartil, mediana | 001 (dashboard 04) + 005 | 13, 96, 97 | Já capturado |
| Plataforma: landings | Visitas por página de unidade, formulário iniciado e enviado | 003 (evento_bruto, dicionário v3) | 93 | Já capturado |
| Plataforma: landings | Desempenho por modelo e variante (A/B/C) | 001 (landing, variante) | 93 | Já capturado |
| Plataforma: landings | Aparelho e canal da visita | 003 (evento_bruto) | 93 | Já capturado |
| Plataforma: tracking | Eventos inválidos, UTM inválida, divergência com GA4 | 003 (evento_invalido, alerta_tracking) | 93, 98 | Já capturado |
| Plataforma: quiz | Quizzes começados e concluídos, conta salva, lead e agendamento | 003 (resposta_quiz, agg_quiz_dia) | 93 | Já capturado |
| Plataforma: quiz | Procedimento recomendado (demanda) | 003 (agg_quiz_dia) | 93 | Já capturado |
| Plataforma: área do cliente | Contas, contas novas, ativos em 30 dias | 002 (cliente) | 95 | Já capturado |
| Plataforma: área do cliente | Consentimentos por canal (e-mail, WhatsApp, push) | 002 (consentimento) | 95 | Já capturado |
| Plataforma: área do cliente | Exibições e cliques das ofertas | 002 (cartao_area_cliente, oferta_unidade) | 95 | Já capturado |
| Plataforma: área do cliente | Agendamentos, remarcações e cancelamentos feitos pelo cliente | 002 (agendamento) | 92, 95 | Já capturado |
| Plataforma: área do cliente | NPS pós-sessão e convites ao Google | 002 (avaliacao) | 95 | Já capturado |
| Plataforma: área do cliente | Campanhas para clientes: enviadas, cliques, agendamentos, comparecimentos | 002 (campanha_envio, atribuicao_conversao, metrica_campanha_dia) | 90, 95 | Já capturado |
| Plataforma: área do cliente | Mural: confirmação de leitura | 002 (aviso_destinatario) | 95 | Já capturado |
| Plataforma: área do cliente | Cota de campanhas por unidade | 002 (consumo_cota) | 95 | Já capturado |
| Plataforma: área do cliente | Pedidos e vendas online | 002 (pedido, pagamento) | 95 | Fase 2 |
| Plataforma: avaliações | Nota média, volume, respondidas, tempo de resposta, pendentes, escaladas, temas | 004 (avaliacao, avaliacao_resposta, avaliacao_escalada) | 94, 97 (link 84) | Integração |
| Plataforma: relatórios | Relatórios salvos e envios agendados | 001 (relatorio_salvo, US8) | 99 | Já capturado |
| Plataforma: relatórios | Regras de alerta e insights | 001 (regra_insight, US15) | 13, 98 | Já capturado |
| Plataforma: auditoria | Registro de exportação com dado pessoal | 001 (auditoria, US21) | 99 | Já capturado |
| DocBiz (agenda) | Agendamentos confirmados (fonte da verdade) | 002 (agendamento) | 13, 90, 91, 92 | Integração |
| DocBiz (agenda) | Comparecimento, faltas, lembrete confirmado | 002 (agendamento, lembrete) | 13, 91, 92 | Integração |
| DocBiz (pacotes) | Pacotes ativos, sessões realizadas, pacotes acabando | 002 (pacote, sessao) | 95 | Integração |
| DocBiz (vendas) | Vendas de pacote e receita por unidade e por lead | 002 (pedido, D3) | 13, 90, 91, 97 | Depende da Salus |
| DocBiz (vendas) | Ticket médio | 002 | 13 | Depende da Salus |
| Google Ads API | Investimento, impressões, cliques, CTR por campanha e geografia | 005 (nova integração) | 13, 90 | Integração |
| Google Ads API | Conversões offline (agendou, compareceu, comprou) devolvidas com gclid | 005 + 003 (coletor) | 90 | Integração |
| Meta Marketing API | Investimento, impressões, cliques, ações por campanha | 005 (nova integração) | 13, 90 | Integração |
| Meta Conversions API | Lead de clique para WhatsApp (ctwa_clid) e retorno do resultado | 003 + 005 | 90, 91 | Integração |
| GA4 Data API | Sessões, origem e mídia (conferência do coletor) | 003 (fonte_externa) | 93 | Integração |
| Business Profile Performance API | Aparições em busca e Maps, ligações, rotas, cliques no site, mensagens | 003 (gbp_metrica_dia) | 94, 97 | Integração |
| Search Console API | Cliques, impressões, CTR, posição, consultas | 003 (fonte_externa search_console) | 94 | Integração |
| Salus (cadastro) | Metas mensais por rede, regional e unidade | 005 (meta, nova) | 13, 98 | Depende da Salus |
| Salus (cadastro) | Orçamento de mídia por campanha e período | 005 | 90, 98 | Depende da Salus |
| Salus (cadastro) | Custo do envio de WhatsApp (tarifa contratada) | 002 | 90 | Depende da Salus |
| Salus (cadastro) | Custo de mídia local da unidade | 001 (política de tags, tela 57) | 97 | Depende da Salus |
| Cálculo 005 | Custo por lead, por agendamento, por comparecimento, ROAS | 005 (sobre Ads, Meta e DocBiz) | 13, 90 | Integração |
| Cálculo 005 | Previsão do mês e faixa provável | 005 | 13, 98 | Já capturado |
| Cálculo 005 | Anomalia (fora da faixa prevista) | 005 (regra_insight tipo novo) | 98 | Já capturado |
| Cálculo 005 | Sazonalidade: mesmo mês do ano anterior | 005 (histórico da plataforma) | 13 | Já capturado |
| Fontes externas | IBGE, INMET, tendências de busca | 003 (fonte_externa) | link 67 | Já capturado |
| Pesquisa de mercado | Benchmarks (WordStream, Pronk, HBR, BrightLocal) | 005 (pesquisa.md) | 90, 92, 94 | Já capturado |

Total: 54 métricas. Já capturado: 35. Integração: 12. Depende da Salus: 6. Fase 2: 1.

## Telas do hub

| Tela | Seção | Arquivo |
|---|---|---|
| 13 | Visão executiva (hub) | `13-admin-relatorios` |
| 90 | Aquisição e campanhas | `90-admin-relatorios-campanhas` |
| 91 | Leads e funil | `91-admin-relatorios-leads-funil` |
| 92 | Atendimento do franqueado | `92-admin-relatorios-atendimento` |
| 93 | Quiz, landings e tráfego | `93-admin-relatorios-quiz-landings` |
| 94 | SEO local, Google e avaliações (liga à 84) | `94-admin-relatorios-seo-avaliacoes` |
| 95 | Área do cliente, ofertas, agendamentos e pacotes | `95-admin-relatorios-area-cliente` |
| 96 | Unidades e regiões | `96-admin-relatorios-unidades` |
| 97 | Relatório da unidade | `97-admin-relatorios-unidade` |
| 98 | Metas, previsão e alertas | `98-admin-relatorios-metas-alertas` |
| 99 | Exportar e agendar envio | `99-admin-relatorios-exportar` |
