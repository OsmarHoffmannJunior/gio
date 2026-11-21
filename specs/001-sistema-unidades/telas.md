# Inventário de telas (rodadas 2 e 3, rev. 3.4)

Atualizado em 21/11/2026. Substitui a numeração de 20 telas da rodada 1 (arquivada em `../../arquivo-rodada1/`). Todas as telas usam dados fictícios de demonstração: telefone (DD) 90000-0000, CNPJ 00.000.000/0001-00, IP 192.0.2.10, domínios `*.exemplo.com.br`. Telas internas levam o selo "Ambiente de demonstração"; landings levam uma faixa no rodapé.

Arquivos: HTML navegável em `../../telas/` (CSS único `estilo.css`), PNG em `../../png/` (1440 px no computador; 390 px a 2x no celular), galeria em `../../galeria.html` e `../../galeria.pdf`, pacote `../../telas-png.zip`. Geradores em `../../gerador/` (s1 a s9, render.py, galeria.py, prototipo.py, verifica_prototipo.py). Protótipo navegável em `../../prototipo/`.

Rodada 3 (21/11/2026): 28 telas novas (43 a 70) das specs 002 e 003, tela 17 evoluída para a auditoria geral (US21, FR-036) e tela 31 com o acesso da rede ao Analytics e ao Search Console da unidade com domínio próprio (decisão do Osmar de 21/11, 09h42). Mesmas verificações por script: contraste AA, texto cortado, texto fora do card, texto escondido atrás da barra de abas no celular (verificação nova) e fonte mínima. As 70 telas passam sem problemas.

Itens da crítica de conjunto (C01 a C07, C09, C10, C44) valem para todas as telas: tokens AA medidos por script, fonte mínima 12 px (rótulos em caixa alta 11 px), controle de período único só onde filtra dados, selo de demonstração.

| # | Tela | Perfis | Arquivo | Crítica coberta | História |
|---|---|---|---|---|---|
| 01 | Entrar | Todos | `01-login` | C11 C12 | US20 |
| 02 | Verificação em duas etapas | Todos | `02-2fa` | C11 |  |
| 03 | Primeiro acesso e senha | Todos | `03-primeiro-acesso-senha` | C11 | US20 |
| 04 | Visão geral | Rede | `04-admin-dashboard-rede` | C13 C14 C15 |  |
| 05 | Unidades em tabela | Rede | `05-admin-unidades-tabela` | C16 |  |
| 06 | Unidades no mapa | Rede | `06-admin-unidades-mapa` | C17 |  |
| 07 | Detalhe da unidade | Rede | `07-admin-unidade-detalhe` | C18 C19 C20 |  |
| 08 | Landing pages da unidade | Rede | `08-admin-unidade-landing-pages` | C19 |  |
| 09 | Aprovações | Rede | `09-admin-aprovacoes` | C21 C22 |  |
| 10 | Central de leads (quadro) | Rede e call center | `10-admin-leads-kanban` | C23 C24 |  |
| 11 | Central de leads (lista) | Rede e call center | `11-admin-leads-lista` | C24 |  |
| 12 | Detalhe do lead | Rede e call center | `12-admin-lead-detalhe` | C25 |  |
| 13 | Relatórios da rede (hub, redesenhada na rodada 5) | Rede | `13-admin-relatorios` | C26; spec 005 US1, US2 |  |
| 14 | Relatórios inteligentes | Rede | `14-admin-relatorios-inteligentes` | nova (P1) |  |
| 15 | Suporte | Rede e franqueado | `15-admin-suporte` | C27 |  |
| 16 | Usuários e perfis | Rede | `16-admin-usuarios-perfis` | C28 C29 | US20 |
| 17 | Auditoria geral | Rede (só perfis de rede) | `17-admin-auditoria` | nova (P1), evoluída na rodada 3 | US21 |
| 18 | LGPD | Rede | `18-admin-lgpd` | nova (P1) |  |
| 19 | SEO local da unidade | Rede (SEO) | `19-admin-seo-local` | nova (P1) |  |
| 20 | Templates e marca | Rede | `20-admin-templates-marca` | nova (P1) |  |
| 21 | Modelos de ficha | Rede | `21-admin-modelos-ficha` | nova (P1) |  |
| 22 | Módulos | Rede | `22-admin-modulos` | nova (P1) |  |
| 23 | Central de ajuda | Todos | `23-central-ajuda` | nova (P1) |  |
| 24 | Início | Franqueado | `24-franqueado-dashboard` | C14 C30 |  |
| 25 | Minha unidade | Franqueado | `25-franqueado-minha-unidade` | C31 |  |
| 26 | Fotos | Franqueado | `26-franqueado-fotos` | C08 C31 |  |
| 27 | Perguntas frequentes | Franqueado | `27-franqueado-faq` | C31 |  |
| 28 | Escolha de modelo | Franqueado | `28-franqueado-templates` | C32 C43 |  |
| 29 | Comparar A e B | Franqueado | `29-franqueado-comparativo-ab` | C43 |  |
| 30 | Editor da página | Franqueado | `30-franqueado-editor` | C33 C34 C43 |  |
| 31 | Domínio próprio | Franqueado | `31-franqueado-dominio` | C35; acesso da rede ao GA4 e ao Search Console (rev. 3.2) |  |
| 32 | Unidade nova | Franqueado | `32-franqueado-unidade-nova` | nova (P1) | US20 |
| 33 | Leads no primeiro dia | Franqueado | `33-franqueado-leads-primeiro-dia` | nova (P1) |  |
| 34 | Notificações | Franqueado | `34-franqueado-notificacoes` | nova (P1) |  |
| 35 | Leads no celular | Franqueado (celular) | `35-mobile-leads` | C36 |  |
| 36 | Lead no celular | Franqueado (celular) | `36-mobile-lead` | C37 C38 |  |
| 37 | Modelo A · Clássico (computador) | Cliente final | `37-landing-a-desktop` | C18 C39 C40 C41 C43 |  |
| 38 | Modelo A · Clássico (celular) | Cliente final | `38-landing-a-mobile` | C39 C40 C42 C43 |  |
| 39 | Modelo B · Vitrine (computador) | Cliente final | `39-landing-b-desktop` | C18 C39 C40 C43 |  |
| 40 | Modelo B · Vitrine (celular) | Cliente final | `40-landing-b-mobile` | C39 C40 C42 C43 |  |
| 41 | Modelo C · Autoridade local (computador) | Cliente final | `41-landing-c-desktop` | C18 C39 C40 |  |
| 42 | Modelo C · Autoridade local (celular) | Cliente final | `42-landing-c-mobile` | C39 C40 C42 |  |

### Rodada 3: área do cliente e clientes e vendas (spec 002)

| # | Tela | Perfis | Arquivo | Código na 002/003 | Fase |
|---|---|---|---|---|---|
| 43 | Entrar ou criar conta | Cliente (celular) | `43-cliente-mobile-entrar` | C01 | P1 |
| 44 | Dados básicos | Cliente (celular) | `44-cliente-mobile-dados` | C03 (C02 incorporado) | P1 |
| 45 | Onboarding de interesses | Cliente (celular) | `45-cliente-mobile-interesses` | C04 | P1 |
| 46 | Início do cliente (rev. 3.4: mesma ordem e rótulos da 52) | Cliente (celular) | `46-cliente-mobile-inicio` | C05, C20 (faixa) | P1 |
| 47 | Ofertas para você | Cliente (celular) | `47-cliente-mobile-ofertas` | C06 | P1 |
| 48 | Agendar: horários | Cliente (celular) | `48-cliente-mobile-agendar-horarios` | C10 | P1 |
| 49 | Agendar: confirmação | Cliente (celular) | `49-cliente-mobile-agendar-confirmacao` | C11 | P1 |
| 50 | Meu pacote | Cliente (celular) | `50-cliente-mobile-pacote` | C14 e C15 | P2 |
| 51 | Privacidade | Cliente (celular) | `51-cliente-mobile-privacidade` | C23 | P1 |
| 52 | Minha conta no site (rev. 3.4: casco de aplicativo) | Cliente (computador) | `52-cliente-inicio-desktop` | C05 (computador), C20 (faixa) | P1 |
| 53 | Procedimentos e preços | Franqueado | `53-franqueado-procedimentos-precos` | U03 | P1 |
| 54 | Promoções | Franqueado | `54-franqueado-promocoes` | U05 | P1 |
| 55 | Campanhas | Franqueado | `55-franqueado-campanhas` | U06 | P1 |
| 56 | Nova campanha (passo 4 de 8) | Franqueado | `56-franqueado-campanha-assistente` | U07 | P1 |
| 57 | Tags e medição | Franqueado | `57-franqueado-tags-medicao` | T11 | 1 |
| 58 | Controles da rede | Rede | `58-admin-controles-liberacoes` | R02 e R03 | P1 |
| 59 | Mural de avisos | Rede | `59-admin-mural-aviso` | R04 (R05 parcial) | P1 |
| 60 | Campanha da rede (prévia) | Rede | `60-admin-campanha-rede` | R07 | P1 |
| 61 | Aprovação de campanhas | Rede | `61-admin-campanhas-aprovacao` | R08 | P1 |
| 62 | Performance e replicar | Rede | `62-admin-performance-campanhas` | R09 e R13 | P1 |

### Rodada 3: quiz, inteligência e tracking (spec 003)

| # | Tela | Perfis | Arquivo | Código na 003 | Fase |
|---|---|---|---|---|---|
| 63 | Gerador de quiz | Rede | `63-admin-quiz-gerador` | Q11 e Q12 | 2 |
| 64 | Quiz: pergunta | Cliente (celular) | `64-quiz-mobile-pergunta` | Q02 | 2 |
| 65 | Quiz: resultado | Cliente (celular) | `65-quiz-mobile-resultado` | Q03 | 2 |
| 66 | Demanda e recomendações | Rede | `66-admin-inteligencia-demanda` | I01 e I05 | 3 |
| 67 | Sazonalidade e clima | Rede | `67-admin-inteligencia-sazonalidade` | I02 (I04 parcial) | 4 |
| 68 | Dicionário de eventos | Rede | `68-admin-tracking-dicionario` | T02 | 1 |
| 69 | Gerador de UTM | Rede | `69-admin-tracking-utm` | T07 | 1 |
| 70 | Saúde do tracking | Rede | `70-admin-tracking-saude` | T04 e T05 | 2 |

Números coerentes entre telas (fonte única em `gerador/base.py`): 130 unidades (SP 86, Sul 14, demais 30); 2.986 leads, 1.733 agendados e 1.071 compareceram na rede, iguais nas telas 04, 68 (lead_enviado, agendamento_concluido, atendimento_compareceu) e 62 (214 agendamentos de campanha dentro dos 1.733); 48.312 clientes na base; alcance de 102 da campanha Ultraformer igual nas telas 55 e 61; cota da unidade 1 de 2 no mês; 412 confirmações esperadas no mural; quiz com 6.940 inícios e 4.512 conclusões (65%).

### Auditoria geral (tela 17, US21, FR-036, SC-011)

Visível só para perfis de rede. Filtros por período, pessoa, perfil, unidade, módulo, tipo de ação e status de aprovação; tabela com 12 registros de exemplo cobrindo alteração, acesso a dado pessoal, permissão, tags, campanha, configuração e exportação; detalhe com antes e depois, quem fez, quem pediu, quem decidiu e o motivo, IP e aparelho; exportação CSV das linhas filtradas (a própria exportação vira registro); cartão "Registro imutável" (append-only, cadeia de hash, retenção D14).

### Telas das specs 002 e 003 que ficaram de fora nesta rodada

Critério: desenhar primeiro as telas de maior impacto da fase 1 e as que explicam as decisões novas (consentimento, cotas, aprovação, medição). As demais ficam descritas nas specs e entram numa próxima rodada.

- Área do cliente: C02 (incorporada na 44), C07, C08, C09, C12, C13, C16 a C22, C24 a C28. Checkout, pagamento e compras (C16 a C18) dependem da decisão de venda online e split (D1 da 002); C27 e C28 são P3.
- Unidade: U01, U02, U04, U08 a U14. U12 (mural do lado da unidade) e U13 (o que a rede liberou) aparecem resumidos na 24 e na 58.
- Rede: R01, R05 (parcial na 59), R06, R10 a R12, R14 a R20. Financeiro (R18) depende do D1 da 002.
- Quiz: Q01, Q04, Q05, Q10, Q13 a Q17 (fase 2).
- Inteligência: I03, I06, I07 (fases 3 e 4; fontes pagas desligadas por decisão do Osmar; I07 depende do D11).
- Tracking: T01, T03, T06, T08 a T10, T12 a T15. O acesso da rede ao GA4 e ao Search Console da unidade com domínio próprio (T10) está resumido nas telas 31 e 57.

### Rodada 5: hub de relatórios da rede (spec 005, 21/11/2026)

| # | Tela | Perfis | Arquivo | Spec 005 | Fase |
|---|---|---|---|---|---|
| 13 | Visão executiva (hub) | Rede | `13-admin-relatorios` | US1, US2, US12 | P1 |
| 90 | Aquisição e campanhas | Rede | `90-admin-relatorios-campanhas` | US3 | P1 |
| 91 | Leads e funil | Rede | `91-admin-relatorios-leads-funil` | US4 | P1 |
| 92 | Atendimento do franqueado | Rede | `92-admin-relatorios-atendimento` | US5 | P1 |
| 93 | Quiz, landings e tráfego | Rede | `93-admin-relatorios-quiz-landings` | US6 | P1 |
| 94 | SEO local, Google e avaliações | Rede | `94-admin-relatorios-seo-avaliacoes` | US7 | P1 |
| 95 | Área do cliente | Rede | `95-admin-relatorios-area-cliente` | US8 | P2 |
| 96 | Unidades e regiões | Rede | `96-admin-relatorios-unidades` | US9 | P1 |
| 97 | Relatório da unidade (`?unidade=<slug>`) | Rede | `97-admin-relatorios-unidade` | US9 | P1 |
| 97f | Relatório da minha unidade | Franqueado (só a própria) | `97-franqueado-relatorio-unidade` | US9a | P1 |
| 89 | Cadastro de metas e regras de alerta | Rede | `89-admin-relatorios-metas-regras` | US10 | P1 |
| 98 | Metas, previsão e alertas | Rede | `98-admin-relatorios-metas-alertas` | US10 | P1 |
| 99 | Exportar e agendar envio | Rede | `99-admin-relatorios-exportar` | US11 | P1 |

Abas no topo de todas as telas do hub levam às seções; filtro global com busca e seleção de várias unidades (no protótipo os números não mudam e a tela avisa); CSV real gerado no navegador a partir da tabela principal, PDF pela impressão; tabelas ordenáveis; mapa com troca de métrica na 96. Gerador: `gerador/s12.py` com dados em `gerador/rel_dados.py` (fictícios e coerentes com as telas 04, 24, 62 a 70 e 84).

Rev. 2 (21/11, 18h, crítica `critica-relatorios.md`): todo nome de unidade abre a 97 daquela unidade (exemplos de cada quartil na 96); 97f no menu do franqueado; 13 abre com manchete, alertas e metas, filtros e legenda recolhidos, KPIs clicáveis e nota no Google; comparecimento com um denominador (já realizados); receita de pacotes x receita atribuída à mídia x ROAS da mídia; 96 com paginação, cabeçalho preso e cartões no celular; filtro na URL com faixa de filtro ativo; estados vazio e de API atrasada; 89 nova; 99 com confirmação e gestão dos envios; alerta de UTM; meta de 90% em 48 h na 94.

### Rodada 4: avaliações do Google (spec 004, 21/11/2026)

| # | Tela | Perfis | Arquivo | Spec 004 | Fase |
|---|---|---|---|---|---|
| 80 | Fila de avaliações | Franqueado (computador) | `80-franqueado-avaliacoes` | US1, US2, US3 | P1 |
| 81 | Responder avaliação (sugestão da IA editável) | Franqueado (computador) | `81-franqueado-avaliacao-detalhe` | US3, US4, US5 | P1 |
| 82 | Avaliações no celular | Franqueado (celular) | `82-mobile-avaliacoes` | US2 | P1 |
| 83 | Responder no celular | Franqueado (celular) | `83-mobile-avaliacao-detalhe` | US3, US4 | P1 |
| 84 | Avaliações da rede (insights) | Rede | `84-admin-avaliacoes-rede` | US5, US6 | P1 |
| 85 | Escaladas para a rede (lista completa) | Rede | `85-admin-avaliacoes-escaladas` | US5, US6 | P1 |
| 86 | Escalada: workspace da rede (acompanhar, assumir, devolver, publicar como rede) | Rede | `86-admin-avaliacao-escalada` | US5 | P1 |
| 87 | Fila da unidade no casco da rede | Rede | `87-admin-avaliacoes-unidade` | US2, US5, US6 | P1 |

Rev. 2 (crítica `critica-avaliacoes.md`, 21/11/2026 17h21):
- **19**: botão principal "Ver a fila desta unidade" (87, casco da rede), secundário "Insights da rede" (84); a lista abre pelas pendentes e notas baixas (Lu M., Paula R., Rodrigo T., Fernanda S.), cada uma abre o workspace da rede (86); "Escaladas desta unidade" leva à 85 filtrada; leitura do perfil no formato "última leitura hoje às 12:40".
- **80 e 82**: ordem padrão por urgência (saúde e notas 1 e 2 primeiro); chips Sem resposta, Nota baixa, Avisadas à rede, Respondidas e Todas são links (`?f=`); temas clicáveis (`?tema=`) com Preço, Procedimento e Sem texto; "Ler agora"; respondidas abrem a 81/83 no estado publicada. Estados: `?estado=vazia`, `desvinculado`, `falha`.
- **81 e 83**: um registro por avaliação, escolhido pelo hash (`#r1` a `#r7`) ou `?r=`; Lu M. (nota 1, saúde) com sugestão que não cita procedimento nem reação e leva à responsável técnica; Bia F. é a avaliação só com nota. Validador ao vivo (procedimento, sessão, saúde, confirmar cliente, desconto) trava o publicar; "X de 4.096" com aviso aos 3.900 e bloqueio acima; atalhos são botões que reescrevem com estado "gerando"; "Escrever do zero"; confirmação antes de publicar nos casos escalados; rascunho salvo com hora; correção manual do tema (FR-403); rótulo associado ao campo. Estados: `?estado=gerando`, `falha`, `validador`, `limite`, `assumida`, `publicada` e `?perfil=recepcao` (só rascunho). Na 83, rolagem com 120 px no fim (`.mob.longo .rolagem.com-tab` em `estilo.css`) e `scroll-padding-bottom`, linha do tempo e "Por que esta sugestão" de volta.
- **84**: primeiro ecrã de ação: período e "Ler agora", cinco KPIs clicáveis com meta (90% respondidas em 48 h; notas 1 e 2 em 24 h, meta 95%) e variação frente a outubro; escaladas sem resposta (sem rascunho primeiro, saúde e nota 1 na frente) com "Assumir" ou "Acompanhar" no workspace (86), "Só saúde" e "Ver todas" (85); unidades com pendências (link para a 87) e "Lembrar unidades"; temas e regiões clicáveis (85 filtrada), com os seis temas; ranking de rapidez no fim. Exportar CSV gera o arquivo. Abaixo de 760 px de cartão, escaladas e regiões viram cartões (sem tabela cortada).
- **85 a 87**: novas (ver tabela). Estados da 87: `?estado=desvinculado`, `falha`, `vazia`.
- **Casco do produto** (`estilo.css`): trilho grudado de altura cheia acima de 1100 px e gaveta com botão de menu no `.top` abaixo disso (o botão "Menu" da faixa da galeria some quando a tela tem o do produto). Seções da lateral em 12 px; estrelas em `#8A5800`.

Menus: "Avaliações" no franqueado (Clientes e vendas) e na rede (Inteligência, contador de escaladas sem resposta); no app do franqueado, a aba "Avaliações" substitui "Página". Números calculados em `gerador/s11.py` com semente fixa (dados fictícios). Pendências: casco de celular próprio para a rede; telas 80 e 81 com `?fixo=1` abaixo de 700 px seguem o casco do computador (sem `?fixo=1` o protótipo redireciona para 82 e 83, mantendo hash e query); miolo do painel segue em largura total (decisão de layout fluido do Osmar, em vez do max-width de 1280 px sugerido na crítica); perfis só de agregados (R-FIN, R-AG) sem tela própria.

### Rodada 3b: área do cliente no computador (crítica da tela 52, 21/11/2026)

| # | Tela | Perfis | Arquivo | Código na 002 | Fase |
|---|---|---|---|---|---|
| 71 | Ofertas | Cliente (computador) | `71-cliente-ofertas-desktop` | C06 | P1 |
| 72 | Agendar (horários e confirmação) | Cliente (computador) | `72-cliente-agendar-desktop` | C10, C11 | P1 |
| 73 | Meu pacote | Cliente (computador) | `73-cliente-pacote-desktop` | C14, C15 | P2 |
| 74 | Avaliar sessão | Cliente (computador) | `74-cliente-avaliar-desktop` | C20 | P1 |
| 75 | Privacidade | Cliente (computador) | `75-cliente-privacidade-desktop` | C23 | P1 |
| 76 | Perfil | Cliente (computador) | `76-cliente-perfil-desktop` | C24 | P1 |
| 77 | Escolher unidade | Cliente (computador e celular) | `77-cliente-unidade-desktop` | C09 | P1 |
| 78 | Avisos | Cliente (computador e celular) | `78-cliente-avisos-desktop` | C21 | P1 |
| 79 | Perfil no celular | Cliente (celular) | `79-cliente-mobile-perfil` | C24 | P1 |

Aplicado da crítica (`critica-tela-52.md`): casco de aplicativo (cabeçalho só da conta com Início, Agendar, Pacotes, Ofertas, sino e menu com Perfil, Privacidade, Ver o site da unidade e Sair; trilho sticky de 240 px com os mesmos cinco destinos do celular; miolo até 1280 px alinhado ao trilho); ordem dos blocos (cumprimento e unidade com Trocar e Ligar, faixa de avaliação com notas 0 a 10 e Avaliar sessão, agendamento e pacote, ofertas com "Por que estou vendo isso?" em todas e destinos próprios, perfil e quiz em faixas); "Pôr na agenda" como ação principal a 8 dias; "Meu pacote" com "Agendar a 5ª sessão"; "Trocar" abre a 77 (seletor próprio, fora do onboarding); 46 e 52 com os mesmos rótulos, sino, quiz e avisos; tab bar do celular com o item ativo marcado e Perfil abrindo a 79. As telas 77 e 78 servem também ao celular pela camada responsiva do casco (abaixo de 900 px o trilho vira barra de abas). Pendência: estados C26 (sem sessão, sessão hoje, atraso, pacote acabando) desenhados na própria home; versões de celular desenhadas de avaliar, avisos e seletor de unidade.

### Layout fluido (rev. 3.4)

Todas as telas deixam de ter moldura fixa de 1440 px: o casco da rede e do franqueado ocupa 100% da largura (sidebar fixa e sticky no protótipo, conteúdo em `minmax(0,1fr)`); landings e telas públicas têm fundo full-bleed com conteúdo limitado a 1312 px (`--lp-pad`); telas de celular abrem como coluna central com fundo contínuo. Formulários com layout simples (rev. 3.5): rótulo, caixa e ajuda em coluna, grades alinhadas ao topo e sem altura forçada; no painel o rótulo fica numa linha só (texto completo no title) e os selos Rede, Editável e Com aprovação aparecem só com ícone em grades de 3 ou 4 colunas; abaixo de 700 px toda grade de formulário vira uma coluna; colunas laterais fixas descem para baixo do conteúdo quando a área útil é menor que 1000 px (notebook de 1280). Checagem automática em `gerador/checa_layout.py` (360, 390, 768, 1024, 1280, 1440 e 1920 px, com e sem ?fixo=1, incluindo formulário esticado), relatório em `revisao-layout/`. Telas de acesso 01 a 03 responsivas de 360 a 1920 px.

## Protótipo navegável (rodada 3)

Pasta `../../prototipo/`, site estático pronto para Cloudflare Pages, gerado por `gerador/prototipo.py` a partir das telas (mesmo HTML e CSS, sem redesenho). Não publicado e sem deploy.

- Entrada em `index.html`: escolha de perfil (Rede, Franqueado, Cliente) e lista de todas as telas. Em todas as páginas há uma barra de demonstração no topo com o selo "Ambiente de demonstração", a troca de perfil e o atalho "Todas as telas".
- Menus laterais, abas e botões principais levam à tela correspondente. Abas e botões sem tela desenhada mostram o aviso "Ação simulada no protótipo: nada é enviado ou gravado."
- Funcionam de verdade: consentimentos da tela 44 (o botão só libera depois dos obrigatórios), filtros, detalhe com antes e depois e exportação CSV da auditoria (17), menu lateral no celular.
- No celular (até 700 px), as landings de computador abrem a versão de celular. As telas de computador da rede e do franqueado usam uma camada responsiva (menu recolhido, colunas empilhadas, tabelas com rolagem); não são um desenho próprio de celular.
- No portal do franqueado, "Leads", "Relatórios", "Suporte" e "Central de ajuda" abrem as telas compartilhadas 10, 13, 15 e 23, com o menu da rede. O escopo por unidade vem do perfil.
- Proteções: meta robots noindex em todas as páginas, `_headers` com `X-Robots-Tag: noindex, nofollow`, `robots.txt` com Disallow /, só dados fictícios.
- Abrir localmente: `cd prototipo && python3 -m http.server 8080` e acessar http://localhost:8080 (ou abrir `index.html` direto no navegador).
- Verificação headless (`gerador/verifica_prototipo.py`): 81 páginas (rev. 3.4), 0 links quebrados, 0 páginas inalcançáveis, 0 erros no navegador, 0 transbordo em 390 px, 17 testes de interação aprovados em 1440 e 390. Prints em `../../prototipo-verificacao/390/` e `/1440/`.

## Contas por convite (US20, FR-034, FR-035)

- 01: não existe "criar conta". Há um cartão "Primeiro acesso?" que explica o convite.
- 03: e-mail de convite da conta de admin da unidade, definição de senha com critérios, ativação do 2FA e esqueci a senha.
- 16: assistente de provisionamento da unidade pela rede e prévia do convite; o admin da unidade só cria usuários nos perfis liberados (Gerente, Recepção).
- 32: primeiro acesso do admin da unidade, com o passo "Convidar equipe".

## Política de campos nas telas

Os estados Rede (T), Editável (E) e Com aprovação (EA) nas telas 07, 09, 19, 20, 25, 26, 27, 30 e 34 seguem `politica-campos.md`: telefone fixo EA, WhatsApp E, endereço T (muda por chamado), ponto de referência E, texto Sobre, fotos e FAQ local E com revisão posterior, promoção fora do modelo e troca de modelo EA.

## Fora do desenho (só na spec)

- Telas da 002 e 003 listadas acima como fora desta rodada.
- Listagem pública de unidades: depende do redesenho do site.
