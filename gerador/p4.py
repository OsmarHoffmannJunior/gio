from base import *
random.seed(21)
def campo(l,v,lock=False,aj='',ic='',dest=False):
    return f'<div class="campo"><label>{l}{" "+i("lock",11) if lock else ""}</label><div class="in{" lock" if lock else ""}" style="{"border-color:var(--rosa);box-shadow:0 0 0 3px #fbe3ef" if dest else ""}">{i(ic,14) if ic else ""}{v}</div>{f"<div class=ajuda>{aj}</div>" if aj else ""}</div>'
# 12 DASHBOARD FRANQUEADO
dias=[f'{d:02d}/11' for d in range(1,22)]
ld=[1,2,1,3,2,0,1,2,3,2,1,3,2,1,2,4,3,2,3,1,2]
ag=[1,1,0,2,1,0,1,1,2,1,1,2,1,1,1,3,2,1,2,1,2]
leads_h=[('Mariana S.','Depilação a laser','Google Ads','v','Agendado sáb 15:30'),('Beatriz L.','Limpeza de pele','Orgânico','a','Novo · 6 min'),('Fernanda R.','Criolipólise','Instagram','b','Em contato')]
cont=f'''
<div class="hero" style="margin-bottom:16px;display:flex;align-items:center;gap:24px;background:linear-gradient(120deg,#6f0052,#b0197e 60%,#e5559f)">
 <div style="position:relative;z-index:1;flex:1"><div style="opacity:.85">Sábado, 21 de novembro</div><h1 style="font-size:26px;font-weight:600;margin:4px 0 6px">Bom dia, Renata. Sua unidade está em 7º na rede.</h1><div style="opacity:.9;max-width:620px">Subiu 3 posições este mês. Responder leads em até 10 minutos e completar o FAQ deixam você no top 5.</div>
 <div style="display:flex;gap:8px;margin-top:14px"><span class="btn" style="background:#fff;color:var(--vinho);border:0">{i('inbox',14)} 2 leads esperando</span><span class="btn" style="background:rgba(255,255,255,.16);color:#fff;border:1px solid rgba(255,255,255,.3)">{i('edit',14)} Completar página</span></div></div>
 <div style="position:relative;z-index:1;background:rgba(255,255,255,.12);border:1px solid rgba(255,255,255,.22);border-radius:16px;padding:16px 18px;width:300px">
  <div style="font-size:12px;opacity:.85">Sua posição no ranking da rede</div>
  <div style="display:flex;align-items:baseline;gap:8px;margin:4px 0 10px"><span class="pop" style="font-size:40px;font-weight:600">7º</span><span style="opacity:.85">de 130</span><span class="pill" style="background:#fff;color:var(--verde);margin-left:auto">{i('trend',11)} +3</span></div>
  <div style="height:8px;border-radius:8px;background:rgba(255,255,255,.2);position:relative"><div style="position:absolute;left:0;width:94%;height:100%;border-radius:8px;background:#fff"></div><span style="position:absolute;left:50%;top:-4px;width:2px;height:16px;background:#ffd6ea"></span></div>
  <div style="display:flex;justify-content:space-between;font-size:11px;opacity:.85;margin-top:6px"><span>130º</span><span>mediana</span><span>1º</span></div></div>
</div>
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">
 <div class="card kpi"><div class="l">{i('inbox',15)} Leads no mês</div><div class="v">41</div><div class="d"><span class="up">+18%</span> · rede: 23 por unidade</div></div>
 <div class="card kpi"><div class="l">{i('cal',15)} Agendados</div><div class="v">27</div><div class="d">66% · rede: 58%</div></div>
 <div class="card kpi"><div class="l">{i('clock',15)} Seu 1º contato</div><div class="v">8 min</div><div class="d"><span class="up">melhor que 82%</span> da rede</div></div>
 <div class="card kpi"><div class="l">{i('star',15)} Google</div><div class="v">4,9</div><div class="d">312 avaliações · 4 sem resposta</div></div>
</div>
<div class="g" style="grid-template-columns:1.5fr 1fr">
 <div class="card"><div class="hd"><h3>Seus leads e agendamentos</h3><div class="leg" style="margin-left:12px"><span><i style="background:#b0197e"></i>Leads</span><span><i style="background:#e5559f"></i>Agendados</span></div><span class="sub" style="margin-left:auto">novembro</span></div>
 {area([ld,ag],['#b0197e','#f2a7cc'],w=640,h=200,labels=dias,ymax=5)}
 <div class="sep"></div>
 <div class="g" style="grid-template-columns:repeat(3,1fr);gap:12px">'''+''.join(f'<div><div class="muted" style="font-size:12px">{a}</div><div style="display:flex;align-items:center;gap:8px;margin-top:4px"><b class="pop" style="font-size:18px">{b}</b><span class="barra" style="flex:1"><i style="width:{c}%"></i></span></div></div>' for a,b,c in [('Google Ads','46%',46),('Google orgânico e mapa','32%',32),('Instagram','22%',22)])+f'''</div></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Leads recentes</h3><span class="btn s" style="margin-left:auto">Ver todos</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it"><span class="av-s" style="background:#fbe3ef">{n[0]}{n.split()[1][0]}</span><div style="flex:1;min-width:0"><b>{n}</b><div class="muted" style="font-size:12px">{t} · {o}</div></div><span class="pill {c}">{s}</span></div>' for n,t,o,c,s in leads_h)+f'''</div></div>
  <div class="card"><div class="hd"><h3>Para subir no ranking</h3><span class="pill l" style="margin-left:auto">3 tarefas</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it"><span style="width:18px;height:18px;border-radius:6px;border:2px solid {"var(--magenta)" if not ok else "var(--verde)"};display:grid;place-items:center;{"background:var(--verde);color:#fff" if ok else ""}">{i("check",10) if ok else ""}</span><span style="flex:1;{"text-decoration:line-through;color:var(--tinta-3)" if ok else ""}">{t}</span><span class="muted" style="font-size:12px">{p}</span></div>' for t,p,ok in [('Responder 4 avaliações do Google','+2 pts',False),('Completar FAQ local (3 de 6)','+3 pts',False),('Corrigir site no perfil do Google','+4 pts',False),('Subir 8 fotos da clínica','feito',True)])+'''</div></div>
 </div>
</div>'''
salvar('12-franqueado-dashboard',pagina('Início',app('franq','inicio',cont)))

# 13 MINHA UNIDADE (EDIÇÃO)
trat=[('Depilação a laser',True,'Destaque'),('Limpeza de pele',True,''),('Criolipólise',True,''),('Microagulhamento',True,''),('Bioestimulador de colágeno',True,''),('Peeling químico',True,''),('Drenagem linfática',False,''),('Ultraformer',False,'Pede aprovação')]
cont=f'''
<div class="cab"><div><h1>Minha unidade</h1><p>O que você muda aqui aparece na página da unidade, no Google e no app de agendamento.</p></div>
<div class="dir"><span class="pill a">{i('clock',11)} 1 alteração em aprovação</span><span class="btn">{i('eye',14)} Ver como cliente</span><span class="btn p">{i('send',14)} Enviar alterações</span></div></div>
<div class="tabs"><a class="on">Informações</a><a>Horários</a><a>Tratamentos <span class="n">6</span></a><a>Fotos <span class="n">8</span></a><a>Equipe <span class="n">2</span></a><a>FAQ <span class="n">3</span></a><a>Avaliações</a></div>
<div class="g" style="grid-template-columns:1fr 330px">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Contato</h3><span class="sub" style="margin-left:auto">{i('lock',12)} Nome, endereço e CNPJ só a rede altera</span></div>
  <div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:14px">{campo('Nome da unidade','GiO Alto da Lapa',True)}{campo('Endereço','Av. São Gualter, 53 · Vila Ida',True)}{campo('Telefone','(11) 3832 4410',False,'','phone')}
  {campo('WhatsApp que recebe leads','(11) 94587 2210',False,'Teste enviado ontem às 14:02 ✓','wa',True)}{campo('Instagram','@gioaltodalapa',False,'','globe')}{campo('E-mail para avisos','altodalapa@exemplo.com.br',False,'','inbox')}</div></div>
  <div class="card"><div class="hd"><h3>Sobre a unidade</h3><span class="sub">até 600 caracteres · aparece no bloco Sobre</span><span class="pill v" style="margin-left:auto">{i('check',11)} Dentro das regras da marca</span></div>
  <div style="border:1px solid var(--linha);border-radius:12px;padding:14px;line-height:1.7">A GiO Alto da Lapa fica na Av. São Gualter e atende a região com depilação a laser e tratamentos faciais e corporais. Estamos a 5 minutos da Praça Cornélia, com estacionamento conveniado na rua Tito. Agende sua avaliação gratuita e conheça a equipe.<span style="display:inline-block;width:2px;height:16px;background:var(--magenta);vertical-align:middle;margin-left:2px"></span></div>
  <div style="display:flex;gap:8px;margin-top:10px;align-items:center"><span class="btn s">{i('sparkle',12)} Sugerir texto com bairros próximos</span><span class="muted" style="font-size:12px;margin-left:auto">312 de 600</span></div></div>
  <div class="card"><div class="hd"><h3>Tratamentos oferecidos</h3><span class="sub">escolha da lista da rede, a descrição é padrão</span></div>
  <div class="g" style="grid-template-columns:1fr 1fr;gap:10px">'''+''.join(f'<div style="display:flex;align-items:center;gap:10px;border:1px solid {"var(--lilas-300)" if on else "var(--linha)"};border-radius:12px;padding:10px 12px;{"background:#fdf8fb" if on else ""}"><span style="width:34px;height:20px;border-radius:20px;background:{"var(--magenta)" if on else "#ddd2e2"};position:relative;flex:none"><span style="position:absolute;top:2px;{"right:2px" if on else "left:2px"};width:16px;height:16px;border-radius:50%;background:#fff"></span></span><b style="font-weight:500;flex:1">{n}</b>{f"<span class=\'pill {"l" if x=="Destaque" else "a"}\'>{x}</span>" if x else ""}</div>' for n,on,x in trat)+f'''</div></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card" style="background:linear-gradient(160deg,#fff,#fdf0f6)"><div class="hd"><h3>Página completa</h3></div>
  <div style="display:flex;align-items:center;gap:14px">{donut([90,10],['#b0197e','#f6e1ec'],tam=104,esp=13,centro='90%',sub='')}<div><b>Falta pouco</b><div class="muted" style="font-size:12px">Complete o FAQ para chegar a 100% e ganhar o selo de página completa.</div></div></div>
  <div class="lista-i" style="margin-top:8px">'''+''.join(f'<div class="it" style="padding:7px 0"><span class="ic {c}" style="width:22px;height:22px;border-radius:7px">{i("check" if c=="v" else "plus",12)}</span><span style="flex:1">{t}</span>{"" if c=="v" else "<span class=\'btn s\'>Fazer</span>"}</div>' for c,t in [('v','Contato e WhatsApp'),('v','Horários'),('v','6 tratamentos'),('v','8 fotos'),('l','FAQ: faltam 3 perguntas')])+f'''</div></div>
  <div class="card"><div class="hd"><h3>{i('clock',15)} Em aprovação</h3></div><div class="muted" style="font-size:12px;line-height:1.6">Texto do bloco Sobre e 2 fotos novas, enviados hoje às 10:42. A rede responde em até 1 dia útil. Você recebe aviso por e-mail e no sino.</div></div>
  <div class="card" style="background:var(--lilas-50);box-shadow:none"><div class="hd"><h3>{i('book',15)} Regras da marca</h3></div><div class="lista-i" style="font-size:12px">'''+''.join(f'<div class="it" style="padding:6px 0">{i("x",12)} {t}</div>' for t in ['Preço ou promoção no texto','Marca de equipamento','Promessa de resultado'])+'''<div class="it" style="padding:6px 0;color:var(--verde)">'''+i('check',12)+''' Use "avaliação gratuita"</div></div></div>
 </div>
</div>'''
salvar('13-franqueado-minha-unidade',pagina('Minha unidade',app('franq','unidade',cont)))

# 14 TEMPLATES
def mini(tipo):
    # miniatura de página em SVG simplificado
    g='#b0197e'
    if tipo=='A':
        return f'''<svg viewBox="0 0 300 380" width="100%"><rect width="300" height="380" fill="#fff"/><rect width="300" height="22" fill="#fff"/><rect x="12" y="7" width="34" height="8" rx="2" fill="#6f0052"/><rect y="22" width="300" height="150" fill="url(#ga)"/>
<defs><linearGradient id="ga" x1="0" x2="1"><stop offset="0" stop-color="#4c1455"/><stop offset="1" stop-color="#b0197e"/></linearGradient></defs>
<rect x="16" y="50" width="120" height="12" rx="3" fill="#fff"/><rect x="16" y="68" width="100" height="12" rx="3" fill="#fff"/><rect x="16" y="90" width="110" height="6" rx="3" fill="#f3c6e0"/><rect x="16" y="100" width="90" height="6" rx="3" fill="#f3c6e0"/>
<rect x="160" y="40" width="124" height="118" rx="10" fill="#fff"/><rect x="170" y="54" width="104" height="14" rx="4" fill="#f1e8f4"/><rect x="170" y="74" width="104" height="14" rx="4" fill="#f1e8f4"/><rect x="170" y="94" width="104" height="14" rx="4" fill="#f1e8f4"/><rect x="170" y="120" width="104" height="22" rx="6" fill="{g}"/>
<rect x="16" y="190" width="80" height="9" rx="3" fill="#24082c"/>''' + ''.join(f'<rect x="{16+k*92}" y="210" width="84" height="70" rx="8" fill="#f8f2fa"/><rect x="{24+k*92}" y="258" width="50" height="6" rx="3" fill="#cdb7d6"/>' for k in range(3)) + '''<rect x="16" y="296" width="268" height="34" rx="8" fill="#f8f2fa"/><rect x="16" y="338" width="268" height="30" rx="8" fill="#24082c"/></svg>'''
    if tipo=='B':
        return f'''<svg viewBox="0 0 300 380" width="100%"><rect width="300" height="380" fill="#fff"/><rect x="12" y="7" width="34" height="8" rx="2" fill="#6f0052"/><image href="../assets/fachada.jpg" x="0" y="22" width="300" height="140" preserveAspectRatio="xMidYMid slice"/><rect y="22" width="300" height="140" fill="#4c1455" opacity=".35"/>
<rect x="16" y="110" width="150" height="12" rx="3" fill="#fff"/><rect x="16" y="128" width="90" height="16" rx="8" fill="{g}"/>
''' + ''.join(f'<rect x="{16+k*68}" y="176" width="62" height="62" rx="8" fill="#e9dcef"/>' for k in range(4)) + '''<rect x="16" y="252" width="100" height="9" rx="3" fill="#24082c"/><rect x="16" y="268" width="268" height="6" rx="3" fill="#e6dcea"/><rect x="16" y="280" width="220" height="6" rx="3" fill="#e6dcea"/><rect x="16" y="300" width="130" height="60" rx="8" fill="#f8f2fa"/><rect x="154" y="300" width="130" height="60" rx="8" fill="#f8f2fa"/></svg>'''
    return f'''<svg viewBox="0 0 300 380" width="100%"><rect width="300" height="380" fill="#fff"/><rect x="12" y="7" width="34" height="8" rx="2" fill="#6f0052"/><rect y="22" width="300" height="110" fill="#fbf4f8"/>
<rect x="16" y="44" width="170" height="12" rx="3" fill="#24082c"/><rect x="16" y="62" width="120" height="12" rx="3" fill="#24082c"/><rect x="16" y="86" width="60" height="16" rx="8" fill="{g}"/><circle cx="240" cy="78" r="36" fill="#e9dcef"/><rect x="200" y="112" width="80" height="12" rx="6" fill="#fff" stroke="#e6dcea"/>
<rect x="16" y="146" width="268" height="90" rx="8" fill="#eef2f0"/><circle cx="150" cy="186" r="7" fill="{g}"/>
<rect x="16" y="248" width="120" height="9" rx="3" fill="#24082c"/>''' + ''.join(f'<rect x="16" y="{266+k*24}" width="268" height="18" rx="5" fill="#f8f2fa"/>' for k in range(4)) + '''</svg>'''
tpls=[('A','Conversão direta','Formulário na primeira dobra e poucos blocos. Para unidades que dependem de anúncio.','Maior taxa de envio na rede: 8,4%',['Formulário no topo','Tratamentos em cards','Prova social','Como chegar'],False),
('B','Vitrine da clínica','Foto da fachada em destaque, galeria e equipe. Para unidades com espaço bonito e boas fotos.','Mais tempo na página: 2 min 31 s',['Foto em destaque','Galeria','Equipe','Avaliações'],True),
('C','Autoridade local','Mapa, bairros atendidos e FAQ longo. Para unidades que querem crescer no Google Maps.','Mais visitas orgânicas: +34%',['Mapa e bairros','FAQ local longo','Avaliações Google','Horários'],False)]
cards=''
for t,n,d,m,bl,atual in tpls:
    cards+=f'''<div class="card" style="padding:0;overflow:hidden;{"border:2px solid var(--magenta);box-shadow:0 14px 34px rgba(176,25,126,.18)" if atual else ""}">
<div style="background:linear-gradient(160deg,#f6eef8,#fdf3f8);padding:22px 34px 0;position:relative">{"<span class='pill' style='position:absolute;right:14px;top:12px;background:var(--magenta);color:#fff'>Em uso</span>" if atual else ""}<div style="border-radius:12px 12px 0 0;overflow:hidden;box-shadow:0 10px 30px rgba(36,8,44,.14);height:300px">{mini(t)}</div></div>
<div style="padding:18px 20px"><div style="display:flex;align-items:center;gap:10px"><span class="pop" style="width:30px;height:30px;border-radius:9px;background:var(--grad);color:#fff;display:grid;place-items:center;font-weight:600">{t}</span><h3 style="font-size:16px">{n}</h3></div>
<p class="muted" style="margin:8px 0 10px;line-height:1.55">{d}</p><div class="pill v" style="margin-bottom:12px">{i('trend',11)} {m}</div>
<div style="display:flex;gap:6px;flex-wrap:wrap;margin-bottom:16px">'''+''.join(f'<span class="chip" style="padding:4px 9px">{b}</span>' for b in bl)+f'''</div>
<div style="display:flex;gap:8px">{"<span class='btn' style='flex:1;justify-content:center'>"+i('edit',14)+" Editar blocos</span>" if atual else "<span class='btn' style='flex:1;justify-content:center'>"+i('eye',14)+" Pré-visualizar</span><span class='btn p' style='flex:1;justify-content:center'>Usar este</span>"}</div></div></div>'''
cont=f'''
<div class="cab"><div><h1>Escolha o modelo da sua página</h1><p>Três modelos aprovados pela rede. Seus dados, fotos e tratamentos entram sozinhos. Pode trocar quando quiser, com aprovação.</p></div>
<div class="dir"><span class="sw"><span class="on">{i('monitor',13)} Computador</span><span>{i('phone2',13)} Celular</span></span></div></div>
<div class="g" style="grid-template-columns:repeat(3,1fr);gap:20px">{cards}</div>
<div class="card" style="margin-top:18px;display:flex;align-items:center;gap:14px;background:var(--lilas-50);box-shadow:none"><div class="ic l">{i('sparkle',16)}</div><div style="flex:1"><b>Recomendação para a GiO Alto da Lapa</b><div class="muted" style="font-size:12px">Você tem 8 fotos e nota 4,9. O modelo B mostra isso melhor. Se quiser mais leads de anúncio, teste o A por 30 dias e compare no relatório.</div></div><span class="btn s">Comparar A e B</span></div>'''
salvar('14-franqueado-templates',pagina('Templates',app('franq','landing',cont)))

# 15 EDITOR DE BLOCOS
blocos=[('Topo e formulário',True,'Fixo'),('Faixa de confiança',True,'Fixo'),('Sobre a unidade',False,'Editável'),('Galeria de fotos',False,'Editável'),('Tratamentos',False,'Editável'),('Equipe',False,'Opcional'),('Avaliações Google',False,'Auto'),('Como chegar',False,'Auto'),('FAQ local',False,'Editável'),('Rodapé e privacidade',True,'Fixo')]
lista=''.join(f'''<div style="display:flex;align-items:center;gap:10px;padding:10px 12px;border-radius:11px;border:1px solid {"var(--magenta)" if n=="Sobre a unidade" else "var(--linha)"};{"background:#fdf3f8" if n=="Sobre a unidade" else "background:#fff"};margin-bottom:7px"><span style="color:#c4b3cc">{i('drag',14) if not lock else i('lock',13)}</span><span style="flex:1;font-weight:500;{"color:var(--tinta-3)" if lock else ""}">{n}</span><span class="pill {"z" if lock else ("l" if t=="Editável" else ("b" if t=="Auto" else "a"))}">{t}</span></div>''' for n,lock,t in blocos)
preview=f'''<div style="background:#fff;border-radius:12px;overflow:hidden;box-shadow:0 20px 50px rgba(36,8,44,.16);width:500px;margin:0 auto">
<div style="height:30px;background:#f3eef5;display:flex;align-items:center;gap:6px;padding:0 12px"><i style="width:9px;height:9px;border-radius:50%;background:#e5b9cf"></i><i style="width:9px;height:9px;border-radius:50%;background:#e9d7a6"></i><i style="width:9px;height:9px;border-radius:50%;background:#bfe0cc"></i><span style="margin-left:12px;font-size:11px;color:var(--tinta-3);background:#fff;padding:3px 10px;border-radius:6px">gioaltodalapa.com.br</span></div>
<div style="display:flex;align-items:center;padding:10px 18px"><img src="../assets/logo-gio.png" style="height:28px"><span style="margin-left:auto;font-size:11px;color:var(--tinta-3)">Tratamentos · Sobre · Dúvidas</span></div>
<div style="height:170px;background:url(../assets/fachada.jpg) center 35%/cover;position:relative"><div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(76,20,85,.85),rgba(76,20,85,.2))"></div><div style="position:absolute;left:22px;top:38px;color:#fff;max-width:280px"><div class="pop" style="font-size:22px;font-weight:600;line-height:1.2">GiO Alto da Lapa</div><div style="font-size:12px;opacity:.9;margin:6px 0 12px">Depilação a laser e estética na Vila Ida</div><span style="background:#fff;color:var(--vinho);font-weight:600;font-size:12px;padding:7px 12px;border-radius:8px">Agendar avaliação gratuita</span></div></div>
<div style="padding:16px 22px;outline:2px solid var(--magenta);outline-offset:-6px;border-radius:10px;margin:10px;position:relative"><span class="pill" style="position:absolute;top:-2px;right:14px;background:var(--magenta);color:#fff">Editando · Sobre</span>
<div class="pop" style="font-weight:600;font-size:16px;margin-bottom:6px">Sobre a unidade</div><div style="font-size:12px;line-height:1.7;color:var(--tinta-2)">A GiO Alto da Lapa fica na Av. São Gualter e atende a região com depilação a laser e tratamentos faciais e corporais. Estamos a 5 minutos da Praça Cornélia, com estacionamento conveniado na rua Tito.</div></div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px;padding:0 22px 20px">'''+''.join(f'<div style="height:76px;border-radius:8px;background:url(../assets/fachada.jpg) {p}/cover"></div>' for p in ['20% 30%','60% 50%','40% 70%','10% 60%'])+'''</div></div>'''
cont=f'''
<div class="cab"><div><h1>Página da unidade · editor</h1><p>Modelo B, Vitrine da clínica. Rascunho salvo há 12 segundos.</p></div>
<div class="dir"><span class="sw"><span class="on">{i('monitor',13)} Computador</span><span>{i('phone2',13)} Celular</span></span><span class="btn">{i('eye',14)} Pré-visualizar</span><span class="btn p">{i('send',14)} Enviar para aprovação</span></div></div>
<div class="g" style="grid-template-columns:262px minmax(0,1fr) 282px;gap:16px">
 <div class="card" style="padding:14px"><div class="hd"><h3>Blocos da página</h3><span class="sub" style="margin-left:auto">arraste</span></div>{lista}<span class="btn s" style="width:100%;justify-content:center;margin-top:4px">{i('plus',12)} Adicionar bloco</span></div>
 <div style="background:repeating-linear-gradient(45deg,#f4eef6,#f4eef6 10px,#f7f2f9 10px,#f7f2f9 20px);border-radius:16px;padding:22px 0">{preview}</div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Bloco Sobre</h3><span class="pill l" style="margin-left:auto">Editável</span></div>
  <div class="campo" style="margin-bottom:12px"><label>Título</label><div class="in">Sobre a unidade</div></div>
  <div class="campo" style="margin-bottom:12px"><label>Texto</label><div class="in" style="height:120px;align-items:flex-start;line-height:1.6;font-size:12px">A GiO Alto da Lapa fica na Av. São Gualter e atende a região com depilação a laser e tratamentos faciais e corporais. Estamos a 5 minutos da Praça Cornélia…</div><div class="ajuda">312 de 600 caracteres</div></div>
  <div class="campo"><label>Fundo</label><div style="display:flex;gap:8px">'''+''.join(f'<span style="width:30px;height:30px;border-radius:9px;background:{c};border:2px solid {"var(--magenta)" if k==0 else "var(--linha)"}"></span>' for k,c in enumerate(['#ffffff','#fbf4f8','#f3eaf6','#24082c']))+f'''</div><div class="ajuda">Só cores da paleta da marca</div></div></div>
  <div class="card"><div class="hd"><h3>{i('shield',15)} Verificação da marca</h3></div>
  <div class="lista-i" style="font-size:12px">'''+''.join(f'<div class="it" style="padding:6px 0"><span class="ic {c}" style="width:22px;height:22px;border-radius:7px">{i("check" if c=="v" else "alert",12)}</span>{t}</div>' for c,t in [('v','Sem preço ou promoção'),('v','Sem marca de equipamento'),('v','Endereço igual ao Google'),('v','Fotos com texto alternativo'),('a','Lighthouse estimado 93 · 1 foto pesada')])+'''</div></div>
 </div>
</div>'''
salvar('15-franqueado-editor',pagina('Editor',app('franq','landing',cont)))

# 16 DOMÍNIO
passos=[('Domínio','gioaltodalapa.com.br','v'),('Apontar DNS','2 registros','v'),('Verificar','automático','v'),('Certificado','SSL ativo','v'),('Publicar','ao vivo','l')]
cont=f'''
<div class="cab"><div><h1>Domínio próprio</h1><p>Use um endereço da unidade sem perder o que a página oficial já conquistou no Google.</p></div>
<div class="dir"><span class="btn">{i('book',14)} Passo a passo</span><span class="btn">{i('help',14)} Pedir ajuda</span></div></div>
<div class="card" style="margin-bottom:16px"><div style="display:grid;grid-template-columns:repeat(5,1fr);gap:0;position:relative">'''+''.join(f'<div style="display:flex;align-items:center;gap:10px;position:relative"><span style="width:34px;height:34px;border-radius:50%;display:grid;place-items:center;flex:none;{"background:var(--verde);color:#fff" if c=="v" else "background:linear-gradient(120deg,#b0197e,#e5559f);color:#fff;box-shadow:0 0 0 5px #fbe3ef"}">{i("check",15) if c=="v" else "5"}</span><div><b>{t}</b><div class="muted" style="font-size:12px">{s}</div></div>{"<span style=\'flex:1;height:2px;background:var(--verde);margin:0 12px;opacity:.5\'></span>" if k<4 else ""}</div>' for k,(t,s,c) in enumerate(passos))+f'''</div></div>
<div class="g" style="grid-template-columns:1.2fr 1fr">
 <div class="card"><div class="hd"><h3>Registros no seu provedor de domínio</h3><span class="pill v" style="margin-left:auto">{i('check',11)} Verificado há 14 min</span></div>
 <table class="t" style="border:1px solid var(--linha);border-radius:12px;overflow:hidden"><thead><tr><th>Tipo</th><th>Nome</th><th>Valor</th><th>Status</th></tr></thead><tbody>
 <tr><td><b>A</b></td><td><code>@</code></td><td><code>76.76.21.21</code></td><td><span class="pill v">{i('check',11)} Ok</span></td></tr>
 <tr><td><b>CNAME</b></td><td><code>www</code></td><td><code>unidades.gio.com.br</code></td><td><span class="pill v">{i('check',11)} Ok</span></td></tr>
 <tr><td><b>TXT</b></td><td><code>_verifica</code></td><td><code>gio-un-4127-8f2a</code></td><td><span class="pill v">{i('check',11)} Ok</span></td></tr></tbody></table>
 <div class="card" style="box-shadow:none;background:#fdf8fb;margin-top:14px;padding:14px"><b>Seus outros e-mails continuam funcionando</b><div class="muted" style="font-size:12px;margin-top:3px">Não mexemos nos registros MX. Só os três acima mudam.</div></div>
 <div style="display:flex;gap:10px;margin-top:16px"><span class="btn p">{i('globe',14)} Publicar no domínio</span><span class="btn">{i('refresh',14)} Verificar de novo</span></div></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('target',15)} Como fica no Google</h3></div>
  <div style="display:flex;flex-direction:column;gap:10px">
   <div style="border:1px solid var(--linha);border-radius:12px;padding:12px"><div class="muted" style="font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase">Endereço principal (canônico)</div><div style="display:flex;align-items:center;gap:8px;margin-top:6px"><span class="ic v" style="width:24px;height:24px;border-radius:7px">{i('check',12)}</span><b>gioaltodalapa.com.br</b></div></div>
   <div style="display:flex;justify-content:center;color:var(--tinta-3)">{i('chevd',16)}</div>
   <div style="border:1px dashed var(--lilas-300);border-radius:12px;padding:12px"><div class="muted" style="font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase">Ficha oficial na rede</div><div style="display:flex;align-items:center;gap:8px;margin-top:6px"><span class="ic l" style="width:24px;height:24px;border-radius:7px">{i('link',12)}</span><b>gio.com.br/unidade/altodalapa</b></div><div class="muted" style="font-size:12px;margin-top:6px">Continua no ar para quem busca na lista de unidades, apontando o canônico para o seu domínio. Uma URL oficial por unidade, nunca duas.</div></div>
  </div></div>
  <div class="card"><div class="hd"><h3>{i('pin',15)} Perfil no Google Maps</h3><span class="pill a" style="margin-left:auto">1 ajuste</span></div><div class="muted" style="font-size:12px;line-height:1.6">O site do seu perfil ainda aponta para o endereço antigo. Troque para <b style="color:var(--tinta)">gioaltodalapa.com.br</b> ou peça para a rede fazer por você.</div><span class="btn s" style="margin-top:10px">Pedir para a rede ajustar</span></div>
 </div>
</div>'''
salvar('16-franqueado-dominio',pagina('Domínio',app('franq','dominio',cont)))
print('p4 ok')
