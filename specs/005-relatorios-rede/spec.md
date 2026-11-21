# Feature Specification: Hub de relatórios da rede

**Feature Branch**: `005-relatorios-rede`
**Created**: 2026-11-21
**Status**: Draft (rev. 2, 21/11/2026, 18h: crítica de design `critica-relatorios.md` aplicada; decisão do Osmar das 17h41 registrada. Rev. 1: proposta e protótipo das telas 13 e 90 a 99)
**Depende de**: `001-sistema-unidades` (lead, unidade, RBAC, dashboards US5, relatórios agendáveis US8, relatórios inteligentes US15, auditoria US21), `002-area-cliente` (cliente, agendamento, pacote, campanhas, NPS), `003-quiz-inteligencia-tracking` (coletor, quiz, fontes externas, GBP e Search Console), `004-avaliacoes-google` (avaliações, tela 84)
**Input**: Osmar, 21/11/2026: "Não dá pra filtrar por unidade, nem tem dados das campanhas feitas. Faça uma pesquisa completa de melhoria... os executivos da empresa gostam muito de gráficos e números, fontes e etc." e (17h10) "a tela 13 deve ser o hub de relatórios da rede que agrega todas as fontes".
**Arquivos**: `pesquisa.md` (pesquisa com fontes), `matriz.md` (fonte x métrica x spec x situação).

## Contexto
- A tela 13 antiga tinha só um período, funil, origem e uma métrica por UF. Não filtrava por unidade, cidade ou campanha e não mostrava investimento, custo por etapa nem retorno.
- As specs 001 a 004 já geram quase todos os dados de que a rede precisa (35 das 54 métricas da matriz). O que falta é juntá-los num lugar, com o mesmo filtro, e trazer custos de mídia, vendas e metas.

## Papéis e escopo
| Papel | O que vê no hub |
|---|---|
| Rede (R-ADM, R-MKT, diretoria) | Tudo, todas as unidades, exportação e agendamento |
| Regional (R-REG) | Só as unidades da regional, com a mediana da rede como referência |
| Rede (R-FIN, R-AG) | Agregados e custos; nunca nome, telefone ou e-mail de lead |
| Franqueado (U-FRQ, U-GER) | Só a própria unidade (tela 97), com posição no ranking e mediana da rede, sem nomes nem números de outras unidades (001, US5) |
| Agência de mídia (convidada) | Só as seções de campanhas e o CSV de campanhas, se a rede liberar |

## Histórias de usuário

### US1. Filtro global (P1)
Uma barra de filtros vale para todos os blocos de todas as seções: período (atalhos e datas), comparação (período anterior, mesmo período do ano anterior, sem comparação), marca, regional, estado, cidade, unidade (busca, várias de uma vez), fonte, campanha e procedimento. O filtro fica na URL, pode ser salvo como visão e acompanha a navegação entre abas.
**Acceptance**: 1. Given unidade "Alto da Lapa" escolhida, When troco de aba, Then todos os blocos mostram só a unidade. 2. Given comparação "ano anterior", Then todas as variações usam o mesmo intervalo do ano anterior.

### US2. Visão executiva (P1) · tela 13
10 indicadores com variação e minigráfico (leads, agendados, comparecimentos, vendas, investimento, CPL, custo por agendamento, ROAS, 1º contato, nota no Google), série diária contra o período anterior, funil completo com referência de mercado, fontes, mapa por estado, ranking com quartis, campanhas com mais leads, alertas, metas do mês e sazonalidade com previsão.

### US3. Aquisição e campanhas (P1) · tela 90
Google Ads e Meta Ads lado a lado; tabela de campanhas com investimento, impressões, cliques, CTR, leads, CPL, agendamentos, custo por agendamento, comparecimentos, vendas, receita e ROAS, ordenável e exportável; dispersão CPL x taxa de agendamento; campanhas para clientes (002); ritmo do orçamento.
Atribuição padrão: último clique em 30 dias, com gclid, fbclid e ctwa_clid guardados no lead (003). Agendamento, comparecimento e venda voltam às plataformas como conversão offline.

### US4. Leads e funil (P1) · tela 91
Funil das 10 fontes até a venda, conversão por grupo de fonte, ponto de entrada, procedimentos, tempo até agendar e motivos de perda (campo novo obrigatório ao marcar lead como perdido).

### US5. Atendimento do franqueado (P1) · tela 92
1º contato (mediana, até 5 min, SLA), faixas de tempo x agendamento (com a referência da HBR), mapa de calor de dia e hora, unidades mais lentas, comparecimento, faltas e efeito do lembrete, unidade x call center.

### US6. Quiz, landings e tráfego (P1) · tela 93
Funil das páginas das unidades, funil do quiz e demanda por procedimento, modelos e variantes, aparelho e canal, saúde do rastreamento (liga à 70).

### US7. SEO local, Google e avaliações (P1) · tela 94
Perfil do Google (Business Profile Performance API), Search Console, avaliações (resumo da spec 004, liga à 84) com as estatísticas da BrightLocal como régua, SEO por estado.

### US8. Área do cliente (P2) · tela 95
Contas, consentimentos, ofertas, agendamentos online, pacotes, NPS e convites ao Google, mural e campanhas. Vendas online entram com a fase 2.

### US9. Unidades e regiões (P1) · telas 96 e 97
Tabela por regional, mapa por estado com troca de métrica (leads por unidade, % que agenda, 1º contato), quartis ("o que separa Q1 de Q4"), dispersão volume x conversão, tabela das 130 unidades com busca, filtros por regional e quartil, ordenação e CSV. A tela 97 é o relatório de uma unidade comparado à mediana da rede, com próximos passos sugeridos. Cada unidade tem endereço próprio (`97-admin-relatorios-unidade.html?unidade=<slug>`); todo nome de unidade no hub (13, 92, mapa, dispersão e as 130 linhas da 96) abre a 97 daquela unidade. Na visão da rede, "Trocar unidade" abre a busca das 130 e "Voltar para Unidades e regiões" leva à 96; slug inexistente mostra "Unidade não encontrada". Na 96, a tabela tem cabeçalho preso, 25 unidades por página (10 no celular), cartões abaixo de 640 px, estado vazio e filtro por estado e regional guardado na URL.

### US9a. Relatório da minha unidade (franqueado) (P1) · tela 97-franqueado
Decisão do Osmar (21/11, 17h41): o franqueado vê só a própria unidade. Mesma página da 97 no casco do franqueado (menu Apoio > Relatórios), sem abas da rede, sem "Trocar unidade" e ignorando qualquer `?unidade=` do endereço; mostra a posição no ranking e a mediana da rede, sem nomes nem números de outras unidades.

### US10. Metas, previsão e alertas (P1) · telas 98 e 89
Metas mensais por rede, regional e unidade (cadastradas pela Salus); acumulado com faixa de previsão e ritmo da meta; regras de alerta (queda de leads, CPL, 1º contato, comparecimento, projeção abaixo da meta, avaliação ruim sem resposta, UTM inválida) e detecção de anomalia por série temporal; alertas abertos. A tela 89 cadastra as metas (rede, regional, exceção por unidade, inclusive 90% das avaliações respondidas em 48 h, 100% das notas 1 e 2 em 24 h e 1º contato de 15 min) e as regras de alerta (limite, frequência, quem recebe, liga/desliga), com contagem de alterações pendentes, descartar e salvar.

### US11. Exportar e agendar envio (P1) · tela 99
PDF executivo e CSV de qualquer seção com os filtros atuais; envio agendado por e-mail (frequência, horário, destinatários com acesso à plataforma, seções). Envio agendado só com números agregados. Exportação com dado pessoal exige permissão, é registrada na auditoria e não pode ser agendada. Agendar passa por revisão e confirmação (resumo com seções, recorte, formato, frequência, horário e número de destinatários); a lista de envios permite pausar, retomar, enviar agora e excluir com confirmação.

### US12. Fonte e situação em cada bloco (P1)
Todo bloco mostra a fonte, a hora da última atualização e o selo da situação do dado (Do sistema, Integração, Depende da Salus, Fase 2), conforme a matriz.

## Requisitos funcionais
- **FR-001** Filtro global persistente na URL e em visões salvas (`relatorio_salvo`).
- **FR-002** Mesmas definições de métrica no hub, no painel da unidade (04) e na exportação.
- **FR-003** Tabela diária agregada por unidade x fonte x campanha x procedimento para resposta rápida (alvo: menos de 2 s para 90 dias).
- **FR-004** Conectores: Google Ads API, Meta Marketing API, Meta Conversions API, GA4 Data API, Business Profile Performance API, Search Console API (detalhes em `pesquisa.md`), com hora da última leitura por fonte.
- **FR-005** Conversões offline: devolver agendamento, comparecimento e venda ao Google Ads (Data Manager API) e ao Meta (Conversions API).
- **FR-006** Cadastro de metas e orçamento (rede, regional, unidade, mês) pela Salus.
- **FR-007** Rateio de campanhas regionais por unidade pela participação nos leads da campanha.
- **FR-008** Novos tipos em `regra_insight`: anomalia (faixa prevista), projeção x meta, CPL da campanha.
- **FR-009** Escopo por perfil igual ao RBAC da 001; o franqueado nunca vê nome ou número de outra unidade.
- **FR-010** Exportações registradas na auditoria (001, US21).

- **FR-011** Nomenclatura única entre 13 e 90: "Receita de pacotes" = vendas de todas as fontes; "Receita atribuída à mídia" = só vendas cujo lead veio de anúncio (último clique em 30 dias); "ROAS da mídia" = receita atribuída à mídia ÷ investimento em mídia. A 13 explica as duas receitas abaixo dos indicadores.
- **FR-012** Comparecimento com um só denominador em todas as telas: compareceram ÷ agendamentos já realizados (compareceram + faltas + cancelamentos); agendamentos futuros ficam fora. Rede: 72%. O rótulo ou a ajuda de cada bloco diz o denominador.
- **FR-013** Estados obrigatórios em cada bloco: vazio (recorte sem dados, com "Limpar filtros"), API atrasada (aviso com a hora da última leitura e o atraso típico) e visão por papel (rede ou franqueado).

## Critérios de sucesso
- Diretoria responde "quanto investimos, quantos leads, quantos agendaram, quanto vendeu e qual campanha dá retorno" em uma tela, sem planilha.
- 100% dos blocos com fonte e hora.
- Relatório semanal enviado toda segunda às 8h sem intervenção.

## Decisões tomadas
- **Franqueado** (Osmar, 21/11, 17h41): vê só a própria unidade (tela 97-franqueado). Fecha a antiga decisão 9.
- **Apresentação** (Osmar, 21/11, 17h41): o resto fica mockado no protótipo para facilitar a apresentação (filtros na URL sem mudar os números, estados vazios e de API atrasada, cadastro de metas e regras, gestão de envios).

## A definir se o projeto for aprovado
Decisão do Osmar (21/11, 17h41): os itens abaixo ficam registrados e só serão decididos se o projeto for aprovado.
1. **Modelo de atribuição**: último clique em 30 dias (proposta) ou outro (primeiro clique, linear)?
2. **Integrações de mídia**: aprovar Google Ads API e Meta Marketing API; quem dá o acesso (MCC e Business Manager da Salus ou da agência)?
3. **GA4, Search Console e Business Profile Performance**: aprovar as três leituras; o acesso ao Business Profile é o mesmo pedido da spec 004.
4. **Dados da Salus**: metas mensais (por rede, regional e unidade), orçamento por campanha, ticket médio e vendas da DocBiz por paciente (liga à D3 da 002). Sem vendas, o hub para em comparecimento e o ROAS fica de fora.
5. **Conversões offline**: devolver agendamento, comparecimento e venda às plataformas? Exige base legal e texto de consentimento revisado (002).
6. **Motivo de perda obrigatório** ao marcar lead como perdido.
7. **Call center noturno e aos sábados**: o mapa de calor mostra que 21% dos leads chegam entre 19h e 22h (número fictício do protótipo); vale levar à Salus.
8. **Destinatários do envio agendado** e frequência (proposta: diretoria e marketing toda segunda às 8h).
9. ~~Franqueado no hub~~: decidido (só a própria unidade, tela 97-franqueado).
10. **Agência como usuária** com acesso só a campanhas?
11. **Custo de envio de WhatsApp** entra no custo das campanhas para clientes?

## Fora de escopo agora
- Dados financeiros completos da unidade (DRE, margem): só se a Salus decidir compartilhar.
- Modelos de atribuição baseados em dados (data-driven) e MMM.
