# Crítica de design: tela 52, início do cliente no computador

Cliente: Gio Estética Avançada (Salus), área do cliente final logado no site da unidade.
Pedido: Osmar, via Stark. Objetivo: a tela precisa ter cara de aplicativo, para o cliente viver no site a mesma experiência do app futuro. A composição ainda está em largura fixa e está sendo convertida para largura total.
Fonte: PNG oficial `png/52-cliente-inicio-desktop.png` (1440 por 905 CSS px, captura 1x), HTML `telas/52-cliente-inicio-desktop.html` e tokens em `telas/estilo.css`. Comparação com as telas 43 a 51 (PNG 780 por 1688, ou seja 390 CSS px em escala 2x, e HTMLs correspondentes). Para o comportamento em largura total, consultei também os renders de verificação em `revisao-layout/1280` e `revisao-layout/1920` (a faixa escura "Ambiente de demonstração · dados fictícios" desses renders é cromo da galeria, não faz parte da tela 52). Spec 002 (`C05`, `C06`, `C20`, `C26`) usada só como checklist de funções, sem repetir a crítica das 20 telas internas. Nenhum arquivo existente foi alterado.
Data da crítica: 21 de novembro de 2026, America/Sao_Paulo.
Método: sete passes (hierarquia, espaçamento, tipografia, cor, interação e estados, texto, acessibilidade) mais um passe de padrões de app no desktop. Contraste WCAG calculado pela luminância relativa a partir dos tokens do CSS e, quando necessário, de pixels amostrados no PNG. Tamanhos de tipo lidos no CSS e no HTML (medido). Valores rotulados como medido, estimado ou proposto. Severidade só assume "bloqueio", "vale corrigir" ou "detalhe".

## 1. Veredito

A tela 52 já parece um produto, não um wireframe. O cartão de próximo agendamento em degradê, a barra do pacote, o selo de demonstração, os tokens corrigidos (Inter 14 px, Poppins nos títulos, verde `#0B7A54`, âmbar `#8A5800`, magenta de botão até `#b0197e`) e o recorte "Olá, Beatriz" estão no nível certo para uma apresentação. O contraste do texto lido passa em AA em todos os pares que amostrei.

O que mais custa é outra coisa: esta ainda é a "minha conta" de um site institucional, não o início de um aplicativo. O cabeçalho é o da landing (Procedimentos, Unidades, Ofertas, Descubra seu tratamento). A lateral é um cartão solto de 240 por cerca de 266 px, que termina no meio da página. Em 1920 CSS px o miolo inteiro, inclusive o menu, fica preso a 1344 px com 288 px de margem dos dois lados (medido). Na primeira fileira, "Complete seu perfil" tem o mesmo peso do agendamento. A avaliação da sessão de 18/11, três dias atrás, é uma linha morta, sem link e sem nota. As ofertas não explicam por que estão ali, e os três cartões apontam para o mesmo horário de avaliação de laser.

Com um casco de app (barra e trilho colados nas bordas, uma ação principal óbvia, avaliação acionável e o padrão "Por que estou vendo isso" da tela 47), esta tela passa a honrar o objetivo do Osmar. Sem isso, o computador e o celular parecem dois produtos.

## 2. Correções em ordem de impacto

1. **Casco de aplicativo em largura total.** Severidade: vale corrigir (é o que mais muda o efeito na apresentação). Evidência medida: o HTML da 52 usa `header` de 72 px com padding `var(--cli-pad)` e um grid `240px 1fr` com o mesmo padding; `--cli-pad` vale `max(48px, calc((100vw - 1344px) / 2))`. No PNG oficial, a mancha útil começa em x = 48 e termina em x = 1391 (largura 1344 px). No render de 1920, a mesma mancha vai de x = 288 a x = 1631 (de novo 1344 px, com 288 px de fundo vazio de cada lado); a lateral não encosta na esquerda. A lateral é um `.card` com `align-self: start` e cerca de 266 px de altura (no oficial, o branco do menu some por volta de y = 366, deixando uns 540 px vazios abaixo). O logotipo não é um link. O bloco "BD Beatriz" não é um menu. Não há sair, tampouco sino de avisos (o sino com ponto existe na 46). Correção proposta: cabeçalho e trilho em largura total, com padding lateral fixo de 24 a 32 px, sem recentrar o casco. Trilho esquerdo de 240 px, `position: sticky`, altura da janela, fundo branco, item ativo como já está (`--grad-franq`, branco em `#86106b` a `#b0197e`, 9,13:1 a 6,39:1, calculado). No cabeçalho, só a navegação da conta (Início, Agendar, Pacotes, Ofertas) mais sino e menu da pessoa (Perfil, Privacidade, Sair). Os destinos de marketing (Procedimentos, Unidades, Descubra seu tratamento) saem da barra logada e viram um item "Ver o site da unidade" no menu. A coluna principal começa ao lado do trilho, com `max-width` proposto de 1280 px e padding 28 a 32 px; o espaço que sobrar em 1920 fica à direita, não dos dois lados. Ver o rascunho na seção 6.

2. **A avaliação pós-sessão não dá para usar.** Severidade: bloqueio. Evidência medida: no HTML da 52, o segundo item de "Avisos" é um `div.it`, não um `a` nem um botão. O texto é "Conte como foi sua última sessão (nota de 0 a 10)". Não há controle de 0 a 10, não há "Avaliar". A sessão citada no item de cima é 18/11 (três dias antes de 21/11/2026). Na primeira fileira, o cartão "Complete seu perfil" (70 por cento, faltam interesses e telefone) leva um botão "Completar" e ocupa a mesma altura do agendamento (cerca de 213 px, medido no PNG: o degradê do próximo agendamento vai até y = 350, com topo visual dos cartões brancos em y = 174). A função é P1 na spec 002 (`C20`) e estava no pedido desta crítica. Correção proposta: se houver avaliação pendente, ela sobe para uma faixa logo abaixo do cumprimento, com a pergunta "Como foi a sessão de depilação de 18/11?" e uma ação clara, ou dez notas de 40 por 40 px (alvo de toque) ou um botão primário "Avaliar sessão" que abre `C20`. O item histórico ("Sessão de 18/11 registrada no seu pacote") pode ficar em Avisos. Enquanto a nota estiver pendente, "Complete seu perfil" desce para uma faixa compacta, no padrão da 46 (linha com ícone, 70 por cento e seta, altura proposta de 56 a 64 px).

3. **A primeira fileira trata três tarefas como iguais.** Severidade: vale corrigir. Evidência medida: o grid é `1.1fr 1fr 1fr` com gap 16 px. Em 1440, a coluna principal tem 1076 px (medido: x = 316 a 1391). Isso dá cerca de 370 px para o agendamento e 337 px para cada um dos outros dois. O agendamento é o único bloco com degradê, o que ajuda, mas a largura quase igual e o botão "Completar" ao lado de "Como chegar" diluem a ação do dia. O cartão do pacote não tem o título "Meu pacote" (a 46 tem) e não oferece "Agendar a 5ª sessão", que é o CTA de 48 px de altura da tela 50. Correção proposta: `grid-template-columns: minmax(420px, 1.6fr) minmax(280px, 1fr)` na primeira fileira, só com agendamento e pacote. No pacote, título "Meu pacote", o número no padrão da 50 ("4 de 10 sessões feitas", o 4 em 28 a 32 px Poppins 600) e um botão "Agendar a 5ª sessão" (a data sugerida 06/12 já está no meta). Perfil e quiz descem, em faixas, depois das ofertas ou ao lado de Avisos.

4. **Ofertas personalizadas sem origem e com destino errado.** Severidade: vale corrigir. Evidência medida: os três cartões da 52 são âncoras para `48-cliente-mobile-agendar-horarios.html`, a mesma tela em que o horário já vem preenchido como "Avaliação gratuita · Depilação a laser" no sábado 29/11 às 10:30. Quem clica em "Limpeza de pele de verão" ou "Semana do Ultraformer" cai no agendamento de laser. Nenhum cartão da 52 traz "Por que estou vendo isso?". Na tela 47, o padrão já existe e está bom: bloco em `--lilas-50`, 13 px, com "Você marcou depilação no quiz «Qual tratamento combina com você?» em 12/11 e tem consentimento de personalização ligado" e o link "Ver ou apagar respostas" para a 51. Só o primeiro cartão da 47 leva esse bloco; o segundo e o terceiro, não. "Ver todas" na 52 também aponta para a 47 em formato de celular. Correção proposta: cada cartão da home traz, abaixo do meta, uma linha "Por que estou vendo isso?" que abre o mesmo texto da 47 (ou um resumo de uma frase) e o atalho para a privacidade. O cartão em si leva à oferta certa, não ao horário de outro procedimento. A ação do cartão segue o rótulo da 47 ("Agendar avaliação" ou "Ver condição"). "Ver todas" abre a equivalente em desktop da 47, com o bloco de origem em todas as ofertas personalizadas, não só na primeira. Oferta de unidade e oferta de rede podem ter razões diferentes (quiz, unidade preferida, consentimento).

5. **A ação principal do agendamento está invertida para daqui a oito dias.** Severidade: vale corrigir. Evidência medida: o próximo horário é "Sáb, 29/11 às 10:30", oito dias depois de 21/11/2026. O botão sólido branco ("Como chegar", `.btn.s`, min-height 32 px, cor `--vinho` em branco, 11,68:1) vem antes do "Remarcar" (contorno, texto branco no magenta, 6,39:1, calculado). A tela 49 já tem "Pôr na agenda" ao lado de "Como chegar", mais a regra "Remarque ou cancele sem custo até 24 h antes" e o cuidado "Chegue 10 minutos antes. Evite sol forte na região nos 7 dias anteriores." Nada disso aparece no cartão da home. Correção proposta: a ação primária do cartão depende do estado (ver item 10). No estado "daqui a alguns dias", o primário é "Pôr na agenda" (arquivo `.ics` ou o equivalente já previsto na 49). "Remarcar" e "Cancelar" ficam como secundários, com a linha de 24 horas em 12 px. "Como chegar" vira primário no dia da sessão ou na véspera. Quando faltar uma semana, uma linha de cuidado pré-sessão pode entrar no próprio cartão.

6. **A unidade preferida é só uma frase, e "Trocar" abre o onboarding.** Severidade: vale corrigir. Evidência medida: o subtítulo do `h1` é "GiO Alto da Lapa é a sua unidade preferida." com um `a.lk` "Trocar" apontando para `45-cliente-mobile-interesses.html`. A tela 45 é o "Passo 3 de 3" do cadastro, com "Pular", chips de interesse, "Como conheceu a Gio?" e o mapa da unidade ("1,2 km · aberta até 20h · nota 4,8"). Nada disso (horário, distância, nota, ligar, ver no mapa) aparece na 52. Correção proposta: um chip ou linha no cabeçalho da página, no padrão da 45: "Sua unidade: GiO Alto da Lapa · aberta até 20h". Ações: "Trocar unidade" (abre só o seletor de unidade, não o passo 3 de 3), "Ligar" e "Como chegar". O cumprimento ("Olá, Beatriz") fica livre dessa frase longa.

7. **Rótulos e informações da 52 e da 46 não são o mesmo produto.** Severidade: vale corrigir. Evidência medida, lado a lado:

   - A 46 chama a aba de "Agendar"; a 52 chama o item de "Agendamentos".
   - A 46 tem título "Meu pacote"; a 52 não tem título no cartão.
   - A 46 mostra duas ofertas, sem foto de 150 px e sem "Por que estou vendo isso"; a 52 mostra três, com foto de 150 px (medido no HTML).
   - Quiz e Avisos existem só na 52. O sino com ponto vermelho (`8 px`, `--magenta`) existe só na 46, e ainda aponta para a tela de privacidade (`51`), não para uma central de avisos.
   - Na 46, "Complete seu perfil" é uma faixa no fim; na 52, é um cartão de primeiro nível.
   - A 46 não mostra a unidade preferida.
   - Na 46 (e em 47 a 51), o item ativo da tab bar não leva a classe `on`: no HTML está `class=""` e, no PNG, Início, Ofertas, Agendar, Pacotes e Perfil aparecem todos em `--tinta-3`. A 52, neste ponto, acerta: Início está com degradê e texto branco.
   - Na 46, a aba "Perfil" abre a 51 (Privacidade). Na 52, Privacidade e Perfil são dois itens, mas Perfil abre a 45 (interesses do onboarding). Não existe uma tela de perfil de verdade (nome, telefone, unidade, avisos).

   Correção proposta: um único mapa de informação para os dois tamanhos (ver seção 4). No desktop, o trilho usa os mesmos cinco destinos do celular (Início, Ofertas, Agendar, Pacotes, Perfil), com Privacidade dentro de Perfil. O estado ativo usa a mesma classe `on` nos dois. O sino entra no cabeçalho da 52 e aponta para avisos, não para a 51. Quiz pode viver na 52 e, no celular, como cartão compacto abaixo das ofertas ou dentro de Ofertas, para os dois não divergirem no conteúdo.

8. **Em 1280 px a terceira oferta quebra o meta.** Severidade: vale corrigir. Evidência medida: em 1280, `--cli-pad` cai para 48 px e a coluna principal fica com 916 px (medido: x = 316 a 1231). Os três cartões de oferta ficam com cerca de 294 px. O meta "Avaliação gratuita e horário estendido · 01 a 07/12" quebra em "01 a" numa linha e "07/12" na seguinte, no render de 1280. Em 1440 o mesmo texto cabe numa linha. Não há `auto-fit` nem ponto de quebra para esta grade (o CSS só fluidifica grades de formulário). Correção proposta: `grid-template-columns: repeat(auto-fit, minmax(260px, 1fr))`, no máximo três (ou quatro acima de 1600 px). Meta com `line-height` 1,4 e, se preciso, a validade numa segunda linha completa ("Válida de 01 a 07/12"), nunca uma data partida no meio. Entre 1100 e 1280, duas colunas de oferta são melhores do que três espremidas. Abaixo disso, usa-se a tela 46, como o render de 390 já faz.

9. **Não há menu da conta, sair nem notificações no computador.** Severidade: vale corrigir. Evidência medida: no header, "BD" (iniciais corretas de Beatriz Demonstração, conferidas na tela 44) e o nome "Beatriz" são `span` e `b`, sem `href` e sem `button`. Não existe "Sair". O sino da 46 não foi trazido. Avisos da 52 são um cartão estático. Correção proposta: o bloco da pessoa vira botão de 40 px de altura, com menu (Perfil, Privacidade, Unidade preferida, Sair). Sino de 40 por 40 px (já existe `.ib`) no cabeçalho, com ponto só quando houver item pendente, apontando para a mesma lista de avisos. "Sair" é obrigatório numa área logada, inclusive na demonstração.

10. **A tela só mostra um estado feliz.** Severidade: vale corrigir. Evidência medida: a 52 (e a 46) exibem agendamento confirmado, pacote com 6 sessões restantes válido até 12/2027, três ofertas e perfil a 70 por cento. Não há variação desenhada para: sem agendamento; sessão hoje ou em andamento; atraso ou falta; pacote acabando (por exemplo 9 de 10, ou validade no mês); pacote vencido; sem ofertas; perfil completo; avaliação já enviada. A spec 002 reserva isso a `C26`, P1. Correção proposta: desenhar, nesta mesma home, pelo menos cinco trocas de estado, com o primário mudando:

   | Estado | O que o cartão principal faz (proposto) |
   |---|---|
   | Sem agendamento, com pacote ativo | "Agendar a 5ª sessão" como primário, data sugerida visível |
   | Sessão amanhã ou hoje | "Como chegar" primário, horário em destaque, cuidado pré-sessão |
   | Atraso (não compareceu) | Faixa âmbar, "Remarcar agora", tom de ajuda e não de culpa |
   | Pacote acabando | "Renovar" ou "Falar com a unidade", validade em `--ambar` `#8A5800` em `--ambar-50` (5,41:1, calculado) |
   | Sem ofertas | Uma linha honesta e o quiz como saída, nunca um grid vazio |

11. **Hierarquia de títulos, barras e área de clique do aviso.** Severidade: detalhe. Evidência medida: depois do `h1` "Olá, Beatriz" (24 px Poppins 600, token `--fs-h1`) vêm vários `h3` (o de "Ofertas para você" com 18 px inline; "Complete seu perfil", quiz e Avisos com 16 px, token `--fs-card`). Não há `h2`. O pacote e os títulos das ofertas são só `b` em 14 px. As barras de 8 px de altura são um `i` com `width: 40%` ou `70%`, sem `role="progressbar"` e sem `aria-valuenow` (o texto ao lado, "6 sessões restantes" e "70%", salva o sentido para quem vê a tela, não para a API de acessibilidade). Correção proposta: um `h2` de seção ("Seu acompanhamento", "Ofertas para você") em 18 px; títulos de cartão em 16 px Poppins 600. Barras com `role="progressbar"`, `aria-valuemin="0"`, `aria-valuemax="10"` (ou 100) e `aria-valuenow`. Qualquer aviso acionável vira link ou botão, com altura mínima de 40 px.

12. **Sombra retirada dos cartões e rótulo em caixa alta de 12 px.** Severidade: detalhe. Evidência medida: pacote, perfil, ofertas, quiz e avisos levam `box-shadow: none` no HTML, ficando só com borda `--linha` `#e6dde9` e raio 16 px. O token `--sombra` existe e o `.card` padrão já a aplica. O rótulo "PRÓXIMO AGENDAMENTO" está em 12 px Inter 600, caixa alta, `letter-spacing: .06em`, branco no degradê (6,39:1 no magenta, 13,65:1 no roxo, calculado; passa AA). Correção proposta: devolver `--sombra` nos cartões clicáveis (pacote e ofertas), ou um estado `:hover` com sombra e translação de 1 px, para eles se comportarem como superfície de app. No rótulo do agendamento, preferir "Próximo agendamento" em 12 px, peso 600, sem caixa alta; a data (20 px Poppins 600, medido) já carrega a hierarquia.

13. **Copy solta e nomes do quiz que não batem.** Severidade: detalhe. Evidência medida: a home e o cabeçalho dizem "Descubra seu tratamento"; a tela 64 titula o quiz de "Qual tratamento combina com você?". A 47 cita o segundo nome no texto de origem da oferta. "4 de 10" no pill da 52 não diz se foram feitas ou se restam (o meta "6 sessões restantes" esclarece, a 50 é que acerta: "4 de 10 sessões feitas"). Correção proposta: um nome só para o quiz, de preferência "Qual tratamento combina com você?", e o botão "Começar o quiz". Pill do pacote: "4 de 10 feitas". Reescritas curtas na seção 5.

## 3. Padrões de app no desktop

O que a 52 já acerta: cumprimento com o primeiro nome, um herói de próxima sessão, pacote com barra, atalho de ofertas, selo claro de demonstração e um item de menu visivelmente ativo. Isso é mais do que um "minha conta" genérico. O que ainda a prende a um site:

- **Navegação.** Duas barras ao mesmo tempo (marketing no topo, conta na lateral) e uma lateral que não persiste na altura da janela. Num app web, o casco é fixo e os destinos da conta são os únicos à vista depois do login. O trilho (ou uma barra única no topo, se quiserem um visual mais leve) precisa estar presente em toda a área logada, não só nesta tela.
- **Cartões como superfície.** Pacote e ofertas já são âncoras, bom. Falta o estado de hover, o foco visível na prática (o CSS tem `:focus-visible` com `--foco`, mas o PNG é estático e não dá para conferir o teclado) e um CTA explícito nos cartões de oferta, como na 47, em vez de a área inteira pular para o lugar errado. "Avisos" não é superfície: as linhas não respondem a clique.
- **Uma ação principal óbvia.** Hoje convivem "Como chegar", "Remarcar", "Completar", "Ver todas", "Começar quiz" e um convite morto de nota 0 a 10. A regra proposta: uma primária por vez, escolhida pelo estado (item 10). Se a avaliação está atrasada, ela ganha a faixa. Se não está, e há sessão daqui a mais de um dia, "Pôr na agenda" ou "Agendar a 5ª sessão" assume. Quiz e perfil nunca competem com isso no mesmo tamanho de botão.
- **Estados e microinterações.** Além da tabela do item 10, o conjunto ganha muito com coisas baratas de implementar: hover de 150 ms nos cartões, a barra do pacote preenchendo ao carregar, um toast "Lembrete colocado na sua agenda", e esqueleto de carregamento no lugar do degradê. Nenhuma delas aparece hoje, e não dá para afirmar o contrário a partir de um PNG.
- **Largura total.** A conversão já começou: `width: 100%` e `--cli-pad` fluido são o caminho certo, e em 1440 o resultado é confortável (48 px de margem, 1344 px de miolo). O problema está no critério do token. Ele limita *casco e conteúdo juntos* a 1344 px, por isso em 1920 o menu flutua no centro com 288 px de margem. O critério proposto é outro: o casco é full bleed; só o miolo tem `max-width` (1280 px proposto) e alinhamento à esquerda, colado no trilho. Grades da home com `auto-fit` e mínimo de 260 px, para 1280 não esmagar a terceira oferta e para 1920 poder mostrar a mesma hierarquia com mais respiro, ou uma quarta oferta, sem esticar uma linha de texto até 1600 px.

## 4. Consistência com o mobile (43 a 51, sobretudo a 46)

A 46 é o equivalente certo desta tela e, em vários pontos, está mais perto de um aplicativo do que a 52: não mistura marketing, tem tab bar de cinco destinos, põe o pacote com título, reduz o perfil a uma faixa e deixa o agendamento ocupar a largura toda. A 52 ganha em conteúdo (quiz, avisos, terceira oferta, unidade preferida, item ativo visível) e perde em foco e em navegação.

Para unificar, eu trataria os dois tamanhos como o mesmo produto com cascos diferentes, não como duas homes.

- Componentes compartilhados: cartão de próximo agendamento (já quase idêntico no HTML das duas), cartão de pacote com título e número "X de Y feitas", faixa de perfil, cartão de oferta com foto, pill, meta, CTA e "Por que estou vendo isso?", faixa de avaliação pendente, chip de unidade preferida.
- Rótulos iguais: Início, Agendar, Pacotes, Ofertas, Perfil. "Agendamentos" some. "Meu pacote" aparece nos dois. O quiz tem um único nome.
- Hierarquia igual: 1) avaliação pendente, se houver; 2) próximo agendamento; 3) meu pacote; 4) ofertas; 5) perfil compacto; 6) quiz. Avisos entram no sino, não como um segundo bloco que só o computador vê. No desktop, agendamento e pacote podem ficar lado a lado; no celular, empilhados, como já estão.
- Ações iguais: "Pôr na agenda", "Remarcar", "Agendar a 5ª sessão", "Ver todas as ofertas", "Começar o quiz". Os destinos da 52 não podem ser as páginas `.mob` de 390 px; cada um precisa da sua versão em desktop (hoje só a home existe no computador, e isso se sente na demonstração).
- O que o desktop não deve copiar do celular: a tab bar de 90 px, o relógio 9:41, a aba Perfil abrindo Privacidade, e o sino apontando para a 51. O que o celular deve ganhar do desktop: item ativo visível (`a.on` em `--vinho`), unidade preferida no cumprimento, origem da oferta, e a avaliação pendente fora de um texto perdido.

Nas telas vizinhas, a 47 já tem o padrão de transparência que a 52 deveria herdar; a 50 já tem o número grande e o CTA do pacote; a 45 já tem o chip rico da unidade (distância, horário, nota 4,8), que o "Trocar" da 52 não deveria reabrir como passo 3 de 3; a 49 já tem "Pôr na agenda" e os cuidados pré-sessão; a 51 já resolve privacidade e pedidos LGPD. A 52 precisa orquestrar isso, não inventar um terceiro idioma visual.

## 5. Tipografia, cor e copy

**Tipografia (medida no CSS e no HTML).** Corpo Inter 14 px, line-height 1,5. H1 24 px Poppins 600. Data do agendamento 20 px Poppins 600. Título "Ofertas para você" 18 px. Títulos de card 16 px (quiz, avisos, complete o perfil) ou 14 px em `b` (pacote e ofertas). Meta 12 px em `--tinta-3`. Botão padrão 14 px com min-height 40 px; botão `.s` 13 px com min-height 32 px. Rótulo do herói 12 px. A escala está saudável e já segue o piso de 12 px pedido na crítica das áreas internas. Não há texto de 10 ou 11 px nesta tela. Ajustes propostos: títulos de cartão e de oferta em 16 px Poppins 600; "4" do pacote em 28 a 32 px, como a 50; botão primário do herói em min-height 40 px (o `.btn.s` de 32 px fica só para "Remarcar" e "Como chegar" quando forem secundários).

**Cor (contraste calculado).** Esta tela já usa os tokens recalibrados e passa em AA para texto normal nos pares que importam:

| Par (medido nos tokens) | Contraste | Leitura |
|---|---|---|
| `--tinta` `#1d1424` em branco | 17,83:1 | Passa AA e AAA |
| Nav e lateral inativa `--tinta-2` `#463b4e` em branco | 10,52:1 | Passa AA e AAA |
| Meta `--tinta-3` `#5E5566` em branco | 7,08:1 | Passa AA e AAA |
| Subtítulo `#5E5566` em `--fundo` `#f6f2f8` | 6,39:1 | Passa AA |
| Link `--vinho` `#6f0052` no fundo | 10,55:1 | Passa AA e AAA |
| Selo demo `#8A5800` em `#fdf1dc` | 5,41:1 | Passa AA (era 2,52:1 na crítica das áreas internas; aqui já está corrigido) |
| "confirmado" `#0B7A54` em branco | 5,35:1 | Passa AA |
| Pill "4 de 10" `#4c1455` em `#f3eaf6` | 11,64:1 | Passa AA e AAA |
| Pill "GiO Alto da Lapa" `#2C5BC4` em `#e9effc` | 5,36:1 | Passa AA |
| Branco no magenta `#b0197e` (fim do degradê, "Remarcar", "Começar quiz") | 6,39:1 | Passa AA |
| Branco no início do degradê `#4c1455` | 13,65:1 | Passa AA e AAA |
| Branco no item ativo `#86106b` | 9,13:1 | Passa AA e AAA |

O rosa `#e5559f` (3,42:1 com branco) não é usado como fundo de texto nesta tela, e deve continuar fora. Não há correção de contraste a fazer na 52, só a disciplina de não reintroduzir o extremo rosa no herói ou no item ativo.

**Reescritas curtas propostas.**

| Onde | Hoje (medido) | Proposto |
|---|---|---|
| Subtítulo | GiO Alto da Lapa é a sua unidade preferida. Trocar | Sua unidade: GiO Alto da Lapa · aberta até 20h. Ações: Trocar unidade, Ligar |
| Pill do pacote | 4 de 10 | 4 de 10 feitas |
| Meta do pacote | 6 sessões restantes · válido até 12/2027 · próxima sugerida em 06/12 | 6 restantes · válida até dez/2027. Próxima sugerida: 06/12 |
| CTA do pacote | (não existe) | Agendar a 5ª sessão |
| Primário do agendamento (oito dias antes) | Como chegar | Pôr na agenda |
| Avaliação | Conte como foi sua última sessão (nota de 0 a 10) | Como foi a sessão de depilação de 18/11? + botão Avaliar sessão |
| Origem da oferta (hoje só na 47) | (ausente na 52) | Por que estou vendo isso? Porque você fez o quiz em 12/11 e manteve a personalização ligada. Ver ou apagar respostas |
| Quiz, título e botão | Descubra seu tratamento / Começar quiz | Qual tratamento combina com você? / Começar o quiz |
| "Ver todas" | Ver todas | Ver todas as ofertas (se o título da seção não estiver ao lado; se estiver, pode ficar "Ver todas") |
| Perfil, botão | Completar | Completar perfil, na faixa compacta |
| Item da lateral | Agendamentos | Agendar |

O texto "Sem perguntas de saúde. Quiz de 6 perguntas, cerca de 1 minuto." deve permanecer: é uma linha de confiança alinhada à decisão de não coletar dado de saúde na fase 1, e está boa.

## 6. Rascunho de layout proposto (largura total)

A primeira tela em 1440 por 900, e também em 1920, deve caber sem rolagem o essencial: cumprimento, unidade, avaliação pendente (se houver), próximo agendamento, pacote e o começo das ofertas. Quiz e perfil compacto podem ficar logo abaixo, ainda visíveis em 1440 (hoje a página oficial já cabe em 905 px de altura; o redesenho não precisa crescer).

Casco. Cabeçalho de 64 a 72 px, branco, borda inferior `--linha`, colado nas bordas da janela. À esquerda, logo Gio (link para Início) com a assinatura "Minha conta". Ao centro ou em seguida, os quatro destinos da conta. À direita, sino e menu "Beatriz". Trilho de 240 px colado à esquerda, altura da janela, sticky, com os mesmos destinos e o item ativo em degradê. Sem cartão flutuante.

Miolo. Padding 28 a 32 px. Largura máxima 1280 px, alinhado à esquerda do espaço que resta. Em 1440 isso rende cerca de 1136 px de miolo (1440 menos 240 menos 64 de padding, proposto). Em 1920 o miolo não passa de 1280 px; os 300 e poucos px que sobram ficam à direita, nunca como margem que empurra o trilho para o centro.

Ordem dos blocos:

1. Cumprimento à esquerda ("Olá, Beatriz", 24 px) e, à direita ou na linha de baixo, o chip da unidade (nome, "aberta até 20h", Trocar unidade, Ligar).
2. Se houver avaliação pendente, faixa plena de 72 a 88 px, com a pergunta da sessão de 18/11 e a ação de avaliar. Sem pendência, este bloco some e o agendamento sobe.
3. Fileira de duas colunas: próximo agendamento (cerca de 1,6 partes) e meu pacote (1 parte). No agendamento, data, procedimento, unidade, endereço, pill de estado e as ações do estado corrente. No pacote, título, 4 de 10 feitas, barra, validade e "Agendar a 5ª sessão".
4. "Ofertas para você" com "Ver todas as ofertas" na mesma linha (`display: flex; align-items: center`, como o HTML já tenta fazer). Três cartões com foto de 120 a 140 px, pill, título 16 px, meta, CTA e a linha "Por que estou vendo isso?".
5. Fileira de duas faixas compactas: complete o perfil (progresso 70 por cento) e o quiz (um botão primário, sem competir com o herói). Avisos ficam no sino.

Esquema da grade em 1440 e acima:

```
[======= cabeçalho full bleed: logo Minha conta | Início Agendar Pacotes Ofertas | sino | Beatriz =======]
[ trilho 240 ][  Olá, Beatriz                          Unidade: Alto da Lapa · até 20h  Trocar  Ligar  ]
[ sticky     ][  [======= Como foi a sessão de 18/11?          Avaliar sessão =======]                ]
[ Início     ][  [ Próximo agendamento  1,6fr ]  [ Meu pacote  1fr                  ]                ]
[ Agendar    ][  [ 29/11 10:30 confirmado     ]  [ 4 de 10 feitas                   ]                ]
[ Pacotes    ][  [ Pôr na agenda   Remarcar   ]  [ Agendar a 5ª sessão  06/12       ]                ]
[ Ofertas    ][  Ofertas para você                                      Ver todas as ofertas         ]
[ Perfil     ][  [ oferta 1 + por que ] [ oferta 2 + por que ] [ oferta 3 + por que ]                ]
[            ][  [ Complete seu perfil 70% ]  [ Qual tratamento combina com você?  Começar o quiz ]  ]
```

Em 1280, a fileira de ofertas cai para duas colunas (`auto-fit`, mínimo 260 px) ou reduz a foto, para o meta não partir a data. Em 390, permanece a tela 46, com os mesmos blocos na ordem acima (avaliação, agendamento, pacote, ofertas, perfil, quiz) e a tab bar já existente, desta vez com o item ativo marcado.

## 7. O que falta nesta tela e no fluxo ligado a ela

Para a área do cliente chegar ao objetivo (site e app como a mesma experiência), falta mais do que polir a 52.

- As telas seguintes no computador. Hoje, quase todo link da 52 abre um HTML de 390 px (47, 48, 49, 50, 51, 45, 64). Na apresentação, isso quebra a ilusão de sistema robusto. Precisam existir, no mesmo casco da 52: ofertas (`C06`), agendar horário e confirmação (`C10` e `C11`), meu pacote (`C14` e `C15`), avaliar sessão (`C20`), privacidade (`C23`) e um perfil de verdade (dados, telefone, unidade, avisos), não o passo 3 do onboarding.
- A faixa e a tela de avaliação (`C20`): nota 0 a 10, comentário, convite para o Google sem incentivo, como já está na spec.
- Os estados vazios e de exceção (`C26`), listados no item 10, desenhados na própria home e não só descritos.
- Central de notificações. O sino da 46 e o cartão Avisos da 52 devem ser a mesma lista (lembrete da sessão, sessão lançada no pacote, avaliação pedida, oferta nova).
- "Pôr na agenda", ligar para a unidade e cuidados pré e pós sessão, que já aparecem na 49 e ainda não alimentam o cartão da home.
- Um seletor de unidade preferida autônomo, reusando o mapa da 45, sem "Passo 3 de 3" nem "Pular".
- Microinterações e estados de interface (hover, foco visível conferido no teclado, carregando, erro de rede, toast).
- No celular, a classe `on` da tab bar e o destino correto de Perfil (hoje a aba de pessoa abre Privacidade). É um conserto barato e visível.
- Na 47, o bloco "Por que estou vendo isso?" nas três ofertas, não só na primeira, para a home poder apontar para um padrão completo.

Nada disso pede um visual novo: os tokens, os cartões, as pills e os botões já estão prontos. O que falta é completar o produto em volta desta única tela de computador.

## 8. Plano curto de aplicação

1. Fechar o casco de app (cabeçalho logado, trilho sticky em altura total, `--cli-pad` só no miolo, menu da pessoa com Sair, sino). É a mudança que se vê na hora, em 1440 e sobretudo em 1920.
2. Tornar a avaliação de 18/11 acionável e colocá-la acima da primeira fileira. Sem isso, a função de NPS permanece só no discurso.
3. Reorganizar a primeira fileira: agendamento e pacote só, título "Meu pacote", "4 de 10 feitas", CTA "Agendar a 5ª sessão", primário do herói conforme o estado ("Pôr na agenda" neste recorte de 29/11). Perfil vira faixa.
4. Corrigir ofertas: origem "Por que estou vendo isso?" em cada cartão, CTA próprio, destino certo, "Ver todas" para uma 47 em desktop. Ajustar a grade com `auto-fit` para o meta não quebrar em 1280.
5. Unificar rótulos e destinos com a 46 (Agendar, Perfil, item `on`, unidade no cumprimento, "Trocar" sem reabrir o onboarding). Desenhar os estados do item 10, ainda que em variações desta mesma home.
6. Só então abrir as telas de computador que faltam (agendar, pacote, avaliar, ofertas, privacidade, perfil), reusando o casco da 52, para a demonstração não cair no layout de 390 px.

Os itens 11 a 13 (títulos, sombra, copy do quiz) podem entrar no mesmo lote do passo 3, sem fila própria.
