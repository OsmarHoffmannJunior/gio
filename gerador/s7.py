"""Rodada 3: área do cliente (spec 002), telas 43 a 52. Dados fictícios."""
from base import *
A=DEMO['altodalapa']
def cx(txt,on=False,obrig=False,sub=''):
    return f'<label class="lin-cx" style="display:flex;gap:10px;align-items:flex-start;padding:8px 0;font-size:14px"><span class="cx{" on" if on else ""}" {"data-obrig=1" if obrig else ""} style="margin-top:2px"></span><span>{txt}{f"<span class=meta style=display:block>{sub}</span>" if sub else ""}</span></label>'
def topo_c(titulo,voltar=None,dir=''):
    v=f'<a href="{L(voltar)}" class="ib" style="width:40px;height:40px" title="Voltar">{i("chev",16,"")}</a>' if voltar else ''
    return f'<div style="display:flex;align-items:center;gap:10px;margin:4px 0 12px">{v.replace("<svg","<svg style=\"transform:rotate(180deg)\"",1) if v else ""}<h1 style="font-size:22px;font-weight:600">{titulo}</h1><span style="margin-left:auto">{dir}</span></div>'
def prog(n,t=3): return f'<div style="display:flex;gap:6px;margin:6px 0 4px">'+''.join(f'<span style="flex:1;height:6px;border-radius:6px;background:{"var(--vinho)" if k<n else "var(--lilas-200)"}"></span>' for k in range(t))+f'</div><div class="meta" style="margin-bottom:12px">Passo {n} de {t}</div>'
SELOM=f'<div style="display:flex;justify-content:center;margin:2px 0 10px">{selo()}</div>'

# ---------- 43 ENTRAR OU CRIAR CONTA (C01, C02) ----------
c=f'''<div style="text-align:center;margin:18px 0 22px"><img src="../assets/logo-gio.png" alt="Gio" style="height:44px"><h1 style="font-size:24px;font-weight:600;margin-top:18px">Entre ou crie sua conta</h1>
<p class="muted" style="margin-top:6px">Acompanhe seus agendamentos, pacotes e as ofertas da sua unidade Gio.</p></div>
{campo('E-mail ou celular','<span class="muted">nome@exemplo.com.br ou (DD) 90000-0000</span>',ic='mail')}
<a class="btn p" href="{L('c-dados')}" style="width:100%;min-height:48px;margin-top:14px">Receber código</a>
<p class="meta" style="text-align:center;margin-top:8px">Enviamos um código de 6 dígitos. Sem senha para lembrar.</p>
<div style="display:flex;align-items:center;gap:10px;margin:18px 0;color:var(--tinta-3);font-size:13px"><span style="flex:1;height:1px;background:var(--linha)"></span>ou<span style="flex:1;height:1px;background:var(--linha)"></span></div>
<a class="btn" href="{L('c-dados')}" style="width:100%;min-height:48px">{i('google',18)} Continuar com Google</a>
<a class="btn" href="{L('c-dados')}" style="width:100%;min-height:48px;margin-top:10px">{i('user',18)} Continuar com Apple</a>
<div class="card" style="padding:14px;margin-top:18px;box-shadow:none"><div style="display:flex;gap:10px"><span class="ic l">{i('shield',16)}</span><div style="font-size:13px"><b>Conta só para maiores de 18 anos.</b> Seus dados de saúde continuam com a clínica e não ficam nesta conta. <a class="lk" href="{L('c-privacidade')}">Aviso de privacidade</a></div></div></div>
<p class="meta" style="text-align:center;margin-top:16px">Trabalha numa unidade? <a class="lk" href="{L('login')}">Entrar no portal</a></p>'''
salvar(ARQ['c-entrar'],pagina('Entrar ou criar conta',mob(c,sem_tab=True,fundo='#fff'),390))

# ---------- 44 DADOS BÁSICOS (C02 confirmado + C03) ----------
c=f'''{topo_c('Criar conta','c-entrar')}{prog(2)}
<div class="aviso v" style="margin-bottom:12px;padding:10px 12px"><div>{i('check',16)}</div><div style="font-size:13px">Código confirmado para be•••@exemplo.com.br</div></div>
<div class="g" style="gap:12px">{campo('Nome','Beatriz Demonstração',ic='user')}
<div class="g" style="grid-template-columns:1fr 1fr;gap:10px">{campo('Cidade','São Paulo/SP',aj='Sugerida pela localização',ic='pin')}{campo('Nascimento','00/00/0000',aj='Só maiores de 18',ic='cal')}</div></div>
<div class="sep"></div>
{cx('Li e aceito os <a class="lk" href="#termos">Termos de uso</a>',obrig=True)}{cx('Li o <a class="lk" href="'+L('c-privacidade')+'">Aviso de privacidade</a>',obrig=True)}
<div class="meta" style="font-weight:600;margin-top:8px">Quero receber ofertas por (opcional)</div>
<div style="display:flex;gap:16px;flex-wrap:wrap">{cx('E-mail')}{cx('WhatsApp')}{cx('Notificação')}</div>
<a class="btn off" data-libera="1" data-href="{L('c-interesses')}" style="width:100%;min-height:48px;margin-top:12px">Criar conta</a>
<p class="meta" style="text-align:center;margin-top:6px">Aceite os termos e o aviso para continuar. Ofertas você liga e desliga quando quiser.</p>'''
salvar(ARQ['c-dados'],pagina('Dados básicos',mob(c,sem_tab=True,fundo='#fff'),390))

# ---------- 45 ONBOARDING DE INTERESSES (C04) ----------
procs=['Depilação a laser','Limpeza de pele','Ultraformer','Peeling','Criolipólise','Microagulhamento','Toxina','Drenagem']
sel={0,1}
c=f'''{topo_c('Seus interesses','c-dados',f'<a class="lk" href="{L("c-inicio")}">Pular</a>')}{prog(3)}
<p class="muted" style="margin-bottom:10px">Assim mostramos ofertas que fazem sentido para você. Leva 20 segundos.</p>
<b>O que você quer cuidar?</b><div style="display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 16px">'''+''.join(f'<span class="chip{" on" if k in sel else ""}" data-toggle="1">{i("check",13) if k in sel else ""}{p}</span>' for k,p in enumerate(procs))+f'''</div>
<b>Unidade preferida</b><div class="card" style="padding:0;overflow:hidden;margin:10px 0 16px;box-shadow:none"><div style="height:110px;overflow:hidden">{mapa_osm('altodalapa',358,110)}</div>
<div style="padding:12px;display:flex;align-items:center;gap:10px"><span class="ic l">{i('pin',16)}</span><div style="flex:1"><b>GiO Alto da Lapa</b><div class="meta">1,2 km · aberta até 20h · nota 4,8</div></div><span class="pill v">{i('check',11)} preferida</span></div></div>
<b>Como conheceu a Gio?</b><div style="display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 0">'''+''.join(f'<span class="chip{" on" if k==1 else ""}" data-toggle="1">{t}</span>' for k,t in enumerate(['Google','Instagram','Indicação','Passando na rua']))+f'''</div>
<p class="meta" style="margin-top:6px">{OSM_CRED}</p>
<a class="btn p" href="{L('c-inicio')}" style="width:100%;min-height:48px;margin-top:10px">Salvar e começar</a>'''
salvar(ARQ['c-interesses'],pagina('Seus interesses',mob(c,sem_tab=True,fundo='#fff'),390))

# ---------- 46 INÍCIO DO CLIENTE (C05) ----------
def card_ag(compacto=False):
    return f'''<div class="card" style="padding:16px;background:var(--grad);color:#fff;border:0">
 <div style="display:flex;align-items:center;gap:8px"><span style="font:600 12px Inter;text-transform:uppercase;letter-spacing:.06em">Próximo · daqui a 8 dias</span><span class="pill v" style="margin-left:auto;background:#fff">confirmado</span></div>
 <div style="font:600 20px Poppins;margin-top:8px">Sáb, 29/11 às 10:30</div><div style="font-size:14px">Avaliação gratuita · Depilação a laser</div><div style="font-size:13px;margin-top:2px">GiO Alto da Lapa · Rua Demonstração, 100</div>
 <div style="display:flex;gap:8px;margin-top:12px"><span class="btn s" style="background:#fff;color:var(--vinho);border:0">{i('cal',13)} Pôr na agenda</span><a class="btn s" href="{L('c-horarios')}" style="background:transparent;color:#fff;border-color:rgba(255,255,255,.7)">Remarcar</a></div>
 <div style="font-size:12px;margin-top:8px">Sem custo até 24 h antes.</div></div>'''
def card_pac():
    return f'''<div class="card" style="padding:16px;box-shadow:none"><div style="display:flex;align-items:center"><b>Depilação a laser · axilas</b><a class="lk" href="{L('c-pacote')}" style="margin-left:auto;font-size:13px">Ver</a></div>
 <div style="display:flex;align-items:end;gap:6px;margin-top:6px"><span style="font:600 26px Poppins;color:var(--vinho);line-height:1">4</span><span class="muted" style="font-size:13px">de 10 sessões feitas</span></div>
 <div style="height:8px;border-radius:8px;background:var(--lilas-100);margin:8px 0 6px;overflow:hidden"><i style="display:block;width:40%;height:100%;background:var(--grad)"></i></div><div class="meta">6 restantes · próxima sugerida em 06/12</div>
 <a class="btn p" href="{L('c-horarios')}" style="width:100%;min-height:44px;margin-top:10px">Agendar a 5ª sessão</a></div>'''
OF=[('trat-laser.jpg','Avaliação gratuita de laser','Promoção da rede · até 30/11','Você marcou depilação no quiz.'),('trat-ultrassom.jpg','Semana do Ultraformer','GiO Alto da Lapa · 01 a 07/12','Oferta da sua unidade preferida.')]
def ofertas_mini():
    return '<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">'+''.join(f'<a class="card" href="{L("c-ofertas")}" style="padding:0;overflow:hidden;box-shadow:none;display:flex;flex-direction:column"><div style="height:76px;background:url(../assets/fotos/{f}) center/cover"></div><div style="padding:10px;flex:1"><b style="font-size:13px;display:block;line-height:1.3">{t}</b><span class="meta">{s}</span></div><div class="porque" style="padding:8px 10px;font-size:12px"><b>Por que estou vendo isso?</b> {w}</div></a>' for f,t,s,w in OF)+'</div>'
c=f'''<div style="display:flex;align-items:center;margin:2px 0 6px"><h1 style="font-size:24px;font-weight:600">Olá, Beatriz</h1><a class="ib" href="{L('c-avisos-d')}" style="margin-left:auto" title="Avisos">{i('bell',18)}<span class="dot"></span></a></div>
<div class="meta" style="display:flex;align-items:center;gap:6px;margin-bottom:12px">{i('pin',13)} GiO Alto da Lapa · aberta até 20h · <a class="lk" href="{L('c-unidade-d')}">Trocar</a></div>
<div class="card" style="padding:12px 14px;box-shadow:none;border:1px solid #f1d6e6;background:#fdf0f6;display:flex;align-items:center;gap:10px;margin-bottom:12px"><span class="ic a">{i('star',16)}</span><div style="flex:1"><b style="font-size:14px">Como foi a sessão de 18/11?</b><div class="meta">Nota de 0 a 10, leva 30 segundos</div></div><a class="btn s p" href="{L('c-avaliar-d')}">Avaliar</a></div>
{card_ag()}<div style="height:12px"></div>
<div style="display:flex;align-items:center;margin-bottom:8px"><b>Meu pacote</b></div>{card_pac()}
<div style="display:flex;align-items:center;margin:14px 0 8px"><b>Ofertas para você</b><a class="lk" href="{L('c-ofertas')}" style="margin-left:auto;font-size:13px">Ver todas</a></div>{ofertas_mini()}
<div class="card" style="padding:12px 14px;margin-top:12px;display:flex;align-items:center;gap:10px;box-shadow:none"><span class="ic l">{i('sparkle',16)}</span><div style="flex:1"><b style="font-size:14px">Qual tratamento combina com você?</b><div class="meta">6 perguntas, sem perguntas de saúde</div></div><a class="btn s" href="{L('q-perg')}">Começar</a></div>
<a class="card" href="{L('c-perfil')}" style="padding:12px 14px;margin-top:10px;display:flex;align-items:center;gap:10px;box-shadow:none"><span class="ic a">{i('user',16)}</span><div style="flex:1"><b style="font-size:14px">Complete seu perfil</b><div class="meta">70% · faltam interesses e telefone</div></div>{i('chev',16)}</a>'''
salvar(ARQ['c-inicio'],pagina('Início do cliente',mob(c,0,longo=True),390))

# ---------- 47 OFERTAS PARA VOCÊ (C06) ----------
ofs=[('trat-laser.jpg','Avaliação gratuita de laser','Promoção da rede','Válida até 30/11 · todas as unidades de SP','Agendar avaliação','Você marcou depilação no quiz "Qual tratamento combina com você?" em 12/11 e tem consentimento de personalização ligado.'),
     ('trat-limpeza.jpg','Limpeza de pele de verão','GiO Alto da Lapa','Condição especial no pacote de 3 sessões · até 15/12','Ver condição','Oferta da sua unidade preferida para quem marcou "pele" nos interesses em 12/11.'),
     ('trat-ultrassom.jpg','Semana do Ultraformer','GiO Alto da Lapa','Avaliação gratuita e horário estendido · 01 a 07/12','Agendar avaliação','Oferta da sua unidade preferida, aberta a todas as clientes vinculadas. Não usa suas respostas.')]
c=f'''{topo_c('Ofertas para você')}
<div style="display:flex;gap:8px;overflow:hidden;margin-bottom:12px">'''+''.join(f'<span class="chip{" on" if k==0 else ""}" data-toggle="1">{t}</span>' for k,t in enumerate(['Todas 3','Laser','Pele','Corpo']))+f'''</div>
<div style="display:flex;flex-direction:column;gap:12px">'''+''.join(f'''<div class="card" style="padding:0;overflow:hidden;box-shadow:none"><div style="display:flex"><div style="width:104px;flex:none;background:url(../assets/fotos/{f}) center/cover"></div><div style="padding:12px;flex:1;min-width:0"><span class="pill {"l" if "rede" in o else "b"}">{o}</span><b style="display:block;margin-top:6px;line-height:1.3">{t}</b><div class="meta" style="margin-top:2px">{d}</div><a class="btn s p" href="{L('c-horarios')}" style="margin-top:8px">{cta}</a></div></div>
<div class="porque" style="padding:10px 12px"><b>{i("help",13)} Por que estou vendo isso?</b><div class="muted" style="margin-top:2px">{ex} <a class="lk" href="{L("c-privacidade")}">Gerenciar</a></div></div></div>''' for f,t,o,d,cta,ex in ofs)+'''</div>'''
salvar(ARQ['c-ofertas'],pagina('Ofertas para você',mob(c,1,longo=True),390))

# ---------- 48 AGENDAR: HORÁRIOS (C10) ----------
dias=[('seg','24'),('ter','25'),('qua','26'),('qui','27'),('sex','28'),('sáb','29'),('dom','30')]
slots=[('09:00',0),('09:30',1),('10:00',0),('10:30',2),('11:00',1),('11:30',1),('14:00',1),('14:30',0),('15:00',1),('16:30',1),('17:00',1),('18:30',1)]
c=f'''{topo_c('Escolha o horário','c-ofertas')}
<div class="card" style="padding:12px 14px;box-shadow:none;display:flex;gap:10px;align-items:center"><span class="ic l">{i('sparkle',16)}</span><div style="flex:1"><b style="font-size:14px">Avaliação gratuita · Depilação a laser</b><div class="meta">30 min · GiO Alto da Lapa</div></div><a class="lk" href="{L('c-ofertas')}" style="font-size:13px">Trocar</a></div>
<div style="display:flex;align-items:center;margin:14px 0 8px"><b>Novembro 2026</b></div>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:6px">'''+''.join(f'<span style="text-align:center;border-radius:12px;padding:8px 0;border:1px solid {"var(--vinho)" if d=="29" else "var(--linha)"};background:{"var(--vinho)" if d=="29" else ("#f1ecf3" if n=="dom" else "#fff")};color:{"#fff" if d=="29" else ("var(--tinta-3)" if n=="dom" else "var(--tinta)")}"><span style="display:block;font-size:12px">{n}</span><b style="font-size:16px">{d}</b></span>' for n,d in dias)+f'''</div>
<div class="meta" style="margin:6px 0 12px">Domingo fechado. Horários reais da agenda da unidade.</div>
<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">'''+''.join(f'<span style="text-align:center;padding:10px 0;border-radius:10px;font-weight:600;font-size:14px;border:1px solid {"var(--vinho)" if s==2 else "var(--linha-forte)"};background:{"var(--vinho)" if s==2 else ("#f1ecf3" if s==0 else "#fff")};color:{"#fff" if s==2 else ("var(--tinta-3)" if s==0 else "var(--tinta)")};{"text-decoration:line-through" if s==0 else ""}" data-toggle="{1 if s else 0}">{h}</span>' for h,s in slots)+f'''</div>
<div class="aviso l" style="margin-top:14px;padding:10px 12px"><div>{i('clock',16)}</div><div style="font-size:13px">O horário fica reservado por 10 minutos. Remarque ou cancele sem custo até 24 h antes.</div></div>
<a class="btn p" href="{L('c-confirma')}" style="width:100%;min-height:48px;margin-top:12px">Confirmar sáb, 29/11 às 10:30</a>'''
salvar(ARQ['c-horarios'],pagina('Agendar: horários',mob(c,2),390))

# ---------- 49 AGENDAR: CONFIRMAÇÃO (C11) ----------
c=f'''<div style="text-align:center;margin:12px 0 14px"><div style="width:72px;height:72px;border-radius:50%;background:var(--verde-50);color:var(--verde);display:grid;place-items:center;margin:0 auto">{i('check',36)}</div>
<h1 style="font-size:22px;font-weight:600;margin-top:12px">Agendamento confirmado</h1><p class="muted">A unidade confirmou na agenda. Lembramos você 1 dia antes.</p></div>
<div class="card" style="padding:14px;box-shadow:none"><div class="lista-i" style="font-size:14px">
<div class="it" style="padding:8px 0">{i('cal',16)}<div><b>Sábado, 29/11 às 10:30</b><div class="meta">30 min</div></div></div>
<div class="it" style="padding:8px 0">{i('sparkle',16)}<div><b>Avaliação gratuita</b><div class="meta">Depilação a laser</div></div></div>
<div class="it" style="padding:8px 0">{i('pin',16)}<div><b>GiO Alto da Lapa</b><div class="meta">Rua Demonstração, 100 · Alto da Lapa</div></div></div></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px"><span class="btn" style="min-height:44px">{i('cal',15)} Pôr na agenda</span><span class="btn" style="min-height:44px">{i('map',15)} Como chegar</span></div>
<div class="card" style="padding:14px;margin-top:10px;box-shadow:none"><b style="font-size:14px">Antes da avaliação</b><ul class="muted" style="font-size:13px;margin:6px 0 0 18px"><li>Chegue 10 minutos antes.</li><li>Evite sol forte na região nos 7 dias anteriores.</li></ul></div>
<a class="btn p" href="{L('c-inicio')}" style="width:100%;min-height:48px;margin-top:12px">Ir para o início</a>'''
salvar(ARQ['c-confirma'],pagina('Agendamento confirmado',mob(c,2),390))

# ---------- 50 DETALHE DO PACOTE (C14, C15) ----------
ses=[('3ª','21/10','feita'),('4ª','18/11','feita'),('5ª','06/12','sugerida')]
c=f'''{topo_c('Meu pacote','c-inicio')}
<div class="card" style="padding:16px;box-shadow:none"><b style="font-size:16px">Depilação a laser · axilas</b><div class="meta">GiO Alto da Lapa · comprado em 12/08/2026</div>
<div style="display:flex;align-items:end;gap:8px;margin-top:12px"><span style="font:600 30px Poppins;color:var(--vinho)">4</span><span class="muted" style="margin-bottom:6px">de 10 sessões feitas</span><span class="pill v" style="margin-left:auto;margin-bottom:6px">ativo</span></div>
<div style="height:8px;border-radius:8px;background:var(--lilas-100);margin:6px 0;overflow:hidden"><i style="display:block;width:40%;height:100%;background:var(--grad)"></i></div><div class="meta">6 restantes · válido até 12/2027 · intervalo de 30 a 45 dias</div></div>
<b style="display:block;margin:14px 0 6px">Sessões</b><div class="meta" style="margin-bottom:6px">1ª e 2ª realizadas em 12/08 e 16/09</div>
<div class="card" style="padding:4px 14px;box-shadow:none"><div class="lista-i">'''+''.join(f'<div class="it" style="padding:9px 0"><span class="ic {"v" if s=="feita" else "a"}" style="width:30px;height:30px">{i("check" if s=="feita" else "clock",14)}</span><div style="flex:1"><b style="font-size:14px">{n} sessão</b><div class="meta">{d} · {"realizada" if s=="feita" else "data sugerida"}</div></div>{"<span class=meta>GiO Alto da Lapa</span>" if s=="feita" else "<span class=\"pill a\">próxima</span>"}</div>' for n,d,s in ses)+f'''</div></div>
<a class="btn p" href="{L('c-horarios')}" style="width:100%;min-height:48px;margin-top:12px">Agendar a 5ª sessão</a>
<p class="meta" style="margin-top:8px">O consumo das sessões vem da agenda da unidade. Vendido por GiO Alto da Lapa · CNPJ {CNPJ_DEMO}. <a class="lk" href="#regulamento">Regulamento</a></p>'''
salvar(ARQ['c-pacote'],pagina('Meu pacote',mob(c,3),390))

# ---------- 51 PRIVACIDADE (C23 + respostas de quiz) ----------
cons=[('Termos de uso','versão 3 · aceito em 12/11/2026',None),('Aviso de privacidade','versão 4 · lido em 12/11/2026',None),('Ofertas por e-mail','ligado em 12/11/2026',True),('Ofertas por WhatsApp','desligado',False),('Personalização','usa suas respostas de quiz e interesses',True)]
c=f'''{topo_c('Privacidade','c-inicio')}
<p class="muted" style="font-size:13px;margin-bottom:10px">A Rede Gio é a controladora dos seus dados; a unidade vê só o necessário.</p>
<div class="card" style="padding:4px 14px;box-shadow:none"><div class="lista-i">'''+''.join(f'<div class="it" style="padding:10px 0"><div style="flex:1"><b style="font-size:14px">{t}</b><div class="meta">{d}</div></div>{"<span class=\"pill z\">obrigatório</span>" if on is None else f"<span class=\"tog{" on" if on else ""}\" data-toggle=\"1\" role=\"switch\"></span>"}</div>' for t,d,on in cons)+f'''</div></div>
<div class="card" style="padding:14px;margin-top:10px;box-shadow:none"><div style="display:flex;align-items:center;gap:10px"><span class="ic l">{i('list',16)}</span><div style="flex:1"><b style="font-size:14px">Minhas respostas de quiz</b><div class="meta">1 quiz · respondido em 12/11/2026</div></div></div>
<div style="display:flex;gap:8px;margin-top:10px"><a class="btn s" href="{L('q-res')}">Ver respostas</a><span class="btn s perigo" data-confirma="Apagar suas respostas de quiz?">Apagar</span></div></div>
<div class="card" style="padding:4px 14px;margin-top:10px;box-shadow:none"><div class="lista-i">
<div class="it" style="padding:10px 0">{i('down',16)}<b style="flex:1;font-size:14px">Baixar meus dados</b>{i('chev',14)}</div>
<div class="it" style="padding:10px 0">{i('edit',16)}<b style="flex:1;font-size:14px">Corrigir meus dados</b>{i('chev',14)}</div>
<div class="it" style="padding:10px 0;color:var(--vermelho)">{i('x',16)}<b style="flex:1;font-size:14px">Excluir minha conta</b>{i('chev',14)}</div></div></div>
<div class="meta" style="margin-top:10px">Pedido de cópia dos dados de 14/11: <b style="color:var(--verde)">concluído</b> em 2 dias.</div>'''
salvar(ARQ['c-privacidade'],pagina('Privacidade',mob(c,4),390))

# 52 (início do cliente no computador) passou para s10.py com o casco de aplicativo.
