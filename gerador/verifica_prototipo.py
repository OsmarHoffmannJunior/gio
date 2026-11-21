"""Verifica o protótipo: links quebrados, telas alcançáveis, erros no navegador, transbordo em 390, interações e prints 390/1440."""
import os, re, glob, json, asyncio, subprocess, time, urllib.parse
from playwright.async_api import async_playwright
D=os.path.dirname(os.path.abspath(__file__))+'/..'; P=f'{D}/prototipo'; V=f'{D}/prototipo-verificacao'
os.makedirs(f'{V}/390',exist_ok=True); os.makedirs(f'{V}/1440',exist_ok=True)
pags=sorted(glob.glob(f'{P}/**/*.html',recursive=True))
quebrados=[]; grafo={}
for f in pags:
    s=open(f,encoding='utf-8').read(); base=os.path.dirname(f); rel=os.path.relpath(f,P); grafo[rel]=set()
    refs=re.findall(r'(?:href|src)="([^"]+)"',s)+re.findall(r'url\(([^)#][^)]*)\)',s)
    for r in refs:
        r=r.strip('\'"')
        if r.startswith(('#','data:','http:','https:','mailto:','tel:','javascript:')): continue
        alvo=os.path.normpath(os.path.join(P if r.startswith('/') else base,urllib.parse.unquote(r.split('#')[0].split('?')[0]).lstrip('/')))
        if not os.path.exists(alvo): quebrados.append((rel,r))
        elif alvo.endswith('.html'): grafo[rel].add(os.path.relpath(alvo,P))
# alcançáveis a partir do índice (inclui links do seletor de perfil injetado pelo proto.js)
extra={'telas/04-admin-dashboard-rede.html','telas/24-franqueado-dashboard.html','telas/46-cliente-mobile-inicio.html','telas/52-cliente-inicio-desktop.html','index.html'}
vis=set(); fila=['index.html']
while fila:
    x=fila.pop()
    if x in vis: continue
    vis.add(x); fila+=list(grafo.get(x,()))+([e for e in extra] if x.startswith('telas/') else [])
inalc=[p for p in grafo if p not in vis and p!='404.html']
PRINTS=['index','01-login','04-admin-dashboard-rede','05-admin-unidades-tabela','07-admin-unidade-detalhe','10-admin-leads-kanban','17-admin-auditoria','24-franqueado-dashboard','25-franqueado-minha-unidade','31-franqueado-dominio',
 '39-landing-b-desktop','43-cliente-mobile-entrar','46-cliente-mobile-inicio','47-cliente-mobile-ofertas','48-cliente-mobile-agendar-horarios','52-cliente-inicio-desktop','53-franqueado-procedimentos-precos','55-franqueado-campanhas','57-franqueado-tags-medicao',
 '58-admin-controles-liberacoes','59-admin-mural-aviso','60-admin-campanha-rede','61-admin-campanhas-aprovacao','62-admin-performance-campanhas','63-admin-quiz-gerador','64-quiz-mobile-pergunta','66-admin-inteligencia-demanda','68-admin-tracking-dicionario','70-admin-tracking-saude']
async def main():
    srv=subprocess.Popen(['python3','-m','http.server','8765','--bind','127.0.0.1'],cwd=P,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
    U='http://127.0.0.1:8765/'; erros=[]; transb=[]; testes=[]
    try:
      async with async_playwright() as p:
        b=await p.chromium.launch(executable_path='/usr/bin/google-chrome',args=['--no-sandbox'])
        for w in (1440,390):
            ctx=await b.new_context(viewport={'width':w,'height':900 if w>400 else 844},device_scale_factor=1 if w>400 else 2,accept_downloads=True)
            for f in pags:
                rel=os.path.relpath(f,P)
                if rel=='404.html': continue
                pg=await ctx.new_page(); falhas=[]
                pg.on('console',lambda m,falhas=falhas: falhas.append('console:'+m.text) if m.type=='error' else None)
                pg.on('pageerror',lambda e,falhas=falhas: falhas.append('js:'+str(e)))
                pg.on('response',lambda r,falhas=falhas: falhas.append(f'{r.status}:{r.url}') if r.status>=400 else None)
                await pg.goto(U+rel); await pg.wait_for_timeout(150)
                if falhas: erros.append((w,rel,falhas[:3]))
                if w==390:
                    sw=await pg.evaluate('document.documentElement.scrollWidth')
                    if sw>392: transb.append((rel,sw))
                n=os.path.basename(rel)[:-5]
                if n in PRINTS: await pg.screenshot(path=f'{V}/{w}/{n}.png',full_page=True)
                await pg.close()
            # interações
            pg=await ctx.new_page()
            await pg.goto(U+'telas/04-admin-dashboard-rede.html'); await pg.click('.pbar a[data-p=franqueado]'); await pg.wait_for_load_state()
            testes.append((w,'troca de perfil rede > franqueado', pg.url.endswith('24-franqueado-dashboard.html')))
            await pg.click('.pbar a[data-p=cliente]'); await pg.wait_for_load_state()
            testes.append((w,'troca de perfil para cliente', ('52-cliente' if w>400 else '46-cliente') in pg.url))
            await pg.goto(U+'telas/44-cliente-mobile-dados.html')
            antes=await pg.get_attribute('[data-libera]','href')
            for c in await pg.query_selector_all('[data-obrig]'): await c.click()
            depois=await pg.get_attribute('[data-libera]','href')
            testes.append((w,'consentimento desmarcado libera o botão só depois dos obrigatórios', antes is None and depois=='45-cliente-mobile-interesses.html'))
            await pg.goto(U+'telas/17-admin-auditoria.html'); await pg.click('#aud-tipos [data-tipo="Permissão"]')
            vis_=await pg.evaluate("Array.from(document.querySelectorAll('#aud-tab tbody tr')).filter(t=>t.style.display!=='none').length")
            testes.append((w,'auditoria: filtro por tipo Permissão mostra 2', vis_==2))
            await pg.click('#aud-tab tbody tr:visible >> nth=0')
            det=await pg.inner_text('#aud-det'); testes.append((w,'auditoria: detalhe com antes e depois', 'ANTES' in det.upper() and 'DEPOIS' in det.upper()))
            async with pg.expect_download() as dl: await pg.click('#aud-csv')
            d=await dl.value; cam=f'{V}/auditoria-{w}.csv'; await d.save_as(cam); linhas=open(cam,encoding='utf-8-sig').read().strip().split('\n')
            testes.append((w,'auditoria: CSV com cabeçalho + 2 linhas filtradas', len(linhas)==3))
            await pg.goto(U+'telas/05-admin-unidades-tabela.html'); await pg.click('.side a[href="58-admin-controles-liberacoes.html"]', timeout=3000) if w>400 else None
            if w>400: testes.append((w,'menu lateral leva a Controles da rede', pg.url.endswith('58-admin-controles-liberacoes.html')))
            if w==390:
                await pg.goto(U+'telas/39-landing-b-desktop.html'); await pg.wait_for_timeout(400)
                testes.append((w,'landing de computador abre a versão de celular em 390', pg.url.endswith('40-landing-b-mobile.html')))
                await pg.goto(U+'telas/04-admin-dashboard-rede.html'); await pg.click('.pbar .pmenu'); vis2=await pg.is_visible('.side')
                testes.append((w,'botão Menu abre a navegação lateral em 390', vis2))
            await pg.goto(U+'telas/07-admin-unidade-detalhe.html'); await pg.click('.btn.p >> nth=0'); t=await pg.inner_text('.ptoast')
            testes.append((w,'botão sem tela própria mostra ação simulada', 'simulada' in t))
            await pg.close(); await ctx.close()
        await b.close()
    finally: srv.terminate()
    r=dict(paginas=len(pags),links_quebrados=quebrados,inalcancaveis=inalc,erros_navegador=erros,transbordo_390=transb,testes=testes)
    json.dump(r,open(f'{V}/relatorio.json','w'),ensure_ascii=False,indent=1)
    print('páginas',len(pags),'| links quebrados',len(quebrados),'| inalcançáveis',inalc,'| erros no navegador',len(erros),'| transbordo em 390',len(transb))
    for e in erros[:10]: print(' erro',e)
    for t in transb[:20]: print(' transbordo',t)
    for t in testes: print(' teste',t)
    for q in quebrados[:10]: print(' quebrado',q)
asyncio.run(main())
