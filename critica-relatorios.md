# Crítica de design: Hub de relatórios da rede (Gio)

Cliente: Gio Estética Avançada (Salus), rede de 130 clínicas franqueadas. Dados fictícios de demonstração.
Pedido: Osmar, via Stark. Público: executivos da Salus, que gostam de gráficos, números e fontes. A tela 13 redesenhada é o hub; as subtelas 90 a 99 detalham campanhas, leads e funil, atendimento, quiz e landings, SEO e avaliações, área do cliente, unidades e regiões, relatório da unidade, metas e alertas, e exportação.
Fonte: 22 PNGs em `revisao-layout/relatorios/` (desktop 1440 CSS px por alturas de 1.757 a 11.151; celular 390 CSS px por alturas de 3.332 a 25.056; captura 1x, sem conversão de escala), HTML em `telas/13-admin-relatorios.html` e `90-*` a `99-*`, tokens em `telas/estilo.css`, spec 005 (`spec.md`, `matriz.md`, `pesquisa.md`). Consistência com `critica-design.md`, `critica-tela-52.md` e `critica-avaliacoes.md` (consultadas, não alteradas). Nenhum arquivo existente foi modificado.
Data da crítica: 21 de novembro de 2026, America/Sao_Paulo.
Método: sete passes por tela (hierarquia, espaçamento, tipografia, cor, interação e estados, texto, acessibilidade), mais acionabilidade, fontes e situação do dado, e celular. Contraste WCAG calculado pela luminância relativa a partir dos tokens do CSS e, quando necessário, de pixels amostrados no PNG. Tamanhos de tipo lidos no CSS e no HTML (medido). Valores rotulados como medido, estimado ou proposto. Severidade só assume "bloqueio", "vale corrigir" ou "detalhe".
A faixa escura "Ambiente de demonstração · dados fictícios" e o trocador Rede / Franqueado / Cliente / Telas no topo dos prints pertencem ao cromo da galeria, não ao produto (mesmo critério da crítica da tela 52). O selo de demonstração do produto é o pill âmbar no cabeçalho administrativo e o rodapé `.demo-rod`.

## 1. Veredito geral

O hub já parece um produto de inteligência da rede, não um relatório improvisado. A identidade (Poppins e Inter, roxo, vinho e magenta), o casco do admin (lateral fixa de 252 px, conteúdo em largura total) e os tokens de contraste recalibrados estão no nível certo para uma apresentação. Quase todo bloco traz fonte, hora (horário de Brasília) e selo de situação, como pedia a US12. As somas internas fecham com disciplina: 2.986 leads, 1.643 de mídia, 1.733 agendados, R$ 62.643 investidos, 10 fontes, 4 pontos de entrada e 130 unidades. O mapa passou a usar malha de UFs do IBGE, o que resolve o bloqueio do polígono desenhado à mão. As barras substituem pizza, há referência de mercado com fonte citada, e a tela 99 trata dado pessoal no envio agendado com a clareza que a LGPD pede. Nas telas de leads, atendimento e área do cliente não aparece nome, telefone, e-mail ou CPF de pessoa.

O que ainda tira o efeito de "página mais útil para executivos" não é falta de gráfico. É a primeira tela da 13, que gasta a dobra com abas, dez filtros e uma legenda longa, enquanto alertas, metas e a nota no Google ficam duas ou três dobras abaixo. É a acionabilidade: os dez KPIs são `div`, o mapa só tem `title` ao passar o mouse, e os 130 links de unidade (mais o ranking e as unidades lentas) apontam todos para `97-admin-relatorios-unidade.html` sem identificar a unidade, de modo que Batel, Paulínia e Montes Claros abrem o relatório do Alto da Lapa. E é a confiança nos números: a 13 rotula "Receita atribuída" com R$ 733 mil (ticket vezes 621 vendas) ao lado de um ROAS 5,8x que, na 90, usa R$ 365 mil; o comparecimento aparece como 72% dos já realizados no hub e como 62% de todos os agendados na 96 e na 97, o que muda se o Alto da Lapa (65%) está acima ou abaixo da rede.

Corrigindo destinos, definições que não fecham e a ordem da primeira tela, o conjunto fica pronto para impressionar diretoria. O conteúdo, os gráficos e a transparência das fontes já estão no caminho certo.

## 2. Correções do conjunto (ordem de impacto)

1. **Destino do relatório da unidade.** Severidade: bloqueio. Evidência medida: os 11 links de unidade da 13, os 8 da 92 e os 130 da 96 têm `href="97-admin-relatorios-unidade.html"` sem query string. A 97 é sempre "GiO Alto da Lapa, 4º de 130". O botão "Trocar unidade" (medido no HTML) só navega de volta à 96, não troca o relatório na própria página. É o mesmo tipo de falha da crítica das avaliações, em que o cartão abria a resposta da pessoa errada. Correção proposta: `97-admin-relatorios-unidade.html?unidade=<slug>` (ou o id da unidade), com o filtro global também na URL. "Trocar unidade" abre o mesmo seletor com busca já existente no filtro, aplica o slug e atualiza KPIs, funil e próximos passos. No protótipo, pelo menos cinco unidades de quartis diferentes (Batel, Alto da Lapa, uma mediana, Montes Claros, Paulínia) precisam ter página ou estado próprio.

2. **Receita atribuída que não fecha com o ROAS.** Severidade: bloqueio. Evidência medida: na 13, o KPI "Receita atribuída" mostra R$ 733 mil, com subtítulo "ticket médio R$ 1.180 (DocBiz)". 621 × 1.180 = 732.780 (fecha). O KPI ao lado, "ROAS da mídia 5,8x", traz o subtítulo "receita atribuída ÷ investimento". 733.000 ÷ 62.643 ≈ 11,7x, não 5,8x. Na 90, "Receita atribuída" vale R$ 365 mil e 365.000 ÷ 62.643 ≈ 5,83x (fecha com o total da tabela, R$ 364.620). O mesmo nome descreve totais diferentes nas duas telas. Correção proposta: na 13, chamar o cartão de "Receita de pacotes" (R$ 733 mil, 621 vendas) e o ROAS de "ROAS da mídia", com subtítulo "R$ 365 mil atribuídos à mídia ÷ R$ 62.643". Manter "Receita atribuída" só na 90, com o valor da atribuição de último clique em 30 dias. Colocar um "por que esses números não são iguais" de uma linha, visível no primeiro ecrã.

3. **Comparecimento com duas definições.** Severidade: bloqueio. Evidência medida: na 13, 91 e 92 o KPI diz "72% dos agendamentos já realizados" (1.071 de 1.071 + 316 + 96 = 1.483, medido). Na 96, a coluna "Comparecem" da rede é 62% (1.071 ÷ 1.733, medido). Na 97, o funil compara Alto da Lapa "65% dos agendados" com "Rede 62%". A US e o FR-002 pedem a mesma definição no hub, no painel da unidade e na exportação. Com a régua de 72%, o Alto da Lapa (17 de 26, 65%) fica abaixo da rede; com a de 62%, fica acima. Correção proposta: uma definição só, escrita no cartão. Recomendação: "comparecimento = compareceram ÷ (agendados − ainda por vir)", ou seja 72%, e repetir essa conta na 96, na 97 e no PDF. Se a rede quiser também a taxa sobre todos os agendados, que seja um segundo indicador, com outro nome.

4. **Primeiro ecrã da 13 não é executivo.** Severidade: vale corrigir. Evidência medida no PNG 1440 × 4.105 e no CSS: até cerca de 900 px de altura cabem cromo, H1, abas em duas linhas, dez filtros (`.rr-f`, 13 px Inter, `min-height: 44` px), a legenda `.rr-legst` (13 px) e os dez KPIs. A série diária começa depois da dobra. "Alertas e anomalias" e "Metas de novembro" aparecem por volta de y = 2.700 (estimado no recorte). A nota 4,4 só entra no índice "Todas as seções do hub", no rodapé (y ≈ 3.700). A US2 pedia a nota no Google entre os dez indicadores; o protótipo trocou por "Receita atribuída" e deixou a nota no fim. No 390, a primeira tela (844 px) mal mostra quatro KPIs, depois de botões, abas e uma legenda de cinco a seis linhas. Correção proposta: a ordem da seção 3. Recolher filtros num resumo de uma linha ("01 a 21 nov 2026 · vs período anterior · Rede Gio · Filtros") e a legenda num botão "Situação dos dados" com os quatro selos. Incluir nota no Google nos KPIs do topo, com meta (por exemplo 4,5, a régua da BrightLocal já citada na 94).

5. **KPIs, mapa e alertas quase sem destino.** Severidade: vale corrigir. Evidência medida: os dez cartões da 13 são `<div class="card kpi rr-k">`, sem `href`, `role="link"` ou `tabindex`. O mapa tem `aria-label="Mapa do Brasil por UF"` e `<title>` em cada UF (bom para o hover), mas o `path` não leva a 96 com `?uf=SP`. Os alertas da 13 têm destino de seção (Goiás e CPL vão à 90, 1º contato à 92, quiz à 93), porém sem recorte na URL: a 90 abre na rede inteira, não na campanha pausada de Goiás. É o mesmo ponto da crítica da tela 84 (KPI clicável com meta e drill-down com destino real). Correção proposta: cada KPI vira um `a.kpi-a` (o estilo já existe em `estilo.css`, da spec 004) para a subtela certa, levando o filtro atual. Clique em Goiás no alerta ou no mapa abre a 96 (ou a 90) já filtrada. Unidades nomeadas no alerta abrem a 97 daquela unidade.

6. **Filtro global que não atravessa as abas.** Severidade: vale corrigir. Evidência medida no JS compartilhado (6.410 caracteres, idêntico nas 11 páginas): ao aplicar, o rótulo do chip muda e a mensagem avisa que "no protótipo os números continuam os da rede". Não há `URLSearchParams`, `pushState` nem query nos `href` das abas. "Salvar visão" só escreve "Visão salva como 'Minha visão' (simulado no protótipo)". A US1 pede filtro na URL, visão salva e persistência ao trocar de aba. O desenho dos recortes (período, comparação, marca, regional, estado, cidade, unidade com busca e múltipla escolha, fonte, campanha, procedimento) está completo e o alvo de toque dos chips é 44 px (medido). Correção proposta: serializar o filtro na query (`?de=2026-11-01&ate=2026-11-21&cmp=anterior&un=alto-da-lapa`), copiá-la para todos os links de aba, KPI e alerta, e, no protótipo, ao menos filtrar a tabela da 96 e o título da 97 para a unidade escolhida, para a demonstração não desmentir o controle.

7. **Tabelas largas no celular e ranking sem números.** Severidade: vale corrigir. Evidência medida: `table.t td` e `th` têm `white-space: nowrap`; o cartão tem `overflow-x: auto`, mas os prints de 390 não mostram sombra, seta nem "arraste para o lado". Na 13, a tabela "Campanhas com mais leads" deixa visíveis só campanha e investido. No ranking da 13 em 390, somem índice, leads e % que agenda (fica a lista de nomes); a linha "mediana da rede: índice …" corta no meio. Na 91, os nomes quebram no meio da palavra ("Perfor manc e Max", "formu lário e landin g") e as colunas de conversão saem da tela. Na 96, "Regionais" já nasce cortada em "POR". Correção proposta: no 390, cartões com as três a cinco métricas da pergunta da tela (não a tabela de 10 a 13 colunas). Na 13, cada unidade do ranking vira um cartão com posição, índice, leads e taxa. Na 96, as regionais em cartões empilhados, com todas as colunas visíveis. Onde a tabela desktop permanecer, indicar o scroll horizontal com sombra interna e `scroll-padding`.

8. **Nota 4,4 contra 4,6, e o rateio da 97.** Severidade: vale corrigir. Evidência medida: 13 e 94 dizem nota média 4,4 (1.231 avaliações no período). A tabela de regionais da 96 e a matriz "O que separa o 1º do 4º quartil" mostram 4,6 em SP, Sul, Demais, Rede e nos quatro quartis. Quatro quartis com a mesma nota não separam nada e conflitam com o 4,4. Na 97, as campanhas somam R$ 312 + 232 + 54 + 81 + 78 = R$ 757, mas o KPI "Mídia atribuída" é R$ 699 (CPL R$ 37). Correção proposta: uma nota só, com o recorte escrito (recentes do período ou acumulada). Fazer a nota variar de verdade entre quartis, ou tirar a linha se ela não separa. Recalcular o rateio da 97 para fechar com o KPI, ou listar as campanhas que faltam.

9. **A tela 96 é longa demais para o uso executivo.** Severidade: vale corrigir. Evidência medida: o PNG desktop tem 11.151 px de altura (cerca de doze ecrãs de 900 px); o de 390 tem 25.056 px (cerca de trinta ecrãs). A tabela das 130 unidades tem 13 colunas (`#`, Unidade, Quartil, Índice, Leads, vs. out, Agendam, Comparecem, Vendas, 1º contato, Mídia, Nota, além das de apoio) e, no recorte do meio da página, o cabeçalho já saiu de vista (não há `position: sticky` no CSS medido). Há busca e filtro por regional e quartil no JS, o que é bom, mas o estado inicial despeja as 130. Correção proposta: cabeçalho preso, 25 a 30 linhas por página (ou janela virtual), estado inicial com Q4 e Q1 (ou "buscar e filtrar"), e no celular uma lista em cartões com as métricas do índice. Manter o CSV para quem quiser o recorte completo.

10. **Alertas incompletos e misturados com insight.** Severidade: vale corrigir. Evidência medida: a 93 registra UTM inválida em 3,1%, acima da regra de 3% descrita na 98, mas esse alerta não aparece nem na 13 nem na 98. A 98 lista seis alertas abertos; a 13 mostra só quatro e omite justamente "Agendamentos projetados em 95% da meta" e "24 avaliações escaladas sem resposta", os dois mais executivos. "Quiz converte mais que o formulário" é oportunidade, não anomalia, e ocupa o lugar de um risco. A regra de 1º contato é "acima de 30 min", mas o alerta aberto fala em "acima de 60 min". Correção proposta: separar "Precisa de ação" e "O que está indo bem". No primeiro ecrã da 13, os riscos (Goiás, CPL, unidades lentas, projeção de agendamento, escaladas, UTM). Conferir o limiar da regra com o texto do alerta. A 94 deve exibir a meta da spec 004 (90% respondidas em 48 h; notas 1 e 2 em 24 h), como pedia a crítica da tela 84.

11. **Selo Fase 2 no lembrete.** Severidade: vale corrigir. Evidência medida: o KPI "Lembrete confirmado 61%" da 92 leva o selo "Fase 2". A matriz 005 classifica "Comparecimento, faltas, lembrete confirmado" como Integração (DocBiz e spec 002). Fase 2, na matriz, é só "Pedidos e vendas online" (bem rotulado na 95). O bloco "Comparecimento e faltas" da mesma 92 mistura os selos Integração e Fase 2. Correção proposta: "Integração" no lembrete, alinhado à matriz. Reservar Fase 2 para vendas online.

12. **Legenda de situação repetida em tela cheia no celular.** Severidade: vale corrigir. Evidência medida: `.rr-legst` (13 px, `margin: -4px 0 14px`) explica os quatro selos com texto corrido e, no 390, ocupa cinco a seis linhas em cada uma das 11 telas, antes de qualquer número. No desktop cabe em duas linhas e é útil na primeira visita. Correção proposta: no 390, uma linha com os quatro pills e um "O que é isso" que abre o texto. Depois da primeira visita, só os pills.

Itens de menor peso (detalhe), ainda no conjunto: rótulos de seção da lateral já sobem para 12 px na regra posterior de `estilo.css` (medido), o que atende o piso da crítica geral; o botão CSV cai para a linha de baixo do H1 nas telas 92, 95, 96 e 97 (o `flex-wrap` do `.cab .dir` quebra a tríade Agendar / PDF / CSV); várias campanhas de Pesquisa repetem CTR 6,1% (parece dado fabricado demais para executivos que olham casa decimal); o filtro de UF diz "AL · 1 unidades" e uma unidade aparece como "São Paulo/SP/SP"; eventos internos no subtítulo de KPI ("unidade_visualizada"); a fonte da 91 e da 93 cita "dicionário v0.1" enquanto a matriz fala em v3; o selo "Ambiente de demonstração" do cabeçalho, visível no desktop (`.selo`, 12 px, âmbar `#8A5800` em `#fdf1dc`, 5,41:1 calculado no token e medido no PNG), não aparece na primeira tela dos prints de 390 (só o rodapé no fim da página).

## 3. Tela 13 em profundidade

**O que precisa fazer.** Responder numa tela, sem planilha: quanto investimos, quantos leads, quantos agendaram, quanto vendeu e qual campanha dá retorno (critério de sucesso da spec). Mostrar variação, meta, alerta e o que mudou. Levar o executivo à subtela ou à unidade com um clique.

**Veredito.** A página já tem o material de um briefing de diretoria: dez KPIs com minigráfico nas três primeiras, série diária contra o período anterior, funil com régua de mercado, origem em barras (e a nota certa de que barra se lê melhor que pizza), mapa IBGE com média por unidade, quartis, campanhas, alertas, metas com ritmo e sazonalidade com previsão. A costura entre fontes é honesta (plataforma 16:40, custo de mídia 14:00, sazonalidade 06:00). O que falha é a ordem, o clique e dois números que não se deixam dividir.

**Primeiro ecrã hoje (medido no PNG 1440, faixa 0 a 900).** Cabeçalho com busca, selo de demonstração e ações. H1 "Relatórios da rede" (24 px, token `--fs-h1`) e linha de apoio. Dez abas do hub em duas linhas. Dez chips de filtro mais Limpar e Salvar visão. Legenda das quatro situações. Grade 5 × 2 de KPIs, valor em 24 px (`.rr-k div.v`, medido), variação em 12 px, selos, sparkline absoluto à direita nas três primeiras (`.rr-sp`, escondido no 390). Não cabem série, funil, alertas nem metas.

**Achados ranqueados da 13 (além dos itens 2, 3, 4 e 5 do conjunto).**

- Hierarquia: "Receita atribuída" e "Vendas de pacote" repetem o mesmo recorte (621 vendas, ticket 1.180) e empurram a nota 4,4 para o rodapé. Investimento sobe 7,6% em verde; para mídia, gastar mais não é automaticamente bom. Proposto: cor neutra quando a métrica não tiver sentido único, ou variação contra orçamento (já existe 94% na 98).
- Tipografia: subtítulos de KPI em 12 px (`.rr-k .d`) passam no contraste (tinta-3 em branco, 7,08:1 calculado), mas o de Leads junta duas comparações ("+14,2% vs. out · +30,4% vs. nov/25") e aperta. Proposto: a variação principal no cartão e a de ano anterior na série, ou um segundo número só no hover e na 13 ampliada.
- Cor: tokens semânticos passam AA no texto de 12 px. Verde `#0B7A54` em `#e5f5ee` = 4,74:1 (calculado, justo no limite). Âmbar `#8A5800` em `#fdf1dc` = 5,41:1 (calculado e medido no PNG do selo). Azul `#2C5BC4` em `#e9effc` = 5,36:1. Variação verde amostrada no PNG (12, 123, 85) em branco = 5,28:1. Branco no rosa `#e5559f` continua 3,42:1 (fica para AA de texto grande; não é o preenchimento dos botões desta tela, que usam magenta `#b0197e`, 6,39:1).
- Interação: PDF chama `window.print()` (aceitável no protótipo). CSV exporta a tabela `#tab-principal` de verdade. "marcar as visíveis" no filtro de unidades é `href="#"`. A série e o funil não são clicáveis por dia ou por etapa.
- Texto: o funil explica "250 ainda por vir" e "445 agendaram sozinhos", o que é honesto. A origem lista primeiro os quatro grupos (1.643 + 1.045 + 270 + 28 = 2.986, medido) e, abaixo, fontes soltas; um leitor apressado pode somar os dois blocos. Proposto: um rótulo "Detalhe das fontes" entre os grupos e as linhas.
- Acessibilidade: `lang="pt-BR"`, abas com `aria-label="Seções do hub de relatórios"`, mapa e séries com `role="img"` e `aria-label`. Os KPIs, sendo `div`, saem da ordem de tabulação como ação. Fonte 12 px no rodapé dos blocos é o piso combinado; não voltou 10 ou 11 px no conteúdo do hub.

**Escolha dos gráficos da 13.** Série diária com quatro linhas e período anterior tracejado: certa para "o que mudou no mês". Funil em barras horizontais de mesma base: certo (evita pizza). Origem em barras: certo. Mapa coroplético por UF com média por unidade (a nota "evita que SP, 86 unidades, domine" é a decisão certa). Metas em barra de ritmo com meta vertical e projeção hachurada: certo, mas hoje está longe demais da dobra. Sazonalidade em colunas com linha do ano anterior e caixa da previsão de novembro: certo. Evitar rosca para origem ou para o funil.

**Proposta de ordem e hierarquia (primeiro ecrã, desktop 1440, altura alvo ~ 900 px).**

```
[Selo: Ambiente de demonstração]     [Agendar envio] [PDF] [CSV]
Relatórios da rede
01 a 21 nov 2026  ·  vs 01 a 21 out  ·  Gio  ·  130 unidades    [Filtros] [Situação dos dados]

Manchete (uma frase):
Projeção de leads em 107% da meta. Goiás caiu 31% após a pausa da campanha.
Agendamentos projetados em 95%. 24 avaliações escaladas sem resposta.

[Alerta] Goiás −31%          [Alerta] 24 escaladas         [Alerta] 3 unidades > 60 min
[Meta leads 107%]            [Meta agend. 95%]             [ROAS 5,8x  ·  R$ 365 mil / R$ 62.643]

KPIs clicáveis (5 × 2), cada um com variação, meta ou mediana, e selo:
Leads 2.986                  Agendados 1.733               Compareceram 1.071
Vendas 621  ·  R$ 733 mil    Investimento R$ 62.643        CPL R$ 38  ·  Custo/agend. R$ 69
ROAS 5,8x                    1º contato 11 min             Nota Google 4,4  ·  77% respondidas
(o décimo slot: Receita de pacotes ou Custo por comparecimento, sem reusar o nome "atribuída")
```

Abaixo da dobra, nesta ordem: série diária; funil com régua de mercado; origem e mapa lado a lado; ranking com quartis e campanhas; sazonalidade; índice das seções (já bom). No 390, a mesma manchete, dois alertas de risco em largura cheia, metas em três cartões, depois KPIs em grade 2 × 5, depois os blocos em coluna única. Sem tabela larga. Sem legenda de parágrafo antes do primeiro número.

## 4. Crítica por subtela (90 a 99)

### 90. Aquisição e campanhas

**O que precisa fazer.** Mostrar Google e Meta lado a lado, custo por etapa (não só CPL), tabela ordenável, dispersão CPL × taxa de agendamento, ritmo do orçamento e campanhas para clientes (US3).

**Veredito.** É a subtela mais convincente para quem olha mídia. Os dez KPIs fecham com a tabela (investimento, impressões, cliques, 1.643 leads, 904 agendamentos, 546 comparecimentos, 309 vendas, R$ 364.620, ROAS 5,8x, todos medidos). "Meta traz lead mais barato, mas agenda menos" é exatamente a frase que a pesquisa pedia. A atribuição (último clique em 30 dias, gclid, fbclid, ctwa_clid, conversão offline) está escrita sob a tabela, no lugar certo.

**Achados.** Vale corrigir: a tabela de 13 colunas no 390. Vale corrigir: o botão CSV do topo deveria exportar esta tabela com nome óbvio; o da 13 exporta outra. Detalhe: CTR 6,1% idêntico em Depilação SP, Ultraformer, Avaliação gratuita, Limpeza de pele, Marca Gio e Depilação GO; para apresentação, variar um pouco ou arredondar de forma menos repetida. Detalhe: "Marca Gio" com ROAS 16,5x e 66% de agenda merece um chamado no topo da 13, não só a segunda linha por volume de leads.

**Gráfico.** O comparativo Google × Meta em cartões com as mesmas métricas é melhor que um gráfico de rosca. A dispersão CPL × % que agenda, com tamanho = leads, retas de média e número no círculo, é o gráfico certo para "qual campanha revisar". Manter anotações no canto ("barato e agenda bem" / "candidatos a revisão"). Evitar eixos sem unidade. No 390, a dispersão precisa de rótulos só nos pontos extremos (Marca Gio, Criolipólise PMax), não nos 13 números empilhados.

### 91. Leads e funil

**O que precisa fazer.** Funil das dez fontes até a venda, conversão por grupo, ponto de entrada, procedimentos, tempo até agendar e motivos de perda (US4).

**Veredito.** O recorte é o certo e as contas fecham (fontes, entrada, procedimentos e faixas de tempo somam 2.986 ou 1.733, medido). Motivos de perda somam 498, com 144 "sem motivo" (29%), o que justifica o campo obrigatório. Não há PII. "Campanhas para clientes agendam 92%" é um insight acionável.

**Achados.** Vale corrigir: a tabela "Funil por fonte" (10 colunas) no 390 quebra palavras e esconde conversão; virar cartão por fonte, com leads, % que agenda, vendas e CPL (ou "sem mídia"). Detalhe: a linha total da tabela repete CPL R$ 38, que é só o da mídia, sob um total de 2.986 leads; escrito assim parece custo de toda a rede. Detalhe: a fonte cita "dicionário v0.1". O grupo "Orgânicos e Google" no KPI inclui Instagram, um nome um pouco largo demais.

**Gráfico.** Barras de conversão por grupo de fonte (agendou / compareceu / comprou) são a escolha certa. Tempo até agendar e motivos de perda também em barras horizontais. Evitar pizza de procedimentos ou de motivos.

### 92. Atendimento do franqueado

**O que precisa fazer.** Mediana e faixas de 1º contato × agendamento, mapa de calor de dia e hora, unidades lentas, comparecimento, faltas, lembrete, unidade × call center (US5).

**Veredito.** É a subtela que melhor conta uma história de operação: quem é contactado em até 5 min agenda 71%, depois de 24 h agenda 19%; 21% dos leads chegam entre 19h e 22h (619 ÷ 2.986 = 20,7%, medido); o call center agenda 69% contra 58% da unidade. Faixas, calor, comparecimento e "quem atendeu" somam 2.986 ou 1.733. Sem PII. A referência da HBR está citada com data e tamanho da amostra, no tom certo (é régua, não do cliente).

**Achados.** Bloqueio do destino: as oito unidades lentas abrem a 97 do Alto da Lapa (item 1). Vale corrigir: selo Fase 2 no lembrete (item 11). Vale corrigir: o subtítulo do KPI "Taxa de contato" ("445 agendaram sozinhos") descreve outro fenômeno. Detalhe: o trio Agendar / PDF / CSV quebra, e o CSV fica sozinho à esquerda, debaixo do H1. Detalhe: a regra da 98 fala em 30 min e o alerta em 60 min.

**Gráfico.** Barras de faixa de tempo: certas. Mapa de calor de uma só matiz (lilás a vinho) com o número dentro da célula (`.rr-heat`, 12 px, célula de 34 px no desktop e 30 px no 390, medido): certo e melhor para daltonismo do que uma escala verde-vermelha. Comparecimento e faltas em barras empilhadas por situação: certo. Evitar relógio ou radar.

### 93. Quiz, landings e tráfego

**O que precisa fazer.** Funil das páginas, funil do quiz e demanda, modelos A/B/C, aparelho e canal, saúde do rastreamento com liga à 70 (US6).

**Veredito.** Fecha o ciclo "antes do lead" e avisa, com razão, que UTM inválida distorce fonte e CPL. Modelos A + B + C = 130 unidades e 412.880 visitas (medido); o A converte 25% mais que o C. Recomendações do quiz somam 4.512. Há link para a 70, a 66 e a 63. "sem dado pessoal" na fonte do quiz é o texto certo.

**Achados.** Vale corrigir: o funil das páginas mistura "começaram o formulário 4.630" com "enviaram 2.986 somando quiz e WhatsApp". A taxa de 64% não é abandono só do formulário (o texto admite 2.758 abandono, mas a barra mistura pontos de entrada). Proposto: um funil só do formulário (visitas, começou, enviou) e o quiz ao lado, como já está. Vale corrigir: UTM 3,1% deveria virar alerta aberto (item 10). Detalhe: o KPI de visitas traz o nome técnico `unidade_visualizada` no subtítulo, que não é copy de executivo. Detalhe: "Leads por visita 0,72%" usa 2.986 no numerador, inclusive leads que podem não ter passado pela página da unidade.

**Gráfico.** Dois funis em barras. Aparelho e canal em barras, não em rosca. Saúde do tracking em três indicadores com limiar (já está bom). Evitar um funil único que some formulário, quiz e WhatsApp na mesma boca.

### 94. SEO local, Google e avaliações

**O que precisa fazer.** Performance do perfil, Search Console, resumo da spec 004 com liga à 84, régua BrightLocal, SEO por estado (US7). E incorporar o que a crítica da 84 pedia para executivos: risco primeiro, KPI clicável com meta, drill-down real.

**Veredito.** A junção perfil + Search Console + avaliações no mesmo hub é o que a pesquisa pedia. As aparições somam 1.284.500 (medido). "104 de 130" e a frase "26 unidades ainda não concederam acesso" são o dado de gestão mais útil da tela, mas ficam abaixo da dobra, depois de cinco KPIs de volume. Há link "Abrir avaliações (84)" e "SEO local da unidade (19)". A fonte do perfil avisa D-2 e a do Search Console, D-3: o tipo certo de transparência.

**Achados.** Vale corrigir: "Sem resposta 284" e "Escaladas abertas 24" (os mesmos números da 84) deveriam estar no primeiro ecrã, com a meta de 90% em 48 h e de notas 1 e 2 em 24 h, e o cartão de escaladas com ênfase (`kpi-a.alerta` já existe no CSS). Vale corrigir: a nota 4,4 daqui não pode conviver com 4,6 na 96 (item 8). Vale corrigir: KPIs ainda são `div`. Detalhe: a tabela "SEO local por estado" lista só sete UFs (94 dos 104 perfis); faltam BA, RJ, PA e as demais. Detalhe: "Posição média −0,6, quanto menor, melhor" precisa de cor de variação invertida (queda é boa) e, de preferência, da palavra "melhorou".

**Gráfico.** Barras de aparições (busca e Maps, celular e computador) e de ações do perfil: certas. Consultas do Search Console em tabela, não em nuvem de palavras. Evitar rosca de 4,4 estrelas. Um histograma de notas 1 a 5, clicável para a 84, faltava na 84 e ainda falta aqui.

### 95. Área do cliente

**O que precisa fazer.** Contas, consentimentos, ofertas, agendamentos online, pacotes, NPS, mural e campanhas; vendas online na fase 2 (US8).

**Veredito.** Página clara, toda em agregados, com a frase certa de LGPD: "Consentimento sempre desmarcado e por finalidade". NPS 76 − 5 = 71 (medido). 486 agendamentos online, 131 remarcações e 214 agendamentos de campanha batem com a 90 e a 92. "Pacotes acabando 812" e "33 unidades ainda não confirmaram o aviso" são ações de rede. Vendas online 94 (R$ 127.840) com selo Fase 2: correto.

**Achados.** Detalhe: o canal "Área do cliente 100%" na barra de consentimentos não é consentimento de marketing; pode parecer que todos aceitaram comunicação. Proposto: retirar essa barra ou chamá-la de "têm conta". Detalhe: quebra do botão CSV no cabeçalho. Vale corrigir, se a 95 for usada no celular: manter o bloco de consentimentos e o de pacotes acabando acima da dobra, não só depois de dez KPIs.

**Gráfico.** Barras de consentimento e composição do NPS (promotores, neutros, detratores): certas. Evitar gauge de NPS. Ofertas em barras de cliques, já no caminho certo.

### 96. Unidades e regiões

**O que precisa fazer.** Tabela por regional, mapa com troca de métrica, quartis ("o que separa Q1 de Q4"), dispersão volume × conversão, tabela das 130 com busca, filtro, ordenação e CSV (US9).

**Veredito.** É o coração do benchmark interno e, em desktop, está rico da maneira certa: regionais com a mesma régua, mapa IBGE com três métricas, tabela de quartis, dispersão e lista completa. Leads 1.984 + 421 + 581 = 2.986 e investimento 42.065 + 8.694 + 11.884 = 62.643 (medido). Sul com 30,1 leads por unidade, contra 23,0 da rede, é um insight imediato. O problema é o formato (página de 11.151 px, 25.056 no celular), a definição de comparecimento (62%), a nota 4,6 uniforme e o clique que leva sempre ao Alto da Lapa.

**Achados.** Além dos itens 1, 3, 8 e 9 do conjunto: a dispersão colorida por quartil usa verde (Q1) e vermelho (Q4), par ruim para daltonismo de verde-vermelho. Proposto: uma só matiz de vinho mais forma (círculo, quadrado) ou rótulo Q1 a Q4 no hover, que já deveria mostrar o nome da unidade e abrir a 97 certa. O eixo Y está escrito ("% que agenda"); o X (volume de leads, estimado pelo desenho) precisa do mesmo rótulo, visível. "Trocar a métrica no mapa" existe (JS `data-mapa`) e é o controle certo; falta o clique no estado filtrar a tabela.

**Gráfico.** Mapa coroplético com média por unidade: certo, e resolve o bloqueio antigo da malha. Tabela de quartis: certa (melhor que quatro pizzas). Dispersão volume × conversão com medianas tracejadas: certa. Evitar outro mapa desenhado à mão e evitar 130 barras na vertical como substituto da tabela.

### 97. Relatório da unidade

**O que precisa fazer.** Uma unidade contra a mediana da rede, com próximos passos, sem expor números de outras unidades ao franqueado (US9 e FR-009).

**Veredito.** O desenho da página está certo: identidade da unidade, posição, KPIs com mediana, funil comparado, fontes, rateio de campanha, série de seis meses e três próximos passos concretos (contato, avaliações, quiz na recepção). A nota de escopo do franqueado está escrita no corpo, no tom certo. O que quebra a demonstração é o conteúdo ser sempre o do Alto da Lapa, o comparecimento com régua diferente da 13, o rateio que não fecha e o botão "Trocar unidade" que só devolve à 96.

**Achados.** Bloqueios 1 e 3, e o rateio do item 8. Detalhe: o KPI "Visitas à página" corta o subtítulo no cartão ("modelo B · página de de", medido no PNG 1440). Proposto: 12 px com `text-wrap` ou uma segunda linha, por exemplo "Modelo B, página de serviço ativa". Detalhe: "4 sem resposta, 2 com nota baixa, uma escalada (tela 80)" é o tipo certo de próximo passo; o destino deveria ser a 80 já filtrada da unidade, não a 97 de outra. Vale corrigir: falta um exemplar de unidade Q4 (Montes Claros ou Paulínia) na apresentação, para a diretoria ver o que a rede faria com quem precisa de apoio.

**Gráfico.** Funil da unidade × rede em tabela de diferenças (pontos percentuais) é mais legível que duas áreas sobrepostas. Série mensal em colunas: certa. Evitar radar de "performance geral".

### 98. Metas, previsão e alertas

**O que precisa fazer.** Metas por rede, regional e unidade; acumulado com faixa de previsão e ritmo; regras e anomalias; alertas abertos (US10).

**Veredito.** É a subtela mais "de executivo" depois que se chega nela. A série acumulada com realizado, projeção, faixa e ritmo da meta (4.000) é o gráfico certo. As metas do mês (107%, 95%, 93%, 94%) fecham com a 13. A soma das regionais é 2.610 + 560 + 830 = 4.000 na meta, 2.986 no realizado e 4.264 na projeção (medido). O bloco "O que precisamos da Salus" é valioso na apresentação: deixa claro o que ainda é Integração ou cadastro. As regras cobrem o que a US10 pediu.

**Achados.** Vale corrigir: a coluna "Ativa" existe no cabeçalho e não mostra controle de ligar, desligar ou editar (não há `checkbox` nem botão além dos filtros, medido no HTML). Vale corrigir: alertas e limiares (itens 10). Detalhe: no 390, a primeira tela ainda gasta a dobra com a legenda; o gráfico certo quase não entra. Proposto: no celular, gráfico e a frase da projeção (4.264, 107%) antes da legenda longa. Falta o estado de "cadastro de meta" (a Salus informa, mas não há tela de edição neste lote).

**Gráfico.** Linha acumulada com faixa e ritmo: certo (é o desenho que o GA4 inspira, e a fonte está citada). Barras de ritmo das metas: certas. Evitar velocímetro. A tabela de regionais é melhor que um mapa só para três linhas.

### 99. Exportar e agendar envio

**O que precisa fazer.** PDF executivo e CSV com os filtros atuais; envio agendado só com agregado; exportação com dado pessoal permissão, auditoria e sem agenda (US11).

**Veredito.** O fluxo está bem pensado: formulário à esquerda, prévia do PDF à direita (logo, três números, mini série, destaques, "números agregados", página 1 de 4), lista de envios com "6 de 6 abriram". A caixa "Sem dado pessoal no envio" é o melhor texto de LGPD do lote e cita a tela 17. Destinatários de exemplo (`diretoria@exemplo.com.br`, `marketing@exemplo.com.br`) são claramente fictícios. Frequência, horário de Brasília e escopo por perfil estão no lugar.

**Achados.** Vale corrigir: os campos são `div.campo .in` visuais, não `input` ou `select` (o único `input` da página é a busca de unidade do filtro global, medido). Não há estado de sucesso, erro, "agendamento salvo", prévia enviada, pausar, editar ou excluir um envio, nem a lista completa dos "+4" destinatários. Vale corrigir: "CSV desta lista" não tem lista à vista (o formulário não é uma tabela); copiar "CSV desta página" ou tirar o botão. Detalhe: o "Agendar envio" do cabeçalho, nesta tela, é circular (o executivo já está no fluxo). Detalhe: a prévia do PDF, boa como miniatura, ainda herda o ROAS 5,8x ao lado de leads e agendados, sem a receita atribuída certa; quando o item 2 for corrigido, a prévia precisa acompanhar. Falta o fluxo (mencionado no texto) de exportação pontual com dado pessoal e o registro na auditoria: um diálogo de confirmação, não só a frase.

**Gráfico.** A mini série da prévia é suficiente. Evitar reproduzir a 13 inteira no primeiro cartão do PDF; a manchete, três a cinco KPIs, dois alertas e a tabela de metas cabem em uma página executiva (proposta).

## 5. Catálogo de gráficos recomendado

| Pergunta do executivo | Gráfico a usar | Evitar |
|---|---|---|
| O que mudou no período? | Linha diária com período de comparação tracejado e pico anotado | Pizza do "mix do mês" |
| Onde o funil vaza? | Barras horizontais de mesma base, com % da etapa anterior e da boca | Funil 3D, rosca, misturar formulário com WhatsApp na mesma boca |
| De onde vêm os leads? | Barras por grupo e, abaixo, detalhe das fontes | Pizza; somar grupo e detalhe no mesmo eixo |
| Qual estado ou regional olhar? | Mapa coroplético IBGE com média por unidade e clique que filtra | Polígono à mão; cor que represente soma absoluta em SP |
| O que separa as melhores unidades? | Tabela de quartis + dispersão volume × conversão com medianas | Ranking só de nomes, sem índice |
| Qual campanha revisar? | Dispersão CPL × taxa de agenda (tamanho = volume) + tabela ordenável | Ordenar o hub só por leads |
| O 1º contato vale a pena? | Barras por faixa de tempo × % que agenda | Relógio |
| Quando chega o lead? | Mapa de calor dia × hora, uma matiz, número na célula | Dois eixos de cores |
| Vamos bater a meta? | Linha acumulada com faixa de previsão e reta (ou degrau) do ritmo | Velocímetro |
| Como está a reputação? | KPIs com meta + histograma de notas 1 a 5 clicável | Rosca da nota 4,4 |
| Aparelho ou canal da visita? | Barras empilhadas ou agrupadas | Rosca de 78% celular |

Cor: usar a escala de vinho e lilás para quantidade; reservar verde, âmbar e vermelho para variação e alerta, já nos tokens que passam AA. Na dispersão de quartis, não apoiar a leitura só no par verde e vermelho.

## 6. Fontes e situação dos dados

O padrão já desenhado é o certo e deve ser mantido em todo bloco: uma linha `.rr-fonte` (12 px, `--tinta-3`, 7,08:1 em branco, calculado) com relógio, a origem em português, a hora da última leitura e o fuso ("horário de Brasília"), mais os selos à direita. Horas diferentes (16:40 da plataforma, 14:00 da mídia, 06:00 do perfil e do Search Console, 15:40 das avaliações) são um acerto: mostram que o hub não finge uma única extração.

**Selo (copy proposta, curta o bastante para o 390).**

- Do sistema (verde): "A plataforma já captura este número."
- Integração (azul): "Depende de API ou da DocBiz. Última leitura: [hora]. Atraso típico: [D-2, 6 h, etc.]."
- Depende da Salus (âmbar): "Entra quando a Salus informar (meta, orçamento, venda, tarifa)."
- Fase 2 (neutro): "Entra com as vendas online da área do cliente."

Onde o número for estimado (projeção, faixa, rateio de campanha regional), escrever "estimado" no próprio valor, não só no rodapé. Onde for medido, não repetir. O selo de demonstração do produto ("Ambiente de demonstração. Números e pessoas são ilustrativos, salvo quando a fonte é citada") deve permanecer no cabeçalho, inclusive no 390, e no rodapé. Não misturar, no mesmo cartão, um volume real de GBP com um inventado, sem o selo: o rodapé já autoriza o fictício, e a apresentação deve tratar tudo deste lote como demonstração.

Conferência de totais (medido, fecha): leads 2.986; mídia 1.643; orgânico 1.045; relacionamento 270; outros 28; agendados 1.733; compareceram + faltas + cancelamentos + futuros = 1.733; vendas 621; investimento Google 49.516 + Meta 13.127 = 62.643; regionais 1.984 + 421 + 581 = 2.986; unidades no filtro 86 + 8 + 7 + 7 + 4 + 3 + 3 + 2 + 2 + 2 + 1 × 6 = 130. O que não fecha está nos itens 2, 3 e 8.

## 7. Drill-down e filtros

**Mapa de navegação proposto (o filtro atual vai sempre na URL).**

- 13, KPI Leads, Agendados, Perdidos → 91
- 13, KPI Investimento, CPL, ROAS, campanha do alerta → 90, com a campanha aberta ou marcada
- 13, KPI 1º contato e alerta de unidades lentas → 92, com a tabela já recortada; cada unidade → 97?unidade=
- 13, KPI Nota e alerta de escaladas → 94 e, de lá, 84 com o mesmo recorte (meta 90% / 24 h à vista)
- 13, metas e alerta de projeção → 98
- 13, mapa ou linha de UF → 96?uf=SP (tabela já filtrada)
- 13, linha do ranking e qualquer nome de unidade no hub → 97?unidade=
- 96, ponto da dispersão e linha da tabela → 97?unidade=
- 97, "Ficha da unidade" já vai à 07 (medido); "Trocar unidade" permanece na 97 e troca o slug; avaliações pendentes → 80 daquela unidade
- 93, saúde do tracking → 70 (já existe o link)
- 95, campanhas e mural → 62 e 59 (já existem)
- 99, "envio com dado pessoal" → diálogo de permissão e registro na 17

**Comportamento do filtro global (proposto, atende a US1).** Uma linha resumo sempre visível. O painel com os dez recortes abre no lugar, como hoje (o popover, a busca de unidade e a múltipla escolha já estão bons). Aplicar grava a query, atualiza os números e o pill "n ativos". Trocar de aba, de KPI ou de alerta preserva a query. "Limpar" volta à rede inteira no período padrão (mês corrente até hoje, comparação com o período anterior). "Salvar visão" pede um nome e aparece de verdade na 99, no campo Filtros. Comparação "ano anterior" e "sem comparação" precisam de um estado visual da 13 (a opção já está no popover, mas não foi prototipada nos números). Regional vê só as suas unidades, com a mediana da rede como referência; franqueado cai na 97 da própria unidade, sem nomes de outras; financeiro e agência não veem PII (já é a regra da spec; falta um estado visual destas visões).

## 8. Celular

Não há barra de abas inferior nestas páginas (o HTML não inclui `.tabbar`; o admin no 390 usa o botão de menu e a lateral em sobreposição a partir de 1.100 px, medido). Não tratei artefato de captura de aba no meio do print, porque ele não aparece neste lote. O padding inferior de aba, portanto, não se aplica; o risco aqui é outro.

A tela 13 em 390 hoje não serve de resumo executivo. A primeira tela (844 px, medido) entrega H1, três botões grandes, abas que cortam "Lea…", o atalho "Filtros rede inteira" (bom), a legenda longa e quatro KPIs, sem manchete, sem alerta e sem meta. A série e o funil, mais abaixo, estão legíveis. O mapa IBGE, no 390, continua reconhecível (isso é um acerto). O ranking perde as métricas. As campanhas perdem CPL e ROAS.

Padrão proposto para as 11 telas no 390: (1) selo compacto de demonstração junto aos ícones; (2) H1 e uma linha de recorte + Filtros; (3) manchete e um a dois alertas; (4) KPIs em grade 2 colunas, valor 20 px (já é o token móvel de `.rr-k div.v`); (5) blocos em coluna; (6) cartões no lugar de tabela larga; (7) gráficos com menos rótulos, só extremos e o ponto do dia. Os chips de filtro em duas colunas, com `min-height: 44` px, já estão no caminho certo quando o painel abre. As abas do hub devem ser uma faixa com `scroll-padding` e o destino visível, não um recorte "Lea".

Na 96, não pedir que o executivo role 25.000 px. Na 99, a coluna única (formulário e, abaixo, a prévia) é a ordem certa. Na 98, o gráfico de previsão deve aparecer antes da legenda.

## 9. O que falta (telas, estados, componentes)

- Relatório da 97 para pelo menos uma unidade de cada quartil, com slug na URL, e um seletor que troca o conteúdo na página.
- Estados do filtro: aplicado (números mudam), vazio (nenhuma unidade no recorte), comparação com o ano anterior e sem comparação.
- Estados de dado: API atrasada ou fora (Search Console D-3, perfil D-2, mídia a cada 6 h), dado parcial, estimado, zero no período.
- Estados da 99: agendamento salvo, prévia enviada, erro de destinatário sem acesso, pausar e editar envio, ver os seis destinatários, diálogo de exportação com dado pessoal e recibo na auditoria (17).
- Cadastro e edição de metas (rede, regional, unidade) e liga/desliga das regras da 98, com confirmação.
- Visões por papel, ainda que em miniatura: regional, franqueado (só 97), financeiro (agregados), agência (só 90 e o CSV de campanhas).
- Histograma de notas e a meta de resposta na 94, com destino real na 84 (pendência da crítica anterior que o hub ainda não fecha).
- Mapa e KPIs como alvo de teclado e de clique, com foco visível (o token `--foco` já existe).
- Cabeçalho preso, paginação e cartões na 96.
- Página ou modal de "visões salvas" (hoje só a mensagem simulada).
- Uma prévia de PDF de uma página no padrão da manchete proposta, já com as definições corrigidas de receita e comparecimento.

Não falta ideia de gráfico, nem a lista de seções. Falta o casco de navegação (filtro, destino, estado) à altura do conteúdo.

## 10. Plano curto de aplicação (ordem sugerida)

1. Corrigir os três bloqueios de confiança: slug na 97 (com quatro ou cinco unidades de verdade no protótipo), nomes e contas de receita e ROAS, uma só definição de comparecimento em 13, 91, 92, 96, 97 e na prévia da 99.
2. Reordenar a 13 no desktop e no 390 (manchete, alertas de risco, metas, KPIs com nota no Google, filtros e legenda recolhidos). Ligar cada KPI, alerta, UF e unidade ao destino com a query do filtro.
3. Persistir o filtro na URL e nas abas; fazer a 96 (tabela) e a 97 (título e números) reagirem a ele, mesmo que as demais páginas ainda mostrem o aviso de protótipo.
4. Substituir tabelas largas do 390 por cartões; prender o cabeçalho e paginar a 96; alinhar a nota 4,4 / 4,6 e o rateio da 97; incluir o alerta de UTM e as metas de resposta na 94.
5. Fechar a 98 (controles das regras) e a 99 (campos de verdade, confirmação, gestão dos envios, prévia com a manchete certa). Aplicar o selo de demonstração no primeiro ecrã do 390. Só então polir detalhe de CTR, CSV que quebra o cabeçalho, copy técnica e grammar do filtro.

Com o passo 1 e o passo 2, a apresentação para a diretoria já muda de figura: os números se deixam dividir, o clique não trai o executivo, e a primeira tela responde às perguntas que a spec definiu como sucesso.
