"""Monta o protótipo navegável estático em ../prototipo/ a partir de ../telas/ (mesmo HTML e CSS das telas).
Uso: python3 prototipo.py   (rodar depois dos geradores s1 a s9 e do render)."""
import os, re, shutil, glob, html
from base import ARQ, D
OUT=f'{D}/prototipo'
if os.path.exists(OUT): shutil.rmtree(OUT)
os.makedirs(f'{OUT}/telas'); os.makedirs(f'{OUT}/assets'); os.makedirs(f'{OUT}/png')
for n in ['fonts','fotos']: shutil.copytree(f'{D}/assets/{n}',f'{OUT}/assets/{n}')
for f in ['logo-gio.png','logo-gio-branco.png','fachada.jpg']: shutil.copy(f'{D}/assets/{f}',f'{OUT}/assets/{f}')
shutil.copy(f'{D}/telas/estilo.css',f'{OUT}/telas/estilo.css')
shutil.copy(f'{D}/gerador/proto/proto.css',f'{OUT}/telas/proto.css'); shutil.copy(f'{D}/gerador/proto/proto.js',f'{OUT}/telas/proto.js')
INV={v:k for k,v in ARQ.items()}
def perfil(k):
    if k in ('login','2fa','senha'): return 'acesso'
    if k.startswith(('f-','m-')): return 'franqueado'
    if k.startswith(('c-','q-')): return 'cliente'
    if k.startswith('lp'): return 'publico'
    return 'rede'
PAR={'lpA':'lpAm','lpB':'lpBm','lpC':'lpCm','c-inicio-d':'c-inicio','c-ofertas-d':'c-ofertas','c-pacote-d':'c-pacote','c-privacidade-d':'c-privacidade','c-perfil-d':'c-perfil','c-agendar-d':'c-horarios'}
PARD={'lpAm':'lpA','lpBm':'lpB','lpCm':'lpC','c-inicio':'c-inicio-d','c-ofertas':'c-ofertas-d','c-pacote':'c-pacote-d','c-privacidade':'c-privacidade-d','c-perfil':'c-perfil-d','c-horarios':'c-agendar-d'}
pngs=set()
for f in sorted(glob.glob(f'{D}/telas/[0-9]*.html')):
    nome=os.path.basename(f)[:-5]; k=INV.get(nome,'')
    s=open(f,encoding='utf-8').read()
    mob='content="width=390"' in s
    s=re.sub(r'<meta name="viewport" content="[^"]*">','<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><link rel="icon" href="data:,">',s)
    s=s.replace('<link rel="stylesheet" href="estilo.css">','<link rel="stylesheet" href="estilo.css"><link rel="stylesheet" href="proto.css">')
    attrs=f' class="{"p-mob" if mob else "p-desk"}" data-perfil="{perfil(k)}"'
    if k in PAR: attrs+=f' data-par-mobile="{ARQ[PAR[k]]}.html"'
    if k in PARD: attrs+=f' data-par-desktop="{ARQ[PARD[k]]}.html"'
    s=s.replace('<body>',f'<body{attrs}>',1)
    s=s.replace('</body>','<script src="proto.js"></script></body>')
    pngs.update(re.findall(r'\.\./png/([\w-]+\.png)',s))
    open(f'{OUT}/telas/{nome}.html','w',encoding='utf-8').write(s)
for p in pngs: shutil.copy(f'{D}/png/{p}',f'{OUT}/png/{p}')
# índice: seletor de perfil e todas as telas
import importlib.util
spec=importlib.util.spec_from_file_location('gal',f'{D}/gerador/galeria_dados.py'); gal=importlib.util.module_from_spec(spec); spec.loader.exec_module(gal)
blocos=''
for g,itens in gal.G:
    blocos+=f'<h2>{html.escape(g)}</h2><div class="lst">'+''.join(f'<a href="telas/{n}.html?fixo=1"><b>{n[:2]}</b><span><strong>{html.escape(t)}</strong><small>{html.escape(p)}</small></span></a>' for n,p,t,d in itens)+'</div>'
idx=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow">
<link rel="icon" href="data:,"><title>Protótipo navegável · Sistema de Unidades Gio (demonstração)</title><link rel="stylesheet" href="telas/estilo.css"><style>
body{{background:var(--fundo)}}.w{{max-width:1180px;margin:0 auto;padding:32px 20px 60px}}
.topo .selo{{white-space:normal}}.topo{{display:flex;align-items:center;gap:14px;flex-wrap:wrap}}.topo img{{height:40px}}
h1{{font-size:28px;margin:18px 0 6px}}h2{{font-size:18px;margin:28px 0 10px}}
.perf{{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:20px}}
.perf a{{background:#fff;border:1px solid var(--linha);border-radius:16px;padding:20px;box-shadow:var(--sombra);display:block}}
.perf a b{{font:600 18px Poppins;display:block;margin-bottom:4px}}.perf a span{{color:var(--tinta-3)}}
.perf a.r{{background:var(--grad);color:#fff;border:0}}.perf a.r span{{color:#fff}}
.lst{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}}
.lst a{{display:flex;gap:10px;align-items:flex-start;background:#fff;border:1px solid var(--linha);border-radius:12px;padding:12px}}
.lst a>b{{font:600 13px Inter;color:var(--vinho);background:var(--lilas-100);border-radius:8px;padding:2px 7px}}
.lst strong{{display:block;font-weight:600}}.lst small{{color:var(--tinta-3);font-size:12px}}
@media(max-width:800px){{.perf,.lst{{grid-template-columns:1fr}}}}
</style></head><body><div class="w">
<div class="topo"><img src="assets/logo-gio.png" alt="Gio"><span class="selo">● Ambiente de demonstração · dados fictícios, sem leads reais</span></div>
<h1>Protótipo navegável do Sistema de Unidades</h1><p class="muted">Escolha um perfil para entrar. Em qualquer tela, a barra escura no topo troca o perfil ou volta para esta lista. Botões sem tela própria mostram um aviso de ação simulada; nada é enviado.</p>
<div class="perf"><a class="r" href="telas/04-admin-dashboard-rede.html"><b>Rede</b><span>Portal da rede: 130 unidades, leads, campanhas, controles, auditoria, quiz e tracking.</span></a>
<a href="telas/24-franqueado-dashboard.html"><b>Franqueado</b><span>Portal da GiO Alto da Lapa: ficha, página, procedimentos, campanhas e tags.</span></a>
<a href="telas/46-cliente-mobile-inicio.html" id="lk-cli"><b>Cliente</b><span>Área do cliente: conta, ofertas, agendamento, pacote, privacidade e quiz.</span></a></div>
<p class="meta" style="margin-top:10px">Acesso interno começa no <a class="lk" href="telas/01-login.html">login</a> (sem cadastro aberto). Cliente cria a própria conta em <a class="lk" href="telas/43-cliente-mobile-entrar.html">Entrar ou criar conta</a>.</p>
{blocos}
<p class="meta" style="margin-top:30px">Ambiente de demonstração. Números e pessoas são ilustrativos, salvo quando a fonte é citada. Página fora de indexação.</p></div>
<script>if(window.innerWidth>=1100)document.getElementById('lk-cli').href='telas/52-cliente-inicio-desktop.html';</script></body></html>'''
open(f'{OUT}/index.html','w',encoding='utf-8').write(idx)
open(f'{OUT}/_headers','w').write('/*\n  X-Robots-Tag: noindex, nofollow\n  X-Frame-Options: SAMEORIGIN\n  Referrer-Policy: no-referrer\n  X-Content-Type-Options: nosniff\n')
open(f'{OUT}/robots.txt','w').write('User-agent: *\nDisallow: /\n')
open(f'{OUT}/404.html','w',encoding='utf-8').write('<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="robots" content="noindex, nofollow"><title>Página não encontrada</title></head><body style="font-family:sans-serif;padding:40px">Página não encontrada. <a href="index.html">Voltar ao protótipo</a></body></html>')
print('prototipo ok', len(glob.glob(f'{OUT}/telas/*.html')),'telas', len(pngs),'miniaturas')
