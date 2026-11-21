# Inventário de telas: Área do Cliente (002)

Rev. 1b, 21/11/2026. Só inventário; nenhuma tela desenhada ainda. Numeração C (cliente), U (painel da unidade), R (painel da rede), para não colidir com as telas 01 a 32 da 001. Prioridade: P1 no MVP, P2 fase 2, P3 fase 3. Todas as telas do cliente nascem mobile first (o app futuro reaproveita fluxos e componentes).

## Cliente (site responsivo e, depois, app)
| # | Tela | Conteúdo principal | Prio |
|---|---|---|---|
| C01 | Entrar ou criar conta | E-mail ou celular, Google, Apple; texto curto do benefício; link para privacidade | P1 |
| C02 | Código de verificação | 6 dígitos, reenviar com contador, trocar canal (e-mail ou WhatsApp), link mágico | P1 |
| C03 | Dados básicos | Nome, cidade (sugerida), "tenho 18 anos ou mais", termos e privacidade desmarcados, marketing por canal desmarcado | P1 |
| C04 | Onboarding de interesses (pulável) | Chips de procedimentos, unidade preferida no mapa, como conheceu, data de nascimento; barra de progresso | P1 |
| C05 | Início do cliente | Próximo agendamento, pacote ativo com sessões, ofertas para você, completar perfil, avisos | P1 |
| C06 | Ofertas para você | Cartões de promoções e campanhas (rede e unidade preferida), "Perto de você", filtro por procedimento, "por que estou vendo isso" | P1 |
| C07 | Catálogo de procedimentos | Categorias, busca, cartões com sessões típicas; preço conforme visibilidade | P1 |
| C08 | Detalhe do procedimento | Para que serve, indicação, sessões, intervalo, cuidados pré e pós, unidades que oferecem, preço (logado ou promoção), CTA agendar ou comprar | P1 |
| C09 | Escolher unidade | Mapa e lista com distância, horário, nota do Google; definir preferida | P1 |
| C10 | Agendar: horários | Calendário com horários reais (DocBiz), reserva temporária, política de remarcação visível | P1 |
| C11 | Agendar: confirmação | Resumo, rota, adicionar à agenda, cuidados pré; estado "solicitado" quando a DocBiz não confirmar na hora | P1 |
| C12 | Meus agendamentos | Próximos e passados; status; confirmar, remarcar, cancelar | P1 |
| C13 | Detalhe do agendamento | Data, unidade, profissional, rota, cuidados; remarcar e cancelar com regra | P1 |
| C14 | Meus pacotes | Lista com barra de sessões feitas e restantes, validade | P2 |
| C15 | Detalhe do pacote | Linha do tempo das sessões, próxima data sugerida, agendar próxima, regulamento, renovar | P2 |
| C16 | Checkout | Itens, unidade vendedora com razão social e CNPJ, regulamento, cupom de promoção, arrependimento de 7 dias explicado | P2 |
| C17 | Pagamento | Pix (QR e copia e cola com prazo), cartão com parcelas, carteira; estados aprovado, pendente, recusado | P2 |
| C18 | Minhas compras | Pedidos, status, recibos e notas para baixar, pedir cancelamento | P2 |
| C19 | Histórico de atendimentos | Data, unidade, procedimento, profissional (sem prontuário) | P2 |
| C20 | Avaliar sessão | Nota 0 a 10, comentário, convite para o Google mostrado a todos | P1 |
| C21 | Central de notificações | Todas as mensagens recebidas, filtros por tipo | P1 |
| C22 | Preferências de comunicação | Canais, horários, frequência; opt-out em 1 toque | P1 |
| C23 | Privacidade | Consentimentos com data e versão, revogar, baixar dados, corrigir, excluir conta, status dos pedidos | P1 |
| C24 | Meu perfil | Dados pessoais, contatos verificados, completude, sessões e dispositivos conectados | P1 |
| C25 | Ajuda e conversa | Artigos da Wiki pública, abrir conversa com a unidade ou a rede, acompanhar chamado | P2 |
| C26 | Estados vazios e erros | Sem agendamento, sem pacote, sem oferta, DocBiz fora, pagamento recusado, sessão expirada | P1 |
| C27 | Perfis familiares | Dependentes, alternar perfil | P3 |
| C28 | Carteira e fidelidade | Créditos, cashback, vale-presente, indicação | P3 |

## Painel da unidade (dentro do painel da 001, menu novo "Clientes e vendas")
| # | Tela | Conteúdo principal | Prio |
|---|---|---|---|
| U01 | Clientes da unidade | Tabela com filtros (vínculo, interesse, faixa etária, última visita, pacote, NPS), PII mascarada, "ver dado" auditado, contagens por consentimento | P1 |
| U02 | Ficha do cliente (visão da unidade) | Resumo 360 limitado à unidade: agendamentos, pacotes, compras, NPS, campanhas recebidas; sem dados de outras unidades | P1 |
| U03 | Procedimentos e preços | Catálogo da rede com ativar, duração local, preço (se liberado), visibilidade; itens bloqueados com cadeado e "pedir liberação" | P1 |
| U04 | Pacotes da unidade | A partir dos modelos da rede: preço, parcelas, comprável online | P2 |
| U05 | Promoções da unidade | Lista e criação por modelo; adesão às promoções da rede | P1 |
| U06 | Campanhas: lista | Rascunhos, em aprovação, no ar, encerradas; cota usada e restante; "usar campanha da rede" | P1 (se liberado) |
| U07 | Campanha: assistente em 8 passos | Objetivo e modelo, oferta, público, alcance (só dentro do teto), canais e conteúdo, período, prévia de alcance e custo, revisão | P1 (se liberado) |
| U08 | Resultados da unidade | Funil da unidade, campanhas, vendas online, no-show, NPS, posição frente à mediana da rede | P1 |
| U09 | Vendas e pacotes ativos | Pedidos, pagamentos, estornos, pacotes a vencer, sessões restantes | P2 |
| U10 | Agenda online | Políticas de remarcação e no-show da unidade dentro dos limites; status da integração DocBiz; solicitações pendentes (fallback) | P1 |
| U11 | Avaliações NPS | Notas, comentários, casos de recuperação com SLA | P1 |
| U12 | Mural de avisos | Avisos da rede, fixados no topo, confirmar leitura, pendentes com prazo | P1 |
| U13 | O que a rede liberou | Funções liberadas, bloqueadas, limites e cotas da unidade, pedidos de liberação | P1 |
| U14 | Conversas com clientes | Caixa de chamados de clientes com SLA | P2 |

## Painel da rede (menu novo "Clientes", "Campanhas" e "Controles")
| # | Tela | Conteúdo principal | Prio |
|---|---|---|---|
| R01 | Painel de clientes da rede | Base total, crescimento, completude, consentimento por canal, interesses por UF e cidade, funil cadastro > agendamento > compra | P1 |
| R02 | Controles da rede (matriz de liberação) | Funções x escopo (rede, regional, unidade) com herança, exceções, padrão bloqueado; impacto ao bloquear | P1 |
| R03 | Limites e alcance | Cotas por período, orçamento de WhatsApp, frequência por cliente, janela, alcance máximo (própria unidade, raio, cidades, UF) por escopo | P1 |
| R04 | Mural: criar aviso | Público (unidades, regionais, filtros, perfis), categoria, prioridade, anexos, fixar, confirmação com prazo, canais; contagem de alcance | P1 |
| R05 | Mural: relatório de leitura | Entregue, aberto, confirmado e pendente por unidade e perfil; reenviar a pendentes | P1 |
| R06 | Biblioteca de modelos de campanha | Modelos por objetivo, campos travados e livres, canais, escopos, aprovação obrigatória | P1 |
| R07 | Campanha da rede: assistente | Os 8 passos sem teto de unidade; alcance por UF, cidade, raio ou unidades específicas; aviso automático às unidades afetadas | P1 |
| R08 | Fila de aprovação de campanhas | Prévia por canal, segmento, alcance, custo, validador; aprovar, reprovar com motivo, pedir ajuste | P1 |
| R09 | Painel de performance | Filtros por período, regional, UF, unidade, canal, objetivo, modelo, procedimento; funil até venda; custo | P1 |
| R10 | Atividade das unidades | Campanhas criadas, enviadas, reprovadas, cota usada, promoções no ar, avisos pendentes, unidades paradas | P1 |
| R11 | Comparativo | 2 a 5 campanhas ou unidades lado a lado com mediana da rede | P2 |
| R12 | Cruzamento de dados | Tabela dinâmica por dimensões, destaques automáticos com amostra mínima | P2 |
| R13 | Replicar campanha | Destinos, ajuste ao teto de cada unidade, prévia por unidade, publicar ou propor | P2 |
| R14 | Catálogo base e política de preço | Procedimentos, descrição aprovada, sessões, cuidados, visibilidade de preço, faixa sugerida | P1 |
| R15 | Modelos de pacote e promoção | Sessões, validade, regulamento; tipos de promoção | P1 |
| R16 | Textos legais e consentimentos | Versões de termos, privacidade, marketing, regulamentos; exigir novo aceite | P1 |
| R17 | Templates de mensagem | Por canal, categoria da Meta, variáveis, status de aprovação | P1 |
| R18 | Financeiro do cliente | Vendas por unidade, split, taxas, estornos, chargebacks, KYC das subcontas | P2 |
| R19 | NPS da rede | Ranking, comentários, casos abertos por unidade | P1 |
| R20 | Integrações da área do cliente | DocBiz, gateway, WhatsApp, e-mail, push: status, filas, reprocessar | P1 |

## Telas da 001 que mudam
Ver `impacto-na-001.md`: dashboard da rede e da unidade (blocos de clientes, campanhas e NPS), ficha da unidade (aba Procedimentos e preços vira oferta_unidade), central de leads (lead vinculado a cliente), solicitações LGPD (pedidos vindos da área do cliente), usuários e perfis (novos módulos), módulos e recursos (área do cliente e submódulos), menu lateral (novos grupos).
