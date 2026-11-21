# Feature Specification: Quiz, inteligência de dados e tracking limpo

**Feature Branch**: `003-quiz-inteligencia-tracking`
**Created**: 2026-11-21
**Status**: Draft (rev. 1, 21/11/2026: quiz, dados correlatos, tracking; rev. 1a 09h30: gerenciador de tags por unidade; rev. 1b 09h33: guia de configuração em wiki e vídeo como entregável futuro; rev. 1c 09h42: decisões do Osmar, ver `decisoes.md` e `respostas-osmar-2026-11-21.md`)
**Depende de**: `001-sistema-unidades` (unidades, RBAC, política de campos, Wiki, insights, eventos), `002-area-cliente` (cliente, interesses, consentimentos, campanhas, controles da rede)
**Anexos**: `pesquisa.md` (fontes linkadas e custos), `data-model.md`, `telas.md`, `decisoes.md`, `resumo.md`, `impacto-na-001-002.md`
**Input**: Osmar, 21/11/2026 09h26: "A franqueada ou a rede pode enviar campanhas do tipo Quizz (precisamos criar um gerador pra isso). Com isso conseguimos conhecer mais dos clientes e quais procedimentos eles mais buscam, cruzar com a idade, cidade, clima do ano (quente, frio, sazonalidades)... Busque mais dados correlatos... Me preocupa também o trackeamento de tudo, de forma limpa e precisa." 09h30: gerenciador de tags na área de SEO de cada unidade (GA4, Search Console e outras), sem duplicar scripts. 09h33: guia de configuração em documento na Wiki e vídeo.

## Contexto
- Hoje o tracking está quebrado (diagnóstico, achados 6 a 8): conversão disparada no clique, UA desligado ainda no código, 17 fichas com GTM extra, PII em cookie, dataLayer e URL, consentimento pré-marcado, nenhum evento com a unidade.
- A 001 já fixa: conversão só no servidor (III), sem PII em analytics (VII), fim dos scripts por unidade (FR-025), eventos padronizados (FR-009).
- A 002 cria cliente, interesses, consentimento por canal, campanhas com assistente e controles da rede com padrão bloqueado.

## Princípios afetados
I, III, V, VII, VIII, IX, X, XI, XIII da constituição, mais XIV e XV propostos na 002. Novo princípio proposto aqui: **XVII. Medição é contrato** (ver `impacto-na-001-002.md`).

## Papéis
| Papel | O que faz nesta spec |
|---|---|
| Rede: R-MKT | Cria modelos de quiz, aprova quiz de unidade, usa a inteligência |
| Rede: R-SEO / dono do tracking (novo papel funcional, D15) | Mantém o plano de medição, o gerenciador de tags, destinos e UTMs; aprova tags de unidade |
| Rede: R-ADM | Libera funções por escopo (002, US17), inclusive "criar quiz" e "tags próprias" |
| Unidade (U-FRQ, U-GER) | Cria quiz a partir de modelo se liberado; preenche campos tipados de tags (GA4 próprio, verificação do Search Console, pixels) conforme política |
| Agência (R-AG) | Lê agregados e o plano de medição; propõe eventos e UTMs; nunca dado pessoal |
| Visitante e cliente | Responde quiz; escolhe consentimentos no banner e na central de privacidade |

---

## Parte A. Gerador de quiz

### US1. Rede cria modelos de quiz (P1)
Como R-MKT quero montar quizzes num editor visual a partir de modelos (ex.: "Qual tratamento combina com você", "Seu momento para depilação a laser", "Objetivo corporal"), para conhecer interesses e recomendar procedimentos.
**Acceptance**
1. Given o editor, When adiciono perguntas (escolha única, múltipla, escala, imagem, faixa etária, cidade), Then cada pergunta tem chave estável, texto, opções com chave e ordem, e pode ser marcada como obrigatória.
2. Given perguntas, When defino ramificação (se resposta X, vá para pergunta Y ou para o fim), Then o editor mostra o fluxo em grafo e bloqueia ciclos e caminhos sem fim.
3. Given regras de recomendação (cada opção soma pontos a procedimentos ou categorias do catálogo), When o quiz termina, Then o resultado mostra de 1 a 3 procedimentos com texto aprovado e CTAs (agendar avaliação gratuita, ver ofertas, salvar resultado).
4. Given uma pergunta com termo de saúde (gravidez, doença, medicamento, alergia, condição de pele médica), When salvo, Then o validador bloqueia na fase 1 (D7 e D8 da 002) e explica o motivo.
5. Given quiz publicado, When edito, Then nasce uma nova versão; respostas antigas continuam ligadas à versão em que foram dadas.

### US2. Unidade cria quiz a partir de modelo, se liberada (P2)
**Acceptance**
1. Given função "quiz da unidade" bloqueada (padrão), When a unidade abre Quizzes, Then vê os quizzes da rede disponíveis para divulgar e o atalho "pedir liberação".
2. Given função liberada, When a unidade duplica um modelo, Then só altera campos livres do modelo (textos de abertura, ordem de procedimentos que oferece, CTA local) e envia para aprovação da rede.
3. Given o quiz aprovado, Then o alcance de distribuição respeita o teto da unidade (002, FR-143).

### US3. Distribuição do quiz como campanha e em pontos fixos (P1)
**Acceptance**
1. Given um quiz publicado, When crio uma campanha no assistente da 002 (objetivo "conhecer interesses"), Then o quiz é o conteúdo, com canais, segmento, cotas, frequência e aprovação da 002.
2. Given pontos fixos, Then o quiz pode ser embutido na landing da unidade (bloco opcional do template), na área do cliente, por link curto com UTM e por QR code na recepção.
3. Given distribuição por unidade, Then cada resposta leva `unidade_id` de origem e a campanha.

### US4. Consentimento e finalidade declarada (P1)
**Acceptance**
1. Given um visitante anônimo, When abre o quiz, Then a tela inicial diz para que servem as respostas ("recomendar tratamentos e mostrar ofertas certas para você") e o link da política; responder não exige cadastro.
2. Given quiz anônimo concluído, Then as respostas ficam ligadas só a um `anon_id` e entram nos agregados; para salvar o resultado e receber ofertas, a pessoa cria conta (002, US1) com o consentimento de personalização desmarcado por padrão.
3. Given cliente logado sem consentimento de personalização, Then as respostas ficam no histórico dele, mas não entram em segmentação até ele consentir (002, FR-111).
4. Given finalidade nova (ex.: usar respostas para pesquisa de expansão), Then precisa de novo texto legal e novo aceite.

### US5. Respostas viram perfil de interesse (P1)
**Acceptance**
1. Given um cliente com consentimento, When conclui o quiz, Then cada procedimento recomendado e cada interesse declarado vira `interesse_cliente` com origem "quiz", peso e data, com decaimento (peso cai com o tempo; padrão: metade em 180 dias).
2. Given barreiras declaradas (preço, dor, tempo, medo de resultado), Then ficam como atributos de perfil usados em segmentação e em mensagens (ex.: explicar parcelamento para quem marcou preço).
3. Given o cliente abre "por que estou vendo isso", Then vê que a oferta veio do quiz e pode apagar as respostas.

### US6. Aprovação e validação (P1)
**Acceptance**
1. Given quiz de unidade, Then vai para a fila de R-MKT com prévia do fluxo e do resultado; quem cria não aprova.
2. Given textos de resultado, Then passam pelo validador de publicidade da marca (002, FR-120): sem promessa de resultado, sem antes e depois, sem marca de equipamento.

### US7. Resultados do quiz (P1)
**Acceptance**
1. Given um quiz, When abro resultados, Then vejo funil (visualizou, iniciou, por pergunta com abandono, concluiu, salvou, cadastrou, agendou, comprou) e distribuição das respostas.
2. Given cruzamentos, Then posso abrir respostas por faixa etária, cidade, UF, unidade, estação e clima do dia (temperatura e UV), sempre agregadas e com amostra mínima de 30 respostas por célula (abaixo disso, a célula fica oculta).

---

## Parte B. Inteligência com dados correlatos

### US8. Catálogo de fontes externas e ingestão agendada (P1)
**Acceptance**
1. Given o catálogo de fontes (ver `pesquisa.md`), Then cada fonte tem dono, licença, custo, frequência, granularidade e status da última coleta.
2. Given rotina diária ou mensal, Then a ingestão grava séries por município IBGE e data (clima, UV, feriados, demografia, PIB, tendências), com reprocessamento e alerta de falha.
3. Given fonte paga ou com licença não comercial (ex.: Open-Meteo grátis), Then a fonte fica desligada até decisão (D10).

### US9. Painel de demanda e sazonalidade (P1)
**Acceptance**
1. Given rede, When abro "Demanda", Then vejo procedimentos mais buscados (quiz, busca interna, cliques no catálogo, agendamentos, Search Console e Trends) por UF, cidade, faixa etária e mês, com fonte e período em cada número (princípio X).
2. Given clima, Then vejo curvas de demanda x temperatura média e índice UV por cidade, e a normal climatológica para comparar.
3. Given potencial, Then vejo penetração (clientes por mil mulheres de 20 a 49 anos, Censo 2022) por unidade e cidades sem unidade com demanda.
4. Given unidade, Then vê só a própria região e a mediana da rede.

### US10. Recomendações automáticas (P2)
**Acceptance**
1. Given regras (ex.: "queda de 3 °C na média semanal + histórico de pico de depilação no inverno"), When disparam, Then o sistema cria um insight (001, FR-028) com explicação, fonte, amostra e ação sugerida ("usar campanha modelo X nas unidades do Sul").
2. Given a ação sugerida, When a rede clica, Then abre o assistente de campanha (002, US19) já preenchido, ou o "replicar" (002, US20).
3. Given recomendação para unidade, Then só aparece se a função estiver liberada e dentro da cota.
4. Given recomendação descartada ou usada, Then o resultado alimenta a avaliação da regra (taxa de acerto).

---

## Parte C. Tracking limpo

### US11. Plano de medição e dicionário de eventos versionado (P1)
**Acceptance**
1. Given o plano de medição, Then cada pergunta de negócio tem os KPIs e os eventos que a respondem.
2. Given o dicionário (tracking plan) como fonte única, Then cada evento tem nome `objeto_acao` em pt-BR no particípio (ex.: `lead_iniciado`, `agendamento_concluido`, `quiz_concluido`), descrição, gatilho, onde dispara (navegador, servidor, app), propriedades com tipo e obrigatoriedade, dono, versão, status (proposto, aprovado, ativo, obsoleto) e mapeamento para destinos (GA4, Meta, Google Ads, TikTok).
3. Given mudança no dicionário, Then gera versão nova, entrada de changelog e pede aprovação do dono do tracking; nada vai a produção sem QA (US18).
4. Given o dicionário, Then o sistema gera os schemas (JSON Schema) e os tipos usados pelo site, pelo app e pelo servidor.

### US12. Coleta first-party com consentimento num só ponto (P1)
**Acceptance**
1. Given qualquer página da rede ou da unidade, Then existe um único carregador de tags (loader) e um único banner de consentimento por marca, sem script livre de unidade.
2. Given o banner, Then segue o guia da ANPD (finalidades por categoria, recusa real, nada pré-marcado, revogação fácil) e alimenta o Consent Mode v2 antes de qualquer tag.
3. Given um evento, Then vai para o coletor próprio no nosso domínio, que valida o schema, carimba `ts_servidor`, `marca`, `unidade_id` e o estado de consentimento, grava no banco e só então distribui aos destinos permitidos pelo consentimento.
4. Given conversão (lead, agendamento, compra, cadastro), Then nasce no servidor depois da resposta 2xx (princípio III) e é enviada por Measurement Protocol, Meta CAPI, Google Ads Data Manager API e TikTok Events API com o mesmo `event_id` usado no navegador (deduplicação).

### US13. UTMs padronizadas com gerador e validação (P1)
**Acceptance**
1. Given o gerador, When crio um link, Then escolho de listas fechadas `utm_source`, `utm_medium` e `utm_campaign` no padrão `marca_unidade-ou-rede_objetivo_aaaamm_nome` em minúsculas sem acento, e o link curto fica registrado com dono.
2. Given chegada com UTM fora do padrão, Then o coletor marca `utm_invalida`, normaliza o que der (caixa, acento) e o painel de qualidade lista as origens a corrigir.
3. Given campanha da 002, Then as UTMs são geradas sozinhas.

### US14. Identidade e costura de jornada (P1)
**Acceptance**
1. Given visitante, Then recebe `anon_id` first-party (só com consentimento de analytics; sem ele, só eventos sem identificador persistente).
2. Given cadastro ou login, Then o servidor liga `anon_id` a `cliente_id` numa tabela de identidade; analytics recebe só `cliente_hash` (por marca, com sal da marca).
3. Given multimarca, Then Gio e Sorridents têm identidades separadas (D9 da 002); nada liga um cliente entre marcas.
4. Given lead e unidade, Then todo evento leva `unidade_id` de contexto (página da unidade, unidade escolhida no formulário ou unidade preferida).

### US15. Deduplicação (P1)
**Acceptance**
1. Given o mesmo evento chegando duas vezes (duplo clique, retry, navegador e servidor), Then o coletor descarta pela chave `event_id` em janela de 48 h e os destinos recebem o mesmo `event_id`.
2. Given conversões no Google Ads, Then há uma só conversão primária por ação, as demais como secundárias.

### US16. Validação automática e alertas de quebra (P1)
**Acceptance**
1. Given um evento fora do schema, Then vai para a fila de inválidos com o motivo, e o painel de qualidade mostra taxa de inválidos por evento e versão.
2. Given monitoramento, Then alerta quando: volume de um evento cai ou sobe mais que X% contra a média de 4 semanas do mesmo dia da semana; uma unidade para de emitir `agendamento_concluido`; taxa de inválidos passa de 1%; aparece PII em propriedade (detector de e-mail, telefone, CPF).
3. Given CI do código, Then testes de contrato verificam que cada chamada de evento bate com o schema da versão ativa; Measurement Protocol é testado no endpoint de validação.

### US17. Atribuição por unidade e campanha, com conversões offline (P1)
**Acceptance**
1. Given o modelo de atribuição da 002 (D5e), Then o mesmo modelo vale para todas as unidades e aparece escrito em todo painel.
2. Given status vindo da DocBiz (compareceu, comprou), Then vira evento de servidor e volta ao Google Ads (Data Manager API, com gclid ou dados com hash e consentimento) e à Meta (CAPI).
3. Given painel, Then vejo lead e venda por unidade, campanha, canal e quiz, com a mesma régua.

### US18. Governança e QA (P1)
**Acceptance**
1. Given o plano, Then há um dono do tracking, um changelog público interno e um ritual de revisão mensal.
2. Given mudança, Then passa por ambiente de homologação com propriedade GA4 de teste, checklist de QA (evento dispara, schema válido, consentimento respeitado, sem PII, destinos recebem, deduplicação ok) e só então publica.
3. Given publicação, Then a versão do contêiner e do dicionário fica registrada e é reversível.

### US19. Armazenamento próprio e warehouse (P1)
**Acceptance**
1. Given evento válido, Then fica no nosso banco (tabela particionada por dia) com retenção definida (D13) e cópia fria mensal em Parquet.
2. Given análise, Then os painéis da 001, 002 e 003 leem do nosso banco ou de um warehouse alimentado por ele, não do GA4.
3. Given GA4, Then o export para BigQuery fica ligado como segunda fonte e para auditoria, sabendo do limite de 1 milhão de eventos por dia na versão padrão.

---

## Parte D. Gerenciador de tags na área de SEO da unidade (09h30)

### US20. Rede define destinos e tags com campos tipados (P1)
Como dono do tracking quero ligar ferramentas por campos tipados, nunca por script colado, para que rede e unidade tenham dados sem duplicar scripts.
**Acceptance**
1. Given a área "Tags e medição" da rede, Then configuro os destinos da rede: GA4 da marca (com dimensões `unidade_id`, `unidade_nome`, `template`, `variante`), Google Ads da rede, Meta Pixel e CAPI da rede, TikTok Pixel e Events API da rede, Search Console (propriedade de domínio) e o coletor próprio.
2. Given campos tipados, Then cada tipo tem validação de formato: GA4 `G-` + alfanumérico; Google Ads `AW-` + dígitos e rótulo de conversão; Meta Pixel só dígitos (15 a 16); TikTok Pixel alfanumérico; meta tag do Search Console só o conteúdo do atributo `content` de `google-site-verification`; Measurement Protocol `api_secret` guardado como segredo.
3. Given "script livre", Then fica bloqueado por padrão (001, FR-025) e só existe como pedido à rede, com revisão de segurança, peso e LGPD.

### US21. Unidade preenche as próprias tags dentro da política (P1)
**Acceptance**
1. Given política de campos (001, US13), Then os campos de tags da unidade nascem T (travado); a rede pode torná-los EA por unidade ou regional.
2. Given GA4 próprio da unidade liberado, When a unidade informa `G-XXXX` e o `api_secret`, Then o loader passa a enviar page_view e medição aprimorada também para esse destino, e os eventos de conversão vão por servidor com `send_to` explícito (ou Measurement Protocol), filtrados para aquela unidade. Nunca se injeta um segundo gtag.js.
3. Given Search Console da unidade, Then o padrão é a rede criar a propriedade por prefixo `/unidade/<slug>/` (verificada automaticamente como filha da propriedade de domínio) e conceder acesso de usuário à unidade. O campo de meta tag serve para unidade que quer ser dona do prefixo ou que usa domínio próprio; o sistema imprime a tag só no `<head>` da página inicial do prefixo ou do domínio.
4. Given Meta ou TikTok da unidade, Then a recomendação é envio só por servidor (sem pixel na página), com o mesmo `event_id`.
5. Given qualquer tag da unidade, Then respeita o consentimento único: destino de anúncio só recebe se `ad_storage` e `ad_user_data` concedidos; GA4 só com `analytics_storage`.
6. Given publicação de tag, Then o sistema mede o impacto estimado de peso e requisições e bloqueia se a landing cair abaixo do piso de Lighthouse mobile 90 (princípio IX).

### US22. Limites conhecidos explicados na tela (P1)
**Acceptance**
1. Given a tela de GA4, Then explica que o GA4 padrão não dá permissão por unidade dentro de uma propriedade; subpropriedades exigem Analytics 360. Por isso a unidade vê os números no painel da plataforma e, se quiser GA4, numa propriedade própria.
2. Given a tela de server-side, Then mostra a opção recomendada e os custos coletados em `pesquisa.md`.

## Parte E. Guia de configuração (entregável futuro, 09h33)

### US23. Guia do gerenciador de tags e do rastreamento na Wiki e em vídeo (P2, fase de lançamento da Wiki)
**Acceptance**
1. Given a Wiki da 001 (US14), Then existe a trilha "Medição e tags" com artigos por perfil: rede (GA4 da marca, dimensões de unidade, destinos, server-side, Consent Mode, UTMs, dicionário), unidade (GA4 próprio, Search Console por prefixo ou domínio próprio, pixels por servidor, o que não fazer) e agência.
2. Given cada artigo, Then tem um vídeo explicativo curto (tela gravada com narração) ligado pelo campo `video_url` do artigo, legenda em pt-BR e data da versão da interface.
3. Given mudança na tela ou no dicionário, Then o artigo e o vídeo afetados ficam marcados "revisar" até serem atualizados.
4. Given ajuda contextual (001, princípio XIII), Then cada tela de Tags e medição leva ao artigo e ao vídeo correspondentes.

---

## Requisitos funcionais
**Quiz**
- FR-201 Editor visual de quiz com tipos de pergunta, chaves estáveis, obrigatoriedade, ramificação em grafo com verificação de ciclos e caminhos sem fim.
- FR-202 Motor de recomendação por pontos (opção > procedimento ou categoria), com empate resolvido pela oferta da unidade e pelo destaque da rede; resultado com 1 a 3 procedimentos e CTAs.
- FR-203 Biblioteca de modelos de quiz da rede com campos travados e livres, escopos e versão.
- FR-204 Quiz da unidade só se liberado (002, FR-142), por duplicação de modelo, com aprovação da rede.
- FR-205 Validador de perguntas: lista de termos de saúde bloqueados na fase 1; validador de publicidade nos resultados.
- FR-206 Distribuição como conteúdo de campanha (002, FR-149), bloco de landing, área do cliente, link curto e QR, sempre com UTM e `unidade_id`.
- FR-207 Resposta anônima com `anon_id`; vínculo ao cliente só com conta; segmentação só com consentimento de personalização.
- FR-208 Conversão de respostas em `interesse_cliente` (origem quiz, peso, decaimento) e atributos de barreira; apagar respostas pela central de privacidade.
- FR-209 Resultados com funil, abandono por pergunta e cruzamentos agregados com amostra mínima de 30 por célula.
- FR-210 Versões de quiz imutáveis depois de publicadas.

**Inteligência**
- FR-211 Catálogo de fontes externas com dono, licença, custo, frequência e status; fonte não comercial ou paga desligada até decisão.
- FR-212 Ingestão agendada por município IBGE e data: clima diário (INMET), normais climatológicas, UV e previsão (se licenciado), feriados, calendário comercial, demografia e PIB (IBGE), tendências (Trends), GBP Performance (com acesso concedido pela unidade).
- FR-213 Tabela de calendário comercial mantida pela rede (nacional, UF, município).
- FR-214 Painel de demanda e sazonalidade com fonte e período em cada número; amostra mínima.
- FR-215 Motor de regras de recomendação gerando insights (001, FR-028) com ação que abre campanha ou replicar (002).
- FR-216 Avaliação de regras (acerto, uso, descarte).

**Tracking**
- FR-217 Plano de medição e dicionário de eventos versionados, com status, dono, changelog e aprovação; geração de JSON Schema e tipos.
- FR-218 Nomenclatura `objeto_acao` em pt-BR no particípio, propriedades em snake_case, sem nome dinâmico; mapeamento para eventos recomendados dos destinos.
- FR-219 Propriedades obrigatórias em todo evento: `event_id`, `event_name`, `schema_versao`, `ts_cliente`, `ts_servidor`, `marca`, `ambiente`, `plataforma`, `anon_id` (se consentido), `sessao_id`, `pagina_tipo`, `consentimento`; e, quando houver contexto, `unidade_id`, `template`, `variante_id`, `campanha_id`, `quiz_id`. Nunca PII.
- FR-220 Loader único por marca com Consent Mode v2 e banner conforme guia da ANPD, versão do texto registrada (002, FR-107).
- FR-221 Coletor first-party no domínio da marca, com validação de schema, carimbo do servidor, deduplicação por `event_id` (48 h), fila de inválidos e gravação no banco.
- FR-222 Distribuição server-side: GA4 Measurement Protocol (rede e unidade), Meta CAPI, Google Ads Data Manager API, TikTok Events API; só para destinos permitidos pelo consentimento; dados de usuário só com hash SHA-256 normalizado e base legal.
- FR-223 Gerador de UTMs com listas fechadas, padrão de nome, link curto, dono; normalização e marcação de UTM inválida na chegada.
- FR-224 Identidade: `anon_id`, `sessao_id`, `cliente_id` e `cliente_hash` por marca; costura no servidor; nenhuma ligação entre marcas.
- FR-225 Conversões offline vindas da DocBiz (compareceu, comprou) como eventos de servidor e envio aos destinos de anúncio.
- FR-226 Painel de qualidade: volume por evento, inválidos, PII detectada, UTMs inválidas, unidades sem conversão, divergência coletor x GA4.
- FR-227 Alertas de quebra por desvio de volume, ausência por unidade, inválidos acima de 1% e PII detectada.
- FR-228 Testes de contrato no CI e validação no endpoint de debug do Measurement Protocol.
- FR-229 Ambientes de homologação com propriedades de teste; checklist de QA obrigatório antes de publicar.
- FR-230 Armazenamento próprio particionado com retenção configurável e arquivo frio em Parquet; export GA4 para BigQuery como segunda fonte.

**Gerenciador de tags**
- FR-231 Área "Tags e medição" na rede e na aba SEO da ficha da unidade, com campos tipados e validados para GA4, Search Console, Google Ads, Meta Pixel e CAPI, TikTok Pixel e Events API.
- FR-232 Script livre bloqueado por padrão; pedido à rede com revisão de segurança, peso e LGPD.
- FR-233 Política de campos para tags (T por padrão; EA por escopo), integrada à 001.
- FR-234 Um único gtag.js por página; destinos extras por configuração; eventos de conversão por servidor com destino explícito.
- FR-235 Search Console: propriedade de domínio da rede; prefixo por unidade criado pela rede com acesso de usuário; meta tag de verificação só para dono de prefixo ou domínio próprio, impressa só na página inicial do prefixo ou domínio.
- FR-236 Orçamento de performance por landing: estimativa de peso e requisições por tag; bloqueio abaixo do piso de Lighthouse 90.
- FR-237 Textos de ajuda com os limites do GA4 (sem permissão por unidade; subpropriedades só no 360) e custos do server-side.

**Guia**
- FR-238 Trilha "Medição e tags" na Wiki com artigos por perfil (rede, unidade, agência) e vídeo explicativo por artigo, legendado, com data de versão da interface; marcação automática "revisar" quando a tela ou o dicionário mudam.

## Success Criteria
- SC-201 100% dos eventos em produção definidos no dicionário ativo; zero evento com nome fora do padrão.
- SC-202 Taxa de eventos inválidos abaixo de 1% por semana.
- SC-203 Zero PII detectada em propriedades de evento, cookies de marketing, dataLayer ou URLs (varredura diária).
- SC-204 Divergência entre conversões do coletor e da DocBiz abaixo de 2% por mês.
- SC-205 100% das conversões de Ads, Meta e GA4 vindas de eventos de servidor com `event_id` deduplicado.
- SC-206 Zero página com mais de um gtag.js ou GTM; zero script livre de unidade sem aprovação.
- SC-207 Todas as landings com Lighthouse mobile de pelo menos 90 com as tags ligadas.
- SC-208 Pelo menos 95% das sessões com UTM válida quando vierem de campanha própria.
- SC-209 Taxa de conclusão de quiz de pelo menos 60% entre quem inicia (meta inicial).
- SC-210 Pelo menos 30% dos clientes com perfil de interesse vindo do quiz em 12 meses.
- SC-211 Alertas de quebra disparados em até 1 hora após a quebra.
- SC-212 Guia "Medição e tags" publicado na Wiki com vídeo antes da abertura do gerenciador de tags às unidades.

## Fora de escopo agora
- Perguntas de saúde e anamnese (fase futura com RIPD, D7 da 002).
- Modelos de previsão por aprendizado de máquina (a fase 1 usa regras explicáveis).
- Compra de dados de terceiros.
- Analytics 360 e subpropriedades.
- Produção do guia e dos vídeos (registrado como entregável futuro, US23).

## Backlog e fases (alinhado à 001 e à 002)
| Fase | Itens |
|---|---|
| 0 (site atual, já recomendado no diagnóstico) | Evento confirmado no servidor, consentimento desmarcado, retirar PII de cookie, dataLayer e URL, limpar GTMs de unidade |
| 1 (com o MVP da 001) | Dicionário v1 e plano de medição, loader único, banner ANPD + Consent Mode v2, coletor próprio, Measurement Protocol e Meta CAPI da rede, UTMs, painel de qualidade básico, gerenciador de tags da rede, Search Console por prefixo |
| 2 (com a fase 1 da 002) | Quiz da rede, interesses do quiz, identidade de cliente, Data Manager API com conversões offline, TikTok, alertas de quebra |
| 3 (com a Wiki da 001 no lançamento às unidades) | **Guia "Medição e tags" na Wiki e vídeos (US23, FR-238)** e, logo depois, o gerenciador de tags da unidade (GA4 próprio, pixels por servidor, meta tag do Search Console) |
| 4 | Quiz de unidade, fontes externas e painel de demanda, recomendações automáticas, warehouse |

## Decisões do Osmar (rev. 1c, 21/11/2026, 09h42)
- Coletor próprio no nosso domínio (D5 = E), com validação, deduplicação, gravação no nosso banco e envio pelo servidor para GA4, Meta, TikTok e Google Ads.
- Analytics da rede (D7): uma propriedade por marca, unidade como dimensão. **Requisito novo do domínio próprio:** quando a unidade tiver domínio próprio, o provisionamento do domínio só conclui depois que a rede recebe acesso ao GA4 e ao Search Console da unidade (usuário da rede com leitura no GA4 e proprietário delegado ou usuário completo no Search Console). Isso aparece no assistente de domínio próprio (001, tela 31) e no gerenciador de tags da unidade (T11).
- Quiz da fase 1 aprovado (D1 a D4): só estética e preferência, sem saúde, unidade só a partir de modelo, sem incentivo.
- Dono do tracking (D15): pessoa nomeada na Gio.
- Retenção de 25 meses de eventos brutos (D13); fontes pagas desligadas (D10, D11, D14); Google Trends por exportação manual (D12).
- Continuam abertas: D6 (onde guardar eventos), D8 (banner) e D9 (nomenclatura, já aplicada na 001).

