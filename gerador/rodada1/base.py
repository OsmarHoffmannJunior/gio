"""Componentes compartilhados para gerar as telas estáticas (dados fictícios)."""
import json, math, random, os
D=os.path.dirname(os.path.abspath(__file__))+'/..'
random.seed(21)
IC={
'home':'<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
'pin':'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
'map':'<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
'users':'<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
'inbox':'<path d="M3 13l3-8h12l3 8v6a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M3 13h5l1.5 3h5L16 13h5"/>',
'chart':'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
'file':'<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
'help':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.5"/><path d="M5.6 5.6l3.9 3.9M14.5 14.5l3.9 3.9M18.4 5.6l-3.9 3.9M9.5 14.5l-3.9 3.9"/>',
'gear':'<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
'layout':'<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>',
'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
'search':'<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
'bell':'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
'filter':'<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
'plus':'<path d="M12 5v14M5 12h14"/>',
'down':'<path d="M12 4v12M6 10l6 6 6-6M4 20h16"/>',
'check':'<path d="M5 12l5 5L20 7"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
'phone':'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
'wa':'<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.5A8.4 8.4 0 1 1 21 11.5z"/><path d="M9 9.5c.5 2 2 3.6 4.5 4.5l1.2-1.2 2 1-.4 1.6c-3.6.4-7.6-3.4-7.3-7l1.6-.4 1 2z"/>',
'star':'<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9z"/>',
'chev':'<path d="M9 6l6 6-6 6"/>','chevd':'<path d="M6 9l6 6 6-6"/>',
'cal':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
'edit':'<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
'eye':'<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
'lock':'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
'phone2':'<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
'monitor':'<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
'image':'<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="M21 15l-5-5L5 21"/>',
'list':'<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
'grid':'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
'zap':'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
'alert':'<path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
'trend':'<path d="M23 6l-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/>',
'link':'<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
'drag':'<circle cx="9" cy="6" r="1"/><circle cx="15" cy="6" r="1"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><circle cx="9" cy="18" r="1"/><circle cx="15" cy="18" r="1"/>',
'more':'<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
'send':'<path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/>',
'clip':'<path d="M21.4 11l-9.2 9.2a6 6 0 0 1-8.5-8.5l9.2-9.2a4 4 0 0 1 5.7 5.7l-9.2 9.2a2 2 0 0 1-2.8-2.8l8.5-8.5"/>',
'book':'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5V21h16"/>',
'x':'<path d="M18 6L6 18M6 6l12 12"/>',
'sparkle':'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 17l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>',
'target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
'mouse':'<rect x="6" y="3" width="12" height="18" rx="6"/><path d="M12 7v4"/>',
'cursor':'<path d="M4 3l7 17 2.5-7.5L21 10z"/>',
'refresh':'<path d="M21 12a9 9 0 0 1-15.4 6.4L3 16M3 12a9 9 0 0 1 15.4-6.4L21 8"/><path d="M21 3v5h-5M3 21v-5h5"/>',
'log':'<path d="M12 8v4l3 3"/><path d="M3.05 11a9 9 0 1 1 .5 4"/><path d="M3 4v5h5"/>',
'tag':'<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/>',
'google':'<path d="M21 12.2c0-.7-.1-1.3-.2-1.9H12v3.6h5a4.3 4.3 0 0 1-1.9 2.8v2.3h3A9 9 0 0 0 21 12.2z"/><path d="M12 21a8.9 8.9 0 0 0 6.1-2.2l-3-2.3a5.5 5.5 0 0 1-8.2-2.9H3.8v2.4A9 9 0 0 0 12 21z"/><path d="M6.9 13.6a5.4 5.4 0 0 1 0-3.4V7.8H3.8a9 9 0 0 0 0 8.1z"/><path d="M12 6.6a4.9 4.9 0 0 1 3.5 1.4l2.6-2.6A8.8 8.8 0 0 0 12 3a9 9 0 0 0-8.2 4.8l3.1 2.4A5.4 5.4 0 0 1 12 6.6z"/>',
}
def i(n,s=16,cls=''): return f'<svg class="i {cls}" viewBox="0 0 24 24" style="width:{s}px;height:{s}px">{IC[n]}</svg>'
U=json.load(open(f'{D}/../raw/api-listagem.json'))['unidades']
UNID=[v for v in U.values()]
def pagina(titulo,corpo,largura=1440,extra_css=''):
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{titulo}</title>
<link rel="stylesheet" href="estilo.css"><style>body{{width:{largura}px}}{extra_css}</style></head><body>{corpo}</body></html>'''
NAV_ADMIN=[('sec','Rede'),('home','Visão geral','rede'),('pin','Unidades','unidades','130'),('shield','Aprovações','aprov','7'),
 ('sec','Relacionamento'),('inbox','Central de leads','leads','38'),('help','Suporte','suporte','12'),
 ('sec','Inteligência'),('chart','Relatórios','rel'),('target','SEO local','seo'),
 ('sec','Plataforma'),('layout','Templates e marca','tpl'),('users','Usuários e acessos','users'),('log','Auditoria','aud')]
NAV_FRANQ=[('sec','Minha operação'),('home','Início','inicio'),('pin','Minha unidade','unidade'),('layout','Página da unidade','landing'),('globe','Domínio','dominio'),
 ('sec','Clientes'),('inbox','Leads','leads','9'),('star','Avaliações','aval'),
 ('sec','Apoio'),('chart','Relatórios','rel'),('help','Suporte da rede','suporte','1'),('book','Base de conhecimento','base')]
def side(modo,ativo):
    nav=NAV_ADMIN if modo=='admin' else NAV_FRANQ
    h=['<aside class="side"><div class="logo"><img src="../assets/'+('logo-gio-branco.png' if modo=='admin' else 'logo-gio.png')+'" alt="Gio"><span>'+('Portal da<br>Rede' if modo=='admin' else 'Portal do<br>Franqueado')+'</span></div>']
    if modo=='admin':
        h.append('<div class="ctx"><div class="av">GR</div><div><b>Rede Gio</b><small>130 unidades · Brasil</small></div>'+i('chevd',14)+'</div>')
    else:
        h.append('<div class="ctx"><div class="av">AL</div><div><b>GiO Alto da Lapa</b><small>São Paulo/SP · Full</small></div>'+i('chevd',14)+'</div>')
    for it in nav:
        if it[0]=='sec': h.append(f'<div class="sec">{it[1]}</div>'); continue
        n=f'<span class="n">{it[3]}</span>' if len(it)>3 else ''
        h.append(f'<a class="{"on" if it[2]==ativo else ""}">{i(it[0],17)}{it[1]}{n}</a>')
    pessoa=('IN','Ingrid N.','Marketing da rede') if modo=='admin' else ('RF','Renata F.','Franqueada')
    h.append(f'<div class="rodape"><div class="av">{pessoa[0]}</div><div><b>{pessoa[1]}</b><small>{pessoa[2]}</small></div><span style="margin-left:auto">{i("gear",16)}</span></div></aside>')
    return ''.join(h)
def topo(placeholder='Buscar unidade, lead, ticket ou pessoa'):
    return f'''<div class="top"><div class="busca">{i('search')}<span>{placeholder}</span><kbd>Ctrl K</kbd></div>
<div class="acoes"><span class="chip">{i('cal',14)} 01 a 21 nov 2026 {i('chevd',12)}</span><div class="ib">{i('help')}</div><div class="ib">{i('bell')}<span class="dot"></span></div></div></div>'''
def app(modo,ativo,conteudo,placeholder=None):
    return f'<div class="app {modo}">{side(modo,ativo)}<main class="main">{topo(placeholder or ("Buscar unidade, lead, ticket ou pessoa" if modo=="admin" else "Buscar lead, ticket ou artigo"))}{conteudo}</main></div>'
# ---------- gráficos SVG ----------
def area(series,cores,w=640,h=200,labels=None,ymax=None,grade=4):
    n=len(series[0]); ymax=ymax or max(max(s) for s in series)*1.15
    px=lambda k: 36+k*(w-46)/(n-1); py=lambda v: h-24-(v/ymax)*(h-40)
    out=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}">','<defs>']
    for k,c in enumerate(cores):
        out.append(f'<linearGradient id="ga{k}{w}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c}" stop-opacity=".28"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>')
    out.append('</defs>')
    for g in range(grade+1):
        y=16+g*(h-40)/grade; v=ymax*(1-g/grade)
        out.append(f'<line x1="36" x2="{w-10}" y1="{y:.1f}" y2="{y:.1f}" stroke="#eee6f1"/><text x="28" y="{y+4:.1f}" font-size="10" fill="#9b90a3" text-anchor="end" font-family="Inter">{int(v)}</text>')
    for k,(s,c) in enumerate(zip(series,cores)):
        pts=' '.join(f'{px(j):.1f},{py(v):.1f}' for j,v in enumerate(s))
        out.append(f'<polygon points="{px(0):.1f},{h-24} {pts} {px(n-1):.1f},{h-24}" fill="url(#ga{k}{w})"/><polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.4" stroke-linejoin="round"/>')
    if labels:
        step=max(1,n//7)
        for j in range(0,n,step): out.append(f'<text x="{px(j):.1f}" y="{h-6}" font-size="10" fill="#9b90a3" text-anchor="middle" font-family="Inter">{labels[j]}</text>')
    out.append('</svg>'); return ''.join(out)
def barras_h(itens,cor='url(#gb)',w=300,larg_rot=120,alt=26,fmt=str):
    mx=max(v for _,v in itens); h=len(itens)*alt
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}"><defs><linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="#4c1455"/><stop offset="1" stop-color="#b0197e"/></linearGradient></defs>']
    for k,(r,v) in enumerate(itens):
        y=k*alt; bw=(w-larg_rot-46)*v/mx
        o.append(f'<text x="0" y="{y+16}" font-size="11.5" fill="#4a3f52" font-family="Inter">{r}</text><rect x="{larg_rot}" y="{y+6}" width="{w-larg_rot-46}" height="12" rx="6" fill="#f3eaf6"/><rect x="{larg_rot}" y="{y+6}" width="{bw:.1f}" height="12" rx="6" fill="{cor}"/><text x="{w}" y="{y+16}" font-size="11.5" fill="#1d1424" text-anchor="end" font-weight="600" font-family="Inter">{fmt(v)}</text>')
    o.append('</svg>'); return ''.join(o)
def donut(partes,cores,tam=150,esp=20,centro='',sub=''):
    tot=sum(partes); r=(tam-esp)/2; c=tam/2; ang=-math.pi/2; o=[f'<svg viewBox="0 0 {tam} {tam}" width="{tam}" height="{tam}">']
    for v,cor in zip(partes,cores):
        a2=ang+2*math.pi*v/tot; large=1 if a2-ang>math.pi else 0
        x1,y1=c+r*math.cos(ang),c+r*math.sin(ang); x2,y2=c+r*math.cos(a2-0.02),c+r*math.sin(a2-0.02)
        o.append(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 {large} 1 {x2:.1f} {y2:.1f}" stroke="{cor}" stroke-width="{esp}" fill="none" stroke-linecap="butt"/>'); ang=a2
    o.append(f'<text x="{c}" y="{c+2}" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="22" fill="#1d1424">{centro}</text><text x="{c}" y="{c+20}" text-anchor="middle" font-family="Inter" font-size="10.5" fill="#7d7286">{sub}</text></svg>')
    return ''.join(o)
def spark(vals,cor='#b0197e',w=90,h=28):
    mx,mn=max(vals),min(vals); pts=' '.join(f'{k*(w-4)/(len(vals)-1)+2:.1f},{h-3-(v-mn)/(mx-mn or 1)*(h-6):.1f}' for k,v in enumerate(vals))
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}"><polyline points="{pts}" fill="none" stroke="{cor}" stroke-width="2" stroke-linejoin="round"/></svg>'
def funil(etapas,w=520):
    mx=etapas[0][1]; o=['<div style="display:flex;flex-direction:column;gap:8px">']
    for k,(r,v,extra) in enumerate(etapas):
        pct=v/mx*100
        o.append(f'<div style="display:grid;grid-template-columns:150px 1fr 120px;align-items:center;gap:12px"><span style="font-weight:500;color:#4a3f52">{r}</span><div style="background:#f3eaf6;border-radius:9px;height:30px;position:relative"><div style="width:{pct:.1f}%;height:100%;border-radius:9px;background:linear-gradient(90deg,#4c1455,{["#6f0052","#86106b","#9d1777","#b0197e","#c43a8f"][k%5]});opacity:{1-k*0.08:.2f}"></div><span style="position:absolute;left:10px;top:6px;color:#fff;font:600 12px Inter">{v:,}</span></div><span class="muted" style="font-size:12px">{extra}</span></div>'.replace(',','.'))
    o.append('</div>'); return ''.join(o)
BR=[(4.4,-51.6),(1.8,-50.0),(-0.5,-48.5),(-1.0,-46.0),(-2.5,-44.3),(-2.9,-41.5),(-3.7,-38.5),(-5.0,-36.3),(-5.8,-35.2),(-8.0,-34.8),(-10.5,-36.3),(-13.0,-38.5),(-15.5,-38.9),(-18.0,-39.6),(-20.3,-40.3),(-22.0,-41.0),(-23.0,-43.2),(-23.8,-45.5),(-25.3,-48.2),(-26.9,-48.6),(-28.5,-48.8),(-30.0,-50.2),(-32.0,-52.0),(-33.7,-53.4),(-32.5,-53.6),(-30.2,-57.6),(-27.5,-55.6),(-25.5,-54.6),(-24.0,-54.3),(-22.5,-55.6),(-22.2,-58.0),(-20.0,-58.2),(-17.6,-57.8),(-16.3,-60.2),(-15.0,-60.3),(-13.5,-61.8),(-12.5,-64.0),(-11.0,-65.4),(-10.0,-67.0),(-11.0,-69.8),(-9.4,-72.8),(-7.4,-73.9),(-4.4,-70.0),(-2.0,-69.5),(-1.0,-69.4),(1.2,-69.9),(1.7,-67.0),(2.2,-64.0),(4.0,-64.5),(5.2,-60.7),(2.0,-56.0),(2.3,-54.5),(4.4,-51.6)]
def proj(lat,lng,w,h,box=(-34.5,5.8,-74.5,-34.0)):
    la0,la1,lo0,lo1=box; return (lng-lo0)/(lo1-lo0)*w, (la1-lat)/(la1-la0)*h
def mapa_br(w,h,pontos,box=(-34.5,5.8,-74.5,-34.0),contorno=True):
    o=[f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="display:block">']
    if contorno:
        pts=' '.join('%.1f,%.1f'%proj(a,b,w,h,box) for a,b in BR)
        o.append(f'<polygon points="{pts}" fill="#f3eaf6" stroke="#d9c3e1" stroke-width="1.5"/>')
    for (lat,lng,cor,r) in pontos:
        x,y=proj(lat,lng,w,h,box)
        if -5<x<w+5 and -5<y<h+5: o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{cor}" fill-opacity=".85" stroke="#fff" stroke-width="1.2"/>')
    o.append('</svg>'); return ''.join(o)
def score(u):
    rnd=random.Random(u['url_site']); base=40+rnd.random()*55
    return int(base)
def salvar(nome,html):
    open(f'{D}/telas/{nome}.html','w',encoding='utf-8').write(html)

import re as _re
def nome_un(u, curto=30):
    n=u['unidade']
    n=_re.sub(r'^(Sp|Rj|Mg|Pr|Rs|Sc|Go|Df|Ba|Ce|Pe|Ma|Es|Ms|Mt|Pa|Am|Rn|Pb|Al|Se|Pi|To|Ro)\s+','',n)
    n=n.replace(' Da ',' da ').replace(' Do ',' do ').replace(' De ',' de ')
    return ('GiO '+n)[:curto]
