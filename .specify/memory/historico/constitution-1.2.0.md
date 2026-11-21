# Constituição: Plataforma de Unidades Salus (marca Gio primeiro)

Versão 1.2.0, 21/11/2026. Vale para spec, plano, telas e código.

Histórico: 1.0.0 (21/11/2026) versão inicial. 1.1.0 (21/11/2026) decisões do Osmar: rede edita qualquer unidade sem aprovação (XII), RBAC por função e escopo (VIII), rede dona dos dados estruturados e política de campos (V e XI).

## Princípios

### I. Multi-marca e multi-tenant desde o primeiro dia
Um código, um deploy, um banco com `marca` e `unidade` em toda tabela de negócio. A Gio é a marca 1; a Sorridents entra como marca 2 sem fork. Tema (cores, logo, fontes, textos legais) é dado da marca, nunca código.

### II. A unidade é a fonte da verdade do NAP
Nome, endereço, telefone, WhatsApp, horários e coordenadas são cadastrados uma vez e alimentam landing, schema, sitemap, listagem pública e checklist do Google Meu Negócio. Coordenadas e horário estruturado são obrigatórios para publicar. O perfil do Google (GBP) é da unidade: a rede não é dona nem edita o GBP. O sistema só lê, compara NAP e dados com o cadastro e alerta; a Wiki orienta a unidade a corrigir.

### III. Toda conversão é confirmada no servidor
Evento de lead e de agendamento só existe depois que o servidor aceitou. Nada de conversão no clique. Todo evento carrega `marca`, `unidade_id`, `template` e origem, e nunca carrega dado pessoal.

### IV. Não competir com DocBiz nem com o CRM
A plataforma capta, qualifica, roteia e mede. Agenda, prontuário e gestão da clínica ficam na DocBiz; CRM fica onde a Salus decidir (Salesforce visto na API). Integração por API/webhook, com fila e reprocessamento; sem integração disponível, exportação e importação.

### V. Autonomia do franqueado dentro da política de campos
A unidade cuida sozinha do dia a dia: fotos, horários, textos de blocos, equipe, FAQ local e promoções dentro das regras. Cada campo da ficha e cada bloco da landing tem um estado definido pela rede por perfil: **travado**, **editável** ou **editável com aprovação** (tabela em `specs/001-sistema-unidades/politica-campos.md`). O que não está na tabela nasce travado. Regras de texto da Gio: sem valores, sem protocolo da rede, sem marca de equipamento, "avaliação gratuita" nos CTAs; o validador automático roda em toda edição, inclusive nas editáveis sem aprovação.

### VI. Uma URL canônica por unidade
Domínio próprio é opção, nunca duplicação. A franqueadora decide por unidade: ficha oficial canônica (padrão), domínio canônico, ou domínio que redireciona. O GBP aponta para a canônica.

### VII. Privacidade por padrão, com a rede como controladora (LGPD)
A rede (franqueadora) é a controladora dos dados pessoais dos leads; as unidades atuam como operadoras, com acesso mínimo para atender. Consequências obrigatórias: consentimento desmarcado e registrado com versão do texto, data e IP; base legal registrada por finalidade; retenção definida pela rede e aplicada por rotina; dado pessoal mascarado por padrão; exportação com dado pessoal controlada pela rede (2FA, motivo, link que expira); solicitações do titular centralizadas na rede. Sem PII em URL, cookie de marketing ou dataLayer. Todo acesso a dado pessoal fica na auditoria. Agência nunca vê PII.

### VIII. Acesso por função e pelo menor escopo (RBAC)
Permissão = perfil (função) x escopo (rede, regional ou unidade) x módulo x ação (ver, editar, aprovar, publicar, exportar, dado pessoal). A rede mantém perfis padrão e pode criar perfis personalizados, sempre abaixo de um teto por escopo: nenhum perfil de unidade alcança schema, SEO técnico, marca ou dados de outra unidade. "Dado pessoal" é uma ação separada de "ver"; exportar dado pessoal exige as duas e 2FA. Toda escrita e todo acesso a dado pessoal geram log. Quem envia uma mudança não aprova a própria mudança.

### IX. Desenho corporativo, rápido e legível
Interface densa mas calma: tabelas com filtros salvos, números grandes só onde decidem algo, ações em no máximo 2 cliques. Landing pública com nota Lighthouse mobile igual ou acima de 90 (o site atual já tira 93 a 96).

### X. Números saem de dados, não de impressão
Dashboards mostram fonte e período. Comparações entre unidades usam a mesma régua (mesmos eventos, mesmo período).

### XI. A rede é dona dos dados estruturados e do SEO técnico
Schema (LocalBusiness/MedicalBusiness ou subtipo), mapeamento NAP, categorias, sameAs, FAQ base, title, description, canonical, robots, sitemap, hreflang e scripts são definidos pela rede (perfil SEO) e gerados pelo sistema. A unidade alimenta valores (horário, fotos, equipe), nunca a estrutura. Nenhum perfil de unidade injeta script, meta tag ou JSON-LD.

### XII. A rede pode corrigir qualquer unidade, sempre às claras
Perfis da rede com permissão de edição alteram ficha e landing de qualquer unidade sem passar pela fila de aprovação. Toda alteração assim exige motivo, grava antes e depois na auditoria, avisa o franqueado (e-mail e sino) com o diff e pode ser revertida por versão. O franqueado pode contestar por chamado; ele não desfaz sozinho uma alteração da rede em campo travado.

### XIII. Configuração por escopo e ajuda em todo lugar
Módulos, recursos, modelos de ficha, menus, variantes de landing e relatórios automáticos são configuração, não código: a rede liga e ajusta por rede, regional e unidade, com herança e sem deploy. Toda tela tem ajuda contextual que leva à Wiki, com artigos por perfil.

## Governança
Emendas mudam a versão (MAJOR remove princípio, MINOR adiciona, PATCH esclarece). Toda spec cita os princípios afetados; toda revisão de tela confere II, III, V, VII, VIII, XI, XII e XIII.
