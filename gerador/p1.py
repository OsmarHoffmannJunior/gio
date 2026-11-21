from base import *
# 01 LOGIN
corpo=f'''<div style="display:grid;grid-template-columns:1fr 560px;min-height:900px;width:1440px">
<div style="background:var(--grad);position:relative;overflow:hidden;color:#fff;padding:56px 64px;display:flex;flex-direction:column">
 <div style="position:absolute;inset:0;background:url(../assets/fachada.jpg) center/cover;opacity:.16;mix-blend-mode:luminosity"></div>
 <div style="position:absolute;right:-140px;top:-140px;width:520px;height:520px;border-radius:50%;border:1px solid rgba(255,255,255,.18)"></div>
 <div style="position:absolute;right:-60px;top:-60px;width:360px;height:360px;border-radius:50%;border:1px solid rgba(255,255,255,.14)"></div>
 <img src="../assets/logo-gio-branco.png" style="height:64px;width:auto;align-self:flex-start;position:relative">
 <div style="margin-top:auto;position:relative;max-width:620px">
  <span class="pill" style="background:rgba(255,255,255,.16);color:#fff">{i('sparkle',12)} Plataforma de Unidades</span>
  <h1 style="font-size:44px;line-height:1.1;font-weight:600;margin:18px 0 14px">Cada unidade com página própria, leads no lugar certo e a rede inteira em um painel.</h1>
  <p style="font-size:16px;opacity:.86;max-width:540px">Franqueadora, franqueados, call center e agências trabalhando sobre os mesmos dados, cada um no seu escopo.</p>
  <div style="display:flex;gap:28px;margin-top:34px">
   <div><div class="pop" style="font-size:28px;font-weight:600">130</div><div style="opacity:.8">unidades</div></div>
   <div><div class="pop" style="font-size:28px;font-weight:600">16</div><div style="opacity:.8">estados</div></div>
   <div><div class="pop" style="font-size:28px;font-weight:600">1</div><div style="opacity:.8">painel para todos</div></div>
  </div>
 </div>
</div>
<div style="background:#fff;padding:72px 64px;display:flex;flex-direction:column;justify-content:center">
 <h2 style="font-size:26px;font-weight:600">Entrar</h2><p class="muted" style="margin:6px 0 26px">Use o e-mail cadastrado pela rede. Não tem acesso? Fale com o suporte da franqueadora.</p>
 <div class="sw" style="margin-bottom:22px;width:100%;display:grid;grid-template-columns:1fr 1fr 1fr"><span class="on" style="text-align:center">Franqueado</span><span style="text-align:center">Rede Gio</span><span style="text-align:center">Parceiro</span></div>
 <div class="campo" style="margin-bottom:14px"><label>E-mail</label><div class="in">{i('users',15)} renata.f@exemplo.com.br</div></div>
 <div class="campo" style="margin-bottom:8px"><label>Senha</label><div class="in">{i('lock',15)} ••••••••••<span style="margin-left:auto">{i('eye',15)}</span></div></div>
 <div style="display:flex;justify-content:space-between;margin:6px 0 22px;font-size:12px"><span class="muted">{i('check',13)} Manter conectado neste aparelho</span><span style="color:var(--vinho);font-weight:600">Esqueci a senha</span></div>
 <span class="btn p" style="justify-content:center;padding:13px">Entrar no portal {i('chev',14)}</span>
 <div style="display:flex;align-items:center;gap:12px;margin:22px 0;color:var(--tinta-3);font-size:12px"><span style="flex:1;height:1px;background:var(--linha)"></span>ou<span style="flex:1;height:1px;background:var(--linha)"></span></div>
 <span class="btn" style="justify-content:center;padding:12px">{i('google',16)} Entrar com conta Google da rede</span>
 <div class="card" style="margin-top:28px;background:var(--lilas-50);box-shadow:none;display:flex;gap:12px;align-items:flex-start">
  <div class="ic l">{i('shield',16)}</div><div><b>Verificação em duas etapas</b><div class="muted" style="font-size:12px">Obrigatória para Rede Gio e call center. Seus acessos e exportações ficam registrados na auditoria (LGPD).</div></div></div>
 <p class="muted" style="font-size:11px;margin-top:26px">Ao entrar você concorda com os Termos de Uso e a Política de Privacidade da rede.</p>
</div></div>'''
salvar('01-login',pagina('Login',corpo))

# 02 DASHBOARD REDE
dias=[f'{d:02d}/11' for d in range(1,22)]
leads=[118,131,125,140,152,98,87,144,151,160,149,171,120,102,166,174,180,169,188,140,121]
agend=[int(v*0.58+random.randint(-6,6)) for v in leads]
comp=[int(v*0.62+random.randint(-4,4)) for v in agend]
ranking=[('Batel · Curitiba',96,'+12'),('Cambuí · Campinas',93,'+8'),('Boulevard Tatuapé',91,'+5'),('Alto da Lapa · SP',90,'+3'),('Bom Fim · Porto Alegre',88,'+1')]
alerts=[('r','alert','17 unidades com GTM próprio','Conversões fora do padrão da rede'),('a','image','70 unidades sem foto','Completude média cai 18 pontos'),('a','pin','13 unidades sem coordenadas','Mapa e schema quebrados'),('r','link','3 GBPs apontam para outro site','Fora da URL canônica'),('a','clock','9 leads fora do SLA agora','Call center Sul e Nordeste')]
uf=[('SP',86),('MG',8),('GO',7),('PR',7),('RS',4),('DF',3),('SC',3),('BA',2)]
cont=f'''
<div class="cab"><div><h1>Visão geral da rede</h1><p>Leads, agendamentos e saúde das 130 unidades. Dados de exemplo, período de 01 a 21/11/2026.</p></div>
<div class="dir"><span class="sw"><span>Hoje</span><span>7 dias</span><span class="on">Mês</span><span>Trimestre</span></span><span class="btn">{i('filter',14)} Filtros <span class="pill l">2</span></span><span class="btn p">{i('down',14)} Exportar</span></div></div>
<div class="g" style="grid-template-columns:repeat(5,1fr);margin-bottom:16px">
 <div class="card kpi"><div class="l">{i('inbox',15)} Leads</div><div class="v">2.986</div><div class="d"><span class="up">+14,2%</span> vs. outubro</div></div>
 <div class="card kpi"><div class="l">{i('cal',15)} Agendados</div><div class="v">1.733</div><div class="d"><span class="up">+9,8%</span> · 58% dos leads</div></div>
 <div class="card kpi"><div class="l">{i('check',15)} Compareceram</div><div class="v">1.071</div><div class="d"><span class="up">+6,1%</span> · via DocBiz</div></div>
 <div class="card kpi"><div class="l">{i('clock',15)} 1º contato</div><div class="v">11 min</div><div class="d">mediana · meta 15 min</div></div>
 <div class="card kpi"><div class="l">{i('target',15)} Completude média</div><div class="v">64%</div><div class="d"><span class="down">72 unidades</span> abaixo de 70%</div></div>
</div>
<div class="g" style="grid-template-columns:1.65fr 1fr;margin-bottom:16px">
 <div class="card"><div class="hd"><h3>Funil diário da rede</h3><div class="leg" style="margin-left:14px"><span><i style="background:#4c1455"></i>Leads</span><span><i style="background:#b0197e"></i>Agendados</span><span><i style="background:#e5559f"></i>Compareceram</span></div><div class="dir"><span class="sw"><span class="on">Volume</span><span>Taxa</span></span></div></div>
 {area([leads,agend,comp],['#4c1455','#b0197e','#e5559f'],w=760,h=230,labels=dias)}</div>
 <div class="card"><div class="hd"><h3>Origem dos leads</h3><span class="sub" style="margin-left:auto">por canal (UTM)</span></div>
 <div style="display:flex;align-items:center;gap:18px">{donut([38,24,17,11,6,4],['#4c1455','#86106b','#b0197e','#e5559f','#f2a7cc','#d9c3e1'],tam=160,esp=22,centro='2.986',sub='leads')}
 <div class="lista-i" style="flex:1">'''+''.join(f'<div class="it" style="padding:6px 0"><i style="width:9px;height:9px;border-radius:3px;background:{c}"></i><span style="flex:1">{r}</span><b>{v}%</b></div>' for r,v,c in [('Google Ads',38,'#4c1455'),('Orgânico e GBP',24,'#86106b'),('Meta Ads',17,'#b0197e'),('Instagram orgânico',11,'#e5559f'),('Direto',6,'#f2a7cc'),('Parcerias',4,'#d9c3e1')])+f'''</div></div></div>
</div>
<div class="g" style="grid-template-columns:1fr 1fr 1.1fr">
 <div class="card"><div class="hd"><h3>Ranking de conversão</h3><span class="sub" style="margin-left:auto">índice 0 a 100</span></div>
 <div class="lista-i">'''+''.join(f'<div class="it"><span class="pop" style="width:20px;font-weight:600;color:var(--vinho)">{k+1}</span><div style="flex:1;min-width:0"><b class="trunc" style="display:block">{n}</b><span class="barra" style="width:100%;margin-top:5px"><i style="width:{v}%"></i></span></div><b style="width:28px;text-align:right">{v}</b><span class="up" style="width:30px;text-align:right;font-size:12px">{d}</span></div>' for k,(n,v,d) in enumerate(ranking))+f'''</div></div>
 <div class="card"><div class="hd"><h3>Unidades por estado</h3><span class="sub" style="margin-left:auto">ativas</span></div>{barras_h(uf,w=320,larg_rot=36,alt=27)}</div>
 <div class="card"><div class="hd"><h3>{i('alert',16)} Alertas da rede</h3><span class="pill r" style="margin-left:auto">5 abertos</span></div>
 <div class="lista-i">'''+''.join(f'<div class="it"><div class="ic {c}">{i(ic,15)}</div><div style="flex:1;min-width:0"><b class="trunc" style="display:block">{t}</b><span class="muted trunc" style="display:block;font-size:12px">{s}</span></div>{i("chev",14)}</div>' for c,ic,t,s in alerts)+'''</div></div>
</div>'''
salvar('02-admin-dashboard-rede',pagina('Dashboard da rede',app('admin','rede',cont)))

# 03 TABELA UNIDADES
amostra=[u for u in UNID if u['url_site'] in ['altodalapa','curitiba','campinas-cambui','boulevardtatuape','porto-alegre-bom-fim','ribeirao-preto-centro','aldeota','asa-sul','salvador','montes-claros','vila-madalena','londrina','go-catalao-centro','ipiranga']]
ordem=['altodalapa','curitiba','campinas-cambui','boulevardtatuape','porto-alegre-bom-fim','ribeirao-preto-centro','aldeota','asa-sul','salvador','vila-madalena','londrina','montes-claros','ipiranga','go-catalao-centro']
amostra.sort(key=lambda u: ordem.index(u['url_site']))
info={'altodalapa':(90,'B','Próprio','4,9',41,'v'),'curitiba':(96,'A','Próprio','4,8',63,'v'),'campinas-cambui':(93,'A','Ficha','4,9',58,'v'),'boulevardtatuape':(91,'C','Ficha','4,7',49,'v'),
'porto-alegre-bom-fim':(81,'A','Ficha','4,8',37,'v'),'ribeirao-preto-centro':(78,'B','Ficha','4,9',33,'a'),'aldeota':(74,'A','Ficha','4,9',29,'a'),'asa-sul':(69,'C','Ficha','4,6',31,'a'),
'salvador':(62,'A','Ficha','4,5',22,'a'),'vila-madalena':(58,'A','Ficha','4,6',26,'a'),'londrina':(55,'B','Ficha','4,7',18,'r'),'montes-claros':(41,'A','Ficha','3,4',9,'r'),'ipiranga':(37,'A','Ficha','4,4',14,'r'),'go-catalao-centro':(28,'Sem','Ficha','4,2',4,'r')}
alertas={'altodalapa':['GBP fora da canônica'],'curitiba':[],'campinas-cambui':['GBP fora da canônica'],'boulevardtatuape':['GTM próprio'],'porto-alegre-bom-fim':['GBP sem telefone'],'ribeirao-preto-centro':['GTM próprio'],'aldeota':[],'asa-sul':['GBP sem site'],'salvador':['Poucas fotos'],'vila-madalena':['Sem FAQ'],'londrina':['Texto padrão'],'montes-claros':['Nota baixa','Texto padrão'],'ipiranga':['Sem coordenadas'],'go-catalao-centro':['Sem tratamentos','Sem fotos']}
linhas=''
for u in amostra:
    c,tpl,dom,nota,leadsn,st=info[u['url_site']]
    corc='v' if c>=80 else ('a' if c>=55 else 'r')
    al=''.join(f'<span class="pill {"r" if k in ("Sem coordenadas","GTM próprio","Sem tratamentos") else "a"}" style="margin-right:4px">{k}</span>' for k in alertas[u['url_site']][:1])+(f'<span class="pill z">+{len(alertas[u["url_site"]])-1}</span>' if len(alertas[u['url_site']])>1 else '') or '<span class="pill v"><i></i>Tudo certo</span>'
    nome=nome_un(u)
    linhas+=f'''<tr><td><span style="display:inline-block;width:16px;height:16px;border:1.5px solid #cfc2d6;border-radius:5px;vertical-align:middle"></span></td>
<td><div class="un"><div class="ft" style="background-image:url(../assets/fachada.jpg)"></div><div><b class="trunc" style="max-width:170px;display:block">{nome}</b><small>{u["bairro"][:22]}</small></div></div></td>
<td><span class="trunc" style="display:block;max-width:150px">{u["nome_cidade"]}/{u["nome_uf"]}</span></td>
<td><span class="barra"><i style="width:{c}%"></i></span> <b style="margin-left:6px">{c}%</b></td>
<td>{"<span class='pill z'>Sem template</span>" if tpl=="Sem" else f"<span class='pill l'>Template {tpl}</span>"}</td>
<td>{"<span class='pill b'>"+i('globe',11)+" Próprio</span>" if dom=="Próprio" else "<span class='muted'>Ficha oficial</span>"}</td>
<td class="num"><b>{leadsn}</b> {spark([random.randint(2,9) for _ in range(10)],w=56,h=20)}</td>
<td class="num">{i('star',12)} {nota}</td><td>{al}</td><td>{i('more',16)}</td></tr>'''
cont=f'''
<div class="cab"><div><h1>Unidades</h1><p>130 ativas em 16 estados. Clique numa linha para abrir a unidade.</p></div>
<div class="dir"><span class="sw"><span class="on">{i('list',13)} Tabela</span><span>{i('map',13)} Mapa</span></span><span class="btn">{i('down',14)} Exportar</span><span class="btn p">{i('plus',14)} Nova unidade</span></div></div>
<div class="g" style="grid-template-columns:repeat(6,1fr);margin-bottom:14px">'''+''.join(f'<div class="card" style="padding:13px 15px"><div class="muted" style="font-weight:500">{a}</div><div class="pop" style="font-size:20px;font-weight:600;margin-top:2px;color:{c}">{b}</div></div>' for a,b,c in [('Ativas','130','var(--tinta)'),('Completude ≥ 80%','31','var(--verde)'),('Abaixo de 55%','46','var(--vermelho)'),('Com domínio próprio','9','var(--azul)'),('Alertas de SEO','58','var(--ambar)'),('Alertas de tracking','17','var(--vermelho)')])+f'''</div>
<div class="card" style="padding:0">
 <div style="display:flex;gap:8px;align-items:center;padding:14px 16px;flex-wrap:wrap;border-bottom:1px solid var(--linha)">
  <div class="busca" style="display:flex;align-items:center;gap:8px;border:1px solid var(--linha);border-radius:10px;padding:7px 10px;width:250px;color:var(--tinta-3)">{i('search',14)} Nome, cidade, CEP ou ID DocBiz</div>
  <span class="chip on">Estado: <b>Todos</b> {i('chevd',12)}</span><span class="chip">Cidade {i('chevd',12)}</span><span class="chip">Status: <b>Ativa</b> {i('chevd',12)}</span><span class="chip">Completude {i('chevd',12)}</span><span class="chip">Desempenho {i('chevd',12)}</span><span class="chip">Template {i('chevd',12)}</span><span class="chip">Domínio {i('chevd',12)}</span><span class="chip">Alertas {i('chevd',12)}</span><span class="chip">Multifranqueado {i('chevd',12)}</span>
  <span style="margin-left:auto" class="muted">{i('eye',14)} Visões: <b style="color:var(--roxo-700)">Prioridade SEO do mês</b></span>
 </div>
 <table class="t"><thead><tr><th></th><th>Unidade</th><th>Cidade</th><th>Completude</th><th>Página</th><th>Domínio</th><th class="num">Leads 30d</th><th class="num">Google</th><th>Alertas</th><th></th></tr></thead><tbody>{linhas}</tbody></table>
 <div style="display:flex;align-items:center;padding:12px 16px;border-top:1px solid var(--linha)" class="muted"><span>Mostrando 14 de 130 · ordenado por completude</span><span style="margin-left:auto;display:flex;gap:6px"><span class="btn s">Anterior</span><span class="btn s" style="background:var(--lilas-100);color:var(--roxo-700)">1</span><span class="btn s">2</span><span class="btn s">3</span><span class="btn s">…</span><span class="btn s">10</span><span class="btn s">Próxima</span></span></div>
</div>'''
salvar('03-admin-unidades-tabela',pagina('Unidades',app('admin','unidades',cont),extra_css='table.t td,table.t th{padding-left:9px;padding-right:9px}'))

# 04 MAPA
pts=[]
for u in UNID:
    if u['latitude'] and u['longitude']:
        s=score(u); cor='#0e9f6e' if s>=80 else ('#d98a00' if s>=55 else '#d5305f')
        pts.append((float(u['latitude']),float(u['longitude']),cor,7))
box_sp=(-24.2,-22.6,-47.4,-45.9)
pts_sp=[(a,b,c,8) for a,b,c,_ in pts]
mapa=mapa_br(700,700,pts)
zoom=mapa_br(380,300,pts_sp,box=box_sp,contorno=False)
cont=f'''
<div class="cab"><div><h1>Unidades no mapa</h1><p>117 unidades com coordenadas. 13 sem coordenadas aparecem na lista ao lado.</p></div>
<div class="dir"><span class="sw"><span>{i('list',13)} Tabela</span><span class="on">{i('map',13)} Mapa</span></span><span class="btn">{i('layout',14)} Camadas</span><span class="btn p">{i('plus',14)} Nova unidade</span></div></div>
<div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap"><span class="chip">Colorir por: <b>Completude</b> {i('chevd',12)}</span><span class="chip">Estado {i('chevd',12)}</span><span class="chip">Template {i('chevd',12)}</span><span class="chip">Domínio próprio {i('chevd',12)}</span><span class="chip on">Alertas: <b>qualquer</b> {i('x',12)}</span><span class="chip">Raio de concorrência {i('chevd',12)}</span></div>
<div class="g" style="grid-template-columns:1fr 380px">
 <div class="card" style="padding:0;position:relative;overflow:hidden;background:#fbf8fc">
  <div style="display:flex;justify-content:center;padding:20px 0 10px">{mapa}</div>
  <div style="position:absolute;left:18px;top:18px" class="card"><div class="leg" style="flex-direction:column;gap:6px"><b style="font-size:12px">Completude da página</b><span><i style="background:#0e9f6e"></i>80% ou mais · 31</span><span><i style="background:#d98a00"></i>55% a 79% · 53</span><span><i style="background:#d5305f"></i>abaixo de 55% · 46</span></div></div>
  <div style="position:absolute;right:18px;top:18px;display:flex;flex-direction:column;gap:6px"><div class="ib">{i('plus')}</div><div class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M5 12h14"/></svg></div><div class="ib">{i('target')}</div></div>
  <div class="card" style="position:absolute;left:28px;top:520px;width:290px;padding:14px">
   <div class="un"><div class="ft" style="background-image:url(../assets/fachada.jpg);width:44px;height:44px"></div><div><b>GiO Alto da Lapa</b><small>Av. São Gualter, 53 · São Paulo/SP</small></div></div>
   <div class="g" style="grid-template-columns:repeat(3,1fr);gap:8px;margin:12px 0"><div><div class="muted" style="font-size:11px">Completude</div><b>90%</b></div><div><div class="muted" style="font-size:11px">Leads 30d</div><b>41</b></div><div><div class="muted" style="font-size:11px">Google</div><b>4,9 ★</b></div></div>
   <div style="display:flex;gap:6px"><span class="btn s p">Abrir unidade</span><span class="btn s">Ver página</span></div></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Grande São Paulo</h3><span class="sub" style="margin-left:auto">zoom</span></div><div style="background:#fbf8fc;border-radius:12px;overflow:hidden">{zoom}</div></div>
  <div class="card"><div class="hd"><h3>{i('alert',15)} Fora do mapa</h3><span class="pill r" style="margin-left:auto">13</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it"><div style="flex:1"><b>{n}</b><div class="muted" style="font-size:12px">{c} · CEP cadastrado</div></div><span class="btn s">{i("pin",12)} Geocodificar</span></div>' for n,c in [('GiO Ipiranga','São Paulo/SP'),('GiO Diadema Centro','Diadema/SP'),('GiO Catalão Centro','Catalão/GO'),('GiO Balsas','Balsas/MA')])+'''<div class="it muted">+ 9 unidades</div></div></div>
 </div>
</div>'''
salvar('04-admin-unidades-mapa',pagina('Mapa de unidades',app('admin','unidades',cont)))
print('p1 ok')
