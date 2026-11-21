# Resumo: quiz, inteligência e tracking limpo (spec 003)

21/11/2026. Uma página para o Osmar. Detalhes e fontes em `spec.md`, `pesquisa.md`, `decisoes.md`, `data-model.md`, `telas.md` e `impacto-na-001-002.md`.

## Quiz
Gerador visual para a rede (e para a unidade, se a rede liberar, a partir de modelos e com aprovação). Perguntas com ramificação, recomendação de 1 a 3 procedimentos no fim e CTAs para agendar ou ver ofertas. Distribuído como campanha da 002, na landing, na área do cliente, por link e por QR na recepção. Responder não exige conta; salvar o resultado e receber ofertas sim, com consentimento de personalização desmarcado. Perguntas de saúde bloqueadas na fase 1. As respostas viram perfil de interesse e barreiras (preço, dor, tempo), que perdem peso com o tempo.

## Inteligência
Cruzar o que o cliente diz (quiz), o que ele faz (catálogo, agendamentos, compras) e o contexto (clima, calendário, demografia, buscas). Fontes gratuitas confirmadas: IBGE (municípios, idade do Censo 2022, PIB, população), INMET (clima observado e normais de 30 anos), feriados nacionais, Google Trends (exportação manual; API ainda em alpha), Search Console e métricas do Google Business Profile da unidade (com acesso concedido por ela). Open-Meteo é grátis só para uso não comercial, e o Places API (concorrência) é pago. Resultado: painéis de demanda, sazonalidade e potencial por cidade, e recomendações automáticas explicadas que abrem a campanha pronta ou o "replicar". A hipótese de que depilação sobe no inverno precisa ser medida antes de virar regra.

## Tracking limpo
1. **Dicionário de eventos versionado** como fonte única (`objeto_acao` em pt-BR, propriedades obrigatórias, dono, changelog, QA).
2. **Um loader e um banner por marca** (guia da ANPD + Consent Mode v2), sem script livre de unidade.
3. **Coletor próprio no nosso domínio**: valida, deduplica por `event_id`, grava no nosso banco e distribui pelo servidor ao GA4 da rede e da unidade, Meta, Google Ads (Data Manager API, conversões offline da DocBiz) e TikTok.
4. **UTMs** por gerador com listas fechadas.
5. **Identidade** anônimo > cliente por marca, sem ligar Gio e Sorridents.
6. **Alertas** de quebra, PII e UTMs inválidas.

Custos coletados: GTM server-side no Cloud Run, cerca de R$ 530,00 por mês (2 servidores); Stape, de R$ 0 a R$ 117,78; Zaraz, 1 milhão de eventos grátis; coletor próprio, dentro do stack já orçado. BigQuery e R2 cabem nas faixas grátis no volume atual.

## Gerenciador de tags da unidade
Campos tipados e validados (GA4, Search Console, Google Ads, Meta, TikTok), cadeado pela política de campos e aprovação da rede. A Google tag aceita vários destinos sem segundo script, mas só page_view e medição aprimorada vão para todos; conversões saem pelo servidor. O GA4 padrão não permite acesso por unidade dentro de uma propriedade, porque subpropriedades só existem no 360. Por isso a unidade vê os números no nosso painel e pode ter um GA4 próprio. No Search Console, a rede cria o prefixo `/unidade/<slug>/`, que é verificado sozinho, e dá acesso à unidade; a meta tag fica para o domínio próprio. O guia em texto na Wiki e em vídeo entra como entregável futuro, antes de abrir as tags às unidades.

## Decisões para o Osmar
1. Arquitetura: coletor próprio + server-side (recomendado) ou sGTM ou Stape (D5).
2. GA4: uma propriedade por marca com unidade como dimensão, e GA4 da unidade opcional (D7, D16).
3. Quiz anônimo, só perguntas de estética na fase 1, unidade só por modelo (D1 a D3).
4. Dono do tracking na Gio (D15).
5. Fontes pagas: Open-Meteo comercial e Places API ficam desligadas até haver verba (D10, D11).
6. Retenção de eventos (D13).
