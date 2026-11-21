# Crítica de design: monitoramento de avaliações do Google (Gio Estética Avançada)

Cliente: Gio Estética Avançada (Salus), rede de 130 clínicas franqueadas.
Pedido: Osmar, via Stark. Objetivo: uma página mais útil. O franqueado vê e responde só as avaliações da própria unidade, com sugestão da IA editável. A rede tem visão geral, insights e levantamentos (nota, tempo de resposta, temas, região, ranking e escaladas).
Fonte: prints de página inteira em `revisao-layout/avaliacoes/` (19, 80, 81, 82, 83 e 84, em 360, 390 e 1440 CSS px, captura 1x, medidas no PNG). HTML em `telas/` e tokens em `telas/estilo.css`. Spec `specs/004-avaliacoes-google/spec.md` usada como checklist (perfis, estados, fluxo de resposta, escalada e insights). Consistência com `critica-design.md` e com o critério de casco da `critica-tela-52.md` (experiência de aplicativo, largura total, trilho de altura cheia, miolo com max-width alinhado ao trilho, ação principal óbvia, estados). Os renders em 768, 1024, 1280 e 1920 foram consultados só para casco e largura. Nenhum arquivo existente foi alterado.
Data da crítica: 21 de novembro de 2026, America/Sao_Paulo.
Método: sete passes por tela (hierarquia, espaçamento, tipografia, cor, interação e estados, texto, acessibilidade), mais consistência entre computador e celular e entre admin e franqueado. Contraste WCAG calculado pela luminância relativa a partir dos tokens do CSS e, quando necessário, de pixels amostrados no PNG. Tamanhos de tipo lidos no CSS e no HTML (medido), não estimados no bitmap, salvo indicação contrária. Valores rotulados como medido, estimado ou proposto. Severidade só assume "bloqueio", "vale corrigir" ou "detalhe".
Observação sobre os prints: todos levam no topo uma faixa de 40 px `#24082c` ("Ambiente de demonstração · dados fictícios"), cromo da galeria, fora do produto. Na tela 82, a barra de abas aparece no meio do print por efeito da captura; no navegador ela fica presa no rodapé, e isso não foi tratado como defeito de layout.

## 1. Veredito geral

O conjunto já cumpre a promessa central e tem cara de produto, não de wireframe. A fila do franqueado (80 e 82) mostra só a GiO Alto da Lapa, põe as sem resposta na frente, destaca nota baixa e menção a saúde, e leva a um compositor claro, com texto editável, atalhos de tom, contagem de caracteres e o botão "Publicar no Google" como ação óbvia. A tela 84 reúne os levantamentos pedidos (nota, resposta, tempo, fila, escaladas, temas, região e dois rankings) e evita o mapa do Brasil desenhado à mão, que tinha sido o pior ponto da crítica geral. O selo "Ambiente de demonstração" e o rodapé de dados ilustrativos estão no lugar certo. Os tokens da rodada 2 (Inter 14 px, Poppins nos títulos, verde `#0B7A54`, âmbar `#8A5800`, magenta `#b0197e`) passam no contraste AA em todos os pares que calculei.

O que mais custa é que o painel da rede informa, mas quase não deixa agir, e que o fluxo de resposta ainda tem um buraco grave. Na 84, temas, unidades, região, período, "Lembrar unidades", "Assumir", "Ver" e "Ver todas" são peças visuais sem destino. "Acompanhar" é o único link real, e ele abre a tela 81 no portal da franqueada, como se a rede fosse a Renata F. A lista de escaladas, que é o trabalho urgente do executivo, começa só na altura 1189 px do print de 1440 (medido), abaixo da primeira tela. No celular, a mesma tabela corta motivo, situação e os botões de ação. No compositor, os quatro cartões da fila apontam para `#r1` a `#r4`, mas as telas 81 e 83 não leem o hash: Lu M. (nota 1, relato de reação na pele, o caso bloqueante da US3) abre a resposta de Paula R., sobre agendamento. No celular da 83, a barra de abas cobre "Salvar rascunho" e quase todo o aviso de cuidados, porque a rolagem tem só 24 px de padding inferior (medido) contra 90 px de barra.

Com a 84 reordenada para ação (escaladas e pendentes no primeiro ecrã, recortes clicáveis, workspace da rede), com um compositor que abre a avaliação certa e com a 83 respirando acima da barra de abas, o módulo fica à altura da meta de surpreender e de ser útil no dia a dia.

## 2. Correções do conjunto em ordem de impacto

1. **Bloqueio. A fila não abre a avaliação certa.** Os cartões da 80 ligam para `81-franqueado-avaliacao-detalhe.html#r1` a `#r4`, e os da 82 para a 83 com os mesmos hashes. O HTML da 81 e da 83 tem só o caso de Paula R., e o script não lê `location.hash`. Quem toca em Lu M. revisa e pode publicar uma resposta de agendamento para um relato de saúde. Correção: um registro por avaliação (tema, sentimento, texto, sugestão, cuidados, linha do tempo) e troca pelo hash ou por rotas próprias. O caso de Lu M. precisa seguir as regras bloqueantes da US3 (não citar procedimento nem reação, convidar para canal privado com a responsável técnica). Enquanto isso não existir, não use a fila com quatro destinos na apresentação.

2. **Bloqueio. Na 83, a barra de abas cobre a ação secundária e o aviso de cuidados.** No PNG de 390, "Publicar no Google" termina por volta de y = 752 e a barra começa por volta de y = 760 (medido). "Salvar rascunho" não aparece. Do aviso só sobra, abaixo da barra, o final da frase "saúde. Assuntos de saúde vão para um canal privado." Causa (medida no CSS): `.mob.longo .rolagem` tem `padding: 0 16px 24px` e a barra tem 90 px de altura. Isto não é o artefato da 82. Correção proposta: `padding-bottom` de 120 px no conteúdo (90 da barra + 30 de respiro) e, de preferência, uma faixa grudada acima da barra com "Publicar no Google" e "Salvar rascunho". O aviso de cuidados fica inteiro acima dessa faixa.

3. **Vale corrigir (impacto de uso da rede). Na 84, quase nada é acionável e as escaladas ficam abaixo da primeira tela.** Só "Acompanhar" tem `href`, e aponta para a 81 no portal do franqueado. "Assumir", "Ver", "Ver todas", "Lembrar unidades", "Exportar CSV", os recortes de período, as linhas de tema, as unidades dos rankings e a tabela por região são `span`. A tabela de escaladas começa em y ≈ 1189 no print de 1440 (medido), fora de um ecrã de 900 ou 1080 CSS px. Correção: ver a seção 5 (hierarquia do primeiro ecrã, cards com destino, workspace da rede). Não reutilizar o casco "Portal do Franqueado · Renata F." para a rede.

4. **Vale corrigir. No celular da 84, a tabela de escaladas e a de região perdem as colunas que importam.** Em 390, "Por região" corta em "RESP" e some com respondidas e sem resposta. Em "Escaladas", cabem unidade, nota e um tema já cortado ("Agendament", "Procediment"); motivo, situação, "Acompanhar", "Assumir" e "Ver" ficam fora. O CSS do protótipo força `table.t { min-width: 640px }` com overflow, sem pista de que há mais à direita. Correção proposta: no estreito, virar as escaladas em cartões (unidade, estrelas, tema, motivo, situação e a ação na largura toda) e a região em lista de três linhas por regional, todas clicáveis. Se manter tabela, deixar uma coluna asomando uns 16 px e uma sombra de overflow.

5. **Vale corrigir. A 19 aponta para o lugar certo, mas com o botão errado e o cromo errado.** O item "Avaliações 24" no menu, ao lado de "SEO local", está visível e coerente. No cartão da unidade, o botão principal é "Monitoramento da rede" (vai para a 84), e o aviso amarelo é que tem a informação útil ("4 sem resposta nesta unidade, 2 com nota baixa"). "Ver a fila da unidade" é só um link de texto e abre a 80 no portal da franqueada. A lista do cartão mostra Ana, Joana e Cris (há 2 dias a 1 semana, notas 4 e 5) e omite Paula (há 3 h, nota 2) e Lu (há 9 h, nota 1). Correção: botão principal "Ver a fila desta unidade", secundário "Insights da rede". A lista abre pelas sem resposta e pelas notas baixas. A fila da rede usa casco de admin (ou "Entrar como unidade", já previsto na spec 001), não o portal da Renata. "Ver FAQ da unidade" tem o mesmo problema (hoje aponta para a 27).

6. **Vale corrigir. O casco de aplicativo ainda não está no CSS do produto.** Em 1440 e 1920 o desenho já é largura total: trilho de 252 px (medido) colado à esquerda, miolo até a borda, padding de 32 px (medido no CSS e no PNG de 1920, margem direita ≈ 32 px). Isso atende o casco da crítica da tela 52. Faltam duas coisas. Primeira: em `estilo.css` o trilho é `position: relative`; o comportamento grudado (`position: sticky; height: calc(100vh - …); overflow-y: auto`) existe só em `gerador/proto/proto.css` para `body.p-desk`, e ainda conta os 40 px da galeria. Segunda: abaixo de 1100 px o menu some e o botão "Menu" aparece só na faixa da galeria. O HTML solto, com `estilo.css` apenas, mantém a grade `252 px + 1fr` no celular e não tem gaveta. Correção proposta: levar trilho grudado e gaveta para o casco do produto (hamburger no `.top`, não no cromo). No miolo, `max-width` de 1280 px alinhado à esquerda do trilho, para em 1920 o texto e as tabelas não esticarem até uns 1636 px (medido). Para o franqueado no telefone, as telas 80 e 81 devem usar o padrão das 82 e 83 (tab bar, KPIs curtos, publicar acima da barra), não um "computador espremido".

7. **Vale corrigir. Filtros e atalhos da IA são peça de cenário.** Na 80, os chips "Sem resposta 4", "Nota baixa 2", "Respondidas" e "Todas" não são controles. O texto "Toque em um tema para filtrar a fila" está sob barras que não recebem clique, e o painel "O que mais aparece" omite Preço e Procedimento, embora Rodrigo e Lu estejam na fila de novembro. A spec (US2) pede filtro por nota, tema, sentimento e situação. Os atalhos "Mais curta", "Mais calorosa", "Convidar para conversar" e "Gerar outra" são `span.chip` sem script. "Publicar no Google" e "Salvar rascunho" também são `span`, não botão. Correção: transformar filtros, temas, atalhos e ações em `button` ou `a`, com estado no e no teclado. Ajustar as barras de tema aos cartões visíveis. No compositor, os atalhos precisam de estado (gerando, nova sugestão, falha) e de confirmação antes de publicar casos escalados ou com menção a saúde.

8. **Detalhe. Tipografia residual de 11 px e estrelas vazias no limite.** O corpo foi para 14 px e os pills para 12 px (medido), o que corrige o ponto mais grave da crítica geral. Continuam em 11 px (medido) `.side .logo span` e `.side .sec`. Proposta: 12 px, como o piso da rodada 2. Estrelas preenchidas amostradas em torno de `#8f5f0b` no branco: 5,51:1 (calculado, passa AA). Contornos vazios amostrados em torno de `#ab8649` a `#a37c38`: 3,34:1 a 3,82:1 (calculado), passam o 3:1 de componente, mas com pouca folga. Um tom um pouco mais escuro (proposto `#8A5800`, o âmbar do sistema) deixa o vazio mais legível.

## 3. Crítica por tela

### 19. SEO local (admin)

**O que a tela precisa fazer.** Continuar a comparar ficha e perfil do Google, agora com atalho visível para o monitoramento de avaliações da unidade e para os insights da rede (ajuste da spec 004 sobre a US13 da 001).

**Veredito.** A página em si está sólida: schema com campos da rede e da unidade, `aggregateRating` marcado como "não usado (política Google)", tabela de divergências, selo de demonstração e dados claramente fictícios ("Rua Demonstração, 100", telefones 90000). O novo destino não é um atalho perdido: entra no menu como "Avaliações 24", imediatamente abaixo do item ativo, e reaparece no cartão. O que falha é a hierarquia dentro do cartão (botão da rede no lugar da fila da unidade, lista que esconde o urgente) e o salto para o cromo do franqueado. Ver item 5 da seção 2.

**Achados**

1. **Vale corrigir.** Inverter o CTA do cartão e filtrar a lista pelas pendentes, como no item 5.
2. **Vale corrigir.** "lido há 3 h" no cartão "Ficha x perfil" não usa o mesmo formato da 80 ("Última leitura hoje às 15:40"). Unificar data e hora, e oferecer "Comparar agora" / "Ler agora" com estado de falha.
3. **Detalhe.** O domínio da ficha quebra no meio da palavra (`gioaltodalapa.exe` numa linha, `mplo.com.br` na outra, medido no print de 1440). Usar `overflow-wrap: anywhere` já está no HTML; preferir quebra em pontuação (`word-break` só no hífen e no ponto) ou uma linha com ellipsis e o URL completo no `title`.
4. **Acerto.** O aviso de política do Google abaixo das avaliações e o schema sem nota agregada estão alinhados ao FR-410.

### 80. Fila do franqueado (computador)

**O que a tela precisa fazer.** Mostrar só as avaliações da própria unidade, com as sem resposta na frente, destaque para nota 1 a 3 e escaladas, filtros (nota, tema, sentimento, situação) e indicadores (nota no Google, sem resposta, tempo de resposta, volume do mês). US2, FR-406.

**Veredito.** É a tela mais convincente do lote no computador. O recorte é só Alto da Lapa (contexto da lateral, título e linha do tempo de leitura). Não há ranking nem texto de outras unidades. Os quatro KPIs estão claros, o "4,8" vem com "(ilustrativo)", as notas baixas têm faixa esquerda em `--vermelho` e as positivas em `--verde` (medido no HTML). "Revisar e responder" é a ação óbvia de cada cartão. O que ainda é cenário: filtros, temas clicáveis e a divergência Preço / Procedimento no painel lateral. A ordem da fila é a mais recente primeiro, não a mais grave: Lu M. (1 estrela, saúde, há 9 h) vem depois de Paula (2 estrelas, há 3 h). A spec pede destaque, e o destaque visual existe; um "mais urgente" como ordenação padrão serviria melhor ao prazo de 24 h das notas 1 e 2 (SC-402).

**Achados**

1. **Vale corrigir.** Ligar os chips e os temas, completar Preço e Procedimento no "O que mais aparece" e oferecer sentimento e situação (por exemplo, "Rede avisada"). Ver item 7 da seção 2.
2. **Vale corrigir.** Ordenação padrão proposta: escaladas e notas 1 a 2 primeiro, depois as demais sem resposta, por data. Manter "mais recentes" como opção.
3. **Detalhe.** "Respondidas recentemente" aparece mesmo com o chip "Sem resposta" selecionado, o que é útil, mas as três linhas não têm destino. Ligar cada uma à 81 no estado "já publicada" (hoje esse estado não tem tela).
4. **Detalhe.** Não há "Ler agora" ao lado de "Última leitura hoje às 15:40", nem estado de perfil desvinculado ou de falha da API (US1, critério 3).
5. **Acerto.** O cartão "Quando a rede entra" e o aviso "Cuidados da resposta" traduzem a US5 e as regras bloqueantes da US3 em linguagem da unidade, sem expor dados de outras franquias.

### 81. Responder avaliação (computador)

**O que a tela precisa fazer.** Revisar, ajustar (mais curta, mais calorosa, convidar para conversar, gerar outra), salvar rascunho ou publicar no Google. US4. Mostrar escalada e, quando couber, que a rede acompanha ou assumiu. US5.

**Veredito.** O compositor está bem desenhado e já parece aplicativo: avaliação à esquerda, sugestão com selo "Editável", campo `contenteditable` (medido), "373 de 4.096 caracteres", atalhos, "Publicar no Google" como botão primário e "Salvar rascunho" ao lado. A coluna da direita explica "Rede acompanhando" (Ingrid N., 13:12), traz a linha do tempo e o "Por que esta sugestão", que é o tipo de copy que dá confiança para publicar. O furo é de produto, não de composição: a tela só encena o caso Paula. Sem o caso Lu, a apresentação não demonstra a regra bloqueante de saúde. O script atual, ao clicar em publicar, só revela o aviso "Resposta enviada ao Google" e troca o botão para "Publicada", sem confirmação e sem validador.

**Achados**

1. **Bloqueio.** Implementar as quatro avaliações e a sugestão correta de Lu M. Ver item 1 da seção 2.
2. **Vale corrigir.** Confirmar antes de publicar quando a avaliação for escalada ou mencionar saúde. O validador (FR-404) precisa ser vivo: a linha "sem dados de saúde · sem confirmar que é cliente" hoje é texto fixo, não reage à edição. Se o texto editado citar procedimento, sessão ou saúde, bloquear o primário e dizer o que trocar.
3. **Vale corrigir.** Estados que faltam no compositor: gerando sugestão, falha ao gerar, campo vazio, recusar sugestão e escrever do zero, limite perto de 4.096 (aviso aos 3.900, bloqueio acima), rascunho salvo, publicação em andamento e erro da API do Google. Os atalhos precisam desses estados, não só do desenho do chip.
4. **Vale corrigir.** O tema ("Agendamento") não é corrigível, embora o FR-403 peça correção manual pela unidade. Proposta: o pill vira um seletor discreto, com "corrigir tema", e isso alimenta o modelo.
5. **Vale corrigir (acessibilidade).** O campo `#resp-txt` tem `role="textbox"` e `aria-multiline="true"`, mas não tem nome acessível: o rótulo "Texto da resposta" não usa `for` / `aria-labelledby` (medido no HTML). As ações são `span.btn` e `span.chip`, fora da ordem de tab. Usar `button` e associar o rótulo ao campo.
6. **Acerto.** A trilha "Avaliações > Paula R.", o selo "Editável" e o "Por que esta sugestão" deixam claro que a IA propõe e a unidade publica.

### 82. Fila no celular

**O que a tela precisa fazer.** O mesmo da 80, no casco de aplicativo do franqueado (tab bar, uma unidade, ação por cartão).

**Veredito.** Está mais perto de app do que a 80 espremida em 390. Título grande, unidade como linha de suporte, dois KPIs (nota e sem resposta), três chips e os mesmos cartões com faixa colorida e "Revisar e responder". A barra de abas (Início, Leads, Agenda, Avaliações, Mais) é o casco certo, com "Avaliações" ativo. Não tratei a barra no meio do print como defeito, conforme o pedido. O que falta, em relação à 80 e à spec, é indicador de tempo e de volume, o chip "Respondidas", os temas, a última leitura e qualquer caminho para as já respondidas.

**Achados**

1. **Vale corrigir.** Trazer para a 82, em versão curta: "Última leitura hoje às 15:40", um terceiro dado (tempo mediano ou "2 com nota baixa" no KPI de sem resposta) e o chip "Respondidas". Temas podem virar uma linha de chips rolável, não o painel de barras da 80.
2. **Vale corrigir.** Os quatro cartões têm o mesmo furo de destino da 80 (item 1 da seção 2).
3. **Detalhe.** "Agenda ↗" aponta para `#docbiz` e sugere saída do sistema. Se a agenda ainda não existe neste protótipo, um destino ou um estado "em breve" evita um link morto ao lado da ação principal.
4. **Acerto.** Só aparece a GiO Alto da Lapa. A hierarquia visual (nota baixa com faixa vermelha, menção a saúde no pill) sobrevive bem aos 390 px.

### 83. Responder no celular

**O que a tela precisa fazer.** O mesmo da 81, com publicar alcançável acima da barra de abas.

**Veredito.** O miolo está bem reduzido: avaliação, selo "Editável", texto, atalhos e um "Publicar no Google" de largura cheia, no padrão certo de aplicativo. A redução, porém, foi longe demais e ainda esbarra na barra. Somem "Convidar para conversar", "de 4.096 caracteres", "sem confirmar que é cliente", "Rede acompanhando", a linha do tempo e "Por que esta sugestão". "Salvar rascunho" existe no HTML e é engolido pela barra, junto com o aviso de cuidados. O hash também não troca o caso. Em 390, a 81 espremida (computador com menu na galeria) mostra mais conteúdo e não cobre o rascunho: as duas telas estreitas não são o mesmo produto.

**Achados**

1. **Bloqueio.** Padding inferior e faixa de ações acima da tab bar, como no item 2 da seção 2.
2. **Bloqueio.** Abrir a avaliação certa, como no item 1.
3. **Vale corrigir.** Devolver "Salvar rascunho" (visível), "Convidar para conversar", a fração "373 de 4.096" e, pelo menos em um bloco recolhível, "Rede acompanhando" e "Por que esta sugestão". Sem isso, o celular publica mais cego do que o computador, justamente nos casos em que a pessoa responde no corredor da clínica.
4. **Vale corrigir.** Os mesmos estados, a confirmação e o nome acessível do campo descritos na 81.

### 84. Avaliações da rede (insights)

**O que a tela precisa fazer.** Painel da rede com nota média, porcentagem respondida, tempo mediano, sem resposta, escaladas; recortes por unidade, região e tema; temas recorrentes com volume e negativas; ranking de quem responde mais rápido e de quem acumula pendentes; lista de escaladas; exportação CSV e lembrete às unidades com pendentes. US6, FR-408.

**Veredito.** Como relatório, a tela já está rica e coerente internamente: 947 de 1.231 = 77%, 204 + 20 + 60 = 284 sem resposta, e os seis temas somam 1.231 (medido no conteúdo). Não há mapa do Brasil, o que é um acerto depois da crítica geral. Como ferramenta de executivo, ela ainda é um cartaz: o primeiro ecrã conta a história (KPIs, temas, região, começo dos rankings) e esconde o trabalho (24 escaladas sem resposta, lembrete, furar um tema ou uma regional). No celular, o relatório até empilha bem os KPIs (a quinta carta, "93 escaladas / 24 ainda sem resposta", ganha largura toda), mas as tabelas perdem as colunas de ação. A seção 5 detalha o redesenho.

**Achados**

1. **Vale corrigir.** Reordenar o primeiro ecrã e ligar cada bloco a um destino, como na seção 5. Trocar o destino de "Acompanhar" por um workspace da rede.
2. **Vale corrigir.** Tabelas no estreito em cartões, item 4 da seção 2.
3. **Vale corrigir.** Não há horário da última leitura nem "Ler agora" (a 80 tem; a 84 diz só "lidas algumas vezes ao dia"). Não há recorte de unidades com perfil não vinculado, nem tendência frente ao período anterior, nem a meta da spec (90% em 48 h, 95% das notas 1 e 2 em 24 h).
4. **Detalhe.** "GiO Sorocaba Shopping Pátio Ci" permanece cortado mesmo quando o nome já quebra linha no celular. "GiO Sao Paulo Casa Verde" está sem acento. Tratar ellipsis com `title` completo e corrigir a grafia.
5. **Detalhe.** As 85 "negativas" somadas nos temas não batem com as 93 escaladas. Pode ser que escalada por saúde não entre como negativa de tema, mas o número pede uma nota de método ou um recorte único.
6. **Acerto.** O selo e o rodapé de demonstração estão visíveis. Os nomes de unidade parecem reais, mas o conjunto está rotulado como ilustrativo, e esta tela não mistura telefone ou endereço de GBP com volume inventado (o problema da crítica geral). Manter o selo em qualquer captura que vá a cliente.

## 4. Consistência desktop, celular, admin e franqueado

O casco de computador já diferencia os dois portais do jeito certo (lateral escura da rede, lateral clara com acento rosa da unidade), com os tokens da rodada 2. Em 1440 e 1920 os dois são largura total, com trilho de 252 px e miolo fluido. Isso é o casco pedido na crítica da tela 52, aplicado a admin e franqueado, sem copiar o layout da área do cliente.

As costuras que ainda aparecem:

- **Trilho grudado e gaveta** vivem no CSS da galeria, não no do produto. Ver item 6 da seção 2.
- **Dois celulares para o mesmo franqueado.** A 82 e a 83 são o app (tab bar, fundo `#fbf7f9`, KPIs curtos). A 80 e a 81 em 390 são o computador com o menu escondido pela galeria, busca oculta abaixo de 600 px (regra do proto) e sem tab bar. Na apresentação, isso parece dois produtos. Proposta: abaixo de 700 px, 80 e 81 usam o casco de 82 e 83.
- **A rede no celular não tem casco próprio.** A 84 e a 19 em 390 dependem da gaveta da galeria e de tabelas de 640 px. Um executivo que abre escaladas no telefone não vê "Assumir".
- **A rede entra no portal da unidade.** "Ver a fila da unidade" (19) e "Acompanhar" (84) trocam o cromo para "Portal do Franqueado" e "Renata F.". Quebra permissão aparente (FR-406) e tira o ar corporativo da apresentação.
- **Rótulos e ações.** "Revisar e responder" é igual na 80 e na 82, bom. "Publicar no Google" é igual na 81 e na 83, bom. Já "Convidar para conversar", a fração de 4.096 e "Por que esta sugestão" somem só no celular. "Última leitura hoje às 15:40" existe na 80 e falta na 82 e na 84. Unificar.
- **Tab bar.** Cinco destinos, item ativo em vinho, altura 90 px com área segura (medido). Está alinhada ao app do franqueado. Na 83 ela não pode cobrir conteúdo (já um bloqueio). Na 82, o recorte no meio do print foi ignorado, como combinado.
- **Tipografia e cor.** Corpo 14 px, H1 24 px, KPI 26 px, pill 12 px (medido). Contraste dos tokens semânticos passa AA (cálculos na seção 2 e abaixo). A lateral do franqueado usava rótulos fracos na crítica geral; `#6B4E78` no branco agora dá 7,03:1 (calculado). Branco no magenta `#b0197e` dá 6,39:1 (calculado). O que resta é o 11 px das seções da lateral e as estrelas vazias no fio dos 3:1.

Contraste calculado (pares de token, texto 12 a 14 px, critério AA 4,5:1): âmbar `#8A5800` em `#fdf1dc` 5,41:1; verde `#0B7A54` em `#e5f5ee` 4,74:1; vermelho `#B4234A` em `#fde8ee` 5,47:1; tinta-3 `#5E5566` no branco 7,08:1; branco em `#b0197e` 6,39:1; branco em `#86106b` (início do degradê do franqueado) 9,13:1. Todos passam. O verde no fundo 50 está justo; não baixar mais a tinta.

## 5. O que deixaria a tela 84 mais útil para executivos

O executivo chega com três perguntas: onde está o risco agora, quem está atrasado, e o que está piorando (tema ou região). A 84 responde às três em texto, mas só na terceira tela e quase sem clique. O primeiro ecrã deveria abrir pelo risco e deixar cada número virar um recorte.

**Ordem proposta do primeiro ecrã (1440, miolo com max-width de 1280 px, alinhado ao trilho):**

1. Título, período (7 dias, 30 dias, intervalo) e "Exportar CSV", mais a hora da última leitura e um "Ler agora".
2. Cinco KPIs, todos clicáveis, com variação frente ao período anterior (proposto: seta e pontos percentuais, não só o absoluto) e, nos de resposta, a meta da spec (90% em 48 h; notas 1 e 2 em 24 h). "Escaladas 93 / 24 ainda sem resposta" e "Sem resposta 284 em 97 unidades" são os dois que pedem ênfase visual (fundo `--vermelho-50` ou barra à esquerda), porque são fila de trabalho, não retrato.
3. Fileira principal, duas colunas:
   - **Escaladas que pedem ação** (ocupa a coluna larga). Padrão: as 24 sem resposta primeiro, depois "unidade respondendo". Cada linha mostra unidade (link para a ficha ou para a fila daquela unidade, no casco da rede), nota, tema, motivo, situação e um botão real ("Assumir" ou "Acompanhar"). Um recorte "só saúde" e um "Ver todas" que abre a lista completa, não um `span`.
   - **Acumulam pendentes**, com "Lembrar unidades" como primário da coluna. Cada unidade é link para a fila dela. Mostrar há quanto tempo a mais antiga espera, não só a nota e a conta.
4. Abaixo da dobra, ou ainda no primeiro ecrã se a altura deixar: **Temas recorrentes** e **Por região**, ambos clicáveis (um tema abre as avaliações daquele tema no período, com ênfase nas notas 1 e 2; uma regional abre o mesmo recorte). Manter a frase de insight ("Agendamento e preço concentram as notas baixas"), virando também um atalho para esses dois temas.
5. **Respondem mais rápido** pode descer. É reconhecimento, não risco. Continua útil, com link para a unidade, e não deve competir com escaladas no primeiro ecrã.

**Workspace da rede (tela que falta, no mesmo casco da 84).** "Acompanhar" e "Assumir" não podem abrir a 81 como Renata. Proposta: uma tela de admin com a avaliação, a sugestão, o rascunho da unidade (se houver), a linha do tempo e as ações "Acompanhar", "Assumir", "Devolver à unidade" e, se assumir, "Publicar como rede". A unidade continua vendo o texto antes de sair, como a spec pede. Perfis só de agregados (R-FIN, R-AG) veem a 84 sem nomes, sem texto e sem esta tela.

**Rascunho de layout (1440):**

```
+------------------------------------------------------------------+
| Avaliações da rede     [7 dias] [30 dias] [01 a 21 nov] [CSV]    |
| Última leitura hoje às 15:40  [Ler agora]                        |
+----------+----------+----------+----------+----------------------+
| Nota 4,4 | 77% resp | 6,7 h    | 284 sem  | 93 escaladas         |
|  vs 30 d | meta 90% | mediana  | 97 un.   | 24 sem resposta      |
|          | em 48 h  |          | [abrir]  | [abrir]              |
+-------------------------------+----------------------------------+
| Escaladas que pedem ação      | Acumulam pendentes               |
| 24 sem resposta primeiro      | [Lembrar unidades]               |
| Unidade  nota  tema  motivo   | Unidade (link)  há X h  n pend.  |
| situação  [Assumir|Acompanhar]|                                  |
+-------------------------------+----------------------------------+
| Temas (clicáveis, % nota 1-2) | Por região (clicável)            |
| + insight de agendamento      | nota, % resp, tempo, fila        |
+-------------------------------+----------------------------------+
| (abaixo) Respondem mais rápido, com link para a unidade          |
+------------------------------------------------------------------+
```

No celular, a mesma ordem: KPIs em grade 2 × 2 mais a carta de escaladas em largura cheia (já está assim), depois a lista de escaladas em cartões, depois pendentes, temas e região. Sem tabela larga.

## 6. Fluxo de resposta com IA: estados que faltam e copy

O estado desenhado (sugestão pronta, texto editável, atalhos, publicar e rascunho) é o certo para o caso feliz. Faltam os estados ao redor, e a copy de alguns deles já pode nascer agora.

- **Gerando.** No lugar do texto, um bloco com "A IA está sugerindo uma resposta no tom da Gio…" e os atalhos e o publicar desfeitos. Não inventar o texto final antes de a sugestão chegar.
- **Sugestão vazia ou falha.** "Não foi possível sugerir uma resposta. Você pode escrever a sua ou tentar de novo." Primário: "Tentar de novo". Secundário: campo vazio já focado.
- **Recusar a sugestão.** Um link discreto "Escrever do zero" limpa o campo, mantém os cuidados à vista e não chama o texto de "resposta sugerida".
- **Atalhos.** "Mais curta", "Mais calorosa", "Convidar para conversar" e "Gerar outra" reescrevem o campo e avisam, por um instante, "Sugestão atualizada. Revise antes de publicar." "Gerar outra" não pode parecer publicar.
- **Validador ao vivo.** Se a edição citar procedimento, data de sessão, resultado individual, saúde ou confirmar que a pessoa é cliente, o primário trava e a linha de ajuda vira erro: "Esta frase confirma atendimento / cita dado de saúde. Tire isso antes de publicar. Assuntos de saúde vão para o WhatsApp ou o telefone da unidade."
- **Limite do Google.** Manter "X de 4.096 caracteres" também na 83. Aos 3.900, aviso âmbar. Acima de 4.096, bloquear publicar: "O Google aceita no máximo 4.096 caracteres."
- **Confirmação.** Para nota 1 ou 2, ou menção a saúde: "Esta avaliação foi avisada à rede. A resposta vai aparecer no Google em alguns minutos e não poderá confirmar que a pessoa é cliente nem discutir o caso em público. Publicar mesmo?"
- **Publicada.** O aviso verde que já existe no HTML ("Resposta enviada ao Google. Registrada na auditoria da rede…") é bom. Somar a hora e um "Ver no Google" quando o espelho voltar, e um "Voltar para a fila" evidente. O botão "Publicada" no estado `.off` já está no script; precisa ser `button` desabilitado, não um `span`.
- **Rede assumiu.** A unidade vê o texto da rede, em leitura, com "A rede assumiu esta resposta. Você está vendo o texto antes de ela sair." Sem o botão publicar.
- **U-REC (recepção).** Vê a fila, edita e salva rascunho. O primário vira "Salvar rascunho" e um texto "Quem publica é a gerência da unidade."
- **Copy da sugestão de Lu M. (proposta, para o caso bloqueante da US3).** Agradecer, demonstrar cuidado, não citar vermelhidão, sessão ou procedimento, e levar para canal privado com a responsável técnica. Assinatura da unidade. Não oferecer desconto nem resultado.

## 7. O que falta de tela ou de estado

- Workspace da rede para acompanhar e assumir (seção 5), e a lista completa de escaladas ("Ver todas").
- Fila da unidade no casco da rede (hoje a 19 e a 84 reutilizam a 80 e a 81).
- Estado "já publicada" e "rascunho salvo" na 81 e na 83, inclusive ao abrir Cris, Joana ou Bia pela lista de respondidas.
- Avaliação só com nota, sem texto.
- Avaliação removida ou editada no Google (US1).
- Perfil não vinculado e falha de leitura, com a data da última leitura bem sucedida (US1, FR-402).
- Fila vazia ("Tudo respondido neste recorte. O tempo mediano desta unidade está em 3,5 h.").
- Permissões: U-REC sem publicar; R-FIN e R-AG na 84 só com agregados, sem nome e sem texto (FR-406).
- Correção manual de tema e sentimento (FR-403).
- Os estados de IA e de limite da seção 6.
- Notificação de nota baixa (o sino da 80 e da 81 já tem ponto; falta a peça da fila ou o destino do sino, FR-409).
- Telas 80 e 81 no casco de app, em vez do computador espremido, e gaveta da 19 e da 84 no casco do produto.

A tela 13 (relatórios da rede) ficou de fora, como combinado com o Stark.

## 8. Plano curto de aplicação

1. Corrigir o compositor: uma avaliação por destino, caso Lu M. no tom da US3, hash ou rota funcionando, validador ao vivo e confirmação nos casos escalados. Liberar a 81 e a 83 juntas.
2. Na 83, colocar conteúdo e ações acima da barra de abas (padding de 120 px e faixa de publicar e rascunho). Devolver os atalhos e a fração de 4.096.
3. Redesenhar a 84 na ordem da seção 5, com links reais e o workspace da rede. No estreito, escaladas e região em cartões.
4. Ajustar a 19: CTA da unidade, lista pelas pendentes, destinos no casco da rede.
5. Ligar filtros, temas e atalhos; acertar as barras "O que mais aparece"; ordenar a fila por urgência.
6. Levar trilho grudado, max-width do miolo e gaveta para `estilo.css`. Unificar o celular do franqueado no casco da 82 e da 83.
7. Fechar estados (vazio, erro, desvinculado, publicada, permissões, avaliação sem texto) e a ponta tipográfica (12 px na lateral, estrelas vazias um pouco mais escuras).

Enquanto os itens 1 a 3 não estiverem prontos, a apresentação já pode usar a 80 e a 84 como retrato, desde que ninguém clique em Lu M., em "Acompanhar" ou nas tabelas no telefone. Com esses três, o módulo passa a ser a ferramenta que o Osmar pediu.
