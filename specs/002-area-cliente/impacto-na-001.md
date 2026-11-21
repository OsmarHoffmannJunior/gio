# Impacto da 002 na spec 001 (notas de integração)

Rev. 1b, 21/11/2026. Esta nota lista o que a spec 001 precisará mudar para receber a Área do Cliente. **Nenhum arquivo da 001 foi alterado por esta spec**; quem estiver editando a 001 aplica estes itens quando a 002 for aprovada.

## Constituição (proposta de versão 1.3.0, MINOR)
1. **Novo princípio XIV. API única para site, painéis e app.** Toda regra de negócio vive na API versionada; site, painéis e app futuro são clientes dela. Autenticação de clientes (OIDC com PKCE) separada da autenticação de usuários internos.
2. **Novo princípio XV. Dado de saúde fora da plataforma até decisão expressa.** Anamnese, contraindicações, prontuário e fotos clínicas ficam na DocBiz. Entrar com isso na plataforma exige RIPD, consentimento específico e emenda da constituição.
3. **Novo princípio XVI. A rede libera, a unidade opera dentro do limite.** Funções comerciais de unidade (preço, procedimentos locais, promoções, campanhas, canais, avisos regionais) nascem bloqueadas; a rede libera por escopo e define cotas, frequência e alcance máximo. Nenhuma unidade alcança a base nacional (teto no banco).
4. **Princípio I:** acrescentar "conta de cliente por marca".
5. **Princípio III:** estender a "cadastro de cliente confirmado, agendamento confirmado pela DocBiz e pedido pago confirmado pelo webhook do gateway".
6. **Princípio IV:** deixar explícito que pacotes e sessões têm a DocBiz como fonte do consumo; a plataforma exibe e vende, mas não substitui agenda nem prontuário.
7. **Princípio V:** a regra "sem valores" passa a depender da política de preço da rede por procedimento (D1 da 002); hoje vale "sem valores" no conteúdo público.
8. **Princípio VII:** incluir clientes (além de leads) e consentimento por canal de marketing; "unidade só vê clientes com vínculo".

## spec.md da 001
- **Papéis:** a linha "Público / Cliente final" passa a apontar para a 002 (conta, agendamentos, compras, privacidade), não só suporte.
- **Regra nova de contas (pedido do Osmar, 09h10):** "sem cadastro manual de conta interna" vale para usuários da rede e das unidades. **Não vale para clientes**, que se cadastram sozinhos na área do cliente. Deixar isso escrito para não haver conflito.
- **US4 (leads):** lead verificado vira ou se liga a um cliente (`lead.cliente_id`); a jornada do lead continua na timeline do cliente.
- **US5 (dashboards):** blocos novos de clientes, campanhas, NPS e vendas online no dashboard da rede e da unidade.
- **US9 (suporte):** chamados de cliente vêm da área do cliente com `cliente_id` e canal.
- **US16 (módulos):** novo módulo "Área do cliente" e submódulos "Pagamento online", "Campanhas de unidade", "Chat com cliente", "Mural de avisos".
- **US19 (LGPD):** pedidos do titular passam a chegar também pela central de privacidade do cliente.
- **FR-024 (promoções):** amplia para modelos com tipos, preço opcional conforme D1, adesão às promoções da rede e regulamento.
- **Decisão D9 da 001 (modelo de promoção):** passa a ser tratada junto com D1 (preço) da 002.
- **Fora de escopo da 001:** "financeiro (DocBiz)" continua, mas a venda online e o split ficam na 002.
- **Novos FRs referenciados:** FR-101 a FR-160 da 002.

## rbac.md
- Novos módulos na matriz: Clientes, Ofertas e preços, Promoções (já parcial), Campanhas para clientes, Mural de avisos, Controles da rede, Vendas e pacotes, NPS, Financeiro do cliente, Performance.
- Proposta de matriz padrão:
  - R-ADM: tudo.
  - R-MKT: Campanhas (V E A P), Mural (V E P), Promoções (V E A P), Performance (V X), Controles (V E com motivo), Clientes (V agregado; D só se a rede der).
  - R-COM: Clientes (V E D X), NPS (V E), Vendas (V), Mural (V E P).
  - R-FIN: Vendas e pacotes (V X), Financeiro do cliente (V E X), sem D.
  - R-CC: Clientes da fila (V E D), Agendamentos (V E).
  - R-AG: Campanhas e Performance só agregados (V X), nunca D.
  - G-REG: Performance e Atividade da regional (V), Mural da regional (V E P se liberado), Controles (V).
  - U-FRQ e U-GER: Clientes vinculados (V, D mascarado), Ofertas, Promoções, Campanhas e canais **só se liberados** (interseção com `liberacao` e `limite_envio`), Mural (V e confirmar), Resultados (V X agregado).
  - U-REC: Clientes vinculados (V, D mascarado), agendamentos e check-in, Mural (V).
- **Teto por nível:** perfil de unidade nunca alcança base nacional, outra unidade, Controles da rede, Financeiro de outra unidade nem exportação de clientes com PII.
- Ação "dado pessoal" vale também para clientes.

## politica-campos.md
- Campos 33 e 34 (promoção) e o bloco Promoções (54) passam a respeitar a liberação "promocoes" da 002: se bloqueado, viram T para a unidade.
- Novos itens: preço por procedimento (T por padrão; E ou EA se liberado), duração local (E), procedimento comercializável online (EA), pacote local por modelo (EA), texto local do procedimento (E com validador).

## dados-ficha.md
- Aba "Tratamentos" vira "Procedimentos e preços" (oferta_unidade): ativo, duração local, preço, visibilidade, comprável online, texto local, destaque.
- Novos dados da unidade: conta de recebimento (subconta do gateway, status KYC), política de agenda (remarcação, no-show), NFS-e (emissor, município), raio padrão de alcance.

## data-model.md
- `tratamento` → `procedimento` com campos novos (ou visão de compatibilidade).
- `unidade_tratamento` → `oferta_unidade`.
- `lead` ganha `cliente_id`.
- `consentimento` ganha `titular_tipo`, `titular_id`, `finalidade`, `canal`, `texto_legal_id`, `acao`, `origem`.
- `promocao` e `modelo_promocao` ampliados (ver `data-model.md` da 002).
- `notificacao` ganha tipo `aviso`; `ticket` ganha `cliente_id` e canal.
- `perfil_permissao.modulo` ganha os novos módulos.
- `modulo` ganha `area_cliente`, `pagamento_online`, `campanhas_unidade`, `chat_cliente`, `mural_avisos`.
- `regra_insight.tipo` ganha `campanha_destaque`, `cota_estourada`, `nps_baixo`, `no_show_alto`, `aviso_pendente`.
- `politica_retencao` ganha entidades da 002.
- `pedido_titular` ganha `cliente_id`.

## telas.md da 001
- Menu lateral do admin: grupos "Clientes", "Campanhas", "Mural" e "Controles".
- Menu do franqueado: "Clientes e vendas", "Campanhas" (cadeado se não liberado), "Mural" com contador de não lidos.
- Dashboard da rede (tela de dashboard) e do franqueado: cartões de clientes, campanhas, NPS e avisos pendentes.
- Ficha da unidade: aba "Procedimentos e preços"; seção "O que a rede liberou".
- Central de leads: indicador "já é cliente" e link para a ficha do cliente.
- Solicitações LGPD: origem "área do cliente".
- Usuários e perfis: novos módulos na edição de perfil.
- Módulos e recursos: novos módulos e a matriz de liberação (pode ser a mesma tela, com abas).

## plan.md
- Novas integrações: gateway com split, emissor de NFS-e (se a DocBiz não emitir), WhatsApp Business Platform, provedor de e-mail transacional e marketing, push (FCM e APNs), provedor OIDC (ou implementação própria).
- Custos: rever `custos/custos.md` com mensageria (WhatsApp por mensagem, e-mail por volume) e gateway (taxas) coletados por script em fontes oficiais.
- Ordem sugerida: 001 fase 1 > 002 fase 1 (conta, controles, mural, agendamento, campanhas da rede) > 002 fase 2 (pagamento, pacotes, campanhas de unidade) > app.
