# Respostas do Osmar às decisões da spec 003 (21/11/2026, 09h42, horário de Brasília)

1. D5 Arquitetura: APROVADO coletor próprio no nosso domínio, com validação, deduplicação, gravação no nosso banco e envio pelo servidor (GA4, Meta, TikTok, Google Ads).
2. D7/D16 Analytics: o Analytics é da rede (uma propriedade por marca, unidade como dimensão). Quando a unidade tiver domínio próprio, a rede precisa receber acesso ao Analytics/Search Console da unidade para coletar os dados também (requisito de provisionamento do domínio próprio).
3. D1 a D4 Quiz fase 1: APROVADO (só perguntas de estética, sem dados de saúde, unidade só a partir de modelo, sem incentivo por enquanto).
4. D15 Dono do tracking: APROVADO, uma pessoa nomeada na Gio.
5. D10 a D14: APROVADO 25 meses de eventos brutos; fontes pagas desligadas por enquanto; Trends por exportação manual.

## 10h14 (horário de Brasília)
6. D6: APROVADO guardar eventos de forma barata (banco próprio + arquivo Parquet no R2 + export GA4/BigQuery sandbox).
7. D8: APROVADO banner de consentimento próprio (guia ANPD + Consent Mode v2).
8. D9: APROVADO nomes dos eventos em português (objeto_acao).
Todas as 16 decisões da spec 003 resolvidas.
