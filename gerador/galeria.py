"""Galeria das rodadas 2 e 3: 70 telas com miniatura, perfil, resumo e caminho. Gera galeria.html (PDF via Chrome)."""
import os,base64,io
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))+'/..'
from galeria_dados import G
def thumb(n):
    im=Image.open(f'{D}/png/{n}.png').convert('RGB')
    w=360 if im.width>500 else 150
    h=int(im.height*w/im.width); im=im.resize((w,h),Image.LANCZOS)
    if h>420: im=im.crop((0,0,w,420))
    b=io.BytesIO(); im.save(b,'JPEG',quality=80); return base64.b64encode(b.getvalue()).decode()
corpo=''
for g,itens in G:
    corpo+=f'<h2 class="grupo">{g}</h2><table>'+''.join(f'''<tr><td class="n">{n[:2]}</td><td class="th"><img src="data:image/jpeg;base64,{thumb(n)}"></td><td><div class="p">{p}</div><h3>{t}</h3><p>{d}</p><a href="telas/{n}.html">telas/{n}.html</a> · <code>png/{n}.png</code></td></tr>''' for n,p,t,d in itens)+'</table>'
tot=sum(len(x) for _,x in G)
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Gio · Sistema de unidades · telas rodadas 2 e 3</title><style>
@font-face{{font-family:Poppins;src:url(assets/fonts/Poppins-SemiBold.ttf);font-weight:600}}@font-face{{font-family:Inter;src:url(assets/fonts/Inter.ttf)}}
@page{{size:A4 landscape;margin:10mm}}*{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}body{{font-family:Inter;margin:0;background:#f6f2f8;color:#1d1424}}.cap{{background:linear-gradient(120deg,#4c1455,#6f0052 55%,#b0197e);color:#fff;padding:40px 56px}}
.cap img{{height:46px}}.cap h1{{font:600 30px Poppins;margin:18px 0 6px}}.cap p{{color:#fff;margin:0;max-width:900px;line-height:1.5}}
.grupo{{font:600 22px Poppins;color:#4c1455;margin:28px 0 0;page-break-after:avoid}}
table{{width:100%;margin:8px 0 0;table-layout:fixed;border-collapse:separate;border-spacing:0 14px}}td{{background:#fff;vertical-align:top;padding:18px}}
td:first-child{{border-radius:16px 0 0 16px}}td:last-child{{border-radius:0 16px 16px 0}}tr{{page-break-inside:avoid}}
.n{{font:600 22px Poppins;color:#86106b;width:46px}}.th{{width:320px}}.th img{{border-radius:10px;border:1px solid #ece4ef;display:block;max-width:320px;max-height:300px;object-fit:cover;object-position:top}}
.p{{display:inline-block;font-size:12px;font-weight:600;color:#4c1455;background:#f1e6f3;padding:3px 10px;border-radius:20px}}h3{{font:600 18px Poppins;margin:10px 0 6px}}p{{color:#463b4e;line-height:1.55;margin:0 0 10px}}code,a{{font-size:12px;color:#86106b}}
.wrap{{padding:0 28px 28px}}
</style></head><body><div class="cap"><img src="assets/logo-gio-branco.png" alt="Gio"><h1>Sistema de unidades · telas, rodadas 2 e 3</h1><p>{tot} telas: acesso, portal da rede, portal do franqueado (computador e celular), páginas públicas nos modelos A, B e C, área do cliente (spec 002) e quiz, inteligência e tracking (spec 003). Protótipo navegável em prototipo/index.html. Ambiente de demonstração: nomes de bairro e cidade são reais; endereço, telefone, CNPJ, avaliações e pessoas são ilustrativos. Cada tela abre como HTML navegável em telas/.</p></div>
<div class="wrap">{corpo}</div></body></html>'''
open(f'{D}/galeria.html','w').write(html); print('galeria ok',tot)
