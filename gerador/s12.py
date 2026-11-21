"""Hub de relatórios da rede: tela 13 (visão executiva) e subtelas 90 a 99. Spec 005. Dados fictícios de rel_dados.py."""
from rel_dados import *
import json as _json
K={'rel':'13-admin-relatorios','rel-camp':'90-admin-relatorios-campanhas','rel-funil':'91-admin-relatorios-leads-funil','rel-atend':'92-admin-relatorios-atendimento',
   'rel-trafego':'93-admin-relatorios-quiz-landings','rel-google':'94-admin-relatorios-seo-avaliacoes','rel-cliente':'95-admin-relatorios-area-cliente',
   'rel-unidades':'96-admin-relatorios-unidades','rel-unidade':'97-admin-relatorios-unidade','rel-config':'89-admin-relatorios-metas-regras','f-rel':'97-franqueado-relatorio-unidade','rel-metas':'98-admin-relatorios-metas-alertas','rel-export':'99-admin-relatorios-exportar'}
def LK(k): return (K.get(k) or ARQ[k])+'.html'
def U97(x): return LK('rel-unidade')+'?unidade='+x['slug']
SECOES=[('rel','Visão executiva'),('rel-camp','Aquisição e campanhas'),('rel-funil','Leads e funil'),('rel-atend','Atendimento'),('rel-trafego','Quiz, landings e tráfego'),
        ('rel-google','SEO local e avaliações'),('rel-cliente','Área do cliente'),('rel-unidades','Unidades e regiões'),('rel-metas','Metas e alertas'),('rel-export','Exportar e agendar')]
def nav(on): return '<nav class="tabs rr-tabs" aria-label="Seções do hub de relatórios">'+''.join(f'<a class="{"on" if k==on else ""}" href="{LK(k)}"{" aria-current=page" if k==on else ""}>{t}</a>' for k,t in SECOES)+'</nav>'
ST={'s':('v','Do sistema'),'i':('b','Integração'),'c':('a','Depende da Salus'),'f':('z','Fase 2')}
def st(*cods): return ''.join(f'<span class="pill {ST[c][0]} rr-st">{ST[c][1]}</span>' for c in cods)
def fonte(txt,quando=ATU,*cods):
    return f'<div class="rr-fonte">{i("clock",12)}<span><b>Fonte:</b> {txt} · atualizado {quando} (horário de Brasília)</span><span class="rr-stw">{st(*cods)}</span></div>'
def card(tit,corpo,fon='',sub='',dir='',cls='',id_=''):
    return f'<section class="card {cls}"{f" id={id_}" if id_ else ""}><div class="hd"><h3>{tit}</h3>{f"<span class=sub>{sub}</span>" if sub else ""}{f"<div class=dir>{dir}</div>" if dir else ""}</div>{corpo}{fon}</section>'
def kv(ic,rot,val,dlt='',det='',cods='s',bom=True,sp=None,href=None,alerta=False):
    sinal=''
    if dlt:
        s,v=dlt
        if bom is None: sinal=f'<span class="rr-neu">{s}</span>'
        else: ok=(v>=0)==bom; sinal=f'<span class="{"up" if ok else "down"}">{s}</span>'
    spk=f'<div class="rr-sp">{spark(sp,"#b0197e",84,24)}</div>' if sp else ''
    tag,attr=('a',f' href="{href}"') if href else ('div','')
    cls=' kpi-a' if href else ''
    cls+=' alerta' if alerta else ''
    return f'<{tag} class="card kpi rr-k{cls}"{attr}><div class="l">{i(ic,15)} {rot}</div><div class="v">{val}</div><div class="d">{sinal} {det}</div>{spk}<div class="rr-kst">{st(*cods)}</div></{tag}>'
def hbar(itens,fmtv=fmt,cor='var(--grad)',extra=None,mx=None):
    """barras horizontais em HTML (responsivas). itens: (rótulo, valor[, cor, texto extra])"""
    mx=mx or max(v for _,v,*r in itens)
    o=['<div class="rr-hb">']
    for it in itens:
        r,v=it[0],it[1]; c=it[2] if len(it)>2 and it[2] else cor; ex=it[3] if len(it)>3 else ''
        o.append(f'<div class="rr-hr"><span class="rr-hl">{r}</span><span class="rr-ht"><i style="width:{max(1.5,v/mx*100):.1f}%;background:{c}"></i></span><b class="rr-hv">{fmtv(v)}</b>{f"<span class=rr-hx>{ex}</span>" if ex else ""}</div>')
    o.append('</div>'); return ''.join(o)
def funil2(etapas,bench=None):
    """etapas: (rótulo, valor, texto da conversão). Barras proporcionais com a conversão entre etapas."""
    mx=etapas[0][1]; o=['<div class="rr-fu">']
    for k,(r,v,cv) in enumerate(etapas):
        o.append(f'<div class="rr-fr"><span class="rr-fl">{r}</span><span class="rr-ft"><i style="width:{v/mx*100:.1f}%"></i></span><b>{fmt(v)}</b><span class="meta rr-fc">{cv}</span></div>')
    o.append('</div>'); return ''.join(o)
def linha(series,labels,w=720,h=240,ymax=None,passo=None,fmty=fmt,area_k=0,band=None):
    """series: (valores, cor, tracejado, rótulo). None = sem ponto. band: (i0, lo[], hi[]) faixa de previsão."""
    vals=[v for s in series for v in s[0] if v is not None]+([v for v in band[2]] if band else [])
    ymax=ymax or max(vals)*1.12; n=len(labels); L0=46
    px=lambda k: L0+k*(w-L0-12)/(n-1); py=lambda v: h-26-(v/ymax)*(h-44)
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" role="img" aria-label="Série temporal">']
    for g in range(5):
        y=18+g*(h-44)/4; v=ymax*(1-g/4)
        o.append(f'<line x1="{L0}" x2="{w-8}" y1="{y:.1f}" y2="{y:.1f}" stroke="#eee6f1"/><text x="{L0-6}" y="{y+4:.1f}" font-size="12" fill="#5E5566" text-anchor="end" font-family="Inter">{fmty(round(v))}</text>')
    if band:
        i0,lo,hi=band; pts=[f'{px(i0+k):.1f},{py(v):.1f}' for k,v in enumerate(hi)]+[f'{px(i0+k):.1f},{py(v):.1f}' for k,v in reversed(list(enumerate(lo)))]
        o.append(f'<polygon points="{" ".join(pts)}" fill="#b0197e" fill-opacity=".12"/>')
    for k,(s,c,dash,_) in enumerate(series):
        pts=[(px(j),py(v)) for j,v in enumerate(s) if v is not None]
        if k==area_k and not dash:
            o.append(f'<polygon points="{pts[0][0]:.1f},{h-26} '+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+f' {pts[-1][0]:.1f},{h-26}" fill="{c}" fill-opacity=".10"/>')
        o.append(f'<polyline points="{" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)}" fill="none" stroke="{c}" stroke-width="2.4" stroke-linejoin="round"{" stroke-dasharray=\"6 5\"" if dash else ""}/>')
    passo=passo or max(1,round(n/7))
    for j in range(0,n,passo): o.append(f'<text x="{px(j):.1f}" y="{h-7}" font-size="12" fill="#5E5566" text-anchor="middle" font-family="Inter">{labels[j]}</text>')
    o.append('</svg>'); return ''.join(o)
def dupla(fn_desk,fn_mob): return f'<div class="rr-dk">{fn_desk}</div><div class="rr-mb">{fn_mob}</div>'
def leg(itens): return '<div class="leg rr-leg">'+''.join(f'<span><i style="background:{c}{";opacity:.55" if d else ""}"></i>{t}</span>' for t,c,d in itens)+'</div>'
def colunas(vals,labels,cor_on='#b0197e',w=720,h=230,linha_aa=None,destaque=None,proj=None):
    mx=max([v for v in vals if v]+(linha_aa or [])+([proj] if proj else []))*1.15; n=len(vals); L0=46; bw=(w-L0-10)/n
    py=lambda v: h-26-(v/mx)*(h-44)
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" role="img" aria-label="Colunas por mês">']
    for g in range(5):
        y=18+g*(h-44)/4; v=mx*(1-g/4); o.append(f'<line x1="{L0}" x2="{w-8}" y1="{y:.1f}" y2="{y:.1f}" stroke="#eee6f1"/><text x="{L0-6}" y="{y+4:.1f}" font-size="12" fill="#5E5566" text-anchor="end" font-family="Inter">{fmt(round(v))}</text>')
    for k,v in enumerate(vals):
        x=L0+k*bw+bw*0.18
        if v is None and proj:
            o.append(f'<rect x="{x:.1f}" y="{py(proj):.1f}" width="{bw*0.64:.1f}" height="{h-26-py(proj):.1f}" rx="5" fill="#fff" stroke="#b0197e" stroke-dasharray="5 4" stroke-width="1.6"/>')
        elif v: o.append(f'<rect x="{x:.1f}" y="{py(v):.1f}" width="{bw*0.64:.1f}" height="{h-26-py(v):.1f}" rx="5" fill="{cor_on if k!=destaque else "#4c1455"}"/>')
        if k%max(1,round(n/7))==0 or n<=12: o.append(f'<text x="{x+bw*0.32:.1f}" y="{h-7}" font-size="12" fill="#5E5566" text-anchor="middle" font-family="Inter">{labels[k]}</text>')
    if linha_aa:
        pts=' '.join(f'{L0+k*bw+bw/2:.1f},{py(v):.1f}' for k,v in enumerate(linha_aa))
        o.append(f'<polyline points="{pts}" fill="none" stroke="#2C5BC4" stroke-width="2.2" stroke-dasharray="6 4"/>')
    o.append('</svg>'); return ''.join(o)
def dispersao(pts,w=560,h=300,xr=None,yr=None,xl='',yl='',fx=str,fy=str,refx=None,refy=None):
    """pts: (x, y, raio, cor, rótulo curto)"""
    x0,x1=xr; y0,y1=yr; L0=48
    PX=lambda v: L0+(v-x0)/(x1-x0)*(w-L0-14); PY=lambda v: h-34-(v-y0)/(y1-y0)*(h-50)
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" role="img" aria-label="Dispersão">']
    for g in range(5):
        yv=y0+(y1-y0)*g/4; xv=x0+(x1-x0)*g/4
        o.append(f'<line x1="{L0}" x2="{w-10}" y1="{PY(yv):.1f}" y2="{PY(yv):.1f}" stroke="#eee6f1"/><text x="{L0-6}" y="{PY(yv)+4:.1f}" font-size="12" fill="#5E5566" text-anchor="end" font-family="Inter">{fy(yv)}</text>')
        o.append(f'<text x="{PX(xv):.1f}" y="{h-16}" font-size="12" fill="#5E5566" text-anchor="middle" font-family="Inter">{fx(xv)}</text>')
    if refx is not None: o.append(f'<line x1="{PX(refx):.1f}" x2="{PX(refx):.1f}" y1="14" y2="{h-34}" stroke="#4c1455" stroke-dasharray="4 4"/>')
    if refy is not None: o.append(f'<line x1="{L0}" x2="{w-10}" y1="{PY(refy):.1f}" y2="{PY(refy):.1f}" stroke="#4c1455" stroke-dasharray="4 4"/>')
    for p in pts:
        x,y,r,c,t=p[:5]; href=p[5] if len(p)>5 else None; fm=p[6] if len(p)>6 else 'c'; cx,cy=PX(x),PY(y)
        if fm=='q': el=f'<rect x="{cx-r:.1f}" y="{cy-r:.1f}" width="{2*r}" height="{2*r}" fill="{c}" fill-opacity=".85"><title>{t}</title></rect>'
        elif fm=='d': el=f'<polygon points="{cx:.1f},{cy-r-1:.1f} {cx+r+1:.1f},{cy:.1f} {cx:.1f},{cy+r+1:.1f} {cx-r-1:.1f},{cy:.1f}" fill="{c}" fill-opacity=".85"><title>{t}</title></polygon>'
        elif fm=='o': el=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="#fff" stroke="{c}" stroke-width="2"><title>{t}</title></circle>'
        else: el=f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{c}" fill-opacity="{'.22' if t and r>=8 else '.8'}" stroke="{c if t and r>=8 else '#fff'}" stroke-width="1.5"><title>{t}</title></circle>'
        o.append(f'<a href="{href}">{el}</a>' if href else el)
        if t and r>=8: o.append(f'<text x="{PX(x):.1f}" y="{PY(y)+4:.1f}" font-size="12" font-weight="700" fill="#1d1424" text-anchor="middle" font-family="Inter">{t.split(" ")[0]}</text>')
    o.append(f'<text x="{w-10}" y="{h-2}" font-size="12" fill="#463b4e" text-anchor="end" font-family="Inter">{xl}</text><text x="{L0}" y="11" font-size="12" fill="#463b4e" font-family="Inter">{yl}</text></svg>')
    return ''.join(o)
def mapa_val(w,h,valores,escala,rotulo):
    """coroplético por UF com título próprio de cada estado"""
    import re as _r
    svg=mapa_geo(w,h,[],BOX_BR,cont_uf={k:1 for k in valores},escala=lambda n:'#f7f1f9',rotulos=True,uid='rr')
    for uf,v in valores.items():
        svg=_r.sub(rf'(<path id="BR-{uf}" class="uf" d="[^"]*" fill=")[^"]*(" stroke="#fff" stroke-width="1"><title>)[^<]*',lambda m:m.group(1)+escala(v)+m.group(2)+f'{uf} · {rotulo(v)}',svg)
    return svg
# barra de filtros global (protótipo: seleção funciona; números seguem os da rede, aviso explícito)
UNS_ORD=sorted(UN,key=lambda x:x['nome'])
def filtros(com_unidade=True):
    lst=''.join(f'<label class="rr-op" data-v="{x["slug"]}" data-txt="{x["nome"].lower()} {x["cid"].lower()} {x["uf"].lower()}"><span class="cx"></span><span>{x["nome"]}<small> · {x["cid"]}/{x["uf"]}</small></span></label>' for x in UNS_ORD)
    def f(rot,val,pop=None,dis=False):
        return f'<button type="button" class="rr-f{" dis" if dis else ""}"{f" data-pop={pop}" if pop else ""}{" disabled" if dis else ""}><small>{rot}</small><span>{val}</span>{i("chevd",12)}</button>'
    simples=lambda pid,ops: f'<div class="rr-pop" id="{pid}" hidden>'+''.join(f'<label class="rr-op" data-v="{"" if k==0 else (o[1] if isinstance(o,tuple) else o)}"><span class="cx{" on" if k==0 else ""}"></span><span>{o[0] if isinstance(o,tuple) else o}</span></label>' for k,o in enumerate(ops))+'<div class="rr-pa"><button type="button" class="btn s p" data-apl>Aplicar</button></div></div>'
    return f'''<div class="rr-fbar" data-acao-propria>
<div class="rr-res"><button type="button" class="btn s rr-ftog" aria-expanded="false">{i("filter",14)} Filtros <span class="pill l">rede inteira</span></button>
<span class="rr-rtx" data-res>{PER} · comparado com {PER_ANT} · Gio · 130 unidades</span>
<details class="rr-legd"><summary>{i("eye",13)} Situação dos dados</summary><div class="rr-legp"><p class="meta" style="margin:0 0 6px">Cada bloco mostra a fonte, a hora da última leitura (horário de Brasília) e um selo:</p><div>{st("s")} a plataforma já captura este número.</div><div>{st("i")} depende de API ou da DocBiz; o bloco diz a última leitura e o atraso típico.</div><div>{st("c")} entra quando a Salus informar (meta, orçamento, venda, tarifa).</div><div>{st("f")} entra com as vendas online da área do cliente.</div></div></details></div>
<div class="rr-filtros">
 {f("Período",PER,"p-per")}{f("Comparar com","período anterior","p-cmp")}{f("Marca","Gio","p-marca")}{f("Regional","todas","p-reg")}{f("Estado","todos","p-uf")}{f("Cidade","todas","p-cid")}
 {f("Unidade","todas as 130","p-un") if com_unidade else ""}{f("Fonte","todas","p-fon")}{f("Campanha","todas","p-cam")}{f("Procedimento","todos","p-pro")}
 <button type="button" class="btn s ghost" data-limpa>Limpar</button><button type="button" class="btn s" data-salva>{i("star",13)} Salvar visão</button>
 {simples("p-per",[PER,("Últimos 7 dias","7d"),("Últimos 30 dias","30d"),("Mês anterior","mes-ant"),("Ano até hoje","ano")])}
 {simples("p-cmp",["Período anterior ("+PER_ANT+")",("Mesmo período do ano anterior ("+PER_AA+")","ano-ant"),("Sem comparação","sem")])}
 {simples("p-marca",["Gio","Sorridents (quando entrar no sistema)"])}
 {simples("p-reg",["Todas",*REGS])}
 {simples("p-uf",["Todos"]+[(f"{u} · {n} {'unidade' if n==1 else 'unidades'}",u) for u,n in UF_CONT.most_common()])}
 {simples("p-cid",["Todas","São Paulo","Campinas","Curitiba","Porto Alegre","Goiânia","Belo Horizonte"])}
 {simples("p-fon",["Todas",*[f[1] for f in FONTES]])}
 {simples("p-cam",["Todas",*sorted({c["pl"]+" · "+c["nome"]+" ("+c["esc"]+")" for c in CAMPS})])}
 {simples("p-pro",["Todos",*[p for p,_ in PROC]])}
 <div class="rr-pop rr-pop-un" id="p-un" hidden><div class="rr-busca">{i("search",14)}<input type="search" placeholder="Buscar unidade, cidade ou UF" aria-label="Buscar unidade"></div>
  <div class="rr-sel meta"><span data-cont>0 selecionadas</span> · <a href="#" class="lk" data-todas>marcar as visíveis</a></div><div class="rr-lst">{lst}</div>
  <div class="rr-pa"><button type="button" class="btn s ghost" data-zera>Limpar</button><button type="button" class="btn s p" data-apl>Aplicar</button></div></div>
</div>
<div class="rr-ativos meta" aria-live="polite"></div></div>'''
CSS='''
.rr-tabs{margin-bottom:12px}
.rr-fbar{position:relative;margin-bottom:16px}
.rr-res{display:flex;gap:8px 12px;align-items:center;flex-wrap:wrap}
.rr-ftog{display:inline-flex}.rr-rtx{font-size:13px;color:var(--tinta-2)}
.rr-filtros{display:none!important}.rr-fbar.aberto .rr-filtros{display:flex!important;margin-top:8px}
.rr-legd{position:relative;margin-left:auto}.rr-legd summary{list-style:none;cursor:pointer;display:inline-flex;gap:6px;align-items:center;font:500 13px Inter;color:var(--tinta-2);padding:8px 10px;border-radius:10px;min-height:40px}
.rr-legd summary::-webkit-details-marker{display:none}.rr-legd:not([open]) .rr-legp{display:none}.rr-legd summary:hover{background:var(--lilas-50)}
.rr-legp{position:absolute;right:0;top:calc(100% + 4px);z-index:25;background:#fff;border:1px solid var(--linha-forte);border-radius:12px;box-shadow:0 12px 30px rgba(36,8,44,.18);padding:12px;width:min(380px,calc(100vw - 32px));display:flex;flex-direction:column;gap:6px;font-size:13px}
.rr-demo{display:none}.rr-acoes{display:flex;gap:8px;flex-wrap:nowrap}
.rr-neu{color:var(--tinta-2);font-weight:600}
a.rr-k{color:inherit}a.rr-k:focus-visible{outline:2px solid var(--vinho);outline-offset:2px}
a.rr-k .l::after{content:"›";margin-left:auto;color:var(--tinta-3);font-size:16px;line-height:1}
.rr-ativos{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:8px;padding:8px 12px;border-radius:10px;background:var(--lilas-50);border:1px solid var(--linha);font-size:13px;color:var(--tinta-2)}
.rr-scroll{overflow-x:auto;border:1px solid var(--linha);border-radius:10px}
.rr-scroll table.t thead th{position:sticky;top:var(--rr-top,0px);z-index:2;background:#fff;box-shadow:0 1px 0 var(--linha);white-space:normal;vertical-align:bottom;line-height:1.25}
.rr-scroll table.t td,.rr-scroll table.t th{padding-left:8px;padding-right:8px}
@media(min-width:1100px){.rr-scroll{overflow:visible}}
.rr-pgr{display:flex;gap:6px;align-items:center;flex-wrap:wrap;margin-top:10px}.rr-pgr button{min-width:40px;min-height:40px}.rr-pgr button.on{background:var(--roxo-700);color:#fff;border-color:var(--roxo-700)}
tr.rr-off,table.rr-tr tr.rr-off{display:none!important}
.rr-vazio{padding:24px;text-align:center;border:1px dashed var(--linha-forte);border-radius:12px;margin-top:10px;font-size:14px}
.rr-atraso{display:flex;gap:8px;align-items:flex-start;padding:8px 10px;border-radius:10px;background:#fdf1dc;color:#5c3b00;font-size:13px;margin-bottom:10px}
.rr-man{background:linear-gradient(120deg,#fff 0%,#fbf5fd 100%);border-left:4px solid var(--vinho)}
.rr-man h2{font:600 20px/1.35 Poppins;margin:4px 0 6px;color:var(--tinta)}.rr-man p{margin:0;font-size:14px;color:var(--tinta-2)}
.rr-explica{font-size:13px;color:var(--tinta-2);margin:-6px 0 16px;padding:10px 12px;background:#fff;border:1px solid var(--linha);border-radius:10px}
.rr-filtros{display:flex;flex-wrap:wrap;gap:8px;align-items:center;background:#fff;border:1px solid var(--linha);border-radius:14px;padding:10px;box-shadow:var(--sombra);position:relative}
.rr-f{display:inline-flex;flex-direction:column;align-items:flex-start;gap:0;padding:5px 30px 5px 11px;border:1px solid var(--linha-forte);border-radius:10px;background:#fff;font:500 13px Inter;color:var(--tinta);position:relative;cursor:pointer;min-height:44px;text-align:left}
.rr-f small{font-size:12px;color:var(--tinta-3);font-weight:500}.rr-f span{font-weight:600;white-space:nowrap}
.rr-f svg{position:absolute;right:9px;top:16px}.rr-f.on{border-color:var(--vinho);background:var(--lilas-50)}
.rr-f.dis{opacity:.6;cursor:not-allowed}
.rr-pop{position:absolute;top:calc(100% + 6px);left:10px;z-index:30;background:#fff;border:1px solid var(--linha-forte);border-radius:12px;box-shadow:0 12px 30px rgba(36,8,44,.18);padding:10px;width:min(360px,calc(100vw - 40px));max-height:420px;overflow:auto}
.rr-pop[hidden]{display:none}
.rr-op{display:flex;gap:10px;align-items:flex-start;padding:7px 6px;border-radius:8px;cursor:pointer;font-size:13px}.rr-op:hover{background:var(--lilas-50)}.rr-op small{color:var(--tinta-3);font-size:12px}
.rr-op .cx{flex:none;margin-top:1px}
.rr-busca{display:flex;gap:8px;align-items:center;border:1px solid var(--linha-forte);border-radius:10px;padding:6px 10px;margin-bottom:8px}.rr-busca input{border:0;outline:0;font:14px Inter;flex:1;min-width:0;background:transparent}
.rr-lst{max-height:250px;overflow:auto;border-top:1px solid var(--linha);border-bottom:1px solid var(--linha);margin:6px 0}
.rr-pa{display:flex;gap:8px;justify-content:flex-end;padding-top:8px}
.rr-ativos{margin-top:6px;min-height:0}.rr-ativos:empty{display:none}
.rr-legst{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center;margin:-4px 0 14px;font-size:13px;color:var(--tinta-2)}
.rr-kpis{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px;margin-bottom:16px}
.rr-k{padding:16px;position:relative}.rr-k div.v{font-size:24px}.rr-k .d{font-size:12px}
.rr-kst{margin-top:8px}.kpi .rr-st{font:600 12px Inter;letter-spacing:0;margin:0}.rr-sp{position:absolute;right:12px;top:46px}
.rr-st{font-size:12px;padding:2px 8px}
.rr-g{display:grid;gap:16px;margin-bottom:16px;align-items:start}
.rr-g2{grid-template-columns:minmax(0,1.45fr) minmax(0,1fr)}.rr-g2e{grid-template-columns:repeat(2,minmax(0,1fr))}.rr-g3{grid-template-columns:repeat(3,minmax(0,1fr))}.rr-g4{grid-template-columns:repeat(4,minmax(0,1fr))}
.rr-g.est{align-items:stretch}
.rr-fonte{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:6px;align-items:start;margin-top:14px;padding-top:10px;border-top:1px dashed var(--linha);font-size:12px;color:var(--tinta-3)}
.rr-fonte .rr-stw{display:flex;gap:4px;flex-wrap:wrap;justify-content:flex-end}.rr-fonte svg{margin-top:2px}
.rr-hb{display:flex;flex-direction:column;gap:9px}
.rr-hr{display:grid;grid-template-columns:minmax(120px,38%) minmax(0,1fr) 64px;gap:6px 10px;align-items:center}
.rr-hr .rr-hx{grid-column:2 / 4;font-size:12px;color:var(--tinta-3);margin-top:-4px}
.rr-hl{font-size:13px;color:var(--tinta-2);font-weight:500}.rr-ht{height:12px;border-radius:6px;background:var(--lilas-100);overflow:hidden}.rr-ht i{display:block;height:100%;border-radius:6px}
.rr-hv{text-align:right;font-variant-numeric:tabular-nums}
.rr-fu{display:flex;flex-direction:column;gap:10px}
.rr-fr{display:grid;grid-template-columns:118px minmax(0,1fr) auto;gap:4px 10px;align-items:center}
.rr-fl{font-weight:500;color:var(--tinta-2);font-size:13px}.rr-ft{height:24px;border-radius:8px;background:var(--lilas-100);overflow:hidden}.rr-ft i{display:block;height:100%;background:linear-gradient(90deg,#4c1455,#b0197e);border-radius:8px}
.rr-fr b{text-align:right;min-width:50px;font-variant-numeric:tabular-nums}.rr-fc{grid-column:2 / 4}
.rr-dk{display:block}.rr-mb{display:none}
.rr-leg{margin:-4px 0 8px}
.rr-sec{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:12px}
.rr-sec a{display:flex;flex-direction:column;gap:4px;border:1px solid var(--linha);border-radius:12px;padding:12px;background:var(--lilas-50)}
.rr-sec a:hover{border-color:var(--lilas-300)}.rr-sec b{font:600 14px Poppins}.rr-sec .n{font:600 20px Poppins;color:var(--roxo-700)}
.rr-q{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:8px}
.rr-q>div{border-radius:10px;padding:10px;background:var(--lilas-50);border:1px solid var(--linha)}.rr-q b{display:block;font:600 18px Poppins}
.rr-heat{display:grid;grid-template-columns:56px repeat(7,minmax(0,1fr));gap:3px;font-size:12px}
.rr-heat span{display:grid;place-items:center;min-height:34px;border-radius:6px;font-variant-numeric:tabular-nums}
.rr-heat .h{color:var(--tinta-3);font-weight:600;min-height:24px}
.rr-bul{display:flex;flex-direction:column;gap:16px}
.rr-bu{display:grid;grid-template-columns:150px minmax(0,1fr) 110px;gap:4px 12px;align-items:center}
.rr-bt{position:relative;height:22px;background:var(--lilas-100);border-radius:6px}
.rr-bt i{position:absolute;left:0;top:5px;bottom:5px;border-radius:4px;background:var(--grad)}
.rr-bt em{position:absolute;top:0;bottom:0;border-radius:6px;background:repeating-linear-gradient(45deg,#e6d3ec 0 6px,#f3eaf6 6px 12px)}
.rr-bt u{position:absolute;top:-4px;bottom:-4px;width:3px;background:#1d1424;border-radius:2px}
.rr-bu .meta{grid-column:2 / 4}
.rr-tab td.num b{font-weight:600}
table.t.rr-tab th[data-sort]{cursor:pointer}
.rr-tools{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin-bottom:10px}
.rr-tools .rr-busca{margin:0;min-width:240px;flex:1;max-width:360px}
.rr-bench{font-size:13px}.rr-bench li{margin:6px 0 6px 18px}
.rr-alv{display:flex;flex-direction:column}
.rr-tr td,.rr-tr th{padding-left:10px;padding-right:10px}
.rr-mini{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px}
.rr-mini>div{background:var(--lilas-50);border:1px solid var(--linha);border-radius:10px;padding:10px}.rr-mini b{display:block;font:600 18px Poppins}
@media (max-width:1100px){
 .rr-kpis{grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
 .rr-g2,.rr-g2e{grid-template-columns:minmax(0,1fr)}.rr-g3,.rr-g4{grid-template-columns:repeat(2,minmax(0,1fr))}
 .rr-sec{grid-template-columns:repeat(3,minmax(0,1fr))}
}
@media (max-width:700px){
 .rr-dk{display:none}.rr-mb{display:block}
 .rr-g3,.rr-g4,.rr-mini{grid-template-columns:minmax(0,1fr)}
 .rr-kpis{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.rr-k{padding:12px}.rr-k div.v{font-size:20px}.rr-sp{display:none}
 .rr-sec{grid-template-columns:repeat(2,minmax(0,1fr))}
 .rr-demo{display:inline-flex;gap:4px;align-items:center}.rr-acoes{flex-wrap:wrap}.rr-legd{margin-left:0}.rr-legp{left:0;right:auto}.rr-rtx{flex-basis:100%;order:3}
 .rr-man h2{font-size:17px}
 table.t.rr-tr,body.p-desk table.t.rr-tr{min-width:0!important;display:block;table-layout:auto!important}
 table.rr-tr thead{display:none}table.rr-tr tbody,table.rr-tr tfoot{display:block}
 table.rr-tr tr{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:8px 14px;padding:12px 2px;border-bottom:1px solid var(--linha)}
 table.rr-tr td{display:block;padding:0!important;border:0!important;white-space:normal!important;text-align:left!important;overflow-wrap:normal;word-break:normal;hyphens:none;min-width:0;height:auto!important}
 table.rr-tr td.rr-c1,table.rr-tr td[colspan]{grid-column:1 / -1}
 table.rr-tr td[data-l]:not(.rr-c1)::before{content:attr(data-l);display:block;font-size:12px;color:var(--tinta-3);font-weight:500;margin-bottom:1px}
 table.rr-tr td.rr-pos{grid-column:1 / -1;font-size:12px;color:var(--tinta-3)}
 .rr-scroll{max-height:none;border:0}
 .rr-f{flex:1 1 calc(50% - 8px)}.rr-f span{white-space:normal}
 .rr-hr{grid-template-columns:minmax(0,1fr) 56px}.rr-hl{grid-column:1 / 3}.rr-ht{grid-column:1}.rr-hr .rr-hx{grid-column:1 / 3}
 .rr-fr{grid-template-columns:minmax(0,1fr) auto}.rr-fl{grid-column:1 / 3}.rr-fc{grid-column:1 / 3}
 .rr-bu{grid-template-columns:minmax(0,1fr) auto}.rr-bu>.rr-bt{grid-column:1 / 3;grid-row:2}.rr-bu .meta{grid-column:1 / 3}
 .rr-q{grid-template-columns:repeat(2,minmax(0,1fr))}
 .rr-heat{grid-template-columns:44px repeat(7,minmax(0,1fr));gap:2px}.rr-heat span{min-height:30px;font-size:12px}
 .rr-fonte{grid-template-columns:auto minmax(0,1fr)}.rr-fonte .rr-stw{grid-column:1 / 3;justify-content:flex-start}
 .rr-tools .rr-busca{min-width:0;max-width:none}
}
@media print{.side,.top,.rr-fbar,.rr-tabs,.pbar,.demo-rod,.cab .dir{display:none!important}.app{display:block!important}.card{break-inside:avoid;box-shadow:none}}
'''
CSS+='''
.rr-fit,body.p-desk table.t.rr-fit{min-width:0}
.rr-ok[hidden],[data-ag-conf][hidden]{display:none!important}
@media(max-width:640px){.rr-tools .rr-busca{flex:1 1 100%;max-width:none}}
.rr-ucab{display:flex;gap:10px 14px;align-items:center;flex-wrap:wrap;margin-bottom:16px;padding:14px 16px;position:relative}
.rr-troca{flex-basis:100%;border-top:1px solid var(--linha);padding-top:10px}.rr-troca .rr-lst{max-height:280px}.rr-troca a.rr-op{color:inherit}
.rr-cols{display:grid;grid-template-columns:repeat(6,minmax(0,1fr));gap:10px;align-items:end;height:170px;padding-top:8px}
.rr-cols>div{display:flex;flex-direction:column;align-items:center;gap:4px;justify-content:flex-end;height:100%}
.rr-cols span{width:70%;max-width:44px;border-radius:6px 6px 2px 2px;background:#b0197e;display:block}.rr-cols span.on{background:#4c1455}
.rr-exq{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:10px}.rr-exq a.chip{text-decoration:none;color:inherit}
.rr-cols b{font-size:13px}.rr-cols small{font-size:12px;color:var(--tinta-3)}
'''
JS=r'''<script>(function(){
var Q=new URLSearchParams(location.search);
var CH={'p-per':'per','p-cmp':'cmp','p-marca':'marca','p-reg':'reg','p-uf':'uf','p-cid':'cid','p-un':'un','p-fon':'fon','p-cam':'cam','p-pro':'pro'};
var FIXOS=['unidade','papel'];
var bar=document.querySelector('.rr-fbar');
function msg(h){var a=document.querySelector('.rr-ativos');if(a)a.innerHTML=h;}
function qs(){var t=Q.toString();return t?'?'+t:'';}
function filtroQ(){var o=new URLSearchParams();Object.keys(CH).forEach(function(k){var v=Q.get(CH[k]);if(v)o.set(CH[k],v);});return o;}
function propaga(){var f=filtroQ();document.querySelectorAll('a[href]').forEach(function(a){if(a.closest('.side'))return;var h0=a.dataset.h0||a.getAttribute('href');if(!/^(13|89|9\d)-[a-z-]+\.html/.test(h0))return;a.dataset.h0=h0;
  var p=h0.split('?'),u=new URLSearchParams(p[1]||'');f.forEach(function(v,k){if(!u.has(k))u.set(k,v);});var t=u.toString();a.setAttribute('href',p[0]+(t?'?'+t:''));});}
function grava(){history.replaceState(null,'',location.pathname+qs());propaga();resumo();document.dispatchEvent(new CustomEvent('rr-filtro',{detail:filtroQ()}));}
function rotulo(pid,v){var p=document.getElementById(pid);if(!p)return v;var o=p.querySelector('.rr-op[data-v="'+v+'"]');return o?o.querySelector('span:last-child').firstChild.textContent.trim():v;}
function resumo(){if(!bar)return;var at=[];Object.keys(CH).forEach(function(pid){var v=Q.get(CH[pid]);var b=bar.querySelector('[data-pop="'+pid+'"]');if(!b)return;var sp=b.querySelector('span');if(!sp.dataset.d0)sp.dataset.d0=sp.textContent;
  if(v){var vs=v.split(',');var tx=pid==='p-un'?(vs.length==1?rotulo(pid,vs[0]):vs.length+' unidades'):rotulo(pid,v);sp.textContent=tx;b.classList.add('on');at.push(b.querySelector('small').textContent+': '+tx);}else{sp.textContent=sp.dataset.d0;b.classList.remove('on');}
  var p=document.getElementById(pid);if(p){var vs2=(v||'').split(',');p.querySelectorAll('.rr-op').forEach(function(o,k){var on=v?vs2.indexOf(o.dataset.v)>=0:(pid!=='p-un'&&k===0);o.querySelector('.cx').classList.toggle('on',on);});}});
 bar.querySelector('.rr-ftog .pill').textContent=at.length?at.length+(at.length==1?' ativo':' ativos'):'rede inteira';
 var r=bar.querySelector('[data-res]');if(r){var per=Q.get('per')?rotulo('p-per',Q.get('per')):r.dataset.per0||(r.dataset.per0=r.textContent.split(' · ')[0]);var un=Q.get('un'),uf=Q.get('uf'),rg=Q.get('reg');
  var esc=un?(un.split(',').length==1?rotulo('p-un',un):un.split(',').length+' unidades'):(uf?'Estado '+uf:(rg?rg:'130 unidades'));var cmp=Q.get('cmp')==='sem'?'sem comparação':(Q.get('cmp')==='ano-ant'?'comparado com o ano anterior':'comparado com o período anterior');r.textContent=per+' · '+cmp+' · Gio · '+esc;}
 var reage=!!document.querySelector('meta[name=rr-reage]');
 msg(at.length?'<b>Filtro ativo:</b> '+at.join(' · ')+' <button type="button" class="btn s ghost" data-limpa2>Limpar</button><span class="meta" style="flex-basis:100%">'+(reage?'Esta página já mostra só o recorte. ':'No protótipo, os números desta página seguem os da rede inteira; ')+'O endereço da página guarda o recorte e as abas o levam junto.</span>':'');
 var l2=document.querySelector('[data-limpa2]');if(l2)l2.addEventListener('click',limpa);}
function limpa(){Object.keys(CH).forEach(function(k){Q.delete(CH[k]);});grava();}
if(bar){
 bar.querySelector('.rr-ftog').addEventListener('click',function(){bar.classList.toggle('aberto');this.setAttribute('aria-expanded',bar.classList.contains('aberto'));});
 bar.querySelectorAll('.rr-f[data-pop]').forEach(function(b){b.addEventListener('click',function(e){e.stopPropagation();var p=document.getElementById(b.dataset.pop);var ab=!p.hidden;
   bar.querySelectorAll('.rr-pop').forEach(function(x){x.hidden=true});if(!ab){p.hidden=false;var r=b.getBoundingClientRect(),q=bar.querySelector('.rr-filtros').getBoundingClientRect();p.style.left=Math.max(0,Math.min(r.left-q.left,q.width-p.offsetWidth))+'px';p.style.top=(r.bottom-q.top+6)+'px';var s=p.querySelector('input');if(s)s.focus();}});});
 bar.querySelectorAll('.rr-pop').forEach(function(p){p.addEventListener('click',function(e){e.stopPropagation();});
  var multi=p.id==='p-un';
  function conta(){if(multi){var n=p.querySelectorAll('.cx.on').length;p.querySelector('[data-cont]').textContent=n+(n==1?' selecionada':' selecionadas');}}
  p.querySelectorAll('.rr-op').forEach(function(o){o.addEventListener('click',function(e){e.preventDefault();var c=o.querySelector('.cx');
    if(!multi){p.querySelectorAll('.cx').forEach(function(x){x.classList.remove('on')});c.classList.add('on');}else{c.classList.toggle('on');}conta();});});
  var s=p.querySelector('input');if(s)s.addEventListener('input',function(){var t=s.value.toLowerCase();p.querySelectorAll('.rr-op').forEach(function(o){o.style.display=o.dataset.txt.indexOf(t)>=0?'':'none';});});
  var td=p.querySelector('[data-todas]');if(td)td.addEventListener('click',function(e){e.preventDefault();p.querySelectorAll('.rr-op').forEach(function(o){if(o.style.display!=='none')o.querySelector('.cx').classList.add('on')});conta();});
  var z=p.querySelector('[data-zera]');if(z)z.addEventListener('click',function(){p.querySelectorAll('.cx').forEach(function(x){x.classList.remove('on')});conta();});
  p.querySelector('[data-apl]').addEventListener('click',function(){var vs=[].map.call(p.querySelectorAll('.cx.on'),function(c){return c.parentNode.dataset.v}).filter(Boolean);
    if(vs.length)Q.set(CH[p.id],vs.join(','));else Q.delete(CH[p.id]);p.hidden=true;grava();});});
 document.addEventListener('click',function(){bar.querySelectorAll('.rr-pop').forEach(function(x){x.hidden=true});});
 bar.querySelector('[data-limpa]').addEventListener('click',limpa);
 bar.querySelector('[data-salva]').addEventListener('click',function(){var n=window.prompt('Nome da visão','Minha visão');if(n)msg('<b>Visão "'+n.replace(/</g,'')+'" salva</b> (simulado no protótipo). Ela aparece em Exportar e agendar, no campo Filtros.');});
}
resumo();propaga();
function csv(t,nome){var l=[].map.call(t.querySelectorAll('tr'),function(r){if(r.style.display==='none'||r.dataset.csv==='0')return null;return [].map.call(r.children,function(c){return '"'+(c.dataset.v||c.innerText).replace(/\s+/g,' ').trim().replace(/"/g,'""')+'"'}).join(';')}).filter(Boolean);
 var b=new Blob(['\ufeff'+l.join('\n')],{type:'text/csv;charset=utf-8'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download=nome+'.csv';document.body.appendChild(a);a.click();a.remove();}
document.querySelectorAll('[data-csv]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();var t=document.getElementById(b.dataset.csv);if(t)csv(t,b.dataset.nome||'relatorio-gio');});});
document.querySelectorAll('[data-pdf]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();window.print();});});
/* tabelas: rótulos para os cartões do celular */
function rrTopo(){var b=document.querySelector('.pbar');document.documentElement.style.setProperty('--rr-top',(b&&getComputedStyle(b).position!=='static'?b.offsetHeight:0)+'px');}rrTopo();window.addEventListener('resize',rrTopo);
window.rrRotula=function(root){(root||document).querySelectorAll('table.rr-tr').forEach(function(t){var hs=[].map.call(t.querySelectorAll('thead th'),function(h){return h.textContent.trim()});
 [].forEach.call(t.querySelectorAll('tbody tr,tfoot tr'),function(r){var c1=false;[].forEach.call(r.children,function(td,k){if(td.colSpan>1)return;if(hs[k])td.setAttribute('data-l',hs[k]);
  if(!c1&&!td.classList.contains('num')){td.classList.add('rr-c1');c1=true;}if(hs[k]==='#')td.classList.add('rr-pos');});});});};
rrRotula();
/* paginação */
function pagina(t){if(!t||!t.dataset.pagina)return;var tam=window.innerWidth<700?10:parseInt(t.dataset.pagina,10);var rs=[].filter.call(t.tBodies[0].rows,function(r){return r.style.display!=='none'});var np=Math.max(1,Math.ceil(rs.length/tam));
 var pg=Math.min(parseInt(t.dataset.pg||'1',10),np);t.dataset.pg=pg;[].forEach.call(t.tBodies[0].rows,function(r){r.classList.add('rr-off')});rs.slice((pg-1)*tam,pg*tam).forEach(function(r){r.classList.remove('rr-off')});
 var c=document.querySelector('[data-pgr="'+t.id+'"]');if(!c)return;var h='<button type="button" class="btn s" data-p="'+(pg-1)+'"'+(pg<=1?' disabled':'')+'>Anterior</button>';
 for(var k=1;k<=np;k++)h+='<button type="button" class="btn s'+(k===pg?' on':'')+'" data-p="'+k+'" aria-label="Página '+k+'"'+(k===pg?' aria-current="page"':'')+'>'+k+'</button>';
 h+='<button type="button" class="btn s" data-p="'+(pg+1)+'"'+(pg>=np?' disabled':'')+'>Próxima</button><span class="meta">'+(rs.length?((pg-1)*tam+1)+' a '+Math.min(pg*tam,rs.length)+' de '+rs.length:'0 de 0')+'</span>';c.innerHTML=h;
 c.querySelectorAll('button[data-p]').forEach(function(b){b.addEventListener('click',function(){t.dataset.pg=b.dataset.p;pagina(t);var w=t.closest('.rr-scroll');if(w)w.scrollTop=0;t.closest('.card').scrollIntoView({block:'start'});});});}
document.querySelectorAll('table[data-ordena]').forEach(function(t){t.querySelectorAll('th[data-sort]').forEach(function(th,k){th.addEventListener('click',function(){var idx=[].indexOf.call(th.parentNode.children,th);var tb=t.tBodies[0];var rs=[].slice.call(tb.rows);var asc=th.dataset.asc!=='1';th.dataset.asc=asc?'1':'0';
 rs.sort(function(a,b){var x=a.children[idx].dataset.v,y=b.children[idx].dataset.v;var nx=parseFloat(x),ny=parseFloat(y);var r=(isNaN(nx)||isNaN(ny))?String(x).localeCompare(String(y)):nx-ny;return asc?r:-r;});rs.forEach(function(r){tb.appendChild(r)});t.dataset.pg='1';pagina(t);});});});
var fb=document.querySelector('[data-filtra]');
if(fb){var tb=document.getElementById(fb.dataset.filtra);var inp=fb.querySelector('input');var est={q:'',reg:'',quart:'',uf:'',un:''};
 function ap(){var n=0;var uns=est.un?est.un.split(','):[];[].forEach.call(tb.tBodies[0].rows,function(r){var ok=(!est.q||r.dataset.txt.indexOf(est.q)>=0)&&(!est.reg||r.dataset.reg===est.reg)&&(!est.quart||r.dataset.q===est.quart)&&(!est.uf||r.dataset.uf===est.uf)&&(!uns.length||uns.indexOf(r.dataset.slug)>=0);r.style.display=ok?'':'none';if(ok)n++;});
  var c=document.querySelector('[data-nlin]');if(c)c.textContent=n+' de '+tb.tBodies[0].rows.length+' unidades';var v=document.querySelector('[data-vazio]');if(v)v.hidden=n>0;tb.dataset.pg='1';pagina(tb);}
 function deQ(f){est.reg=f.get('reg')||'';est.uf=f.get('uf')||'';est.un=f.get('un')||'';fb.querySelectorAll('[data-reg]').forEach(function(x){x.classList.toggle('on',x.dataset.reg===est.reg)});ap();}
 inp.addEventListener('input',function(){est.q=inp.value.toLowerCase();ap();});
 fb.querySelectorAll('[data-reg]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();if(b.dataset.reg)Q.set('reg',b.dataset.reg);else Q.delete('reg');grava();});});
 fb.querySelectorAll('[data-quart]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();var ja=b.classList.contains('on');fb.querySelectorAll('[data-quart]').forEach(function(x){x.classList.remove('on')});if(!ja){b.classList.add('on');est.quart=b.dataset.quart;}else est.quart='';ap();});});
 document.querySelectorAll('[data-limpa-tab]').forEach(function(b){b.addEventListener('click',function(){inp.value='';est.q='';est.quart='';fb.querySelectorAll('[data-quart]').forEach(function(x){x.classList.remove('on')});limpa();});});
 document.addEventListener('rr-filtro',function(e){deQ(e.detail);});deQ(filtroQ());}
else document.querySelectorAll('table[data-pagina]').forEach(pagina);
document.querySelectorAll('[data-mapa]').forEach(function(sw){sw.querySelectorAll('span').forEach(function(s){s.addEventListener('click',function(){sw.querySelectorAll('span').forEach(function(x){x.classList.remove('on')});s.classList.add('on');document.querySelectorAll('[data-m]').forEach(function(m){m.hidden=m.dataset.m!==s.dataset.v;});});});});
/* mapa clicável: abre Unidades e regiões já filtrada pelo estado */
document.querySelectorAll('[data-mapa-link] path[id^="BR-"]').forEach(function(p){var uf=p.id.slice(3);p.setAttribute('tabindex','0');p.setAttribute('role','link');p.style.cursor='pointer';
 function vai(){if(document.querySelector('[data-filtra]')){Q.set('uf',uf);Q.delete('reg');grava();var t=document.getElementById('tab-principal');if(t)t.closest('.card').scrollIntoView({block:'start'});}else{var f=filtroQ();f.set('uf',uf);location.href='96-admin-relatorios-unidades.html?'+f.toString();}}
 p.addEventListener('click',vai);p.addEventListener('keydown',function(e){if(e.key==='Enter'||e.key===' '){e.preventDefault();vai();}});});
document.querySelectorAll('[data-tog]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();var on=!b.classList.contains('on');b.classList.toggle('on',on);b.setAttribute('aria-checked',on?'true':'false');var l=b.parentNode.querySelector('[data-togl]');if(l)l.textContent=on?'Ligada':'Desligada';var a=document.querySelector('.rr-ok');if(a){a.hidden=false;a.querySelector('[data-txt]').textContent=(on?'Regra ligada: ':'Regra desligada: ')+b.dataset.tog+'. A mudança fica registrada na auditoria (simulado no protótipo).';}});});
document.querySelectorAll('[data-toast]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();var a=document.querySelector(b.dataset.alvo||'.rr-ok');if(a){a.hidden=false;a.querySelector('[data-txt]').textContent=b.dataset.toast;a.scrollIntoView({block:'nearest'});}});});
})();</script>'''
def cab_rel(tit,sub,on,agendar=True,csv_nome=None):
    ag=f'<a class="btn" href="{LK("rel-export")}">{i("mail",14)} Agendar envio</a>' if agendar else ''
    dir=f'''<span class="pill a rr-demo">{i("eye",12)} Demonstração</span><span data-acao-propria class="rr-acoes">{ag}<button type="button" class="btn" data-pdf>{i("file",14)} PDF</button><button type="button" class="btn p" data-csv="tab-principal" data-nome="{csv_nome or "gio-"+K[on]}">{i("down",14)} CSV</button></span>'''
    return cabec(tit,sub,dir)+nav(on)+filtros()
def pg(chave,titulo,corpo,modo='admin',ativo='rel',reage=False):
    nome=K[chave]
    h=pagina(titulo,app(modo,ativo,corpo),extra_css=CSS).replace('</body>',JS+'</body>')
    if reage: h=h.replace('</head>','<meta name="rr-reage" content="1"></head>',1)
    salvar(nome,h)

# ================= 13 VISÃO EXECUTIVA (hub) =================
CPL=INV/L_PAGO; CPA=INV/sum(AGF[k] for k in CTR); ROAS=REC_PAGO/INV
COMP_DEF='compareceram ÷ agendamentos já realizados (compareceram + faltas + cancelamentos); os futuros ficam fora'
def kpis_exec():
    return '<div class="rr-kpis">'+''.join([
     kv('inbox','Leads',fmt(L),var(L,ANT['L']),'vs. 01 a 21 out','s',sp=LD,href=LK('rel-funil')),
     kv('cal','Agendados',fmt(AG),var(AG,ANT['AG']),f'{pct(AG,L,0)} dos leads','s',sp=AGD,href=LK('rel-funil')),
     kv('check','Comparecimento',pct(CP,CP+REALIZ_FALTA,0),('+1,4 p.p.',1),f'{fmt(CP)} de {fmt(CP+REALIZ_FALTA)} agendamentos já realizados','si',href=LK('rel-atend')),
     kv('tag','Vendas de pacote',fmt(VD),var(VD,ANT['VD']),f'receita de pacotes {brl(REC/1000,0)} mil (todas as fontes)','ic',href=LK('rel-funil')),
     kv('zap','Investimento em mídia',brl(INV),var(INV,ANT['INV']),f'{pct(round(INV/21*30),95000,0)} do orçamento no ritmo atual','i',bom=None,href=LK('rel-camp')),
     kv('target','Custo por lead (mídia)',brl(CPL),var(CPL,ANT['INV']/1532),f'{fmt(L_PAGO)} leads de anúncio','i',bom=False,href=LK('rel-camp')),
     kv('cal','Custo por agendamento',brl(CPA),var(CPA,ANT['INV']/824),'só agendamentos de mídia paga','i',bom=False,href=LK('rel-camp')),
     kv('chart','ROAS da mídia',br(ROAS)+'x',var(ROAS,5.4),f'{brl(REC_PAGO/1000,0)} mil atribuídos à mídia ÷ {brl(INV)}','ic',href=LK('rel-camp')),
     kv('clock','1º contato (mediana)','11 min',(f'−2 min',1),f'meta 15 min · {pct(1094,L,0)} em até 5 min','s',href=LK('rel-atend')),
     kv('star','Nota no Google',br(AV['media'])+' ★',('+0,1',1),f'meta 4,5 · {AV["tx"]}% respondidas · {fmt(AV["tot"])} no período','i',href=LK('rel-google'))])+'</div>'+\
     f'<p class="rr-explica"><b>Por que há duas receitas:</b> a receita de pacotes ({brl(REC/1000,0)} mil) soma as {VD} vendas de todas as fontes. A receita atribuída à mídia ({brl(REC_PAGO/1000,0)} mil) é só a parte cujo lead veio de anúncio (último clique em 30 dias); o ROAS da mídia divide essa parte pelo investimento. <b>Comparecimento</b> em todo o hub = {COMP_DEF}.</p>'
serie=dupla(linha([(LD,'#4c1455',False,''),(LD_ANT,'#4c1455',True,''),(AGD,'#b0197e',False,''),(CPD,'#e5559f',False,'')],DIAS,w=760,h=250),
            linha([(LD,'#4c1455',False,''),(LD_ANT,'#4c1455',True,''),(AGD,'#b0197e',False,'')],DIAS,w=360,h=230,passo=5))
c_serie=card(f'{i("trend",16)} Leads, agendados e comparecimentos por dia',leg([('Leads',"#4c1455",0),('Leads no período anterior',"#4c1455",1),('Agendados',"#b0197e",0),('Compareceram',"#e5559f",0)])+serie
  +f'<p class="meta">Pico em 19/11 (188 leads, dia seguinte ao início do Verão sem pelos no Meta). Quedas de fim de semana: sábados e domingos têm 34% menos leads que a média dos dias úteis.</p>',
  fonte('leads e agendamentos da plataforma; comparecimento da DocBiz','hoje, 16:40','s','i'))
c_funil=card(f'{i("filter",16)} Funil completo da rede',funil2([('Leads',L,'100%'),('Em contato',CT,f'{pct(CT,L,0)} dos leads · {fmt(445)} agendaram sozinhos'),('Agendados',AG,f'{pct(AG,L,0)} dos leads'),('Compareceram',CP,f'{pct(CP,CP+REALIZ_FALTA,0)} dos agendamentos já realizados · {FUTUROS} ainda por vir'),('Compraram pacote',VD,f'{pct(VD,CP,0)} de quem compareceu')])
  +f'<div class="aviso l" style="margin-top:12px"><div>{i("book",15)}</div><div style="font-size:13px"><b>Referência de mercado</b><div class="meta">Clínicas de estética nos EUA: lead para consulta 25 a 40%, comparecimento 70 a 80%, consulta para tratamento 50 a 65% (Pronk, 2026). A rede está acima no agendamento e dentro da faixa no comparecimento.</div></div></div>',
  fonte('plataforma (leads e agenda) e DocBiz (comparecimento e venda)','hoje, 16:40','s','i','c'))
grp=[(g,sum(f[3] for f in FONTES if f[2]==g),sum(AGF[f[0]] for f in FONTES if f[2]==g)) for g in GRUPOS]
corg={'Mídia paga':'#6f0052','Orgânico':'#2C5BC4','Relacionamento':'#0B7A54','Outros':'#9a8fa1'}
c_fontes=card(f'{i("chart",16)} De onde vêm os leads',hbar([(g,v,corg[g],f'{pct(v,L,0)} dos leads · {pct(a,v,0)} agendam') for g,v,a in grp])
  +'<div class="sep"></div>'+hbar([(f[1],f[3],f[4]) for f in sorted(FONTES,key=lambda f:-f[3])[:6]])+f'<p class="meta" style="margin-top:8px">Barras em vez de pizza: comprimento é lido com mais precisão (NN/g). <a class="lk" href="{LK("rel-funil")}">Ver as 10 fontes e o funil de cada uma</a></p>',
  fonte('UTM e click IDs do coletor próprio (spec 003)','hoje, 16:40','s'))
uf_lpu={uf:round(sum(x['l'] for x in us)/len(us),1) for uf,us in UF_AG.items()}
esc_l=lambda v:'#ead9f0' if v<15 else ('#d8bde3' if v<20 else ('#c39ad3' if v<25 else '#a877bd'))
mp=mapa_val(360,330,uf_lpu,esc_l,lambda v:br(v)+' leads por unidade')
c_mapa=card(f'{i("map",16)} Leads por unidade, por estado','<div data-mapa-link>'+dupla(mp,mapa_val(300,280,uf_lpu,esc_l,lambda v:br(v)+' leads por unidade'))+'</div>'
  +leg([('menos de 15','#ead9f0',0),('15 a 20','#d8bde3',0),('20 a 25','#c39ad3',0),('25 ou mais','#a877bd',0)])+f'<p class="meta">Média por unidade evita que SP (86 unidades) domine o mapa. Clique num estado para abrir as unidades dele. <a class="lk" href="{LK("rel-unidades")}">Trocar a métrica no mapa completo</a></p>',
  fonte('plataforma; malha de UFs do IBGE','hoje, 16:40','s'))
top=ORD[:5]; bot=ORD[-5:]
lin=lambda x:f'<tr><td class="num" data-v="{x["pos"]}">{x["pos"]}º</td><td style="white-space:normal"><a class="lk" href="{U97(x)}">{x["nome"]}</a><div class="meta">{x["cid"]}/{x["uf"]} · Q{x["q"]} · 1º contato {x["t1"]} min</div></td><td class="num" data-v="{x["idx"]}"><b>{x["idx"]}</b></td><td class="num" data-v="{x["l"]}">{x["l"]}</td><td class="num" data-v="{x["tx_ag"]:.3f}">{pct(x["ag"],x["l"],0)}</td></tr>'
qs=[[x for x in UN if x['q']==q] for q in (1,2,3,4)]
c_rank=card(f'{i("trend",16)} Ranking e quartis das unidades','<div class="rr-q">'+''.join(f'<div><span class="meta">Quartil {q+1}</span><b>{len(us)} unid.</b><span class="meta">índice {min(x["idx"] for x in us)} a {max(x["idx"] for x in us)} · {pct(soma(us,"ag"),soma(us,"l"),0)} agendam</span></div>' for q,us in enumerate(qs))+'</div>'
  +'<table class="t rr-tr" style="margin-top:12px"><thead><tr><th class="num">#</th><th>Unidade</th><th class="num">Índice</th><th class="num">Leads</th><th class="num">Agendam</th></tr></thead><tbody>'+''.join(lin(x) for x in top)+'<tr><td colspan="5" class="meta" style="white-space:normal;height:32px;text-align:center">mediana da rede: índice '+str(round(mediana([x["idx"] for x in UN])))+f' · 1º contato {round(mediana([x["t1"] for x in UN]))} min</td></tr>'+''.join(lin(x) for x in bot)+'</tbody></table>',
  fonte('índice de conversão (mesmo da tela 04 e do painel do franqueado)','hoje, 16:40','s'),dir=f'<a class="btn s" href="{LK("rel-unidades")}">Todas as 130 {i("chev",12)}</a>')
tc=sorted(CAMPS,key=lambda c:-c['leads'])[:6]
c_camp=card(f'{i("send",16)} Campanhas com mais leads','<table class="t rr-tr" id="tab-principal"><thead><tr><th>Campanha</th><th class="num">Investido</th><th class="num">Leads</th><th class="num">CPL</th><th class="num">Agend.</th><th class="num">ROAS</th></tr></thead><tbody>'
  +''.join(f'<tr><td class="trunc"><b>{c["nome"]}</b><div class="meta">{c["pl"]} · {c["esc"]}</div></td><td class="num">{brl(c["inv"])}</td><td class="num">{c["leads"]}</td><td class="num">{brl(c["inv"]/c["leads"])}</td><td class="num">{c["ag"]}</td><td class="num"><b>{br(c["rec"]/c["inv"])}x</b></td></tr>' for c in tc)+'</tbody></table>',
  fonte('Google Ads API e Meta Marketing API (custo); plataforma (leads); DocBiz (receita)','hoje, 14:00','i','c'),dir=f'<a class="btn s" href="{LK("rel-camp")}">Todas {i("chev",12)}</a>')
AG_PROJ=round(AG/21*30)
MG=max(CAMPS,key=lambda c:c['rec']/c['inv'])
ALERTAS=[('r','trend','Goiás: leads −31% na semana','Desde 17/11, quando a campanha Depilação a laser (GO) foi pausada. 7 unidades afetadas.',LK('rel-unidades')+'?uf=GO'),
 ('r','star',f'{AV["esc_pend"]} avaliações escaladas sem resposta','Nota 1 ou 2 ou menção a saúde. Meta: notas 1 e 2 respondidas em 24 h.',LK('aval-esc')),
 ('a','target',f'Agendamentos projetados em {pct(AG_PROJ,2600,0)} da meta',f'Faltam {fmt(2600-AG_PROJ)} para 2.600 no ritmo atual. Maior lacuna na Regional SP.',LK('rel-metas')),
 ('r','clock','3 unidades com 1º contato acima de 60 min','Montes Claros (74 min), Catalão (66) e Ipiranga (61). Agendam 14 pontos menos que a mediana.',LK('rel-atend')),
 ('a','zap','CPL do Remarketing limpeza de pele +38%','R$ 31 contra R$ 22 nas 4 semanas anteriores. Fadiga de criativo provável.',LK('rel-camp')),
 ('a','alert','UTM inválida em 3,1%, acima do limite de 3%','Distorce fonte e CPL. Dois links de parceiras sem utm_source.',LK('rel-trafego'))]
BEM=[('v','sparkle','Quiz converte mais que o formulário','9,3% dos quizzes concluídos viram lead e 56% desses agendam, contra 52% do formulário.',LK('rel-trafego')),
 ('v','chart',f'Marca Gio rende {br(MG["rec"]/MG["inv"])}x',f'CPL de {brl(MG["inv"]/MG["leads"])} e {pct(MG["ag"],MG["leads"],0)} agendam. Candidata a mais orçamento.',LK('rel-camp')),
 ('v','pin','Regional Sul com 30,1 leads por unidade','Contra 23,0 da rede, com o mesmo investimento por unidade.',LK('rel-unidades')+'?reg=Regional+Sul')]
def lista_al(itens): return '<div class="lista-i">'+''.join(f'<a class="it" href="{h}" style="align-items:flex-start"><div class="ic {c}">{i(ic,15)}</div><div style="flex:1;min-width:0"><b>{t}</b><div class="meta">{d}</div></div>{i("chev",14)}</a>' for c,ic,t,d,h in itens)+'</div>'
c_alert=card(f'{i("alert",16)} Precisa de ação',lista_al(ALERTAS),fonte('regras de alerta e detecção de anomalia (spec 005)','hoje, 16:40','s'),dir=f'<a class="btn s" href="{LK("rel-metas")}">Todos os alertas {i("chev",12)}</a>')
c_bem=card(f'{i("sparkle",16)} O que está indo bem',lista_al(BEM),fonte('relatórios inteligentes (regras da rede)','hoje, 16:40','s'))
def bullet(rot,real,meta,proj,origem,fmtv=fmt):
    mx=max(meta,proj)*1.1; orc='Invest' in rot; cor='' if orc else ('up' if proj>=meta else 'down')
    return f'<div class="rr-bu"><b style="font-size:13px">{rot}</b><span class="rr-bt"><em style="left:{real/mx*100:.1f}%;width:{(proj-real)/mx*100:.1f}%"></em><i style="width:{real/mx*100:.1f}%"></i><u style="left:{meta/mx*100:.1f}%"></u></span><span style="text-align:right;font-size:13px"><b>{fmtv(real)}</b> <span class="meta">de {fmtv(meta)}</span></span><span class="meta">Projeção do mês: <span class="{cor}">{fmtv(proj)} ({pct(proj,meta,0)} {"do orçamento" if orc else "da meta"})</span> · {origem}</span></div>'
c_metas=card(f'{i("target",16)} Metas de novembro','<div class="rr-bul">'+''.join(bullet(r,a,m,p,o,(lambda v:brl(v)) if 'Invest' in r else fmt) for r,a,m,p,o in METAS)+'</div>'+leg([('realizado até 21/11','#86106b',0),('projeção até 30/11','#e6d3ec',0),('meta','#1d1424',0)]),
  fonte('metas cadastradas pela Salus; projeção pelo ritmo diário com peso de dia da semana','hoje, 16:40','c'),dir=f'<a class="btn s" href="{LK("rel-metas")}">Previsão {i("chev",12)}</a>')
c_prev=card(f'{i("cal",16)} Sazonalidade, ano anterior e previsão',leg([('Leads por mês',"#b0197e",0),('Mesmo mês do ano anterior',"#2C5BC4",1),('Novembro projetado',"#e6d3ec",0)])
  +dupla(colunas(MES_L,MESES,linha_aa=MES_AA,proj=PREV,w=620,h=230),colunas(MES_L,[m[:3] for m in MESES],linha_aa=MES_AA,proj=PREV,w=360,h=220))
  +f'<p class="meta">Novembro: {fmt(L)} leads até dia 21, projeção de {fmt(PREV)} (faixa de {fmt(PREV_LO)} a {fmt(PREV_HI)}) contra {fmt(MES_AA[-1])} em nov/25. Pico anual em julho, como na tela 67.</p>',
  fonte('plataforma desde dez/25; antes disso, importação do AGDM (somente leitura)','hoje, 06:00','s'))
HUB=[('rel-camp','send','Aquisição e campanhas',brl(INV),'investidos · ROAS '+br(ROAS)+'x'),('rel-funil','filter','Leads e funil',fmt(L),'leads de 10 fontes'),('rel-atend','clock','Atendimento','11 min','1º contato (mediana)'),
 ('rel-trafego','sparkle','Quiz, landings e tráfego',fmt(QZ['fim']),'quizzes concluídos'),('rel-google','google','SEO local e avaliações',br(AV['media'])+' ★',f'{AV["tx"]}% respondidas'),('rel-cliente','users','Área do cliente',fmt(CLI['base']),'clientes com conta'),
 ('rel-unidades','pin','Unidades e regiões','130','ranking, quartis e mapa'),('rel-unidade','home','Relatório da unidade','130','uma página por unidade'),('rel-metas','target','Metas e alertas',pct(PREV,4000,0),'da meta de leads projetada'),('rel-export','mail','Exportar e agendar','3','envios agendados')]
c_hub=card(f'{i("grid",16)} Todas as seções do hub','<div class="rr-sec">'+''.join(f'<a href="{LK(k)}"><span class="meta">{i(ic,13)} {t}</span><span class="n">{n}</span><span class="meta">{d}</span></a>' for k,ic,t,n,d in HUB)+'</div>'
  +f'<p class="meta" style="margin-top:10px">Telas operacionais ligadas ao hub: <a class="lk" href="{LK("aval-rede")}">Avaliações da rede (84)</a> · <a class="lk" href="{LK("perf")}">Performance de campanhas para clientes (62)</a> · <a class="lk" href="{LK("intel")}">Demanda e quiz (66)</a> · <a class="lk" href="{LK("sazon")}">Sazonalidade (67)</a> · <a class="lk" href="{LK("saude")}">Saúde do tracking (70)</a> · <a class="lk" href="{LK("insights")}">Relatórios inteligentes (14)</a></p>')
MAN=f'''<section class="card rr-man"><span class="meta">Resumo de {PER} · atualizado hoje, 16:40 (horário de Brasília)</span>
<h2>Leads projetados em {pct(PREV,4000,0)} da meta; agendamentos em {pct(AG_PROJ,2600,0)}.</h2>
<p>Goiás caiu 31% na semana depois da pausa da campanha de depilação a laser. {AV["esc_pend"]} avaliações escaladas estão sem resposta e a UTM inválida passou do limite (3,1% contra 3%).</p></section>'''
corpo=cab_rel('Relatórios da rede','Hub que junta todas as fontes: aquisição, leads, atendimento, Google, área do cliente, unidades e metas.','rel')+MAN+f'''
<div class="rr-g rr-g2" style="margin-top:16px">{c_alert}{c_metas}</div>
'''+kpis_exec()+f'''
<div class="rr-g rr-g2">{c_serie}{c_funil}</div>
<div class="rr-g rr-g2e">{c_fontes}{c_mapa}</div>
<div class="rr-g rr-g2e">{c_rank}{c_camp}</div>
<div class="rr-g rr-g2e">{c_bem}{c_prev}</div>
{c_hub}'''
pg('rel','Relatórios da rede',corpo)

# ================= 90 AQUISIÇÃO E CAMPANHAS =================
IMP=sum(c['imp'] for c in CAMPS); CLQ=sum(c['cli'] for c in CAMPS); CPT=sum(c['cp'] for c in CAMPS); AGP=sum(c['ag'] for c in CAMPS)
k90='<div class="rr-kpis">'+''.join([kv('zap','Investimento',brl(INV),var(INV,ANT['INV']),'Google Ads e Meta Ads','i',bom=None),kv('eye','Impressões',fmt(IMP),var(IMP,1190000),'13 campanhas ativas ou pausadas','i'),
 kv('cursor','Cliques',fmt(CLQ),var(CLQ,21900),f'CTR {pct(CLQ,IMP,2)}','i'),kv('inbox','Leads de mídia',fmt(L_PAGO),var(L_PAGO,1532),f'{pct(L_PAGO,CLQ,1)} dos cliques','si'),
 kv('target','Custo por lead',brl(CPL),var(CPL,ANT['INV']/1532),'referência Brasil: R$ 18 a R$ 90','i',bom=False),kv('cal','Custo por agendamento',brl(INV/AGP),var(INV/AGP,ANT['INV']/824),f'{fmt(AGP)} agendamentos de mídia','si',bom=False),
 kv('check','Custo por comparecimento',brl(INV/CPT),var(INV/CPT,ANT['INV']/515),f'{fmt(CPT)} comparecimentos','si',bom=False),kv('tag','Vendas atribuídas',fmt(sum(c['vd'] for c in CAMPS)),('+6,8%',6.8),'último clique em 30 dias','ic'),
 kv('trend','Receita atribuída à mídia',brl(REC_PAGO/1000)+' mil',('+12,4%',12.4),'vendas de leads de anúncio (DocBiz)','ic'),kv('chart','ROAS da mídia',br(ROAS)+'x',var(ROAS,5.4),'receita atribuída à mídia ÷ investimento','ic')])+'</div>'+f'<p class="rr-explica">A receita atribuída à mídia ({brl(REC_PAGO/1000,0)} mil) é a parte da receita de pacotes ({brl(REC/1000,0)} mil, todas as fontes, na visão executiva) cujo lead veio de anúncio, por último clique em 30 dias. O ROAS da mídia usa só essa parte.</p>'
def plat(pl):
    cs=[c for c in CAMPS if c['pl']==pl]; inv=soma(cs,'inv'); ld=soma(cs,'leads'); ag=soma(cs,'ag'); cp=soma(cs,'cp'); rec=soma(cs,'rec')
    return f'<div><h4 style="font:600 15px Poppins;margin-bottom:8px">{pl}</h4><div class="rr-mini"><div><span class="meta">Investido</span><b>{brl(inv)}</b></div><div><span class="meta">Leads</span><b>{fmt(ld)}</b></div><div><span class="meta">CPL</span><b>{brl(inv/ld)}</b></div><div><span class="meta">Agendam</span><b>{pct(ag,ld,0)}</b></div><div><span class="meta">Custo/agend.</span><b>{brl(inv/ag)}</b></div><div><span class="meta">ROAS da mídia</span><b>{br(rec/inv)}x</b></div></div></div>'
c_plat=card(f'{i("grid",16)} Google Ads x Meta Ads',f'<div class="rr-atraso">{i("clock",14)}<span><b>Meta Ads com leitura atrasada:</b> a última leitura foi às 14:00 e a das 16:00 falhou (limite de chamadas da API). Os números do Meta podem subir na próxima leitura, às 18:00.</span></div><div class="g">'+plat('Google Ads')+plat('Meta Ads')+'</div><p class="meta" style="margin-top:10px">Meta traz lead mais barato, mas agenda menos: o custo por agendamento fica próximo. Por isso o hub ordena por custo por agendamento e ROAS, não só por CPL.</p>',
  fonte('Google Ads API (GAQL, metrics.cost_micros) e Meta Marketing API (Insights); leads e agenda da plataforma','hoje, 14:00 (custo atualiza a cada 6 h)','i','s'))
c_bench=card(f'{i("book",16)} Referências de mercado','''<ul class="rr-bench">
<li><b>Google Ads, beleza e cuidados pessoais (EUA, 2025):</b> CPL de US$ 60,34, conversão de 7,82% e CPC de US$ 5,70, alta de 60% no ano. <a class="lk" href="https://www.wordstream.com/blog/2025-google-ads-benchmarks" target="_blank" rel="noopener">WordStream/LocaliQ</a></li>
<li><b>Meta Ads, campanhas de lead em beleza (EUA, 2025):</b> CPL de US$ 51,42 e conversão de 5,29%. <a class="lk" href="https://www.wordstream.com/blog/facebook-ads-benchmarks-2025" target="_blank" rel="noopener">WordStream/LocaliQ</a></li>
<li><b>Clínicas de estética no Brasil (2025):</b> CPL de R$ 18 a R$ 45 no Meta e de R$ 40 a R$ 90 no Google. <a class="lk" href="https://apicemarketing.com.br/blog/quanto-custa-lead-meta-ads-2025.html" target="_blank" rel="noopener">Ápice Marketing</a> (referência de agência, usar como ordem de grandeza)</li>
<li><b>Custo por agendamento:</b> costuma ser 2 a 3 vezes o CPL, porque nem todo lead agenda nem comparece. <a class="lk" href="https://pronkmedspamarketing.com/blog/med-spa-digital-marketing-benchmarks/" target="_blank" rel="noopener">Pronk, 2026</a></li></ul>''',fonte('pesquisa de 21/11/2026 (spec 005, pesquisa.md)','21/11, 17:00'))
th='<th>Campanha</th><th class="num" data-sort>Investido</th><th class="num" data-sort>Impressões</th><th class="num" data-sort>Cliques</th><th class="num" data-sort>Leads</th><th class="num" data-sort>CPL</th><th class="num" data-sort>Agend.</th><th class="num" data-sort>Custo/agend.</th><th class="num" data-sort>Compar.</th><th class="num" data-sort>Vendas</th><th class="num" data-sort>Receita atribuída</th><th class="num" data-sort>ROAS</th>'
td=lambda c:f'<tr><td class="trunc" data-v="{c["nome"]}"><b>{c["nome"]}</b><div class="meta">{c["pl"]} · {dict(ga_pesq="Pesquisa",ga_pmax="Performance Max",meta_form="Formulário e landing",meta_wa="Clique para WhatsApp")[c["fo"]]} · {c["esc"]} ({c["un"]} unid.) · CTR {pct(c["cli"],c["imp"],1)}</div><span class="pill {"a" if "paus" in c["st"] else ("r" if "subiu" in c["st"] else "v")}" style="margin-top:4px">{c["st"]}</span></td><td class="num" data-v="{c["inv"]}">{brl(c["inv"])}</td><td class="num" data-v="{c["imp"]}">{fmt(c["imp"])}</td><td class="num" data-v="{c["cli"]}">{fmt(c["cli"])}</td><td class="num" data-v="{c["leads"]}">{c["leads"]}</td><td class="num" data-v="{c["inv"]/c["leads"]:.2f}">{brl(c["inv"]/c["leads"])}</td><td class="num" data-v="{c["ag"]}">{c["ag"]}</td><td class="num" data-v="{c["inv"]/c["ag"]:.2f}">{brl(c["inv"]/c["ag"])}</td><td class="num" data-v="{c["cp"]}">{c["cp"]}</td><td class="num" data-v="{c["vd"]}">{c["vd"]}</td><td class="num" data-v="{c["rec"]}">{brl(c["rec"])}</td><td class="num" data-v="{c["rec"]/c["inv"]:.2f}"><b>{br(c["rec"]/c["inv"])}x</b></td></tr>'
tot=f'<tfoot><tr><td><b>Total da mídia paga</b><div class="meta">CTR {pct(CLQ,IMP,1)}</div></td><td class="num"><b>{brl(INV)}</b></td><td class="num"><b>{fmt(IMP)}</b></td><td class="num"><b>{fmt(CLQ)}</b></td><td class="num"><b>{fmt(L_PAGO)}</b></td><td class="num"><b>{brl(CPL)}</b></td><td class="num"><b>{fmt(AGP)}</b></td><td class="num"><b>{brl(INV/AGP)}</b></td><td class="num"><b>{CPT}</b></td><td class="num"><b>{sum(c["vd"] for c in CAMPS)}</b></td><td class="num"><b>{brl(REC_PAGO)}</b></td><td class="num"><b>{br(ROAS)}x</b></td></tr></tfoot>'
c_tab=card(f'{i("list",16)} Todas as campanhas de mídia paga',f'<table class="t rr-tab rr-tr" id="tab-principal" data-ordena><thead><tr>{th}</tr></thead><tbody>'+''.join(td(c) for c in sorted(CAMPS,key=lambda c:-c['inv']))+f'</tbody>{tot}</table><p class="meta" style="margin-top:8px">Clique no título da coluna para ordenar. Atribuição: último clique em 30 dias, com gclid, fbclid e ctwa_clid guardados no lead pelo coletor (spec 003). Comparecimento e venda voltam da DocBiz e sobem para o Google Ads como conversão offline.</p>',
  fonte('Google Ads API e Meta Marketing API (investimento, impressões, cliques); plataforma (leads, agenda); DocBiz (comparecimento, venda, receita)','hoje, 14:00','i','s','c'),
  dir=f'<span data-acao-propria><button type="button" class="btn s" data-csv="tab-principal" data-nome="gio-campanhas">{i("down",13)} CSV</button></span>')
pts=[(c['inv']/c['leads'],c['ag']/c['leads']*100,6+c['leads']/22,'#6f0052' if c['pl']=='Google Ads' else '#d23c8f',f"{k+1} {c['nome']} ({c['esc']}): CPL {brl(c['inv']/c['leads'])}, {pct(c['ag'],c['leads'],0)} agendam") for k,c in enumerate(CAMPS)]
c_disp=card(f'{i("target",16)} Custo por lead x taxa de agendamento',leg([('Google Ads','#6f0052',0),('Meta Ads','#d23c8f',0),('tamanho = leads','#cfb0da',0)])
  +dupla(dispersao(pts,w=600,h=310,xr=(10,70),yr=(40,70),xl='CPL (R$)',yl='% que agenda',fx=lambda v:f'{v:.0f}',fy=lambda v:f'{v:.0f}%',refx=CPL,refy=AG/L*100),dispersao(pts,w=340,h=280,xr=(10,70),yr=(40,70),xl='CPL',yl='% agenda',fx=lambda v:f'{v:.0f}',fy=lambda v:f'{v:.0f}%',refx=CPL,refy=AG/L*100))
  +'<p class="meta">Canto superior esquerdo: barato e agenda bem (Marca Gio, Peeling no WhatsApp). Canto inferior direito: candidatos a revisão (Criolipólise PMax). Linhas tracejadas: CPL médio e taxa média da rede. Número no círculo = linha da tabela por ordem de cadastro.</p>',
  fonte('cálculo da plataforma sobre os dados da tabela','hoje, 14:00','i','s'))
c_crm=card(f'{i("send",16)} Campanhas para clientes (área do cliente)','<table class="t rr-tr"><thead><tr><th>Campanha</th><th class="num">Enviadas</th><th class="num">Cliques</th><th class="num">Agend.</th><th class="num">Compar.</th></tr></thead><tbody>'
  +''.join(f'<tr><td class="trunc"><b>{c["nome"]}</b><div class="meta">{c["esc"]}</div></td><td class="num">{fmt(c["env"])}</td><td class="num">{fmt(c["cli"])}</td><td class="num">{c["ag"]}</td><td class="num">{c["cp"]}</td></tr>' for c in CRM)+f'</tbody></table><p class="meta" style="margin-top:8px">Mesmos números da tela 62 ({PF[3][1]} agendamentos dentro dos {fmt(AG)} da rede). Custo de envio do WhatsApp entra quando a Salus informar a tarifa contratada. <a class="lk" href="{LK("perf")}">Abrir performance e replicar</a></p>',
  fonte('campanha_envio e atribuicao_conversao (spec 002)','hoje, 16:40','s','c'))
pac=[('Google Ads',sum(c['inv'] for c in CAMPS if c['pl']=='Google Ads'),68000),('Meta Ads',sum(c['inv'] for c in CAMPS if c['pl']=='Meta Ads'),27000)]
c_pace=card(f'{i("clock",16)} Ritmo do orçamento de novembro','<div class="rr-bul">'+''.join(bullet(p,v,o,round(v/21*30),'orçamento da Salus',lambda x:brl(x)) for p,v,o in pac)+'</div>',fonte('investimento das APIs; orçamento informado pela Salus','hoje, 14:00','i','c'))
corpo=cab_rel('Aquisição e campanhas','Investimento, leads, agendamentos, comparecimentos e receita de cada campanha, com o custo em cada etapa.','rel-camp')+k90+f'''
<div class="rr-g rr-g2">{c_plat}{c_bench}</div>{c_tab}
<div class="rr-g rr-g2" style="margin-top:16px">{c_disp}{c_pace}</div>{c_crm}'''
pg('rel-camp','Aquisição e campanhas',corpo)

# ================= 91 LEADS, FONTES E FUNIL =================
JA_CLI=612
k91='<div class="rr-kpis">'+''.join([kv('inbox','Leads',fmt(L),var(L,ANT['L']),'10 fontes, 4 pontos de entrada'),kv('zap','Da mídia paga',pct(L_PAGO,L,0),('+1,2 p.p.',1),f'{fmt(L_PAGO)} leads','si'),
 kv('globe','Orgânicos (busca, Google e Instagram)',pct(1045,L,0),('−0,8 p.p.',-1),'SEO, perfil no Google e Instagram'),kv('phone','Taxa de contato',pct(CT,L,0),('+2,1 p.p.',1),'leads com 1º contato registrado'),
 kv('cal','Agendaram',pct(AG,L,0),('−2,3 p.p.',-1),f'{fmt(AG)} agendamentos'),kv('check','Comparecimento',pct(CP,CP+REALIZ_FALTA,0),('+1,4 p.p.',1),f'{fmt(CP)} de {fmt(CP+REALIZ_FALTA)} agendamentos já realizados','si'),
 kv('tag','Compraram',pct(VD,CP,0),('+0,9 p.p.',1),f'{VD} pacotes','ic'),kv('clock','Até agendar (mediana)','1 dia',('−0,4 dia',1),'46% agendam no mesmo dia'),
 kv('user','Já eram clientes',pct(JA_CLI,L,0),('+3,0 p.p.',1),f'{JA_CLI} leads ligados a uma conta (spec 002)'),kv('x','Perdidos',fmt(498),('−6,1%',1),'com motivo registrado em 71%')])+'</div>'
rows=''.join(f'<tr><td class="trunc" data-v="{f[1]}"><span style="display:inline-block;width:10px;height:10px;border-radius:3px;background:{f[4]};margin-right:6px"></span><b>{f[1]}</b></td><td data-v="{f[2]}">{f[2]}</td><td class="num" data-v="{f[3]}">{fmt(f[3])}</td><td class="num" data-v="{f[3]/L:.4f}">{pct(f[3],L,1)}</td><td class="num" data-v="{AGF[f[0]]}">{AGF[f[0]]}</td><td class="num" data-v="{AGF[f[0]]/f[3]:.3f}"><b>{pct(AGF[f[0]],f[3],0)}</b></td><td class="num" data-v="{CPF[f[0]]}">{CPF[f[0]]}</td><td class="num" data-v="{VDF[f[0]]}">{VDF[f[0]]}</td><td class="num" data-v="{VDF[f[0]]*TICKET}">{brl(VDF[f[0]]*TICKET)}</td><td class="num" data-v="{INVF.get(f[0],0)/f[3]:.2f}">{brl(INVF[f[0]]/f[3]) if f[0] in INVF else "sem mídia"}</td></tr>' for f in FONTES)
c_tf=card(f'{i("list",16)} Funil por fonte',f'<table class="t rr-tab rr-tr" id="tab-principal" data-ordena><thead><tr><th>Fonte</th><th>Grupo</th><th class="num" data-sort>Leads</th><th class="num" data-sort>% dos leads</th><th class="num" data-sort>Agend.</th><th class="num" data-sort>Agendam</th><th class="num" data-sort>Compar.</th><th class="num" data-sort>Vendas</th><th class="num" data-sort>Receita</th><th class="num" data-sort>CPL</th></tr></thead><tbody>{rows}</tbody><tfoot><tr><td><b>Rede</b></td><td></td><td class="num"><b>{fmt(L)}</b></td><td class="num">100%</td><td class="num"><b>{fmt(AG)}</b></td><td class="num"><b>{pct(AG,L,0)}</b></td><td class="num"><b>{fmt(CP)}</b></td><td class="num"><b>{VD}</b></td><td class="num"><b>{brl(REC)}</b></td><td class="num">{brl(CPL)}</td></tr></tfoot></table>'
  +'<p class="meta" style="margin-top:8px">Perfil no Google e indicação agendam mais que qualquer mídia paga. Campanhas para clientes agendam 92% porque o clique já leva à agenda da área do cliente.</p>',
  fonte('UTM e click IDs (coletor, spec 003); agenda; DocBiz','hoje, 16:40','s','i','c'),dir=f'<span data-acao-propria><button type="button" class="btn s" data-csv="tab-principal" data-nome="gio-fontes">{i("down",13)} CSV</button></span>')
def mini_funil(g):
    fs=[f for f in FONTES if f[2]==g]; l=sum(f[3] for f in fs); a=sum(AGF[f[0]] for f in fs); c=sum(CPF[f[0]] for f in fs); v=sum(VDF[f[0]] for f in fs)
    return f'<div style="margin-bottom:14px"><b style="font-size:13px">{g}</b> <span class="meta">· {fmt(l)} leads</span>'+hbar([('Agendaram',a/l*100,corg[g]),('Compareceram',c/l*100,corg[g]),('Compraram',v/l*100,corg[g])],fmtv=lambda x:br(x,0)+'%',mx=100)+'</div>'
c_mf=card(f'{i("filter",16)} Conversão sobre leads, por grupo de fonte',''.join(mini_funil(g) for g in GRUPOS),fonte('plataforma e DocBiz','hoje, 16:40','s','c'))
c_pt=card(f'{i("mouse",16)} Como o lead entrou',hbar([(r,v,'',pct(v,L,0)+' dos leads') for r,v in PONTO])+'<p class="meta" style="margin-top:8px">WhatsApp e telefone só contam como lead quando o clique é identificado pelo coletor (evento whatsapp_clicado com retorno da conversa). Os demais cliques ficam em Quiz, landings e tráfego.</p>',fonte('eventos lead_enviado e quiz_concluido (dicionário v3)','hoje, 16:40','s'))
c_pr=card(f'{i("tag",16)} Procedimentos mais procurados',hbar([(r,v,'',pct(v,L,0)) for r,v in PROC]),fonte('campo tratamento do lead','hoje, 16:40','s'))
c_tempo=card(f'{i("cal",16)} Tempo do lead até o agendamento',hbar([('No mesmo dia',797,''),('No dia seguinte',364,''),('2 a 3 dias',260,''),('4 a 7 dias',156,''),('8 dias ou mais',156,'')]),fonte('lead.criado_em x agendamento.criado_em','hoje, 16:40','s'))
c_perda=card(f'{i("x",16)} Motivos de perda',hbar([('Não respondeu ao contato',134,'#B4234A'),('Achou caro',75,'#B4234A'),('Só pesquisando',60,'#B4234A'),('Horário ou distância',49,'#B4234A'),('Outro',36,'#B4234A'),('Sem motivo registrado',144,'#cfb0da')])+'<p class="meta" style="margin-top:8px">Pede um campo novo e obrigatório ao marcar o lead como perdido (lista fechada). Hoje o AGDM não guarda motivo.</p>',fonte('lead.status perdido + motivo (campo novo proposto)','hoje, 16:40','s'))
corpo=cab_rel('Leads e funil','Cada fonte do lead até a venda, como ele entrou, o que procura, quanto demora para agendar e por que se perde.','rel-funil')+k91+c_tf+f'''
<div class="rr-g rr-g3" style="margin-top:16px">{c_mf}{c_pt}{c_pr}</div><div class="rr-g rr-g2e">{c_tempo}{c_perda}</div>'''
pg('rel-funil','Leads e funil',corpo)

# ================= 92 ATENDIMENTO DO FRANQUEADO =================
k92='<div class="rr-kpis">'+''.join([kv('clock','1º contato (mediana)','11 min',('−2 min',1),'meta da rede: 15 min'),kv('zap','Contato em até 5 min',pct(1094,L,0),('+4,8 p.p.',1),f'{fmt(1094)} leads'),
 kv('phone','Taxa de contato',pct(CT,L,0),('+2,1 p.p.',1),f'{fmt(CT)} leads com 1º contato registrado'),kv('shield','SLA cumprido',"82%",('+3 p.p.',1),'1º contato dentro do prazo da unidade'),
 kv('users','Foram ao call center','19%',('−2 p.p.',1),'sem horário escolhido após 30 min'),kv('check','Comparecimento',pct(CP,CP+REALIZ_FALTA,0),('+1,4 p.p.',1),f'{fmt(CP)} de {fmt(CP+REALIZ_FALTA)} agendamentos já realizados','si'),
 kv('x','Faltas',fmt(316),('−4,2%',1),'mais 96 cancelamentos','si'),kv('refresh','Remarcações',fmt(131),('+8',-1),'pela área do cliente ou unidade','s'),
 kv('bell','Lembrete confirmado','61%',('+5 p.p.',1),'dos agendamentos com lembrete','i'),kv('cal','Agendamentos futuros',fmt(FUTUROS),('',0),'de 22/11 em diante')])+'</div>'
mx=max(t for *_,t in FAIXAS)
c_fx=card(f'{i("zap",16)} Velocidade do 1º contato x agendamento',hbar([(r,round(a/n*100),'#b0197e' if k<3 else ('#cfb0da' if k==6 else '#B4234A'),f'{fmt(n)} leads · {a} agendaram') for k,((r,n,_),a) in enumerate(zip(FAIXAS,AG_FX))],fmtv=lambda v:f'{v}%',mx=100)
  +'<div class="aviso l" style="margin-top:12px"><div>'+i('book',15)+'</div><div style="font-size:13px"><b>Por que importa</b><div class="meta">Empresas que tentam contato em até 1 hora têm quase 7 vezes mais chance de qualificar o lead do que as que esperam mais uma hora (Harvard Business Review, 2011, 1,25 milhão de leads). Na rede, quem recebe contato em até 5 min agenda 71%, contra 19% depois de 24 h.</div></div></div>',
  fonte('lead.primeiro_contato_em (unidade e call center); agenda','hoje, 16:40','s'))
hmx=max(HEAT)
def hc(v):
    r=v/hmx; a=0.08 if r<.25 else (.2 if r<.45 else (.34 if r<.62 else (.75 if r<.82 else .92)))
    return f'background:rgba(76,20,85,{a});color:{"#fff" if a>.5 else "#1d1424"}'
heat='<div class="rr-heat"><span class="h"></span>'+''.join(f'<span class="h">{d}</span>' for d in DSEM)+''.join(f'<span class="h">{h}</span>'+''.join(f'<span style="{hc(HEAT[d*7+k])}" title="{DSEM[d]}, {h}: {HEAT[d*7+k]} leads">{HEAT[d*7+k]}</span>' for d in range(7)) for k,h in enumerate(HORAS))+'</div>'
c_heat=card(f'{i("grid",16)} Quando os leads chegam',heat+f'<p class="meta" style="margin-top:10px">{pct(sum(HEAT[d*7+5] for d in range(7)),L,0)} chegam entre 19h e 22h, quando a maioria das unidades já fechou. Sugestão: call center da rede cobrindo noites e sábados.</p>',fonte('lead.criado_em, horário de Brasília','hoje, 16:40','s'))
lentas=sorted(UN,key=lambda x:-x['t1'])[:8]
c_lent=card(f'{i("alert",16)} Unidades mais lentas no 1º contato','<table class="t rr-tr"><thead><tr><th>Unidade</th><th class="num">1º contato</th><th class="num">Leads</th><th class="num">Agendam</th></tr></thead><tbody>'+''.join(f'<tr><td class="trunc"><a class="lk" href="{U97(x)}">{x["nome"]}</a><div class="meta">{x["cid"]}/{x["uf"]}</div></td><td class="num"><span class="pill {"r" if x["t1"]>30 else "a"}">{x["t1"]} min</span></td><td class="num">{x["l"]}</td><td class="num">{pct(x["ag"],x["l"],0)}</td></tr>' for x in lentas)+'</tbody></table>',fonte('mediana por unidade no período','hoje, 16:40','s'))
c_falta=card(f'{i("check",16)} Comparecimento e faltas',hbar([('Compareceram',CP,'#0B7A54'),('Faltaram',316,'#B4234A'),('Cancelaram sem remarcar',96,'#C77A00'),('Ainda vão acontecer',FUTUROS,'#cfb0da')])
  +'<div class="sep"></div>'+hbar([('Com lembrete confirmado',84,'#0B7A54'),('Lembrete sem resposta',63,'#C77A00'),('Sem lembrete',58,'#B4234A')],fmtv=lambda v:f'{v}%',mx=100)+'<p class="meta" style="margin-top:6px">Comparecimento por situação do lembrete (spec 002, entidade lembrete). Referência de mercado: 70 a 80% (Pronk, 2026).</p>',
  fonte('DocBiz (compareceu, faltou) e lembretes da área do cliente','hoje, 16:40','i'))
c_quem=card(f'{i("users",16)} Quem atendeu',hbar([('Equipe da unidade',2087,'#6f0052',f'{pct(1220,2087,0)} agendaram'),('Call center da rede',454,'#2C5BC4',f'{pct(312,454,0)} agendaram')]),fonte('lead.fila e responsável','hoje, 16:40','s'))
corpo=cab_rel('Atendimento do franqueado','Velocidade e qualidade do atendimento aos leads: 1º contato, SLA, horários de pico, call center, comparecimento e faltas.','rel-atend')+k92+f'''
<div class="rr-g rr-g2e">{c_fx}{c_heat}</div><div class="rr-g rr-g2">{c_lent}<div class="rr-g" style="margin:0">{c_falta}{c_quem}</div></div>'''
pg('rel-atend','Atendimento do franqueado',corpo.replace('id="tab-principal"','') if False else corpo.replace('<table class="t rr-tr"><thead><tr><th>Unidade</th><th class="num">1º contato','<table class="t rr-tr" id="tab-principal"><thead><tr><th>Unidade</th><th class="num">1º contato',1))

# ================= 93 QUIZ, LANDINGS E TRÁFEGO =================
EVD={e[0]:e[2] for e in EV}
k93='<div class="rr-kpis">'+''.join([kv('eye','Páginas de unidade abertas',fmt(EVD['unidade_visualizada']),('+9,6%',9.6),'visitas às páginas das unidades'),kv('edit','Formulários começados',fmt(EVD['lead_iniciado']),('+11,0%',11),pct(EVD['lead_iniciado'],EVD['unidade_visualizada'],2)+' das visitas'),
 kv('inbox','Leads por visita',pct(L,EVD['unidade_visualizada'],2),('+0,03 p.p.',1),f'{fmt(L)} leads'),kv('wa','Cliques no WhatsApp',fmt(EVD['whatsapp_clicado']),('+14%',14),f'{PONTO[2][1]} viraram lead identificado'),
 kv('phone','Cliques no telefone',fmt(EVD['telefone_clicado']),('+3%',3),f'{PONTO[3][1]} ligações rastreadas'),kv('pin','Cliques em como chegar',fmt(EVD['rota_clicada']),('+7%',7),'intenção de visita'),
 kv('sparkle','Quizzes começados',fmt(QZ['ini']),('+22%',22),'mesmo número da tela 66'),kv('check','Quizzes concluídos',fmt(QZ['fim']),('+19%',19),f'{QZ_PCT}% de conclusão'),
 kv('inbox','Leads do quiz',fmt(QZ['leads']),('+31%',31),pct(QZ['leads'],QZ['fim'],1)+' dos concluídos'),kv('zap','Eventos inválidos',EV_INVAL_PCT+'%',('−0,2 p.p.',1),'limite de alerta 1%')])+'</div>'
FORM_AG=round(PONTO[0][1]*0.52)
c_site=card(f'{i("globe",16)} Funil do formulário das páginas',funil2([('Visitas',EVD['unidade_visualizada'],'100%'),('Começaram o formulário',EVD['lead_iniciado'],pct(EVD['lead_iniciado'],EVD['unidade_visualizada'],2)+' das visitas'),('Enviaram o formulário',PONTO[0][1],pct(PONTO[0][1],EVD['lead_iniciado'],0)+' de quem começou'),('Agendaram',FORM_AG,pct(FORM_AG,PONTO[0][1],0)+' dos leads do formulário')])+f'<p class="meta" style="margin-top:8px">Só o formulário, para o abandono ser do formulário mesmo. Quiz ({PONTO[1][1]}), WhatsApp ({PONTO[2][1]}) e telefone ({PONTO[3][1]}) trazem os outros {fmt(L-PONTO[0][1])} leads: quiz ao lado e todos em <a class="lk" href="{LK("rel-funil")}">Leads e funil</a>.</p>'
  +'<p class="meta" style="margin-top:8px">Abandono do formulário: 2.758 começaram e não enviaram. Oportunidade: formulário em 2 etapas com salvamento parcial e WhatsApp como alternativa no mesmo bloco.</p>',fonte('coletor próprio (eventos do dicionário v3)','hoje, 16:40','s'))
VAR=[('Modelo A',46,151200,763),('Modelo B',52,163900,721),('Modelo C',32,97780,388)]
c_var=card(f'{i("layout",16)} Modelos de página e variantes','<table class="t rr-tr" id="tab-principal"><thead><tr><th>Modelo</th><th class="num">Unidades</th><th class="num">Visitas</th><th class="num">Leads pelo formulário</th><th class="num">Por mil visitas</th></tr></thead><tbody>'
  +''.join(f'<tr><td><b>{m}</b></td><td class="num">{u}</td><td class="num">{fmt(v)}</td><td class="num">{l}</td><td class="num"><b>{br(l/v*1000)}</b></td></tr>' for m,u,v,l in VAR)+f'</tbody></table><p class="meta" style="margin-top:8px">Modelo A converte 25% mais que o C com o mesmo tráfego. Testes A/B por unidade continuam na tela 29. Páginas de serviço (ex.: Depilação a laser no Alto da Lapa) entram como linhas próprias quando ativas.</p>',
  fonte('eventos com template e variante_id','hoje, 16:40','s'),dir=f'<a class="btn s" href="{LK("f-ab")}">Comparar A e B {i("chev",12)}</a>')
c_quiz=card(f'{i("sparkle",16)} Quiz "Qual tratamento combina com você?"',funil2([('Começaram',QZ['ini'],'100%'),('Concluíram',QZ['fim'],f'{QZ_PCT}%'),('Salvaram com conta',QZ['conta'],pct(QZ['conta'],QZ['fim'],0)+' dos concluídos'),('Viraram lead',QZ['leads'],pct(QZ['leads'],QZ['fim'],1)+' dos concluídos'),('Agendaram',236,'56% dos leads do quiz')])
  +'<div class="sep"></div><b style="font-size:13px">Procedimento recomendado no resultado</b>'+hbar(QZ['dem'])+f'<p class="meta" style="margin-top:8px"><a class="lk" href="{LK("intel")}">Demanda e recomendações (66)</a> · <a class="lk" href="{LK("quiz")}">Gerador de quiz (63)</a></p>',
  fonte('resposta_quiz e agg_quiz_dia (spec 003), sem dado pessoal','hoje, 16:40','s'))
c_disp2=card(f'{i("phone2",16)} Aparelho e canal das visitas',hbar([('Celular',322100,'#6f0052','78%'),('Computador',82580,'#2C5BC4','20%'),('Tablet',8200,'#9a8fa1','2%')])+'<div class="sep"></div>'+hbar([('Google (orgânico e perfil)',171300,'#2C5BC4'),('Google Ads',98400,'#4c1455'),('Meta Ads',64900,'#b0197e'),('Instagram orgânico',41200,'#8fa9e6'),('Direto e outros',37080,'#9a8fa1')]),
  fonte('coletor próprio; GA4 Data API como conferência (divergência '+DIVERG_GA4+'%)','hoje, 16:40','s','i'))
c_trk=card(f'{i("zap",16)} Saúde do rastreamento','<div class="rr-mini"><div><span class="meta">Eventos inválidos</span><b>'+EV_INVAL_PCT+'%</b><span class="meta">limite 1%</span></div><div><span class="meta">UTMs inválidas</span><b>'+UTM_INVAL_PCT+'%</b><span class="meta">alerta acima de 3%</span></div><div><span class="meta">Coletor x GA4</span><b>'+DIVERG_GA4+'%</b><span class="meta">aceitável até 5%</span></div></div>'
  +f'<p class="meta" style="margin-top:10px">Os números do hub dependem dessa saúde: com UTM inválida acima de 3%, a fonte "Direto e outros" cresce e o custo por fonte fica distorcido. <a class="lk" href="{LK("saude")}">Abrir saúde do tracking (70)</a></p>',fonte('alerta_tracking (spec 003)','hoje, 16:40','s'))
corpo=cab_rel('Quiz, landings e tráfego','O que acontece nas páginas das unidades e no quiz antes de virar lead, e a saúde dos dados que alimentam o hub.','rel-trafego')+k93+f'''
<div class="rr-g rr-g2e">{c_site}{c_quiz}</div><div class="rr-g rr-g2">{c_var}<div class="rr-g" style="margin:0">{c_disp2}{c_trk}</div></div>'''
pg('rel-trafego','Quiz, landings e tráfego',corpo)

# ================= 94 SEO LOCAL, GOOGLE E AVALIAÇÕES =================
IMPG=GBP['imp_busca_mob']+GBP['imp_maps_mob']+GBP['imp_busca_desk']+GBP['imp_maps_desk']
k94='<div class="rr-kpis">'+''.join([kv('star','Nota no Google (período)',br(AV['media'])+' ★',('+0,1',1),f'meta 4,5 · {fmt(AV["tot"])} avaliações de 1 a 21/11','i',href=LK('aval-rede')),
 kv('inbox','Sem resposta',fmt(AV['pend']),('',0),'avaliações aguardando resposta','i',href=LK('aval-rede'),alerta=True),
 kv('alert','Escaladas abertas',str(AV['esc_pend']),('',0),'nota 1 ou 2 ou menção a saúde','i',href=LK('aval-esc'),alerta=True),
 kv('clock','Respondidas em até 48 h',f"{AV['r48']}%",('+6 p.p.',1),f'meta 90% · mediana de {br(AV["medh"])} h','si',href=LK('aval-rede')),
 kv('shield','Notas 1 e 2 em até 24 h',f"{AV['r24_baixas']}%",('+4 p.p.',1),f'meta 100% · {AV["n_baixas"]} avaliações baixas','si',href=LK('aval-rede')),
 kv('link','Perfis vinculados',f"{GBP['vinculados']} de 130",('+9',1),f'{130-GBP["vinculados"]} unidades ainda sem acesso','i'),
 kv('eye','Aparições no Google',fmt(IMPG),('+6,3%',6.3),'busca e Maps, perfis vinculados','i'),kv('phone','Ligações pelo perfil',fmt(GBP['lig']),('+4,1%',4.1),'botão ligar do perfil','i'),
 kv('pin','Pedidos de rota',fmt(GBP['rotas']),('+8,8%',8.8),'abrir rotas no Maps','i'),kv('globe','Cliques no site',fmt(GBP['site']),('+5,0%',5),'botão site do perfil','i'),
 kv('wa','Cliques no WhatsApp do perfil',fmt(GBP['msg']),('+12%',12),'botão de mensagem','i'),kv('search','Cliques orgânicos',fmt(GSC['cliques']),('+7,7%',7.7),'Search Console, prefixos /unidade/','i'),
 kv('trend','Posição média',br(GSC['pos']),('−0,6, melhorou',1),'quanto menor, melhor','i')])+'</div>'
c_gbp=card(f'{i("google",16)} Perfil no Google das unidades',f'<div class="rr-atraso">{i("clock",14)}<span><b>Dado com atraso de 2 dias (D-2):</b> o Google entrega as métricas do perfil por dia, com até 48 h de atraso. Última leitura completa: 19/11. {130-GBP["vinculados"]} unidades ainda não deram acesso e ficam fora destes números.</span></div>'+hbar([('Busca no celular',GBP['imp_busca_mob'],'#2C5BC4'),('Maps no celular',GBP['imp_maps_mob'],'#5b82d6'),('Busca no computador',GBP['imp_busca_desk'],'#8fa9e6'),('Maps no computador',GBP['imp_maps_desk'],'#b6c8ef')])
  +'<div class="sep"></div><b style="font-size:13px">Ações a partir do perfil</b>'+hbar([('Pedidos de rota',GBP['rotas'],'#0B7A54'),('Cliques no site',GBP['site'],'#0B7A54'),('Ligações',GBP['lig'],'#0B7A54'),('WhatsApp',GBP['msg'],'#0B7A54')])
  +f'<p class="meta" style="margin-top:8px">{130-GBP["vinculados"]} unidades ainda não concederam acesso ao perfil: ficam fora destes números até o vínculo (mesma pendência da spec 004). A API entrega só totais diários, sem hora do dia.</p>',
  fonte('Business Profile Performance API, fetchMultiDailyMetricsTimeSeries','hoje, 06:00 (diário, D-2)','i'))
c_gsc=card(f'{i("search",16)} Busca orgânica (Search Console)','<div class="rr-mini"><div><span class="meta">Cliques</span><b>'+fmt(GSC['cliques'])+'</b></div><div><span class="meta">Impressões</span><b>'+fmt(GSC['imp'])+'</b></div><div><span class="meta">CTR</span><b>'+br(GSC['ctr'],2)+'%</b></div></div>'
  +'<table class="t rr-tr" id="tab-principal" style="margin-top:12px"><thead><tr><th>Consulta (agrupada)</th><th class="num">Cliques</th><th class="num">Posição</th></tr></thead><tbody>'+''.join(f'<tr><td class="trunc">{q}</td><td class="num">{fmt(c)}</td><td class="num">{br(p)}</td></tr>' for q,c,p in GSC_CONS)+'</tbody></table><p class="meta" style="margin-top:8px">Nomes de cidade e bairro agrupados para comparar unidades. Dados finais com 2 a 3 dias de atraso; o Search Console guarda 16 meses, então o hub arquiva o histórico.</p>',
  fonte('Search Console API, searchAnalytics.query por prefixo /unidade/&lt;slug&gt;/','hoje, 06:00 (D-3)','i'))
c_av=card(f'{i("star",16)} Avaliações do Google: metas de resposta','<div class="rr-bul">'+''.join(f'<div class="rr-bu"><b style="font-size:13px">{r}</b><span class="rr-bt"><i style="width:{v}%"></i><u style="left:{m}%"></u></span><span style="text-align:right;font-size:13px"><b>{v}%</b> <span class="meta">meta {m}%</span></span><span class="meta">{d}</span></div>' for r,v,m,d in [('Respondidas em até 48 h',AV['r48'],90,f'faltam {90-AV["r48"]} p.p. para a meta da spec 004'),('Notas 1 e 2 em até 24 h',AV['r24_baixas'],100,f'{AV["n_baixas"]} avaliações com nota 1 ou 2 no período'),('Respondidas no total',AV['tx'],95,f'{AV["pend"]} sem resposta; {AV["esc_pend"]} escaladas para a rede')])+'</div>'
  +f'''<ul class="rr-bench" style="margin-top:10px"><li>68% dos consumidores só escolhem negócios com 4 estrelas ou mais, e 31% exigem 4,5.</li><li>74% só consideram avaliações dos últimos 3 meses; 47% evitam negócios com menos de 20 avaliações.</li><li>80% preferem negócios que respondem a todas as avaliações; respostas genéricas afastam 50%.</li></ul>
<p class="meta">Fonte dos números de mercado: <a class="lk" href="https://www.brightlocal.com/research/local-consumer-review-survey/" target="_blank" rel="noopener">BrightLocal, Local Consumer Review Survey 2026</a> (1.002 consumidores dos EUA).</p>''',
  fonte('espelho das avaliações (spec 004, tela 84)','hoje, 15:40 (leitura a cada 4 h)','i','s'),dir=f'<a class="btn s" href="{LK("aval-rede")}">Abrir avaliações (84) {i("chev",12)}</a>')
ufs=[u for u,_ in UF_CONT.most_common(7)]; ufs_r=[u for u in UF_CONT if u not in ufs]
_grp=[(u,[u]) for u in ufs]+[(f'Demais ({len(ufs_r)} UFs)',ufs_r)]
_vinc=dict(zip([g for g,_ in _grp],dist(GBP['vinculados'],[sum(UF_CONT[u] for u in us) for _,us in _grp])))
def _lin_seo(g,us):
    n=sum(UF_CONT[u] for u in us); un=[y for y in UN if y['uf'] in us]
    return f'<tr><td><b>{g}</b></td><td class="num">{n}</td><td class="num">{_vinc[g]}</td><td class="num">{round(sum(completude(x) for x in UNID if x["nome_uf"] in us)/n)}%</td><td class="num">{br(nota_media(un))}</td></tr>'
c_seo=card(f'{i("target",16)} SEO local por estado','<table class="t rr-tr"><thead><tr><th>UF</th><th class="num">Unidades</th><th class="num">Perfis vinculados</th><th class="num">Completude</th><th class="num">Nota no período</th></tr></thead><tbody>'
  +''.join(_lin_seo(g,us) for g,us in _grp)+f'</tbody><tfoot><tr><td><b>Rede</b></td><td class="num">130</td><td class="num">{GBP["vinculados"]}</td><td class="num">{round(sum(completude(x) for x in UNID)/130)}%</td><td class="num">{br(nota_media(UN))}</td></tr></tfoot></table><p class="meta" style="margin-top:8px">Completude é a mesma da tela 05. Nota no período = média das avaliações recebidas de 1 a 21/11. <a class="lk" href="{LK("seo")}">SEO local da unidade (19)</a></p>',
  fonte('ficha da unidade (plataforma) e perfil do Google','hoje, 16:40','s','i'))
corpo=cab_rel('SEO local, Google e avaliações','Como as unidades aparecem no Google, o que as pessoas fazem a partir do perfil, a busca orgânica e a reputação.','rel-google')+k94+f'''
<div class="rr-g rr-g2e">{c_gbp}{c_gsc}</div><div class="rr-g rr-g2e">{c_av}{c_seo}</div>'''
pg('rel-google','SEO local, Google e avaliações',corpo)

# ================= 95 ÁREA DO CLIENTE =================
k95='<div class="rr-kpis">'+''.join([kv('users','Clientes com conta',fmt(CLI['base']),('+7,1%',7.1),'base da marca Gio'),kv('plus','Contas novas',fmt(CLI['novos']),('+18%',18),f'{QZ["conta"]} vieram do quiz'),
 kv('user','Ativos em 30 dias',fmt(CLI['ativos_30d']),('+9%',9),pct(CLI['ativos_30d'],CLI['base'],0)+' da base'),kv('wa','Aceitam WhatsApp',f"{CLI['cons']['WhatsApp']}%",('+2 p.p.',1),fmt(CONS_REDE['WhatsApp'])+' clientes'),
 kv('cal','Agendamentos online',fmt(CLI['ag_online']),('+24%',24),f'dentro dos {fmt(AG)} da rede','s'),kv('grid','Pacotes ativos',fmt(CLI['pac_ativos']),('+3%',3),'lidos da DocBiz','i'),
 kv('check','Sessões realizadas',fmt(CLI['sess_mes']),('+5%',5),'no período','i'),kv('alert','Pacotes acabando',fmt(CLI['pac_acabando']),('',0),'1 ou 2 sessões restantes','i'),
 kv('star','NPS pós-sessão',str(CLI['nps']),('+3',1),f'{fmt(CLI["nps_resp"])} respostas'),kv('tag','Vendas online',fmt(CLI['venda_online']),('',0),brl(CLI['venda_online_val'])+' (piloto)','f')])+'</div>'
c_cons=card(f'{i("shield",16)} Consentimentos por canal',hbar([(k,v,'#0B7A54',fmt(CONS_REDE[k])+' clientes') for k,v in CLI['cons'].items() if k!='Área do cliente'],fmtv=lambda v:f'{v}%',mx=100)
  +'<p class="meta" style="margin-top:8px">Percentual sobre os clientes com conta (100% têm acesso à área do cliente, que não é consentimento de marketing). Consentimento sempre desmarcado e por finalidade (spec 002, LGPD).</p>',fonte('consentimento (estado atual por finalidade e canal)','hoje, 16:40','s'))
c_vit=card(f'{i("tag",16)} Ofertas na área do cliente',f'<div class="rr-mini"><div><span class="meta">Exibições</span><b>{fmt(CLI["vitrine_exib"])}</b></div><div><span class="meta">Cliques</span><b>{fmt(CLI["vitrine_cli"])}</b></div><div><span class="meta">CTR</span><b>{pct(CLI["vitrine_cli"],CLI["vitrine_exib"],1)}</b></div></div>'
  +'<div class="sep"></div>'+hbar([('Avaliação gratuita de depilação',1620),('Verão sem pelos',1240),('Limpeza de pele com 20%',690),('Ultraformer: sessão bônus',410),('Indique e ganhe',250)])+'<p class="meta" style="margin-top:8px">Cliques nos cartões "Ofertas para você" e "Perto de você".</p>',fonte('cartao_area_cliente (exibições e cliques)','hoje, 16:40','s'))
c_ag=card(f'{i("cal",16)} Agendamentos e pacotes',hbar([('Agendados pela área do cliente',CLI['ag_online'],'#6f0052'),('Remarcados pelo cliente',CLI['remarc'],'#C77A00'),('Cancelados pelo cliente',CLI['cancel'],'#B4234A')])
  +'<div class="sep"></div>'+hbar([('Pacotes ativos',CLI['pac_ativos'],'#2C5BC4'),('Sessões realizadas no período',CLI['sess_mes'],'#2C5BC4'),('Pacotes acabando',CLI['pac_acabando'],'#C77A00','oportunidade de renovação: campanha automática "pacote acabando"'),('Vencem em 30 dias com sessões sobrando',214,'#B4234A')]),
  fonte('agendamento e pacote (fonte da verdade: DocBiz)','hoje, 16:40','i','s'))
c_nps=card(f'{i("star",16)} NPS e convite ao Google',hbar([('Promotores (9 e 10)',76,'#0B7A54'),('Neutros (7 e 8)',19,'#C77A00'),('Detratores (0 a 6)',5,'#B4234A')],fmtv=lambda v:f'{v}%',mx=100)
  +f'<div class="sep"></div><div class="rr-mini"><div><span class="meta">NPS</span><b>{CLI["nps"]}</b></div><div><span class="meta">Convites ao Google</span><b>{fmt(CLI["google_conv"])}</b></div><div><span class="meta">Clicaram</span><b>{fmt(CLI["google_cliq"])}</b></div></div><p class="meta" style="margin-top:8px">Convite para todos, sem filtro por nota e sem incentivo (regra da spec 002). Detratores abrem caso de recuperação no suporte.</p>',
  fonte('avaliacao (NPS) da área do cliente','hoje, 16:40','s'))
c_mur=card(f'{i("flag",16)} Mural de avisos e campanhas',f'<div class="rr-mini"><div><span class="meta">Confirmaram o último aviso</span><b>{MURAL_CONF} de 130</b></div><div><span class="meta">Campanhas para clientes</span><b>{len(CRM)} linhas</b></div><div><span class="meta">Agendamentos de campanha</span><b>{PF[3][1]}</b></div></div><p class="meta" style="margin-top:10px">{130-MURAL_CONF} unidades ainda não confirmaram: lembrete automático amanhã às 9h. <a class="lk" href="{LK("mural")}">Mural</a> · <a class="lk" href="{LK("perf")}">Performance de campanhas (62)</a></p>',
  fonte('aviso_destinatario e metrica_campanha_dia (spec 002)','hoje, 16:40','s'))
tab95='<table class="t rr-tr" id="tab-principal" style="display:none"><tbody>'+''.join(f'<tr><td>{r}</td><td>{v}</td></tr>' for r,v in [('Clientes com conta',CLI['base']),('Contas novas',CLI['novos']),('Agendamentos online',CLI['ag_online']),('Pacotes ativos',CLI['pac_ativos']),('NPS',CLI['nps'])])+'</tbody></table>'
corpo=cab_rel('Área do cliente','Contas, consentimentos, ofertas, agendamentos online, pacotes, NPS e avisos (spec 002). Vendas online entram com a fase 2.','rel-cliente')+k95+f'''
<div class="rr-g rr-g3">{c_cons}{c_vit}{c_nps}</div><div class="rr-g rr-g2e">{c_ag}{c_mur}</div>{tab95}'''
pg('rel-cliente','Área do cliente',corpo)

# ================= 96 UNIDADES E REGIÕES =================
def tcp(us): return soma(us,'cp')/soma(us,'real')
def rlin(nome,us,href):
    l=soma(us,'l'); nm=f'<a class="lk" href="{href}">{nome}</a>' if href else f'<b>{nome}</b>'
    return f'<tr><td>{nm}</td><td class="num">{len(us)}</td><td class="num">{fmt(l)}</td><td class="num">{br(l/len(us))}</td><td class="num">{pct(soma(us,"ag"),l,0)}</td><td class="num">{round(tcp(us)*100)}%</td><td class="num">{round(mediana([x["t1"] for x in us]))} min</td><td class="num">{brl(soma(us,"inv"))}</td><td class="num">{brl(soma(us,"inv")/soma(us,"lp"))}</td><td class="num">{br(nota_media(us))}</td></tr>'
c_reg=card(f'{i("map",16)} Regionais','<table class="t rr-tr"><thead><tr><th>Regional</th><th class="num">Unidades</th><th class="num">Leads</th><th class="num">Leads por unidade</th><th class="num">% que agenda</th><th class="num">Comparecimento</th><th class="num">1º contato</th><th class="num">Investido</th><th class="num">CPL</th><th class="num">Nota no período</th></tr></thead><tbody>'
  +''.join(rlin(r,[x for x in UN if x['reg']==r],'?reg='+r.replace(' ','+')) for r in REGS)+'</tbody><tfoot>'+rlin('Rede',UN,None)+'</tfoot></table>'
  +f'<p class="meta" style="margin-top:8px">Comparecimento = {COMP_DEF}. Nota no período = média das avaliações recebidas de 1 a 21/11.</p>',fonte('plataforma, APIs de mídia e perfil do Google','hoje, 16:40','s','i'))
tx_uf={uf:round(soma(us,'ag')/soma(us,'l')*100) for uf,us in UF_AG.items()}; t1_uf={uf:round(mediana([x['t1'] for x in us])) for uf,us in UF_AG.items()}
esc_t=lambda v:'#ead9f0' if v<55 else ('#d8bde3' if v<58 else ('#c39ad3' if v<61 else '#a877bd'))
esc_1=lambda v:'#a877bd' if v<=9 else ('#c39ad3' if v<=12 else ('#d8bde3' if v<=16 else '#ead9f0'))
mp3=lambda w,h:(f'<div data-m="l">{mapa_val(w,h,uf_lpu,esc_l,lambda v:br(v)+" leads por unidade")}</div><div data-m="t" hidden>{mapa_val(w,h,tx_uf,esc_t,lambda v:f"{v}% agendam")}</div><div data-m="c" hidden>{mapa_val(w,h,t1_uf,esc_1,lambda v:f"1º contato {v} min")}</div>')
c_map=card(f'{i("map",16)} Mapa por estado',f'<div class="sw" data-mapa data-acao-propria style="margin-bottom:10px;flex-wrap:wrap"><span class="on" data-v="l">Leads por unidade</span><span data-v="t">% que agenda</span><span data-v="c">1º contato</span></div>'
  +'<div data-mapa-link>'+mp3(380,350)+'</div><p class="meta">Tons mais escuros = melhor resultado em cada métrica. Clique num estado para filtrar a tabela das unidades.</p>',fonte('plataforma; malha IBGE','hoje, 16:40','s'))
c_map=c_map.replace('width="380"','width="380" style="max-width:100%;height:auto;display:block"')
qd=[[x for x in UN if x['q']==q] for q in (1,2,3,4)]
c_qt=card(f'{i("trend",16)} O que separa o 1º do 4º quartil','<table class="t rr-tr"><thead><tr><th>Indicador</th><th class="num">Q1</th><th class="num">Q2</th><th class="num">Q3</th><th class="num">Q4</th></tr></thead><tbody>'
  +''.join(f'<tr><td>{r}</td>'+''.join(f'<td class="num">{fn(us)}</td>' for us in qd)+'</tr>' for r,fn in [('Unidades',len),('Leads por unidade',lambda us:br(soma(us,"l")/len(us))),('% que agenda',lambda us:pct(soma(us,"ag"),soma(us,"l"),0)),('Comparecimento',lambda us:f'{round(tcp(us)*100)}%'),('1º contato (mediana)',lambda us:f'{round(mediana([x["t1"] for x in us]))} min'),('Nota no Google (acumulada)',lambda us:br(sum(x["nota_g"] for x in us)/len(us))),('Completude média',lambda us:f'{round(sum(COMPL_FIX.get(x["slug"],50) for x in us)/len(us))}%')])
  +'</tbody></table><p class="meta" style="margin-top:8px">O 1º contato é o que mais separa os quartis. A nota acumulada no Google também cai do Q1 ao Q4; a nota do período (só novembro) varia pouco entre quartis e fica nas regionais. Benchmarking por quartil é prática comum em redes de franquia (FRANdata).</p><div class="rr-exq"><span class="meta">Abrir o relatório de uma unidade de exemplo:</span>'+''.join(f'<a class="chip" href="{U97(us[len(us)//2])}">Q{n} · {us[len(us)//2]["nome"]}</a>' for n,us in zip((1,2,3,4),qd))+'</div>',fonte('índice de conversão por unidade','hoje, 16:40','s'))
QC={1:('#4c1455','c'),2:('#86106b','q'),3:('#b0197e','d'),4:('#4c1455','o')}
pts=[(x['l'],x['tx_ag']*100,5,QC[x['q']][0],f"{x['nome']} · Q{x['q']} · {x['l']} leads · {round(x['tx_ag']*100)}% agendam",U97(x),QC[x['q']][1]) for x in UN]
legq='<div class="leg rr-leg" style="gap:14px"><span><b style="color:#4c1455">●</b> Q1</span><span><b style="color:#86106b">■</b> Q2</span><span><b style="color:#b0197e">◆</b> Q3</span><span><b style="color:#4c1455">○</b> Q4</span><span class="meta">clique num ponto para abrir a unidade</span></div>'
c_sc=card(f'{i("target",16)} Volume x conversão das 130 unidades',legq+dupla(dispersao(pts,w=560,h=300,xr=(0,60),yr=(40,75),xl='leads no período (eixo X)',yl='% que agenda',fx=lambda v:f'{v:.0f}',fy=lambda v:f'{v:.0f}%',refx=L/130,refy=AG/L*100),dispersao(pts,w=340,h=260,xr=(0,60),yr=(40,75),xl='leads no período',yl='% agenda',fx=lambda v:f'{v:.0f}',fy=lambda v:f'{v:.0f}%',refx=L/130,refy=AG/L*100))
  +'<p class="meta">Direita e acima: muito lead e boa conversão. Esquerda e abaixo: pouca demanda e pouca conversão, prioridade de apoio. Linhas tracejadas: médias da rede.</p>',fonte('plataforma','hoje, 16:40','s'))
rows=''.join(f'<tr data-txt="{x["nome"].lower()} {x["cid"].lower()} {x["uf"].lower()}" data-reg="{x["reg"]}" data-q="{x["q"]}" data-uf="{x["uf"]}" data-slug="{x["slug"]}"><td class="num" data-v="{x["pos"]}">{x["pos"]}º</td><td data-v="{x["nome"]}" style="white-space:normal;min-width:170px"><a class="lk" href="{U97(x)}">{x["nome"]}</a><div class="meta">{x["cid"]} ({x["uf"]}) · {x["reg"]}</div></td><td class="num" data-v="{x["q"]}"><span class="pill {["","v","b","a","r"][x["q"]]}">Q{x["q"]}</span></td><td class="num" data-v="{x["idx"]}"><b>{x["idx"]}</b></td><td class="num" data-v="{x["l"]}">{x["l"]}<div class="meta {"up" if x["l"]>=x["l_ant"] else "down"}">{var(x["l"],x["l_ant"])[0]}</div></td><td class="num" data-v="{x["tx_ag"]:.3f}">{pct(x["ag"],x["l"],0)}</td><td class="num" data-v="{x["tx_cp"]:.3f}">{round(x["tx_cp"]*100)}%</td><td class="num" data-v="{x["vd"]}">{x["vd"]}</td><td class="num" data-v="{x["t1"]}">{x["t1"]} min</td><td class="num" data-v="{x["inv"]}">{brl(x["inv"])}</td><td class="num" data-v="{x["nota_g"]}">{br(x["nota_g"])}</td></tr>' for x in ORD)
c_tab=card(f'{i("list",16)} Todas as unidades',f'''<div class="rr-tools" data-filtra="tab-principal" data-acao-propria><div class="rr-busca">{i("search",14)}<input type="search" placeholder="Buscar unidade, cidade ou UF" aria-label="Buscar na tabela"></div>
<span class="chip on" data-reg="">Todas</span>'''+''.join(f'<span class="chip" data-reg="{r}">{r}</span>' for r in REGS)+''.join(f'<span class="chip" data-quart="{q}">Q{q}</span>' for q in (1,2,3,4))+f'''<span class="meta" data-nlin>130 de 130 unidades</span><button type="button" class="btn s" data-csv="tab-principal" data-nome="gio-unidades" style="margin-left:auto">{i("down",13)} CSV do recorte</button></div>
<div class="rr-scroll"><table class="t rr-tab rr-tr" id="tab-principal" data-ordena data-pagina="25"><thead><tr><th class="num" data-sort>#</th><th data-sort>Unidade</th><th class="num" data-sort>Quartil</th><th class="num" data-sort>Índice</th><th class="num" data-sort>Leads <span class="meta">(vs. out)</span></th><th class="num" data-sort>% que agenda</th><th class="num" data-sort title="compareceram ÷ agendamentos já realizados">Comparecimento</th><th class="num" data-sort>Vendas</th><th class="num" data-sort>1º contato</th><th class="num" data-sort>Mídia</th><th class="num" data-sort>Nota Google</th></tr></thead><tbody>{rows}</tbody></table></div>
<div class="rr-vazio" data-vazio hidden data-acao-propria><b>Nenhuma unidade neste recorte.</b><div class="meta" style="margin:4px 0 10px">Confira a busca, o estado ou o quartil escolhido.</div><button type="button" class="btn s" data-limpa-tab>Limpar filtros</button></div>
<div class="rr-pgr" data-pgr="tab-principal" data-acao-propria></div>
<p class="meta" style="margin-top:8px">25 unidades por página (10 no celular), cabeçalho fixo ao rolar. O CSV leva todas as unidades do recorte, não só a página. Clique no título da coluna para ordenar.</p>''',
  fonte('plataforma, DocBiz, APIs de mídia (rateio por geografia da campanha) e perfil do Google','hoje, 16:40','s','i','c'))
corpo=cab_rel('Unidades e regiões','Comparação entre regionais, estados e as 130 unidades, com quartis, mapa e a tabela completa para filtrar, ordenar e exportar.','rel-unidades')+f'''
<div class="rr-g rr-g2">{c_reg}{c_map}</div><div class="rr-g rr-g2e">{c_qt}{c_sc}</div>{c_tab}'''
pg('rel-unidades','Unidades e regiões',corpo,reage=True)

# ================= 97 RELATÓRIO DA UNIDADE (uma página por unidade: ?unidade=<slug>) =================
MED=dict(l=mediana([x['l'] for x in UN]),t1=mediana([x['t1'] for x in UN]),idx=mediana([x['idx'] for x in UN]))
REDE=dict(ct=round(CT/L*100),ag=round(AG/L*100),cp=round(CP/(CP+REALIZ_FALTA)*100),vd=round(VD/CP*100),cpl=round(INV/L_PAGO),medl=round(MED['l']),medt1=round(MED['t1']),medidx=round(MED['idx']),ticket=TICKET)
UJ=[[x['slug'],x['nome'],x['cid'],x['uf'],x['reg'],x['q'],x['pos'],x['idx'],x['l'],x['l_ant'],x['ct'],x['ag'],x['cp'],x['real'],x['vd'],x['t1'],x['inv'],x['lp'],x['nota_g'],x['nota'],x['nav'],x['pend'],x['lig'],x['rotas'],x['vis'],x['mod'],x['fon'],[[c[0],c[1],c[2],c[3],c[4]] for c in x['camps']],x['hist']] for x in UN]
ICS={k:i(k,15) for k in ['trend','inbox','cal','check','tag','clock','zap','phone','star','globe','filter','chart','send','sparkle','pin','search','chev','alert','users','eye','home','bell']}
FJ=[[f[1],f[4]] for f in FONTES]
def corpo97(modo):
    """modo 'rede' (escolhe a unidade pela URL) ou 'franq' (só a própria unidade, sem nomes de outras)"""
    cfg=_json.dumps(dict(modo=modo,padrao='altodalapa',rede=REDE,lk={'u':LK('rel-unidade'),'lista':LK('rel-unidades'),'ficha':LK('unidade') if modo=='rede' else LK('f-unidade'),'aval':LK('aval-un') if modo=='rede' else LK('f-aval'),'quiz':LK('rel-trafego'),'franq':LK('f-rel'),'atend':LK('rel-atend')}),ensure_ascii=False)
    dados=f'<script>var RR_U={_json.dumps(UJ,ensure_ascii=False,separators=(",",":"))};var RR_F={_json.dumps(FJ,ensure_ascii=False)};var RR_I={_json.dumps(ICS,ensure_ascii=False)};var RR_C={cfg};</script>'
    return dados+'<div id="rr97" aria-live="polite"></div>'+JS97
JS97=r'''<script>(function(){
var C=RR_C,R=C.rede,I=RR_I,Q=new URLSearchParams(location.search);
function f(n){return String(n).replace(/\B(?=(\d{3})+(?!\d))/g,'.');}
function brl(n){return 'R$ '+f(Math.round(n));}function br1(n){return n.toFixed(1).replace('.',',');}
function pc(a,b){return b?Math.round(a/b*100):0;}
function esc(t){return String(t).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]});}
function st(c){return {s:'<span class="pill v rr-st">Do sistema</span>',i:'<span class="pill b rr-st">Integração</span>',c:'<span class="pill a rr-st">Depende da Salus</span>'}[c]||'';}
function fonte(t,q,cs){return '<div class="rr-fonte">'+I.clock.replace('width="15" height="15"','width="12" height="12"')+'<span><b>Fonte:</b> '+t+' · atualizado '+q+' (horário de Brasília)</span><span class="rr-stw">'+cs.split('').map(st).join('')+'</span></div>';}
function card(t,c,fo,dir){return '<section class="card"><div class="hd"><h3>'+t+'</h3>'+(dir?'<div class="dir">'+dir+'</div>':'')+'</div>'+c+(fo||'')+'</section>';}
function kv(ic,rot,val,d,det,cs,bom){var s='';if(d){var ok=(d[1]>=0)===(bom!==false);s='<span class="'+(ok?'up':'down')+'">'+d[0]+'</span> ';}return '<div class="card kpi rr-k"><div class="l">'+I[ic]+' '+rot+'</div><div class="v">'+val+'</div><div class="d">'+s+det+'</div><div class="rr-kst">'+cs.split('').map(st).join('')+'</div></div>';}
var M={};RR_U.forEach(function(u){M[u[0]]=u;});
var slug=C.modo==='franq'?C.padrao:(Q.get('unidade')||((Q.get('un')||'').split(',').length===1&&Q.get('un'))||C.padrao);
var u=M[slug],box=document.getElementById('rr97');
if(!u){box.innerHTML='<div class="rr-vazio"><b>Unidade não encontrada</b><div class="meta" style="margin:4px 0 10px">O endereço pede a unidade "'+esc(slug)+'", que não existe ou não está no seu acesso.</div><a class="btn s" hr'+'ef="'+C.lk.lista+'">Escolher na lista de unidades</a></div>';return;}
var k={slug:u[0],nome:u[1],cid:u[2],uf:u[3],reg:u[4],q:u[5],pos:u[6],idx:u[7],l:u[8],lant:u[9],ct:u[10],ag:u[11],cp:u[12],real:u[13],vd:u[14],t1:u[15],inv:u[16],lp:u[17],ng:u[18],np:u[19],nav:u[20],pend:u[21],lig:u[22],rot:u[23],vis:u[24],mod:u[25],fon:u[26],camps:u[27],hist:u[28]};
document.title=k.nome+' · Relatório da unidade · Sistema de Unidades Gio (demonstração)';
var tag=C.modo==='franq'?'':'<button type="button" class="btn s" data-troca aria-expanded="false">'+I.search+' Trocar unidade</button>';
var troca=C.modo==='franq'?'':'<div class="rr-troca" hidden><div class="rr-busca">'+I.search+'<input type="search" placeholder="Buscar unidade, cidade ou UF" aria-label="Buscar unidade"></div><div class="rr-lst">'+RR_U.slice().sort(function(a,b){return a[1].localeCompare(b[1])}).map(function(x){return '<a class="rr-op" data-txt="'+esc((x[1]+' '+x[2]+' '+x[3]).toLowerCase())+'" hr'+'ef="'+C.lk.u+'?unidade='+x[0]+'"><span>'+esc(x[1])+'<small> · '+esc(x[2])+' ('+x[3]+') · Q'+x[5]+'</small></span></a>'}).join('')+'</div></div>';
var cab='<div class="card rr-ucab"><div class="un"><div class="ft" style="background-image:url(../assets/fotos/fachada.jpg);width:48px;height:48px"></div><div><b>'+esc(k.nome)+'</b><small>'+esc(k.cid)+' ('+k.uf+') · '+k.reg+' · quartil '+k.q+'</small></div></div><span class="pill '+['','v','b','a','r'][k.q]+'" style="margin-left:auto">'+k.pos+'º de 130</span>'+
 (C.modo==='franq'?'<a class="btn s" hr'+'ef="'+C.lk.ficha+'">Minha unidade '+I.chev+'</a>':'<a class="btn s" hr'+'ef="'+C.lk.ficha+'">Ficha da unidade '+I.chev+'</a>'+tag+'<a class="btn s ghost" hr'+'ef="'+C.lk.lista+'">Voltar para Unidades e regiões</a>')+troca+'</div>';
var ag=pc(k.ag,k.l),cp=pc(k.cp,k.real),cpl=k.lp?k.inv/k.lp:0,vl=pc(k.l-k.lant,k.lant);
var kp='<div class="rr-kpis">'+[kv('trend','Posição no ranking',k.pos+'º de 130',null,'quartil '+k.q+' · índice '+k.idx+' (mediana '+R.medidx+')','s'),
 kv('inbox','Leads',f(k.l),[(vl>=0?'+':'−')+Math.abs(vl)+'%',vl],'mediana da rede: '+R.medl,'s'),
 kv('cal','Agendados',f(k.ag),null,ag+'% dos leads · rede '+R.ag+'%','s'),
 kv('check','Comparecimento',cp+'%',null,k.cp+' de '+k.real+' agendamentos já realizados · rede '+R.cp+'%','si'),
 kv('tag','Vendas de pacote',f(k.vd),null,'receita de pacotes '+brl(k.vd*R.ticket),'ic'),
 kv('clock','1º contato (mediana)',k.t1+' min',null,'mediana da rede: '+R.medt1+' min','s'),
 kv('zap','Mídia atribuída',brl(k.inv),null,'CPL '+brl(cpl)+' · rede '+brl(R.cpl)+' (estimado por rateio)','i'),
 kv('phone','Ligações pelo perfil',f(k.lig),null,f(k.rot)+' pedidos de rota','i'),
 kv('star','Nota no Google',br1(k.ng)+' ★',null,'acumulada · no período '+br1(k.np)+' em '+k.nav+' avaliações · '+k.pend+' sem resposta','i'),
 kv('globe','Visitas à página',f(k.vis),null,'modelo '+k.mod+' da página da unidade','s')].join('')+'</div>';
function lin(r,a,b,d){var df=a-b;return '<tr><td style="white-space:normal">'+r+'<div class="meta">'+d+'</div></td><td class="num"><b>'+a+'%</b></td><td class="num">'+b+'%</td><td class="num"><span class="'+(df>=0?'up':'down')+'">'+(df>=0?'+':'−')+Math.abs(df)+' p.p.</span></td></tr>';}
var fu=card(I.filter+' Funil da unidade x rede','<table class="t rr-tr rr-fit" id="tab-principal"><thead><tr><th>Etapa</th><th class="num">Unidade</th><th class="num">Rede</th><th class="num">Diferença</th></tr></thead><tbody>'+
 lin('Leads com contato',pc(k.ct,k.l),R.ct,'contatos ÷ leads')+lin('Leads que agendam',ag,R.ag,'agendados ÷ leads')+lin('Comparecimento',cp,R.cp,'compareceram ÷ agendamentos já realizados')+lin('Comparecimentos que compram',pc(k.vd,k.cp),R.vd,'vendas ÷ compareceram')+'</tbody></table>'+
 '<p class="meta" style="margin-top:8px">'+(C.modo==='franq'?'Você vê só a sua unidade, com a posição no ranking e a mediana da rede. Nomes e números de outras unidades não aparecem.':'O franqueado vê esta mesma página só da própria unidade, com a posição e a mediana da rede, sem nomes nem números de outras unidades. <a class="lk" hr'+'ef="'+C.lk.franq+'">Ver como o franqueado do Alto da Lapa vê</a>')+'</p>',fonte('plataforma e DocBiz','hoje, 16:40','sc'));
var mx=Math.max.apply(null,k.fon.concat([1]));var fo=card(I.chart+' Fontes dos leads da unidade','<div class="rr-hb">'+k.fon.map(function(v,j){return [v,j]}).sort(function(a,b){return b[0]-a[0]}).filter(function(p){return p[0]>0}).map(function(p){return '<div class="rr-hr"><span class="rr-hl">'+RR_F[p[1]][0]+'</span><span class="rr-ht"><i style="width:'+Math.max(1.5,p[0]/mx*100).toFixed(1)+'%;background:'+RR_F[p[1]][1]+'"></i></span><b class="rr-hv">'+p[0]+'</b></div>'}).join('')+'</div>',fonte('UTM e click IDs','hoje, 16:40','s'));
var sl=0,sv=0;var ca=card(I.send+' Campanhas que trouxeram leads para a unidade','<table class="t rr-tr rr-fit"><thead><tr><th>Campanha</th><th class="num">Leads</th><th class="num">Custo rateado</th></tr></thead><tbody>'+k.camps.map(function(c){sl+=c[3];sv+=c[4];return '<tr><td style="white-space:normal">'+c[0]+' · '+esc(c[1])+'<div class="meta">alcance: '+c[2]+'</div></td><td class="num">'+c[3]+'</td><td class="num">'+brl(c[4])+'</td></tr>'}).join('')+'</tbody><tfoot><tr><td><b>Total da unidade</b></td><td class="num"><b>'+sl+'</b></td><td class="num"><b>'+brl(sv)+'</b></td></tr></tfoot></table><p class="meta" style="margin-top:8px">Rateio estimado das campanhas regionais pela participação da unidade nos leads de cada campanha; o total é a mídia atribuída do indicador acima. Investimento local próprio da unidade entra quando a política de tags liberar (tela 57).</p>',fonte('APIs de mídia e plataforma','hoje, 14:00','i'));
var hm=Math.max.apply(null,k.hist),ms=['jun','jul','ago','set','out','nov'];
var hi=card(I.trend+' Leads nos últimos 6 meses (até o dia 21 de cada mês)','<div class="rr-cols" role="img" aria-label="Leads por mês">'+k.hist.map(function(v,j){return '<div><b>'+v+'</b><span style="height:'+Math.max(4,v/hm*120).toFixed(0)+'px"'+(j===5?' class="on"':'')+'></span><small>'+ms[j]+'</small></div>'}).join('')+'</div>',fonte('plataforma','hoje, 16:40','s'));
var ac=[];
if(k.t1>30)ac.push(['r','clock','Reduzir o 1º contato ('+k.t1+' min)','A rede tem mediana de '+R.medt1+' min. Quem é contatado em até 5 min agenda 71%. Ver horários de pico.',C.lk.atend]);
else if(k.t1<=10)ac.push(['v','check','Manter o 1º contato abaixo de 10 min','Hoje '+k.t1+' min. É o que mais separa o 1º do 4º quartil.',null]);
if(ag<R.ag-3)ac.push(['a','cal','Melhorar a conversão em agendamento','A unidade agenda '+ag+'% dos leads, contra '+R.ag+'% da rede. Roteiro de ligação e oferta de horário no 1º contato.',null]);
if(k.pend>0)ac.push(['a','star','Responder as '+k.pend+' avaliações pendentes','Meta: 90% respondidas em 48 h e notas 1 e 2 em 24 h.',C.lk.aval+(C.modo==='franq'?'':'?u='+encodeURIComponent(k.nome).replace(/%20/g,'+'))]);
if(cp<R.cp)ac.push(['a','bell','Confirmar presença 24 h antes','Comparecimento de '+cp+'% contra '+R.cp+'% da rede.',null]);
if(k.q===4)ac.push(['r','users','Plano de apoio da regional','Unidade no 4º quartil: visita da regional e treinamento de atendimento neste mês.',null]);
ac.push(['l','sparkle','Ativar o quiz na recepção por QR','Unidades com QR do quiz têm 18% mais contas novas.',C.lk.quiz]);
var ap=card(I.sparkle+' Próximos passos sugeridos','<div class="lista-i">'+ac.slice(0,3).map(function(a){var t='<div class="ic '+a[0]+'">'+(I[a[1]]||I.sparkle)+'</div><div style="flex:1;min-width:0"><b>'+a[2]+'</b><div class="meta">'+a[3]+'</div></div>';return a[4]?'<a class="it" style="align-items:flex-start" hr'+'ef="'+a[4]+'">'+t+I.chev+'</a>':'<div class="it" style="align-items:flex-start">'+t+'</div>'}).join('')+'</div>',fonte('relatórios inteligentes (regras da rede)','hoje, 16:40','s'));
box.innerHTML=cab+kp+'<div class="rr-g rr-g2e">'+fu+fo+'</div><div class="rr-g rr-g2e">'+ca+'<div class="rr-g" style="margin:0">'+hi+ap+'</div></div>';
if(window.rrRotula)rrRotula(box);
var tb=box.querySelector('[data-troca]'),tp=box.querySelector('.rr-troca');
if(tb){tb.addEventListener('click',function(){tp.hidden=!tp.hidden;tb.setAttribute('aria-expanded',!tp.hidden);if(!tp.hidden)tp.querySelector('input').focus();});
 tp.querySelector('input').addEventListener('input',function(){var t=this.value.toLowerCase();tp.querySelectorAll('.rr-op').forEach(function(o){o.style.display=o.dataset.txt.indexOf(t)>=0?'':'none'});});}
})();</script>'''
corpo=cab_rel('Relatório da unidade','Tudo de uma unidade em uma página, comparado com a mediana da rede. Abre a partir do ranking, da tabela, do mapa ou de qualquer nome de unidade no hub.','rel-unidades',csv_nome='gio-relatorio-unidade')+corpo97('rede')
pg('rel-unidade','Relatório da unidade',corpo,reage=True)
# visão do franqueado: só a própria unidade, casco do franqueado, sem abas da rede nem troca de unidade
corpo_f=cabec('Relatório da minha unidade','Seus números do mês comparados com a mediana da rede. Por regra da rede, você vê só a sua unidade.',f'<span class="pill a rr-demo">{i("eye",12)} Demonstração</span><span data-acao-propria class="rr-acoes"><button type="button" class="btn" data-pdf>{i("file",14)} PDF</button><button type="button" class="btn p" data-csv="tab-principal" data-nome="gio-minha-unidade">{i("down",14)} CSV</button></span>')+f'<div class="rr-res" style="margin-bottom:16px"><span class="rr-rtx">{PER} · comparado com {PER_ANT} · GiO Alto da Lapa</span></div>'+corpo97('franq')
pg('f-rel','Relatório da minha unidade',corpo_f,modo='franqueado',ativo='f-rel')

# ================= 98 METAS, PREVISÃO E ALERTAS =================
acum=[sum(LD[:k+1]) for k in range(21)]; dias30=[f'{d:02d}/11' for d in range(1,31)]
media_d=(PREV-L)/9; proj=[None]*20+[acum[-1]]+[round(acum[-1]+media_d*k) for k in range(1,10)]
lo=[acum[-1]]+[round(acum[-1]+(PREV_LO-L)/9*k) for k in range(1,10)]; hi=[acum[-1]]+[round(acum[-1]+(PREV_HI-L)/9*k) for k in range(1,10)]
meta_l=[round(4000*(k+1)/30) for k in range(30)]
real=acum+[None]*9
c_prev=card(f'{i("trend",16)} Leads acumulados em novembro e previsão',leg([('Realizado','#4c1455',0),('Projeção','#b0197e',1),('Faixa provável','#e6d3ec',0),('Ritmo da meta (4.000)','#2C5BC4',1)])
  +dupla(linha([(real,'#4c1455',False,''),(proj,'#b0197e',True,''),(meta_l,'#2C5BC4',True,'')],dias30,w=760,h=260,band=(20,lo,hi),ymax=4700),linha([(real,'#4c1455',False,''),(proj,'#b0197e',True,''),(meta_l,'#2C5BC4',True,'')],dias30,w=360,h=230,band=(20,lo,hi),ymax=4700,passo=7))
  +f'<p class="meta">Projeção de {fmt(PREV)} leads (faixa de {fmt(PREV_LO)} a {fmt(PREV_HI)}), pelo ritmo das últimas 3 semanas com peso por dia da semana. Previsão mais robusta (modelo de série temporal com sazonalidade anual) quando houver 12 meses completos na plataforma.</p>',
  fonte('plataforma; meta informada pela Salus','hoje, 16:40','s','c'))
c_bul=card(f'{i("target",16)} Metas do mês','<div class="rr-bul">'+''.join(bullet(r,a,m,p,o,(lambda v:brl(v)) if 'Invest' in r else fmt) for r,a,m,p,o in METAS)+'</div>'+f'<p class="meta" style="margin-top:10px"><a class="lk" href="{LK("rel-config")}">Cadastrar ou ajustar metas (rede, regional e unidade)</a></p>',fonte('metas cadastradas pela Salus','hoje, 16:40','c'))
MR=[('Regional SP',2610,LEADS_UF['SP']),('Regional Sul',560,LEADS_UF['PR']+LEADS_UF['RS']+LEADS_UF['SC']),('Demais regionais',830,L-LEADS_UF['SP']-LEADS_UF['PR']-LEADS_UF['RS']-LEADS_UF['SC'])]
c_mr=card(f'{i("map",16)} Meta de leads por regional','<table class="t rr-tr" id="tab-principal"><thead><tr><th>Regional</th><th class="num">Meta</th><th class="num">Realizado</th><th class="num">Projeção</th><th class="num">Da meta</th></tr></thead><tbody>'
  +''.join(f'<tr><td><b>{r}</b></td><td class="num">{fmt(m)}</td><td class="num">{fmt(v)}</td><td class="num">{fmt(round(v*PREV/L))}</td><td class="num"><span class="{"up" if v*PREV/L>=m else "down"}">{pct(v*PREV/L,m,0)}</span></td></tr>' for r,m,v in MR)+'</tbody></table>',fonte('meta por regional (Salus); projeção proporcional','hoje, 16:40','c'))
REG_AL=[('Queda de leads acima de 25% na semana','UF, regional e unidade','Diária','Marketing e regional',True),('Anomalia fora da faixa prevista (série temporal)','Leads, agendamentos, CPL por campanha','Diária','Marketing',True),
 ('CPL da campanha acima de 30% da média de 4 semanas','Campanha','Diária','Marketing e agência',True),('1º contato acima de 60 min na semana','Unidade','Diária','Regional e unidade',True),
 ('Comparecimento abaixo de 65%','Unidade','Semanal','Regional',True),('Projeção abaixo de 90% da meta','Rede e regional','Semanal','Diretoria',True),('Avaliação 1 ou 2 estrelas sem resposta em 24 h','Unidade','A cada 4 h','Unidade e rede',True),('UTM inválida acima de 3%','Rede','Diária','Tracking',True),('Investimento acima de 105% do orçamento no ritmo','Plataforma de mídia','Diária','Marketing e financeiro',False)]
TOGC='border:0;padding:0;cursor:pointer;flex:none'
c_reg=card(f'{i("alert",16)} Regras de alerta e anomalia','<div class="aviso v rr-ok" hidden role="status" style="margin-bottom:10px"><div>'+i("check",15)+'</div><div data-txt style="font-size:13px"></div></div><table class="t rr-tr"><thead><tr><th>Regra</th><th>Recorte</th><th>Frequência</th><th>Situação</th></tr></thead><tbody>'+''.join(f'<tr><td class="trunc"><b>{r}</b><div class="meta">Recebe: {q}</div></td><td class="trunc">{c}</td><td>{f}</td><td><span data-acao-propria style="display:inline-flex;gap:8px;align-items:center"><button type="button" class="tog{" on" if on else ""}" role="switch" aria-checked="{"true" if on else "false"}" aria-label="Ligar ou desligar: {r}" data-tog="{r}" style="{TOGC}"></button><span class="meta" data-togl>{"Ligada" if on else "Desligada"}</span></span></td></tr>' for r,c,f,q,on in REG_AL)+'</tbody></table>'
  +'<p class="meta" style="margin-top:8px">A regra de anomalia segue a lógica do GA4: um modelo de série temporal prevê o valor do dia e alerta quando o real sai da faixa provável (90 dias de treino para série diária). <a class="lk" href="https://support.google.com/analytics/answer/9517187" target="_blank" rel="noopener">Google Analytics, detecção de anomalias</a></p>',
  fonte('regra_insight (spec 001, FR-028) com tipos novos da spec 005','hoje, 16:40','s'),dir=f'<a class="btn s" href="{LK("rel-config")}">{i("edit",13)} Editar limites e metas</a>')
c_al=card(f'{i("bell",16)} Alertas abertos: precisa de ação',lista_al(ALERTAS),fonte('alertas gerados pelas regras ao lado','hoje, 16:40','s'))
c_al2=card(f'{i("sparkle",16)} Oportunidades (não são alertas)',lista_al(BEM),fonte('relatórios inteligentes','hoje, 16:40','s'))
c_salus=card(f'{i("users",16)} O que precisamos da Salus para completar o hub','<div class="lista-i">'+''.join(f'<div class="it" style="align-items:flex-start"><div class="ic a">{i(ic,15)}</div><div><b>{t}</b><div class="meta">{d}</div></div></div>' for ic,t,d in [('target','Metas mensais','Leads, agendamentos, comparecimentos e vendas por rede, regional e unidade.'),('zap','Orçamento e custos de mídia','Acesso às contas do Google Ads e do Meta (ou MCC e Business Manager) e o orçamento por campanha.'),('tag','Vendas e receita na DocBiz','Pacotes vendidos, valor e unidade, por paciente, para fechar o funil até a venda (perguntas D3 da spec 002).'),('google','Acesso às APIs do Google','Business Profile APIs (mesmo pedido da spec 004) e Search Console por prefixo.')])+'</div>')
corpo=cab_rel('Metas, previsão e alertas','Ritmo contra as metas, previsão do mês, regras de alerta e anomalias, e o que falta da Salus.','rel-metas')+f'''
<div class="rr-g rr-g2">{c_prev}{c_bul}</div><div class="rr-g rr-g2">{c_reg}<div class="rr-g" style="margin:0">{c_al}{c_al2}</div></div><div class="rr-g rr-g2e">{c_mr}{c_salus}</div>'''
pg('rel-metas','Metas, previsão e alertas',corpo)

# ================= 89 CADASTRO DE METAS E REGRAS DE ALERTA =================
CSS89='''
.rr-in{width:110px;max-width:100%;border:1px solid var(--linha-forte);border-radius:8px;padding:7px 9px;font:inherit;font-size:14px;text-align:right;background:#fff;color:var(--tinta)}
.rr-in:focus{outline:2px solid #b0197e;outline-offset:1px}.rr-in.w{width:100%;text-align:left}select.rr-in{text-align:left;width:auto}
.rr-salva{position:sticky;bottom:0;z-index:5;display:flex;gap:8px;flex-wrap:wrap;align-items:center;padding:12px 16px;margin-top:16px;background:#fff;border:1px solid var(--linha);border-radius:12px;box-shadow:0 -4px 16px rgba(30,10,40,.06)}
.rr-conf{border:1px solid #b0197e;background:#fbf4f9;border-radius:12px;padding:14px;margin-top:14px}
.rr-chk{display:flex;flex-wrap:wrap;gap:6px}.rr-chk .chip{cursor:pointer}
.rr-fm{display:grid;grid-template-columns:1fr 1fr;gap:12px 14px}.rr-fm label{display:flex;flex-direction:column;gap:5px;font-weight:600;font-size:13px;color:var(--tinta-2);min-width:0}
.rr-fm .meta{font-weight:400}.rr-fm .full{grid-column:1/-1}
@media(max-width:640px){.rr-fm{grid-template-columns:1fr}}
.rr-acs{display:flex;gap:6px;flex-wrap:wrap}
'''
CSS+=CSS89
inp=lambda v,suf='',ar='':f'<span style="display:inline-flex;gap:6px;align-items:center;justify-content:flex-end"><input class="rr-in" type="text" inputmode="decimal" value="{v}" aria-label="{ar}" data-muda>{f"<span class=meta>{suf}</span>" if suf else ""}</span>'
MET89=[(r,fmt(m) if 'Invest' not in r else fmt(m),'R$' if 'Invest' in r else '',a,p,o) for r,a,m,p,o in METAS]
c_m1=card(f'{i("target",16)} Metas de novembro da rede','<table class="t rr-tr"><thead><tr><th>Indicador</th><th class="num">Meta</th><th class="num">Realizado até 21/11</th><th class="num">Projeção</th><th>Quem informa</th></tr></thead><tbody>'
  +''.join(f'<tr><td><b>{r}</b></td><td class="num">{inp(m,"",f"Meta de {r}")}</td><td class="num">{brl(a) if "Invest" in r else fmt(a)}</td><td class="num">{brl(p) if "Invest" in r else fmt(p)}</td><td>{o}</td></tr>' for r,m,_,a,p,o in MET89)
  +f'<tr><td><b>Avaliações respondidas em 48 h</b></td><td class="num">{inp("90","%","Meta de resposta em 48 horas")}</td><td class="num">{AV["r48"]}%</td><td class="num">—</td><td>Rede (tela 94)</td></tr>'
  +f'<tr><td><b>Notas 1 e 2 respondidas em 24 h</b></td><td class="num">{inp("100","%","Meta de resposta a notas baixas")}</td><td class="num">{AV["r24_baixas"]}%</td><td class="num">—</td><td>Rede (telas 84 e 94)</td></tr>'
  +f'<tr><td><b>1º contato (mediana)</b></td><td class="num">{inp("15","min","Meta de primeiro contato")}</td><td class="num">{round(mediana([x["t1"] for x in UN]))} min</td><td class="num">—</td><td>Rede</td></tr>'
  +'</tbody></table><p class="meta" style="margin-top:8px">As metas comerciais e o orçamento vêm da Salus; as de atendimento e avaliações a rede define aqui. A barra de metas da tela Metas e alertas e a manchete da visão executiva leem estes valores.</p>',fonte('metas cadastradas (tabela meta, spec 005)','hoje, 16:40','c','s'))
c_m2=card(f'{i("map",16)} Metas de leads por regional e unidade','<table class="t rr-tr"><thead><tr><th>Recorte</th><th class="num">Meta de leads</th><th class="num">Unidades</th><th>Como distribui</th></tr></thead><tbody>'
  +''.join(f'<tr><td><b>{r}</b></td><td class="num">{inp(fmt(m),"",f"Meta da {r}")}</td><td class="num">{n}</td><td>pelo histórico de 3 meses</td></tr>' for (r,m,v),n in zip(MR,[UF_CONT["SP"],UF_CONT["PR"]+UF_CONT["RS"]+UF_CONT["SC"],130-UF_CONT["SP"]-UF_CONT["PR"]-UF_CONT["RS"]-UF_CONT["SC"]]))
  +'</tbody><tfoot><tr><td><b>Soma das regionais</b></td><td class="num"><b>'+fmt(sum(m for _,m,_ in MR))+'</b></td><td class="num">130</td><td>igual à meta da rede</td></tr></tfoot></table>'
  +'<p class="meta" style="margin:12px 0 6px"><b>Exceção por unidade</b> (quando a regional combinar uma meta diferente):</p><table class="t rr-tr"><thead><tr><th>Unidade</th><th class="num">Meta sugerida</th><th class="num">Meta combinada</th></tr></thead><tbody>'
  +''.join(f'<tr><td><a class="lk" href="{U97(x)}">{x["nome"]}</a><div class="meta">quartil {x["q"]}</div></td><td class="num">{round(x["hist"][-2]*30/21*1.05)}</td><td class="num">{inp(round(x["hist"][-2]*30/21*1.05)+(10 if k==0 else 0),"",f"Meta combinada de {x['nome']}")}</td></tr>' for k,x in enumerate([[y for y in UN if y['q']==q][3] for q in (1,2,3,4)]))
  +'</tbody></table>',fonte('metas por regional e unidade (opcional)','hoje, 16:40','c'))
LIM=[('25','%'),('faixa','90%'),('30','%'),('60','min'),('65','%'),('90','%'),('24','h'),('3','%'),('105','%')]
c_r=card(f'{i("alert",16)} Regras de alerta: limite, frequência e quem recebe','<table class="t rr-tr"><thead><tr><th>Regra</th><th class="num">Limite</th><th>Frequência</th><th>Quem recebe</th><th>Ligada</th></tr></thead><tbody>'
  +''.join(f'<tr><td style="white-space:normal;min-width:180px"><b>{r}</b><div class="meta">{c}</div></td><td class="num">{inp(lv,ls,f"Limite: {r}") if lv!="faixa" else "<span class=meta>faixa provável "+ls+"</span>"}</td><td><select class="rr-in" aria-label="Frequência: {r}" data-muda>'+''.join(f'<option{" selected" if o==f else ""}>{o}</option>' for o in ['A cada 4 h','Diária','Semanal'])+f'</select></td><td style="white-space:normal">{q}</td><td><span data-acao-propria style="display:inline-flex;gap:8px;align-items:center"><button type="button" class="tog{" on" if on else ""}" role="switch" aria-checked="{"true" if on else "false"}" aria-label="Ligar ou desligar: {r}" data-tog="{r}" style="{TOGC}"></button><span class="meta" data-togl>{"Ligada" if on else "Desligada"}</span></span></td></tr>' for (r,c,f,q,on),(lv,ls) in zip(REG_AL,LIM))
  +'</tbody></table><p class="meta" style="margin-top:8px">Cada alerta aberto aparece na manchete da visão executiva, na tela Metas e alertas e no e-mail de quem recebe. O franqueado recebe só os alertas da própria unidade.</p>',fonte('regra_insight (spec 001, FR-028) com tipos novos da spec 005','hoje, 16:40','s'))
c_h=card(f'{i("clock",16)} Últimas alterações','<div class="lista-i">'+''.join(f'<div class="it" style="align-items:flex-start"><div class="ic l">{i(ic,15)}</div><div><b>{t}</b><div class="meta">{d}</div></div></div>' for ic,t,d in [('target','Meta de leads de novembro: 3.800 → 4.000','Marketing da rede · 03/11, 10h12'),('alert','Regra "UTM inválida acima de 3%" ligada','Tracking · 01/11, 9h40'),('alert','1º contato: limite de 45 → 60 min','Diretoria de operações · 28/10, 16h05')])+'</div><p class="meta" style="margin-top:8px">Todas as mudanças ficam na auditoria (tela 17).</p>',fonte('auditoria','hoje, 16:40','s'))
salva=f'''<div class="rr-salva" data-acao-propria><span class="meta" data-sujo>Nenhuma alteração pendente.</span><span style="margin-left:auto;display:flex;gap:8px;flex-wrap:wrap"><button type="button" class="btn s ghost" data-desfaz>Descartar</button><button type="button" class="btn p" data-toast="Metas e regras salvas. A visão executiva e a tela Metas e alertas passam a usar os novos valores na próxima leitura (simulado no protótipo; os números da demonstração não mudam).">{i("check",14)} Salvar metas e regras</button></span></div>
<script>(function(){{var s=document.querySelector('[data-sujo]'),n=0;document.querySelectorAll('[data-muda]').forEach(function(e){{e.dataset.ini=e.value;e.addEventListener('change',function(){{n=document.querySelectorAll('[data-muda]').length&&Array.prototype.filter.call(document.querySelectorAll('[data-muda]'),function(x){{return x.value!==x.dataset.ini}}).length;s.textContent=n?n+(n>1?' alterações pendentes':' alteração pendente')+'. Salve para aplicar.':'Nenhuma alteração pendente.';}});}});
document.querySelector('[data-desfaz]').addEventListener('click',function(){{document.querySelectorAll('[data-muda]').forEach(function(e){{e.value=e.dataset.ini}});s.textContent='Alterações descartadas.';}});}})();</script>'''
ok='<div class="aviso v rr-ok" hidden role="status" style="margin-bottom:14px"><div>'+i("check",15)+'</div><div data-txt style="font-size:13px"></div></div>'
corpo=cab_rel('Cadastro de metas e regras de alerta','Metas do mês (rede, regional e unidade) e as regras que geram os alertas do hub, com limite, frequência, quem recebe e liga/desliga.','rel-metas',agendar=False)+ok+f'''
<div class="rr-g">{c_m1}{c_m2}{c_r}{c_h}</div>{salva}'''
pg('rel-config','Cadastro de metas e regras de alerta',corpo)

# ================= 99 EXPORTAR E AGENDAR ENVIO =================
SECS=['Visão executiva','Aquisição e campanhas','Leads e funil','Atendimento','Quiz, landings e tráfego','SEO local e avaliações','Área do cliente','Unidades e regiões','Metas e alertas']
form=f'''<form class="rr-fm" data-agenda onsubmit="return false">
<label class="full">Nome do relatório<input class="rr-in w" name="nome" value="Resumo executivo semanal da rede" required></label>
<div class="full"><span style="font-weight:600;font-size:13px;color:var(--tinta-2)">Seções</span><div class="rr-chk" style="margin-top:6px" data-secs>'''+''.join(f'<button type="button" class="chip{" on" if s in ("Visão executiva","Aquisição e campanhas","Metas e alertas") else ""}" aria-pressed="{"true" if s in ("Visão executiva","Aquisição e campanhas","Metas e alertas") else "false"}">{s}</button>' for s in SECS)+f'''</div></div>
<label>Recorte<select class="rr-in w" name="rec"><option>Rede inteira</option>'''+''.join(f'<option>{r}</option>' for r in REGS)+f'''<option>Filtros atuais desta sessão</option></select></label>
<label>Período de cada envio<select class="rr-in w" name="per"><option>Semana anterior (segunda a domingo)</option><option>Mês anterior</option><option>Ontem</option></select></label>
<label>Formato<select class="rr-in w" name="fmt"><option>PDF executivo + CSV das tabelas</option><option>Só PDF</option><option>Só CSV</option></select></label>
<label>Frequência<select class="rr-in w" name="freq"><option>Toda segunda-feira</option><option>Todo dia útil</option><option>Todo dia 1º do mês</option></select></label>
<label>Horário (Brasília)<input class="rr-in w" name="hora" type="time" value="08:00"></label>
<label>Destinatários<input class="rr-in w" name="para" value="diretoria@exemplo.com.br, marketing@exemplo.com.br"><span class="meta">Só pessoas com acesso à plataforma; cada uma recebe no próprio escopo.</span></label>
<label class="full">Mensagem de abertura<input class="rr-in w" name="msg" value="Bom dia. Segue o resumo da rede com os destaques da semana."></label>
</form>
<div class="aviso l" style="margin-top:14px"><div>{i("shield",15)}</div><div style="font-size:13px"><b>Sem dado pessoal no envio</b><div class="meta">PDF e CSV agendados levam só números agregados. Exportação com nome, telefone ou e-mail de lead exige perfil com permissão de dado pessoal, fica na auditoria (tela 17) e não pode ser agendada.</div></div></div>
<div data-acao-propria style="display:flex;gap:8px;flex-wrap:wrap;margin-top:14px"><button type="button" class="btn p" data-ag-rev>{i("check",14)} Revisar e agendar</button><button type="button" class="btn" data-toast="Prévia enviada para o seu e-mail (simulado no protótipo).">{i("send",14)} Enviar uma prévia para mim</button></div>
<div class="rr-conf" data-ag-conf hidden role="dialog" aria-label="Confirmar agendamento"><b>Confirme o agendamento</b><div class="meta" data-ag-res style="margin:6px 0 10px"></div><div data-acao-propria style="display:flex;gap:8px;flex-wrap:wrap"><button type="button" class="btn p" data-ag-ok>{i("check",14)} Confirmar</button><button type="button" class="btn s ghost" data-ag-volta>Voltar e ajustar</button></div></div>'''
c_form=card(f'{i("mail",16)} Agendar envio por e-mail',form)
prev=f'''<div style="border:1px solid var(--linha);border-radius:12px;overflow:hidden"><div style="background:var(--grad);padding:12px 14px;display:flex;align-items:center;gap:10px"><img src="../assets/logo-gio-branco.png" alt="Gio" style="height:24px"><span style="color:#fff;font:600 13px Inter">Resumo executivo · {PER}</span></div>
<div style="padding:14px"><div class="g" style="grid-template-columns:repeat(3,minmax(0,1fr));gap:8px">'''+''.join(f'<div><div class="meta">{r}</div><b>{v}</b><div class="meta {c}">{d}</div></div>' for r,v,d,c in [('Leads',fmt(L),var(L,ANT['L'])[0],'up'),('Agendados',fmt(AG),var(AG,ANT['AG'])[0],'up'),('Retorno da mídia paga',br(ROAS)+'x','pacotes atribuídos ÷ mídia','')])+f'''</div>
<div style="margin:10px 0">{colunas(LD[-14:],DIAS[-14:],w=340,h=120)}</div><p class="meta">Destaques: projeção de {pct(PREV,4000,0)} da meta de leads; Goiás −31% na semana; {AV["esc_pend"]} avaliações escaladas sem resposta.</p><p class="meta">Página 1 de 4 · gerado às 08:00 (horário de Brasília) · números agregados</p></div></div>'''
c_prev2=card(f'{i("file",16)} Prévia do PDF',prev)
AGS=[('Resumo executivo semanal da rede','Segunda, 8h','PDF + CSV','Diretoria e marketing · 6 pessoas','há 5 dias · 6 de 6 abriram',True),('Campanhas e mídia','Dia útil, 9h','CSV','Agência · 2 pessoas','hoje, 9h · entregue',True),('Regional SP: unidades e atendimento','Segunda, 9h','PDF','Gestor regional · 1 pessoa','há 5 dias · entregue',True),('Avaliações da rede (mensal)','Dia 1º, 8h','PDF','Marketing · 3 pessoas','01/11 · 1 destinatário sem acesso, não enviado a ele',False)]
def lag(a,b,c,d,e,on): return f'<tr data-ag-lin><td style="white-space:normal;min-width:170px"><b>{a}</b><div class="meta">{d}</div></td><td>{b}</td><td>{c}</td><td style="white-space:normal">{e}</td><td><span class="pill {"v" if on else "z"}" data-ag-st>{"Ativo" if on else "Pausado"}</span></td><td><span class="rr-acs" data-acao-propria><button type="button" class="btn s" data-ag-pausa>{"Pausar" if on else "Retomar"}</button><button type="button" class="btn s" data-toast="Envio de &quot;{a}&quot; disparado agora para {d.split(" · ")[1]} (simulado).">Enviar agora</button><button type="button" class="btn s ghost" data-ag-exc>Excluir</button></span></td></tr>'
c_ags=card(f'{i("cal",16)} Envios agendados','<div class="aviso v rr-ok" hidden role="status" style="margin-bottom:10px"><div>'+i("check",15)+'</div><div data-txt style="font-size:13px"></div></div><table class="t rr-tr" id="tab-principal"><thead><tr><th>Relatório</th><th>Quando</th><th>Formato</th><th>Último envio</th><th>Situação</th><th>Ações</th></tr></thead><tbody data-ag-tb>'+''.join(lag(*a) for a in AGS)+'</tbody></table><div class="rr-vazio" data-ag-vazio hidden><b>Nenhum envio agendado.</b><div class="meta">Use o formulário acima para criar o primeiro.</div></div>',fonte('relatorio_salvo e envio_agendado (spec 005)','hoje, 16:40','s'))
c_now=card(f'{i("down",16)} Exportar agora',f'<div data-acao-propria style="display:flex;gap:8px;flex-wrap:wrap"><button type="button" class="btn" data-csv="tab-principal" data-nome="gio-envios-agendados">{i("down",14)} CSV desta lista</button><button type="button" class="btn" data-pdf>{i("file",14)} PDF desta página</button><a class="btn" href="{LK("rel-unidades")}">CSV das 130 unidades</a></div><p class="meta" style="margin-top:8px">Cada tela do hub também tem PDF e CSV no topo, sempre com os filtros ativos.</p>')
JS99=r'''<script>(function(){
var f=document.querySelector('[data-agenda]'),cf=document.querySelector('[data-ag-conf]'),tb=document.querySelector('[data-ag-tb]'),ok=document.querySelector('.rr-ok');
function toast(t){if(ok){ok.hidden=false;ok.querySelector('[data-txt]').textContent=t;ok.scrollIntoView({block:'nearest'});}}
function secs(){return Array.prototype.map.call(document.querySelectorAll('[data-secs] .chip.on'),function(c){return c.textContent});}
document.querySelectorAll('[data-secs] .chip').forEach(function(c){c.addEventListener('click',function(e){e.preventDefault();c.classList.toggle('on');c.setAttribute('aria-pressed',c.classList.contains('on'));});});
function vazio(){document.querySelector('[data-ag-vazio]').hidden=!!tb.querySelector('tr');}
function liga(tr){var p=tr.querySelector('[data-ag-pausa]'),s=tr.querySelector('[data-ag-st]'),x=tr.querySelector('[data-ag-exc]'),n=tr.querySelector('b').textContent;
 p.addEventListener('click',function(){var on=s.textContent==='Ativo';s.textContent=on?'Pausado':'Ativo';s.className='pill '+(on?'z':'v');p.textContent=on?'Retomar':'Pausar';toast((on?'Envio pausado: ':'Envio retomado: ')+n+'.');});
 x.addEventListener('click',function(){if(x.dataset.c){tr.remove();vazio();toast('Envio excluído: '+n+'. Fica registrado na auditoria.');}else{x.dataset.c=1;x.textContent='Confirmar exclusão';x.classList.remove('ghost');setTimeout(function(){if(x.isConnected){delete x.dataset.c;x.textContent='Excluir';x.classList.add('ghost');}},4000);}});}
tb.querySelectorAll('tr').forEach(liga);
document.querySelector('[data-ag-rev]').addEventListener('click',function(){var s=secs();if(!f.nome.value.trim()||!s.length||!f.para.value.trim()){toast('Preencha o nome, pelo menos uma seção e os destinatários.');return;}
 var n=f.para.value.split(',').filter(function(x){return x.trim()}).length;cf.querySelector('[data-ag-res]').textContent='"'+f.nome.value+'" · '+s.join(', ')+' · '+f.rec.value+' · '+f.fmt.value+' · '+f.freq.value+' às '+f.hora.value+' (Brasília) · '+n+(n>1?' destinatários':' destinatário')+'. O primeiro envio sai no próximo horário programado.';cf.hidden=false;cf.scrollIntoView({block:'nearest'});});
document.querySelector('[data-ag-volta]').addEventListener('click',function(){cf.hidden=true;});
document.querySelector('[data-ag-ok]').addEventListener('click',function(){var n=f.para.value.split(',').filter(function(x){return x.trim()}).length;var d=document.createElement('tbody');
 d.innerHTML='<tr data-ag-lin><td style="white-space:normal;min-width:170px"><b></b><div class="meta"></div></td><td></td><td></td><td>ainda não enviado</td><td><span class="pill v" data-ag-st>Ativo</span></td><td><span class="rr-acs" data-acao-propria><button type="button" class="btn s" data-ag-pausa>Pausar</button><button type="button" class="btn s ghost" data-ag-exc>Excluir</button></span></td></tr>';
 var tr=d.firstChild;tr.querySelector('b').textContent=f.nome.value;tr.querySelector('.meta').textContent=f.rec.value+' · '+n+(n>1?' pessoas':' pessoa');tr.children[1].textContent=f.freq.value.replace('Toda ','').replace('Todo ','')+', '+f.hora.value;tr.children[2].textContent=f.fmt.value;
 tb.insertBefore(tr,tb.firstChild);liga(tr);if(window.rrRotula)rrRotula(tr.closest('table').parentNode);cf.hidden=true;vazio();toast('Agendamento criado: '+f.nome.value+'. Aparece no topo da lista abaixo (simulado no protótipo).');});
})();</script>'''
corpo=cab_rel('Exportar e agendar envio','Relatórios em PDF e CSV para os executivos, no horário certo e no escopo de cada pessoa.','rel-export',agendar=False)+f'''
<div class="rr-g rr-g2">{c_form}<div class="rr-g" style="margin:0">{c_prev2}{c_now}</div></div>{c_ags}'''+JS99
pg('rel-export','Exportar e agendar envio',corpo)
print('s12 ok')
