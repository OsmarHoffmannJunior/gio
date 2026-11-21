# Constituição: Plataforma de Unidades Salus (marca Gio primeiro)

Versão 1.4.0, 21/11/2026. Vale para spec, plano, telas e código.

Histórico: 1.0.0 (21/11/2026) versão inicial. 1.1.0 (21/11/2026) decisões do Osmar: rede edita qualquer unidade sem aprovação (XII), RBAC por função e escopo (VIII), rede dona dos dados estruturados e política de campos (V e XI). 1.2.0 (21/11/2026) GBP da unidade (II), rede controladora LGPD (VII), configuração por escopo e ajuda (XIII). 1.3.0 (21/11/2026) contas internas só por convite (VIII). 1.4.0 (21/11/2026) integração das specs 002 (área do cliente) e 003 (quiz, inteligência e tracking): novos princípios XIV a XVII e ajustes em I, III, IV, V, VII, IX, X e XI. A proposta "1.3.0" escrita nas notas de impacto da 002 e da 003 entrou como 1.4.0, porque a 1.3.0 já tinha sido usada pela regra de convite. Cópias anteriores em `historico/`.

## Princípios

### I. Multi-marca e multi-tenant desde o primeiro dia
Um código, um deploy, um banco com `marca` e `unidade` em toda tabela de negócio. A Gio é a marca 1; a Sorridents entra como marca 2 sem fork. Tema (cores, logo, fontes, textos legais) é dado da marca, nunca código. Cada marca tem a própria conta de cliente (conta de cliente por marca).

### II. A unidade é a fonte da verdade do NAP
Nome, endereço, telefone, WhatsApp, horários e coordenadas são cadastrados uma vez e alimentam landing, schema, sitemap, listagem pública e checklist do Google Meu Negócio. Coordenadas e horário estruturado são obrigatórios para publicar. O perfil do Google (GBP) é da unidade: a rede não é dona nem edita o GBP. O sistema só lê, compara NAP e dados com o cadastro e alerta; a Wiki orienta a unidade a corrigir.

### III. Toda conversão é confirmada no servidor
Evento de lead e de agendamento só existe depois que o servidor aceitou. Nada de conversão no clique. Todo evento carrega `marca`, `unidade_id`, `template` e origem, e nunca carrega dado pessoal. Vale também para cadastro de cliente confirmado, agendamento confirmado pela DocBiz e pedido pago confirmado pelo webhook do gateway. Conversões são enviadas aos destinos de anúncio pelo servidor, com o mesmo `event_id` do navegador para deduplicar.

### IV. Não competir com DocBiz nem com o CRM
A plataforma capta, qualifica, roteia e mede. Agenda, prontuário e gestão da clínica ficam na DocBiz; CRM fica onde a Salus decidir (Salesforce visto na API). Integração por API/webhook, com fila e reprocessamento; sem integração disponível, exportação e importação. Pacotes e sessões têm a DocBiz como fonte do consumo: a plataforma exibe e vende, mas não substitui agenda nem prontuário.

### V. Autonomia do franqueado dentro da política de campos
A unidade cuida sozinha do dia a dia: fotos, horários, textos de blocos, equipe, FAQ local e promoções dentro das regras. Cada campo da ficha e cada bloco da landing tem um estado definido pela rede por perfil: **travado**, **editável** ou **editável com aprovação** (tabela em `specs/001-sistema-unidades/politica-campos.md`). O que não está na tabela nasce travado. Regras de texto da Gio: sem valores, sem protocolo da rede, sem marca de equipamento, "avaliação gratuita" nos CTAs; o validador automático roda em toda edição, inclusive nas editáveis sem aprovação. A regra "sem valores" passa a seguir a política de preço da rede por procedimento (D1 da 002); enquanto o grupo não confirmar, vale "sem preço no conteúdo público", com preço só para cliente logado e em promoções.

### VI. Uma URL canônica por unidade
Domínio próprio é opção, nunca duplicação. A franqueadora decide por unidade: ficha oficial canônica (padrão), domínio canônico, ou domínio que redireciona. O GBP aponta para a canônica.

### VII. Privacidade por padrão, com a rede como controladora (LGPD)
A rede (franqueadora) é a controladora dos dados pessoais dos leads; as unidades atuam como operadoras, com acesso mínimo para atender. Consequências obrigatórias: consentimento desmarcado e registrado com versão do texto, data e IP; base legal registrada por finalidade; retenção definida pela rede e aplicada por rotina; dado pessoal mascarado por padrão; exportação com dado pessoal controlada pela rede (2FA, motivo, link que expira); solicitações do titular centralizadas na rede. Sem PII em URL, cookie de marketing ou dataLayer. Todo acesso a dado pessoal fica na auditoria. Agência nunca vê PII. Vale também para clientes da área do cliente: consentimento por canal de marketing, e a unidade só vê clientes com vínculo com ela. Respostas de quiz só entram em segmentação com consentimento de personalização; perguntas de saúde ficam bloqueadas até o princípio XV mudar.

### VIII. Acesso por função e pelo menor escopo (RBAC)
Permissão = perfil (função) x escopo (rede, regional ou unidade) x módulo x ação (ver, editar, aprovar, publicar, exportar, dado pessoal). A rede mantém perfis padrão e pode criar perfis personalizados, sempre abaixo de um teto por escopo: nenhum perfil de unidade alcança schema, SEO técnico, marca ou dados de outra unidade. "Dado pessoal" é uma ação separada de "ver"; exportar dado pessoal exige as duas e 2FA. Toda escrita e todo acesso a dado pessoal geram log. Quem envia uma mudança não aprova a própria mudança. Não existe cadastro aberto de conta interna: a rede provisiona a unidade e entrega a conta de admin da unidade pronta, por convite de uso único; no primeiro acesso a pessoa troca a senha e ativa o 2FA, e depois convida a própria equipe somente nos perfis de unidade que a rede liberou. Contas da rede e de parceiros também nascem só por convite da rede.

### IX. Desenho corporativo, rápido e legível
Interface densa mas calma: tabelas com filtros salvos, números grandes só onde decidem algo, ações em no máximo 2 cliques. Landing pública com nota Lighthouse mobile igual ou acima de 90 (o site atual já tira 93 a 96). O orçamento de performance vale com as tags ligadas.

### X. Números saem de dados, não de impressão
Dashboards mostram fonte e período. Comparações entre unidades usam a mesma régua (mesmos eventos, mesmo período). Toda recomendação automática mostra fonte, regra e amostra.

### XI. A rede é dona dos dados estruturados e do SEO técnico
Schema (LocalBusiness/MedicalBusiness ou subtipo), mapeamento NAP, categorias, sameAs, FAQ base, title, description, canonical, robots, sitemap, hreflang e scripts são definidos pela rede (perfil SEO) e gerados pelo sistema. A unidade alimenta valores (horário, fotos, equipe), nunca a estrutura. Nenhum perfil de unidade injeta script, meta tag ou JSON-LD. Tags, destinos e verificação do Search Console são estrutura da rede; a unidade só preenche campos tipados liberados.

### XII. A rede pode corrigir qualquer unidade, sempre às claras
Perfis da rede com permissão de edição alteram ficha e landing de qualquer unidade sem passar pela fila de aprovação. Toda alteração assim exige motivo, grava antes e depois na auditoria, avisa o franqueado (e-mail e sino) com o diff e pode ser revertida por versão. O franqueado pode contestar por chamado; ele não desfaz sozinho uma alteração da rede em campo travado.

### XIII. Configuração por escopo e ajuda em todo lugar
Módulos, recursos, modelos de ficha, menus, variantes de landing e relatórios automáticos são configuração, não código: a rede liga e ajusta por rede, regional e unidade, com herança e sem deploy. Toda tela tem ajuda contextual que leva à Wiki, com artigos por perfil.

### XIV. API única para site, painéis e app
Toda regra de negócio vive na API versionada; site, painéis e app futuro são clientes dela. A autenticação de clientes (OIDC com PKCE) é separada da autenticação de usuários internos. Clientes se cadastram sozinhos na área do cliente; a regra de convite do princípio VIII vale só para contas internas.

### XV. Dado de saúde fora da plataforma até decisão expressa
Anamnese, contraindicações, prontuário e fotos clínicas ficam na DocBiz. Trazer esses dados para a plataforma exige RIPD, consentimento específico e emenda desta constituição. Conta de cliente só para maiores de 18 anos.

### XVI. A rede libera, a unidade opera dentro do limite
Funções comerciais da unidade (preço, procedimentos locais, promoções, campanhas, canais, avisos regionais, quiz e tags) nascem bloqueadas; a rede libera por escopo e define cotas, frequência e alcance máximo. Nenhuma unidade alcança a base nacional (teto aplicado no banco). Padrão aprovado em 21/11/2026: 2 campanhas por mês por unidade, no máximo 1 mensagem por semana por cliente somando rede e unidades, alcance só na base da própria unidade e aprovação da rede.

### XVII. Medição é contrato
Todo evento existe primeiro no dicionário versionado, com dono, schema e mapeamento de destinos; nenhum evento, tag ou destino vai para produção sem QA e aprovação. Um único carregador e um único banner de consentimento por marca; nenhum script livre de unidade. Eventos seguem o padrão `objeto_acao` em português.

## Governança
Emendas mudam a versão (MAJOR remove princípio, MINOR adiciona, PATCH esclarece). Toda spec cita os princípios afetados; toda revisão de tela confere II, III, V, VII, VIII, XI, XII, XIII, XVI e XVII.
