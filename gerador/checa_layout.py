"""Checagem automática de layout do protótipo navegável, com navegador headless, em 360, 390, 768, 1024, 1280, 1440 e 1920 px, com e sem ?fixo=1.
Inclui checagem de formulário esticado: campo mais alto que o conteúdo, vão > 48 px entre campos seguidos, card de formulário muito mais alto que o conteúdo.
Para cada uma das 70 telas: área útil ocupada (sem faixa lateral > 24 px fora da sidebar), elementos sobrepostos,
campos e rótulos desalinhados na mesma linha, overflow horizontal, texto cortado, fonte mínima e contraste AA.
Saída: ../revisao-layout/relatorio.json, resumo.csv e prints em ../revisao-layout/<largura>/.
Uso: python3 checa_layout.py [tela ...]"""
import sys,os,re,json,glob,asyncio,subprocess,time,csv
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))+'/..'
SITE=[p for p in glob.glob(D+'/*') if os.path.isdir(p) and os.path.exists(p+'/_headers')][0]
OUT=D+'/revisao-layout'
LARG=[360,390,768,1024,1280,1440,1920]
MODOS=[('?fixo=1',''),('','-sf')]  # com ?fixo=1 (como o índice abre) e sem (com os redirecionamentos de celular/computador)
CHECK=re.search(r"CHECK=r'''(.*?)'''",open(D+'/gerador/render.py').read(),re.S).group(1)
LAYOUT=r'''()=>{
const vw=document.documentElement.clientWidth, P=[];
const vis=e=>{const s=getComputedStyle(e);return s.display!=='none'&&s.visibility!=='hidden'&&e.getBoundingClientRect().width>0};
const rolavel=e=>{let a=e.parentElement;while(a&&a!==document.body){const s=getComputedStyle(a);if(/(auto|scroll)/.test(s.overflowX))return true;a=a.parentElement;}return false};
const sobreposto=e=>{let a=e;while(a&&a!==document.body){const s=getComputedStyle(a);if(s.position==='absolute'||s.position==='fixed'||s.position==='sticky')return true;a=a.parentElement;}return false};
// 1. overflow horizontal da página
if(document.documentElement.scrollWidth>window.innerWidth+1) P.push('OVERFLOW:página '+document.documentElement.scrollWidth+'px');
// 2. área útil
const app=document.querySelector('.app'), mob=document.querySelector('.mob');
if(app){const side=app.querySelector('.side'), main=app.querySelector('.main'); const mr=main.getBoundingClientRect();
 const sr=side&&vis(side)?side.getBoundingClientRect():null; const esq=sr?mr.left-sr.right:mr.left, dir=vw-mr.right;
 if(esq>24) P.push('FAIXA:esquerda '+Math.round(esq)+'px'); if(dir>24) P.push('FAIXA:direita '+Math.round(dir)+'px');
 const ps=getComputedStyle(main); const lim=mr.right-parseFloat(ps.paddingRight);
 let maxr=0;[...main.children].forEach(c=>{if(vis(c)&&!c.classList.contains('demo-rod'))maxr=Math.max(maxr,c.getBoundingClientRect().right)});
 if(lim-maxr>24) P.push('FAIXA:conteúdo termina '+Math.round(lim-maxr)+'px antes da borda');}
else if(mob){const cb=getComputedStyle(mob).backgroundColor, bb=getComputedStyle(document.body).backgroundColor;
 const mr=mob.getBoundingClientRect(); if(vw-mr.width>24 && cb!==bb) P.push('FAIXA:fundo lateral '+bb+' diferente da tela '+cb);}
else if(!document.body.classList.contains('p-mob')){[...document.body.children].forEach(c=>{if(c.classList.contains('pbar')||c.classList.contains('ptoast')||c.tagName==='SCRIPT'||!vis(c))return;
 const r=c.getBoundingClientRect(); if(r.left>24||vw-r.right>24) P.push('FAIXA:bloco '+c.tagName.toLowerCase()+' com '+Math.round(r.left)+'/'+Math.round(vw-r.right)+'px livres');});}
// 3. sobreposição de textos e controles (caixas de linha reais, fora de camadas posicionadas de propósito)
const clip=el=>{let r={l:-1e9,r:1e9,t:-1e9,b:1e9},a=el;while(a&&a!==document.documentElement){const s=getComputedStyle(a);if(s.overflowX!=='visible'||s.overflowY!=='visible'){const q=a.getBoundingClientRect();r={l:Math.max(r.l,q.left),r:Math.min(r.r,q.right),t:Math.max(r.t,q.top),b:Math.min(r.b,q.bottom)};}a=a.parentElement;}return r};
const caixas=[];const tw=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;
while(n=tw.nextNode()){const el=n.parentElement; if(!n.textContent.trim()||!el||el.closest('svg,.pbar,.ptoast,script,style')||!vis(el)||sobreposto(el))continue;
 const rg=document.createRange();rg.selectNodeContents(n);const k=clip(el);[...rg.getClientRects()].forEach(r=>{const bx={el,l:Math.max(r.left,k.l),r:Math.min(r.right,k.r),t:Math.max(r.top+r.height*.22,k.t),b:Math.min(r.bottom-r.height*.22,k.b),tx:n.textContent.trim().slice(0,24)};if(bx.r-bx.l>2&&bx.b-bx.t>2)caixas.push(bx)});}
document.querySelectorAll('.in,.btn,.chip,.pill,input,select,textarea').forEach(el=>{if(!vis(el)||el.closest('svg,.pbar')||sobreposto(el))return;const r=el.getBoundingClientRect();caixas.push({el,l:r.left+1,r:r.right-1,t:r.top+1,b:r.bottom-1,tx:'['+(el.className||el.tagName)+']',ctl:1})});
let nsob=0;for(let a=0;a<caixas.length&&nsob<8;a++)for(let b=a+1;b<caixas.length;b++){const A=caixas[a],B=caixas[b];
 if(A.el===B.el||A.el.contains(B.el)||B.el.contains(A.el))continue; const w=Math.min(A.r,B.r)-Math.max(A.l,B.l), h=Math.min(A.b,B.b)-Math.max(A.t,B.t);
 if(w>3&&h>3){P.push('SOBREPOSTO:"'+A.tx+'" x "'+B.tx+'"');nsob++;break;}}
// 4. campos na mesma linha: rótulos e caixas alinhados
const grupos=new Map();document.querySelectorAll('.campo').forEach(c=>{if(!vis(c))return;const k=c.parentElement;if(!grupos.has(k))grupos.set(k,[]);grupos.get(k).push(c)});
grupos.forEach(cs=>{const linhas={};cs.forEach(c=>{const t=Math.round(c.getBoundingClientRect().top/6);(linhas[t]=linhas[t]||[]).push(c)});
 Object.values(linhas).forEach(l=>{if(l.length<2)return;const ins=l.map(c=>c.querySelector('.in')).filter(Boolean).map(x=>x.getBoundingClientRect().top);
  const lb=l.map(c=>c.querySelector('label')).filter(Boolean).map(x=>x.getBoundingClientRect().height);
  if(ins.length>1&&Math.max(...ins)-Math.min(...ins)>2)P.push('DESALINHADO:caixas com '+Math.round(Math.max(...ins)-Math.min(...ins))+'px de diferença ('+l.map(c=>c.querySelector('label')?.textContent.trim().slice(0,14)).join(' | ')+')');
  if(lb.length>1&&Math.max(...lb)-Math.min(...lb)>2)P.push('DESALINHADO:rótulos de alturas diferentes ('+l.map(c=>c.querySelector('label')?.textContent.trim().slice(0,14)).join(' | ')+')');});});
// 5. texto cortado (reticências ou overflow escondido) e elementos fora da tela
document.querySelectorAll('body *').forEach(e=>{if(e.closest('svg,.pbar')||!vis(e))return;const s=getComputedStyle(e);
 const direto=[...e.childNodes].some(x=>x.nodeType===3&&x.textContent.trim());
 if(direto&&e.scrollWidth>e.clientWidth+1&&e.clientWidth>0&&(s.textOverflow==='ellipsis'||s.overflowX==='hidden')){
   if(e.closest('table')&&e.title) P.push('TRUNCADO_INTENCIONAL:'+e.textContent.trim().slice(0,30)); else P.push('CORTADO:'+e.textContent.trim().slice(0,40));}
 const r=e.getBoundingClientRect(); const kc=e.parentElement?clip(e.parentElement):{r:1e9}; if(Math.min(r.right,kc.r)>vw+1&&r.width>0&&!rolavel(e)&&!e.closest('.side:not(.aberta)')) P.push('FORA_DA_TELA:'+e.tagName.toLowerCase()+':'+e.textContent.trim().slice(0,24));});
// 6. formulários esticados
document.querySelectorAll('.campo').forEach(c=>{if(!vis(c))return;const r=c.getBoundingClientRect();let lo=1e9,hi=-1e9;[...c.children].forEach(k=>{if(!vis(k))return;const q=k.getBoundingClientRect();lo=Math.min(lo,q.top);hi=Math.max(hi,q.bottom)});
 if(hi>lo&&r.height-(hi-lo)>24)P.push('FORM_ESTICADO:campo com '+Math.round(r.height)+'px para '+Math.round(hi-lo)+'px de conteúdo ('+(c.querySelector('label')?.textContent.trim().slice(0,16))+')');
 let n=c.nextElementSibling;while(n&&!vis(n))n=n.nextElementSibling;if(n){const q=n.getBoundingClientRect();if(q.top>=r.bottom-1&&q.left<r.right&&q.right>r.left){const g=q.top-r.bottom;if(g>48)P.push('FORM_ESTICADO:vão de '+Math.round(g)+'px depois de '+(c.querySelector('label')?.textContent.trim().slice(0,16)));}}});
new Set([...document.querySelectorAll('.campo')].map(c=>c.closest('.card,form')).filter(Boolean)).forEach(k=>{if(!vis(k))return;const r=k.getBoundingClientRect(),s=getComputedStyle(k);let hi=-1e9;
 const tw2=document.createTreeWalker(k,NodeFilter.SHOW_ELEMENT|NodeFilter.SHOW_TEXT);let e;while(e=tw2.nextNode()){let q;if(e.nodeType===3){if(!e.textContent.trim()||!vis(e.parentElement))continue;const rg=document.createRange();rg.selectNodeContents(e);q=rg.getBoundingClientRect();}else{if(!vis(e)||e.children.length)continue;q=e.getBoundingClientRect();}hi=Math.max(hi,q.bottom)}
 const sobra=r.bottom-parseFloat(s.paddingBottom)-parseFloat(s.borderBottomWidth)-hi;if(sobra<=48)return;
 const pai=k.parentElement,ps=getComputedStyle(pai);const linha=[...pai.children].filter(x=>x!==k&&vis(x)&&Math.abs(x.getBoundingClientRect().top-r.top)<4);
 if((ps.display.includes('grid')||ps.display.includes('flex'))&&linha.length&&Math.abs(Math.max(...linha.map(x=>x.getBoundingClientRect().height))-r.height)<4)P.push('CARD_IGUALADO_NA_LINHA:'+Math.round(sobra)+'px (altura da linha, campos compactos)');
 else P.push('FORM_ESTICADO:card de formulário com '+Math.round(sobra)+'px vazios no fim');});
return [...new Set(P)];}'''
GRAVES=('FORM_ESTICADO','OVERFLOW','FAIXA','SOBREPOSTO','DESALINHADO','CORTADO','FORA_DA_TELA','CORTE','FONTE<12','CONTRASTE')
async def main(alvos):
    srv=subprocess.Popen([sys.executable,'-m','http.server','8766','--bind','127.0.0.1'],cwd=SITE,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    rel={}
    try:
      async with async_playwright() as p:
        br=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w in LARG:
            os.makedirs(f'{OUT}/{w}',exist_ok=True)
            ctx=await br.new_context(viewport={'width':w,'height':900 if w>390 else 844})
            pg=await ctx.new_page()
            for q,suf in MODOS:
              for n in alvos:
                await pg.goto(f'http://127.0.0.1:8766/telas/{n}.html{q}')
                try: await pg.wait_for_load_state('networkidle',timeout=8000)
                except Exception: pass
                await pg.wait_for_timeout(150)
                final=pg.url.rsplit('/',1)[-1].split('?')[0][:-5]
                lay=await pg.evaluate(LAYOUT); ch=await pg.evaluate(CHECK)
                probs=lay+[b for b in ch['bad'] if b.startswith(('CORTE:','CORTE_CEL','FONTE<12')) and not b.startswith('FONTE<12:0:')]+['CONTRASTE:'+c for c in ch['contraste']]
                if not suf: await pg.screenshot(path=f'{OUT}/{w}/{n}.png',full_page=True)
                rel.setdefault(n,{})[f'{w}{suf}']={'aberta':final,'problemas':probs}
                g=[x for x in probs if x.startswith(GRAVES)]
                if g: print(w,suf or 'fixo',n,'->',final if final!=n else '', g[:6])
            await ctx.close()
        await br.close()
    finally: srv.terminate()
    return rel
alvos=sys.argv[1:] or sorted(os.path.basename(f)[:-5] for f in glob.glob(SITE+'/telas/[0-9]*.html'))
rel=asyncio.run(main(alvos))
if len(alvos)>=70 or not os.path.exists(OUT+'/relatorio.json'): todo=rel
else: todo=json.load(open(OUT+'/relatorio.json')); todo.update(rel)
json.dump(todo,open(OUT+'/relatorio.json','w'),ensure_ascii=False,indent=1)
with open(OUT+'/resumo.csv','w',newline='',encoding='utf-8-sig') as f:
    wr=csv.writer(f,delimiter=';'); wr.writerow(['tela','largura','aberta_como','graves','avisos','detalhe'])
    for n in sorted(todo):
        for w,v in todo[n].items():
            g=[x for x in v['problemas'] if x.startswith(GRAVES)]; a=[x for x in v['problemas'] if not x.startswith(GRAVES)]
            wr.writerow([n,w,v['aberta'],len(g),len(a),' | '.join(v['problemas'])[:900]])
tot=sum(1 for n in todo for w,v in todo[n].items() if any(x.startswith(GRAVES) for x in v['problemas']))
print('telas',len(todo),'| combinações tela x largura com problema grave:',tot,'de',sum(len(v) for v in todo.values()))
