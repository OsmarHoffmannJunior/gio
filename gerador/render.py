"""Renderiza telas/*.html em png/ (1440 px; telas *mobile* em 390 px @2x) e checa por script:
overflow horizontal, texto cortado, elementos fora da borda e contraste AA (texto x fundo efetivo, degradê no pior caso).
Saída: lista por tela e relatório em png/checagem.json."""
import sys,glob,os,asyncio,json
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))+'/..'
CHECK=r'''()=>{
const W=document.documentElement.scrollWidth, cw=window.innerWidth; const bad=[]; const contraste=[]; let textos=0;
document.querySelectorAll('.mob:not(.longo) .rolagem').forEach(r=>{const rb=r.getBoundingClientRect().bottom; const tb=r.parentElement.querySelector('.tabbar'); const lim=tb?Math.min(rb,tb.getBoundingClientRect().top):rb;
 r.querySelectorAll('*').forEach(e=>{const b=e.getBoundingClientRect(); if(b.height>0 && b.bottom>lim+1 && e.children.length===0 && (e.textContent.trim()||e.tagName==='IMG')) bad.push('CORTE_CEL:'+e.textContent.trim().slice(0,30));});});
function parse(c){const m=c.match(/rgba?\(([^)]+)\)/); if(!m) return null; const p=m[1].split(',').map(x=>parseFloat(x)); return [p[0],p[1],p[2],p.length>3?p[3]:1];}
function lum(c){const f=v=>{v/=255;return v<=0.03928?v/12.92:Math.pow((v+0.055)/1.055,2.4)}; return 0.2126*f(c[0])+0.7152*f(c[1])+0.0722*f(c[2]);}
function ratio(a,b){const l1=lum(a),l2=lum(b);return (Math.max(l1,l2)+0.05)/(Math.min(l1,l2)+0.05);}
function blend(top,bot){const a=top[3];return [top[0]*a+bot[0]*(1-a),top[1]*a+bot[1]*(1-a),top[2]*a+bot[2]*(1-a),1];}
function fundos(el){ // lista de cores possíveis do fundo (degradê: todas as paradas); null se foto sem véu
  let camadas=[]; let e=el;
  while(e && e.nodeType===1){const s=getComputedStyle(e);
    const bi=s.backgroundImage;
    if(bi && bi!=='none'){ if(bi.includes('url(')){ if(!camadas.length) return null; }
      const cs=(bi.match(/rgba?\([^)]+\)/g)||[]).map(parse);
      if(cs.length){camadas.push({grad:cs}); if(cs.every(c=>c[3]>=0.99)) break;}
    }
    const bc=parse(s.backgroundColor); if(bc && bc[3]>0){camadas.push({cor:bc}); if(bc[3]>=0.99) break;}
    e=e.parentElement;}
  let bases=[[255,255,255,1]];
  for(let k=camadas.length-1;k>=0;k--){const c=camadas[k]; const cores=c.cor?[c.cor]:c.grad; const nb=[]; bases.forEach(b=>cores.forEach(cc=>nb.push(blend(cc,b)))); bases=nb;}
  return bases;}
function opac(el){let o=1,e=el;while(e&&e.nodeType===1){o*=parseFloat(getComputedStyle(e).opacity);e=e.parentElement;}return o;}
document.querySelectorAll('body *').forEach(e=>{const s=getComputedStyle(e); const r=e.getBoundingClientRect();
  if(e.children.length===0 && !e.closest('svg') && e.textContent.trim() && s.overflow!=='hidden' && s.textOverflow!=='ellipsis' && e.scrollWidth>e.clientWidth+2 && e.clientWidth>0 && s.display!=='inline') bad.push('CORTE:'+e.tagName+':'+e.textContent.trim().slice(0,40));
  if(r.right>cw+1 && r.width>0 && !(e.closest('svg'))) bad.push('FORA:'+e.tagName+'.'+(e.className.baseVal!==undefined?e.className.baseVal:e.className)+':'+e.textContent.trim().slice(0,30));
  {const c=e.parentElement&&e.parentElement.closest('.card'); if(c && r.width>0 && !e.closest('svg')){const cr=c.getBoundingClientRect(); if(r.right>cr.right+1||r.left<cr.left-1) bad.push('SAI_DO_CARD:'+e.tagName+':'+e.textContent.trim().slice(0,30));}}
  const direto=[...e.childNodes].some(n=>n.nodeType===3&&n.textContent.trim());
  if(!direto || r.width===0 || s.visibility==='hidden' || s.display==='none') return;
  if(e.closest('[data-sem-contraste]')) return;
  const isSvg=e instanceof SVGElement; let cor=parse(isSvg?(s.fill&&s.fill!=='none'?s.fill:s.color):s.color); if(!cor) return;
  const bgs=fundos(isSvg?e.closest('div,section,main,body'):e); if(!bgs) return;
  textos++;
  const o=opac(e); cor=[cor[0],cor[1],cor[2],cor[3]*o];
  const fs=parseFloat(s.fontSize), fw=parseInt(s.fontWeight)||400; const grande= fs>=24 || (fs>=18.66 && fw>=700);
  const min=grande?3:4.5; let pior=99;
  bgs.forEach(b=>{const c=cor[3]<1?blend(cor,b):cor; pior=Math.min(pior,ratio(c,b));});
  if(pior<min) contraste.push((pior).toFixed(2)+':'+fs+'px:'+e.textContent.trim().slice(0,36));
  if(fs<12 && !isSvg && !((s.textTransform==="uppercase"&&fs>=11))) bad.push('FONTE<12:'+fs+':'+e.textContent.trim().slice(0,30));
});
return {W,cw,bad:[...new Set(bad)].slice(0,20),contraste:[...new Set(contraste)].slice(0,25),textos}}'''
async def main(nomes):
    rel={}
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for f in nomes:
            n=os.path.basename(f)[:-5]
            mob='mobile' in n
            w=390 if mob else 1440
            pg=await b.new_page(viewport={'width':w,'height':844 if mob else 900},device_scale_factor=2 if mob else 1)
            await pg.goto('file://'+os.path.abspath(f)); await pg.wait_for_timeout(300)
            r=await pg.evaluate(CHECK)
            await pg.screenshot(path=f'{D}/png/{n}.png',full_page=True)
            rel[n]=r
            print(n,w,'scrollW',r['W'],'textos',r['textos'],'| problemas:',r['bad'] or 'nenhum','| contraste<AA:',r['contraste'] or 'nenhum')
            await pg.close()
        await b.close()
    old={}
    pj=f'{D}/png/checagem.json'
    if os.path.exists(pj) and len(nomes)<10: old=json.load(open(pj))
    old.update(rel); json.dump(old,open(pj,'w'),ensure_ascii=False,indent=1)
alvos=[f'{D}/telas/{a}.html' for a in sys.argv[1:]] or sorted(glob.glob(f'{D}/telas/[0-9]*.html'))
asyncio.run(main(alvos))
