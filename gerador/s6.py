from base import *
A=DEMO['altodalapa']
# ---------- MOBILE (app do franqueado) ----------
def status_bar(): return '<div style="height:44px;display:flex;align-items:center;padding:0 22px;font:600 15px Inter;color:var(--tinta)"><span>9:41</span><span style="margin-left:auto;display:flex;gap:6px;align-items:center"><span style="width:18px;height:10px;border:1.5px solid var(--tinta);border-radius:3px"></span></span></div>'
def tabbar(on):
    it=[('home','Início','f-inicio'),('inbox','Leads','m-leads'),('cal','Agenda',None),('layout','Página','f-tpl'),('more','Mais','f-notif')]
    return '<nav class="tabbar">'+''.join(f'<a class="{"on" if k==on else ""}" href="{L(lk) if lk else "#docbiz"}" style="position:relative">{i(ic,22)}<span>{t}{" ↗" if not lk else ""}</span>{"<span style=\"position:absolute;top:0;left:50%;margin-left:6px;background:var(--magenta);color:#fff;font:600 12px Inter;border-radius:10px;padding:0 6px;line-height:18px\">9</span>" if t=="Leads" else ""}</a>' for k,(ic,t,lk) in enumerate(it))+'</nav>'
leads=[('Mariana S.','Depilação a laser','Google Ads','há 4 min','l','Novo'),('Juliana P.','Limpeza de pele','Orgânico','há 22 min','l','Novo'),('Fernanda L.','Ultraformer','Instagram','há 1 h','l','Novo'),('Camila R.','Depilação a laser','Meta Ads','há 3 h','b','Em contato'),('Beatriz M.','Peeling','Orgânico','ontem','a','Agendado')]
chips=[('Todos',9),('Novo',3),('Em contato',2),('Agendado',3),('Compareceu',1)]
corpo=f'''<div class="mob">{status_bar()}<div class="rolagem" style="padding:0 16px">
 <div style="display:flex;align-items:center;margin:4px 0 12px"><div><div class="meta">GiO Alto da Lapa</div><h1 style="font-size:24px;font-weight:600">Leads</h1></div><span class="ib" style="margin-left:auto">{i('search',18)}</span></div>
 <div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:6px">'''+''.join(f'<span class="chip{" on" if k==0 else ""}" style="padding:6px 10px">{t} <b>{n}</b></span>' for k,(t,n) in enumerate(chips))+f'''</div>
 <div class="meta" style="margin-bottom:10px">3 + 2 + 3 + 1 = 9 em aberto</div>
 <div style="display:flex;flex-direction:column;gap:10px">'''+''.join(f'<a class="card" href="{L("m-lead")}" style="padding:14px;display:flex;gap:12px;align-items:center;box-shadow:none"><span class="av-s" style="width:40px;height:40px;font-size:14px">{n[0]}{n.split()[1][0]}</span><div style="flex:1;min-width:0"><div style="display:flex;align-items:center;gap:8px"><b class="trunc">{n}</b><span class="pill {c}" style="margin-left:auto;flex:none">{s}</span></div><div class="meta trunc">{t} · {o}</div><div class="meta">{q}</div></div></a>' for n,t,o,q,c,s in leads)+f'''</div>
</div>{tabbar(1)}</div>'''
salvar(ARQ['m-leads'],pagina('Leads no celular',corpo,390))
corpo=f'''<div class="mob">{status_bar()}<div class="rolagem" style="padding:0 16px">
 <a href="{L('m-leads')}" class="lk" style="display:inline-flex;align-items:center;gap:4px;min-height:40px">{i('chev',14)} Leads</a>
 <div style="display:flex;gap:12px;align-items:center;margin:4px 0 14px"><span class="av-s" style="width:52px;height:52px;font-size:18px">MS</span><div><h1 style="font-size:22px;font-weight:600">Mariana S.</h1><div class="meta">Depilação a laser · Google Ads · há 4 min</div></div></div>
 <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px"><span class="btn p" style="min-height:48px">{i('wa',18)} WhatsApp</span><span class="btn" style="min-height:48px">{i('phone',18)} Ligar</span></div>
 <p class="meta" style="margin:8px 0 14px">{i('log',12)} Ligar ou abrir o WhatsApp fica registrado na auditoria. O número não é exibido para a recepção.</p>
 <div class="card" style="padding:14px;margin-bottom:10px"><b>Status</b><div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap">'''+''.join(f'<span class="chip{" on" if k==0 else ""}">{t}</span>' for k,t in enumerate(['Novo','Em contato','Agendado','Não converteu']))+f'''</div></div>
 <div class="card" style="padding:14px;margin-bottom:10px"><b>Mensagem do formulário</b><p class="muted" style="margin-top:6px">Quero saber sobre pacote de axilas e virilha. Prefiro sábado de manhã.</p></div>
 <div class="card" style="padding:14px"><div style="display:flex;gap:8px;align-items:center"><span class="ic v" style="width:30px;height:30px">{i('shield',14)}</span><b>Consentimento registrado</b></div><p class="meta" style="margin-top:6px">Aviso de privacidade v3 aceito em 21/11 às 09:37. Marketing por WhatsApp: não autorizado.</p></div>
</div>{tabbar(1)}</div>'''
salvar(ARQ['m-lead'],pagina('Lead no celular',corpo,390))

# ---------- LANDINGS PÚBLICAS ----------
FAIXA='<div style="background:#24082c;color:#fff;text-align:center;font-size:13px;padding:8px 12px">Página de demonstração do sistema de unidades Gio. Alguns dados podem ser ilustrativos.</div>'
TRATS=[('Depilação a laser','trat-laser'),('Limpeza de pele','trat-limpeza'),('Ultraformer','trat-ultrassom'),('Microagulhamento','trat-micro'),('Peeling','sala-facial'),('Criolipólise','sala-laser')]
REV=[('Ana P.','Atendimento atencioso e a sala é muito limpa.'),('Joana M.','Gostei do resultado, a equipe explica tudo.'),('Cris L.','Horários flexíveis e ambiente tranquilo.')]
FAQ=['Quanto tempo dura a sessão de laser?','Precisa raspar antes da sessão?','A unidade tem estacionamento?','Atendem aos sábados?','Quantas sessões são necessárias?','Como chegar de transporte público?']
def topo_lp(d,mob=False):
    if mob: return f'<header style="display:flex;align-items:center;padding:12px 16px;background:#fff;border-bottom:1px solid var(--linha)"><img src="../assets/logo-gio.png" alt="Gio" style="height:30px"><span style="margin-left:auto;width:40px;height:40px;display:grid;place-items:center">{i("list",22)}</span></header>'
    return f'<header style="display:flex;align-items:center;gap:28px;padding:16px var(--lp-pad);background:#fff;border-bottom:1px solid var(--linha)"><img src="../assets/logo-gio.png" alt="Gio" style="height:38px"><span class="meta" style="font-weight:600;color:var(--tinta-2)">{d["nome"]}</span><nav style="margin-left:auto;display:flex;gap:24px;color:var(--tinta-2);font-weight:500"><a>Tratamentos</a><a>A unidade</a><a>Avaliações</a><a>Perguntas</a><a>Como chegar</a></nav><a class="btn p" href="#agendar">Agendar avaliação</a></header>'
def form(d,compact=False):
    return f'''<div class="card" id="agendar" style="color:var(--tinta);padding:{20 if compact else 24}px;box-shadow:0 20px 50px rgba(36,8,44,.18)">
 <h3 style="font-size:19px;font-weight:600">Agende sua avaliação gratuita</h3><p class="meta" style="margin:4px 0 14px">{d['nome']} · resposta pelo WhatsApp em até 15 min no horário de atendimento</p>
 <div style="display:flex;flex-direction:column;gap:10px">
  <div class="campo"><label>Nome</label><div class="in" style="color:var(--tinta-3)">Como podemos te chamar?</div></div>
  <div class="campo"><label>WhatsApp</label><div class="in" style="color:var(--tinta-3)">(00) 00000-0000</div></div>
  <div class="campo"><label>Tratamento de interesse</label><div class="in" style="color:var(--tinta-3)">Escolha uma opção <span style="margin-left:auto">{i('chevd',14)}</span></div></div>
  <label style="display:flex;gap:10px;align-items:flex-start;font-size:13px;color:var(--tinta-2);min-height:40px"><span class="cx" style="margin-top:2px;flex:none"></span><span>Li o <a class="lk">Aviso de Privacidade</a> e autorizo a Gio a usar meus dados para responder este pedido. <b>Obrigatório</b></span></label>
  <label style="display:flex;gap:10px;align-items:flex-start;font-size:13px;color:var(--tinta-2);min-height:40px"><span class="cx" style="margin-top:2px;flex:none"></span><span>Quero receber novidades e ofertas por WhatsApp (opcional)</span></label>
  <span class="btn off" style="min-height:48px">Quero agendar</span>
  <span class="meta">O botão libera depois que você aceitar o aviso de privacidade.</span>
 </div></div>'''
def rodape(d,mob=False):
    pad='28px 20px' if mob else '40px var(--lp-pad)'
    cols='1fr' if mob else '1.4fr 1fr 1fr'
    return f'''<footer style="background:#24082c;color:#f3eaf6;padding:{pad}"><div style="display:grid;grid-template-columns:{cols};gap:24px">
 <div><img src="../assets/logo-gio-branco.png" alt="Gio" style="height:34px"><p style="margin-top:10px;font-size:13px">{d['nome']} · {d['end']} · {d['bairro']} · {d['cidade']}/{d['uf']} · CEP {d['cep']}</p><p style="font-size:13px">CNPJ {d['cnpj']} · dados ilustrativos</p></div>
 <div style="font-size:13px"><b style="color:#fff">Contato</b><p style="margin-top:6px">{d['tel']}<br>WhatsApp {d['wa']}<br>{d['ig']}</p></div>
 <div style="font-size:13px"><b style="color:#fff">Rede Gio</b><p style="margin-top:6px"><a style="text-decoration:underline">Aviso de Privacidade</a><br><a style="text-decoration:underline">Seus direitos (LGPD)</a><br><a style="text-decoration:underline">Outras unidades</a></p></div></div></footer>'''
def tratamentos(cols=3,mob=False):
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:{12 if mob else 16}px">'+''.join(f'<div class="card" style="padding:0;overflow:hidden;box-shadow:none"><div style="height:{110 if mob else 150}px;background:url(../assets/fotos/{f}.jpg) center/cover"></div><div style="padding:{10 if mob else 14}px"><b>{t}</b>{"" if mob else "<div class=\"meta\" style=\"margin-top:2px\">Avaliação gratuita</div>"}</div></div>' for t,f in TRATS)+'</div>'
def reviews(d,cols=3):
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:14px">'+''.join(f'<div class="card" style="box-shadow:none"><div style="color:#8A5800">{"★"*5}</div><p style="margin:8px 0">{t}</p><div class="meta">{n} · Google (ilustrativo)</div></div>' for n,t in REV)+'</div>'
def faqbox(n=4,aberta=True,lista=None):
    FQ=lista or FAQ
    return '<div style="border:1px solid var(--linha);border-radius:14px;padding:4px 16px;background:#fff">'+''.join(f'<div style="display:flex;align-items:center;gap:12px;min-height:56px;border-bottom:1px solid var(--linha)"><b style="flex:1">{q}</b><span style="width:40px;height:40px;display:grid;place-items:center;color:var(--vinho);{"transform:rotate(180deg)" if (k==0 and aberta) else ""}">{i("chevd",18)}</span></div>'+('<p class="muted" style="padding:10px 0 14px">Depende da área: de 10 a 40 minutos. A equipe explica tudo na avaliação gratuita.</p>' if (k==0 and aberta) else '') for k,q in enumerate(FQ[:n]))+'</div>'
def chegar(d,osm,h=260,raio=None):
    return f'<div class="card" style="padding:0;overflow:hidden;box-shadow:none">{mapa_osm(osm,800,h,raio=raio)}<div style="padding:12px 16px;display:flex;gap:10px;align-items:center;flex-wrap:wrap"><b>{d["end"]} · {d["bairro"]}</b><span class="credito" style="margin-left:auto">{OSM_CRED} · posição aproximada</span></div></div>'
def confianca(cols=4):
    it=[('shield','Equipamentos aprovados pela Anvisa'),('users','Equipe treinada pela rede'),('star','Avaliação gratuita'),('cal','Horários até 20h')]
    return f'<div style="display:grid;grid-template-columns:repeat({cols},1fr);gap:12px">'+''.join(f'<div style="display:flex;gap:10px;align-items:center;background:#fff;border:1px solid var(--linha);border-radius:12px;padding:12px"><div class="ic l">{i(ic,16)}</div><b style="font-size:13px">{t}</b></div>' for ic,t in it)+'</div>'
def sec(t,sub='',mob=False): return f'<h2 style="font-size:{22 if mob else 28}px;font-weight:600;margin-bottom:4px">{t}</h2>'+(f'<p class="muted" style="margin-bottom:16px">{sub}</p>' if sub else '<div style="height:14px"></div>')
# A · Clássico (Batel)
d=DEMO['curitiba']
corpo=f'''{FAIXA}{topo_lp(d)}
<section style="background:var(--grad);color:#fff;padding:56px var(--lp-pad);position:relative;overflow:hidden"><div style="position:absolute;inset:0;background:url(../assets/fotos/sala-laser.jpg) center/cover;opacity:.16;mix-blend-mode:luminosity"></div>
 <div style="position:relative;display:grid;grid-template-columns:1fr 440px;gap:48px;align-items:center">
  <div><span class="pill" style="background:rgba(255,255,255,.18);color:#fff">{i('pin',12)} {d['bairro']} · {d['cidade']}</span><h1 style="font-size:46px;line-height:1.1;font-weight:600;margin:16px 0">Depilação a laser e estética avançada no {d['bairro']}</h1><p style="font-size:18px;max-width:560px">Avaliação gratuita, equipe treinada e horários até 20h. Responda o formulário e falamos com você pelo WhatsApp.</p>
  <div style="display:flex;gap:24px;margin-top:24px"><div><b class="pop" style="font-size:26px">{d['nota']} ★</b><div>{d['aval']} avaliações no Google (ilustrativo)</div></div></div></div>
  {form(d)}</div></section>
<section style="padding:28px var(--lp-pad);background:#fff">{confianca()}</section>
<section style="padding:48px var(--lp-pad)">{sec('Tratamentos nesta unidade','6 tratamentos disponíveis no '+d['bairro'])}{tratamentos(3)}</section>
<section style="padding:48px var(--lp-pad);background:#fff">{sec('O que dizem no Google')}{reviews(d)}</section>
<section style="padding:48px var(--lp-pad);display:grid;grid-template-columns:1fr 1fr;gap:32px"><div>{sec('Perguntas frequentes')}{faqbox(4)}</div><div>{sec('Como chegar')}{chegar(d,'batel',300)}</div></section>
{rodape(d)}'''
salvar(ARQ['lpA'],pagina(f'{d["nome"]} · Modelo A',corpo))
corpo=f'''{FAIXA}{topo_lp(d,True)}
<section style="background:var(--grad);color:#fff;padding:28px 20px"><span class="pill" style="background:rgba(255,255,255,.18);color:#fff">{i('pin',12)} {d['bairro']} · {d['cidade']}</span><h1 style="font-size:30px;line-height:1.15;font-weight:600;margin:12px 0">Depilação a laser e estética no {d['bairro']}</h1><p>Avaliação gratuita e resposta pelo WhatsApp.</p></section>
<section style="padding:0 16px;margin-top:-6px">{form(d,True)}</section>
<div style="position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--linha);padding:10px 16px;display:flex;gap:10px;align-items:center;margin-top:16px"><b>{d['nota']} ★</b><span class="meta">{d['aval']} avaliações</span><a class="btn p" href="#agendar" style="margin-left:auto;min-height:44px">Agendar</a></div>
<section style="padding:24px 16px">{confianca(2)}</section>
<section style="padding:8px 16px 24px">{sec('Tratamentos','6 disponíveis nesta unidade',True)}{tratamentos(2,True)}</section>
<section style="padding:24px 16px;background:#fff">{sec('Avaliações',mob=True)}{reviews(d,1)}</section>
<section style="padding:24px 16px">{sec('Perguntas frequentes',mob=True)}{faqbox(4)}</section>
<section style="padding:0 16px 24px">{sec('Como chegar',mob=True)}{chegar(d,'batel',220)}</section>
{rodape(d,True)}'''
salvar(ARQ['lpAm'],pagina(f'{d["nome"]} · Modelo A celular',corpo,390))
# B · Vitrine (Alto da Lapa)
d=A
gal=['fachada','recepcao','sala-laser','sala-facial','espera','equipe']
equipe=[('FC','Fernanda C.','Esteticista responsável'),('LT','Larissa T.','Especialista em laser'),('BM','Bruna M.','Recepção e agenda')]
corpo=f'''{FAIXA}{topo_lp(d)}
<section style="height:560px;background:url(../assets/fotos/fachada.jpg) center 40%/cover;position:relative"><div style="position:absolute;inset:0;background:rgba(255,255,255,.25)"></div>
 <div style="position:absolute;left:var(--lp-pad);bottom:48px;background:rgba(255,255,255,.95);border-radius:20px;padding:28px 32px;max-width:620px;box-shadow:0 20px 50px rgba(36,8,44,.18)">
  <span class="pill l">{i('pin',12)} {d['bairro']} · {d['cidade']}/{d['uf']}</span>
  <h1 style="font-size:40px;line-height:1.1;font-weight:600;margin:12px 0 8px">{d['nome']}</h1>
  <div style="display:flex;gap:10px;align-items:center;margin-bottom:16px"><b style="color:#8A5800">★★★★★</b><b>{d['nota']}</b><span class="muted">{d['aval']} avaliações no Google (ilustrativo)</span></div>
  <div style="display:flex;gap:10px"><a class="btn p" href="#agendar" style="min-height:48px;padding:12px 22px">Agendar avaliação</a><a class="btn" style="min-height:48px">{i('wa',16)} WhatsApp</a></div></div></section>
<div style="display:grid;grid-template-columns:1fr 400px;gap:40px;padding:48px var(--lp-pad);align-items:start">
 <div>
  <section style="margin-bottom:44px">{sec('Conheça a unidade','Fotos reais do espaço')}<div style="display:grid;grid-template-columns:2fr 1fr 1fr;grid-template-rows:170px 170px;gap:10px">'''+''.join(f'<div style="background:url(../assets/fotos/{f}.jpg) center/cover;border-radius:14px;{"grid-row:span 2" if k==0 else ""}"></div>' for k,f in enumerate(gal[1:6]))+f'''</div></section>
  <section style="margin-bottom:44px">{sec('Nossa equipe')}<div style="display:grid;grid-template-columns:1.2fr 1fr;gap:16px;align-items:center"><div style="height:220px;border-radius:16px;background:url(../assets/fotos/equipe.jpg) center/cover"></div><div class="lista-i">'''+''.join(f'<div class="it"><span class="av-s" style="width:44px;height:44px;font-size:14px">{a}</span><div><b>{n}</b><div class="meta">{c}</div></div></div>' for a,n,c in equipe)+f'''</div></div></section>
  <section style="margin-bottom:44px">{sec('Tratamentos','6 tratamentos nesta unidade')}{tratamentos(3)}</section>
  <section style="margin-bottom:44px">{sec('Avaliações no Google')}{reviews(d)}</section>
  <section style="margin-bottom:44px">{sec('Perguntas frequentes')}{faqbox(4)}</section>
  <section>{sec('Como chegar')}{chegar(d,'altodalapa',280)}</section>
 </div>
 <div style="position:sticky;top:24px">{form(d)}</div>
</div>
{rodape(d)}'''
salvar(ARQ['lpB'],pagina(f'{d["nome"]} · Modelo B',corpo))
corpo=f'''{FAIXA}{topo_lp(d,True)}
<section style="height:360px;background:url(../assets/fotos/fachada.jpg) center 40%/cover;position:relative"><div style="position:absolute;inset:0;background:rgba(255,255,255,.25)"></div>
 <div style="position:absolute;left:16px;right:16px;bottom:16px;background:rgba(255,255,255,.95);border-radius:16px;padding:18px">
  <h1 style="font-size:26px;font-weight:600">{d['nome']}</h1><div style="display:flex;gap:8px;align-items:center;margin:6px 0 12px"><b style="color:#8A5800">★★★★★</b><b>{d['nota']}</b><span class="meta">{d['aval']} avaliações</span></div>
  <a class="btn p" href="#agendar" style="width:100%;min-height:48px">Agendar avaliação</a></div></section>
<div style="position:sticky;top:0;z-index:5;background:#fff;border-bottom:1px solid var(--linha);padding:10px 16px;display:flex;gap:10px;align-items:center"><b>{d['bairro']}</b><a class="btn p" href="#agendar" style="margin-left:auto;min-height:44px">Agendar</a></div>
<section style="padding:20px 16px">{sec('Conheça a unidade',mob=True)}<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">'''+''.join(f'<div style="height:120px;background:url(../assets/fotos/{f}.jpg) center/cover;border-radius:12px"></div>' for f in gal[1:5])+f'''</div></section>
<section style="padding:4px 16px 20px">{sec('Tratamentos','6 nesta unidade',True)}{tratamentos(2,True)}</section>
<section style="padding:20px 16px;background:#fff">{sec('Avaliações',mob=True)}{reviews(d,1)}</section>
<section style="padding:20px 16px">{form(d,True)}</section>
<section style="padding:4px 16px 24px">{sec('Perguntas frequentes',mob=True)}{faqbox(4)}</section>
{rodape(d,True)}'''
salvar(ARQ['lpBm'],pagina(f'{d["nome"]} · Modelo B celular',corpo,390))
# C · Autoridade local (Cambuí)
d=DEMO['campinas-cambui']
bairros=['Cambuí','Guanabara','Nova Campinas','Taquaral','Bosque','Centro','Jardim Proença']
faqC=FAQ+['Atendem moradores de Barão Geraldo?','Tem horário depois do trabalho?']
corpo=f'''{FAIXA}{topo_lp(d)}
<section style="position:relative;height:440px;overflow:hidden">{mapa_osm('cambui',1440,440,raio=170)}
 <div style="position:absolute;left:var(--lp-pad);top:48px;background:#fff;border-radius:20px;padding:26px 30px;max-width:560px;box-shadow:0 20px 50px rgba(36,8,44,.18)">
  <span class="pill l">{i('pin',12)} Raio de atendimento de 3 km</span>
  <h1 style="font-size:38px;line-height:1.12;font-weight:600;margin:12px 0 8px">Depilação a laser no {d['bairro']}, {d['cidade']}</h1>
  <p class="muted">Atendemos {", ".join(bairros[:-1])} e {bairros[-1]}.</p>
  <div style="display:flex;flex-wrap:wrap;gap:6px;margin-top:12px">'''+''.join(f'<span class="chip" style="min-height:30px;padding:4px 10px">{b}</span>' for b in bairros)+f'''</div></div>
 <span class="credito" style="position:absolute;right:16px;bottom:10px;background:rgba(255,255,255,.9);padding:2px 8px;border-radius:6px">{OSM_CRED}</span></section>
<div style="display:grid;grid-template-columns:1fr 400px;gap:40px;padding:40px var(--lp-pad);align-items:start">
 <div>
  <section style="margin-bottom:40px"><div style="display:flex;align-items:center;gap:12px;margin-bottom:14px"><h2 style="font-size:28px;font-weight:600">Quem mora perto avalia</h2><b style="margin-left:auto;font-size:18px">{d['nota']} ★</b><span class="muted">{d['aval']} avaliações (ilustrativo)</span></div>{reviews(d)}</section>
  <section style="margin-bottom:40px">{sec('Perguntas de quem é do bairro','Respostas da equipe da unidade')}{faqbox(8,lista=faqC)}</section>
  <section style="margin-bottom:40px">{sec('Tratamentos','6 tratamentos nesta unidade')}{tratamentos(3)}</section>
  <section>{sec('Como chegar','A 5 minutos do Centro de Convivência, posição aproximada')}{chegar(d,'cambui',260)}</section>
 </div>
 <div style="position:sticky;top:24px">{form(d)}</div>
</div>
{rodape(d)}'''
corpo=corpo.replace("".join([]),"")
salvar(ARQ['lpC'],pagina(f'{d["nome"]} · Modelo C',corpo))
corpo=f'''{FAIXA}{topo_lp(d,True)}
<section style="position:relative;height:260px;overflow:hidden">{mapa_osm('cambui',390,260,raio=80)}<span class="credito" style="position:absolute;right:8px;bottom:6px;background:rgba(255,255,255,.9);padding:2px 6px;border-radius:6px">{OSM_CRED}</span></section>
<section style="padding:20px 16px;background:#fff"><span class="pill l">{i('pin',12)} Raio de 3 km</span><h1 style="font-size:28px;line-height:1.15;font-weight:600;margin:10px 0 6px">Depilação a laser no {d['bairro']}, {d['cidade']}</h1><p class="muted">Atendemos {", ".join(bairros[:4])} e região.</p></section>
<div style="position:sticky;top:0;z-index:5;background:#fff;border-top:1px solid var(--linha);border-bottom:1px solid var(--linha);padding:10px 16px;display:flex;gap:10px;align-items:center"><b>{d['nota']} ★</b><span class="meta">{d['aval']} avaliações</span><a class="btn p" href="#agendar" style="margin-left:auto;min-height:44px">Agendar</a></div>
<section style="padding:20px 16px">{sec('Quem mora perto avalia',mob=True)}{reviews(d,1)}</section>
<section style="padding:4px 16px 20px">{sec('Perguntas do bairro',mob=True)}{faqbox(6,lista=faqC)}</section>
<section style="padding:4px 16px 20px">{form(d,True)}</section>
<section style="padding:4px 16px 24px">{sec('Tratamentos','6 nesta unidade',True)}{tratamentos(2,True)}</section>
{rodape(d,True)}'''
salvar(ARQ['lpCm'],pagina(f'{d["nome"]} · Modelo C celular',corpo,390))
print('s6 ok')
