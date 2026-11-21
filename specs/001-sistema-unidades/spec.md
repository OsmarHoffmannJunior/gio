# Feature Specification: Plataforma de Unidades Gio (substitui o AGDM)

**Feature Branch**: `001-sistema-unidades`
**Created**: 2026-11-21
**Status**: Draft (rev. 3.3, 21/11/2026: auditoria geral só para a rede (US21, FR-036, SC-011); rev. 3.2: integração das specs 002 e 003, eventos renomeados para `objeto_acao`, constituição 1.4.0; rev. 3.1: contas internas só por convite e provisionamento da unidade; override da rede, RBAC, política de campos, schema da rede; Wiki, relatórios inteligentes, módulos, modelos de ficha, variantes de landing; GBP da unidade; rede controladora LGPD)
**Anexos**: `rbac.md` (matriz de permissões), `politica-campos.md` (política campo a campo), `dados-ficha.md` (inventário de todos os dados da ficha), `data-model.md`, `telas.md`
**Input**: Pedido do Osmar: "sistema robusto, completo, moderno e corporativo"; franqueado com login; landing de alta conversão com 3 templates editáveis por bloco; domínio próprio; painel com filtros, origem e jornada do lead, acesso por unidade, gráficos, relatórios e suporte integrado; SEO local. Base: `relatorio-diagnostico.md`, `agdm/mapa-agdm.md`, `custos/custos.md` e a Page "Gio: proposta do novo sistema de unidades".

## Contexto (o que existe hoje, AGDM da DocPix)
- Telas: dashboard (unidades ativas, acessos, agendamentos/mês), agendamentos (Status, ID DocBiz, Nome, E-mail, Unidade, datas; sem telefone), restrições de horário, unidades (cadastro), relatórios (7), usuários por cargo, empresa, perfil, suporte para a DocPix.
- Cadastro real da unidade: Ativo, Unidade DocBiz, nome, CRO, telefone, WhatsApp, e-mail, inauguração, texto de não inaugurada, permitir agendamentos, endereço (CEP, UF, cidade, bairro, logradouro, número, complemento, referência), Facebook, Instagram, descrição de serviços, horário de funcionamento (linhas), horário de agendamento (seg a dom), URL do site; imagens (jpg até 2 MB, fachada, ordem); tratamentos (marcar no catálogo global); Confs. Site (meta keywords/description, scripts head/body, Agendamento Conclusão, Formulário ID).
- Lacunas: sem login de franqueado, sem vínculo usuário e unidade, sem coordenadas, sem title/canonical/schema, sem origem detalhada nem jornada do lead, sem SLA, sem tickets da unidade.

## Papéis
Os papéis viram perfis RBAC (perfil x escopo x módulo x ação). A matriz completa está em `rbac.md`.

| Nível | Perfil padrão | Escopo | Resumo |
|---|---|---|---|
| Rede | Admin da rede (R-ADM) | Rede | Configura marca, perfis, schema base; edita qualquer unidade sem fila |
| Rede | Marketing (R-MKT) | Rede ou regional | Conteúdo, templates, landings; aprova conteúdo; edita direto com aviso |
| Rede | SEO (R-SEO) | Rede | Dados estruturados, SEO técnico, NAP, domínio, GBP; aprova SEO |
| Rede | Comercial/Atendimento (R-COM) | Rede | Leads, SLA e distribuição |
| Rede | Call center (R-CC) | Rede ou regional | Opera a fila atribuída |
| Rede | Financeiro/Leitura (R-FIN) | Rede | Indicadores e relatórios, sem dado pessoal |
| Rede | Agência (R-AG, externo) | Rede ou regional | Analytics, campanhas, SEO com aprovação; nunca dado pessoal |
| Regional | Gestor regional (G-REG) | Lista de unidades | Acompanha e cobra a região |
| Unidade | Franqueado (U-FRQ) | 1 ou N unidades (multifranqueado) | Edita conforme a política; convida a equipe |
| Unidade | Gerente da unidade (U-GER) | Unidade | Operação: ficha, landing, leads |
| Unidade | Recepcionista (U-REC) | Unidade | Atende leads; vê a ficha |
| Público | Cliente final | Os próprios atendimentos, conta, agendamentos, compras e privacidade (spec 002) | Usa a área do cliente da spec 002; abre e acompanha solicitações de suporte. Clientes se cadastram sozinhos: a regra de convite (US20) vale só para usuários internos |

## User Scenarios & Testing

### US1. Admin Gio enxerga e filtra a rede inteira (P1)
Como Admin Gio quero listar as 130 unidades com filtros (UF, cidade, status, completude, desempenho, domínio próprio, template, alertas de SEO/tracking) em tabela e mapa, para agir onde há problema.
**Independent Test**: com a base importada do AGDM, filtrar "SP + completude < 60% + sem fotos" e exportar CSV.
**Acceptance**
1. Given 130 unidades, When aplico 3 filtros, Then a tabela e o mapa mostram o mesmo subconjunto e o contador atualiza.
2. Given um filtro aplicado, When salvo como "visão", Then ela aparece no menu de visões e pode ser compartilhada com outro admin.
3. Given uma unidade sem coordenadas, When abro o mapa, Then ela aparece na lista "fora do mapa" com alerta.

### US2. Franqueado edita a própria unidade (P1)
Como franqueado quero editar dados, horários, fotos, equipe, tratamentos e FAQ da minha unidade, para manter a página correta sem pedir à Gio.
**Acceptance**
1. Given login de franqueado, When abro o sistema, Then vejo só a minha unidade (ou grupo, se multifranqueado).
2. Given edição de um campo **E** (horário, foto comum, texto Sobre, equipe, promoção por modelo), When salvo e o validador passa, Then publica na hora, landing e schema atualizam e o log registra antes e depois.
3. Given edição de um campo **EA** (telefone, foto de fachada, antes e depois, área atendida, template), When salvo, Then entra em "aguardando aprovação" na fila do perfil de rede indicado e não publica.
3b. Given campo **T** (nome, endereço, schema, title, scripts), When abro, Then vejo cadeado, o motivo e o atalho "pedir alteração" (abre chamado).
4. Given completude abaixo de 80%, When abro "Minha unidade", Then vejo a lista do que falta com ganho estimado em pontos.

### US3. Landing de alta conversão por templates (P1)
Como franqueado quero escolher um entre 3 templates (A Conversão direta, B Vitrine da clínica, C Autoridade local) e editar bloco a bloco, com preview mobile e desktop.
**Acceptance**
1. Given template escolhido, When reordeno ou desligo um bloco opcional, Then o preview atualiza em menos de 1 s.
2. Given bloco travado (marca, rodapé legal, formulário), When tento editar, Then vejo cadeado e o motivo.
3. Given texto com valor em R$ ou marca de equipamento, When publico, Then o validador bloqueia e aponta a regra.
4. Given mudança em item EA, When envio, Then vai para a fila de aprovação do perfil indicado na política (R-MKT ou R-SEO) com diff visual; itens E publicam direto.

### US4. Central de leads com origem, jornada e SLA (P1)
Como unidade e call center quero ver os leads em kanban e lista, com origem (canal, UTM, campanha), jornada no site em linha do tempo e SLA de primeiro contato.
**Acceptance**
1. Given lead novo, When chega, Then entra em "Novo" com contador de SLA e notificação para quem está na distribuição.
2. Given lead sem horário escolhido (equivalente ao ABERTO do AGDM), When passa X minutos, Then vai para a fila do call center.
3. Given lead agendado, When a DocBiz confirma, Then o card mostra ID DocBiz e status sincronizado (agendado, compareceu, não compareceu).
4. Given abro o lead, Then vejo a linha do tempo: primeira visita, páginas, campanha, formulário etapa 1, etapa 2, contato, agendamento.
5. Given papel agência, When abro leads, Then só vejo agregados, sem nome, e-mail ou telefone.
6. Given lead verificado, When o cliente cria conta ou já tem conta (spec 002), Then o lead se liga ao cliente (`lead.cliente_id`), o card mostra "já é cliente" e a jornada continua na linha do tempo do cliente.

### US5. Dashboards da rede e da unidade (P1)
Como Admin quero um dashboard executivo (funil, canais, ranking de unidades, mapa de calor por UF, alertas); como franqueado quero o meu (funil, origem, SLA, posição no ranking, avaliações do Google).
**Acceptance**
1. Given período e filtros, When troco o período, Then todos os cartões usam a mesma régua e mostram a fonte.
2. Given franqueado, When vejo o ranking, Then vejo minha posição e a mediana da rede, não os números nominais de outras unidades.
3. Given área do cliente ligada (spec 002), Then os dashboards da rede e da unidade ganham blocos de clientes, campanhas, NPS, vendas online e avisos pendentes.

### US6. Domínio próprio com canonical definido (P2)
Como franqueado quero ligar meu domínio; como Admin quero definir a estratégia de canonical por unidade.
**Acceptance**
1. Given domínio informado, When valido DNS, Then vejo passo a passo (CNAME/ALIAS), status do SSL e verificação.
2. Given estratégia "domínio redireciona", Then o domínio responde 301 para a ficha oficial.

### US7. SEO local e comparação com o GBP (P1)
Como SEO da rede quero ver, por unidade, title, canonical, schema, sitemap e a comparação do cadastro com o GBP (nota, avaliações, categoria, site, NAP), com alertas. O GBP é da unidade: o sistema lê e compara, nunca edita (decisão do Osmar).
**Acceptance**
1. Given GBP apontando para outro site, Then a unidade recebe alerta "GBP fora da URL canônica".
2. Given NAP do GBP diferente do cadastro, Then alerta com os dois valores lado a lado.
3. Given alerta de GBP, Then a unidade recebe a tarefa com o link do artigo da Wiki que ensina a corrigir no próprio GBP; o sistema não tem botão de editar o GBP.

### US8. Relatórios agendáveis (P2)
**Acceptance**: Given relatório salvo, When agendo semanal, Then os destinatários recebem PDF/CSV no horário, respeitando o escopo de cada um.

### US9. Suporte integrado (P2)
Como unidade quero abrir tickets para a Gio (categoria, prioridade, SLA, anexos); como cliente final quero abrir uma solicitação ligada à unidade; ambos com base de conhecimento.
**Acceptance**
1. Given ticket aberto, Then aparece na fila certa com SLA e responsável.
2. Given artigo relacionado, When digito o assunto, Then o sistema sugere artigos antes de abrir.
3. Given chamado aberto por cliente na área do cliente (spec 002), Then o ticket chega com `cliente_id` e canal.

### US10. Usuários, permissões, auditoria e LGPD (P1)
**Acceptance**
1. Given convite, When o usuário aceita, Then entra com perfil e escopo definidos (ver US12) e 2FA obrigatório para perfis de rede, regional e quem tem exportar ou dado pessoal.
2. Given exportação com PII, Then fica registrada na auditoria com usuário, data, filtro e quantidade.
3. Given pedido do titular, Then é possível localizar, exportar e anonimizar o lead.
4. Given a tela de login, Then não existe opção de criar conta: o acesso só nasce por convite (ver US20).

### US11. Rede altera qualquer unidade sem fila, às claras (P1)
Como Admin da rede (ou Marketing e SEO no seu módulo) quero alterar a ficha e a landing de qualquer unidade e publicar na hora, para corrigir erro, cumprir regra legal ou aplicar uma mudança da rede, sem depender do franqueado.
**Independent Test**: R-ADM troca o horário de sábado da GiO Alto da Lapa e publica; o franqueado recebe aviso e vê o diff na auditoria da unidade.
**Acceptance**
1. Given perfil de rede com E no módulo, When altero um campo de qualquer estado (T, E ou EA) e publico, Then publica sem passar pela fila e a tela marca "alterado pela rede".
2. Given publicação pela rede, Then o motivo é obrigatório e a auditoria grava usuário, perfil, campo, antes, depois, motivo, IP e horário.
3. Given publicação pela rede, Then U-FRQ e U-GER recebem aviso (sino e e-mail) com o diff e o botão "contestar" (abre chamado ligado à alteração).
4. Given a unidade tinha rascunho ou item na fila no mesmo campo, When a rede publica, Then o rascunho da unidade fica marcado "em conflito" e não é descartado em silêncio.
5. Given alteração em massa (ex.: FAQ base em 130 unidades), Then a rede vê uma prévia de quantas unidades mudam, publica em lote com um só motivo e cada unidade recebe um aviso.
6. Given alteração da rede, When alguém com permissão reverte pela versão, Then volta o valor anterior, com novo registro na auditoria.

### US12. Perfis por função com escopo rede, regional e unidade (P1)
Como Admin da rede quero perfis padrão por função (Marketing, SEO, Comercial/Atendimento, Call center, Financeiro/Leitura, Agência, Gestor regional, Franqueado, Gerente, Recepcionista) e criar perfis personalizados, para dar a cada pessoa só o que ela precisa.
**Acceptance**
1. Given um perfil, Then cada permissão é a combinação módulo x ação (ver, editar, aprovar, publicar, exportar, dado pessoal) e o perfil tem um nível (rede, regional, unidade).
2. Given perfil personalizado de nível unidade, When tento dar E em Dados estruturados, Marca ou Integrações, Then o sistema bloqueia (teto do nível).
3. Given perfil Agência, When tento ligar "dado pessoal", Then o sistema bloqueia, inclusive em perfil personalizado.
4. Given uma pessoa com duas atribuições (Gerente na unidade A, Leitura na B), Then em cada unidade vale só a atribuição daquela unidade.
5. Given mudança num perfil, Then todos que o usam são afetados, a auditoria grava o diff de permissões e a tela mostra quantas pessoas o usam antes de salvar.
6. Given R-ADM, When uso "ver como" outro perfil, Then vejo a interface daquele perfil em modo só leitura, com registro na auditoria.
7. Given U-FRQ, When convido alguém, Then só posso dar U-GER ou U-REC (ou personalizados de unidade liberados pela rede) e só nas minhas unidades.

### US13. Rede define os dados estruturados base e a política de campos (P1)
Como SEO da rede quero definir por marca o schema base (tipo, mapeamento NAP, categorias, sameAs, parentOrganization, FAQ base) e, como Admin, a política campo a campo (T, E, EA) por perfil de unidade, para que a unidade cuide do dia a dia sem quebrar SEO técnico nem marca.
**Acceptance**
1. Given schema base da marca, When a unidade muda um valor (ex.: horário), Then o JSON-LD da unidade é regerado com o valor novo e a estrutura da rede, e passa no validador de dados estruturados antes de publicar.
2. Given política de campos, Then cada campo da ficha e cada bloco da landing mostra seu estado por perfil, e campo sem regra nasce T.
3. Given mudança na política (ex.: telefone de EA para E), Then vale para todas as unidades da marca na hora, com registro na auditoria.
4. Given perfil de unidade, When abro a aba de SEO da minha unidade, Then vejo a prévia do schema e do title em modo leitura, sem editar.
5. Given schema inválido (ex.: unidade sem coordenadas), Then a landing não publica e a rede vê o alerta.

### US14. Wiki e central de ajuda para todos os perfis (P1)
Como qualquer usuário quero uma central de ajuda com artigos por perfil e por módulo, busca, vídeos e novidades, para aprender a usar o sistema sem abrir chamado.
**Acceptance**
1. Given meu perfil, When abro a Wiki, Then vejo primeiro a trilha do meu perfil (ex.: "Primeiros passos do franqueado", "Guia do call center") e os módulos que tenho habilitados.
2. Given busca por termo, Then aparecem artigos, vídeos e perguntas, com destaque do trecho.
3. Given trilha "Seu Google Meu Negócio", Then a unidade vê checklist (NAP igual ao cadastro, categoria recomendada, horários e feriados, fotos, respostas a avaliações, posts, link para a landing oficial com UTM) e marca o que já fez.
4. Given qualquer tela do sistema, When clico em ajuda, Then abre o artigo daquela tela.
5. Given novidade publicada pela rede, Then aparece em "Novidades" e no sino de quem é afetado.
6. Given artigo, Then mostra "foi útil?" e a rede vê os artigos mais buscados sem resultado.

### US15. Relatórios inteligentes automáticos (P2)
Como rede e como unidade quero receber insights gerados dos dados (quedas, picos, anomalias, oportunidades) com alertas e envio agendado por e-mail.
**Acceptance**
1. Given queda de leads acima do limite numa unidade, When a rotina diária roda, Then gera um insight com número, comparação, causa provável (canal, campanha, horário) e ação sugerida.
2. Given insight, Then mostra a fonte, o período e a regra que o gerou (nada de "caixa preta").
3. Given assinatura de resumo semanal, Then cada destinatário recebe só os insights do seu escopo, sem dado pessoal no e-mail.
4. Given insight descartado ou resolvido, Then sai da lista e alimenta a melhoria da regra.

### US16. Módulos e recursos por rede, regional e unidade (P1)
Como Admin da rede quero ligar e desligar módulos e recursos (ex.: Variantes de landing, Promoções, Relatórios inteligentes, Domínio próprio, App do celular) por rede, regional ou unidade, para fazer piloto e liberar aos poucos.
**Acceptance**
1. Given recurso desligado na rede, Then some do menu e das permissões de todos.
2. Given recurso ligado na rede e desligado numa regional, Then fica desligado nas unidades daquela regional, salvo exceção por unidade.
3. Given mudança de módulo, Then a auditoria registra e as unidades afetadas recebem aviso.
4. Given tela de módulos, Then vejo para cada recurso onde está ligado (contagem de unidades) e a origem da regra (herdada ou exceção).
5. Given specs 002 e 003, Then existem os módulos "Área do cliente" (submódulos "Pagamento online", "Campanhas de unidade", "Chat com cliente", "Mural de avisos"), "Quiz", "Inteligência" e "Tracking e tags"; as funções comerciais de unidade seguem a matriz de liberação da 002 (Controles da rede), padrão bloqueado.

### US17. Modelos de ficha e menu da ficha (P1)
Como Marketing da rede quero listar, selecionar, editar, duplicar e definir o modelo principal de ficha (blocos, campos visíveis e menu com itens, ordem e âncoras), para padronizar as 130 fichas e testar novos formatos.
**Acceptance**
1. Given lista de modelos, Then vejo nome, unidades que usam, status (rascunho, ativo, principal) e última edição.
2. Given "duplicar", Then nasce um rascunho idêntico que posso editar sem afetar quem usa o original.
3. Given "definir como principal", Then unidades sem modelo próprio passam a usar o novo após confirmação, com prévia de impacto e aviso.
4. Given editor do menu, When reordeno itens ou troco âncoras, Then a prévia atualiza e o sistema avisa âncora sem bloco correspondente.

### US18. Landing pages e variantes por unidade (P1)
Como Marketing e como unidade quero, além da landing principal, variantes de A/B, de campanha e por serviço, listadas na ficha da unidade (seção "Landing pages") com status, URL e desempenho.
**Acceptance**
1. Given a ficha da unidade, Then a seção "Landing pages" lista a principal e as variantes com tipo, status (rascunho, em teste, no ar, encerrada), URL, período, leads, taxa de envio e vencedora.
2. Given variante de campanha, Then publica com noindex e canonical para a principal (princípio VI).
3. Given teste A/B, Then a divisão de tráfego é na mesma URL, com amostra mínima e significância antes de declarar vencedora.
4. Given variante por serviço (ex.: depilação a laser na unidade), Then é indexável, com conteúdo próprio e link no menu da ficha.
5. Given variante criada pela unidade, Then vai para aprovação de Marketing (política, item 82).

### US19. Privacidade com a rede como controladora (P1)
Como rede controladora quero centralizar consentimento, base legal, retenção, mascaramento, exportação e pedidos do titular, com as unidades acessando o mínimo para atender.
**Acceptance**
1. Given lead novo, Then o consentimento fica registrado com versão, data, IP e base legal por finalidade (atendimento, marketing).
2. Given perfil de unidade, Then o telefone e o e-mail aparecem mascarados e as ações de contato usam botões, com registro do acesso.
3. Given pedido do titular recebido por qualquer canal, Then entra na fila LGPD da rede com prazo de 15 dias e a unidade só pode encaminhar.
4. Given fim do prazo de retenção, Then a rotina anonimiza o lead e mantém só o agregado.
5. Given pedido de exportação com PII por uma unidade, Then exige liberação da rede, 2FA e motivo.
6. Given pedido feito pelo cliente na central de privacidade (spec 002), Then entra na mesma fila com origem "área do cliente" e `cliente_id`.

### US20. Provisionamento da unidade e contas por convite (P1)
Decisão do Osmar (21/11/2026): como é uma rede, não existe cadastro manual de conta interna. A rede provisiona a unidade e entrega uma conta de admin da unidade pronta; o admin da unidade monta a própria equipe.
**Acceptance**
1. Given a rede cria uma unidade (dados base, modelo de ficha, módulos, regional), When conclui o provisionamento, Then o sistema cria a conta U-FRQ (admin da unidade) e envia convite por e-mail com link de uso único válido por 72 h.
2. Given o primeiro acesso pelo convite, Then a pessoa define a senha (mínimo 12 caracteres, sem reaproveitar as 5 últimas), ativa o 2FA e só então entra no portal.
3. Given o admin da unidade logado, When convida alguém, Then só pode escolher perfis de unidade liberados pela rede (padrão: U-GER e U-REC); não cria perfis nem dá acesso a outra unidade.
4. Given convite vencido, Then só a rede reenvia (para U-FRQ) ou o admin da unidade reenvia (para a própria equipe); tudo fica na auditoria.
5. Given "esqueci a senha", Then a resposta é a mesma exista ou não a conta, o link vale 30 min e todas as sessões abertas são encerradas após a troca.
Telas: 01, 03, 16, 32.

### US21. Auditoria geral do sistema, visível só para a rede (P1)
Pedido do Osmar (21/11/2026, 09h52): um log de auditoria geral que registra tudo o que todos alteram (rede, regionais, unidades e perfis), visível apenas para perfis da rede.
**Acceptance**
1. Given qualquer escrita no sistema (ficha, landing, schema, domínio, permissões, perfis, módulos, controles, tags, campanhas, promoções, avisos, configurações) ou acesso a dado pessoal, Then nasce um registro com quem fez, perfil, escopo, unidade, módulo, tipo de ação, antes e depois, motivo, IP e aparelho.
2. Given ação que passa por aprovação, Then o registro guarda quem pediu, quem aprovou ou rejeitou, o motivo da decisão e o status (pendente, aprovado, rejeitado, direto, direto da rede).
3. Given perfil da rede com acesso à auditoria, When filtro por período, pessoa, perfil, unidade, módulo, tipo de ação e status de aprovação, Then a lista e o total respeitam os filtros, e ao abrir um registro vejo o diff antes e depois.
4. Given exportação, Then sai um CSV com os registros filtrados, e a própria exportação vira um registro.
5. Given qualquer perfil, inclusive R-ADM, Then não existe editar nem apagar registro: a tabela é só de inclusão, com cadeia de resumos verificável; a retenção segue a política definida (D14).
6. Given perfil de regional ou de unidade, Then a tela de auditoria geral não aparece; a unidade continua recebendo o aviso de cada alteração da rede na própria ficha (princípio XII) pelas notificações.
7. Given envio de campanha, configuração de tag, mudança de permissão ou leitura de dado pessoal (LGPD), Then o registro tem tipo próprio e filtro rápido.
Telas: 17 (e o protótipo, com filtros por tipo, detalhe com diff e exportação CSV funcionando).

## Requisitos funcionais (resumo)
- FR-001 Importar unidades, fotos, tratamentos e agendamentos do AGDM, com deduplicação (há slug duplicado e cerca de 250 registros para 130 ativas).
- FR-002 Completude da ficha calculada (0 a 100) com pesos públicos.
- FR-003 Coordenadas obrigatórias para publicar, com geocodificação a partir do CEP.
- FR-004 3 templates, blocos travados/livres, validador de regras da marca, preview, aprovação, versões.
- FR-005 Domínio próprio com verificação, SSL e estratégia de canonical.
- FR-006 Lead com unidade, origem (UTM, gclid, fbclid, referrer), páginas vistas, consentimento.
- FR-007 Status do lead sincronizado com DocBiz; envio ao CRM; aviso por WhatsApp/e-mail.
- FR-008 SLA configurável por marca e unidade; distribuição call center x unidade por regra.
- FR-009 Eventos padronizados conforme o dicionário versionado da spec 003 (FR-217 a FR-219), no padrão `objeto_acao` em português: `unidade_visualizada` (antes view_unidade), `lead_iniciado`, `agendamento_concluido`, `whatsapp_clicado` (antes clique_whatsapp), `telefone_clicado` (antes clique_telefone), `rota_clicada` (antes clique_rota), `atendimento_compareceu` (antes "compareceu offline").
- FR-010 Dashboards rede e unidade; relatórios salvos, agendados e exportáveis.
- FR-011 Tickets unidade para Gio e cliente para unidade; base de conhecimento.
- FR-012 Perfis RBAC (perfil x escopo x módulo x ação); auditoria de escrita e de acesso a PII; consentimento com versão. Detalhe em FR-015 a FR-020.
- FR-013 SEO: title, description, canonical, schema da marca (LocalBusiness/MedicalBusiness ou subtipo, decisão em aberto), sitemap, hubs por UF e cidade, alertas. Estrutura só pela rede (FR-021).
- FR-014 GBP: place_id, nota, avaliações, categoria, site do GBP, divergências de NAP.

- FR-015 Override da rede: perfis de rede com E publicam em qualquer unidade do escopo sem fila; motivo obrigatório; marca "alterado pela rede" no campo.
- FR-016 Aviso ao franqueado e ao gerente em cada alteração da rede (sino e e-mail, resumo diário opcional), com diff e "contestar" ligado a um chamado.
- FR-017 Versionamento de ficha e landing por campo e bloco, com reverter; conflito entre rascunho da unidade e alteração da rede é sinalizado, nunca descartado.
- FR-018 Alteração em massa pela rede com prévia de impacto, lote, motivo único e aviso por unidade.
- FR-019 RBAC: perfis padrão (rbac.md), perfis personalizados criados só pela rede, teto por nível, várias atribuições por pessoa, "ver como" em modo leitura.
- FR-020 Ação "dado pessoal" separada de "ver"; exportar com PII exige 2FA, motivo e link que expira; bloqueio de PII para Agência no banco (RLS), não só na tela.
- FR-021 Schema base por marca: tipo, mapeamento NAP, categorias, sameAs, parentOrganization, FAQ base; JSON-LD gerado por unidade e validado antes de publicar.
- FR-022 Política de campos editável pela rede: estado T, E, EA, L ou O por campo, bloco e perfil; campo novo nasce T; tabela inicial em politica-campos.md.
- FR-023 Validador automático da marca em toda edição, inclusive E; pós-moderação: a rede despublica um item E com motivo e aviso.
- FR-024 Promoções por modelo da rede (tratamento, condição, validade obrigatória), saindo do ar sozinhas no fim da validade. Ampliação pela spec 002: modelos com tipos, preço opcional conforme a política de preço (D1 da 002), adesão às promoções da rede e regulamento; se a liberação "promocoes" estiver bloqueada, os campos de promoção viram T para a unidade.
- FR-025 Fim de scripts por unidade: nenhum perfil de unidade injeta script, meta ou JSON-LD; pixels extras só por pedido à rede. Tags da unidade só por campos tipados do gerenciador de tags (spec 003, FR-231 a FR-235).
- FR-026 Rota "pedir alteração" em campo T, abrindo chamado com o campo, o valor atual e o valor pedido.

- FR-027 Wiki: artigos com perfil-alvo, módulo, vídeo, tags; busca; trilhas por perfil; trilha "Seu Google Meu Negócio" com checklist marcável; novidades; ajuda contextual por tela; métrica "foi útil". Nova trilha "Medição e tags" com artigos por perfil e vídeo explicativo por artigo (spec 003, US23 e FR-238), incluindo o guia de configuração do gerenciador de tags em arquivo e em vídeo (pedido do Osmar, 21/11/2026); entregável da fase de lançamento da Wiki, antes de abrir o gerenciador às unidades. Artigos ganham `versao_interface` e marcação automática "revisar".
- FR-028 Relatórios inteligentes: regras de detecção (queda, pico, SLA, completude, divergência GBP, campanha), insight com fonte e regra, assinatura por e-mail (diário, semanal), sem PII no e-mail. Tipos novos (spec 002 e 003): `campanha_destaque`, `cota_estourada`, `nps_baixo`, `no_show_alto`, `aviso_pendente`, `sazonal_clima`, `demanda_quiz`, `penetracao_baixa`, `concorrencia`, `tracking_quebrado`, `utm_invalida`.
- FR-029 Módulos e recursos com herança rede > regional > unidade, exceções e auditoria.
- FR-030 Modelos de ficha: CRUD, duplicar, versão, principal da rede, campos visíveis, blocos, menu (itens, ordem, âncoras) com validação de âncora.
- FR-031 Variantes de landing: tipos A/B, campanha, serviço; status; regras de canonical e indexação por tipo; divisão de tráfego; métricas por variante; seção "Landing pages" na ficha da unidade.
- FR-032 GBP: vínculo do place_id pela unidade, leitura periódica e comparação de NAP, categoria, site, horário e nota; alerta com link para a Wiki; nenhuma escrita no GBP.
- FR-033 LGPD centralizada: base legal por finalidade, política de retenção por marca com anonimização automática, fila única de pedidos do titular na rede (prazo 15 dias), mascaramento padrão para perfis de unidade, exportação com PII liberada pela rede.
- FR-034 Sem autocadastro: login sem "criar conta"; contas internas nascem por convite (rede para perfis de rede, regional e U-FRQ; admin da unidade para U-GER e U-REC dentro dos perfis liberados).
- FR-035 Provisionamento da unidade: assistente da rede (dados base, modelo de ficha, módulos, regional, domínio) que termina com a criação da conta U-FRQ e o convite; primeiro acesso obriga troca de senha e ativação de 2FA.
- FR-036 Auditoria geral só de inclusão (append-only): registro de toda escrita e de todo acesso a dado pessoal, com antes e depois, motivo, solicitante, aprovador ou quem rejeitou, status de aprovação, IP e aparelho; filtros por período, pessoa, perfil, unidade, módulo, tipo e status; detalhe com diff; exportação CSV registrada; retenção por política (D14); sem UPDATE nem DELETE no banco (permissão revogada e gatilho de bloqueio) e cadeia de hashes para verificar integridade; visível só para perfis da rede com permissão.

## Integração com as specs 002 e 003 (rev. 3.2)
Aplicado a partir de `specs/002-area-cliente/impacto-na-001.md` e `specs/003-quiz-inteligencia-tracking/impacto-na-001-002.md`.
- Requisitos referenciados: FR-101 a FR-160 (área do cliente, controles da rede, campanhas, mural, vendas) e FR-201 a FR-238 (quiz, inteligência, tracking e tags).
- Princípios novos da constituição 1.4.0: XIV (API única), XV (dado de saúde fora), XVI (a rede libera, a unidade opera dentro do limite) e XVII (medição é contrato).
- Regras aprovadas pelo Osmar em 21/11/2026 (`specs/002-area-cliente/respostas-osmar-2026-11-21.md`): 2 campanhas por mês por unidade; no máximo 1 mensagem por semana por cliente, somando rede e unidades; alcance padrão só na base da própria unidade; aprovação da rede; conta de cliente só para maiores de 18; ficha de saúde fora da fase 1. Pendentes com a Salus: participação da rede nas vendas (recebimento direto pelo franqueado, split só se necessário), política de preço e as 7 perguntas sobre a DocBiz.
- Gerenciador de tags da unidade (pedido do Osmar): um único carregador da rede envia cada evento uma vez e distribui para o GA4 da marca e, se liberado, para o GA4 próprio da unidade, sem duplicar scripts; a unidade só preenche campos tipados (ID de medição, meta tag do Search Console, Ads, Meta, TikTok) que passam por aprovação.
- Telas: rodada 3 desenha as principais telas da 002 e da 003 (ver `telas.md`).

## Success Criteria
- SC-001 130 de 130 unidades com canonical próprio e schema local no lançamento (hoje 0).
- SC-002 Todas as unidades com coordenadas (hoje faltam 13) e pelo menos 6 fotos (hoje 70 sem foto).
- SC-003 100% das conversões de Ads e GA4 vindas de evento confirmado no servidor.
- SC-004 Mediana de primeiro contato dentro do SLA definido pela Gio.
- SC-005 Franqueado publica uma alteração simples sem ajuda em menos de 5 minutos.
- SC-006 Landing pública com Lighthouse mobile de pelo menos 90.

- SC-007 100% das alterações da rede em unidades com motivo, diff na auditoria e aviso entregue ao franqueado.
- SC-008 Zero JSON-LD inválido em produção (validação diária das 130 unidades).
- SC-010 100% das contas internas criadas por convite registrado na auditoria; zero contas criadas por autocadastro.
- SC-011 100% das escritas e dos acessos a dado pessoal com registro na auditoria geral; zero registros alterados ou apagados (verificação diária da cadeia de hashes).
- SC-009 Pelo menos 80% das edições da unidade publicam sem fila (campos E), com fila de aprovação respondida em até 1 dia útil.

## Riscos e lacunas
1. **Contrato de franquia.** O override da rede e a política de campos precisam caber no contrato e na COF. Se o contrato dá ao franqueado o controle do marketing local, a alteração sem consentimento pode gerar conflito. Validar com o jurídico da Salus.
2. **Confiança do franqueado.** Override frequente vira atrito. Mitigação:
   - motivo obrigatório, aviso com diff e contestação;
   - relatório mensal de alterações da rede por unidade;
   - meta de pouco override fora de lote.
3. **Explosão de perfis.** Perfis personalizados demais ficam impossíveis de auditar. Mitigação: teto por nível, contagem de uso, revisão trimestral e só R-ADM cria.
4. **GBP da unidade (resolvido em 21/11/2026).** A unidade é dona do GBP. Risco remanescente: a rede não garante NAP, categoria e site. Mitigação: comparação diária, alerta com link para a Wiki e indicador de divergência no ranking. Hoje só 3 de 10 GBPs da amostra apontam para a ficha.
5. **LGPD (resolvido em 21/11/2026).** A rede é controladora e as unidades operadoras. Risco remanescente: o contrato de franquia precisa de cláusula de operador (instruções, sigilo, incidente) e as unidades precisam aceitar o termo no primeiro acesso.
6. **Publicidade em saúde e estética.**
   - Antes e depois, promessa de resultado e registro profissional têm regras de conselho de classe e do CDC.
   - A política deixa antes e depois como EA com termo de uso de imagem, mas falta a regra fechada por tratamento.
7. **Promoções x regra "sem valores".** A regra atual da Gio proíbe valores, e Osmar quer promoções editáveis "dentro das regras". Sem um modelo claro (percentual? brinde? sessão de avaliação?), a promoção vira brecha para preço.
8. **Schema de saúde.**
   - MedicalBusiness pressupõe atendimento de saúde; para unidade só de estética, um subtipo como BeautySalon ou HealthAndBeautyBusiness pode ser mais correto.
   - Escolher errado não gera punição direta, mas confunde a categoria.
   - AggregateRating de avaliações próprias não gera estrelas no Google e fica desligado.
9. **Conflitos de edição.** Rede e unidade no mesmo campo ao mesmo tempo. Coberto por versão e "em conflito", mas a fusão de texto fica manual.
10. **Volume de auditoria.** Leitura de PII e edições em massa geram muito registro. Definir retenção (ex.: 5 anos para escrita, 2 anos para leitura) e arquivamento frio.
11. **Fim do GTM por unidade.** As 17 unidades com GTM próprio perdem tags de terceiros. É preciso um inventário e uma migração antes do corte, ou a unidade perde mensuração que usa hoje.
12. **Sorridents.** A política de campos e o schema são por marca. O perfil dentista tem CRO e regras do CFO diferentes, então não dá para copiar a tabela da Gio.

## Decisões em aberto (para o Osmar e a Gio)
| # | Decisão | Opções | Recomendação ou resolução | Status |
|---|---|---|---|---|
| D1 | Quem na rede faz override | Só R-ADM / R-ADM + R-MKT + R-SEO no seu módulo | R-ADM + R-MKT + R-SEO, cada um no seu módulo | Aberta; recomendação usada nas telas da rodada 2 |
| D2 | Gestor regional aprova itens EA da sua região? | Não / Sim para conteúdo | Sim para conteúdo, não para SEO | Aberta; recomendação usada nas telas da rodada 2 |
| D3 | Gestor regional vê dado pessoal de leads? | Não / Sim | Não; só agregados | Aplicada na rodada 2 de telas; coerente com a rede controladora (LGPD resolvida) |
| D4 | Recepcionista exporta leads ou vê telefone completo? | Vê e atua sem exportar / Só primeiro nome | Vê e atua pelos botões, sem exportar | Aplicada na rodada 2 de telas; coerente com a rede controladora (LGPD resolvida) |
| D5 | Franqueado cria perfis personalizados da unidade? | Não / Sim, dentro de um teto | Não na fase 1 | Aberta; recomendação usada nas telas da rodada 2 |
| D6 | Aviso ao franqueado | A cada alteração / Resumo diário / Ambos configurável | A cada alteração fora de lote; lote em resumo | Aberta; recomendação usada nas telas da rodada 2 |
| D7 | Franqueado pode contestar e bloquear? | Só contestar / Contestar suspende a mudança | Só contestar (decisão fica com a rede) | Aberta; recomendação usada nas telas da rodada 2 |
| D8 | Tipo de schema | LocalBusiness / MedicalBusiness / BeautySalon / HealthAndBeautyBusiness, por tipo de unidade | Decidir com o jurídico e o SEO da rede; testar no Search Console | Aberta; recomendação usada nas telas da rodada 2 |
| D9 | Modelo de promoção | Sem preço (brinde, condição) / Percentual / Livre com aprovação | Sem preço por modelo (E); qualquer outra coisa EA | Passa a ser tratada junto com D1 (preço) da spec 002: recomendação mantida pelo Osmar (sem preço público; preço só logado e em promoções), pendente de confirmação do grupo Salus |
| D10 | Dono do GBP | Rede / Unidade | A unidade é dona e edita o próprio GBP; o sistema só compara e alerta; a Wiki orienta | Resolvida pelo Osmar (21/11/2026) |
| D11 | Unidade inativa | 410 / 301 para a mais próxima / Página "unidade fechada" com as próximas | Página com as unidades próximas por 90 dias e depois 301 | Aberta; recomendação usada nas telas da rodada 2 |
| D12 | Horário de agenda | Digitado na plataforma / Lido da DocBiz | Ler da DocBiz se a API permitir | Aberta; recomendação usada nas telas da rodada 2 |
| D13 | FAQ local no schema FAQPage | Sim / Não | Sim, só para FAQ aprovado ou base (o Google hoje mostra FAQ rico só para sites de governo e saúde de autoridade, então o ganho é semântico) | Aberta; recomendação usada nas telas da rodada 2 |
| D14 | Retenção da auditoria | 2, 5 ou 10 anos | 5 anos escrita, 2 anos leitura de PII | Aberta; recomendação usada nas telas da rodada 2 |
| D16 | Criação de contas internas | Autocadastro / Convite | Só convite: rede provisiona a unidade e entrega o admin da unidade, que convida a equipe nos perfis liberados | Resolvida pelo Osmar (21/11/2026) |
| D15 | Controlador LGPD | Rede / Conjunto / Unidade | Rede controladora, unidades operadoras com acesso mínimo; pedidos do titular centralizados na rede | Resolvida pelo Osmar (21/11/2026) |

## Fora de escopo agora
- Redesenho do site institucional e da listagem pública de unidades (fica para depois, já citado pelo Osmar).
- Agenda clínica, prontuário e financeiro (DocBiz). A venda online, pacotes e o split ficam na spec 002.
