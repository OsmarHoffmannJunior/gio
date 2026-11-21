# Política de campos: ficha, landing e dados estruturados

Versão 1.1, 21/11/2026 (1.1: itens 72 a 83 vindos de dados-ficha.md; GBP como autonomia da unidade). Princípios: II, V, VI, XI, XII. A rede (R-ADM) edita esta tabela por marca; a Sorridents terá a sua.

## Estados
- **T · Travado:** a unidade só vê. Mudança só pela rede, ou por chamado da unidade.
- **E · Editável:** a unidade publica direto. O validador automático roda (regras da marca, formato, tamanho), e a rede pode despublicar depois (pós-moderação).
- **EA · Editável com aprovação:** a unidade edita um rascunho e publica só depois da aprovação do perfil da rede indicado.
- **L · Leitura:** visível, sem edição. Inclui campos automáticos (vindos do GBP, da DocBiz ou calculados).
- **O · Oculto:** o perfil não vê o campo.

Regras gerais:
- Campo novo nasce T.
- Por padrão a política vale igual para U-FRQ e U-GER. A rede pode diferenciar por perfil personalizado (ex.: gerente sem acesso a promoções).
- A coluna "Rede" diz qual perfil de rede edita direto (override, princípio XII) e qual aprova os EA. R-ADM sempre pode.

## 1. Ficha da unidade
| # | Campo | Grupo | Alimenta | U-FRQ e U-GER | U-REC | Rede (edita / aprova) | Validação e notas |
|---|---|---|---|---|---|---|---|
| 1 | Nome público da unidade | Identificação | Landing, schema `name`, GBP, listagem | T | L | R-SEO | Padrão "GiO + bairro/cidade"; igual ao GBP |
| 2 | Slug e URL da ficha oficial | Identificação | URL, canonical, sitemap | T | L | R-SEO | Mudança gera 301 automático |
| 3 | Status (ativa, em inauguração, inativa) | Identificação | Publicação, listagem, noindex | T | L | R-ADM | Inativa = 410 ou 301 para a unidade mais próxima (decisão em aberto) |
| 4 | Tipo (full, slim) | Identificação | Catálogo de tratamentos permitido | T | L | R-ADM | |
| 5 | Razão social e CNPJ | Identificação | Rodapé legal, schema `legalName` (opcional) | T | O | R-ADM | |
| 6 | ID DocBiz, ID CRM (Salesforce) | Integração | Envio do lead, status | T | O | R-ADM | Sincronizado; nunca editado à mão pela unidade |
| 7 | Responsável técnico e registro profissional | Regulatório | Rodapé, página, schema `employee` | EA | L | R-ADM aprova | Exigência de conselho de classe varia por tratamento (decisão em aberto) |
| 8 | Data de inauguração e texto de "em breve" | Identificação | Landing de pré-abertura | EA | L | R-MKT aprova | |
| 9 | Permitir agendamentos online | Operação | Formulário ligado ou desligado | E | L | R-COM | Desligar pede motivo e avisa a rede |
| 10 | CEP, logradouro, número, complemento, bairro, cidade, UF | NAP | Landing, schema `address`, GBP, mapa | T | L | R-SEO | Mudança de endereço é processo (chamado), mexe no GBP |
| 11 | Ponto de referência e "como chegar" (texto) | Localização | Bloco Como chegar | E | L | R-MKT pós-modera | Validador da marca |
| 12 | Latitude e longitude (pino) | NAP | Mapa, schema `geo`, listagem | T (sugerir ajuste = EA) | L | R-SEO | Geocodificado pelo CEP; ajuste de pino pela unidade vai para aprovação |
| 13 | Telefone fixo | NAP | Landing, schema `telephone`, GBP | EA | L | R-SEO aprova | Tem que bater com o GBP; teste de ligação opcional |
| 14 | WhatsApp que recebe leads | Operação | Roteamento do lead, botão WhatsApp | E | L | R-COM | Só ativa após código de verificação enviado ao número; troca avisa a rede |
| 15 | E-mail da unidade e e-mail de avisos | Operação | Notificações | E | L | R-ADM | Confirmação por link |
| 16 | Área atendida (bairros) | SEO local | Texto da landing, schema `areaServed` | EA | L | R-SEO aprova | Máx. 10 bairros reais; sem cidades vizinhas onde há outra unidade |
| 17 | Horário de funcionamento | NAP | Landing, schema `openingHoursSpecification`, GBP | E | L | R-SEO pós-modera | A unidade muda o valor; a rede controla o mapeamento |
| 18 | Exceções e feriados | NAP | Landing, schema `specialOpeningHours`, GBP | E | L | R-SEO pós-modera | Feriados nacionais pré-carregados pela rede |
| 19 | Horário de agenda online | Operação | Slots do formulário | E | L | R-COM | Pode vir da DocBiz (decisão em aberto) |
| 20 | Texto "Sobre a unidade" | Conteúdo | Bloco Sobre, schema `description` | E | L | R-MKT pós-modera | Até 600 caracteres, validador da marca |
| 21 | Fotos da unidade (recepção, salas, equipe) | Conteúdo | Galeria, schema `image` | E | L | R-MKT pós-modera | Mín. 1200 px, sem rosto de cliente sem termo, alt obrigatório (sugerido automático) |
| 22 | Foto principal da fachada | Conteúdo | Topo, og:image, schema `image[0]` | EA | L | R-MKT aprova | Logo atual da marca visível |
| 23 | Fotos de antes e depois | Conteúdo sensível | Galeria de resultados | EA | O | R-ADM aprova | Termo de uso de imagem anexado e regras de publicidade em saúde (decisão em aberto) |
| 24 | Ordem e texto alternativo das fotos | Conteúdo | Galeria | E | L | R-MKT | |
| 25 | Equipe: nome, cargo, foto | Conteúdo | Bloco Equipe | E | L | R-MKT pós-modera | Consentimento do profissional para uso da imagem |
| 26 | Equipe: registro profissional | Regulatório | Bloco Equipe | EA | L | R-ADM aprova | |
| 27 | Tratamentos oferecidos (ligar ou desligar do catálogo) | Conteúdo | Bloco Tratamentos, schema `makesOffer` | E | L | R-MKT | Só itens do catálogo permitidos ao tipo da unidade |
| 28 | Tratamento em destaque | Conteúdo | Ordem dos cards | E | L | R-MKT | |
| 29 | Texto local de um tratamento | Conteúdo | Card do tratamento | EA | L | R-MKT aprova | Texto nacional é T |
| 30 | Tratamento fora do catálogo | Catálogo | Catálogo | T (pedido) | O | R-ADM | Entra no catálogo da marca, não só na unidade |
| 31 | FAQ local (perguntas da unidade) | Conteúdo | Bloco FAQ, schema `FAQPage` (decisão em aberto) | E | L | R-SEO pós-modera | Máx. 8; validador da marca |
| 32 | FAQ base da rede | Conteúdo | Bloco FAQ | T | L | R-SEO e R-MKT | Atualização em massa em todas as unidades |
| 33 | Promoção estruturada (título, tratamento, validade, condições do modelo) | Conteúdo | Bloco Promoções, faixa do topo | E | L | R-MKT pós-modera | Só por modelo da rede; validade obrigatória; sai do ar sozinha no fim |
| 34 | Promoção fora do modelo ou banner próprio | Conteúdo | Bloco Promoções | EA | O | R-MKT aprova | |
| 35 | Instagram e Facebook da unidade | Social | Rodapé, schema `sameAs` | E | L | R-SEO pós-modera | Entra no sameAs só depois de validado pela rede |
| 36 | Perfil do Google (place_id, link do GBP) | SEO local | Comparação NAP x GBP, sameAs, leitura de nota | E (a unidade informa o próprio perfil) | L | R-SEO valida o vínculo | O GBP é da unidade (decisão do Osmar, 21/11/2026). O sistema só lê e compara, nunca edita o GBP |
| 37 | Resposta a avaliações do Google | Reputação | GBP (fora do sistema) | Feita no próprio GBP pela unidade | L | ninguém na rede | O sistema mostra avaliações sem resposta e a trilha da Wiki traz modelos e boas práticas |
| 38 | Nota e número de avaliações | Reputação | Faixa de prova social | L | L | automático | Vem do GBP; nunca digitado |
| 72 | Shopping ou centro comercial e loja | NAP | schema `containedInPlace`, texto | EA | L | R-SEO aprova | Comum em unidades de shopping |
| 73 | Atributos (estacionamento, acessibilidade, Wi-Fi, formas de pagamento) | Conteúdo | schema `amenityFeature`, `paymentAccepted`, landing | E | L | R-MKT pós-modera | Lista fechada da rede; deve espelhar o GBP da unidade |
| 74 | Descrição do perfil do Google | GBP (fora do sistema) | GBP | Editada no GBP pela unidade | L | ninguém na rede | O sistema compara e sugere texto; não publica no GBP |
| 75 | Link de agendamento e site no GBP | GBP (fora do sistema) | GBP | Configurado no GBP pela unidade | L | ninguém na rede | O sistema mostra a URL oficial recomendada (com UTM) e alerta quando o GBP aponta para outro site |
| 76 | Fechamento temporário (início, fim, motivo) | Operação | Landing, schema `specialOpeningHours` | E | L | R-COM é avisado | A unidade também deve marcar no GBP (checklist da Wiki) |
| 77 | Vídeo ou tour da unidade | Conteúdo | Bloco Galeria, `VideoObject` | EA | L | R-MKT aprova | |
| 78 | Contato interno do franqueado (nome, e-mail, celular) | Operação | Avisos internos | E | O | R-ADM | Não aparece no site |
| 79 | Regional e grupo de unidades | Identificação | Escopo de acesso | T | O | R-ADM | |
| 80 | Modelo de ficha aplicado | Estrutura | Blocos, menu, campos visíveis | T | L | R-ADM e R-MKT | Modelo principal da rede vale por padrão |
| 81 | Menu da ficha (itens, ordem, âncoras) | Estrutura | Navegação da página | T | L | R-MKT e R-SEO | Definido no modelo de ficha; a unidade só vê |
| 82 | Variantes de landing (A/B, campanha, serviço) | Landing | URLs de variante | EA (pedir ou criar rascunho) | L | R-MKT aprova e publica | Campanha: noindex e canonical para a principal; A/B: mesma URL; serviço: indexável com conteúdo próprio |
| 83 | Módulos e recursos habilitados | Plataforma | Menu e permissões | L | O | R-ADM | Herança rede > regional > unidade |

## 2. Blocos da landing
| # | Bloco ou item | U-FRQ e U-GER | U-REC | Rede (edita / aprova) | Notas |
|---|---|---|---|---|---|
| 39 | Escolha do template (A, B, C) | EA | L | R-MKT aprova | Troca registra versão e permite comparar resultados |
| 40 | Ordem dos blocos opcionais | E | L | R-MKT | Blocos fixos não se movem |
| 41 | Ligar ou desligar bloco opcional (Equipe, Promoções, Galeria) | E | L | R-MKT | |
| 42 | Topo: imagem | E (entre fotos aprovadas) | L | R-MKT | |
| 43 | Topo: título e subtítulo | T (modelo com variáveis: bairro, cidade, tratamento) | L | R-MKT e R-SEO | O H1 é SEO técnico |
| 44 | Formulário (campos, consentimento, botão) | T | L | R-ADM | Conversão confirmada no servidor (princípio III) |
| 45 | Texto dos botões (CTA) | T | L | R-MKT | "Avaliação gratuita" |
| 46 | Faixa de confiança | T | L | R-MKT | |
| 47 | Bloco Sobre | E | L | R-MKT pós-modera | Campo 20 |
| 48 | Bloco Galeria | E | L | R-MKT pós-modera | Campos 21 a 24 |
| 49 | Bloco Tratamentos | E | L | R-MKT | Campos 27 a 29 |
| 50 | Bloco Equipe | E | L | R-MKT pós-modera | Campos 25 e 26 |
| 51 | Bloco Avaliações | L (automático) | L | R-MKT | Escolha dos depoimentos exibidos: E (decisão em aberto) |
| 52 | Bloco Como chegar e horários | L (gerado do NAP) + E no texto | L | R-SEO | Campos 10 a 12, 17 e 18 |
| 53 | Bloco FAQ | E (local) + T (base) | L | R-SEO | Campos 31 e 32 |
| 54 | Bloco Promoções | E (modelo) / EA (fora do modelo) | L | R-MKT | Campos 33 e 34 |
| 55 | Cores e fundos de bloco | E (só paleta da marca) | L | R-MKT | |
| 56 | Rodapé, aviso de privacidade, texto de consentimento | T | L | R-ADM (jurídico) | Versão do texto registrada no consentimento |

## 3. Dados estruturados e SEO técnico (só a rede, perfil SEO)
| # | Item | U-FRQ e U-GER | U-REC | Rede | Notas |
|---|---|---|---|---|---|
| 57 | Tipo de schema (LocalBusiness, MedicalBusiness ou subtipo) | L (prévia) | O | R-SEO | Por marca e por tipo de unidade (decisão em aberto) |
| 58 | Mapeamento NAP para schema (`name`, `address`, `geo`, `telephone`, `openingHours`) | L | O | R-SEO | Valores vêm da ficha; a estrutura é da rede |
| 59 | Categorias do schema (e recomendação de categoria do GBP) | L | O | R-SEO | A categoria do GBP é escolhida pela unidade no próprio GBP; a rede só recomenda na Wiki |
| 60 | `sameAs` (redes, GBP, perfis oficiais) | L | O | R-SEO | Campo 35 entra após validação |
| 61 | `parentOrganization` e `brand` (rede Gio, Grupo Salus) | L | O | R-SEO | |
| 62 | FAQPage, Service/Offer e BreadcrumbList | L | O | R-SEO | Gerados dos blocos |
| 63 | AggregateRating e Review no schema | O | O | R-SEO | Desligado por padrão: o Google não exibe estrelas de avaliação marcadas pelo próprio negócio em LocalBusiness |
| 64 | Title e meta description | L | O | R-SEO | Modelo com variáveis + ajuste por unidade só pela rede |
| 65 | Canonical e estratégia de domínio (ficha, domínio, redireciona) | L | O | R-SEO | Princípio VI |
| 66 | Robots, noindex, sitemap, hreflang | O | O | R-SEO | |
| 67 | Open Graph (og:title, og:image) | L | O | R-SEO | og:image vem do campo 22 |
| 68 | Scripts, pixels e tags (head e body) | O | O | R-SEO e R-ADM | Fim do GTM por unidade (hoje 17 unidades têm o próprio); pixel extra só por pedido |
| 69 | Eventos de conversão e IDs de GA4/Ads | O | O | R-SEO | Disparo só pelo servidor (princípio III) |
| 70 | Domínio próprio: pedido e configuração de DNS | E (pedido + DNS) | O | R-SEO aprova a publicação | A estratégia de canonical é sempre da rede |
| 71 | Regras da marca (lista de termos proibidos, obrigatórios, limites) | L | L | R-ADM e R-MKT | Mostradas ao lado do editor |

## Rev. 3.2 (21/11/2026): itens das specs 002 e 003
- Campos 33 e 34 (promoção) e o bloco Promoções (54) respeitam a liberação "promocoes" da 002: se bloqueada, viram T para a unidade.
- Preço por procedimento: T por padrão; E ou EA se liberado (política de preço, D1 da 002, recomendação: sem preço público).
- Duração local do procedimento: E.
- Procedimento comercializável online: EA.
- Pacote local por modelo: EA.
- Texto local do procedimento: E com validador.
- Tags (003): `tag.ga4_unidade`, `tag.gsc_meta`, `tag.google_ads_unidade`, `tag.meta_pixel_unidade`, `tag.tiktok_unidade` são T por padrão e EA quando liberadas por escopo; `tag.script_livre` é sempre T para unidade.
