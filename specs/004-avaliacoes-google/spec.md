# Feature Specification: Monitoramento e resposta de avaliações do Google por unidade

**Feature Branch**: `004-avaliacoes-google`
**Created**: 2026-11-21
**Status**: Draft (rev. 2, 21/11/2026 17h21: crítica de design aplicada; telas 19 e 80 a 87)
**Depende de**: `001-sistema-unidades` (unidades, RBAC, SEO local US13 e tela 19, auditoria só da rede US21, notificações), `002-area-cliente` (tom da marca, consentimento), `003-quiz-inteligencia-tracking` (temas e inteligência)
**Input**: Osmar, 21/11/2026: "Existe a opção de fazer monitoramento aqui (tela 19) e trazer insights pra respostas adequadas para atender quem avalia a unidade especificamente?" e "Aí cada cliente pode controlar o seu, né? E nós temos através do painel no geral, certo? Aí pode fazer levantamento."

## Contexto
- A tela 19 já mostra a nota e as últimas avaliações do perfil do Google da unidade, só para leitura. As respostas hoje são feitas por cada unidade direto no Google, sem padrão de tom, sem prazo e sem visão da rede.
- O perfil do Google (Google Business Profile, GBP) pertence à unidade. O sistema não edita o perfil (decisão da 001); responder avaliações é a única escrita prevista, e só com autorização do dono do perfil.
- Estética envolve dado sensível: uma resposta pública não pode confirmar que a pessoa é cliente, citar procedimento, sessão ou condição de saúde (LGPD art. 11 e código de ética profissional).

## Papéis
| Papel | O que faz nesta spec |
|---|---|
| Unidade (U-FRQ, U-GER) | Vê e responde só as avaliações da própria unidade; revisa, edita e publica a sugestão da IA |
| Unidade (U-REC) | Lê a fila e salva rascunho, se a rede liberar; não publica |
| Rede (R-ADM, R-MKT, R-SEO) | Visão geral de todas as unidades, levantamentos, exportação; acompanha ou assume avaliações escaladas |
| Rede (R-FIN, R-AG) | Só agregados (nota, volume, temas), sem texto nem nome de quem avaliou |

## Histórias de usuário

### US1. Coleta das avaliações por unidade (P1)
O sistema lê as avaliações de cada location do GBP pela API (nota, texto, data, nome público exibido pelo Google, status e texto da resposta) algumas vezes ao dia (padrão: a cada 4 horas, mais leitura sob demanda) e guarda o histórico.
**Acceptance**: 1. Given uma unidade com o perfil vinculado, When a leitura roda, Then avaliações novas aparecem na fila em até 4 horas, sem duplicar. 2. Given avaliação editada ou removida no Google, Then o sistema atualiza ou marca como removida. 3. Given falha de API ou perfil desvinculado, Then a unidade e a rede veem o aviso com a data da última leitura.

### US2. Fila de avaliações sem resposta (P1)
A unidade vê primeiro as sem resposta, com destaque para nota 1 a 3 e para as escaladas, filtros por nota, tema, sentimento e situação, e indicadores (nota no Google, sem resposta, tempo de resposta, volume do mês). Tela 80 (computador) e 82 (celular).

### US3. Classificação e sugestão de resposta por IA (P1)
Para cada avaliação, a IA classifica tema (atendimento, resultado, agendamento, preço, procedimento, estrutura e outros configuráveis pela rede) e sentimento (positivo, neutro, negativo), e escreve uma sugestão de resposta no tom da Gio que cita o que a pessoa disse.
**Regras da sugestão (bloqueantes)**: não confirmar que a pessoa é cliente ou paciente; não citar procedimento, data de sessão, resultado individual nem dado de saúde, mesmo que a pessoa tenha citado; quando houver relato de problema de saúde, agradecer, demonstrar cuidado e levar para canal privado (WhatsApp ou telefone da unidade), sem discutir o caso em público; não oferecer desconto nem prometer resultado; assinatura padrão da unidade. Um validador revisa o texto final (inclusive o editado pela unidade) e bloqueia termos proibidos, como o validador do quiz (003).
**Acceptance**: Given avaliação com relato de reação na pele, Then a sugestão não menciona o procedimento nem a reação e convida para contato privado com a responsável técnica.

### US4. Revisar, editar e publicar (P1)
A unidade revisa, ajusta com atalhos (mais curta, mais calorosa, convidar para conversar, gerar outra), salva rascunho ou publica. A publicação usa a API do GBP; a resposta aparece no Google em minutos. Telas 81 e 83.

### US5. Escalada para a rede (P1)
Avaliações com 1 ou 2 estrelas ou que mencionem problema de saúde avisam também a rede. A rede pode acompanhar (vê rascunhos e a resposta antes de sair) ou assumir (a resposta passa a ser da rede, e a unidade vê o texto antes da publicação).

### US6. Insights e levantamentos da rede (P1)
Painel da rede (tela 84, com link a partir da tela 19): nota média, % respondidas, tempo mediano de resposta, sem resposta, escaladas; recortes por unidade, região e tema; temas recorrentes com volume e negativas; ranking de quem responde mais rápido e de quem acumula pendentes; lista de escaladas; exportação CSV (registrada na auditoria) e lembrete às unidades com pendentes.

### US7. Workspace da rede e fila da unidade no casco da rede (P1)
A rede nunca entra no portal do franqueado. "Acompanhar" e "Assumir" abrem o workspace da rede (tela 86): avaliação, rascunho da unidade (se houver), linha do tempo, outras pendentes da unidade e as ações Acompanhar, Assumir a resposta, Devolver à unidade e, depois de assumir, Publicar como rede (com validador e confirmação). A lista completa de escaladas (85) filtra por situação, saúde, nota, tema, região e unidade. A fila de uma unidade (87) abre a partir da 19, da 84 e da 86, sempre no casco da rede.

## Estados e copy do fluxo de resposta (rev. 2)
| Estado | Onde | Comportamento |
|---|---|---|
| Gerando | 81, 83 | "A IA está sugerindo uma resposta no tom da Gio…"; atalhos e publicar desativados; não mostra texto final antes de chegar |
| Sugestão vazia ou falha | 81, 83 | "Não foi possível sugerir uma resposta. Você pode escrever a sua ou tentar de novo." Primário "Tentar de novo"; campo vazio focado |
| Recusar sugestão | 81, 83 | "Escrever do zero" limpa o campo, o título vira "Sua resposta" e os cuidados continuam à vista |
| Atalhos | 81, 83 | Mais curta, Mais calorosa, Convidar para conversar, Gerar outra: reescrevem o campo e avisam "Sugestão atualizada. Revise antes de publicar." |
| Validador ao vivo | 81, 83, 86 | Procedimento, sessão, dado de saúde, confirmar cliente ou prometer desconto travam o publicar com a frase do que tirar |
| Limite | 81, 83 | "X de 4.096"; aviso âmbar aos 3.900; acima de 4.096, "O Google aceita no máximo 4.096 caracteres." e publicar bloqueado |
| Confirmação | 81, 83, 86 | Nota 1 ou 2, ou saúde: "Esta avaliação foi avisada à rede. A resposta vai aparecer no Google em alguns minutos e não pode confirmar que a pessoa é cliente nem discutir o caso em público. Publicar mesmo?" |
| Publicada | 81, 83 | Aviso verde com hora, texto publicado, registro na auditoria e "Voltar para a fila"; respondidas abrem direto neste estado |
| Rascunho salvo | 81, 83 | "Rascunho salvo às HH:MM." |
| Rede assumiu | 81, 83 | Texto da rede em leitura, "A rede assumiu esta resposta. Você está vendo o texto antes de ele sair."; sem publicar |
| Recepção (U-REC) | 81, 83 | Sem publicar; primário "Salvar rascunho" e "Quem publica é a gerência da unidade." |
| Perfil desvinculado | 80, 82, 87 | "Perfil do Google não vinculado", data da última leitura e como vincular |
| Falha de leitura | 80, 82, 87 | "Não conseguimos ler o Google agora", última leitura bem sucedida e "Tentar agora" |
| Fila vazia | 80, 82, 87 | "Tudo respondido neste recorte. O tempo mediano desta unidade está em X h." |
| Avaliação sem texto | 80 a 83, 87 | "Só nota, sem texto"; sugestão curta de agradecimento; tema "Sem texto" |

No protótipo, os estados abrem por query (`?estado=` e `?perfil=recepcao`) e a avaliação pelo hash (`#r1` a `#r7`).

## Requisitos funcionais
- **FR-401** Coleta pela API do GBP (Business Profile APIs, recurso de reviews por location: listar, obter, responder, apagar resposta), a cada 4 h por padrão e sob demanda, com controle de cota.
- **FR-402** Vínculo do perfil por unidade: o dono do perfil (unidade) concede acesso à conta da rede como gerente; sem vínculo, a unidade aparece como "perfil não vinculado".
- **FR-403** Classificação de tema e sentimento por IA, com lista de temas mantida pela rede e correção manual pela unidade (alimenta a melhoria do modelo).
- **FR-404** Sugestão de resposta com as regras bloqueantes da US3 e validador final antes de publicar.
- **FR-405** Escalada automática (nota 1 ou 2, ou menção a saúde detectada pela IA) com aviso à rede e situação: unidade respondendo, rede acompanhando, rede assumiu, respondida.
- **FR-406** Permissões: franqueado só a própria unidade; rede, todas; perfis só de agregados não veem texto nem nome.
- **FR-407** Auditoria (só da rede, como US21 da 001): leitura de avaliação escalada, rascunho, publicação, edição de resposta, assunção pela rede e exportação, com autor, horário, texto antes e depois.
- **FR-408** Indicadores e exportação da US6; período padrão do controle de período (C09).
- **FR-409** Notificações: nova avaliação com nota baixa avisa a unidade na hora (e-mail e sino); resumo diário de pendentes; lembrete da rede.
- **FR-411** Fila ordenada por urgência (menção a saúde, notas 1 e 2, depois as demais sem resposta por data); filtros por situação, nota, tema e sentimento; última leitura com "Ler agora".
- **FR-412** Painel da rede acionável: KPIs com meta da SC-401 e SC-402 e variação frente ao período anterior; cada número, tema, região e unidade abre um recorte; escaladas e pendentes no primeiro ecrã.
- **FR-410** Avaliações nunca entram no schema da página (política do Google para avaliações próprias) e não são usadas em campanhas.

## Dados (resumo)
`avaliacao` (id do Google, unidade, nota, texto, nome exibido, data, atualizada_em, removida), `avaliacao_resposta` (texto, origem: IA, unidade ou rede, autor, publicada_em, status), `avaliacao_classificacao` (tema, sentimento, menciona_saude, confiança, corrigida_por), `avaliacao_escalada` (motivo, situação, responsável na rede). Retenção: espelho do Google enquanto o perfil estiver vinculado; texto removido no Google é apagado do espelho em até 24 h.

## Critérios de sucesso
- SC-401: 90% das avaliações respondidas em até 48 h na rede em 3 meses.
- SC-402: avaliações com nota 1 ou 2 respondidas em até 24 h em 95% dos casos.
- SC-403: zero respostas publicadas que confirmem atendimento ou citem dado de saúde (auditoria amostral mensal).

## Pendências e riscos
- **Acesso à API do GBP (bloqueante)**: a Salus precisa pedir acesso às Business Profile APIs ao Google (formulário de acesso, projeto no Google Cloud com as APIs habilitadas, aprovação pode levar semanas) e cada unidade precisa vincular o perfil à conta da rede. Sem isso, o painel funciona só com importação manual.
- Cota da API e contas de serviço: definir com o time técnico da Salus.
- Revisão jurídica das regras de resposta (LGPD e conselhos profissionais).
- Crítica de design aplicada em 21/11/2026 (rev. 2). Ainda em aberto: casco de celular próprio para a rede, tela para perfis só de agregados (R-FIN, R-AG), avaliação removida ou editada no Google (US1) desenhada, notificação de nota baixa no sino (FR-409).
