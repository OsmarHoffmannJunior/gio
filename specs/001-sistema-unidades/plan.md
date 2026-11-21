# Implementation Plan: Plataforma de Unidades Gio

**Branch**: `001-sistema-unidades` | **Date**: 2026-11-21 | **Spec**: spec.md

## Summary
App multi-tenant e multi-marca com três superfícies: (1) painel interno (Admin Gio, call center, agência, multifranqueado, unidade), (2) landings públicas por unidade em 3 templates, com domínio próprio opcional, (3) portal de suporte do cliente final. Integra DocBiz, CRM e WhatsApp; mede por eventos confirmados no servidor.

## Technical Context (recomendação, custos em `custos/custos.md`)
- Front e SSR: Next.js (App Router) em um projeto Vercel Pro, domínios custom por API.
- Banco: Postgres (Neon, always-on), RLS por `marca_id` e escopo do usuário.
- Mídia: Cloudflare R2 com otimização na borda.
- E-mail: Resend Pro. WhatsApp: template utility opcional.
- Filas e webhooks: fila com reprocessamento para DocBiz/CRM.
- Analytics: GA4 + Ads via GTM único da rede, eventos server-side; tabela própria de eventos para jornada e dashboards.
- Infra estimada no cenário base de 130 unidades: R$ 482,54/mês (R$ 3,71 por unidade). Desenvolvimento: faixa ilustrativa de R$ 60 mil a R$ 315 mil (400 a 900 h), não é orçamento.

## Constitution Check
I multi-marca: tabelas com `marca_id`, tema por marca. OK
II NAP único: unidade alimenta landing, schema, sitemap, GBP. OK
III conversão no servidor: eventos só após 2xx. OK
IV DocBiz/CRM: só integração, sem agenda própria. OK
V limites da marca: blocos travados, validador, aprovação. OK
VI canonical único: campo `estrategia_canonical`. OK
VII LGPD: consentimento versionado, PII fora de analytics. OK
VIII menor escopo: RLS + papéis. OK

## Estrutura de módulos
```
app/
  (painel)/rede, unidades, unidades/[id]/{dados,horarios,tratamentos,fotos,landing,dominio,seo,integracoes,usuarios,historico}
  (painel)/leads, leads/[id], relatorios, suporte, base, usuarios, auditoria, config/{marca,templates,catalogo,sla,regras}
  (franqueado)/inicio, minha-unidade, landing, leads, suporte, relatorios
  (publico)/unidade/[slug]  + domínios custom via middleware
  (cliente)/ajuda, solicitacoes
api/ leads, eventos, webhooks/docbiz, webhooks/crm, gbp-sync, dominios
```

## Fases
0. Correções no site atual (canonical, title, sitemap, evento confirmado, consentimento, limpeza de GTMs).
1. MVP: importação AGDM, cadastro da unidade, 1 template, login franqueado, central de leads com status, eventos, SEO local.
2. 3 templates, editor por bloco, aprovações, domínio próprio, GBP.
3. DocBiz/CRM bidirecional, conversão offline, jornada, dashboards e relatórios agendados.
4. Suporte (tickets, base, cliente final) e Sorridents como marca 2.

## Riscos
DocBiz sem API; papel do Salesforce indefinido; transição com a DocPix; adesão dos franqueados; LGPD.

## Rev. 2 (21/11/2026): impacto das decisões do Osmar no plano
- Constituição 1.1.0: princípios V e VIII revistos, XI e XII novos. Verificação: as telas 05, 11 e 13 hoje não atendem a XI e XII e precisam mudar (ver telas.md).
- A fase 1 passa a incluir o núcleo de RBAC (perfil, atribuicao, teto, RLS com PII), a política de campos e o versionamento por campo, porque a edição da unidade depende deles.
- O schema base e o validador de JSON-LD entram na fase 1 junto com a landing, já que nenhuma unidade publica sem schema válido.
- Riscos novos (contrato de franquia, dono do GBP, controlador LGPD, promoções) ficam em spec.md, seção "Riscos e lacunas" e "Decisões em aberto".

## Rev. 3.2 (21/11/2026): specs 002 e 003
- Integrações novas: gateway com split opcional (recebimento direto pelo franqueado, pendente de confirmar participação da rede), emissor de NFS-e (se a DocBiz não emitir), WhatsApp Business Platform, e-mail transacional e de marketing, push (FCM e APNs), provedor OIDC (ou implementação própria).
- Custos: rever `custos/custos.md` com mensageria e gateway coletados por script em fontes oficiais. Server-side de tags fica fora (usa o stack existente).
- Fase 0 já prevê a limpeza do tracking no site atual. Fase 1 ganha coletor próprio, carregador único, banner de consentimento e dicionário v1 de eventos.
- Wiki: guia de configuração do gerenciador de tags em arquivo e vídeo antes de abrir as tags às unidades.
- Ordem sugerida: 001 fase 1, 002 fase 1 (conta, controles, mural, agendamento, campanhas da rede), 002 fase 2 (pagamento, pacotes, campanhas de unidade), app.
