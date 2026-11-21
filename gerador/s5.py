from base import *
random.seed(3)
A=DEMO['altodalapa']
def cabec(t,p,dir=''): return f'<div class="cab"><div><h1>{t}</h1><p>{p}</p></div><div class="dir">{dir}</div></div>'
def F(ativo,cont,**k): return app('franq',ativo,cont,**k)
# ---------- 24 DASHBOARD DO FRANQUEADO ----------
dias=[f'{d:02d}/11' for d in range(1,22)]
ld=[1,2,3,1,2,2,0,3,2,1,2,3,1,2,3,2,3,2,3,2,1]
ag=[max(0,v-1+random.randint(0,1)) for v in ld]
cont=f'''
<div class="hero" style="margin-bottom:16px;background:var(--grad-franq)"><div style="position:relative;display:flex;align-items:center;gap:20px">
 <div><div style="font-size:14px">Bom dia, Renata</div><h1 style="font-size:24px;font-weight:600;margin:4px 0">Sua unidade está em 4º lugar no índice de conversão da rede</h1><div style="font-size:14px">Índice 90 de 100, o mesmo usado no painel da rede. Faltam 3 itens para a página chegar a 100% de completude.</div></div>
 <a class="btn" href="{L('f-unidade')}" style="margin-left:auto;background:#fff;color:var(--vinho);border:0">Completar a página {i('chev',14)}</a></div></div>
<div class="cab" style="margin-bottom:12px"><div><h2 style="font-size:18px;font-weight:600">Resultados</h2></div><div class="dir">{periodo()}</div></div>
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">
 {kpi('inbox','Leads','41','<span class="up">+11%</span> vs. outubro')}{kpi('cal','Agendados','26','63% dos leads')}{kpi('check','Compareceram','17','fonte DocBiz')}{kpi('clock','1º contato (mediana)','9 min','meta da rede 15 min')}
</div>
<div class="g" style="grid-template-columns:1.5fr 1fr">
 <div class="card"><div class="hd"><h3>Leads e agendamentos por dia</h3><div class="leg" style="margin-left:12px"><span><i style="background:#86106b"></i>Leads</span><span><i style="background:#e5559f"></i>Agendados</span></div></div>{area([ld,ag],['#86106b','#e5559f'],w=640,h=220,labels=dias,ymax=4)}</div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('bell',16)} Precisa da sua atenção</h3><a class="lk" href="{L('f-notif')}" style="margin-left:auto;font-size:13px">Ver todas</a></div>
   <div class="lista-i">
    <a class="it" href="{L('leads')}"><div class="ic l">{i('inbox',15)}</div><div style="flex:1"><b>9 leads em aberto</b><div class="meta">2 sem primeiro contato</div></div>{i('chev',14)}</a>
    <a class="it" href="{L('f-notif')}"><div class="ic a">{i('edit',15)}</div><div style="flex:1"><b>A rede alterou o horário de sábado</b><div class="meta">9h às 15h para 9h às 17h · pode contestar até 28/11</div></div>{i('chev',14)}</a>
    <a class="it" href="{L('ajuda')}"><div class="ic r">{i('google',15)}</div><div style="flex:1"><b>Seu perfil do Google tem outro telefone</b><div class="meta">Corrija no Google. Veja o passo a passo.</div></div>{i('chev',14)}</a>
    <a class="it" href="{L('f-faq')}"><div class="ic v">{i('check',15)}</div><div style="flex:1"><b>Pergunta "estacionamento" revisada</b><div class="meta">a rede revisou ontem às 18:20, sem ajustes</div></div>{i('chev',14)}</a>
   </div></div>
  <div class="card"><div class="hd"><h3>Completude da página</h3><b class="pop" style="margin-left:auto;font-size:20px">90%</b></div><span class="barra" style="width:100%;height:8px"><i style="width:90%"></i></span>
   <div class="meta" style="margin-top:8px">Faltam: 6 tratamentos do catálogo, 3 perguntas locais, link da página no Google.</div></div>
 </div>
</div>'''
salvar(ARQ['f-inicio'],pagina('Início',F('f-inicio',cont)))

# ---------- 25 MINHA UNIDADE ----------
trat=[('Depilação a laser',True),('Limpeza de pele',True),('Ultraformer',True),('Peeling',True),('Criolipólise',True),('Microagulhamento',True),('Toxina',False),('Preenchimento',False),('Drenagem',False),('Carboxiterapia',False),('Radiofrequência',False),('Laser lavieen',False)]
cont=cabec('Minha unidade','O que aparece na página e no Google da sua unidade. Cada campo mostra quem pode mudar.',f'<a class="btn" href="{L("lpB")}">{i("eye",14)} Ver página</a><span class="btn p">{i("check",14)} Salvar</span>')+f'''
<div class="tabs"><a class="on">Dados e contato</a><a>Horários</a><a>Tratamentos <span class="n">6 de 12</span></a><a href="{L('f-fotos')}">Fotos <span class="n">8</span></a><a href="{L('f-faq')}">Perguntas frequentes</a><a href="{L('f-tpl')}">Landing pages</a><a>Equipe</a></div>
<div class="leg" style="margin-bottom:14px"><span><span class="pill e">{i('edit',11)} Editável</span> muda na hora</span><span><span class="pill ea">{i('shield',11)} Com aprovação</span> a rede revisa em até 48 h</span><span><span class="pill t">{i('lock',11)} Rede</span> só a rede altera</span></div>
<div class="g" style="grid-template-columns:1fr 360px">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Contato</h3></div><div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:14px">{campo('Nome público',A['nome'],'T')}{campo('Telefone fixo',A['tel'],'EA','Troca aprovada pelo SEO','phone')}{campo('WhatsApp',A['wa'],'E','','wa')}
  {campo('E-mail',A['email'],'E','','mail')}{campo('Instagram',A['ig'],'E')}{campo('CNPJ',A['cnpj'],'T')}</div></div>
  <div class="card"><div class="hd"><h3>Endereço</h3><a class="lk" href="{L('suporte')}" style="margin-left:auto;font-size:13px">Mudou de endereço? Abra um chamado</a></div><div class="g" style="grid-template-columns:1fr 2fr 1fr;gap:14px">{campo('CEP',A['cep'],'T')}{campo('Endereço',A['end'],'T')}{campo('Bairro',A['bairro'],'T')}
  {campo('Ponto de referência','Ao lado da praça','E','Publicado hoje às 08:10; a rede revisa depois')}{campo('Coordenadas','definidas pelo endereço','T')}{campo('Cidade/UF',f"{A['cidade']}/{A['uf']}",'T')}</div></div>
  <div class="card"><div class="hd"><h3>Tratamentos</h3><span class="sub" style="margin-left:auto">6 publicados de 12 no catálogo da rede</span></div>
   <div style="display:flex;flex-wrap:wrap;gap:8px">'''+''.join(f'<span class="chip{" on" if on else ""}">{i("check",12) if on else i("plus",12)} {t}</span>' for t,on in trat)+f'''</div></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('google',15)} Seu perfil do Google</h3></div><p class="meta" style="margin:-6px 0 10px">O perfil é seu e você cuida dele no Google. Comparamos com esta ficha todo dia.</p>
   <div class="lista-i" style="font-size:13px"><div class="it"><span class="pill v">igual</span><span>Nome e endereço</span></div><div class="it"><span class="pill a">diverge</span><span>Telefone: Google mostra (11) 90000-0009</span></div><div class="it"><span class="pill r">falta</span><span>Link da página oficial</span></div></div>
   <a class="btn s" href="{L('ajuda')}" style="margin-top:10px">{i('book',12)} Como corrigir no Google</a></div>
  <div class="card"><div class="hd"><h3>Dados estruturados</h3><span class="pill t" style="margin-left:auto">{i('lock',11)} Rede</span></div><p class="meta">A rede define o schema e o SEO técnico da sua página. Seus dados de contato, horários e FAQ alimentam esse schema automaticamente.</p></div>
 </div>
</div>'''
salvar(ARQ['f-unidade'],pagina('Minha unidade',F('f-unidade',cont)))

# ---------- 26 FOTOS ----------
fotos=[('fachada','Fachada','Publicada'),('recepcao','Recepção','Publicada'),('sala-laser','Sala de laser','Publicada'),('sala-facial','Sala de estética facial','Publicada'),('espera','Sala de espera','Publicada'),('equipe','Equipe em atendimento','Revisão da rede')]
cont=cabec('Fotos','Fotos reais da unidade. A primeira é a capa da página e a sugestão para o Google.',f'<span class="btn p">{i("plus",14)} Enviar fotos</span>')+f'''
<div class="g" style="grid-template-columns:1fr 330px">
 <div class="card"><div class="hd"><h3>Galeria da página</h3><span class="sub">6 de 8 recomendadas · arraste para ordenar</span></div>
  <div class="g" style="grid-template-columns:repeat(4,1fr);gap:12px">'''+''.join(f'<div style="border:1px solid var(--linha);border-radius:12px;overflow:hidden"><div style="height:140px;background:url(../assets/fotos/{f}.jpg) center/cover;position:relative">{"<span class=\"pill l\" style=\"position:absolute;left:8px;top:8px\">Capa</span>" if k==0 else ""}<span style="position:absolute;right:8px;top:8px;background:#fff;border-radius:8px;padding:4px;display:grid;color:var(--tinta-2)">{i("drag",14)}</span></div><div style="padding:10px"><b style="font-size:13px">{t}</b><div style="margin-top:4px"><span class="pill {"v" if s=="Publicada" else "a"}">{s}</span></div></div></div>' for k,(f,t,s) in enumerate(fotos))+''.join(f'<div style="border:2px dashed var(--linha-forte);border-radius:12px;display:grid;place-items:center;min-height:200px;color:var(--tinta-2);text-align:center;padding:12px"><div>{i("plus",22)}<div style="font-weight:600;margin-top:6px">{t}</div><div class="meta">sugestão</div></div></div>' for t in ['Equipamento','Detalhe do atendimento'])+f'''</div></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Boas práticas</h3></div><div class="lista-i" style="font-size:13px">'''+''.join(f'<div class="it">{i("check",14)}<span>{t}</span></div>' for t in ['Luz natural, sem filtro','Horizontal, no mínimo 1200 px','Sem rosto de cliente sem autorização','Sem texto ou preço na imagem','Fotos diferentes entre si'])+f'''</div></div>
  <div class="aviso l"><div>{i('shield',16)}</div><div style="font-size:13px">Fotos publicam na hora e a rede revisa depois. Foto com profissional da equipe precisa do consentimento dela; fotos de antes e depois passam por aprovação.</div></div>
 </div>
</div>'''
salvar(ARQ['f-fotos'],pagina('Fotos',F('f-fotos',cont)))

# ---------- 27 FAQ ----------
base=[('Quanto tempo dura a sessão de laser?','Depende da área: de 10 a 40 minutos.'),('Precisa raspar antes da sessão?','Sim, de 24 a 48 horas antes. A equipe orienta na avaliação.')]
loc=[('A unidade tem estacionamento?','Publicada','v'),('Atendem aos sábados?','Publicada','v'),('Como chegar de metrô?','Revisão da rede','a'),('Aceitam cartão de crédito?','Rascunho','z')]
cont=cabec('Perguntas frequentes','Perguntas da rede (fixas) e da sua unidade. Viram FAQ na página e no schema.',f'<span class="btn p">{i("plus",14)} Nova pergunta local</span>')+f'''
<div class="g" style="grid-template-columns:1fr 1fr">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Da sua unidade</h3><span class="pill e" style="margin-left:auto">{i('edit',11)} publica na hora · até 8</span></div>
   <div class="lista-i">'''+''.join(f'<div class="it"><span style="color:var(--tinta-3)">{i("drag",16)}</span><b style="flex:1">{p}</b><span class="pill {c}">{s}</span>{i("edit",15)}</div>' for p,s,c in loc)+f'''</div></div>
  <div class="card" style="border:2px solid var(--magenta)"><div class="hd"><h3>Editando: Como chegar de metrô?</h3></div>
   {campo('Pergunta','Como chegar de metrô?','E')}<div style="height:10px"></div>{campo('Resposta','A estação mais próxima fica a 12 minutos a pé. Saia pela rua principal e siga até a praça.','E','Sem preço e sem promessa de resultado. Até 300 caracteres.')}
   <div style="display:flex;gap:8px;margin-top:12px"><span class="btn p">Publicar</span><span class="meta" style="align-self:center">O SEO da rede revisa depois</span><span class="btn ghost">Cancelar</span></div></div>
  <div class="card"><div class="hd"><h3>Da rede</h3><span class="pill t" style="margin-left:auto">{i('lock',11)} fixas</span></div>
   <div class="lista-i">'''+''.join(f'<div class="it"><span style="flex:1"><b>{p}</b></span>{i("lock",14)}</div>' for p,_ in base)+f'''</div></div>
 </div>
 <div class="card"><div class="hd"><h3>{i('eye',16)} Prévia na página</h3><span class="sub" style="margin-left:auto">FAQPage válido</span></div>
  <div style="border:1px solid var(--linha);border-radius:14px;padding:6px 16px">'''+''.join(f'<div style="display:flex;align-items:center;gap:12px;min-height:56px;border-bottom:1px solid var(--linha)"><b style="flex:1">{p}</b><span style="width:40px;height:40px;display:grid;place-items:center;color:var(--vinho);{"transform:rotate(180deg)" if k==0 else ""}">{i("chevd",18)}</span></div>'+(f'<p class="muted" style="padding:10px 0 14px">{base[0][1]}</p>' if k==0 else '') for k,p in enumerate([b[0] for b in base]+['A unidade tem estacionamento?','Atendem aos sábados?']))+f'''</div>
  <p class="meta" style="margin-top:10px">Ícone de seta com área de toque de 40 px. A primeira pergunta aparece aberta.</p></div>
</div>'''
salvar(ARQ['f-faq'],pagina('Perguntas frequentes',F('f-faq',cont)))

# ---------- 28 TEMPLATES (escolha do franqueado) ----------
tp=[('A','Clássico','Formulário logo no topo. Bom para quem investe em anúncio.','37-landing-a-desktop.png','2,4%',False),('B','Vitrine','Fotos, equipe e avaliações antes do formulário.','39-landing-b-desktop.png','2,1%',True),('C','Autoridade local','Mapa de bairros atendidos e FAQ local longo.','41-landing-c-desktop.png','1,9%',False)]
cont=cabec('Página da unidade','Escolha o modelo da sua página. Trocar de modelo passa pela aprovação da rede.',f'<a class="btn" href="{L("f-ab")}">{i("layout",14)} Comparar A x B</a><a class="btn p" href="{L("f-editor")}">{i("edit",14)} Editar página atual</a>')+f'''
<div class="tabs"><a class="on">Modelo</a><a href="{L('f-editor')}">Conteúdo</a><a>Landing pages <span class="n">4</span></a><a href="{L('f-dominio')}">Domínio</a></div>
<div class="g" style="grid-template-columns:repeat(3,1fr)">'''+''.join(f'<div class="card" style="padding:0;overflow:hidden;{"border:2px solid var(--magenta)" if cur else ""}"><div style="height:300px;background:#efe7f2 url(../png/{img}) top center/cover"></div><div style="padding:16px"><div style="display:flex;align-items:center;gap:8px"><b class="pop" style="font-size:17px">Modelo {k} · {n}</b>{"<span class=\"pill l\" style=\"margin-left:auto\">em uso</span>" if cur else ""}</div><p class="muted" style="margin-top:4px">{d}</p><div class="meta" style="margin-top:8px">Conversão média na rede: <b style="color:var(--tinta)">{cv}</b> (visita para lead, 30 dias)</div><div style="display:flex;gap:8px;margin-top:12px"><a class="btn s" href="{L("lp"+k)}">{i("monitor",12)} Ver exemplo</a>{"" if cur else "<span class=\"btn s p\">Pedir troca</span>"}</div></div></div>' for k,n,d,img,cv,cur in tp)+'''</div>'''
salvar(ARQ['f-tpl'],pagina('Página da unidade',F('f-tpl',cont)))

# ---------- 29 COMPARATIVO A x B ----------
lin=[('Formulário','Logo no topo','Depois das fotos e avaliações'),('Primeira dobra','Formulário completo','Foto da fachada, nota e botão Agendar'),('Fotos','3 fotos','Galeria com 8 fotos'),('Equipe','Não aparece','Seção com a equipe'),('Indicado para','Unidades com anúncio forte','Unidades com boas fotos e avaliações'),('Conversão média na rede','2,4%','2,1%'),('Tempo médio na página','1 min 12 s','2 min 31 s')]
cont=cabec('Comparar modelos A e B','Lado a lado, no computador e no celular. Dados da rede nos últimos 30 dias.',f'<a class="btn" href="{L("f-tpl")}">{i("chev",14)} Voltar</a><span class="btn p">Pedir troca para A</span>')+f'''
<div class="g" style="grid-template-columns:1fr 1fr;margin-bottom:16px">'''+''.join(f'<div class="card"><div class="hd"><h3>Modelo {k} · {n}</h3>{"<span class=\"pill l\" style=\"margin-left:auto\">em uso</span>" if k=="B" else ""}</div><div style="display:grid;grid-template-columns:1fr 130px;gap:12px;align-items:start"><div style="height:330px;border-radius:10px;border:1px solid var(--linha);background:#efe7f2 url(../png/{d}) top center/cover"></div><div style="height:330px;border-radius:18px;border:5px solid #24082c;background:#efe7f2 url(../png/{m}) top center/cover"></div></div></div>' for k,n,d,m in [('A','Clássico','37-landing-a-desktop.png','38-landing-a-mobile.png'),('B','Vitrine','39-landing-b-desktop.png','40-landing-b-mobile.png')])+f'''</div>
<div class="card" style="padding:0"><table class="t"><thead><tr><th></th><th>Modelo A · Clássico</th><th>Modelo B · Vitrine</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>' for a,b,c in lin)+'''</tbody></table></div>'''
salvar(ARQ['f-ab'],pagina('Comparar modelos',F('f-tpl',cont)))

# ---------- 30 EDITOR (prévia é a página B real) ----------
blocos=[('Topo com foto da fachada','T'),('Nota do Google e botão Agendar','T'),('Galeria de fotos','E'),('Sobre a unidade','E'),('Tratamentos','E'),('Equipe','E'),('Avaliações','T'),('Perguntas frequentes','E'),('Formulário de agendamento','T'),('Como chegar','T')]
nm={'T':('t','Rede'),'E':('e','Editável'),'EA':('ea','Aprovação')}
cont=cabec('Editar página','A prévia ao lado é a página real do modelo B da sua unidade.',f'<span class="sw"><span class="on">{i("monitor",13)} Computador</span><span>{i("phone2",13)} Celular</span></span><span class="btn">Salvar rascunho</span><span class="btn p">{i("check",14)} Publicar</span>')+f'''
<div class="g" style="grid-template-columns:330px 1fr">
 <div class="card" style="padding:12px"><div class="meta" style="font-weight:600;text-transform:uppercase;letter-spacing:.06em;padding:6px 8px">Blocos da página</div>'''+''.join(f'<div style="display:flex;align-items:center;gap:10px;padding:10px 8px;border-radius:10px;{"background:var(--lilas-100)" if t=="Galeria de fotos" else ""}"><span style="color:var(--tinta-3)">{i("drag",16)}</span><span style="flex:1;font-weight:500">{t}</span><span class="pill {nm[e][0]}">{nm[e][1]}</span></div>' for t,e in blocos)+f'''
  <div class="sep"></div><div class="meta" style="padding:0 8px">Blocos da rede ficam na ordem definida pelo modelo. Você reordena só os editáveis.</div>
  <div class="aviso a" style="margin-top:12px"><div>{i('zap',16)}</div><div style="font-size:13px"><b>Lighthouse celular: 93</b><br>A foto "Equipe em atendimento" pesa 410 KB. Ao publicar, ela é comprimida para cerca de 160 KB e a página fica em 780 KB no total (meta da rede: 90 ou mais).</div></div></div>
 <div class="card" style="padding:0;overflow:hidden;background:#e9e1ee">
  <div style="display:flex;gap:6px;align-items:center;padding:10px 14px;background:#fff;border-bottom:1px solid var(--linha)"><span style="width:10px;height:10px;border-radius:50%;background:#e6dde9"></span><span style="width:10px;height:10px;border-radius:50%;background:#e6dde9"></span><span style="width:10px;height:10px;border-radius:50%;background:#e6dde9"></span><span class="meta" style="margin-left:12px">{A['dom']}</span></div>
  <div style="height:760px;overflow:hidden;position:relative" data-sem-contraste><iframe src="{L('lpB')}" style="width:1440px;height:1900px;border:0;transform:scale(.538);transform-origin:0 0;pointer-events:none" title="Prévia"></iframe></div>
 </div>
</div>'''
salvar(ARQ['f-editor'],pagina('Editar página',F('f-tpl',cont)))

# ---------- 31 DOMÍNIO ----------
cont=cabec('Domínio próprio','Use um endereço próprio para a página da unidade. A rede cuida do certificado e do redirecionamento.',f'<span class="btn p">{i("refresh",14)} Verificar de novo</span>')+f'''
<div class="g" style="grid-template-columns:1fr 1fr">
 <div class="card"><div class="hd"><h3>Configuração atual</h3><span class="pill v" style="margin-left:auto">{i('check',11)} Ativo</span></div>
  {campo('Domínio',A['dom'],'EA','Troca de domínio passa pela rede (canônica e redirecionamentos).','globe')}
  <div style="height:14px"></div>
  <table class="t" style="font-size:13px"><thead><tr><th>Tipo</th><th>Nome</th><th>Valor</th><th>Situação</th></tr></thead><tbody>
  <tr><td>A</td><td>@</td><td><b>{IP_DEMO}</b></td><td><span class="pill v">ok</span></td></tr>
  <tr><td>CNAME</td><td>www</td><td>paginas.exemplo.com.br</td><td><span class="pill v">ok</span></td></tr>
  <tr><td>TXT</td><td>@</td><td>verificacao-gio=7f3a…</td><td><span class="pill v">ok</span></td></tr></tbody></table>
  <div class="lista-i" style="font-size:13px;margin-top:10px"><div class="it">{i('lock',14)} Certificado HTTPS válido até 19/02/2027</div><div class="it">{i('link',14)} /unidade/altodalapa/ redireciona para o domínio (301)</div></div></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="meta" style="font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-bottom:10px">Estado de falha (exemplo)</div>
   <div class="aviso r"><div>{i('alert',18)}</div><div><b>O domínio não aponta para a página</b><div style="font-size:13px;margin-top:4px">O registro A está com 198.51.100.24. Troque para <b>{IP_DEMO}</b> no painel onde você comprou o domínio. Depois da troca, a verificação pode levar até 24 h.</div><div style="display:flex;gap:8px;margin-top:10px"><a class="btn s" href="{L('ajuda')}">{i('book',12)} Passo a passo</a><a class="btn s" href="{L('suporte')}">Falar com a rede</a></div></div></div></div>
  <div class="card"><div class="hd"><h3>{i('key',16)} Acesso da rede ao Analytics e ao Search Console</h3><span class="pill a" style="margin-left:auto">1 de 2</span></div>
   <p class="meta" style="margin-bottom:10px">Com domínio próprio, a rede precisa receber acesso ao Analytics e ao Search Console do domínio para coletar os dados junto com os seus. O domínio só fica como endereço principal depois dos dois acessos.</p>
   <div class="lista-i" style="font-size:13px">
    <div class="it"><span class="ic v">{i('check',15)}</span><div style="flex:1"><b>Google Analytics do domínio</b><div class="meta">Leitura concedida para medicao@rede.exemplo.com.br em 18/11</div></div><span class="pill v">concedido</span></div>
    <div class="it"><span class="ic a">{i('clock',15)}</span><div style="flex:1"><b>Search Console do domínio</b><div class="meta">Adicione medicao@rede.exemplo.com.br como usuário completo</div></div><a class="btn s" href="{L('f-tags')}">Ver como</a></div></div>
   <p class="meta" style="margin-top:10px">Publicar a página e conectar o domínio são ações separadas. O botão Publicar fica no editor.</p></div>
 </div>
</div>'''
salvar(ARQ['f-dominio'],pagina('Domínio',F('f-dominio',cont)))

# ---------- 32 UNIDADE NOVA (estado vazio) ----------
NOVA=('NV','GiO Unidade Nova','Campinas/SP · em implantação')
passos=[('Definir senha e ativar 2FA',True,'feito no primeiro acesso'),('Conferir dados enviados pela rede',True,'endereço, CNPJ e horários'),('Convidar sua equipe',False,'gerente e recepção, nos perfis liberados pela rede'),('Enviar 8 fotos reais',False,'fachada, recepção, salas'),('Escrever o texto Sobre a unidade',False,'publica na hora; a rede revisa depois'),('Reivindicar o perfil no Google',False,'o perfil é seu; o guia mostra como'),('Publicar a página',False,'libera quando a completude passar de 70%')]
cont=f'''
<div class="hero" style="margin-bottom:16px;background:var(--grad-franq)"><div style="position:relative"><div style="font-size:14px">Boas-vindas, Lívia</div><h1 style="font-size:24px;font-weight:600;margin:4px 0">Sua unidade foi criada pela rede. Vamos deixar tudo pronto para os primeiros clientes.</h1><div style="font-size:14px">Você entrou como admin da unidade. Siga os passos abaixo; a página só vai ao ar quando estiver completa.</div></div></div>
<div class="g" style="grid-template-columns:1.3fr 1fr">
 <div class="card"><div class="hd"><h3>Primeiros passos</h3><span class="pill l" style="margin-left:auto">2 de 7</span></div><span class="barra" style="width:100%;height:8px;margin-bottom:8px"><i style="width:29%"></i></span>
  <div class="lista-i">'''+''.join(f'<div class="it"><span class="cx{" on" if ok else ""}"></span><div style="flex:1"><b style="{"color:var(--tinta-3)" if ok else ""}">{t}</b><div class="meta">{d}</div></div>{"" if ok else "<span class=\"btn s\">Começar</span>"}</div>' for t,ok,d in passos)+f'''</div></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('users',16)} Convidar equipe</h3></div>
   {campo('E-mail','nome@exemplo.com.br','','','mail')}<div style="height:10px"></div>
   <div class="campo"><label>Perfil</label><div class="in">Gerente da unidade {i('chevd',13)}</div><div class="ajuda">Liberados pela rede: Gerente da unidade, Recepção.</div></div>
   <span class="btn p" style="width:100%;margin-top:12px">{i('send',14)} Enviar convite</span></div>
  <div class="card vazio" style="padding:26px"><div class="ilu">{i('chart',32)}</div><b style="font-size:16px">Ainda sem números</b><p class="meta" style="margin-top:4px">Leads, agendamentos e o índice de conversão aparecem aqui depois que a página for publicada.</p></div>
 </div>
</div>'''
salvar(ARQ['f-nova'],pagina('Unidade nova',F('f-inicio',cont,ctx=NOVA,sem_badges=True)))

# ---------- 33 LEADS NO PRIMEIRO DIA (quadro vazio) ----------
cols=['Novo','Em contato','Agendado','Compareceu','Não converteu']
cont=cabec('Leads','Quadro da sua unidade. Os leads chegam aqui pela página, pelo call center e pelo WhatsApp.',f'<span class="sw"><span class="on">Quadro</span><span>Lista</span></span>')+f'''
<div class="card vazio" style="margin-bottom:16px;display:flex;gap:24px;align-items:center;text-align:left;padding:24px 28px"><div class="ilu" style="margin:0">{i('inbox',36)}</div><div style="flex:1"><b style="font-size:18px">Nenhum lead ainda, e tudo bem</b><p class="muted" style="margin-top:4px">Assim que a página for publicada, cada pedido de agendamento aparece na coluna Novo e você recebe um aviso no WhatsApp da unidade. A meta da rede é o primeiro contato em até 15 minutos.</p></div><div style="display:flex;flex-direction:column;gap:8px"><a class="btn p" href="{L('f-nova')}">Ver primeiros passos</a><a class="btn" href="{L('ajuda')}">{i('video',14)} Como atender um lead (2 min)</a></div></div>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px">'''+''.join(f'<div style="background:#f1ebf4;border-radius:14px;padding:10px;min-height:360px"><div style="display:flex;align-items:center;padding:4px 4px 10px"><b>{c}</b><b style="margin-left:auto" class="muted">0</b></div><div style="border:2px dashed var(--linha-forte);border-radius:12px;height:110px;display:grid;place-items:center;color:var(--tinta-2);font-size:13px;text-align:center;padding:10px">{"Leads novos chegam aqui" if k==0 else "Arraste um lead para cá"}</div></div>' for k,c in enumerate(cols))+'</div>'
salvar(ARQ['f-leads'],pagina('Leads, primeiro dia',F('leads',cont,ctx=NOVA,sem_badges=True)))

# ---------- 34 NOTIFICAÇÕES ----------
nt=[('a','edit','A rede alterou o horário de sábado','Ingrid N. (Marketing da rede) · hoje 08:41','Antes: 9h às 15h · Depois: 9h às 17h · Motivo: campanha de fim de ano, de 22/11 a 20/12.',True),
('v','check','Pergunta "estacionamento" revisada pela rede, sem ajustes','Rede · ontem 18:20','',False),
('r','google','Seu perfil do Google mostra outro telefone','Comparação diária · ontem 07:00','Google: (11) 90000-0009 · Ficha: (11) 90000-0000. Corrija no próprio Google.',False),
('l','sparkle','Página de serviço trouxe 11 leads em 30 dias','Relatório inteligente · segunda 08:00','',False),
('a','image','Foto "Equipe em atendimento" em revisão','Rede · segunda 15:12','Já publicada. A rede confere o consentimento da profissional.',False)]
cont=cabec('Notificações','Avisos da rede, aprovações, comparação com o Google e insights.',f'<span class="btn">{i("gear",14)} Preferências</span><span class="btn">Marcar todas como lidas</span>')+f'''
<div class="tabs"><a class="on">Todas <span class="n">5</span></a><a>Alterações da rede <span class="n">1</span></a><a>Aprovações</a><a>Google</a><a>Insights</a></div>
<div class="g" style="grid-template-columns:1fr 360px">
 <div class="card" style="padding:0">'''+''.join(f'<div style="display:flex;gap:14px;padding:16px 18px;border-bottom:1px solid var(--linha);{"background:#fff8ec" if dest else ""}"><div class="ic {c}">{i(ic,16)}</div><div style="flex:1"><b>{t}</b><div class="meta">{q}</div>{f"<p style=\"margin-top:6px;color:var(--tinta-2)\">{d}</p>" if d else ""}{"<div style=\"display:flex;gap:8px;margin-top:10px\"><span class=\"btn s\">Ver na ficha</span><span class=\"btn s perigo\">Contestar</span><span class=\"meta\" style=\"align-self:center\">até 28/11</span></div>" if dest else ""}</div>{"<span style=\"width:9px;height:9px;border-radius:50%;background:var(--magenta);margin-top:6px\"></span>" if k<3 else ""}</div>' for k,(c,ic,t,q,d,dest) in enumerate(nt))+f'''</div>
 <div class="card" style="border:2px solid var(--magenta)"><div class="hd"><h3>Contestar alteração</h3></div>
  <p class="meta" style="margin-bottom:10px">A alteração continua valendo enquanto a rede analisa. A resposta chega aqui e por e-mail.</p>
  <div class="campo"><label>Por que você discorda?</label><div class="in" style="min-height:90px;align-items:flex-start">Aos sábados só temos uma profissional depois das 15h. Podemos estender só até 16h?</div></div>
  <span class="btn p" style="width:100%;margin-top:12px">Enviar contestação</span></div>
</div>'''
salvar(ARQ['f-notif'],pagina('Notificações',F('f-notif',cont)))
print('s5 ok')
