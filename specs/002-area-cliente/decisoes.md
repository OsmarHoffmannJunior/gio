# Decisões em aberto: Área do Cliente (002)

Rev. 1b, 21/11/2026 (requisitos do Osmar das 09h15: controle da rede com padrão bloqueado, mural de avisos, campanhas com assistente, performance e replicar). Numeração própria (D1 a D16 desta spec; as decisões da 001 continuam D1 a D15 da 001). Recomendações são propostas para o Osmar validar com a Gio, a Salus, a DocBiz e o jurídico. Nada aqui é parecer jurídico.

## Resumo
| # | Decisão | Recomendação | Quem decide |
|---|---|---|---|
| D1 | Preço no site | Sem preço público; preço só para cliente logado e dentro de promoções com regulamento | Osmar + Gio (marketing) + jurídico |
| D2 | Quem recebe o dinheiro | Split no gateway: unidade recebe direto na subconta; rede recebe a taxa dela, se houver | Gio + Salus (financeiro) + jurídico/contábil |
| D3 | Integração com a DocBiz | API em tempo real para agenda, paciente e sessões; fallback de solicitação com SLA | DocBiz + Osmar |
| D4 | Quem envia campanha | Resolvido em parte pelo Osmar: rede controla tudo, padrão bloqueado; unidade só envia se liberada, por modelo, com aprovação da rede. Em aberto: quando liberar "sem aprovação" | Osmar + Gio (marketing) |
| D5 | Limites e cotas | 1 marketing por semana por cliente (global), 2 campanhas por mês por unidade, janela 9 h a 21 h | Gio (marketing) |
| D6 | Idade mínima | Conta só para maiores de 18; menores depois como dependentes | Osmar + jurídico |
| D7 | Dados de saúde | Não coletar na plataforma agora; anamnese digital só em fase futura com RIPD | Osmar + jurídico + DocBiz |
| D8-D16 | Demais | Ver detalhes | Variado |

## D1. Preço: mostrar ou não
Contexto: a regra atual da Gio proíbe valores na comunicação pública. O pedido do Osmar envolve promoções e compra pelo sistema, que exigem preço em algum momento (o CDC e a lei de precificação pedem preço claro quando há oferta de venda).

| Opção | Prós | Contras |
|---|---|---|
| A. Nunca mostrar; só "avaliação gratuita" e venda na unidade | Mantém a regra e o modelo comercial (vende na avaliação) | Impede compra online e promoção com valor; cliente que pesquisa preço vai ao concorrente |
| B. Preço só para logado | Captura cadastro (troca justa: "entre para ver condições"); preço fora do Google | Algum atrito; preço vaza por print |
| C. Preço só em promoções, com regulamento | Usa preço como gatilho controlado; validade e limite | Sem preço de tabela, a promoção perde referência "de/por" |
| D. Preço público | Transparência; SEO de intenção "quanto custa" | Rompe a regra; guerra de preço entre unidades vizinhas |

**Recomendação: B + C.** Página pública sem preço (mantém regra e SEO atual); logado vê preço da unidade preferida; promoções podem mostrar preço com regulamento. A rede define por procedimento a visibilidade (oculto, só logado, só promoção) e uma faixa sugerida.
**Atenção jurídica:** franqueadora impor preço mínimo de revenda pode ser questionado no CADE (fixação de preço de revenda). Preço sugerido e teto costumam ser mais seguros que piso. Validar com o jurídico da Salus antes de ligar "piso".
**Sorridents:** o Código de Ética Odontológica restringe anúncio de preços, descontos e formas de pagamento. Para a marca 2, a opção provável é A. Validar com o jurídico.

## D2. Pagamento e quem recebe
| Opção | Como funciona | Prós | Contras |
|---|---|---|---|
| A. Rede recebe tudo e repassa | Uma conta da rede; repasse mensal à unidade | Simples de integrar; controle total | A rede passa a ter receita bruta de terceiros (tributação e risco fiscal), conciliação manual, a rede responde por estorno e chargeback; nota fiscal confusa (quem presta o serviço é a unidade) |
| B. Split no gateway (marketplace) | Cada unidade tem subconta (KYC do CNPJ); o gateway divide na hora: unidade recebe o valor, rede recebe taxa ou royalty, se houver | Dinheiro vai direto a quem presta; nota pela unidade; conciliação automática | Onboarding de 130 CNPJs; taxa de split; escolher gateway com split, Pix, parcelado e antifraude |
| C. Cada unidade com seu gateway | Unidade conecta a própria conta | Autonomia | 130 integrações diferentes, sem padrão nem relatório de rede |
| D. Sem pagamento online na fase 1 | Agenda e pacote visível; paga na unidade | Lança rápido, sem risco financeiro | Não entrega o "pagou pelo sistema" do pedido |

**Recomendação: B**, com piloto em 5 a 10 unidades. Se a DocBiz já tiver financeiro e emissão de nota integrados a um gateway, avaliar usar o mesmo para não duplicar caixa. Começar com D nas unidades que ainda não fizeram o KYC.
Subdecisões:
- **D2a** Taxa da rede no split: nenhuma, percentual de royalty de marketing digital, ou tarifa fixa por venda online. Depende do contrato de franquia.
- **D2b** Regulamento de cancelamento: arrependimento de 7 dias para compra online com estorno integral (CDC, art. 49); depois disso, proporcional às sessões feitas, com multa limitada (o CDC veda vantagem excessiva). Texto pelo jurídico.
- **D2c** Nota fiscal: emitida pela unidade vendedora (NFS-e municipal) via DocBiz, se emitir, ou via emissor integrado. Rede nunca emite nota de serviço da unidade.
- **D2d** Parcelamento: sem juros até N vezes por conta da unidade ou com juros para o cliente; definir por modelo de pacote.
- **D2e** Pix Automático para planos recorrentes (ex.: manutenção mensal): fase 2.

Antes de escolher o gateway: levantar com script, em fonte oficial de cada gateway, taxas de Pix, cartão, antecipação, split, subconta e chargeback. Os números não entram nesta spec sem essa coleta.

## D3. Integração com a DocBiz
Perguntas para a DocBiz (enviar via Osmar):
1. Existe API de disponibilidade por unidade, procedimento, profissional e sala? Qual latência?
2. Existe API para criar, remarcar e cancelar agendamento, e webhook de mudança (confirmado, compareceu, faltou)?
3. Existe cadastro de paciente com ID estável e busca por CPF, e-mail ou celular?
4. Pacotes e sessões: a DocBiz registra pacote vendido e consumo por sessão? Expõe por API? Aceita criar pacote vendido fora?
5. Financeiro: a DocBiz emite NFS-e? Tem gateway integrado? Registra pagamento externo?
6. Quem é o controlador do dado clínico na DocBiz hoje (unidade, rede ou Salus) e há contrato de operador?
7. Ambiente de homologação, limites de chamada e SLA.

| Opção | Prós | Contras |
|---|---|---|
| A. API em tempo real (DocBiz fonte da verdade) | Disponibilidade real, sem conflito, respeita o princípio IV | Depende da DocBiz expor API e da latência |
| B. Solicitação de horário + confirmação pela unidade | Funciona sem API | Atrito, SLA humano, cliente não vê vagas reais |
| C. Agenda própria na plataforma, espelhada | Independência | Duplica agenda, conflito de horário, viola o princípio IV |

**Recomendação: A com fallback B.** Pacote e sessões: DocBiz como fonte do consumo; a plataforma guarda o espelho para exibir rápido. Se a DocBiz não expuser pacotes, a plataforma registra o pacote e a unidade marca a sessão (fase de transição, com conferência semanal).

## D4. Quem envia campanha
| Opção | Prós | Contras |
|---|---|---|
| A. Unidade dispara livre | Agilidade | Spam, conflito entre unidades, risco de publicidade irregular, custo de WhatsApp sem controle |
| B. Unidade monta por modelo; plataforma envia; aprovação conforme política | Controle, consistência de marca, a unidade nunca recebe a lista | Fila de aprovação na rede |
| C. Só a rede envia; unidade pede | Máximo controle | Gargalo; unidade sem autonomia, contra o pedido do Osmar |

**Diretriz do Osmar (21/11/2026, 09h15):** a rede configura tudo antes, com padrão bloqueado; campanhas de unidade passam pela aprovação da rede; nenhuma unidade envia para a base toda. Isso fixa a opção B e afasta A.

**Recomendação: B.** Nos 3 primeiros meses toda campanha de unidade passa por R-MKT. Depois, campanhas que usam modelo sem campos livres publicam direto (E, pós-moderadas), e texto livre continua EA.

## D5. Limites e cotas (proposta inicial para calibrar)
- Por cliente, somando rede e unidades: no máximo 1 mensagem de marketing por semana e 4 por mês; nenhuma entre 21 h e 9 h nem aos domingos (configurável).
- Por unidade: 2 campanhas por mês, alcance máximo por campanha limitado ao seu segmento elegível; WhatsApp com orçamento mensal definido pela rede.
- Prioridade quando há disputa: rede (nacional) > unidade preferida do cliente > unidade mais próxima.
- **D5b. Conflito entre unidades na mesma cidade** (São Paulo tem dezenas):
  - A. "Base da cidade" inteira para qualquer unidade: simples, mas gera disputa e spam.
  - B. Só clientes vinculados à unidade + clientes sem unidade preferida dentro do raio (padrão 5 km em capitais, 15 km no interior): **recomendado**.
  - C. Só clientes vinculados.
  Promoções de unidades próximas continuam visíveis na vitrine "Perto de você" da área do cliente (sem envio ativo).

- **D5c. Alcance máximo que a rede pode conceder** (Osmar pediu estado, cidade, raio ou só clientes da própria unidade): recomendação de padrão ao liberar: "clientes da própria unidade"; raio e cidade como exceção; UF só para unidades únicas no estado; "base nacional" nunca para unidade.
- **D5d. Quem pode publicar avisos no mural**: só a rede (R-ADM, R-MKT, R-COM) ou também o gestor regional para a sua regional. Recomendação: rede e gestor regional (se liberado); unidade não publica no mural.
- **D5e. Atribuição de resultados**: último clique em até 7 dias para agendamento e 30 dias para venda (recomendado) ou primeiro clique ou multitoque. Precisa ser igual para todas as unidades.
- **D5f. Replicar campanha**: a rede publica direto nas unidades de destino (com aviso) ou propõe e a unidade aceita. Recomendação: as duas opções, escolha na hora; publicar direto só para campanha com oferta nacional.

## D6. Idade mínima e dado de idade
- A. Conta só para 18+ (declaração no cadastro; data de nascimento na compra). **Recomendado.**
- B. 16+ com aceite do responsável: exige verificação do responsável (LGPD, art. 14, melhor interesse); complexo.
- C. Menores como dependentes da conta de um responsável: fase futura (ver `ideias.md`).
Pedir **data de nascimento** em vez de "idade" (idade fica desatualizada e não permite aniversário). Na etapa leve, aceitar "pular"; na compra, obrigatória.

## D7. Dados de saúde (anamnese, contraindicações, fotos clínicas)
São dados pessoais sensíveis (LGPD, art. 11). Exigem consentimento específico e destacado ou outra base do art. 11 (ex.: tutela da saúde por profissional), RIPD, acesso mínimo e segurança reforçada.
- A. Não coletar na plataforma; ficam na DocBiz e no atendimento. **Recomendado para a fase 1.**
- B. Anamnese digital pré-consulta na plataforma, enviada à DocBiz e apagada da plataforma após a sincronização. Fase 2, com RIPD e aval do responsável técnico.
- C. Guardar na plataforma. Não recomendado.
"Interesse em procedimento" não é dado de saúde por si, mas combinações (ex.: interesse em tratamento ligado a condição médica) podem revelar saúde. Mitigação: interesses em categorias de estética, não de condições.

## D8. Controladoria do dado clínico
A 001 fixou a rede como controladora dos leads (D15 da 001). Para pacientes na DocBiz (prontuário), o responsável costuma ser a clínica e o profissional. Opções: rede controladora de tudo; controladoria conjunta rede e unidade para dado clínico; unidade controladora do clínico. **Recomendação:** rede controladora da conta, marketing e compras online; dado clínico fica com quem a DocBiz e o contrato já definem, documentado em contrato de operador. Validar com o jurídico.

## D9. Conta por marca ou conta Salus
- A. Conta por marca (Gio e Sorridents separadas). **Recomendado**: controladores e regras de publicidade diferentes.
- B. Conta Salus única com consentimento para compartilhar entre marcas: fase futura, se houver estratégia cruzada.

## D10. Métodos de entrada no lançamento
Recomendação: OTP por e-mail, link mágico, Google e Apple no lançamento; OTP por WhatsApp quando o custo por mensagem de autenticação for aprovado; senha opcional; passkey e biometria no app. Para o app iOS, se houver login social, oferecer Apple ou outra opção que atenda às regras da App Store.

## D11. Personalização com interesses inferidos
Recomendação: só com consentimento de personalização (opt-in), exibindo "por que estou vendo isso".

## D12. WhatsApp: provedor, número e custo
- Número por marca (oficial, verificado) com o nome da unidade na mensagem, ou número por unidade. **Recomendado: por marca** na fase 1 (custo e reputação); número por unidade só para conversa humana.
- Meta cobra por mensagem de template (marketing, utilidade, autenticação), com preço por categoria e país. Rede define quem paga campanha de unidade (cota inclusa ou débito na unidade). Coletar preços na fonte oficial antes de orçar.

## D13. Política de no-show
Recomendação escalonada: 1ª falta, aviso; 2ª em 6 meses, confirmação ativa obrigatória 24 h antes; 3ª, agendamento online só com sinal (se D2 permitir) ou só pela unidade. Para pacote, a sessão faltada sem aviso conta como feita só se o regulamento aceito disser isso.

## D14. Transferência de pacote entre unidades
Opções: proibida; permitida com aceite das duas unidades e acerto financeiro definido pela rede; livre na rede com compensação automática no split. **Recomendação:** fase 2, com aceite das duas unidades e regra de rateio da rede.

## D15. Endereço da área do cliente
Opções: caminho no domínio principal (`/minha-conta`) via proxy, ou subdomínio (`conta.` ou `minha.`). **Recomendação:** subdomínio da marca com SSO (cookies primários, sem afetar o WordPress atual), e o site institucional linka "Entrar".

## D16. Escopo do MVP e fases
- **Fase 1 (MVP):** controles da rede (padrão bloqueado) e mural de avisos, conta e cadastro progressivo, consentimentos e central de privacidade, interesses, unidade preferida, catálogo com visibilidade de preço, promoções por modelo, agendamento (API ou fallback), meus agendamentos, NPS, notificações por e-mail e WhatsApp transacional, painel da unidade (clientes, ofertas, promoções) e da rede.
- **Fase 1 também:** campanhas da rede com assistente e modelos (área do cliente e e-mail), painel de performance básico.
- **Fase 2:** pagamento online com split, pacotes e sessões, recibos e nota, campanhas de unidade com cota e WhatsApp, cruzamento e replicar campanha, chat, lista de espera.
- **Fase 3:** app com push, carteira e fidelidade, indicação, vale-presente, anamnese digital (se D7 B), perfis familiares, transferência entre unidades.
