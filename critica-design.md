# Crítica de design: Sistema de Unidades Gio

Cliente: Gio Estética Avançada (Salus), rede de 130 clínicas franqueadas.
Pedido: Osmar, via Stark. Meta: um sistema robusto, corporativo e moderno, capaz de surpreender na apresentação.
Fonte: 20 PNGs em `png/` (desktop 1440 CSS px; celular 390 CSS px em captura 2x, medidas convertidas), HTML em `telas/` (a pasta `html/` citada no pedido não existe), `telas/estilo.css`, `specs/001-sistema-unidades/` e `galeria.pdf` (consulta de contexto). Nenhum arquivo existente foi alterado.
Data da crítica: 21 de novembro de 2026, America/Sao_Paulo.
Método: sete passes por tela (hierarquia, espaçamento, tipografia, cor, interação e estados, texto, acessibilidade). Contraste WCAG calculado pela luminância relativa a partir dos tokens do CSS e, quando necessário, de pixels amostrados no PNG. Tamanhos de tipo lidos no CSS e no HTML (medido), não estimados no bitmap, salvo indicação contrária. Valores rotulados como medido, estimado ou proposto. Severidade só assume "bloqueio", "vale corrigir" ou "detalhe".

## 1. Veredito geral

O conjunto já tem cara de produto, não de wireframe. A identidade (Poppins e Inter, roxo, vinho e magenta, logo e fachada) está aplicada com disciplina. As telas que mais convencem na apresentação são o detalhe do lead com jornada e LGPD, a fila de aprovações com diff e validador de marca, o assistente de domínio, o dashboard do franqueado com posição no ranking (sem expor números de outras unidades) e a landing A com formulário na primeira tela. O portal da franqueadora e o do franqueado já se diferenciam de propósito (lateral escura versus clara com acento rosa), o que é um acerto.

O que mais custa, e o que tira o efeito de "sistema robusto e corporativo", está em quatro pontos. O mapa do Brasil é um polígono desenhado à mão, sem estados e com silhueta irreconhecível. Os modelos B e C da landing existem só como miniatura esquemática, enquanto só o A ganhou página cheia. O admin compacta texto de 10 e 11 px e usa cores semânticas que falham no contraste (âmbar 2,52:1, verde de variação 3,39:1, rótulos da lateral clara 2,52:1, branco no extremo rosa dos botões e do item ativo). Por fim, endereços e telefones reais de unidades (conferidos no GBP do próprio projeto) convivem com notas, CEPs e volumes inventados, o que pode parecer dado oficial numa apresentação.

Corrigindo mapa, contraste e escala tipográfica, fechando B e C em fidelidade de produção e sinalizando dados ilustrativos com rigor, o material fica pronto para surpreender.

## 2. Top 10 correções do conjunto (ordem de impacto)

1. **Mapa do Brasil.** Trocar o polígono de `mapa_br()` em `gerador/base.py` por um SVG simplificado de malha oficial do IBGE (UFs). Manter o recorte de Grande São Paulo e a lista "Fora do mapa". Sem isso, a tela 04 (e qualquer dashboard com mapa) parece protótipo.
2. **Contraste das cores semânticas e do acento rosa.** Recalibrar tokens para texto de 12 a 14 px atingir no mínimo 4,5:1. Prioridade: `--ambar` nos pills (medido 2,52:1), `.side .sec` do franqueado `#b59ac0` em branco (2,52:1), variação verde `#0e9f6e` em branco (3,39:1), branco no extremo `#e5559f` de botões e item ativo (3,42:1 no token; 2,73:1 amostrado à direita do item "Início").
3. **Escala tipográfica do admin.** Subir o corpo de 13 px (medido em `html,body`) para 14 px. Piso de texto lido em 12 px. Eliminar 10 px e 11 px em cabeçalho de tabela, pills, rótulos de seção e ajuda.
4. **Modelos B e C em fidelidade de produção.** Desenhar desktop e celular completos, no mesmo nível das telas 19 e 20, com blocos e hierarquia claramente distintos do A. Atualizar as miniaturas da tela 14 e o preview do editor (15).
5. **Dados ilustrativos versus dados reais.** O dashboard 02 já diz "Dados de exemplo". Estender o aviso a relatórios, landings e fichas. Onde a unidade é real (Batel, Alto da Lapa), ou se usa o NAP oficial e os números oficiais do GBP, ou se fictionaliza tudo (telefone 0000, endereço genérico, nota redonda). Hoje o mix parece operação verdadeira.
6. **Consentimento da landing pré-marcado.** O checkbox "Li o aviso de privacidade..." aparece marcado (ícone de check desenhado no HTML, sem estado desmarcado). Padrão incompatível com LGPD. Deixar desmarcado e impedir o envio até o aceite.
7. **Estados da interface que contradizem os próprios números.** No kanban, o chip "SLA: estourado" está ativo, mas as colunas somam 314 cards e o KPI mostra 9 fora do SLA. Em Suporte, a aba "Abertos" lista tickets já resolvidos. No topo, o período global "01 a 21 nov 2026" compete com o chip "Mês" e com "Últimos 7 dias". Na apresentação, esses cortes quebram a confiança.
8. **Celular: conteúdo sob a barra e área segura.** Na tela 18, o card da jornada fica cortado pela tab bar (medido no PNG 2x: a base arredondada some sob os ícones). Falta `padding-bottom` de pelo menos 56 px CSS (proposto) além da safe area. Na 17, o botão WhatsApp perde contraste no extremo direito do degradê.
9. **Uma única foto de fachada repetida.** Tabela, detalhe, aprovações, editor e landing reutilizam `assets/fachada.jpg`. A galeria "2 fotos novas, 1 removida" e a vitrine da clínica perdem credibilidade. Variar fachada, recepção e sala, ainda que em banco limitado.
10. **Abas e densidade que não escalam.** O detalhe da unidade (05) entrega 11 abas numa faixa só, com badges. A tabela (03) e a matriz de permissões (11) usam cabeçalho 11 px em `#7d7286` sobre `#faf6fb` (4,25:1, abaixo de 4,5:1). Resolver com tipografia, cor e, nas abas, rolagem horizontal ou grupo "Mais".

## 3. Consistência entre Admin Gio e Franqueado

A divisão visual está correta e deve ser preservada: o admin é um painel de rede (lateral em degradê `#2a0a33` a `#4c1455`, item ativo branco com texto `--roxo-700`), o franqueado é um portal da unidade (lateral branca, item ativo em degradê `#b0197e` a `#e5559f`). Os componentes (card 16 px de raio, chips, pills, tabela `.t`, KPI, busca com `Ctrl K`, botões `.btn`) são os mesmos, o que dá unidade de sistema. O que falta é um conjunto explícito de tokens e alguns alinhamentos de conteúdo.

### 3.1 Sistema de tokens proposto

**Tipografia (Inter no corpo, Poppins em títulos e números).** Hoje o corpo é 13 px (medido). Proposto:

| Papel | Tamanho | Peso | Uso |
|---|---|---|---|
| H1 de página | 24 px | 600 | Já medido em `.cab h1`. Manter. |
| Título de card | 16 px | 600 | Hoje `.card h3` tem 14 px. Subir. |
| Corpo | 14 px | 400 | `html,body`. Line-height 1,5. |
| Secundário | 13 px | 500 | Chips, abas, botão padrão. |
| Meta e ajuda | 12 px | 500 | Piso para texto lido. Substituir 10 e 11 px. |
| KPI | 26 a 28 px | 600 | Já medido em `.kpi .v` (26 px). Manter, com `tabular-nums`. |
| Rótulo de seção da lateral | 11 px | 600 | Hoje 10 px. Letter-spacing 0,08 em, não 0,12 em, para não afinar demais. |

**Espaçamento (escala de 4).** Proposto: 4, 8, 12, 16, 20, 24, 32, 40, 48. Padding do `.main`: 24 32 (hoje 22 28 32, medido). Gap de grid e cards: 16 (já medido em `.g`). Padding de card: 20 (hoje 18). Altura mínima de linha de tabela: 48 px. Alvo de toque: 40 px (`.ib` já tem 38, quase lá).

**Cores semânticas (propostas, contraste calculado para texto normal).** Manter a marca. Trocar só o que falha em texto pequeno.

| Papel | Token atual (medido) | Problema | Proposto | Contraste calculado |
|---|---|---|---|---|
| Texto principal | `--tinta` `#1d1424` em branco | Nenhum (17,83:1) | Manter | 17,83:1 |
| Texto muted | `--tinta-3` `#7d7286` em `#f6f2f8` / `#faf6fb` | 4,10:1 no fundo; 4,25:1 no th | `#5E5566` no fundo e no th | Recalcular ao aplicar; alvo ≥ 4,5:1 |
| Sucesso | `--verde` `#0e9f6e` em branco / `--verde-50` | 3,39:1 e 3,06:1 | `#0B7A54` | 5,35:1 no branco; 4,83:1 no `--verde-50` |
| Atenção | `--ambar` `#d98a00` em `--ambar-50` / branco | 2,52:1 e 2,77:1 | `#8A5800` | 6,04:1 no branco; 5,49:1 no `--ambar-50` |
| Perigo | `--vermelho` `#d5305f` em `--vermelho-50` | 4,06:1 no pill (abaixo de 4,5:1) | `#B4234A` no pill | 5,47:1 no `--vermelho-50` |
| Info | `--azul` `#3b6fd8` em `--azul-50` | 4,09:1 | `#2C5BC4` | Alvo ≥ 4,5:1 no `--azul-50` |
| Acento rosa em texto ou com branco por cima | `--rosa` `#e5559f` | 3,42:1 | Texto rosa só em `#b0197e` (6,39:1 no branco). Botão e item ativo: degradê que termine em `#b0197e`, ou texto `#24082c` sobre fundo rosa claro. | 6,39:1 (branco em magenta) |
| Seção da lateral do franqueado | `#b59ac0` em branco | 2,52:1 | `#6B4E78` | 7,03:1 |
| Seção da lateral do admin (parte baixa) | `#a585b1` em `#4c1455` | 4,28:1 | `#E3D3EA` ou `#D7C4E0` | Alvo ≥ 4,5:1 |

**Componentes compartilhados.**

- Tabela: th 12 px, peso 600, cor `#5E5566`, sem depender de caixa alta para hierarquia. Linha 48 px. Colunas numéricas à direita com `tabular-nums` (já existe `.num`).
- KPI: rótulo 13 px, valor 26 a 28 px, variação na cor semântica nova, fonte da métrica e do período sempre visíveis (o 02 já faz isso no subtítulo).
- Estado vazio: ilustração simples + uma frase + uma ação primária. Nenhuma das 20 telas mostra vazio, carregando ou erro. Criar um padrão único para os dois portais.
- Badge e pill: texto 12 px, padding 4 10, nunca 11 px. Status por texto e cor, não só por cor.
- Botão primário do admin: manter o degradê `--grad` (`#4c1455` a `#b0197e`), branco no vinho e no roxo passa (11,68:1 e 6,39:1 no magenta). Botão primário do franqueado: degradê só até `#b0197e`, sem terminar em `#e5559f`.
- Item ativo da lateral do franqueado: mesmo ajuste de degradê, ou fundo magenta sólido `#b0197e` com branco (6,39:1).

### 3.2 O que diverge hoje entre as telas

| Ponto | Admin Gio | Franqueado | Avaliação |
|---|---|---|---|
| Lateral | Degradê escuro, item ativo branco | Branca, item ativo rosa | Acerto de produto. Corrigir só contraste. |
| Assinatura | "Portal da Rede" | "Portal do Franqueado" | Acerto. |
| Busca | Unidade, lead, ticket ou pessoa | Lead, ticket ou artigo | Acerto de escopo. |
| Período global no topo | Presente em quase todas as telas internas | Presente também | Ruim nos dois: o controle não deveria aparecer em Unidades, Aprovações, Domínio ou Editor, onde o recorte de data não se aplica. |
| Ranking | "Alto da Lapa" em 4º no índice de conversão (tela 02) | "Sua unidade está em 7º na rede" (tela 12) | Conflito de métrica ou de dado. Nomear os dois índices ou unificar o número na apresentação. |
| Tratamentos da mesma unidade | Aba com badge 12 (tela 05) | Aba com badge 6 (tela 13) | Provável "6 ligados de 12 do catálogo", mas isso não está escrito. |
| Badge de leads na lateral | 38 na rede | 8 ou 9 (lateral 8, mobile "Todos 9") | Quebrar a conta na demo. |
| Completude Alto da Lapa | 90% nos dois | 90% nos dois | Consistente. |
| Foto | A mesma fachada | A mesma fachada | Fraco nos dois. |
| Pills de status | Mesma classe, mesmo problema de âmbar | Idem | Corrigir no token, não tela a tela. |


## 4. Crítica por tela

### 01. Login

**O que a tela precisa fazer.** Autenticar os papéis (franqueado, Rede Gio, parceiro), oferecer SSO Google da rede, antecipar o 2FA obrigatório e deixar claro o escopo (130 unidades, 16 estados, um painel).

**Veredito.** É a melhor primeira impressão do conjunto: fachada com overlay, headline de 44 px (medido), formulário limpo e o cartão de 2FA e LGPD no lugar certo. Os problemas estão no contraste de apoio, no interruptor de papel que não muda o contexto, e na ausência da tela seguinte (desafio 2FA e erro de senha).

**Achados**

1. **Vale corrigir. Contraste do texto legal e do muted.** O parágrafo "Ao entrar você concorda..." está em 11 px (medido) com `--tinta-3` `#7d7286` em branco: 4,54:1, no limite de AA e abaixo de AAA. O texto "Use o e-mail cadastrado..." é muted no tamanho do corpo. Correção: 12 px e, se permanecer 12 px, escurecer muted para `#5E5566` (proposto).
2. **Vale corrigir. Interruptor Franqueado / Rede Gio / Parceiro.** Os três estados visuais existem (`.sw`), mas o formulário, o e-mail `renata.f@exemplo.com.br` e o cartão de 2FA não mudam. Na apresentação, trocar o papel deveria trocar pelo menos o subtítulo ("Entrar no portal da unidade" versus "Entrar no painel da rede") e a nota de 2FA (obrigatória só para Rede Gio e call center). Correção: três estados de copy, mesmo layout.
3. **Detalhe. "Manter conectado" já aparece marcado**, com um ícone de check sempre visível, sem caixa vazia. Correção: checkbox de 20 px, desmarcada por padrão, ou marcada só se for uma preferência explícita, com estado vazio visível.
4. **Detalhe. Faltam estados de interação** (senha visível, erro de credencial, conta inexistente, 2FA). Para a apresentação, um frame de erro e um de 2FA valem mais do que um novo ornamento no login.
5. **Acerto a preservar.** "Esqueci a senha" usa `--vinho` `#6f0052` em branco (11,68:1, calculado). Headline e subtítulo sobre o overlay passaram na amostragem do PNG: branco em fundo aproximado `#792b6f` com 8,79:1; subtítulo `#eadce7` em `#731761` com 7,85:1. E-mail de exemplo é claramente fictício.

### 02. Dashboard da rede

**O que a tela precisa fazer.** Dar ao Admin Gio (e à agência, sem PII) um pulso da rede: funil, canais, ranking, volume por UF e alertas acionáveis (US5, US1, US7).

**Veredito.** É um dashboard executivo convincente, com alertas que vêm do diagnóstico real (GTM próprio, unidades sem foto, sem coordenadas, GBP fora da canônica). O aviso "Dados de exemplo" no subtítulo é o padrão que o resto do conjunto deveria copiar. O que enfraquece é a cor das variações, um recorte de período contraditório e totais de UF que não fecham 130.

**Achados**

1. **Vale corrigir. Variação verde `#0e9f6e` em branco.** Amostrado no "+14,2% vs. outubro": 3,39:1, abaixo de 4,5:1 para 12 px (medido em `.kpi .d`). Correção: `--verde` proposto `#0B7A54` (5,35:1 em branco).
2. **Vale corrigir. Período.** O chip "Mês" está ativo, o topo mostra "01 a 21 nov 2026" e o subtítulo confirma 01 a 21/11/2026. Não é um mês. Correção: chip "Personalizado" ou "Até hoje", e um único controle de período (o do topo ou o da página, não os dois).
3. **Vale corrigir. "Unidades por estado" não fecha a rede.** Soma visível: 86+8+7+7+4+3+3+2 = 120, com 8 UFs, enquanto o login e a lateral dizem 16 estados e 130 unidades. Correção: exibir as 16 UFs (as menores em "Outros") e um total 130, ou uma barra "demais estados, 10".
4. **Vale corrigir. Ranking da tela 02 versus tela 12.** Aqui Alto da Lapa é 4º (índice 90). No portal do franqueado ela é 7ª. Correção: rotular "Ranking de conversão (índice 0 a 100)" e "Posição geral da unidade", ou usar o mesmo número nos dois lugares na demo.
5. **Detalhe. O KPI "1º contato, 11 min" não tem variação**, ao contrário dos três à esquerda. Incluir "versus mês anterior" ou "versus meta 15 min" no mesmo padrão.
6. **Acerto.** Alertas específicos e clicáveis, donut de origem com total no centro, funil com Volume e Taxa, fonte dos dados no subtítulo.

### 03. Unidades, tabela

**O que a tela precisa fazer.** Listar as 130 unidades com filtros, visões salvas, exportação e entrada no detalhe (US1).

**Veredito.** É a tela mais "sistema" do admin: filtros ricos, visão "Prioridade SEO do mês", completude em barra, alertas por linha, sparklines de leads e Google. A densidade é alta e o tipo dos cabeçalhos não aguenta o recado.

**Achados**

1. **Vale corrigir. Cabeçalho de tabela 11 px em caixa alta**, cor `--tinta-3` `#7d7286` sobre `--lilas-50` `#faf6fb`. Contraste calculado: 4,25:1, abaixo de 4,5:1, ainda por cima em 11 px (medido em `table.t th`). Correção: 12 px, peso 600, cor `#5E5566`, caixa alta opcional.
2. **Vale corrigir. Pills âmbar de alerta** ("GBP fora da canônica", "Poucas fotos", "Sem FAQ", "Texto padrão"). Token `--ambar` `#d98a00` em `--ambar-50` `#fdf3e1`: 2,52:1, insuficiente inclusive para texto grande. Correção: texto `#8A5800` (5,49:1 no mesmo fundo).
3. **Vale corrigir. Há checkboxes por linha e nenhuma barra de ação em lote** (exportar seleção, atribuir, abrir chamado). Ou se tira o checkbox nesta versão, ou se mostra a barra ao marcar a primeira linha.
4. **Detalhe. KPI "Abaixo de 55%" é 46**, mas a legenda do mapa (04) diz 40. "Alertas de SEO 58" e "Alertas de tracking 17" são fortes; só precisam bater com o mapa e com os alertas do dashboard.
5. **Detalhe. Miniaturas iguais** em todas as linhas (`fachada.jpg`). Quebra a leitura de "unidade real".
6. **Acerto.** Paginação "Mostrando 14 de 130, ordenado por completude", troca Tabela e Mapa, domínio próprio versus ficha oficial, e a visão salva visível.

### 04. Unidades, mapa

**O que a tela precisa fazer.** Mostrar o mesmo subconjunto da tabela no mapa, com unidades sem coordenada à parte (US1, critério 3).

**Veredito.** A arquitetura está certa: colorir por completude, inset de Grande São Paulo, card da unidade, lista "Fora do mapa" com "Geocodificar". A silhueta do Brasil, porém, é um polígono único gerado por `mapa_br()` a partir de pontos manuais (`BR` em `gerador/base.py`), sem UFs, com recorte do Norte e do Nordeste irreconhecível. Este é o ponto que mais tira o ar corporativo do conjunto. Ver seção 6.

**Achados**

1. **Vale corrigir (impacto de apresentação equivalente a bloqueio de credibilidade).** Substituir o `polygon` atual por malha oficial simplificada. Proposta concreta na seção 6. Manter inset, zoom, camadas e a lista lateral.
2. **Vale corrigir. Totais da legenda.** "80% ou mais: 31" bate com a tabela. "Abaixo de 55%: 40" não bate com os 46 da tabela. 31+53+40 = 124, não 117 (unidades no mapa) nem 130. Correção: os três intervalos mais "sem completude", somando 117 no mapa e 13 fora.
3. **Detalhe. O mapa local ("Como chegar") das telas 05, 19 e 20** repete o problema em escala menor: cruzamento genérico, sem ruas reais. Tratar com o mesmo plano (mapa de ruas estilizado ou captura de MapLibre/OSM).
4. **Acerto.** "117 unidades com coordenadas. 13 sem coordenadas aparecem na lista ao lado." Copy alinhada à spec. Botão Geocodificar é a ação certa.

### 05. Detalhe da unidade (Admin)

**O que a tela precisa fazer.** Abrir a ficha completa, com campos travados da rede, SEO e GBP, completude, acessos e atalho "Entrar como unidade" (US2, US7).

**Veredito.** Rica e bem pensada: cadeados, "NAP igual ao Google", raio de atendimento, horários em cartões, alerta de GBP, pessoas com acesso. O topo (hero + 11 abas) está no limite do que a largura 1440 aguenta, e o CNPJ 12.345.678/0001-90 ao lado de um endereço real destoa.

**Achados**

1. **Vale corrigir. Onze abas numa faixa só** (Dados e contato, Horários, Tratamentos 12, Fotos 8, Página, Domínio, SEO e Google 1, Integrações, Leads 41, Usuários 3, Histórico). Medido no HTML, todas no `.tabs`. Em 1192 px de conteúdo (1440 menos 248 de lateral, medido em `.app`) o conjunto fica apertado e não prevê overflow. Correção: abas primárias (Dados, Página, SEO, Leads) e um grupo "Mais"; ou rolagem com `scroll-padding-inline` e indicador de que há mais à direita.
2. **Vale corrigir. CNPJ 12.345.678/0001-90** é placeholder clássico, na mesma ficha que usa Av. São Gualter, 53 (endereço real da unidade no GBP do projeto). Ver seção 5. Correção: CNPJ com máscara visível do tipo 00.000.000/0000-00 e selo "exemplo", ou um número claramente reservado para demonstração.
3. **Vale corrigir. CEP 05071 000 e telefones (11) 3832 4410 e (11) 94587 2210** não conferem com o GBP da mesma unidade (CEP 05455-000, telefone +55 11 99614-6446). O domínio `gioaltodalapa.com.br` é o oficial. Correção na seção 5.
4. **Detalhe. Mapa de coordenadas** (-23,5361, -46,7203) é só duas vias esquemáticas. Se a coordenada existe, um recorte real de mapa muda o nível da tela.
5. **Detalhe. Badge de tratamentos 12 aqui versus 6 no franqueado.** Escrever "6 publicados, 12 no catálogo" nos dois lados.
6. **Acerto.** Campos com cadeado, "Entrar como unidade", "Salvar alterações" e a checklist de completude com o item vermelho do GBP.

### 06. Aprovações

**O que a tela precisa fazer.** Fila de mudanças com diff, regras da marca e decisão (US3, critérios 3 e 4).

**Veredito.** É uma das telas mais impressionantes e já está pronta para a apresentação. O lado a lado "Publicado hoje" e "Proposta da unidade", o destaque do trecho novo, o alerta de "Resultados garantidos" e a galeria com Mantida, Removida e Nova mostram um produto de governança, não um CMS solto.

**Achados**

1. **Vale corrigir. Alerta "1 termo para revisar"** e o box âmbar usam a paleta que falha em 2,52:1. Aplicar o token de atenção proposto. O conteúdo do aviso é excelente e deve permanecer.
2. **Detalhe. As cinco miniaturas da galeria** são a mesma fachada, o que enfraquece o próprio recurso de "foto nova versus removida". Variar as imagens.
3. **Detalhe. Falta o estado "fila vazia"** e o estado "devolver com nota" (campo de nota aberto). Um dos dois, num frame extra, fecha o fluxo na demo.
4. **Acerto.** Meta "responder em até 1 dia útil", checklist automático (preço, marca de equipamento, NAP, fotos 1600 px) e histórico de versões com responsável.

### 07. Central de leads, kanban

**O que a tela precisa fazer.** Operar leads da rede e da unidade, com origem, fila, SLA e sincronização DocBiz (US4, US8 não, US4).

**Veredito.** O quadro está claro, os cards carregam tratamento, origem, unidade e relógio de SLA, e os KPIs de fila (call center versus unidade, DocBiz, mediana) são os certos. O estado da tela, porém, se contradiz: o filtro "SLA: estourado" está ligado e o quadro não parece filtrado.

**Achados**

1. **Vale corrigir. Filtro ativo versus dados.** Chip `.chip.on` "SLA: estourado" (medido no HTML). Colunas: 38+61+112+74+29 = 314 cards no recorte, com "Ver mais". O KPI diz "9 fora do SLA agora". Na walkthrough isso aparece imediatamente. Correção: ou desligar o chip (estado "Fila: Todas"), ou reduzir o quadro aos 9 estourados e alinhar os totais das colunas.
2. **Vale corrigir. Dois recortes de tempo.** Topo "01 a 21 nov 2026" e chip "Últimos 7 dias". Um só deve governar a tela.
3. **Vale corrigir. Relógios de SLA em pill verde e âmbar**, 11 px (medido em `.pill`). Verde em `--verde-50` 3,06:1; âmbar 2,52:1. Aplicar os tokens novos. O vermelho de "41 min" em Juliana P. precisa permanecer óbvio, com contraste de texto ≥ 4,5:1.
4. **Detalhe.** Não há coluna ou estado "sem cards" nem a vista Lista (o interruptor existe, a tela não foi desenhada). A vista lista ajuda call center em volume alto e merece um frame.
5. **Acerto.** Distinção Unidade versus Call center no card, "Regras de distribuição", e SLA em minutos na coluna Novo.

### 08. Detalhe do lead

**O que a tela precisa fazer.** Mostrar jornada, origem (UTM), status DocBiz, consentimento e ações (WhatsApp, ligar, transferir), com PII mascarado para quem não tiver o evento de auditoria (US4, US10).

**Veredito.** A melhor tela de produto do pacote. Máscara de telefone e e-mail, aviso de auditoria, linha do tempo do anúncio ao agendamento, tabela UTM, stepper DocBiz e cartão de consentimento (versão, IP, retenção). Quase não há o que bloquear.

**Achados**

1. **Detalhe. Horários da jornada em 11 ou 12 px muted** (11 px aparece no HTML desta tela). Subir para 12 px e escurecer se o muted permanecer no limite.
2. **Detalhe. "Fechou pacote"** no stepper não está no enum da spec (`novo`, `contatado`, `agendado`, `compareceu`, `nao_compareceu`, `perdido`). Ou entra no modelo, ou vira um evento de negócio fora do status do lead, para não prometer um CRM que a spec deixou na DocBiz.
3. **Detalhe.** O WhatsApp da unidade aparece aberto na jornada: (11) 94587 2210. É o mesmo número inventado da ficha. Se a PII do lead está mascarada, o telefone da unidade pode aparecer, mas deve ser consistente com a ficha oficial.
4. **Acerto.** "Dados mascarados. Ver completo fica registrado na auditoria." Este padrão deveria ser citado na apresentação. Consentimento com "Retenção até 19/11/2028" e versão LGPD v3 é o nível corporativo que a meta pede.

### 09. Relatórios

**O que a tela precisa fazer.** Montar, salvar, agendar e exportar relatórios no escopo de cada papel, com cuidado de PII (US8, US10).

**Veredito.** A biblioteca, o construtor (linhas, colunas, métrica), a agenda por destinatário e o aviso de exportação com dados pessoais estão no tom certo. O gráfico e a tabela não falam a mesma métrica, e as linhas de SP, PR e MG quase se sobrepõem.

**Achados**

1. **Vale corrigir. Gráfico versus tabela.** O título do gráfico é "Taxa de agendamento sobre leads (%)", eixo até 70. A tabela lista volumes (SP junho 980, novembro 1.530). Correção: ou a tabela passa a taxa, ou o gráfico passa a volume, e o título acompanha.
2. **Vale corrigir. Variação "+58%" em verde** no mesmo token 3,39:1. Aplicar `#0B7A54`.
3. **Detalhe. Só SP, PR e MG no gráfico**, enquanto a tabela inclui GO e RS. Ou se plotam todos, ou a tabela filtra o mesmo recorte.
4. **Detalhe. Os números mensais de SP (980 a 1.530 agendamentos)** parecem operação real. O aviso de "dados de exemplo" não está nesta tela. Ver seção 5.
5. **Acerto.** "Cada pessoa recebe só os dados que o perfil permite ver." Agenda com Diretoria Salus, franqueados, call center e agência. Aviso de que a planilha com telefone só sai com permissão e link que expira em 24 h.

### 10. Suporte

**O que a tela precisa fazer.** Fila de tickets da unidade para a Gio, artigo sugerido, SLA e verificação ligada ao domínio (US9).

**Veredito.** Inbox clássica bem executada, com um ticket de DNS que demonstra o produto (domínio próprio + base de conhecimento + checagem A, CNAME, SSL, 301). A aba "Abertos" não deveria listar tickets resolvidos.

**Achados**

1. **Vale corrigir. Aba "Abertos 12" contém #1475 e #1474 com pill "Resolvido".** Correção: resolvidos só na aba Resolvidos; o item selecionado, se resolvido, não permanece na lista de abertos.
2. **Vale corrigir. Pills "Em andamento" e "Aguardando unidade"** na paleta âmbar e lilás. Aplicar tokens novos; "Urgente" e "Resolvido" precisam passar de 4,5:1 em 12 px.
3. **Detalhe.** O endereço citado no fio, `gioasasul.com.br`, merece uma revisão de grafia (unidade Asa Sul). É o tipo de detalhe que um franqueado da rede aponta na hora.
4. **Acerto.** Artigo sugerido "útil para 92% de quem leu", composer com Responder e Nota interna, atalho `/` para artigo, e o bloco de verificação automática do domínio.


### 11. Usuários e permissões

**O que a tela precisa fazer.** Expor matriz de papéis, 2FA, auditoria do dia e o caminho para solicitações LGPD (US10).

**Veredito.** É a tela que mais comunica "corporativo". A matriz (Admin, Marketing, Call center, Agência, Multifranqueado, Franqueado, Recepção), os quatro princípios (isolamento por unidade, dado mascarado, 2FA, acesso que expira) e o log "Ingrid N. exportou 2.986 leads" são exatamente o que a apresentação precisa. A leitura dos ícones da matriz e o tipo pequeno pedem ajuste. As abas "Solicitações LGPD 2" e "Segurança" não têm tela desenhada.

**Achados**

1. **Vale corrigir. Cabeçalhos e legendas em 10 e 11 px** (10 px medido em inline desta tela; th 11 px no CSS). A matriz só funciona se a legenda "Tudo, Ler, Próprias, Fila, Não" for imediatamente legível. Correção: 12 px, ícones com rótulo textual na primeira visualização ou um `title` visível no hover, e um pouco mais de largura nas colunas Call center e Multifranqueado, que já aparecem abreviadas.
2. **Vale corrigir. A aba "Solicitações LGPD 2" é um compromisso da spec (US10, critério 3) sem tela.** Ver seção 9. Na apresentação, clicar nessa aba e cair em branco é pior do que omitir o badge.
3. **Detalhe. Arquitetura da auditoria.** Existe item "Auditoria" na lateral, botão "Auditoria completa" e o card "Auditoria de hoje". Três entradas para a mesma coisa. Correção: o card permanece como pulso; o botão abre a tela cheia; o item de menu pode ser o mesmo destino, sem página-irmã vazia.
4. **Detalhe. Juliana M. com 2FA "Não" em pill âmbar**, 2,52:1. Além da cor, o estado "Recepção sem 2FA" é um bom gancho de produto (a spec exige 2FA para admin, não para recepção). Deixar o critério visível: "obrigatório para Rede Gio, call center e agência".
5. **Acerto.** 214 pessoas, 2FA visível por linha, exportação de PII no log, convite na primária.

### 12. Dashboard do franqueado

**O que a tela precisa fazer.** Mostrar o pulso da unidade, posição no ranking (sem números nominais das outras), origem, SLA e o que falta para subir (US5, critério 2).

**Veredito.** Cumpre a spec com elegância: "Bom dia, Renata. Sua unidade está em 7º na rede.", régua de 130º a 1º com a mediana marcada, comparação com a rede em cada KPI ("melhor que 82% da rede"), e a lista "Para subir no ranking" com ganho em pontos. É o cartão de visitas do portal claro. O contraste da lateral e do degradê ativo é o que impede de chamar a tela de pronta.

**Achados**

1. **Bloqueio. Rótulos de seção da lateral** "MINHA OPERAÇÃO", "CLIENTES", "APOIO": `#b59ac0` em branco, 2,52:1 (calculado no token; 10 px medido em `.side .sec`). Ilegível para texto pequeno. Correção: `#6B4E78` (7,03:1) e 11 px.
2. **Bloqueio. Item ativo "Início".** Degradê `#b0197e` a `#e5559f`. Branco amostrado à esquerda do item sobre `#d06bac`: 3,29:1; à direita sobre `#e479b3`: 2,73:1; no ponto médio sobre `#c94e9b`: 4,16:1. Nenhum atinge 4,5:1. Correção: fundo sólido `#b0197e` ou degradê que não clareie além de `#b0197e`.
3. **Vale corrigir. Ícones inativos da lateral** `#a58bb1` em branco: 3,03:1, abaixo de 3:1 exigido para gráfico de interface. Correção: `#6B4E78` ou `--tinta-2`.
4. **Vale corrigir. Posição 7º aqui versus 4º no admin**, já citado. E o gráfico "Seus leads e agendamentos" com eixo 0 a 5 deixa o traço serrilhado, com cara de volume baixo demais para o discurso de "rede robusta". Se 41 leads no recorte é o dado da demo, o eixo pode ir a 8 ou 10, com média móvel, para o desenho respirar.
5. **Detalhe. Canais 46% + 32% + 22% = 100%**, sem "outros", enquanto o admin tem seis origens. Uma fatia "Outros" alinha os dois mundos.
6. **Acerto.** CTAs "2 leads esperando" e "Completar página" no hero, comparação com a mediana da rede, e tarefas com "+2 pts", "+3 pts", "+4 pts". Não exibe o nome das outras unidades no ranking, como a spec pede.

### 13. Minha unidade

**O que a tela precisa fazer.** O franqueado edita o que pode, vê o que a rede trava, acompanha completude e o que está em aprovação (US2).

**Veredito.** Clara, com o foco certo: WhatsApp em estado de foco, teste enviado, texto "Sobre" com contagem 312 de 600 e selo "Dentro das regras da marca", toggles de tratamento, Ultraformer "Pede aprovação", card "Em aprovação" e regras da marca visíveis. É o par perfeito da tela 06.

**Achados**

1. **Vale corrigir. Mesmos NAP e Instagram** `@gioaltodalapa` ao lado de e-mail `@exemplo.com.br`. O campo Instagram parece conta real. Aplicar a regra da seção 5.
2. **Vale corrigir. "Tratamentos 6" e checklist "6 tratamentos"** contra "12" no admin. Correção: "6 ligados, 6 do catálogo ocultos" ou equivalente.
3. **Detalhe. O Ultraformer com "Pede aprovação"** é uma ótima demonstração da regra "sem marca de equipamento". Na apresentação, vale abrir essa linha. O pill âmbar precisa do token novo.
4. **Detalhe. Abas Fotos, Equipe, FAQ e Avaliações** não foram desenhadas. Pelo menos Fotos (upload com estado "aguardando aprovação", US2 critério 3) e FAQ (faltam 3, ganho de completude) merecem um frame, porque o dashboard promete esses ganhos.
5. **Acerto.** "Nome, endereço e CNPJ só a rede altera." "Sugerir texto com bairros próximos." "1 alteração em aprovação" no topo. O cursor no texto mostra o estado de edição sem esforço.

### 14. Escolha de template

**O que a tela precisa fazer.** Oferecer A, B e C com preview, métrica de qualidade e troca com aprovação (US3).

**Veredito.** A lógica de produto está madura: nomes certos (Conversão direta, Vitrine da clínica, Autoridade local), métricas ("Maior taxa de envio na rede: 8,4%", "Mais tempo na página: 2 min 31 s", "Mais visitas orgânicas: +34%"), recomendação personalizada e interruptores Computador e Celular. A execução visual não está no mesmo nível: A e C são wireframes, só B tem foto porque está "Em uso". Ver seção 7.

**Achados**

1. **Vale corrigir. Miniaturas A e C em fidelidade de diagrama**, enquanto o restante do sistema já parece produto. Na apresentação, isso comunica "dois templates ainda não existem". Correção: capturas das landings cheias (seção 7), no mesmo recorte da miniatura de B.
2. **Detalhe. O interruptor Computador / Celular** não tem estado celular desenhado. Um segundo recorte das três miniaturas em 390 px fecha a história.
3. **Detalhe. "Comparar A e B"** é um botão sem tela. Um comparativo lado a lado (formulário primeiro versus foto primeiro) seria uma das peças mais fortes da demo.
4. **Acerto.** A recomendação usa dados da unidade ("8 fotos e nota 4,9") e não empurra o A só porque converte mais. Isso é discurso de rede, não de agência empurrando template único.

### 15. Editor da landing

**O que a tela precisa fazer.** Editar bloco a bloco, com preview, blocos fixos, validador de marca e envio para aprovação (US3).

**Veredito.** O três painéis (lista, preview, inspetor) estão corretos. Cadeado "Fixo" no topo, na faixa de confiança e no rodapé, "Auto" em avaliações e como chegar, "Opcional" em equipe, e a "Verificação da marca" com Lighthouse estimado 93 são o tipo de detalhe que surpreende. O preview ainda mostra quatro vezes a mesma foto, e o modelo B não tem uma landing cheia de referência.

**Achados**

1. **Vale corrigir. Preview do modelo B** deveria corresponder a uma página B real (seção 7). Hoje o preview é um recorte híbrido, com formulário no hero (cara de A) e bloco Sobre em edição.
2. **Vale corrigir. Galeria no preview com quatro fotos idênticas.** Mesmo problema da fachada única.
3. **Detalhe. "arraste" na lista de blocos** não tem handle visível nem estado de arraste. Um handle de 12 a 16 px à esquerda de cada item deixa a affordance explícita.
4. **Detalhe. Aviso "Lighthouse estimado 93, 1 foto pesada"** é ouro para a meta SC-006 (≥ 90 no mobile). Manter, talvez com o peso estimado em KB.
5. **Acerto.** "Rascunho salvo há 12 segundos." Paleta de fundo limitada às cores da marca. Enviar para aprovação como primária, não "Publicar agora".

### 16. Domínio próprio

**O que a tela precisa fazer.** Guiar DNS, SSL, verificação e estratégia de canonical, com o ajuste do GBP (US6, US7).

**Veredito.** Outra tela pronta para a apresentação: stepper de 5 passos, tabela A / CNAME / TXT, "Verificado há 14 min", o recado "Seus outros e-mails continuam funcionando" (não mexemos no MX) e o card "Como fica no Google" com canônico e 301 da ficha da rede. O aviso de que o perfil no Google Maps ainda aponta para o endereço antigo é exatamente o alerta da spec.

**Achados**

1. **Vale corrigir. O IP `76.76.21.21` é um anycast real da Vercel.** Em uma demo, isso é verossímil e útil, mas deve entrar na lista de dados que parecem oficiais (seção 5), com a observação de que não é o IP de uma unidade específica.
2. **Detalhe. Passo 5 "Publicar ao vivo" e o botão "Publicar no domínio"** dizem a mesma ação com nomes diferentes. Unificar a copy.
3. **Detalhe. Falta o estado de falha** (CNAME incorreto, SSL pendente), que a tela 10 já sugere no ticket. Um frame "verificação falhou" com o passo vermelho e o valor esperado versus o encontrado deixaria o assistente completo.
4. **Acerto.** "Uma URL oficial por unidade, nunca duas." "Pedir para a rede ajustar" no GBP. "Passo a passo" e "Pedir ajuda" no topo.

### 17. Leads no celular (390 CSS px, captura 2x)

**O que a tela precisa fazer.** Deixar a recepção responder leads no telefone, com SLA, WhatsApp e ligação (US4).

**Veredito.** Hierarquia certa: alerta "2 leads esperando", chips de fila, cards com ação primária só enquanto o lead espera, tab bar clara. Medidas abaixo já estão em CSS px (pixels do PNG divididos por 2). O botão WhatsApp falha contraste no extremo do degradê, e há uma quebra de linha estranha no primeiro card.

**Achados**

1. **Vale corrigir. Botão WhatsApp** em degradê magenta/rosa, texto branco. Amostrado no PNG 2x e convertido: no meio do botão, branco sobre `#c6328b` com 4,67:1 (passa); à direita, branco sobre `#de4e9b` com 3,56:1 (falha). Correção: mesmo ajuste do botão primário do franqueado, degradê limitado a `#b0197e`, ou fundo sólido.
2. **Vale corrigir. Quebra "Orgânico ·" / "página"** no card de Beatriz L. (visível no PNG). Parece um termo cortado ("página da unidade" ou origem mal rotulada). Correção: uma linha, com `ellipsis` se faltar espaço, ou a origem só como "Orgânico".
3. **Detalhe. Badge da lateral no desktop é 8, o chip "Todos" é 9.** Alinhar. Os chips não cobrem Agendado e Perdido; se "Todos 9" inclui esses estados, os chips deveriam somar 9 ou haver um "Mais filtros".
4. **Detalhe. Tab "Agenda"** aponta para um território que a spec deixou na DocBiz. Se o item existe, precisa de uma tela ou de um deep link explícito ("Abre a agenda DocBiz"). Senão, "Mais" absorve.
5. **Acerto.** WhatsApp e Ligar só nos leads que pedem ação agora. Mariana (já agendada) e Fernanda (em contato) vão para o detalhe, sem duplicar o CTA. Alerta de SLA no topo com a mediana do dia (8 min).

### 18. Lead no celular

**O que a tela precisa fazer.** Abrir o lead com ações (WhatsApp, ligar, nota), próximo passo e jornada, em uma mão.

**Veredito.** Compacta com clareza, e a jornada reduzida funciona. O problema grave é físico: a barra inferior cobre o final do card da jornada.

**Achados**

1. **Bloqueio. Card da jornada cortado pela tab bar.** Medido na faixa inferior do PNG (780×1688, escala 2x): o canto inferior do card e a continuação da linha do tempo desaparecem sob Início, Leads, Agenda, Avaliações e Mais. No desktop a jornada tem mais eventos (confirmação DocBiz, avaliação agendada). Correção: `padding-bottom` do conteúdo ≥ 56 px CSS da tab bar, mais a safe area do iOS (proposto 34 px em aparelhos com home indicator), e a lista da jornada rolável por inteiro. A tab bar deve ter fundo opaco e sombra, não sobrepor o card.
2. **Detalhe. O título da barra é só "Lead".** Usar o nome ("Mariana S.") reduz o salto entre lista e detalhe.
3. **Detalhe.** Telefone e e-mail não aparecem (no desktop estão mascarados). Está correto se Ligar e WhatsApp disparam o app nativo. Uma linha "Toque em Ligar para usar o número. O acesso fica na auditoria." alinha com a tela 08.
4. **Acerto.** Próximo passo "Avaliação sáb. 22/11 · 15:30" no bloco em degradê, com o lembrete de WhatsApp. Pills de status, origem e SLA no topo do card.

### 19. Landing pública, template A, desktop

**O que a tela precisa fazer.** Converter visita em avaliação (formulário na primeira tela), com NAP, prova social e FAQ, no modelo "Conversão direta" (US3, SC-006).

**Veredito.** A hierarquia de conversão está certa: formulário à direita, H1 52 px (medido), telefone no header, faixa de confiança, tratamentos, avaliações, como chegar e FAQ. É uma landing de rede, não uma home genérica. Os dois furos que mais importam: o aceite de privacidade já vem marcado, e o NAP da GiO Batel é o real (telefone (41) 3076 6107 e endereço conferidos no GBP do projeto) com uma contagem de avaliações que não é a do GBP (290 na tela, 775 no GBP).

**Achados**

1. **Bloqueio. Consentimento pré-marcado.** O check está desenhado como SVG sempre visível, no desktop e no mobile. Correção: caixa vazia de 20 px, botão "Quero agendar" inativo ou com erro até o aceite, e o aviso de privacidade como link. Sem isso, a landing ensina o padrão errado numa rede que faz questão de LGPD no painel.
2. **Vale corrigir. NAP real com métrica inventada.** Telefone (41) 3076 6107, Rua Deputado Antônio Baby, 63, CEP 80240 370 conferem com o GBP "GiO Batel". A nota 4,8 confere; "290 avaliações" não (GBP: 775). WhatsApp (41) 98477 6619 não está no campo de telefone do GBP. Instagram `@giobatel` parece conta real. Correção na seção 5. Na apresentação, um cliente da unidade reconhece o endereço e questiona o 290.
3. **Vale corrigir. Mapa "Como chegar"** é um esquema de vias, não um mapa. O botão "Abrir no Google Maps" salva o uso, mas a área (estimada em cerca de 560×280 CSS px no desktop) é um dos primeiros lugares que o olho busca. Usar recorte real ou estilo MapLibre nas cores da marca.
4. **Detalhe. FAQ aberto usa um X**, os fechados usam chevron. X significa fechar a página, não recolher. Correção: chevron para cima no item aberto, para baixo nos demais, alvo 40 px.
5. **Detalhe. Subtítulo do hero.** Amostrado no PNG: `#f2ebf1` sobre fundo aproximado `#7d397a`, 6,55:1, passa. Rótulos "TRATAMENTOS" em magenta `#b0197e` (primeiro pixel amostrado) sobre o fundo claro: o token magenta em branco é 6,39:1, passa. Manter magenta, não rosa, nesses rótulos.
6. **Acerto.** Formulário curto (nome, WhatsApp, tratamento), CTA "Quero agendar", "avaliação gratuita" repetida com consistência, e o rodapé com aviso de privacidade e "Outras unidades GiO".

### 20. Landing pública, template A, mobile (390 CSS px, captura 2x)

**O que a tela precisa fazer.** O mesmo que a 19, no telefone, com o formulário ainda na primeira rolagem (US3, SC-006).

**Veredito.** A adaptação é fiel e boa: "Agendar" no header, hero legível, formulário logo abaixo, faixa de confiança em grelha 2×2, tratamentos em lista, avaliações, mapa, FAQ e rodapé. Dois buracos de paridade com o desktop e o mesmo consentimento marcado.

**Achados**

1. **Bloqueio. Mesmo consentimento pré-marcado** da tela 19. A mesma correção.
2. **Vale corrigir. Paridade de tratamentos.** O desktop lista seis (Depilação, Limpeza, Criolipólise, Bioestimulador, Microagulhamento, Peeling). O HTML e o PNG mobile param em quatro (os dois últimos não existem no `20-landing-publica-mobile.html`). Correção: os seis, na mesma ordem.
3. **Vale corrigir. "Seus dados seguros"** quebra em três linhas (Seus dados / seguros / LGPD), enquanto os outros três itens da grelha ficam em duas. Correção: "Dados protegidos" + "LGPD", ou ícone + uma linha de título e uma de apoio, com altura fixa de card.
4. **Vale corrigir. Mapa esquemático e NAP real**, iguais à 19. O recorte mobile do mapa (quase quadrado no PNG) deixa o esquema ainda mais evidente.
5. **Detalhe.** A página é longa (7110 px de captura 2x, cerca de 3555 px CSS). Não é um problema por si, mas um CTA "Agendar" persistente após o formulário sair da tela evitaria a subida até o header. Proposto: barra fixa de 56 px com "Agendar avaliação" depois que o hero sai do viewport, sem cobrir o campo em foco.
6. **Acerto.** H1 32 px (medido), formulário na primeira tela, botão "Agendar" no header, e a mesma ordem de seções do desktop.


## 5. Números fictícios que parecem reais

O dashboard 02 já acerta o tom com "Dados de exemplo, período de 01 a 21/11/2026". Esse selo não se repete nas landings, nas fichas, nos relatórios nem no domínio. Pior: unidades reais da rede entram na demo com parte do NAP oficial e parte inventada. Abaixo, o que conferi no `gbp-gio.csv` do próprio projeto (fonte aberta neste workspace, não chute).

Regra proposta para a apresentação: um selo persistente "Dados ilustrativos" no canto do painel (admin e franqueado) e uma faixa discreta no rodapé das landings de demo. Se a unidade for real, NAP e GBP saem iguais aos oficiais, ou a unidade é trocada por uma ficha 100% fictícia (nome, rua, telefone 0000, e-mail @exemplo.com.br, nota redonda). Não misturar os dois.

| Tela | Dado | Situação | Como sinalizar |
|---|---|---|---|
| 02, 03, 09, 11 | 2.986 leads, 1.733 agendados, 1.071 comparecimentos, exportação de 2.986 leads | Inventados, verossímeis. Só o 02 declara "dados de exemplo". | Selo global no painel. No 09, repetir a fonte no título da prévia. |
| 02, 03, 12 | Alertas 17 GTM, 70 sem foto, 13 sem coordenadas, 3 GBPs | Vêm do diagnóstico real da rede. Parecem (e provavelmente são) números de operação. | Se forem reais, dizer "situação atual da rede, 21/11/2026". Se a apresentação for externa ou ampla, arredondar e marcar como ilustrativo. |
| 02 vs 12 | Ranking 4º (índice 90) versus 7º na rede | Dois números oficiais demais para discordarem. | Unificar ou nomear as métricas. |
| 05, 13 | Av. São Gualter, 53, Villa Ida, domínio gioaltodalapa.com.br, nota 4,9 | Endereço e domínio conferem com o GBP. O GBP registra Alto de Pinheiros, CEP 05455-000, telefone +55 11 99614-6446, 231 avaliações. | A tela usa CEP 05071 000, telefones (11) 3832 4410 e (11) 94587 2210, 312 avaliações. Ou se alinha ao GBP, ou se fictionaliza o endereço. |
| 05 | CNPJ 12.345.678/0001-90 | Placeholder óbvio ao lado de um endereço real. | Máscara 00.000.000/0000-00 com selo "exemplo", nunca este clássico. |
| 05, 13, 01 | E-mails `@exemplo.com.br` | Claramente fictícios. Manter. | Padrão a seguir nos telefones. |
| 08 | Lead #L-20031, ID DocBiz 88231, gclid, telefone mascarado | Bem resolvido. O gclid parece real, o que é adequado numa demo, desde que o painel esteja selado como ilustrativo. | Sem mudança, com o selo global. |
| 16 | IP 76.76.21.21, CNAME `unidades.gio.com.br`, TXT `gio-un-4127-8f2a` | O IP é anycast real da Vercel. O restante é plausível. | Adequado para demo de DNS. Manter e cobrir com o selo global, sem pretender que o domínio já esteja no ar. |
| 19, 20 | (41) 3076 6107, Rua Deputado Antônio Baby, 63, CEP 80240 370, nota 4,8 | Telefone, endereço e CEP conferem com o GBP "GiO Batel". Nota 4,8 confere. | "290 avaliações" não confere (GBP: 775). WhatsApp (41) 98477 6619 não está no telefone do GBP. `@giobatel` parece conta real. Alinhar 775 e o WhatsApp oficial, ou trocar a landing de demo para uma unidade fictícia. |
| 12, 13, 17 | 41 leads, 27 agendados, 8 min, 312 avaliações | 312 avaliações da Alto da Lapa não conferem com as 231 do GBP. | Se a unidade é real, usar 231. Se é demo, usar um número redondo e o selo. |
| 10 | Ticket #1482, prazos "hoje às 18:00" | Verossímil e bom para a história. | Coberto pelo selo global. |
| 07 | Nomes Mariana S., Beatriz L., etc. | Primeiro nome e inicial: bom padrão de demo. Manter. | Não completar sobrenomes. |

Copy proposta para o selo do painel: "Ambiente de demonstração. Números e pessoas são ilustrativos, salvo quando a fonte é citada (ex.: Google da unidade)." Copy proposta para a landing de demo: "Página de demonstração do sistema de unidades Gio. Alguns dados podem ser ilustrativos."

## 6. Mapa do Brasil: alternativa ao desenho à mão

Hoje `gerador/base.py` define `mapa_br()` e projeta um polígono `BR` de pontos manuais num `viewBox` 0 0 700 700, preenchido com `#f3eaf6` e traço `#d9c3e1`. Não há UFs, ilhas nem recorte reconhecível do Norte e do Nordeste. Os pontos das unidades, o inset de Grande São Paulo e a lista "Fora do mapa" já são a arquitetura certa e devem permanecer.

**Recomendação (mocks e produto).**

1. **Nos mocks, trocar o polígono por um SVG oficial simplificado.** Fonte: Malhas Territoriais do IBGE (UF, ano mais recente disponível), dado aberto. Simplificar com Mapshaper (Visvalingam, cerca de 2% a 5% dos vértices) até a silhueta ficar leve e ainda inconfundível (Norte largo, recorte de PE/AL/SE, cabeça de SP e RJ, Sul em V). Exportar um SVG com 27 paths de UF (id `BR-SP`, etc.) mais o contorno. Pintar as UFs por completude média quando o filtro "Colorir por: Estado" estiver ativo; no modo atual (completude por unidade), o fundo das UFs fica neutro e os pontos continuam por cima. Crédito discreto: "Malha: IBGE".
2. **Não recomendo cartograma de tiles por UF como vista principal.** O admin precisa reconhecer o território e a concentração em São Paulo. O inset de Grande São Paulo já resolve a densidade. Um cartograma pode ser uma camada opcional depois, não o mapa da demo.
3. **No produto, MapLibre GL JS com estilo claro na paleta Gio** (fundo `#fbf8fc`, água branca, limites de UF em `#d9c3e1`) e agrupamento de pontos (cluster) até o zoom 7 ou 8. A mesma base serve para o recorte "Como chegar" das fichas e das landings, com um pin e o botão que já existe para o Google Maps. Protomaps ou tiles próprios evitam chave de provedor na demo.
4. **Unidades sem coordenada** continuam fora do desenho, na lista "Fora do mapa", com Geocodificar. Esse padrão já está alinhado à spec e é melhor do que inventar um ponto.

Esforço do item 1 (SVG estático nos mocks): baixo, e é o que mais muda a percepção na apresentação. O item 3 pode vir na implementação.

## 7. Modelos B e C da landing, saindo da miniatura

Só o modelo A tem página cheia (telas 19 e 20). B aparece como miniatura com foto porque está "em uso" na Alto da Lapa; C é um diagrama. Para sair desse estágio, cada modelo precisa de um desktop 1440 e um mobile 390 no mesmo grau de acabamento do A, mais as miniaturas da tela 14 e o preview do editor 15 gerados a partir dessas páginas, não de retângulos.

A diferença tem que ser visível em três segundos, não só no texto de apoio.

**A. Conversão direta** (já desenhado, manter). Formulário na primeira tela, hero com overlay da marca, faixa de confiança curta, tratamentos em cards com ícone, avaliações, como chegar, FAQ. Objetivo: taxa de envio. O que já está medido na tela 14 ("8,4% de envio") deve continuar sendo a métrica de escolha.

**B. Vitrine da clínica** (prioridade, é o "em uso" da demo). A foto da fachada é o herói, com overlay bem mais leve (opacidade proposta 0,20 a 0,30, não o véu magenta do A). Na primeira tela: nome da unidade, nota do Google, e um botão "Agendar", sem o formulário completo. Em seguida, galeria de 6 a 8 fotos (fachada, recepção, sala, equipe), bloco da equipe com foto, cargo e registro, tratamentos com foto real e não só ícone, avaliações, e só então o formulário, ou um formulário fixo à direita no desktop depois da dobra. Objetivo: tempo na página e confiança. Métrica já anunciada: "2 min 31 s".

**C. Autoridade local.** Abre com mapa do raio de atendimento e os bairros (o componente "Raio de atendimento" da tela 05, em versão pública), H1 com o bairro e a cidade, bloco "Atendemos Vila Ida, Alto de Pinheiros, Lapa..." e FAQ local longo (estacionamento, como chegar, convênios, primeira avaliação). Avaliações do Google em destaque no primeiro terço. Formulário persistente no desktop (coluna) e barra "Agendar" no mobile. Objetivo: visita orgânica e GBP. Métrica já anunciada: "+34% visitas orgânicas".

Blocos comuns (travados nos três): marca e logo, rodapé legal, formulário, aviso de privacidade. Blocos que diferenciam: posição do formulário, peso da galeria, equipe, mapa e tamanho do FAQ. O editor (15) já tem Fixo, Editável, Auto e Opcional: basta refletir o conjunto de blocos de cada modelo.

Para a apresentação, o mínimo viável é: B desktop + B mobile, e uma miniatura fiel de C no desktop. O ideal é B e C nos dois recortes, mais o estado "Comparar A e B" prometido na tela 14.

## 8. O que tornaria o conjunto mais impressionante na apresentação

Ordenado por impacto sobre esforço, só o que é viável com o que já existe.

1. **Mapa oficial clicável no dashboard da rede (alto impacto, esforço médio).** A tela 02 ganha um Brasil correto no lugar (ou ao lado) de "Unidades por estado". Clique numa UF filtra a tabela 03. É a imagem que a diretoria leva embora.
2. **Landings B e C em fidelidade de produção (alto, esforço médio).** Fecha o buraco mais visível depois do mapa e demonstra os três produtos que a spec vende.
3. **Selo de demonstração e dados alinhados ao GBP (alto, esforço baixo).** Evita o momento em que alguém da rede reconhece a unidade e aponta o número errado. Esforço pequeno, risco grande se não for feito.
4. **Comparativo A e B (alto, esforço baixo a médio).** A tela 14 já promete o botão. Dois recortes lado a lado (formulário primeiro versus foto primeiro) tornam a escolha de template uma decisão, não um catálogo.
5. **Estado vazio e estado com poucos dados (alto, esforço baixo).** Uma unidade nova em 28% de completude, um kanban com a coluna Novo vazia no primeiro dia, um suporte sem tickets. Mostra que o sistema foi pensado além do "preenchido com dados bonitos".
6. **Diff visual antes e depois na aprovação (médio a alto, esforço médio).** A tela 06 já tem o texto lado a lado. Um interruptor "Ver na página" com as duas versões da landing (ou um controle de arraste) eleva a governança ao nível que a meta pede.
7. **Histórico do ranking no portal do franqueado (médio, esforço baixo).** A régua 7º com mediana já é ótima. Uma linha de 90 dias da posição ("saiu do 15º para o 7º") transforma o gamification em trajetória.
8. **Central de notificações a partir do sino (médio, esforço baixo).** O ponto rosa já existe no topo. Um painel com "9 leads fora do SLA", "7 aprovações" e "GBP fora da canônica" amarra o dashboard aos fluxos.
9. **Mapa real em "Como chegar" (médio, esforço médio).** Nas telas 05, 19 e 20. Pouca linha de código nos mocks (uma captura estilizada basta), muita percepção de produto acabado.
10. **Modo escuro opcional só no admin (baixo a médio impacto, esforço médio).** A lateral já é escura; estender o canvas para um "centro de comando" agrada a quem vive no painel. Não é prioridade para a primeira apresentação, é um "extra" se houver tempo depois dos itens 1 a 6. Não aplicar no portal do franqueado nem na landing.

Microinterações que cabem nos mocks ou num protótipo curto, sem virar projeto: anel de SLA que muda de verde para âmbar e vermelho no card; o "rascunho salvo há 12 segundos" já existente no editor, repetido em Minha unidade; foco visível de 2 px em `--magenta` nos campos (a tela 13 já sugere o anel no WhatsApp).

## 9. Telas que faltam

Ligadas à spec e ao inventário em `telas.md`. Prioridade em função da apresentação e do risco de clicar num item já desenhado no menu e não ter destino.

**Prioridade 1 (existem no menu, na spec P1, ou quebram a demo se alguém clicar)**

| Tela | Papel | O que faz | Ligação |
|---|---|---|---|
| Desafio de 2FA e "esqueci a senha" | Todos, com 2FA obrigatório no admin | Fechar o fluxo da tela 01. | US10, critério 1 |
| Solicitações LGPD (titular) | Admin | A aba já tem badge 2: localizar, exportar e anonimizar o lead. | US10, critério 3; FR-012 |
| Auditoria completa | Admin | Destino do botão e do item de menu, com filtro por usuário, entidade e PII. | US10, critério 2 |
| SEO local (lista da rede) | Admin | Item "SEO local" na lateral, sem tela. Alertas de title, canonical, schema e GBP em massa. | US7, FR-013, FR-014 |
| Templates e marca | Admin | Item "Templates e marca" na lateral. Tema, blocos travados, regras de texto, catálogo. | US3, FR-004; também a linha não desenhada em `telas.md` |
| Notificações | Admin e franqueado | Painel do sino (já com ponto). | US4 (SLA), US3 (aprovações), US7 (alertas) |
| Estados vazios, carregando e erro (404, 500, falha de DNS) | Todos | Um padrão, aplicado em leads, aprovações, suporte e domínio. | Transversal, SC-005 |
| Vista lista da central de leads | Admin, call center, franqueado | O interruptor Quadro / Lista já está na tela 07. | US4 |
| Fotos e FAQ no "Minha unidade" | Franqueado | Abas já visíveis; upload com "aguardando aprovação" e lista do que falta com ganho em pontos. | US2, critérios 3 e 4 |

**Prioridade 2 (spec P1 ou P2, fortalecem a apresentação se houver tempo)**

| Tela | Papel | O que faz | Ligação |
|---|---|---|---|
| Onboarding da unidade nova | Franqueado | Primeiro acesso, checklist de completude, escolha de template, convite da recepção. | US2, SC-005 |
| Convite e edição de pessoa | Admin e franqueado | Modal de convite com papel e escopo, a partir de "Convidar pessoa". | US10 |
| Configuração de SLA e regras de distribuição | Admin | Destino de "Regras de distribuição" na tela 07. | US4, FR-008 |
| Base de conhecimento e portal do cliente | Unidade e cliente final | Já prevista em `telas.md` como não desenhada. | US9, FR-011 |
| Dashboard do multifranqueado | Multifranqueado | Consolidado do grupo, comparativo entre as próprias unidades, sem ver a rede toda. | US5, papel M |
| Visão da agência (sem PII) | Agência | Mesmo dashboard 02, com leads agregados e sem nomes. | US4, critério 5 |
| Falha de verificação de domínio | Franqueado e admin | O passo vermelho do assistente 16. | US6 |
| Início, avaliações e "Mais" no celular | Franqueado | A tab bar já os exibe. Início pode ser o dashboard 12 em 390 px. | US5 |

**Prioridade 3 (fora de escopo agora ou laterais)**

Listagem pública de unidades e redesenho do site institucional (a própria spec tira do escopo). Agenda clínica (DocBiz). Modo escuro do admin. E-mails e WhatsApp transacionais em preview. Tela de permissões da aba "Segurança" (pode viver como âncora da 11).

## 10. Plano de aplicação (ordem sugerida)

Ordem pensada para o Stark aplicar, da correção que mais muda a apresentação para o acabamento. Nenhuma destas etapas altera o que já está forte (jornada do lead, aprovações, domínio, ranking do franqueado, formulário na primeira tela do A).

1. **Tokens.** Corpo 14 px, piso 12 px, cores semânticas da tabela da seção 3, degradê do franqueado parado em `#b0197e`, rótulos da lateral clara em `#6B4E78`. Um único commit de `estilo.css` beneficia quase todas as telas.
2. **Mapa.** SVG IBGE simplificado no `mapa_br()`, totais da legenda fechando 117 + 13, inset mantido. Em seguida, recortes de "Como chegar" nas telas 05, 19 e 20.
3. **Dados.** Selo "Ambiente de demonstração". Alinhar ou fictionalizar NAP e avaliações de Batel e Alto da Lapa. Trocar o CNPJ clássico. Desligar o chip "SLA: estourado" ou filtrar de verdade. Tirar resolvidos da aba Abertos. Unificar período e os rankings 4º / 7º. Alinhar badges 8 e 9, tratamentos 6 e 12, UFs 120 e 130.
4. **Landing e LGPD.** Checkbox desmarcado, botão preso ao aceite, tratamentos mobile com os seis itens, CTA persistente no mobile, ícone do FAQ unificado.
5. **Templates B e C.** Página B desktop e mobile, miniatura fiel de C, preview do editor gerado dessas páginas, telas 14 atualizadas. Se couber, o comparativo A e B.
6. **Celular do franqueado.** Padding acima da tab bar, jornada completa e rolável, contraste do WhatsApp, quebra "Orgânico · página", título da 18 com o nome do lead.
7. **Abas, tabela e fotos.** Overflow das 11 abas da ficha, cabeçalho de tabela 12 px, barra de ação em lote ou remoção do checkbox, banco mínimo de fotos distintas.
8. **Telas que faltam, só as de P1 que a demo pode encontrar.** 2FA, notificações, vazio, SEO local (mesmo que seja uma lista simples), LGPD com os 2 pedidos, vista lista de leads, fotos e FAQ do franqueado.
9. **Extras de encantamento**, se ainda houver tempo: mapa no dashboard 02, histórico do ranking, diff visual da landing, modo escuro do admin.

Fim da crítica. Arquivo complementar com a lista aberta: `critica-design-correcoes-abertas.md`.
