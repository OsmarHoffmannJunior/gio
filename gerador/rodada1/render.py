"""Renderiza telas/*.html em png/ com Chromium (Playwright) e checa overflow horizontal e texto cortado."""
import sys,glob,os,asyncio
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))+'/..'
MOBILE={'17-mobile-leads','18-mobile-lead','20-landing-publica-mobile'}
CHECK='''()=>{const W=document.documentElement.scrollWidth, cw=window.innerWidth; const bad=[];
document.querySelectorAll('body *').forEach(e=>{const s=getComputedStyle(e); if(e.children.length===0 && e.textContent.trim() && s.overflow!=='hidden' && s.textOverflow!=='ellipsis' && e.scrollWidth>e.clientWidth+2 && e.clientWidth>0 && s.display!=='inline') bad.push(e.tagName+':'+e.textContent.trim().slice(0,40)); const r=e.getBoundingClientRect(); if(r.right>cw+1 && r.width>0) bad.push('FORA:'+e.tagName+'.'+e.className+':'+e.textContent.trim().slice(0,30));});
return {W,cw,bad:bad.slice(0,15)}}'''
async def main(nomes):
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for f in nomes:
            n=os.path.basename(f)[:-5]
            w=390 if n in MOBILE else 1440
            pg=await b.new_page(viewport={'width':w,'height':844 if w<500 else 900},device_scale_factor=1 if w>500 else 2)
            await pg.goto('file://'+os.path.abspath(f)); await pg.wait_for_timeout(250)
            r=await pg.evaluate(CHECK)
            await pg.screenshot(path=f'{D}/png/{n}.png',full_page=True)
            print(n,w,'scrollW',r['W'],'| problemas:',r['bad'] if r['bad'] else 'nenhum')
            await pg.close()
        await b.close()
alvos=[f'{D}/telas/{a}.html' for a in sys.argv[1:]] or sorted(glob.glob(f'{D}/telas/*.html'))
asyncio.run(main(alvos))
