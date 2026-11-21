# Inventário de telas: quiz, inteligência e tracking (003)

Rev. 1b, 21/11/2026. Só inventário; nada desenhado. Numeração Q (quiz), I (inteligência), T (tracking e tags), para não colidir com a 001 (01 a 32) e a 002 (C, U, R). Prioridade pela fase do backlog em `spec.md`.

## Quiz: público (site, área do cliente e app)
| # | Tela | Conteúdo | Fase |
|---|---|---|---|
| Q01 | Abertura do quiz | Título, tempo estimado, finalidade das respostas em uma frase, link da política, começar | 2 |
| Q02 | Pergunta | Uma pergunta por tela, barra de progresso, voltar, opções grandes com imagem | 2 |
| Q03 | Resultado | 1 a 3 procedimentos com texto aprovado, unidade mais próxima, CTAs (agendar avaliação gratuita, ver ofertas, salvar resultado) | 2 |
| Q04 | Salvar resultado | Cadastro leve da 002 (C01 a C03) com consentimento de personalização desmarcado | 2 |
| Q05 | Bloco de quiz na landing | Versão embutida no template da unidade | 2 |

## Quiz: painel (rede e unidade)
| # | Tela | Conteúdo | Fase |
|---|---|---|---|
| Q10 | Biblioteca de quizzes | Modelos da rede, quizzes publicados, rascunhos, em aprovação; filtros; "duplicar modelo" (unidade, se liberado) | 2 |
| Q11 | Editor de fluxo | Grafo de perguntas com arrastar, ramificações, alerta de ciclo e de caminho sem fim | 2 |
| Q12 | Editor de pergunta | Tipo, texto, opções, imagens, obrigatória; validador de termos de saúde com explicação | 2 |
| Q13 | Regras de recomendação | Matriz opção x procedimento com pontos; simulador "se eu responder assim, o resultado é" | 2 |
| Q14 | Textos de resultado | Por procedimento, com validador de publicidade e prévia celular e desktop | 2 |
| Q15 | Publicar e distribuir | Finalidade e texto legal, versão, canais (campanha da 002, landing, área do cliente, link, QR), alcance dentro do teto | 2 |
| Q16 | Fila de aprovação de quiz | Prévia do fluxo e do resultado; aprovar, reprovar com motivo | 2 |
| Q17 | Resultados do quiz | Funil, abandono por pergunta, distribuição de respostas, cruzamentos (idade, cidade, UF, unidade, estação, clima) com amostra mínima | 2 |

## Inteligência
| # | Tela | Conteúdo | Fase |
|---|---|---|---|
| I01 | Demanda por procedimento | Ranking por fonte (quiz, catálogo, agendamentos, Search Console, Trends), filtros de UF, cidade, faixa, período | 4 |
| I02 | Sazonalidade e clima | Curvas mensais de demanda x temperatura, UV e normal climatológica por cidade | 4 |
| I03 | Potencial e penetração | Mapa de clientes por mil habitantes da faixa-alvo, cidades sem unidade com demanda | 4 |
| I04 | Calendário comercial | Datas nacionais, estaduais e municipais; campanhas planejadas por data | 4 |
| I05 | Recomendações | Lista de insights com explicação, fonte, amostra e botões "criar campanha" e "replicar" | 4 |
| I06 | Fontes de dados | Catálogo com dono, licença, custo, frequência, última coleta, status; ligar e desligar | 4 |
| I07 | Concorrência local | Concorrentes no raio, nota e avaliações (só se D11 liberar) | 4 |

## Tracking e gerenciador de tags
| # | Tela | Conteúdo | Fase |
|---|---|---|---|
| T01 | Plano de medição | Perguntas de negócio, KPIs, eventos ligados | 1 |
| T02 | Dicionário de eventos | Lista com status, dono, versão; detalhe com propriedades, tipos, gatilho, mapeamento por destino; propor mudança | 1 |
| T03 | Changelog e versões | Versões do dicionário e do loader, diff, aprovar, reverter | 1 |
| T04 | Monitor de qualidade | Volume por evento, inválidos, PII detectada, UTMs inválidas, unidades sem conversão, divergência coletor x GA4 x DocBiz | 1 |
| T05 | Alertas | Alertas abertos, regras (desvio, ausência, inválidos, PII), destinatários | 2 |
| T06 | Inspetor de eventos (debug) | Fluxo ao vivo de um navegador de teste em homologação, validação de schema e destinos que receberam | 1 |
| T07 | Gerador de UTMs e links | Listas fechadas, padrão de nome, link curto, QR, lista de links com dono e cliques | 1 |
| T08 | Destinos da rede | GA4 da marca, Google Ads, Meta, TikTok, Search Console (domínio), coletor; campos tipados, segredos, consentimento exigido, status | 1 |
| T09 | Consentimento | Texto do banner por versão, categorias, mapeamento para Consent Mode v2, taxa de aceite por categoria | 1 |
| T10 | Search Console por unidade (visão da rede) | Propriedades por prefixo criadas, acesso concedido a quem, verificações por meta tag, domínios próprios | 1 |
| T11 | Ficha da unidade, aba SEO: "Tags e medição" | Campos tipados (GA4 próprio, api_secret, meta tag do Search Console, Ads, Meta, TikTok) com cadeado conforme política, validação ao digitar, status de aprovação, consentimento exigido, impacto de performance, link para a Wiki e o vídeo | 3 |
| T12 | Pedido de tag ou script | Formulário de pedido da unidade (tipo, motivo), revisão da rede (segurança, peso, LGPD) | 3 |
| T13 | Fila de aprovação de tags | Diff, validação, peso estimado, aprovar ou reprovar | 3 |
| T14 | Orçamento de performance | Peso e requisições por landing com as tags ligadas, nota Lighthouse mobile, bloqueios | 3 |
| T15 | Ajuda "Limites do GA4" | Explicação curta (sem permissão por unidade; subpropriedades só no 360), custos do server-side, artigo e vídeo | 3 |

## Telas da 001 e da 002 que mudam
Ver `impacto-na-001-002.md`: aba SEO da ficha (001) ganha "Tags e medição"; Wiki ganha a trilha "Medição e tags"; dashboard de insights recebe os tipos novos; assistente de campanha (002, U07 e R07) ganha objetivo "quiz"; área do cliente (002, C06) mostra "por que estou vendo isso" com origem quiz; central de privacidade (002, C23) ganha "minhas respostas de quiz".
