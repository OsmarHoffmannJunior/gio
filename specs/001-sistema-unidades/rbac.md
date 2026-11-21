# Matriz RBAC: perfil x escopo x módulo x ação

Versão 1.0, 21/11/2026. Princípios: VIII, XI, XII, VII. Proposta para validação do Osmar e da Gio.

## Modelo
Permissão efetiva = **perfil** (função) x **escopo** (rede, regional ou unidade) x **módulo** x **ação**.

- **Ações:** V ver · E editar · A aprovar · P publicar · X exportar · D dado pessoal (nome, telefone, e-mail completos do lead).
- **Escopo:**
  - Rede: todas as unidades da marca.
  - Regional: lista de unidades atribuída (ex.: "SP interior", "Sul").
  - Unidade: uma ou mais unidades. O multifranqueado é o perfil Franqueado com N unidades no escopo, não um perfil à parte.
- Uma pessoa pode ter mais de uma atribuição (ex.: Gerente na unidade A e Leitura na unidade B). Vale a soma, sempre dentro do escopo de cada atribuição.
- Na unidade, "E" respeita a política de campos (`politica-campos.md`). Na rede, "E" publica direto (princípio XII: motivo, auditoria, aviso ao franqueado).
- "P" sem "A" significa publicar só o que não exige aprovação.

## Perfis padrão
| Código | Perfil | Nível | Para quem |
|---|---|---|---|
| R-ADM | Admin da rede | Rede | Dono da plataforma na Gio. Tudo, inclusive perfis e marca |
| R-MKT | Marketing | Rede | Conteúdo, landings, templates, campanhas, aprovações de conteúdo |
| R-SEO | SEO | Rede | Dados estruturados, SEO técnico, domínio, GBP, aprovações de SEO |
| R-COM | Comercial/Atendimento | Rede | Gestão comercial dos leads, SLA, distribuição |
| R-CC | Call center | Rede ou regional | Opera a fila de leads atribuída |
| R-FIN | Financeiro/Leitura | Rede | Leitura de indicadores e relatórios, sem dado pessoal |
| R-AG | Agência (externo) | Rede ou regional | Analytics, campanhas e SEO com aprovação. Nunca dado pessoal (princípio VII) |
| G-REG | Gestor regional | Regional | Consultor de campo: acompanha e cobra as unidades da região |
| U-FRQ | Admin da unidade (franqueado) | Unidade | Conta entregue pela rede no provisionamento, por convite. Edita conforme a política e convida a equipe só nos perfis de unidade liberados (padrão U-GER e U-REC) |
| U-GER | Gerente da unidade | Unidade | Operação do dia a dia: ficha, landing, leads |
| U-REC | Recepcionista | Unidade | Atende leads e consulta a ficha |

## Matriz padrão (módulo x perfil)
Célula vazia = sem acesso. "agr." = só agregados, sem linha de lead. "pol." = conforme a política de campos. "fila" = só leads da fila atribuída.

| Módulo | R-ADM | R-MKT | R-SEO | R-COM | R-CC | R-FIN | R-AG | G-REG | U-FRQ | U-GER | U-REC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Ficha da unidade | V E A P X | V E A P (conteúdo) | V E A P (NAP, área, SEO) | V | V | V | V | V | V E P (pol.) | V E P (pol.) | V |
| Landing da unidade | V E A P | V E A P | V E A P (blocos SEO) | V | V | V | V E (vai para aprovação) | V | V E P (pol.) | V E P (pol.) | V |
| Dados estruturados e SEO técnico | V E A P | V | V E A P X | | | | V E (vai para aprovação) | V | V (prévia) | V (prévia) | |
| Domínio e canonical | V E A P | V | V E A P | | | | V | V | V E (pedido e DNS) | V | |
| Fila de aprovações | V A | V A (conteúdo) | V A (SEO) | | | | V (próprios envios) | V | V (próprios envios) | V (próprios envios) | |
| Leads | V E X D | V X (agr.) | V (agr.) | V E X D | V E D (fila) | V (agr.) | V X (agr.) | V (agr.) | V E D, X sem PII (X com PII só se a rede liberar) | V E D, X sem PII | V E D (mascarado, ação pelos botões) |
| Dashboards e relatórios | V X | V X | V X | V X | V (fila) | V X | V X (agr.) | V X | V X | V X | V |
| Avaliações Google (leitura do GBP) | V | V | V | V | | V | V | V | V (responde no próprio GBP) | V (responde no próprio GBP) | V |
| Suporte | V E | V E | V E | V E | V E | V E | V E (próprios) | V E | V E | V E | V E |
| Usuários e perfis | V E | | | | | | | V | V E (só perfis U-GER e U-REC da própria unidade) | V | |
| Auditoria geral | V X | V | V | V | | V | | | | | |
| Solicitações LGPD do titular | V E X D | | | V (leitura) | | | | | V (encaminhar pedido) | V (encaminhar pedido) | V (encaminhar pedido) |
| Wiki e central de ajuda | V E P | V E P | V E P | V | V | V | V | V | V | V | V |
| Relatórios inteligentes (insights) | V E | V E | V E | V E | V | V | V (agr.) | V | V | V | |
| Módulos e recursos (feature toggles) | V E | | | | | | | V | | | |
| Modelos de ficha e menu | V E P | V E P | V E P | | | | | V | V (prévia) | V (prévia) | |
| Marca, templates, catálogo, regras, SLA | V E A P | V E (A do R-ADM) | V E (schema base, A do R-ADM) | V E (SLA e distribuição) | | V | | V | | | |
| Integrações (DocBiz, CRM, GA4/GTM, Search Console) | V E | | V E (GA4, GTM, Search Console) | V (status) | | | V (status) | | | | |

## Regras transversais
0. **LGPD (decisão do Osmar, 21/11/2026):** a rede é controladora e as unidades são operadoras. Perfis de unidade veem dado pessoal só dos leads da própria unidade, mascarado por padrão, para atender. Exportar com PII é exceção liberada pela rede. Pedidos do titular entram e são resolvidos na rede; a unidade só encaminha.

1. **Teto por escopo:** um perfil personalizado não passa do teto do seu nível.
   - Unidade: nunca Dados estruturados (E), Marca, Integrações, outra unidade nem ação da rede.
   - Regional: nunca Marca nem Integrações.
2. **Dado pessoal:**
   - D é concedido à parte. X com D exige 2FA, motivo e gera arquivo com link que expira em 24 h.
   - R-AG nunca recebe D, nem por perfil personalizado (bloqueio no banco).
3. **Segregação:** quem envia uma mudança não aprova a mesma mudança. R-ADM pode publicar direto (override), mas isso não conta como "aprovação": é uma "alteração da rede" (princípio XII).
4. **Override da rede (decisão 1 do Osmar):** R-ADM, R-MKT (conteúdo) e R-SEO (SEO) editam e publicam em qualquer unidade do escopo sem fila. São obrigatórios:
   - motivo;
   - registro de antes e depois na auditoria;
   - aviso ao franqueado e ao gerente com o diff;
   - versão para reverter.
   Edição em massa (ex.: FAQ base em 130 unidades) gera um aviso agregado por unidade.
5. **2FA:** obrigatório para todo perfil de rede e regional, e para qualquer perfil com X ou D.
6. **Expiração:** perfis externos (R-AG) e temporários têm data de fim. Contas sem login há 90 dias são suspensas.
8. **Contas só por convite (decisão do Osmar, 21/11/2026):** não há autocadastro. A rede convida perfis de rede, regional, parceiros e o U-FRQ de cada unidade provisionada. O U-FRQ convida U-GER e U-REC da própria unidade. Convite de uso único, 72 h; primeiro acesso troca a senha e ativa 2FA (U-REC só se a rede exigir).
7. **Ver como:** R-ADM pode simular a visão de qualquer perfil, só leitura e registrado na auditoria. Serve para suporte e para testar perfis personalizados.

## Rev. 3.2 (21/11/2026): módulos das specs 002 e 003
Aplicado das notas de impacto da 002 e da 003. Ação "dado pessoal" (D) vale também para clientes da área do cliente. Funções comerciais de unidade só valem se liberadas pela rede (interseção do perfil com `liberacao` e `limite_envio` da 002, princípio XVI).

| Módulo | R-ADM | R-MKT | R-SEO | R-COM | R-CC | R-FIN | R-AG | G-REG | U-FRQ | U-GER | U-REC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clientes | V E D X | V (agr.; D só se a rede der) | | V E D X | V E D (fila) | | | V (agr.) | V, D mascarado (vinculados) | V, D mascarado (vinculados) | V, D mascarado (vinculados) |
| Ofertas e preços | V E A P | V E A P | | V | | V | | V | V E (se liberado) | V E (se liberado) | V |
| Promoções | V E A P | V E A P | | V | | V | | V | V E (se liberado) | V E (se liberado) | V |
| Campanhas para clientes | V E A P | V E A P | | V | | | V X (agr.) | V | V E (se liberado, dentro da cota) | V E (se liberado) | |
| Mural de avisos | V E P | V E P | | V E P | | | | V (E P na regional, se liberado) | V (confirmar) | V (confirmar) | V |
| Controles da rede | V E | V E (com motivo) | | | | | | V | | | |
| Vendas e pacotes | V X | | | V | | V X | | V | V X (agr.) | V | V (check-in) |
| NPS | V E | V | | V E | | | | V | V | V | |
| Financeiro do cliente | V E X | | | | | V E X | | | V (da unidade) | | |
| Performance | V X | V X | | V | | V X | V X (agr.) | V | V X (agr.) | V | |
| Quiz | V E A P | V E A P | | | | | V (agr.) | V | V E (se liberado) | V E (se liberado) | |
| Inteligência | V X | V X | V X | V | | V | V (agr.) | V | V (da unidade) | V | |
| Tracking e tags | V E A P | V | V E A P (dono do tracking) | | | | V (dicionário e agregados) | V | E nos campos de tags liberados | | |

**Teto por nível (002):** perfil de unidade nunca alcança base nacional, outra unidade, Controles da rede, Financeiro de outra unidade nem exportação de clientes com PII. **Contas:** a regra 8 (só convite) vale para usuários internos; clientes se cadastram sozinhos na área do cliente (spec 002).
**Auditoria geral (pedido do Osmar, 21/11/2026, 09h52):** só perfis de rede veem a auditoria geral (R-ADM vê e exporta; R-MKT, R-SEO, R-COM e R-FIN veem; R-AG, R-CC, regionais e unidades não veem). Nenhum perfil edita ou apaga registro, nem por perfil personalizado (teto no banco). A unidade continua recebendo o aviso de cada alteração da rede na própria ficha pelas notificações.

## Perfis personalizados
- Criados só pela rede (R-ADM), a partir de um perfil padrão (clonar e ajustar) ou do zero, sempre dentro do teto do nível.
- Exemplos esperados:
  - "SEO sem domínio";
  - "Marketing regional Sul";
  - "Gerente sem exportação";
  - "Recepção sem dado pessoal (só vê primeiro nome)";
  - "Agência de mídia" (só Leads agr. e Relatórios).
- Mudança num perfil vale para todos que o usam e entra na auditoria com o diff de permissões.
- A tela mostra, para cada perfil, quantas pessoas o usam e um simulador "ver como".
