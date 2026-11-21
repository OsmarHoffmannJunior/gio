# Inventário completo dos dados editáveis da ficha da unidade

Versão 1.0, 21/11/2026. Princípios: II, V, XI, XIII. Cruza três fontes do projeto:
- **AGDM:** cadastro atual da unidade no painel da DocPix (`../../../agdm/mapa-agdm.md`, telas 05 a 08).
- **Site:** o que as 130 fichas públicas mostram hoje (`../../../fichas-completude.csv`, `resumo-fichas.json`).
- **GBP:** o que os perfis do Google mostram (`../../../gbp-gio.csv`, amostra de 10 perfis).

Política de edição: código da tabela em `politica-campos.md` (coluna "Pol."). Estados: T travado, E editável, EA editável com aprovação, L leitura, O oculto. Quando a coluna diz "U: E", vale para Franqueado e Gerente; a Recepcionista é L, salvo nota.

## Cobertura hoje (130 fichas, script `scripts/` do diagnóstico, 21/11/2026)
| Dado | Fichas com o dado |
|---|---|
| Telefone na API | 111 |
| WhatsApp | 129 |
| E-mail | 130 |
| Coordenadas | 117 |
| Instagram e Facebook | 130 |
| Foto de fachada marcada | 57 |
| Complemento | 34 |
| Ponto de referência | 2 |
| ID Salesforce | 123 |
| Fotos na ficha | 70 fichas com zero fotos (máximo 15) |
| Texto "Estrutura" padrão (sem texto local) | 127 |
| Equipe, avaliações, FAQ, link do GBP, link de rota | 0 |
| Schema local, canonical próprio, preços | 0 |

No GBP (amostra de 10): 10 reivindicados; 8 com categoria principal "Serviço de depilação a laser"; só 3 apontam para a URL da ficha; telefone bate com a ficha em 8.

## Inventário
Legenda de origem: **AGDM** campo existe no cadastro atual · **Site** aparece na ficha pública · **GBP** aparece no perfil do Google · **Novo** não existe hoje.

### 1. Identificação e operação
| # | Campo | Tipo | Obrig. | Validação | Origem atual | Schema e SEO | Pol. |
|---|---|---|---|---|---|---|---|
| 1 | Nome público da unidade | texto 60 | sim | Padrão "GiO + bairro/cidade"; igual ao título do GBP | AGDM "Unidade"; Site H1; GBP título (com variações, ex. "GiOlaser Campinas Cambuí") | `name`, title, H1 | 1 · U: T |
| 2 | Slug da ficha | texto | sim | minúsculas, sem acento, único | AGDM "URL Site"; Site URL | URL, canonical, sitemap | 2 · U: T |
| 3 | Status | lista (ativa, em inauguração, temporariamente fechada, inativa) | sim | | AGDM Ativo/Inativo | robots, `openingHours` vazio se fechada | 3 · U: T |
| 4 | Fechamento temporário (início, fim, motivo) | datas + texto | não | fim maior que início | GBP "fechado temporariamente"; Novo na plataforma | `specialOpeningHours`, faixa na landing | 76 · U: E (avisa a rede) |
| 5 | Tipo de clínica | lista (full, slim) | sim | | API `tipo_clinica` | catálogo permitido | 4 · U: T |
| 6 | Regional e grupo de unidades (multifranqueado) | referência | sim | | Novo | não | 79 · U: T |
| 7 | Razão social | texto | sim | | AGDM select DocBiz "Nome [Razão social - CNPJ]" | `legalName` (opcional) | 5 · U: T |
| 8 | CNPJ | máscara 00.000.000/0000-00 | sim | dígito verificador | AGDM (via DocBiz) | não | 5 · U: T |
| 9 | ID DocBiz | inteiro | sim | existe na DocBiz | AGDM "Unidade DocBiz" | não | 6 · U: T |
| 10 | ID CRM (Salesforce) | texto | não | | API `id_salesforce` (123 de 130) | não | 6 · U: T |
| 11 | Responsável técnico, conselho e registro | texto + lista + texto | depende do tratamento | formato do registro por conselho | AGDM "CRO" (campo herdado do odontológico; "123" no exemplo) | `employee`, rodapé | 7 · U: EA |
| 12 | Data de inauguração | data | não | | AGDM | landing "em breve" | 8 · U: EA |
| 13 | Texto de não inaugurada | texto 200 | não | validador da marca | AGDM | landing "em breve" | 8 · U: EA |
| 14 | Permitir agendamentos online | sim/não | sim | | AGDM | formulário | 9 · U: E |
| 15 | Contato interno do franqueado (nome, e-mail, celular) | texto | sim | e-mail e celular verificados | Novo (AGDM não tem franqueado) | não, uso interno | 78 · U: E · Recepção: O |
| 16 | Modelo de ficha aplicado | referência | sim | modelo ativo da marca | Novo | define blocos e menu | 80 · U: T |
| 17 | Módulos habilitados na unidade | lista | sim | herdado da rede ou regional | Novo | não | 83 · U: L |

### 2. Endereço e localização (NAP)
| # | Campo | Tipo | Obrig. | Validação | Origem atual | Schema e SEO | Pol. |
|---|---|---|---|---|---|---|---|
| 18 | CEP | máscara 00000-000 | sim | consulta de CEP | AGDM; Site texto; GBP | `postalCode` | 10 · U: T |
| 19 | UF, cidade, bairro | lista + texto | sim | IBGE | AGDM; Site; GBP (bairro às vezes diferente, ex. "Alto de Pinheiros") | `addressRegion`, `addressLocality` | 10 · U: T |
| 20 | Logradouro e número | texto | sim | | AGDM; Site; GBP | `streetAddress` | 10 · U: T |
| 21 | Complemento, andar, loja | texto | não | | AGDM (34 de 130) | `streetAddress` | 10 · U: T |
| 22 | Shopping ou centro comercial | referência + texto | não | | Novo (várias unidades ficam em shopping, ex. Boulevard Tatuapé, Manauara) | `containedInPlace` | 72 · U: EA (SEO) |
| 23 | Ponto de referência | texto 120 | não | | AGDM (2 de 130) | landing | 11 · U: E |
| 24 | Texto "como chegar" (transporte, estacionamento) | texto 400 | não | validador da marca | Novo | landing, FAQ | 11 · U: E |
| 25 | Latitude e longitude | decimal | sim para publicar | dentro do município | API (117 de 130); AGDM não tem | `geo`, mapa | 12 · U: T (sugerir ajuste EA) |
| 26 | Área atendida (bairros) | lista até 10 | não | bairros reais do município | Novo | `areaServed`, texto | 16 · U: EA |

### 3. Contato
| # | Campo | Tipo | Obrig. | Validação | Origem atual | Schema e SEO | Pol. |
|---|---|---|---|---|---|---|---|
| 27 | Telefone fixo | máscara | sim | igual ao GBP | AGDM; API (111 de 130); Site; GBP | `telephone` | 13 · U: EA |
| 28 | WhatsApp que recebe leads | máscara celular | sim | código de verificação | AGDM; API (129); Site link | botão, não vai no schema | 14 · U: E |
| 29 | E-mail da unidade | e-mail | sim | confirmação por link | AGDM (único e-mail; padrão uf.unidade@) | `email` (opcional) | 15 · U: E |
| 30 | E-mail de avisos (leads, aprovações) | lista de e-mails | não | confirmação | Novo | não | 15 · U: E |
| 31 | Instagram | @perfil | não | perfil existe | AGDM; API (130); Site link (129) | `sameAs` após validação | 35 · U: E |
| 32 | Facebook | perfil | não | | AGDM; API (130) | `sameAs` após validação | 35 · U: E |
| 33 | Link de agendamento no GBP | URL | não | aponta para a landing com UTM | GBP campo de agendamento (vazio na amostra) | GBP | 75 · feito no GBP pela unidade; sistema recomenda a URL |

### 4. Horários
| # | Campo | Tipo | Obrig. | Validação | Origem atual | Schema e SEO | Pol. |
|---|---|---|---|---|---|---|---|
| 34 | Horário de funcionamento por dia | dia + abre + fecha (até 2 faixas) | sim | fecha maior que abre | AGDM (linhas com descrição livre, ex. "Segunda a sexta"); Site; GBP | `openingHoursSpecification` | 17 · U: E |
| 35 | Exceções e feriados | data + horário ou fechado | não | | AGDM "Restrições de horários" (global, não por unidade) | `specialOpeningHours`, GBP | 18 · U: E |
| 36 | Horário de agenda online | dia + abre + fecha | sim | dentro do funcionamento | AGDM "Horário de Agendamento" | slots do formulário | 19 · U: E |

### 5. Conteúdo da ficha e da landing
| # | Campo | Tipo | Obrig. | Validação | Origem atual | Schema e SEO | Pol. |
|---|---|---|---|---|---|---|---|
| 37 | Texto "Sobre a unidade" | texto 600 | sim para completude | validador da marca; mínimo 200 caracteres para não ser padrão | AGDM "Descrição Serviços"; Site seção "Estrutura" (127 de 130 com texto padrão) | `description` | 20 · U: E |
| 38 | Descrição do perfil do Google | texto 750 | não | regras do GBP (sem URL, sem promoção) | GBP | GBP | 74 · feito no GBP pela unidade; sistema compara |
| 39 | Fotos da unidade | imagem jpg/webp, mín. 1200 px | mín. 6 para completude | sem rosto de cliente sem termo | AGDM "Gerenciar Imagens" (jpg até 2 MB); Site (70 fichas sem foto); GBP (17 a 75 fotos na amostra) | `image`, galeria | 21 · U: E |
| 40 | Categoria da foto (fachada, recepção, sala, equipe, resultado) | lista | sim | | AGDM só "Fachada sim/não" | ordem, og:image | 21 e 22 · U: E (fachada EA) |
| 41 | Título e texto alternativo da foto | texto 125 | sim | sugerido automático | AGDM "Título do Arquivo" | `alt` | 24 · U: E |
| 42 | Ordem das fotos | inteiro | sim | | AGDM "Ordem" | galeria | 24 · U: E |
| 43 | Fotos de antes e depois | imagem + termo de uso de imagem | não | termo anexado | Novo | não indexar rosto | 23 · U: EA (Rede ADM) |
| 44 | Vídeo ou tour da unidade | URL de vídeo | não | domínio permitido | Novo | `VideoObject` (decisão da rede) | 77 · U: EA (MKT) |
| 45 | Equipe: nome, cargo, foto | texto + imagem | não | consentimento de imagem | Novo (Site: 0 fichas com equipe) | bloco Equipe | 25 · U: E |
| 46 | Equipe: registro profissional | texto | quando aplicável | formato por conselho | Novo | bloco Equipe | 26 · U: EA |
| 47 | Tratamentos e áreas oferecidos | seleção no catálogo (Depilação a laser por área, Protocolos, Terapia capilar, Corporais, Faciais, Multifuncionais) | mín. 1 | só itens do tipo de clínica | AGDM "Gerenciar Tratamentos" (marcar e desmarcar) | `makesOffer` / `Service` | 27 · U: E |
| 48 | Tratamento em destaque | referência | não | | Novo | ordem | 28 · U: E |
| 49 | Texto local de um tratamento | texto 300 | não | validador da marca | Novo | card | 29 · U: EA |
| 50 | Pedido de tratamento fora do catálogo | chamado | | | Novo | | 30 · U: T |
| 51 | FAQ local | pergunta + resposta, até 8 | não | validador da marca | Novo (Site: 0) | `FAQPage` (D13) | 31 · U: E |
| 52 | FAQ base | | | | Novo | `FAQPage` | 32 · U: T |
| 53 | Promoção por modelo | modelo + tratamento + condição + validade | não | validade obrigatória, sem preço (D9) | Novo (Site: 0 preços) | não | 33 · U: E |
| 54 | Banner ou promoção fora do modelo | imagem + texto | não | | Novo | não | 34 · U: EA |
| 55 | Atributos (estacionamento, acessibilidade, Wi-Fi, formas de pagamento) | marcações | não | lista da rede, espelha o GBP | GBP atributos; Novo na plataforma | `amenityFeature`, `paymentAccepted` | 73 · U: E |
| 56 | Resposta a avaliações do Google | texto | não | modelos da rede; sem dado de saúde | GBP | não | 37 · feito no GBP pela unidade |
| 57 | Nota e total de avaliações | número | | automático | GBP (4,6 a 4,9 na amostra) | prova social (sem `AggregateRating`) | 38 · U: L |
| 58 | Depoimentos exibidos na landing | seleção entre avaliações do Google | não | só avaliações públicas | Novo | não | 51 · U: E (D recomendada) |

### 6. Landing, modelo de ficha e variantes
| # | Campo | Tipo | Obrig. | Validação | Origem atual | Schema e SEO | Pol. |
|---|---|---|---|---|---|---|---|
| 59 | Template da landing principal (A, B, C) | lista | sim | | Novo | estrutura | 39 · U: EA |
| 60 | Ordem e liga/desliga de blocos opcionais | lista | | permitidos pelo modelo | Novo | | 40 e 41 · U: E |
| 61 | Menu da ficha (itens, ordem, âncoras) | lista ordenada | sim | âncora existe na página | Site: menu do tema (1 link no cabeçalho) | navegação, links internos | 81 · U: T |
| 62 | Variante de landing (A/B, campanha, serviço) | registro (tipo, slug, template, blocos, UTM, período) | não | slug único; canonical conforme o tipo | Novo (AGDM "Formulário ID" por unidade fazia as vezes de campanha) | campanha: noindex + canonical para a principal; A/B: mesma URL; serviço: indexável | 82 · U: EA (MKT) |
| 63 | Cores e fundos de bloco | paleta | | só paleta da marca | Novo | | 55 · U: E |

### 7. SEO técnico e integrações (só a rede)
| # | Campo | Tipo | Origem atual | Pol. |
|---|---|---|---|---|
| 64 | Title e meta description | texto | AGDM meta description (vazia no exemplo) e meta keywords (abandonar); Site: title igual em todas ("Unidade - GIO Estética Avançada") | 64 · U: L |
| 65 | Canonical e estratégia de domínio | lista | Site: 130 de 130 apontam para /unidade/ (que retorna 302) | 65 · U: L |
| 66 | Robots, sitemap | | Site: index, follow | 66 · U: O |
| 67 | Tipo de schema e categorias | lista | Site: só Organization, WebPage, BreadcrumbList; GBP: categoria principal | 57 e 59 · U: L |
| 68 | sameAs, parentOrganization, brand | lista | Novo | 60 e 61 · U: L |
| 69 | Place ID e link do GBP | texto | Novo (Site: 0 links para o GBP) | 36 · U: E (vínculo validado pela rede) |
| 70 | Domínio próprio | domínio + DNS | GBP: alguns já apontam para domínio próprio (ex. Alto da Lapa) | 70 · U: E (pedido) |
| 71 | Scripts de head, body start, body end | código | AGDM "Confs. Site" (GTM por unidade) | 68 · U: O |
| 72 | Script de conclusão e ID do formulário de agendamento | código e texto | AGDM "Agendamento Conclusão" e "Formulário ID" (vazios no exemplo) | 69 · U: O |

## Rev. 3.2 (21/11/2026): dados novos das specs 002 e 003
- A aba "Tratamentos" vira "Procedimentos e preços" (`oferta_unidade`): ativo, duração local, preço, visibilidade, comprável online, texto local, destaque.
- Dados novos da unidade: conta de recebimento (subconta do gateway, status KYC), política de agenda (remarcação, no-show), NFS-e (emissor, município), raio padrão de alcance.
- Seção "O que a rede liberou" na ficha (liberações, limites, cotas).
- Aba SEO ganha a seção "Tags e medição": GA4 próprio (ID de medição), `api_secret` (segredo, nunca exibido depois de salvo), meta tag do Search Console, Google Ads, Meta, TikTok; cada campo com status de aprovação e consentimento exigido.
## Lacunas encontradas no cruzamento
1. O AGDM não tem coordenadas, franqueado, destinatário de leads, equipe, FAQ, avaliações nem title, canonical e schema por unidade. Tudo isso é novo na plataforma.
2. O campo "CRO" do AGDM vem do modelo odontológico (Sorridents). Na Gio ele vira "responsável técnico, conselho e registro", com regra por tratamento.
3. O horário do AGDM é texto livre ("Segunda a sexta"). Precisa virar estruturado por dia para gerar schema e casar com o GBP.
4. As restrições de horário do AGDM são globais (feriados nacionais). A plataforma precisa de exceções por unidade, mantendo a lista nacional como base.
5. GBP e ficha divergem em bairro, telefone e site em parte da amostra. Decisão do Osmar: o GBP é da unidade. A plataforma compara e alerta lado a lado (US7) e a Wiki ensina a corrigir no GBP.
6. Meta keywords não tem uso em busca e sai do modelo.
