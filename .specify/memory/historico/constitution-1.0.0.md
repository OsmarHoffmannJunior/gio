# Constituição: Plataforma de Unidades Salus (marca Gio primeiro)

Versão 1.0.0, 21/11/2026. Vale para spec, plano, telas e código.

## Princípios

### I. Multi-marca e multi-tenant desde o primeiro dia
Um código, um deploy, um banco com `marca` e `unidade` em toda tabela de negócio. A Gio é a marca 1; a Sorridents entra como marca 2 sem fork. Tema (cores, logo, fontes, textos legais) é dado da marca, nunca código.

### II. A unidade é a fonte da verdade do NAP
Nome, endereço, telefone, WhatsApp, horários e coordenadas são cadastrados uma vez e alimentam landing, schema, sitemap, listagem pública e checklist do Google Meu Negócio. Coordenadas e horário estruturado são obrigatórios para publicar.

### III. Toda conversão é confirmada no servidor
Evento de lead e de agendamento só existe depois que o servidor aceitou. Nada de conversão no clique. Todo evento carrega `marca`, `unidade_id`, `template` e origem, e nunca carrega dado pessoal.

### IV. Não competir com DocBiz nem com o CRM
A plataforma capta, qualifica, roteia e mede. Agenda, prontuário e gestão da clínica ficam na DocBiz; CRM fica onde a Salus decidir (Salesforce visto na API). Integração por API/webhook, com fila e reprocessamento; sem integração disponível, exportação e importação.

### V. Autonomia do franqueado com limites da marca
O franqueado edita a própria unidade sem pedir a ninguém. Blocos de marca e compliance são travados; mudanças sensíveis (fotos de antes e depois, promoções, textos de tratamento) passam por aprovação. Regras de texto da Gio: sem valores, sem protocolo da rede, sem marca de equipamento, "avaliação gratuita" nos CTAs.

### VI. Uma URL canônica por unidade
Domínio próprio é opção, nunca duplicação. A franqueadora decide por unidade: ficha oficial canônica (padrão), domínio canônico, ou domínio que redireciona. O GBP aponta para a canônica.

### VII. Privacidade por padrão (LGPD)
Consentimento desmarcado, registrado com versão do texto, data e IP real. Sem PII em URL, cookie de marketing ou dataLayer. Acesso a dados pessoais registrado em auditoria. Papel de agência nunca vê PII.

### VIII. Acesso pelo menor escopo
Cada usuário vê só as unidades do seu escopo (rede, grupo de unidades, unidade). Permissão por papel e por módulo; toda ação de escrita gera log.

### IX. Desenho corporativo, rápido e legível
Interface densa mas calma: tabelas com filtros salvos, números grandes só onde decidem algo, ações em no máximo 2 cliques. Landing pública com nota Lighthouse mobile igual ou acima de 90 (o site atual já tira 93 a 96).

### X. Números saem de dados, não de impressão
Dashboards mostram fonte e período. Comparações entre unidades usam a mesma régua (mesmos eventos, mesmo período).

## Governança
Emendas mudam a versão (MAJOR remove princípio, MINOR adiciona, PATCH esclarece). Toda spec cita os princípios afetados; toda revisão de tela confere II, III, V, VII e VIII.
