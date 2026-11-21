"""Rodada 3b: área do cliente no computador com casco de aplicativo (crítica da tela 52), telas 52 e 71 a 78,
e perfil no celular (79). Mesmos destinos e rótulos do celular. Dados fictícios."""
from base import *
A=DEMO['altodalapa']
RAIL=[('home','Início','c-inicio-d'),('tag','Ofertas','c-ofertas-d'),('cal','Agendar','c-agendar-d'),('grid','Pacotes','c-pacote-d'),('user','Perfil','c-perfil-d')]
TOPNAV=[('Início','c-inicio-d'),('Agendar','c-agendar-d'),('Pacotes','c-pacote-d'),('Ofertas','c-ofertas-d')]
def cli(ativo,miolo,titulo):
    top=f'''<header class="cli-top"><a class="marca" href="{L('c-inicio-d')}"><img src="../assets/logo-gio.png" alt="Gio, ir para o início"><span>Minha conta</span></a>
<nav aria-label="Conta">'''+''.join(f'<a href="{L(k)}" class="{"on" if k==ativo else ""}">{t}</a>' for t,k in TOPNAV)+f'''</nav>
<div class="dir">{selo()}<a class="ib" href="{L('c-avisos-d')}" title="Avisos">{i('bell',18)}<span class="dot"></span></a>
<details class="cli-menu"><summary><span class="av-s" style="width:36px;height:36px">BD</span><b>Beatriz</b>{i('chevd',14)}</summary><div class="pop">
<a href="{L('c-perfil-d')}">{i('user',16)} Perfil</a><a href="{L('c-privacidade-d')}">{i('lock',16)} Privacidade</a><a href="{L('lpB')}">{i('globe',16)} Ver o site da unidade</a><a href="{L('c-entrar')}">{i('x',16)} Sair</a></div></details></div></header>'''
    rail='<aside class="cli-rail" aria-label="Área do cliente">'+''.join(f'<a href="{L(k)}" class="{"on" if k==ativo else ""}"{" aria-current=page" if k==ativo else ""}>{i(ic,18)}{t}</a>' for ic,t,k in RAIL)+f'''
<div class="rod"><b style="color:var(--tinta);display:block">GiO Alto da Lapa</b>aberta até 20h<br><a class="lk" href="{L('c-unidade-d')}">Trocar unidade</a></div></aside>'''
    tab='<nav class="cli-tab">'+''.join(f'<a href="{L(k)}" class="{"on" if k==ativo else ""}">{i(ic,22)}<span>{t}</span></a>' for ic,t,k in RAIL)+'</nav>'
    corpo=f'{top}<div class="cli-app">{rail}<main class="cli-main"><div class="miolo">{miolo}<div class="demo-rod">{i("eye",13)} {SELO_TXT}</div></div></main></div>{tab}'
    return pagina(titulo,corpo)
def h(t,p='',dir=''): return f'<div class="cab"><div><h1>{t}</h1>{f"<p>{p}</p>" if p else ""}</div><div class="dir">{dir}</div></div>'
WHY={'laser':f'Você marcou depilação no quiz "Qual tratamento combina com você?" em 12/11 e tem consentimento de personalização ligado.',
     'limpeza':'Oferta da sua unidade preferida para quem marcou "pele" nos interesses em 12/11.',
     'ultra':'Oferta da sua unidade preferida, aberta a todas as clientes vinculadas. Não usa suas respostas.'}
OFS=[('laser','trat-laser.jpg','Avaliação gratuita de laser','Promoção da rede','Válida até 30/11 · unidades de SP','Agendar avaliação'),
     ('limpeza','trat-limpeza.jpg','Limpeza de pele de verão','GiO Alto da Lapa','3 sessões com condição especial · até 15/12','Ver condição'),
     ('ultra','trat-ultrassom.jpg','Semana do Ultraformer','GiO Alto da Lapa','Avaliação gratuita e horário estendido · 01 a 07/12','Agendar avaliação')]
def destino(k,cta): return f"{L('c-ofertas-d')}#{k}" if cta=='Ver condição' else f"{L('c-agendar-d')}?proc={k}"
def card_oferta(k,f,t,o,d,cta,alto=130):
    return f'''<div class="card" id="{k}" style="padding:0;overflow:hidden;box-shadow:none;display:flex;flex-direction:column"><a href="{destino(k,cta)}" style="display:block;height:{alto}px;background:url(../assets/fotos/{f}) center/cover" aria-label="{t}"></a>
<div style="padding:14px;flex:1"><span class="pill {"l" if "rede" in o else "b"}">{o}</span><b style="display:block;margin-top:8px;font-size:16px">{t}</b><div class="meta" style="line-height:1.45">{d}</div>
<a class="btn s p" href="{destino(k,cta)}" style="margin-top:10px">{cta}</a></div>
<div class="porque"><b>{i("help",13)} Por que estou vendo isso?</b><div class="muted" style="margin-top:2px">{WHY[k]} <a class="lk" href="{L('c-privacidade-d')}">Gerenciar</a></div></div></div>'''
GRADE3='grid-template-columns:repeat(auto-fit,minmax(max(260px,calc((100% - 32px)/3)),1fr))'
# ---------- 52 INÍCIO ----------
nota=''.join(f'<a href="{L("c-avaliar-d")}?nota={n}" aria-label="Nota {n}">{n}</a>' for n in range(11))
m=f'''<div class="cab" style="align-items:center"><div><h1>Olá, Beatriz</h1><p>Sábado, 21 de novembro</p></div>
<div class="dir"><div class="card" style="padding:8px 8px 8px 14px;box-shadow:none;display:flex;align-items:center;gap:12px"><span class="ic l">{i('pin',16)}</span><div><b style="font-size:14px">Sua unidade: GiO Alto da Lapa</b><div class="meta">aberta até 20h · 1,2 km · nota 4,8</div></div>
<a class="btn s" href="{L('c-unidade-d')}">Trocar unidade</a><span class="btn s">{i('phone',13)} Ligar</span></div></div></div>
<div class="card" style="box-shadow:none;border:1px solid #f1d6e6;background:linear-gradient(120deg,#fff 0%,#fdf0f6 100%);display:flex;align-items:center;gap:18px;flex-wrap:wrap;margin-bottom:16px">
<span class="ic a" style="width:44px;height:44px">{i('star',20)}</span><div style="flex:1;min-width:260px"><b style="font-size:16px">Como foi a sessão de depilação a laser de 18/11?</b><div class="meta">De 0 a 10, quanto você recomendaria a GiO Alto da Lapa? Leva 30 segundos.</div></div>
<div class="notas" role="group" aria-label="Nota de 0 a 10">{nota}</div><a class="btn p" href="{L('c-avaliar-d')}">Avaliar sessão</a></div>
<div class="g" style="grid-template-columns:minmax(420px,1.6fr) minmax(280px,1fr);margin-bottom:22px">
<div class="card" style="padding:20px;background:var(--grad);color:#fff;border:0">
 <div style="display:flex;align-items:center;gap:8px"><span style="font:600 12px Inter;text-transform:uppercase;letter-spacing:.06em">Próximo agendamento · daqui a 8 dias</span><span class="pill v" style="margin-left:auto;background:#fff">confirmado</span></div>
 <div style="font:600 26px Poppins;margin-top:10px">Sáb, 29/11 às 10:30</div><div style="font-size:15px">Avaliação gratuita · Depilação a laser · 30 min</div><div style="font-size:14px;margin-top:2px">GiO Alto da Lapa · Rua Demonstração, 100 · Alto da Lapa</div>
 <div style="display:flex;gap:8px;margin-top:14px;flex-wrap:wrap"><span class="btn" style="background:#fff;color:var(--vinho);border:0">{i('cal',14)} Pôr na agenda</span><a class="btn" href="{L('c-agendar-d')}?proc=laser" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.7)">Remarcar</a><span class="btn" data-confirma="Cancelar a avaliação de 29/11?" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.7)">Cancelar</span></div>
 <div style="font-size:12px;margin-top:10px">Remarque ou cancele sem custo até 24 h antes. Antes da avaliação: evite sol forte na região nos 7 dias anteriores.</div></div>
<div class="card" style="box-shadow:none;display:flex;flex-direction:column"><div class="hd" style="margin-bottom:6px"><h3>{i('grid',16)} Meu pacote</h3><a class="lk" href="{L('c-pacote-d')}" style="margin-left:auto;font-size:13px">Ver pacote</a></div>
 <div class="muted" style="font-size:14px">Depilação a laser · axilas</div>
 <div style="display:flex;align-items:end;gap:8px;margin-top:8px"><span style="font:600 30px Poppins;color:var(--vinho);line-height:1">4</span><span class="muted">de 10 sessões feitas</span></div>
 <div style="height:8px;border-radius:8px;background:var(--lilas-100);margin:10px 0 6px;overflow:hidden"><i style="display:block;width:40%;height:100%;background:var(--grad)"></i></div>
 <div class="meta">6 restantes · válido até 12/2027 · próxima sugerida em 06/12</div>
 <a class="btn p" href="{L('c-agendar-d')}?proc=pacote" style="margin-top:auto;align-self:flex-start;min-height:44px">Agendar a 5ª sessão</a></div></div>
<div style="display:flex;align-items:center;margin:0 0 10px"><h3 style="font-size:18px">Ofertas para você</h3><a class="lk" href="{L('c-ofertas-d')}" style="margin-left:auto">Ver todas as ofertas</a></div>
<div class="g" style="{GRADE3};margin-bottom:16px">'''+''.join(card_oferta(*o) for o in OFS)+f'''</div>
<div class="g" style="grid-template-columns:1fr 1fr">
<a class="card" href="{L('c-perfil-d')}" style="box-shadow:none;display:flex;align-items:center;gap:14px;padding:14px 18px"><span class="ic a">{i('user',16)}</span><div style="flex:1"><b>Complete seu perfil</b><div style="height:6px;border-radius:6px;background:var(--lilas-100);margin:6px 0 4px;overflow:hidden;max-width:260px"><i style="display:block;width:70%;height:100%;background:var(--grad)"></i></div><div class="meta">70% · faltam interesses e telefone</div></div>{i('chev',16)}</a>
<div class="card" style="box-shadow:none;display:flex;align-items:center;gap:14px;padding:14px 18px"><span class="ic l">{i('sparkle',16)}</span><div style="flex:1"><b>Qual tratamento combina com você?</b><div class="meta">6 perguntas, cerca de 1 minuto, sem perguntas de saúde</div></div><a class="btn s" href="{L('q-perg')}">Começar o quiz</a></div></div>'''
salvar(ARQ['c-inicio-d'],cli('c-inicio-d',m,'Minha conta'))
# ---------- 71 OFERTAS ----------
m=h('Ofertas para você','Promoções da rede e da sua unidade preferida. Cada oferta diz por que aparece para você.')+f'''
<div style="display:flex;gap:8px;margin-bottom:14px">'''+''.join(f'<span class="chip{" on" if k==0 else ""}" data-toggle="1">{t}</span>' for k,t in enumerate(['Todas 3','Laser','Pele','Corpo']))+f'''</div>
<div class="g" style="{GRADE3}">'''+''.join(card_oferta(*o,alto=170) for o in OFS)+'''</div>'''
salvar(ARQ['c-ofertas-d'],cli('c-ofertas-d',m,'Ofertas para você'))
# ---------- 72 AGENDAR (horários e confirmação na mesma tela) ----------
dias=[('seg','24'),('ter','25'),('qua','26'),('qui','27'),('sex','28'),('sáb','29'),('dom','30'),('seg','01'),('ter','02'),('qua','03'),('qui','04'),('sex','05'),('sáb','06'),('dom','07')]
slots=['09:00','09:30','10:00','10:30','11:00','11:30','14:00','14:30','15:00','16:30','17:00','18:30']
off={'09:00','10:00','14:30'}
m=h('Agendar','Horários reais da agenda da GiO Alto da Lapa. O horário fica reservado por 10 minutos.')+f'''
<div class="g" style="grid-template-columns:minmax(0,1.5fr) minmax(300px,1fr)">
<div class="card" style="box-shadow:none">
 <div class="campo" style="margin-bottom:14px"><label><span class="lt">Procedimento</span></label><div class="in" id="ag-proc">{i('sparkle',15)} <span>Avaliação gratuita · Depilação a laser · 30 min</span></div></div>
 <b style="display:block;margin-bottom:8px">Novembro e dezembro de 2026</b>
 <div id="ag-dias" style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px">'''+''.join(f'<span data-dia="{d}" data-acao-propria="1" style="text-align:center;border-radius:12px;padding:8px 0;border:1px solid var(--linha);background:{"#f1ecf3" if n=="dom" else "#fff"};color:{"var(--tinta-3)" if n=="dom" else "var(--tinta)"};cursor:pointer"><span style="display:block;font-size:12px">{n}</span><b style="font-size:16px">{d}</b></span>' for n,d in dias)+f'''</div>
 <div class="meta" style="margin:6px 0 12px">Domingo fechado.</div>
 <div id="ag-hor" style="display:grid;grid-template-columns:repeat(6,1fr);gap:8px">'''+''.join(f'<span data-hora="{s}" data-acao-propria="1" style="text-align:center;padding:10px 0;border-radius:10px;font-weight:600;font-size:14px;border:1px solid var(--linha-forte);background:{"#f1ecf3" if s in off else "#fff"};color:{"var(--tinta-3)" if s in off else "var(--tinta)"};{"text-decoration:line-through" if s in off else "cursor:pointer"}">{s}</span>' for s in slots)+f'''</div></div>
<div class="g" style="align-content:start">
 <div class="card" style="box-shadow:none" id="ag-resumo"><h3>Resumo</h3><div class="lista-i" style="font-size:14px;margin-top:6px">
  <div class="it">{i('cal',16)}<div><b id="ag-quando">Sáb, 29/11 às 10:30</b><div class="meta">duração conforme o procedimento</div></div></div>
  <div class="it">{i('sparkle',16)}<div><b id="ag-nome">Avaliação gratuita · Depilação a laser</b><div class="meta" id="ag-orig">da oferta da rede</div></div></div>
  <div class="it">{i('pin',16)}<div><b>GiO Alto da Lapa</b><div class="meta">Rua Demonstração, 100 · <a class="lk" href="{L('c-unidade-d')}">Trocar unidade</a></div></div></div></div>
  <span class="btn p" id="ag-ok" data-acao-propria="1" style="width:100%;min-height:48px;margin-top:12px">Confirmar horário</span>
  <div class="meta" style="margin-top:8px">Remarque ou cancele sem custo até 24 h antes.</div></div>
 <div class="card" id="ag-feito" style="box-shadow:none;display:none;border:1px solid #bfe3d2"><div style="display:flex;gap:10px;align-items:center"><span class="ic v">{i('check',16)}</span><b>Agendamento confirmado</b></div>
  <p class="muted" style="margin:6px 0 10px">A unidade confirmou na agenda. Lembramos você 1 dia antes.</p>
  <div style="display:flex;gap:8px;flex-wrap:wrap"><span class="btn p">{i('cal',14)} Pôr na agenda</span><span class="btn">{i('map',14)} Como chegar</span><a class="btn" href="{L('c-inicio-d')}">Ir para o início</a></div>
  <ul class="muted" style="font-size:13px;margin:10px 0 0 18px"><li>Chegue 10 minutos antes.</li><li>Evite sol forte na região nos 7 dias anteriores.</li></ul></div>
</div></div>
<script>(function(){{
var P={{laser:['Avaliação gratuita · Depilação a laser · 30 min','29','10:30','da oferta da rede'],limpeza:['Limpeza de pele de verão · 1ª de 3 sessões · 60 min','26','16:30','da oferta da GiO Alto da Lapa'],ultra:['Avaliação gratuita · Ultraformer · 30 min','02','15:00','da Semana do Ultraformer'],pacote:['Depilação a laser · axilas · 5ª de 10 sessões · 20 min','06','09:30','do seu pacote']}};
var q=(location.search.match(/proc=(\\w+)/)||[])[1]||'laser',p=P[q]||P.laser,dia=p[1],hora=p[2];
var sem={{'24':'Seg, 24/11','25':'Ter, 25/11','26':'Qua, 26/11','27':'Qui, 27/11','28':'Sex, 28/11','29':'Sáb, 29/11','01':'Seg, 01/12','02':'Ter, 02/12','03':'Qua, 03/12','04':'Qui, 04/12','05':'Sex, 05/12','06':'Sáb, 06/12'}};
function pinta(){{document.querySelectorAll('#ag-dias [data-dia]').forEach(function(e){{var on=e.dataset.dia===dia;e.style.background=on?'var(--vinho)':(e.textContent.indexOf('dom')===0?'#f1ecf3':'#fff');e.style.color=on?'#fff':(e.textContent.indexOf('dom')===0?'var(--tinta-3)':'var(--tinta)');e.style.borderColor=on?'var(--vinho)':'var(--linha)';}});
 document.querySelectorAll('#ag-hor [data-hora]').forEach(function(e){{if(e.style.textDecoration)return;var on=e.dataset.hora===hora;e.style.background=on?'var(--vinho)':'#fff';e.style.color=on?'#fff':'var(--tinta)';e.style.borderColor=on?'var(--vinho)':'var(--linha-forte)';}});
 document.getElementById('ag-quando').textContent=(sem[dia]||dia)+' às '+hora;}}
document.querySelector('#ag-proc span').textContent=p[0];document.getElementById('ag-nome').textContent=p[0].split(' · ').slice(0,2).join(' · ');document.getElementById('ag-orig').textContent=p[3];
document.querySelectorAll('#ag-dias [data-dia]').forEach(function(e){{if(e.textContent.indexOf('dom')!==0)e.addEventListener('click',function(){{dia=e.dataset.dia;pinta();}});}});
document.querySelectorAll('#ag-hor [data-hora]').forEach(function(e){{if(!e.style.textDecoration)e.addEventListener('click',function(){{hora=e.dataset.hora;pinta();}});}});
document.getElementById('ag-ok').addEventListener('click',function(){{document.getElementById('ag-feito').style.display='block';document.getElementById('ag-feito').scrollIntoView({{block:'nearest'}});}});
pinta();}})();</script>'''
salvar(ARQ['c-agendar-d'],cli('c-agendar-d',m,'Agendar'))
# ---------- 73 PACOTE ----------
ses=[('1ª','12/08','feita'),('2ª','16/09','feita'),('3ª','21/10','feita'),('4ª','18/11','feita'),('5ª','06/12','sugerida')]
m=h('Meu pacote','Sessões, validade e regulamento. O consumo vem da agenda da unidade.')+f'''
<div class="g" style="grid-template-columns:minmax(0,1.4fr) minmax(300px,1fr)">
<div class="card" style="box-shadow:none"><b style="font-size:18px">Depilação a laser · axilas</b><div class="meta">GiO Alto da Lapa · comprado em 12/08/2026</div>
 <div style="display:flex;align-items:end;gap:8px;margin-top:14px"><span style="font:600 32px Poppins;color:var(--vinho);line-height:1">4</span><span class="muted">de 10 sessões feitas</span><span class="pill v" style="margin-left:auto">ativo</span></div>
 <div style="height:8px;border-radius:8px;background:var(--lilas-100);margin:10px 0 6px;overflow:hidden"><i style="display:block;width:40%;height:100%;background:var(--grad)"></i></div><div class="meta">6 restantes · válido até 12/2027 · intervalo de 30 a 45 dias</div>
 <a class="btn p" href="{L('c-agendar-d')}?proc=pacote" style="margin-top:14px;min-height:48px">Agendar a 5ª sessão</a>
 <p class="meta" style="margin-top:10px">Vendido por GiO Alto da Lapa · CNPJ {CNPJ_DEMO}. <a class="lk" href="#regulamento">Regulamento</a></p></div>
<div class="card" style="box-shadow:none"><h3>Sessões</h3><div class="lista-i" style="margin-top:6px">'''+''.join(f'<div class="it" style="padding:9px 0"><span class="ic {"v" if s=="feita" else "a"}" style="width:30px;height:30px">{i("check" if s=="feita" else "clock",14)}</span><div style="flex:1"><b style="font-size:14px">{n} sessão</b><div class="meta">{d} · {"realizada" if s=="feita" else "data sugerida"}</div></div>{"<span class=meta>GiO Alto da Lapa</span>" if s=="feita" else "<span class=\"pill a\">próxima</span>"}</div>' for n,d,s in ses)+'''</div></div></div>'''
salvar(ARQ['c-pacote-d'],cli('c-pacote-d',m,'Meu pacote'))
# ---------- 74 AVALIAR SESSÃO (C20) ----------
m=h('Avaliar sessão','Sessão de depilação a laser · axilas · 18/11 · GiO Alto da Lapa')+f'''
<div class="g" style="grid-template-columns:minmax(0,1.4fr) minmax(300px,1fr)">
<div class="card" style="box-shadow:none" id="av-form"><b style="font-size:16px">De 0 a 10, quanto você recomendaria a GiO Alto da Lapa a uma amiga?</b>
 <div class="notas" id="av-notas" style="margin:12px 0 4px">'''+''.join(f'<span data-n="{n}" data-acao-propria="1">{n}</span>' for n in range(11))+f'''</div>
 <div class="meta" style="display:flex;justify-content:space-between;max-width:500px"><span>0 · nada provável</span><span>10 · muito provável</span></div>
 <b style="display:block;margin:16px 0 8px">O que marcou a sessão? (opcional)</b><div style="display:flex;gap:8px;flex-wrap:wrap">'''+''.join(f'<span class="chip" data-toggle="1">{t}</span>' for t in ['Atendimento','Pontualidade','Limpeza','Explicações','Conforto','Resultado'])+f'''</div>
 <div class="campo" style="margin-top:14px"><label><span class="lt">Comentário (opcional)</span></label><div class="in" style="min-height:88px;align-items:flex-start;color:var(--tinta-3)">Conte o que podemos manter ou melhorar. Não escreva dados de saúde.</div></div>
 <span class="btn p" id="av-env" data-acao-propria="1" style="margin-top:14px;min-height:48px">Enviar avaliação</span></div>
<div class="g" style="align-content:start">
 <div class="card" style="box-shadow:none"><h3>{i('google',16)} Avaliar também no Google</h3><p class="muted" style="margin:6px 0 10px">Opcional, mostrado para qualquer nota. Não damos brinde nem desconto por avaliação.</p><span class="btn s">Abrir o perfil da unidade no Google</span></div>
 <div class="card" id="av-ok" style="box-shadow:none;display:none;border:1px solid #bfe3d2"><div style="display:flex;gap:10px;align-items:center"><span class="ic v">{i('check',16)}</span><b>Obrigada, Beatriz</b></div><p class="muted" style="margin-top:6px">Sua avaliação foi para a unidade. Se a nota for até 6, a equipe entra em contato em até 2 dias úteis.</p><a class="btn s" href="{L('c-inicio-d')}" style="margin-top:10px">Voltar ao início</a></div>
</div></div>
<script>(function(){{var n=(location.search.match(/nota=(\\d+)/)||[])[1];function marca(v){{document.querySelectorAll('#av-notas [data-n]').forEach(function(e){{e.classList.toggle('on',e.dataset.n===v)}});}}
if(n)marca(n);document.querySelectorAll('#av-notas [data-n]').forEach(function(e){{e.addEventListener('click',function(){{marca(e.dataset.n)}})}});
document.getElementById('av-env').addEventListener('click',function(){{document.getElementById('av-ok').style.display='block';}});}})();</script>'''
salvar(ARQ['c-avaliar-d'],cli('c-inicio-d',m,'Avaliar sessão'))
# ---------- 75 PRIVACIDADE ----------
cons=[('Termos de uso','versão 3 · aceito em 12/11/2026',None),('Aviso de privacidade','versão 4 · lido em 12/11/2026',None),('Ofertas por e-mail','ligado em 12/11/2026',True),('Ofertas por WhatsApp','desligado',False),('Personalização','usa suas respostas de quiz e interesses',True)]
m=h('Privacidade','A Rede Gio é a controladora dos seus dados; a unidade vê só o necessário.',f'<a class="btn" href="{L("c-perfil-d")}">Voltar ao perfil</a>')+f'''
<div class="g" style="grid-template-columns:minmax(0,1.3fr) minmax(300px,1fr)">
<div class="card" style="box-shadow:none"><h3>Consentimentos</h3><div class="lista-i" style="margin-top:6px">'''+''.join(f'<div class="it" style="padding:10px 0"><div style="flex:1"><b style="font-size:14px">{t}</b><div class="meta">{d}</div></div>{"<span class=\"pill z\">obrigatório</span>" if on is None else f"<span class=\"tog{" on" if on else ""}\" data-toggle=\"1\" role=\"switch\"></span>"}</div>' for t,d,on in cons)+f'''</div></div>
<div class="g" style="align-content:start">
<div class="card" style="box-shadow:none"><div style="display:flex;align-items:center;gap:10px"><span class="ic l">{i('list',16)}</span><div style="flex:1"><b style="font-size:14px">Minhas respostas de quiz</b><div class="meta">1 quiz · respondido em 12/11/2026</div></div></div>
<div style="display:flex;gap:8px;margin-top:10px"><a class="btn s" href="{L('q-res')}">Ver respostas</a><span class="btn s perigo" data-confirma="Apagar suas respostas de quiz?">Apagar</span></div></div>
<div class="card" style="box-shadow:none"><div class="lista-i">
<div class="it" style="padding:10px 0">{i('down',16)}<b style="flex:1;font-size:14px">Baixar meus dados</b>{i('chev',14)}</div>
<div class="it" style="padding:10px 0">{i('edit',16)}<b style="flex:1;font-size:14px">Corrigir meus dados</b>{i('chev',14)}</div>
<div class="it" style="padding:10px 0;color:var(--vermelho)">{i('x',16)}<b style="flex:1;font-size:14px">Excluir minha conta</b>{i('chev',14)}</div></div>
<div class="meta" style="margin-top:8px">Pedido de cópia dos dados de 14/11: <b style="color:var(--verde)">concluído</b> em 2 dias.</div></div></div></div>'''
salvar(ARQ['c-privacidade-d'],cli('c-perfil-d',m,'Privacidade'))
# ---------- 76 PERFIL ----------
m=h('Perfil','Seus dados, sua unidade preferida, seus interesses e como prefere receber avisos.',f'<span class="btn p">{i("check",14)} Salvar</span>')+f'''
<div class="g" style="grid-template-columns:minmax(0,1.4fr) minmax(300px,1fr)">
<div class="g" style="align-content:start">
<div class="card" style="box-shadow:none"><h3>Dados pessoais</h3><div class="g" style="grid-template-columns:1fr 1fr;margin-top:12px">
{campo('Nome','Beatriz Demonstração',ic='user')}{campo('Como prefere ser chamada','Beatriz')}{campo('E-mail','beatriz@exemplo.com.br','L',aj='Verificado em 12/11. Para trocar, confirme o novo e-mail.',ic='mail')}{campo('Celular','Adicionar celular',aj='Opcional. Falta para completar o perfil.',ic='phone')}</div></div>
<div class="card" style="box-shadow:none"><h3>Interesses</h3><p class="meta" style="margin:4px 0 10px">Usados só para personalizar ofertas, se a personalização estiver ligada.</p><div style="display:flex;gap:8px;flex-wrap:wrap">'''+''.join(f'<span class="chip{" on" if s else ""}" data-toggle="1">{t}</span>' for t,s in [('Depilação a laser',1),('Limpeza de pele',1),('Ultraformer',0),('Peeling',0),('Microagulhamento',0),('Criolipólise',0)])+f'''</div></div></div>
<div class="g" style="align-content:start">
<div class="card" style="box-shadow:none"><h3>{i('pin',16)} Unidade preferida</h3><b style="display:block;margin-top:8px">GiO Alto da Lapa</b><div class="meta">Rua Demonstração, 100 · aberta até 20h · nota 4,8</div><a class="btn s" href="{L('c-unidade-d')}" style="margin-top:10px">Trocar unidade</a></div>
<div class="card" style="box-shadow:none"><h3>{i('bell',16)} Avisos</h3><div class="lista-i" style="margin-top:6px">'''+''.join(f'<div class="it" style="padding:8px 0"><b style="flex:1;font-size:14px">{t}</b><span class="tog{" on" if s else ""}" data-toggle="1" role="switch"></span></div>' for t,s in [('Lembrete de sessão',1),('Sessão lançada no pacote',1),('Pedido de avaliação',1)])+f'''</div><div class="meta" style="margin-top:6px">Ofertas por e-mail e WhatsApp ficam em Privacidade.</div></div>
<div class="card" style="box-shadow:none;padding:6px 16px"><div class="lista-i"><a class="it" href="{L('c-privacidade-d')}" style="padding:10px 0">{i('lock',16)}<b style="flex:1;font-size:14px">Privacidade e consentimentos</b>{i('chev',14)}</a><a class="it" href="{L('c-entrar')}" style="padding:10px 0">{i('x',16)}<b style="flex:1;font-size:14px">Sair</b>{i('chev',14)}</a></div></div>
</div></div>'''
salvar(ARQ['c-perfil-d'],cli('c-perfil-d',m,'Perfil'))
# ---------- 77 SELETOR DE UNIDADE ----------
uns=[('GiO Alto da Lapa','Rua Demonstração, 100 · Alto da Lapa','1,2 km','aberta até 20h','4,8',True),('GiO Perdizes','Rua Demonstração, 410 · Perdizes','2,9 km','aberta até 21h','4,7',False),('GiO Pompeia','Rua Demonstração, 77 · Pompeia','3,4 km','aberta até 20h','4,9',False),('GiO Vila Leopoldina','Rua Demonstração, 15 · Vila Leopoldina','3,8 km','fecha às 19h','4,6',False)]
m=h('Escolher unidade preferida','A unidade preferida aparece no início, nas ofertas e no agendamento. Você pode agendar em qualquer unidade.',f'<a class="btn" href="{L("c-inicio-d")}">Cancelar</a>')+f'''
<div class="g" style="grid-template-columns:minmax(0,1fr) minmax(0,1.2fr)">
<div class="card" style="box-shadow:none;padding:6px 16px"><div class="lista-i">'''+''.join(f'<div class="it" style="padding:12px 0;gap:12px"><span class="ic {"v" if s else "l"}">{i("pin",16)}</span><div style="flex:1"><b>{n}</b><div class="meta">{e}</div><div class="meta">{d} · {hh} · nota {nt}</div></div>{"<span class=\"pill v\">preferida</span>" if s else f"<a class=\"btn s\" href=\"{L("c-inicio-d")}\">Escolher</a>"}</div>' for n,e,d,hh,nt,s in uns)+f'''</div></div>
<div class="card" style="padding:0;overflow:hidden;box-shadow:none;position:relative">{mapa_osm('altodalapa',720,460,raio=140)}<span class="credito" style="position:absolute;right:10px;bottom:8px;background:rgba(255,255,255,.9);padding:2px 8px;border-radius:6px">{OSM_CRED}</span></div></div>'''
salvar(ARQ['c-unidade-d'],cli('c-inicio-d',m,'Escolher unidade'))
# ---------- 78 AVISOS ----------
avs=[('star','a','Como foi a sessão de 18/11?','Avalie de 0 a 10 · pedido hoje às 09:00','c-avaliar-d',True),('cal','l','Lembrete: avaliação no sábado, 29/11 às 10:30','GiO Alto da Lapa · enviaremos outro lembrete 1 dia antes','c-agendar-d',True),('check','v','Sessão de 18/11 registrada no seu pacote','4 de 10 sessões feitas','c-pacote-d',False),('tag','b','Nova oferta: Semana do Ultraformer','01 a 07/12 na sua unidade preferida','c-ofertas-d',False),('down','z','Cópia dos seus dados pronta','pedido de 14/11, concluído em 2 dias','c-privacidade-d',False)]
m=h('Avisos','A mesma lista do sino, no computador e no celular.',f'<span class="btn">Marcar todos como lidos</span>')+'''
<div class="card" style="box-shadow:none;padding:6px 18px;max-width:880px"><div class="lista-i">'''+''.join(f'<a class="it" href="{L(k)}" style="padding:12px 0;gap:12px;{"font-weight:600" if novo else ""}"><span class="ic {c}">{i(ic,16)}</span><div style="flex:1"><b>{t}</b><div class="meta">{d}</div></div>{"<span class=\"pill b\">novo</span>" if novo else ""}{i("chev",14)}</a>' for ic,c,t,d,k,novo in avs)+'</div></div>'
salvar(ARQ['c-avisos-d'],cli('c-inicio-d',m,'Avisos'))
# ---------- 79 PERFIL NO CELULAR ----------
def topo_m(t,v): return f'<div style="display:flex;align-items:center;gap:10px;margin:4px 0 12px"><a href="{L(v)}" class="ib" style="width:40px;height:40px" title="Voltar"><svg class="i" viewBox="0 0 24 24" style="width:16px;height:16px;transform:rotate(180deg)">{IC["chev"]}</svg></a><h1 style="font-size:22px;font-weight:600">{t}</h1></div>'
c=f'''{topo_m('Perfil','c-inicio')}
<div class="card" style="padding:14px;box-shadow:none;display:flex;gap:12px;align-items:center"><span class="av-s" style="width:48px;height:48px;font-size:16px">BD</span><div style="flex:1"><b>Beatriz Demonstração</b><div class="meta">beatriz@exemplo.com.br</div></div></div>
<a class="card" href="{L('c-perfil-d')}" style="padding:12px 14px;margin-top:10px;display:flex;align-items:center;gap:10px;box-shadow:none"><span class="ic a">{i('user',16)}</span><div style="flex:1"><b style="font-size:14px">Complete seu perfil</b><div class="meta">70% · faltam interesses e telefone</div></div>{i('chev',16)}</a>
<div class="card" style="padding:4px 14px;margin-top:10px;box-shadow:none"><div class="lista-i">
<a class="it" href="{L('c-unidade-d')}" style="padding:11px 0">{i('pin',16)}<div style="flex:1"><b style="font-size:14px">Unidade preferida</b><div class="meta">GiO Alto da Lapa · aberta até 20h</div></div>{i('chev',14)}</a>
<a class="it" href="{L('c-avisos-d')}" style="padding:11px 0">{i('bell',16)}<div style="flex:1"><b style="font-size:14px">Avisos</b><div class="meta">2 novos</div></div>{i('chev',14)}</a>
<a class="it" href="{L('c-perfil-d')}" style="padding:11px 0">{i('sparkle',16)}<div style="flex:1"><b style="font-size:14px">Interesses</b><div class="meta">Depilação a laser, limpeza de pele</div></div>{i('chev',14)}</a>
<a class="it" href="{L('c-privacidade')}" style="padding:11px 0">{i('lock',16)}<div style="flex:1"><b style="font-size:14px">Privacidade e consentimentos</b><div class="meta">ofertas, personalização, seus dados</div></div>{i('chev',14)}</a>
<a class="it" href="{L('c-entrar')}" style="padding:11px 0">{i('x',16)}<b style="flex:1;font-size:14px">Sair</b>{i('chev',14)}</a></div></div>'''
salvar(ARQ['c-perfil'],pagina('Perfil',mob(c,4),390))
print('s10 ok')
