# PROGRESSO · Sistema de unidades Gio (telas + spec)

Atualizado em 21/11/2026, 09:05 (horário de Brasília).

## Feito
- [x] Estrutura de pastas e .specify (modelo spec-kit)
- [x] Identidade visual: logos, fachada, fontes locais (assets/)
- [x] Constituição: .specify/memory/constitution.md (10 princípios)
- [x] Spec: specs/001-sistema-unidades/spec.md (papéis, US1 a US10, FR, SC)
- [x] Plano: specs/001-sistema-unidades/plan.md
- [x] Modelo de dados: specs/001-sistema-unidades/data-model.md
- [x] Inventário de telas: specs/001-sistema-unidades/telas.md
- [x] Design system: telas/estilo.css (admin escuro, franqueado claro com acento rosa)
- [x] Geradores: gerador/base.py, p1.py a p5.py (20 telas HTML em telas/)
- [x] PNGs: png/ (1440 px desktop, 390 px mobile com escala 2x), render com gerador/render.py
- [x] Checagem: overflow horizontal e texto cortado por script + revisão visual de cada PNG
- [x] Checagem de travessões no texto visível: nenhum
- [x] Galeria: galeria.html e galeria.pdf (11 páginas, A4 paisagem)
- [x] Zip: telas-png.zip (20 PNGs)

## Rev. 2 da spec (decisões do Osmar, 21/11/2026)
- [x] Constituição 1.1.0: V (política de campos), VIII (RBAC), XI (rede dona do schema e do SEO técnico), XII (override da rede às claras). Versão anterior em .specify/memory/historico/constitution-1.0.0.md.
- [x] spec.md: papéis viram perfis RBAC; US2, US3 e US10 ajustadas; US11 (override), US12 (perfis), US13 (schema base e política); FR-015 a FR-026; SC-007 a SC-009; Riscos e lacunas (12); Decisões em aberto D1 a D14
- [x] rbac.md (novo): perfis padrão, matriz módulo x perfil x ação, regras transversais, perfis personalizados
- [x] politica-campos.md (novo): 71 itens (38 campos da ficha, 18 blocos da landing, 15 de schema e SEO técnico) com T, E, EA, L, O por perfil
- [x] data-model.md: perfil, perfil_permissao, teto_nivel, atribuicao, regional, politica_campo, schema_base, faq_base, seo_unidade, valor_campo_versao, lote_alteracao, promocao, notificacao, contestacao; auditoria ampliada
- [x] telas.md: mudanças anotadas para 05, 11 e 13 (e efeitos menores em 06, 12 e 15)
- [x] plan.md: nota de impacto (rev. 2)
- [x] Redesenho das telas 05, 11, 13 (e 06, 12, 15): feito na rodada 2 (novas 07, 16, 25 e 09, 24, 30)
- [ ] Respostas do Osmar e da Gio para D1 a D14

## Rodada 2 de telas (crítica + decisões + pedidos novos), iniciada 21/11/2026 08:55
Plano (marcar ao concluir):
- [x] R2.1 Spec (telas.md fica para o fim): wiki/docs, relatórios inteligentes, módulos (feature toggles), modelos de ficha + menu, landing pages e variantes; dados-ficha.md (inventário); politica-campos.md completada; constitution/spec/telas.md
- [x] R2.2 Tokens novos em telas/estilo.css (corpo 14, piso 12, cores AA, degradê franqueado até #b0197e, lateral clara #6B4E78) + selo "Ambiente de demonstração"
- [x] R2.3 Script de contraste no render.py (texto x fundo efetivo, degradê no pior caso)
- [x] R2.4 Mapa do Brasil com malha oficial de UFs (IBGE, embutida em assets/geo/br-ufs-ibge.json; mapa_geo/mapa_br em gerador/base.py), legenda 117 + 13 = 130
- [x] R2.5 Banco de fotos distintas (assets/fotos/, 6 fotos ilustrativas) e recortes OSM em assets/geo/osm-*.json (Overpass, 3 unidades)
- [x] R2.1b Regra nova (09:10): sem cadastro manual de conta interna. Rede provisiona a unidade e envia convite da conta admin da unidade (U-FRQ); primeiro acesso troca senha e ativa 2FA; admin da unidade cria os demais usuários dentro dos perfis permitidos. Ajustar spec.md, rbac.md, constituição, telas 01, 03 (vira primeiro acesso e senha), 16 e 32. NÃO mexer em specs/002-area-cliente/.
- [x] R2.6 Dados de demo fictícios (NAP, CNPJ, avaliações, Instagram, WhatsApp, IP 192.0.2.10)
- [x] R2.7 Telas refeitas e novas (42), links entre telas (protótipo estático). Geradores novos: gerador/s1.py (01 a 06, feito), s2.py (07 a 12, feito), s3.py (13 a 18, feito), s4.py (19 a 23, feito), s5.py (24 a 34, feito; miniaturas dependem dos PNGs das landings, renderizar duas vezes), s6.py (35 a 42). Rodada 1 arquivada em arquivo-rodada1/.
- [x] R2.8 Render 1440 e 390@2x, checagem script + visual de cada PNG (42 telas, 0 problemas de overflow, corte, fonte ou contraste AA; relatório em png/checagem.json)
- [x] R2.9 galeria.html, galeria.pdf (24 p.), telas-png.zip (42 PNGs) regerados após ajustes da política de campos e C34; telas.md reescrito (42 telas, crítica por tela, US20); spec rev. 3.1 com regra de convite; relatório final entregue ao Stark em 21/11/2026

Geradores da rodada 1 guardados em gerador/rodada1/ (histórico).

## Como regenerar
cd gerador && for p in s1 s2 s3 s4 s5 s6 s7 s8 s9; do python3 $p.py; done && python3 render.py && python3 render.py && python3 galeria.py && python3 prototipo.py && python3 verifica_prototipo.py   (render duas vezes: telas 20, 28 e 29 usam PNGs das landings como miniatura)
Zip: python3 com zipfile dos png/NN-*.png (não há zip no box). Protótipo local: cd prototipo && python3 -m http.server 8080
PDF: google-chrome --headless=new --no-sandbox --no-pdf-header-footer --print-to-pdf=galeria.pdf file://$PWD/../galeria.html

## Pendente
- Crítica de design (o Stark encaminha ao Critiquista)
- Redesenho das telas afetadas pela rev. 2 da spec (feito na rodada 2)
- Rodada 3: perguntas D1, D2, D3 da 002 para a Salus; D6, D8, D9 da 003 em aberto; vídeo e guia de configuração de tags (anotado); telas da 002/003 fora desta rodada listadas em specs/001-sistema-unidades/telas.md; nada publicado

## Spec 002 e 003 (executor da área do cliente), 21/11/2026
- [x] specs/002-area-cliente/: spec.md (rev. 1c), data-model.md, telas.md, decisoes.md, ideias.md, impacto-na-001.md, resumo.md. Inclui controles da rede com padrão bloqueado, mural de avisos, campanhas com assistente, performance e replicar.
- [x] specs/003-quiz-inteligencia-tracking/: spec.md (US1 a US23, FR-201 a FR-238, SC-201 a SC-212, backlog por fase), pesquisa.md (fontes linkadas e custos coletados em 21/11), data-model.md (com dicionário de eventos v0.1), telas.md (Q, I, T), decisoes.md (D1 a D16), impacto-na-001-002.md, resumo.md. Inclui gerenciador de tags por unidade (09h30) e guia de configuração na Wiki e em vídeo como entregável futuro (09h33).
- [x] Aplicar impacto-na-001.md (002) e impacto-na-001-002.md (003) na spec 001: feito na rodada 3 (ver abaixo).
- [ ] Decisões D1 a D16 da 002 e D1 a D16 da 003 com o Osmar.

## Rodada 3 (21/11/2026, a partir das 09h39): spec 002/003 na 001, telas novas e protótipo
- [x] R3.1 Constituição 1.4.0 (XIV a XVII, ajustes I, III, IV, V, VII, IX, X, XI); cópia da 1.3.0 em .specify/memory/historico/
- [x] R3.2 Spec 001 rev. 3.2: spec.md (papéis, US4, US5, US9, US16, US19, FR-009 renomeado, FR-024/025/027/028, D9, seção Integração), rbac.md, politica-campos.md, dados-ficha.md, data-model.md, plan.md
- [x] R3.3 Spec 003: decisões do Osmar 09h42 marcadas em decisoes.md (13 de 16) e seção no spec.md. Pasta 002 não editada.
- [x] R3.3b Auditoria geral (Osmar 09h52): spec rev. 3.3 (US21, FR-036, SC-011), rbac (só rede), data-model (tabela append-only), tela 17 refeita com filtro por tipo, detalhe com diff e CSV em JS
- [x] R3.3c Decisões da 003 (09h42): tela 31 e 57 mostram acesso da rede ao GA4 e Search Console da unidade com domínio próprio
- [x] R3.4 Telas novas: s7 (43 a 52), s8 (53 a 62), s9 (63 a 70); navegação lateral com grupos novos (gerador/s7.py cliente, s8.py unidade e rede, s9.py quiz, inteligência e tracking) + ajuste da tela 31 (acesso da rede ao GA4 e Search Console)
- [x] R3.5 Render e checagem (70 telas, 0 problemas; nova checagem CORTE_CEL para conteúdo escondido atrás da barra do celular) (render.py detecta celular pela largura do viewport)
- [x] R3.6 Protótipo em prototipo/ (gerador/prototipo.py): cópia fiel das telas, seletor de perfil, noindex, _headers, verificação de links e prints 390 e 1440. Verificação: 72 páginas, 0 links quebrados, 0 erros, 0 transbordo em 390, 17 testes ok. Coerência corrigida: eventos agendamento_concluido 1.733 e atendimento_compareceu 1.071 (iguais à tela 04)
- [x] R3.7 telas.md (70 telas, protótipo, fora da rodada), galeria.html e galeria.pdf (39 páginas), telas-png.zip (70 PNGs), relatório ao Stark

## Publicação no Cloudflare Pages (aprovada pelo Osmar 21/11 10h14)
- [x] Projeto Pages criado na conta do Osmar (plano gratuito, *.pages.dev, sem domínio próprio), deploy de produção 84991e9c feito por envio direto pela API (99 arquivos)
- [x] Proteção Basic Auth (usuário gio) em _worker.js, equivalente a functions/_middleware.js (fontes em deploy-pages/); falha fechada (503) sem secret; X-Robots-Tag noindex em todas as respostas, incluindo 401 e 503; /robots.txt público com Disallow /
- [x] Secret GIO_DEMO_SENHA cadastrado pelo Osmar (10h26); novo deploy de produção f00358de (retry não existe para envio direto); curl: sem credencial 401, errada 401, robots 200, senha do box 200 no index e em 5 telas (após o 308 do Pages para URL sem .html), noindex em todas
- [ ] Trocar a senha por uma forte (a atual coincide com a do box e é fácil de adivinhar pelo endereço) e republicar

## Rodada 3.4 (21/11/2026, 10h36 a 11h30): layout fluido, formulários e crítica da 52
- [x] Layout fluido: casco a 100% (sidebar fixa, conteúdo `minmax(0,1fr)`), landings e telas públicas full-bleed com conteúdo até 1312 px, celular com fundo contínuo.
- [x] Formulários: subgrid em `.campo` (rótulo, caixa e ajuda alinhados), selos à direita do rótulo (só ícone em coluna estreita), legenda dos selos na 07, colunas laterais descem abaixo de 1000 px úteis.
- [x] Checador `gerador/checa_layout.py` (1280, 1440, 1920, 390): faixa branca, sobreposição, desalinhamento, transbordo, texto cortado, contraste AA. Relatório e prints em `revisao-layout/`; prints de antes em `revisao-layout/antes/`.
- [x] Crítica da 52 aplicada na 52 e na 46 (casco de aplicativo, ordem dos blocos, faixa de avaliação, Pôr na agenda, Meu pacote, porquê nas ofertas, Trocar abre seletor próprio, tab bar com item ativo, Perfil fora da Privacidade).
- [x] Telas novas 71 a 79 (versões de computador de ofertas, agendar, pacote, avaliar, privacidade, perfil; seletor de unidade; avisos; perfil no celular). `gerador/s10.py`.
- [x] PNGs, galeria (HTML e PDF), zip e protótipo regenerados; verificação de navegação sem links quebrados.
- [ ] Pendente: estados C26 na home (sem sessão, sessão hoje, atraso, pacote acabando); versões de celular desenhadas de avaliar, avisos e seletor de unidade (hoje usam o casco responsivo); troca da senha do protótipo recomendada.
- [x] Checagens finais: render 79 telas sem problema; checa_layout 0 de 316 combinações com problema grave (0 avisos); navegação 81 páginas, 0 links quebrados, 0 erros, 0 transbordo em 390, 17 de 17 testes ok.
- [x] Deploy único em produção 21/11 11h28 (horário de Brasília): fb57808c-47e0-45da-97bb-aa3b99e80ba5. curl: 401 sem credencial e com senha errada, 200 com a senha do env em 7 rotas, robots 200, X-Robots-Tag noindex no 401 e no 200.

## Rodada 3.5 (21/11/2026, 11h52 a 13h): formulários esticados e telas de acesso no celular
- [x] Causa: a regra nova de alinhamento dos campos (subgrid em `.campo` + `container-type:inline-size` em todo `.campo`) vazou para fora do painel. Nos formulários em coluna (landings 37 a 42) o `container-type` fazia o Chrome esticar cada campo até a altura do herói (campo de 469 px para 70 px de conteúdo); no painel, o subgrid esticava campos vizinhos (07 e-mail, 12, 25 coordenadas e cidade).
- [x] Correção: removidos subgrid e container query dos campos. Layout simples: rótulo, caixa e ajuda em coluna; grades com `align-items:start`; no painel (701 px ou mais) rótulo em uma linha com texto completo no title, selos só com ícone em grades de 3 e 4 colunas; abaixo de 700 px toda grade de formulário vira uma coluna; cards de formulário em grade ficam na altura do próprio conteúdo.
- [x] Camada do protótipo (≤1100 px): a regra que punha toda grade em uma coluna deixou de quebrar o seletor de perfil do login (.sw), o calendário (7 colunas) e os horários da 72; checkbox e texto não se separam mais; KPIs e formulários usam várias colunas no tablet.
- [x] 01, 02, 03: telas de acesso responsivas (classes .acesso, .acesso-form, .acesso-pg); 02 com 6 caixas fluidas numa linha a partir de 360 px, números tabulares sem quebra (.num), SMS mascarado com contador e código de recuperação, botões em largura total no celular.
- [x] checa_layout.py: larguras 360, 390, 768, 1024, 1280, 1440, 1920, com e sem ?fixo=1; checagem nova FORM_ESTICADO (campo mais alto que o conteúdo, vão > 48 px entre campos seguidos, card de formulário com sobra > 48 px que não vem da altura da linha).
- [x] Conferência visual: recortes dos formulários em `revisao-layout/formularios/` (390, 1024, 1440) e folhas de contato.
