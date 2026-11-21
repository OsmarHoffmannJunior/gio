# Resumo: Área do Cliente Gio (spec 002)

21/11/2026. Uma página para o Osmar. Detalhes em `spec.md`, `decisoes.md`, `ideias.md`, `data-model.md`, `telas.md` e `impacto-na-001.md`.

## O que é
Uma área de login do cliente dentro do site da Gio, ligada ao painel da rede e das unidades (spec 001), e feita sobre uma API única que o aplicativo futuro vai usar sem retrabalho. A rede segue como controladora dos dados; a DocBiz segue dona da agenda, do prontuário e do consumo de sessões.

## Módulos
1. **Conta sem atrito:** e-mail ou celular com código, link mágico, Google ou Apple; cadastro mínimo (nome, cidade, 18+, termos) e o resto depois (interesses, unidade preferida, como conheceu, nascimento).
2. **Privacidade:** consentimentos separados por finalidade e canal, sempre desmarcados e versionados; central do titular (revogar, baixar, corrigir, excluir).
3. **Interesses e unidade preferida:** base para ofertas certas e para a regra de quem a unidade pode alcançar.
4. **Catálogo e preço:** rede define o procedimento; unidade ativa e precifica só se liberada; preço só para logado e em promoções (proposta).
5. **Promoções e campanhas:** assistente em 8 passos com modelos, segmentação, prévia de alcance e custo, canais (área do cliente, e-mail, WhatsApp, push), aprovação da rede.
6. **Controles da rede:** tudo nasce bloqueado; a rede libera por rede, regional ou unidade e define cotas, frequência por cliente e alcance máximo (própria unidade, raio, cidade, UF). Unidade nunca alcança a base toda.
7. **Mural de avisos internos:** comunicados da rede para franqueados e equipes, segmentados, com fixar, prazo e confirmação de leitura.
8. **Agendamento:** horários reais da DocBiz, remarcar, cancelar, lembretes, política de falta.
9. **Compras e pacotes:** Pix e cartão parcelado, sessões feitas e restantes, validade, recibo e nota da unidade, arrependimento de 7 dias.
10. **Relacionamento:** NPS pós-sessão, convite ao Google para todos (sem incentivo), notificações, chat e suporte.
11. **Performance:** o que cada unidade faz, funil até venda atribuída, comparativos, cruzamentos e botão de replicar campanha.

## 10 melhores ideias extras
Lembrete inteligente da próxima sessão; confirmação ativa com encaixe de vagas; avaliação gratuita online com pré-triagem leve; quiz de recomendação; indicação com recompensa; renovação e upgrade de pacote; cuidados pré e pós automáticos; carteira de créditos e cashback; vale-presente digital; anamnese e termo do procedimento assinados online (fase 3, dado de saúde).

## Decisões para o Osmar
1. **Preço (D1):** sem preço público, preço para logado e em promoções? (Sorridents provavelmente sem preço, por regra do CFO.)
2. **Quem recebe (D2):** split no gateway, com o dinheiro direto para a unidade? Taxa da rede? Nota pela unidade?
3. **DocBiz (D3):** enviar as 7 perguntas sobre API de agenda, paciente, pacotes e nota.
4. **Campanhas de unidade (D4, D5):** cota inicial (2 por mês?), frequência por cliente (1 por semana?), alcance padrão "clientes da própria unidade", quando liberar sem aprovação.
5. **Idade mínima (D6):** só 18+ e data de nascimento em vez de idade.
6. **Dado de saúde (D7):** fora da plataforma na fase 1.
7. **Conta por marca (D9)** e **endereço** da área (D15).
8. **Escopo do MVP (D16).**

## Caminho sugerido
Fase 1: conta, privacidade, controles da rede, mural, catálogo, promoções, campanhas da rede, agendamento, NPS e performance básica. Fase 2: pagamento com split, pacotes e sessões, campanhas de unidade com WhatsApp, comparativos e replicar. Fase 3: app com push, fidelidade, indicação, vale-presente, perfis familiares e anamnese digital.
