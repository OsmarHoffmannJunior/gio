# Feature Specification: Área do Cliente Gio (conta, ofertas, agenda, compras e relacionamento)

**Feature Branch**: `002-area-cliente`
**Created**: 2026-11-21
**Status**: Draft (rev. 1c, 21/11/2026: integração com a 003, objetivo quiz e funções quiz_unidade e tags_unidade; rev. 1b: controle da rede com padrão bloqueado, mural de avisos internos, campanhas completas com assistente, painel de performance e replicar campanha)
**Depende de**: `001-sistema-unidades` (unidades, catálogo, leads, RBAC, auditoria, LGPD centralizada, Wiki, módulos)
**Anexos**: `data-model.md`, `telas.md`, `decisoes.md`, `ideias.md`, `impacto-na-001.md`, `resumo.md`
**Input**: Pedido do Osmar (21/11/2026): área de login do cliente dentro do site da Gio, com onboarding leve (nome, cidade, idade, procedimentos de interesse, como conheceu a Gio, aceite de termos, validação de e-mail); mapear gostos; oferecer procedimentos em promoção na rede; admin da unidade envia promoções limitadas para a base da sua cidade, que aparecem na área do cliente; cliente agenda e acompanha compras (ex.: pacote de depilação a laser pago pelo sistema, com datas, horários e sessões feitas); admin da unidade cadastra procedimentos e promoções; dados prontos para um aplicativo futuro.

## Contexto
- Hoje o cliente não tem conta. O agendamento do site é um fluxo próprio em 2 etapas (AGDM): etapa 1 cria a intenção "ABERTO" (nome, e-mail, celular), etapa 2 escolhe data e hora e empurra para a DocBiz ("REALIZADO" com ID DocBiz). O consentimento vem marcado e há PII em cookie, dataLayer e URL (diagnóstico, achado 8).
- Agenda, prontuário e gestão financeira das clínicas ficam na DocBiz (braço de tecnologia da Salus). As unidades têm `id_docbiz` e `id_salesforce`.
- A regra de texto atual da Gio proíbe valores na comunicação pública ("avaliação gratuita" nos CTAs). Nenhuma ficha tem preço.
- A rede (franqueadora) é a controladora LGPD; as unidades são operadoras (decisão D15 da 001).
- Multimarca: a Sorridents terá a mesma área do cliente, com regras de conselho diferentes (CFO).

## Princípios da constituição afetados
I (multimarca: conta, catálogo e textos legais por marca), III (conversão confirmada no servidor: cadastro, agendamento e compra), IV (não competir com a DocBiz: agenda, prontuário e sessões continuam lá; a plataforma é a vitrine e o canal), V (unidade ativa e precifica dentro da política), VII (rede controladora, consentimento granular, central do titular), VIII (novos módulos e ações no RBAC), XIII (módulo liga e desliga por escopo). Princípios novos propostos em `impacto-na-001.md`: XIV (API única para site e app) e XV (dado de saúde fora da plataforma até decisão expressa).

## Papéis
| Papel | Escopo | Resumo |
|---|---|---|
| Visitante | Público | Navega, vê catálogo e promoções públicas, inicia cadastro ou agendamento |
| Cliente (titular) | A própria conta | Cadastro, perfil, interesses, consentimentos, agendamentos, compras, pacotes, avaliações, suporte e central de privacidade |
| Dependente (fase futura) | Conta de um responsável | Menor ou familiar gerido por um cliente titular (ver `ideias.md`) |
| Unidade (U-FRQ, U-GER, U-REC) | Própria unidade | Ofertas e preços conforme política, promoções e campanhas dentro da cota, base de clientes da unidade (mascarada por padrão), vendas, pacotes, NPS, chat |
| Rede (R-ADM, R-MKT, R-COM, R-CC, R-FIN, R-SEO) | Rede ou regional | Catálogo base, política de preço, modelos de promoção e campanha, limites, aprovação, textos legais, gateway e repasses, painel de clientes da rede, central do titular |
| Agência (R-AG) | Rede ou regional | Só agregados de campanha e funil; nunca dado pessoal |
| Sistemas | Integração | DocBiz (paciente, agenda, sessões, financeiro), Salesforce (CRM), gateway de pagamento, emissor de NFS-e, WhatsApp Business Platform, provedor de e-mail, push (FCM e APNs) |

## Jornadas principais
1. **Primeira visita até cliente.** Visitante vê uma promoção na ficha da unidade, clica em "quero", informa e-mail ou celular, recebe código (OTP) ou entra com Google ou Apple, aceita termos, escolhe unidade e interesse. Em menos de 60 segundos tem conta e vê a promoção salva.
2. **Agendar avaliação gratuita.** Cliente logado escolhe procedimento e unidade, vê horários reais da DocBiz, confirma, recebe confirmação e lembretes (24 h e 2 h), pode remarcar ou cancelar dentro da política.
3. **Comprar pacote.** Após a avaliação, a unidade oferece um pacote (ou o cliente compra uma oferta online). Paga com Pix ou cartão parcelado, recebe recibo e nota, o pacote aparece em "Meus pacotes" com sessões, validade e intervalo recomendado; a próxima sessão já pode ser agendada.
4. **Acompanhar tratamento.** Após cada sessão, o contador de sessões atualiza a partir da DocBiz, chegam cuidados pós e um pedido de avaliação rápida (NPS). Quando faltam 2 sessões, o sistema sugere renovação.
5. **Receber promoção da unidade.** A unidade monta uma campanha a partir de um modelo da rede, escolhe segmento (raio, interesse, faixa etária), vê o alcance e o consumo da cota, envia para aprovação ou publica (conforme política). O cliente vê na área "Ofertas para você" e, se consentiu no canal, recebe por e-mail, WhatsApp ou push.
6. **Exercer direitos de titular.** Cliente abre "Privacidade", vê o que foi consentido e quando, revoga marketing por canal, baixa seus dados ou pede exclusão. O pedido cai na fila única da rede (001, FR-033).

## User Scenarios & Testing

### US1. Cadastro progressivo sem atrito (P1)
Como visitante quero criar conta com o mínimo de dados e completar o resto depois, para não desistir no meio.
**Etapas**: (1) identificador: e-mail ou celular, ou Google/Apple; (2) verificação: código de 6 dígitos por e-mail ou WhatsApp, ou link mágico por e-mail; (3) nome, cidade (sugerida pela localização aproximada do IP, sem guardar o IP como localização), declaração de maioridade, aceite de termos e privacidade (desmarcados); (4) opcional e pulável: procedimentos de interesse (até 5 chips), unidade preferida, como conheceu a Gio, data de nascimento. O resto (CPF, endereço, gênero, celular adicional) só quando for necessário (compra, nota, agendamento).
**Acceptance**
1. Given visitante na tela de entrada, When informa e-mail válido, Then recebe código em até 30 s e a conta só fica ativa após o código (status "verificado").
2. Given checkbox de termos desmarcado, When tenta continuar, Then o botão fica desabilitado com explicação; nada vem pré-marcado.
3. Given cadastro concluído só com etapas 1 a 3, When entra na home do cliente, Then vê um cartão "complete seu perfil" com progresso e benefício claro (ex.: ofertas certas para você), sem bloquear o uso.
4. Given e-mail já cadastrado, When tenta criar conta, Then o sistema não revela a existência da conta: envia um código de acesso ao e-mail (prevenção de enumeração).
5. Given menor de 18 anos declarado, When tenta concluir, Then a conta não é criada e aparece a orientação de cadastro pelo responsável (decisão D6).
6. Given lead anterior (001) com o mesmo e-mail ou celular verificado, When a conta é criada, Then o lead é vinculado ao cliente, sem duplicar, e a jornada anterior aparece no histórico interno.

### US2. Entrar com segurança e sem senha (P1)
Como cliente quero entrar com código, link mágico, Google, Apple ou senha opcional e, no app, biometria ou passkey.
**Acceptance**
1. Given código enviado, When erro 5 vezes, Then bloqueio de 15 min e aviso por e-mail.
2. Given login social, When o e-mail do provedor coincide com conta existente verificada, Then vincula após confirmação por código.
3. Given sessão no site, When abro o app (futuro), Then entro com o mesmo cadastro (OIDC com PKCE).
4. Given troca de e-mail ou celular, When confirmo, Then exige código no contato antigo e no novo e registra auditoria.

### US3. Consentimentos granulares e central de privacidade (P1)
Como titular quero escolher o que aceito, por finalidade e canal, e mudar quando quiser.
**Consentimentos**: termos de uso (obrigatório), política de privacidade (ciência), marketing por canal (e-mail, WhatsApp, SMS, push, separados e desmarcados), personalização por interesses (opcional), compartilhamento com a unidade preferida para ofertas locais (opcional), uso de imagem em fotos de evolução (futuro, específico), dado de saúde (futuro, específico e destacado).
**Acceptance**
1. Given qualquer consentimento, When concedido ou revogado, Then grava versão do texto, data, hora, IP real, canal, user agent e origem (site, app, unidade).
2. Given revogação de marketing por WhatsApp, When uma campanha é disparada, Then o cliente é excluído do envio por WhatsApp em até 1 minuto e continua recebendo mensagens transacionais (confirmação de agendamento).
3. Given "Baixar meus dados", When peço, Then recebo arquivo JSON e PDF legível em até 15 dias (meta: na hora, com link que expira em 24 h).
4. Given "Excluir minha conta", When confirmo, Then o pedido entra na fila do titular da rede; dados com obrigação legal de guarda (nota fiscal, pagamentos, prontuário na DocBiz) ficam retidos e o resto é anonimizado, com explicação ao titular.
5. Given texto legal novo, When publicado pela rede, Then clientes veem aviso no próximo acesso; mudança material pede novo aceite.

### US4. Perfil de interesses e preferências (P1)
Como cliente quero dizer o que me interessa para ver ofertas que fazem sentido.
**Acceptance**
1. Given interesses marcados, When abro "Ofertas para você", Then a ordem prioriza esses procedimentos e a unidade preferida.
2. Given interesse inferido (navegação, compras), When exibido, Then aparece como "sugerido" e só entra na segmentação se o consentimento de personalização estiver ativo.
3. Given preferências de contato (canal, faixa de horário, frequência máxima), When uma campanha é enviada, Then o envio respeita o mais restritivo entre preferência do cliente e regra da rede.

### US5. Unidade preferida e multiunidade (P1)
**Acceptance**
1. Given cidade informada, When escolho unidade, Then vejo as mais próximas com distância, horário e nota no Google.
2. Given cliente com atendimentos em 2 unidades, When abro a área, Then vejo tudo junto, com a unidade em cada item; a unidade preferida define as ofertas locais.
3. Given troca de unidade preferida, When confirmo, Then a unidade antiga deixa de vê-lo na base de marketing (continua vendo histórico de atendimento próprio).

### US6. Catálogo de procedimentos (P1)
Como cliente quero ver procedimentos, para que servem, indicação, número típico de sessões e cuidados; como rede quero definir a base; como unidade quero ativar o que ofereço e definir preço quando a política permitir.
**Acceptance**
1. Given catálogo base da rede (nome, categoria, descrição aprovada, contraindicações gerais, sessões típicas, intervalo, cuidados pré e pós, URL nacional), When a unidade ativa um item, Then ele aparece na ficha e na área do cliente daquela unidade.
2. Given política de preço "só logado" (decisão D1), When visitante vê o procedimento, Then aparece "entre para ver condições"; logado vê preço da unidade preferida.
3. Given unidade tenta preço fora da faixa da rede (piso e teto, se a rede definir), When salva, Then o validador bloqueia ou envia para aprovação conforme política.
4. Given texto da unidade com promessa de resultado ou marca de equipamento, When publica, Then o validador da marca (001, FR-023) bloqueia.

### US7. Promoções da rede e da unidade (P1)
**Acceptance**
1. Given modelo de promoção da rede (tipo: avaliação gratuita, sessão bônus, percentual, pacote com condição, brinde), When a unidade cria uma promoção, Then só preenche os campos do modelo, com validade obrigatória e regulamento gerado.
2. Given promoção com preço (se D1 permitir), When publicada, Then mostra preço "de" e "por" com regras do CDC (preço à vista, condições, validade, estoque ou limite) e o texto legal do modelo.
3. Given promoção da rede, When a unidade não quer participar, Then pode sair se a rede marcou "adesão opcional".
4. Given fim da validade, Then a promoção sai do ar sozinha e pedidos em andamento são honrados.

### US8. Campanhas segmentadas com cota e aprovação (P1)
Como admin da unidade quero enviar promoções para clientes da minha região, de forma limitada; como rede quero proteger a base de excesso e conflitos entre unidades. Só vale para unidades que a rede liberou (US17); o fluxo completo de criação está em US19.
**Segmentação**: raio em km a partir da unidade ou cidade, interesse, faixa etária, unidade preferida, comportamento (sem visita há 90 dias, pacote acabando, aniversariante do mês), excluindo quem não consentiu no canal.
**Acceptance**
1. Given segmento montado, When abro a prévia, Then vejo alcance por canal (com e sem consentimento), custo estimado do WhatsApp, cota restante do mês e conflitos (clientes com outra unidade preferida ficam fora por padrão).
2. Given cota mensal da unidade esgotada (ex.: 2 campanhas por mês, decisão D5), When tento enviar, Then o envio é bloqueado com a data da próxima cota.
3. Given limite por cliente (ex.: no máximo 1 mensagem de marketing por semana somando rede e unidades), When várias campanhas competem, Then o motor de frequência escolhe pela prioridade da rede e adia ou descarta o resto, registrando o motivo.
4. Given política "campanha de unidade com aprovação", When envio, Then entra na fila de R-MKT com prévia; aprovação responde em até 1 dia útil; quem cria não aprova.
5. Given campanha enviada, When abro resultados, Then vejo entregues, abertos, cliques, cadastros, agendamentos, comparecimentos e vendas atribuídos, sem PII para agência.
6. Given unidade, When monto o segmento, Then nunca vejo a lista nominal antes do envio; vejo só contagens (o envio é feito pela plataforma em nome da marca e da unidade).

### US9. Agendamento integrado à DocBiz (P1)
**Acceptance**
1. Given procedimento e unidade, When abro horários, Then vejo disponibilidade real da DocBiz para o tipo de atendimento (avaliação ou sessão) e profissional/sala quando aplicável.
2. Given confirmação, When a DocBiz aceita, Then o agendamento existe com ID DocBiz, o evento `agendamento_concluido` é emitido no servidor (princípio III) e o cliente recebe confirmação com rota e "adicionar à agenda".
3. Given DocBiz indisponível, When confirmo, Then o pedido entra como "solicitado" na fila da unidade com SLA, o cliente é avisado de que a confirmação chega em até X horas e nada aparece como confirmado sem a DocBiz.
4. Given política de remarcação da unidade (ex.: até 24 h antes, máximo 2 vezes), When remarco ou cancelo, Then a DocBiz é atualizada e o horário é liberado.
5. Given ausência sem aviso (no-show), When a DocBiz marca, Then a política da rede é aplicada (aviso, depois exigência de sinal ou de confirmação ativa) e a sessão do pacote é tratada conforme regulamento.
6. Given lembretes, Then saem 24 h e 2 h antes (canal transacional), com botões confirmar, remarcar e cancelar.

### US10. Compras, pacotes e sessões (P1)
**Acceptance**
1. Given oferta comprável, When pago com Pix, cartão à vista ou parcelado, Then o pedido só vira "pago" no webhook do gateway (princípio III) e o pacote é criado na DocBiz.
2. Given pacote pago, When abro "Meus pacotes", Then vejo procedimento, área, sessões contratadas, feitas, agendadas e restantes, validade, intervalo recomendado e próxima data sugerida.
3. Given sessão realizada na unidade, When a DocBiz registra, Then o contador atualiza em até 15 min e o histórico mostra data, unidade e profissional.
4. Given compra online, When o cliente pede arrependimento em até 7 dias sem sessão feita, Then o estorno integral é processado (CDC, art. 49); com sessão feita, segue o regulamento (decisão D2b).
5. Given pagamento, Then recibo fica disponível na hora e a NFS-e da unidade emissora em até 48 h, ambos baixáveis.
6. Given compra presencial na unidade (DocBiz), When o cliente tem conta, Then o pacote aparece na área (somente leitura) após vínculo do paciente DocBiz ao cliente.

### US11. Histórico de atendimentos (P2)
**Acceptance**
1. Given atendimentos na DocBiz, When abro histórico, Then vejo data, unidade, procedimento, profissional e status; nada de conteúdo de prontuário (princípio XV proposto).

### US12. Avaliação pós-sessão (NPS) e avaliação no Google (P1)
**Acceptance**
1. Given sessão concluída, When passam 2 h, Then o cliente recebe pedido de nota 0 a 10 e comentário opcional.
2. Given qualquer nota, Then o convite para avaliar no Google é mostrado a todos (sem filtro por nota, sem recompensa), conforme política do Google contra seleção de avaliações e incentivos.
3. Given nota 0 a 6, Then abre um caso de recuperação para a unidade com SLA e visibilidade da rede.
4. Given NPS, Then alimenta o dashboard da unidade e da rede (001, US5) e o ranking, com mesma régua (princípio X).

### US13. Notificações multicanal (P1)
**Acceptance**
1. Given tipo de mensagem (transacional, relacionamento, marketing), Then cada uma respeita base legal e consentimento; transacional não depende de opt-in de marketing, mas o WhatsApp exige opt-in do canal pelas regras da Meta.
2. Given central de notificações na área do cliente, Then todas as mensagens enviadas aparecem lá, mesmo as que não chegaram por canal externo.
3. Given app instalado (futuro), Then push substitui WhatsApp quando o cliente preferir, reduzindo custo.

### US14. Suporte e chat (P2)
**Acceptance**
1. Given dúvida, When abro "Ajuda", Then vejo artigos públicos da Wiki (001, US14) e posso abrir conversa com a unidade ou com a rede (pagamento, privacidade).
2. Given conversa aberta, Then vira chamado (001, FR-011) com SLA, e o cliente acompanha o status.
3. Given conversa por WhatsApp, Then é registrada no mesmo chamado (fase 2).

### US15. Gestão da base, segmentos, campanhas e resultados pela unidade e pela rede (P1)
**Acceptance**
1. Given perfil de unidade, When abro "Clientes", Then vejo só clientes com vínculo com a unidade (preferida, agendamento, compra ou atendimento), com PII mascarada por padrão (001, princípio VII) e ação "ver dado" auditada.
2. Given rede, When abro o painel de clientes, Then vejo base total, crescimento, completude de perfil, consentimento por canal, interesses mais comuns por UF e cidade, e funil cadastro > agendamento > comparecimento > compra.
3. Given unidade, When abro resultados, Then vejo vendas online, pacotes ativos, sessões a vencer, no-show, NPS e campanhas, e o comparativo com a mediana da rede.
4. Given exportação de clientes com PII, Then segue a regra da 001 (D + X, 2FA, motivo, link de 24 h), liberada só pela rede.

### US16. Cadastro de procedimentos, ofertas e preços pela unidade (P1)
**Acceptance**
1. Given catálogo base, When a unidade ativa um procedimento, Then define disponibilidade, duração local, preço (se permitido), pacotes locais a partir de modelos da rede (ex.: 6, 8 ou 10 sessões) e se é comprável online.
2. Given procedimento fora do catálogo, When a unidade quer oferecer, Then pede inclusão à rede por chamado (não cria item livre).

### US17. Controle total da rede sobre o que cada unidade pode fazer (P1)
Como rede quero liberar ou bloquear, por unidade, regional ou rede inteira, as funções de preço, cadastro de procedimentos e pacotes, promoções, campanhas para clientes e avisos, e definir antes os limites de envio, para que nenhuma unidade consiga falar com a base toda nem sair das regras.
**Regras**: tudo nasce **bloqueado** para perfis de unidade. A rede liga por permissão de função (o que pode) e por **limite** (quanto e para quem). Herança rede > regional > unidade, com exceção por unidade (001, FR-029). Alcance máximo que a rede pode conceder a uma unidade: apenas clientes da própria unidade, raio em km, cidades listadas ou UF listada; "base nacional" não existe como opção para unidade (teto no banco).
**Acceptance**
1. Given unidade recém-provisionada, When o admin da unidade abre Clientes, Campanhas, Preços ou Procedimentos, Then vê as funções bloqueadas com cadeado, o motivo "não liberado pela rede" e o atalho "pedir liberação" (chamado).
2. Given R-ADM ou R-MKT na tela "Controles da rede", When libera "Campanhas para clientes" para a regional Sul com cota de 2 campanhas por mês, alcance "clientes da própria unidade + raio de 5 km" e canais "área do cliente e e-mail", Then todas as unidades da regional herdam, a mudança entra na auditoria com motivo e as unidades recebem aviso no mural.
3. Given exceção para uma unidade (ex.: cota 0 por inadimplência ou cota 4 por piloto), When salvo, Then a unidade passa a usar a exceção e a tela mostra "exceção local" ao lado do valor herdado.
4. Given um perfil de unidade tenta montar segmento fora do alcance concedido (outra cidade, raio maior, UF), When salva, Then a API recusa (teto aplicado no servidor e no banco, não só na tela).
5. Given qualquer configuração, When nenhuma regra foi definida, Then vale "bloqueado".
6. Given a rede bloqueia uma função já em uso, When confirma, Then o sistema mostra o impacto (campanhas agendadas, promoções no ar, preços publicados) e pede escolha: manter até o fim, pausar ou despublicar; o franqueado é avisado.

### US18. Mural de avisos internos da rede para as unidades (P1)
Como rede quero publicar avisos para os franqueados e equipes (novidades do sistema, promoções da rede, comunicados, treinamentos, prazos), segmentados por unidade, regional e perfil, com leitura confirmada, fixação e prazo.
**Acceptance**
1. Given novo aviso, When escolho público (todas, regionais, unidades, filtros como UF ou módulo ligado, e perfis U-FRQ, U-GER, U-REC), categoria, prioridade, anexos ou link para a Wiki, início e fim, Then vejo a contagem de pessoas e unidades alcançadas antes de publicar.
2. Given aviso com "exige confirmação de leitura" e prazo, When a pessoa abre, Then precisa clicar "li e entendi"; quem não confirmou até o prazo recebe lembrete e aparece no relatório de pendências por unidade.
3. Given aviso fixado, Then fica no topo do mural e no painel inicial da unidade até o fim ou até desafixar.
4. Given aviso urgente, Then dispara sino e e-mail (e WhatsApp interno, se configurado) além do mural.
5. Given aviso publicado, When abro o relatório, Then vejo entregue, aberto, confirmado e pendente por unidade, regional e perfil, e posso reenviar só para pendentes.
6. Given promoção nacional da rede, When publicada, Then pode gerar automaticamente um aviso no mural com o kit (artes, regulamento, datas) e o botão "aderir" quando a adesão for opcional.
7. Given gestor regional com permissão, Then publica avisos só para as unidades da sua regional (se a rede liberar).

### US19. Campanhas para clientes com assistente e modelos (P1)
Como rede (e unidade, se liberada) quero criar campanhas para clientes por um assistente passo a passo, a partir de modelos, com segmento, vínculo a procedimentos e produtos, período, CTA, alcance, canais, prévia de alcance e aprovação da rede para campanhas de unidade.
**Passos do assistente**:
1. **Objetivo e modelo**: escolher objetivo (agendar avaliação, vender pacote, reativar cliente inativo, aniversário, lançamento, renovação de pacote, conhecer interesses com quiz da spec 003) e um modelo da biblioteca (texto, arte, CTA e regras prontos; campos livres só onde o modelo permite).
2. **Oferta**: vincular procedimentos, pacotes ou produtos do catálogo e, se houver, a promoção (US7), com regulamento automático.
3. **Público**: interesses, faixa etária, cidade, histórico (comprou, fez sessão, inativo há N dias, pacote acabando, NPS), unidade preferida ou clientes de unidades específicas; consentimento por canal aplicado sozinho.
4. **Alcance geográfico**: UF, cidades, raio ou "clientes destas unidades"; para unidade, só dentro do teto concedido (US17).
5. **Canais e conteúdo**: área do cliente (cartão em "Ofertas para você"), e-mail, WhatsApp (template aprovado pela Meta), push (app); prévia por canal em desktop e celular; link e CTA com UTM automático.
6. **Período e envio**: início e fim da campanha, data e hora de disparo ou disparo recorrente (ex.: aniversariantes), janela de silêncio.
7. **Prévia de alcance e custo**: total elegível, por canal, excluídos por consentimento, por frequência e por conflito com outra unidade; custo estimado de WhatsApp; consumo da cota.
8. **Revisão e envio**: validador de publicidade (FR-120), checklist, envio para aprovação (unidade) ou publicação (rede, com motivo se afetar unidades).
**Acceptance**
1. Given campanha de unidade, When envio, Then vai para a fila de aprovação da rede (R-MKT) com a prévia completa; publicação direta só se a rede tiver liberado "sem aprovação" para aquele modelo.
2. Given campanha da rede para clientes de unidades específicas, When publicada, Then as unidades afetadas recebem aviso no mural com datas e oferta.
3. Given rascunho, When salvo em qualquer passo, Then posso voltar depois; o assistente mostra o progresso e bloqueia avanço com erro claro.
4. Given campanha no ar, When pauso ou encerro, Then os disparos futuros param na hora e o cartão some da área do cliente no fim.
5. Given modelo novo criado pela rede, Then fica disponível só para os escopos e perfis escolhidos.

### US20. Painel de performance e replicar campanha (P1)
Como rede quero ver o que cada unidade está fazendo em campanhas, avisos e promoções, com estatísticas e comparativos, descobrir o que funciona e replicar para outras unidades.
**Acceptance**
1. Given painel, When filtro por período, regional, UF, unidade, canal, objetivo, modelo e procedimento, Then vejo entregas, aberturas, cliques, cadastros, agendamentos, comparecimentos e vendas atribuídas (valor e quantidade), custo e retorno estimado, com fonte e período (princípio X).
2. Given atividade das unidades, Then vejo por unidade: campanhas criadas, enviadas, reprovadas, cota usada, promoções no ar, avisos confirmados e pendentes, e unidades sem nenhuma ação no período.
3. Given comparativo, When seleciono 2 a 5 campanhas ou unidades, Then vejo as métricas lado a lado com a mediana da rede e o funil de cada uma.
4. Given cruzamento, When escolho dimensões (modelo x canal x faixa etária x procedimento x porte da cidade x dia da semana), Then vejo uma tabela dinâmica com taxa de conversão e destaques automáticos ("WhatsApp converte 2,1x mais que e-mail para depilação em cidades do interior"), com amostra mínima antes de sugerir.
5. Given campanha que performou bem, When clico "replicar", Then escolho unidades ou regionais de destino, o sistema ajusta alcance ao teto de cada uma, mostra a prévia por unidade e cria rascunhos ou publica (rede) ou propõe às unidades via mural com "usar esta campanha".
6. Given unidade, Then vê o próprio desempenho e a posição frente à mediana da rede, sem dados nominais de outras unidades.

## Requisitos funcionais
Numeração a partir de FR-101 para não colidir com a 001.

**Identidade e conta**
- FR-101 Pool de identidade de clientes separado dos usuários internos (001), por marca; e-mail e celular únicos por marca.
- FR-102 Métodos de entrada: OTP por e-mail, OTP por WhatsApp (template de autenticação), link mágico, Google, Apple, senha opcional; no app, passkey e biometria. Rate limit, bloqueio progressivo, detecção de bot sem captcha visível quando possível.
- FR-103 Cadastro progressivo com etapas puláveis e completude de perfil; dado só pedido quando a função exige (minimização).
- FR-104 Declaração de maioridade obrigatória; data de nascimento opcional no início e obrigatória para comprar (D6).
- FR-105 Deduplicação com leads da 001 e pacientes DocBiz por e-mail ou celular verificados; vínculo `cliente_vinculo_docbiz` por unidade.
- FR-106 Sessões com refresh token rotativo; encerramento remoto de sessões; aviso de novo dispositivo.

**Consentimento e privacidade**
- FR-107 Consentimento granular por finalidade e canal, desmarcado, versionado (texto, data, IP real, canal, origem), com histórico imutável.
- FR-108 Central de privacidade: ver e revogar consentimentos, baixar dados, corrigir, pedir exclusão e portabilidade; pedidos vão para a fila do titular da rede (001, FR-033).
- FR-109 Textos legais por marca e versão; mudança material exige novo aceite.
- FR-110 Sem PII em URL, cookie de marketing ou dataLayer; eventos com `cliente_hash` só no servidor; conversões aprimoradas com hash no servidor quando houver consentimento.

**Interesses e preferências**
- FR-111 Interesses declarados e inferidos separados; inferidos só com consentimento de personalização.
- FR-112 Preferências de contato: canais, faixa horária, frequência máxima, idioma futuro.

**Catálogo, ofertas e preço**
- FR-113 Catálogo base por marca (001, `tratamento` ampliado): descrição aprovada, sessões típicas, intervalo, duração, cuidados pré e pós, contraindicações gerais, faixa etária mínima, imagens.
- FR-114 Oferta por unidade: ativar, duração local, preço e pacotes conforme política de preço da rede (piso, teto, visibilidade: oculto, só logado, só em promoção, público) (D1).
- FR-115 Modelos de pacote da rede (quantidade de sessões, validade, intervalo, regras de transferência e cancelamento).

**Promoções e campanhas**
- FR-116 Promoções por modelo (001, FR-024 ampliado) com tipos, validade, limite de uso, regulamento gerado, adesão opcional ou obrigatória às promoções da rede.
- FR-117 Segmentos dinâmicos por raio, cidade, interesse, faixa etária, unidade preferida, comportamento e consentimento; prévia só com contagens.
- FR-118 Campanhas com canal, agenda, cota por unidade e período, limite de frequência por cliente global, prioridade rede > unidade, janela de silêncio (ex.: 21 h a 9 h), aprovação conforme política, teste A/B de assunto (fase 2).
- FR-119 Opt-out em 1 clique em todo envio de marketing, com efeito imediato.
- FR-120 Validador de publicidade em saúde e estética por marca: sem promessa de resultado, sem antes e depois em campanha, sem marca de equipamento, sem termos proibidos por conselho; regras diferentes para Sorridents (CFO).
- FR-121 Atribuição de resultados: entrega, abertura, clique, cadastro, agendamento, comparecimento, venda, por campanha, unidade e canal.

**Agendamento**
- FR-122 Disponibilidade e reserva pela API da DocBiz; reserva temporária de horário por 5 min durante a confirmação.
- FR-123 Fallback "solicitação de horário" com SLA na fila da unidade quando a DocBiz não responder ou não expuser API (D3).
- FR-124 Remarcar e cancelar conforme política por unidade dentro de limites da rede; lembretes 24 h e 2 h; confirmação ativa.
- FR-125 Política de no-show configurável (aviso, sinal, bloqueio de agendamento online por período), sempre informada antes do agendamento.
- FR-126 Lista de espera por procedimento e unidade com aviso de vaga (fase 2, ver `ideias.md`).

**Pagamentos, pedidos e pacotes**
- FR-127 Checkout com Pix, cartão à vista e parcelado, e carteira digital; tokenização no gateway (PCI fora da plataforma).
- FR-128 Recebimento conforme D2 (recomendado: split no gateway, valor da venda para a subconta da unidade e taxa da rede, se houver, para a conta da rede).
- FR-129 Pedido com itens, unidade vendedora, status (aguardando, pago, cancelado, estornado, parcialmente usado), regulamento aceito e versão.
- FR-130 Pacote com sessões contratadas, consumidas, agendadas e restantes; validade; sincronizado com a DocBiz (fonte da verdade do consumo).
- FR-131 Arrependimento em 7 dias para compra online (CDC, art. 49) e regras de cancelamento proporcional após uso; estorno pelo gateway.
- FR-132 Recibo imediato e NFS-e emitida pela unidade vendedora (pela DocBiz ou emissor integrado, D2c); identificação do fornecedor (razão social e CNPJ da unidade) no checkout (Decreto 7.962/2013).
- FR-133 Conciliação e repasses: relatório por unidade de vendas, taxas, estornos e chargebacks.

**Relacionamento**
- FR-134 NPS pós-sessão com caso de recuperação para notas baixas; convite ao Google para todos, sem incentivo.
- FR-135 Central de notificações do cliente; motor de templates por marca com variáveis; canais e-mail, WhatsApp, SMS (opcional), push.
- FR-136 Chat e chamados do cliente integrados ao suporte da 001.

**Painéis**
- FR-137 Painel da unidade: clientes (vínculo), segmentos, campanhas, cota, ofertas, promoções, vendas, pacotes, sessões a vencer, no-show, NPS.
- FR-138 Painel da rede: base, consentimentos, interesses, funil, campanhas da rede e das unidades, aprovações, financeiro, ranking, alertas (inclui insights da 001, FR-028).
- FR-139 RBAC: novos módulos (clientes, ofertas e preços, campanhas, vendas e pacotes, NPS, financeiro do cliente) com ações V, E, A, P, X, D da 001.

**Controle da rede (US17)**
- FR-142 Matriz de liberação por função x escopo (rede, regional, unidade) com herança e exceção: preços, cadastro de procedimentos e pacotes locais, promoções, campanhas para clientes, canais permitidos (área do cliente, e-mail, WhatsApp, push), avisos regionais, ver base de clientes, exportar, quiz da unidade e tags da unidade (spec 003). Padrão bloqueado para tudo.
- FR-143 Limites por escopo: cota de campanhas e de mensagens por período, orçamento de WhatsApp, frequência máxima por cliente, janela de horário, alcance máximo (apenas clientes da própria unidade, raio em km, cidades ou UF listadas); "base nacional" proibida para perfis de unidade por teto no banco.
- FR-144 Impacto ao bloquear (campanhas, promoções, preços em uso) com escolha manter, pausar ou despublicar; auditoria e aviso ao franqueado.
- FR-145 Pedido de liberação pela unidade via chamado, com histórico.

**Mural de avisos internos (US18)**
- FR-146 Avisos com categoria, prioridade, corpo rico, anexos, link para Wiki, público por unidade, regional, filtros e perfil, início e fim, fixar, exigir confirmação de leitura com prazo.
- FR-147 Entrega no mural, sino, e-mail e, opcionalmente, WhatsApp interno; lembrete automático a pendentes; relatório de leitura por unidade e perfil; reenviar a pendentes.
- FR-148 Aviso automático gerado por promoção nacional e por campanha da rede que afete unidades, com botão "aderir" quando a adesão for opcional.

**Campanhas com assistente (US19)**
- FR-149 Assistente em 8 passos com rascunho salvo, validação por passo e progresso.
- FR-150 Biblioteca de modelos de campanha por objetivo, com campos travados e livres, canais, arte, CTA, regras e escopos de uso; versão.
- FR-151 Vínculo da campanha a procedimentos, pacotes, produtos e promoções do catálogo; UTM e link curto automáticos.
- FR-152 Prévia de alcance e custo antes de enviar: elegíveis por canal e exclusões por consentimento, frequência, conflito e teto.
- FR-153 Disparo único, agendado ou recorrente (gatilhos: aniversário, inatividade, pacote acabando, pós-sessão); pausar e encerrar a qualquer momento.
- FR-154 Aprovação da rede para campanha de unidade, com diff e prévia; liberação "sem aprovação" por modelo.

**Performance (US20)**
- FR-155 Painel de performance de campanhas, promoções e avisos por unidade, regional, canal, modelo, objetivo e procedimento, com funil até venda atribuída e custo.
- FR-156 Atividade das unidades: criadas, enviadas, reprovadas, cota usada, promoções no ar, avisos pendentes, unidades inativas no período.
- FR-157 Comparativo lado a lado (2 a 5 campanhas ou unidades) com mediana da rede.
- FR-158 Cruzamento por dimensões (tabela dinâmica) com destaques automáticos que exigem amostra mínima e mostram a regra usada.
- FR-159 Replicar campanha para unidades ou regionais, ajustando ao teto de cada uma, com prévia por unidade, criação de rascunhos, publicação pela rede ou proposta às unidades pelo mural.
- FR-160 Modelo de atribuição documentado (padrão: último clique da campanha em até 7 dias para agendamento e 30 dias para venda), igual para todas as unidades.

**Plataforma**
- FR-140 API única versionada (REST com OpenAPI), autenticação OIDC (site e app), webhooks de saída; o site e o app futuro consomem a mesma API.
- FR-141 Módulo "Área do cliente" e submódulos (pagamento online, campanhas de unidade, chat) ligáveis por rede, regional e unidade (001, FR-029).

## Requisitos não funcionais
- Área do cliente com LCP mobile abaixo de 2,5 s e Lighthouse mobile de pelo menos 90 nas páginas públicas.
- Acessibilidade WCAG 2.2 AA.
- Disponibilidade da API de 99,5% no mês; fila com reprocessamento para DocBiz, gateway e mensageria.
- Criptografia em trânsito e em repouso; CPF e data de nascimento cifrados por campo.
- Logs de acesso a dado pessoal na auditoria da 001.

## Success Criteria
- SC-101 Pelo menos 70% de conclusão do cadastro entre quem inicia (meta inicial, medir na primeira versão).
- SC-102 Cadastro mínimo concluído em até 60 s na mediana.
- SC-103 100% dos agendamentos online com ID DocBiz ou em fila de solicitação com SLA; zero agendamento "confirmado" sem a DocBiz.
- SC-104 100% dos pedidos "pagos" confirmados por webhook do gateway.
- SC-105 Contador de sessões divergente da DocBiz em menos de 0,5% dos pacotes (auditoria semanal).
- SC-106 Nenhum envio de marketing para quem não consentiu no canal (teste automatizado em toda campanha).
- SC-107 Taxa de opt-out por campanha abaixo de 1% (sinal de segmentação boa e de limite de frequência).
- SC-108 Pedidos do titular atendidos em até 15 dias (meta interna de 5).
- SC-109 Taxa de resposta do NPS de pelo menos 25%.
- SC-111 Zero envio de unidade fora do alcance concedido pela rede (teste automatizado e trava no banco).
- SC-112 Avisos com confirmação obrigatória lidos por pelo menos 90% dos destinatários até o prazo.
- SC-113 Unidade cria uma campanha por modelo, do zero ao envio para aprovação, em até 5 minutos na mediana.
- SC-110 Queda de no-show em relação à linha de base de cada unidade após lembretes e confirmação ativa.

## Casos de borda
- Cliente com o mesmo celular em duas contas (casal ou família): o celular é único; sugerir perfis familiares (futuro).
- Cliente compra em uma unidade e quer fazer sessão em outra: só com transferência aprovada pelas duas unidades e regra financeira da rede (ver `ideias.md`).
- Unidade fecha com pacotes ativos: a rede define a unidade que assume, aviso ao cliente e opção de estorno proporcional.
- Preço mudou depois da compra: pedido mantém preço e regulamento da versão aceita.
- Promoção esgota durante o checkout: reserva de vaga por 10 min.
- DocBiz marca sessão que o cliente diz não ter feito: contestação por chamado, com evidência da DocBiz.
- E-mail do cliente vira inválido (bounce): canal marcado como inválido e pedido de atualização no próximo acesso.
- Cliente revoga tudo: continua com conta e transacionais; some de segmentos.

## Fora de escopo agora
- Prontuário, anamnese clínica e fotos clínicas (ficam na DocBiz ou em spec própria após decisão D7).
- Aplicativo nativo (a API e o modelo já nascem prontos para ele).
- Marketplace entre marcas (Gio e Sorridents) e conta Salus única (D9).
- Programa de fidelidade, cashback, indicação e vale-presente (priorizados em `ideias.md`).
- Telemedicina e teleconsulta.
- Redesenho do site institucional.
- Desenho de telas (fica para depois da validação desta spec).
