"""Rodada 3: quiz, inteligência e tracking (spec 003), telas 63 a 70. Dados fictícios."""
from base import *
def R(ativo,c): return app('admin',ativo,c)
TABS_INT=[('Demanda','intel'),('Sazonalidade e clima','sazon'),('Quiz','quiz'),('Fontes de dados',None)]
TABS_TR=[('Saúde do tracking','saude'),('Dicionário de eventos','dic'),('Links e UTMs','utm'),('Destinos',None),('Consentimento',None)]
TOT_EV=sum(v for _,_,v in EV)

# ---------- 63 GERADOR DE QUIZ (Q11 + Q12) ----------
nos=[('P1','Qual região você quer cuidar primeiro?',0,30),('P2','Qual é o seu objetivo?',0,140),('P3a','Frequência de depilação',0,260),('P3b','Como está sua pele hoje?',0,260),('P4','Quando quer começar?',0,370),('R','Resultado e unidade mais próxima',0,470)]
def grafo():
    W={'P3a':196,'P3b':196}; X={'P1':70,'P2':70,'P3a':0,'P3b':224,'P4':70,'R':70}
    o=['<svg viewBox="0 0 420 540" width="100%" height="540" style="display:block">']
    arestas=[('P1','P2',''),('P2','P3a','se "pelos"'),('P2','P3b','se "pele"'),('P3a','P4',''),('P3b','P4',''),('P4','R','')]
    pos={k:(X[k],y,W.get(k,280)) for k,_,x,y in nos}
    for a_,b_,t in arestas:
        x1,y1,w1=pos[a_]; x2,y2,w2=pos[b_]; cx1=x1+w1/2; cx2=x2+w2/2
        o.append(f'<path d="M{cx1},{y1+56} C{cx1},{y1+80} {cx2},{y2-24} {cx2},{y2}" fill="none" stroke="#b9a6c2" stroke-width="2"/>')
        if t: o.append(f'<text x="{cx2}" y="{y2-10}" text-anchor="middle" font-size="12" fill="#5E5566" font-family="Inter">{t}</text>')
    for k,t,x,y in nos:
        x,_,w=pos[k]; sel=k=='P2'; cor='#6f0052' if sel else ('#0B7A54' if k=='R' else '#5E5566')
        lim=38 if w>200 else 24
        tt=t if len(t)<=lim else t[:lim-1]+'…'
        o.append(f'<rect x="{x}" y="{y}" width="{w}" height="56" rx="12" fill="{"#fbf3f8" if sel else "#fff"}" stroke="{cor if sel or k=="R" else "#cdbfd3"}" stroke-width="{2 if sel else 1.4}"/><text x="{x+14}" y="{y+22}" font-size="12" font-weight="700" fill="{cor}" font-family="Inter">{k}</text><text x="{x+14}" y="{y+42}" font-size="13" fill="#1d1424" font-family="Inter">{tt}</text>')
    o.append('</svg>'); return ''.join(o)
c=f'<div class="migalha"><a href="{L("intel")}">Demanda e quiz</a>{i("chev",12)}<span>Qual tratamento combina com você?</span><span class="pill z" style="margin-left:8px">modelo da rede · rascunho v3</span></div>'+cabec('Gerador de quiz','Monte o fluxo de perguntas. Fase 1: só estética e preferência, sem perguntas de saúde.',f'<a class="btn" href="{L("q-perg")}">{i("phone2",14)} Testar no celular</a><span class="btn p">{i("send",14)} Enviar para aprovação</span>')+tabs([('Fluxo','quiz'),('Regras de recomendação',None),('Textos de resultado',None),('Publicar e distribuir',None),('Resultados','intel')],0)+f'''
<div class="g" style="grid-template-columns:200px 1fr 400px;align-items:start">
<div class="card" style="padding:12px"><div class="meta" style="font-weight:600;margin-bottom:8px">PERGUNTAS</div>'''+''.join(f'<div style="display:flex;gap:8px;align-items:center;padding:8px;border-radius:10px;{"background:var(--lilas-100);font-weight:600" if k=="P2" else ""}">{i("drag",14)}<span class="trunc" style="font-size:13px">{k} · {t}</span></div>' for k,t,x,y in nos[:-1])+f'''<span class="btn s" style="margin-top:10px;width:100%" data-sem-rota="1">{i("plus",12)} Pergunta</span>
<div class="aviso v" style="margin-top:12px;padding:10px"><div>{i('check',14)}</div><div style="font-size:12px">Sem ciclos e sem caminho sem fim.</div></div></div>
<div class="card" style="padding:12px 16px">{grafo()}</div>
<div class="card"><div class="hd"><h3>Pergunta P2</h3><span class="pill l" style="margin-left:auto">escolha única</span></div><div class="g" style="gap:12px">
{campo('Texto da pergunta','Qual é o seu objetivo?',ic='edit')}
<div class="campo"><label>Opções e pontos</label>'''+''.join(f'<div style="display:flex;gap:8px;align-items:center;padding:8px 0;border-bottom:1px dashed var(--linha);font-size:13px">{i("drag",13)}<span style="flex:1">{o}</span><span class="pill l">{p}</span></div>' for o,p in [('Reduzir pelos','Laser +3'),('Pele mais uniforme','Limpeza +2 · Peeling +2'),('Firmeza do rosto','Ultraformer +3'),('Gordura localizada','Criolipólise +3')])+f'''</div>
<div class="campo"><label>Nova opção (teste do validador)</label><div class="in err">Tenho alergia ou doença de pele</div><div class="erro">Termo de saúde bloqueado na fase 1 ("alergia", "doença"). Use perguntas de preferência.</div></div>
<div style="display:flex;gap:16px;font-size:13px;align-items:center"><span style="display:flex;gap:8px;align-items:center"><span class="tog on" data-toggle="1"></span>Obrigatória</span><span style="display:flex;gap:8px;align-items:center"><span class="tog on" data-toggle="1"></span>Imagem nas opções</span></div></div></div></div>'''
salvar(ARQ['quiz'],pagina('Gerador de quiz',R('intel',c)))

# ---------- 64 QUIZ NO CELULAR: PERGUNTA (Q02) ----------
op=[('trat-laser.jpg','Reduzir pelos',True),('trat-limpeza.jpg','Pele mais uniforme',False),('trat-ultrassom.jpg','Firmeza do rosto',False),('trat-micro.jpg','Textura e marcas',False)]
cq=f'''<div style="display:flex;align-items:center;gap:10px;margin:4px 0 8px"><a class="ib" href="{L('c-inicio')}" title="Voltar">{i('x',16)}</a><div style="flex:1"><div style="height:6px;border-radius:6px;background:var(--lilas-200);overflow:hidden"><i style="display:block;width:33%;height:100%;background:var(--vinho)"></i></div></div><span class="meta">2 de 6</span></div>
<div class="meta" style="margin-top:10px">Qual tratamento combina com você?</div><h1 style="font-size:24px;font-weight:600;line-height:1.25;margin:4px 0 16px">Qual é o seu objetivo principal?</h1>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">'''+''.join(f'<a class="card" href="{L("q-res")}" style="padding:0;overflow:hidden;box-shadow:none;border:2px solid {"var(--vinho)" if s else "var(--linha)"}"><div style="height:118px;background:url(../assets/fotos/{f}) center/cover"></div><div style="padding:12px;display:flex;gap:8px;align-items:center"><b style="font-size:14px;flex:1;line-height:1.3">{t}</b>{"<span class=\"ic\" style=\"width:24px;height:24px;background:var(--vinho);color:#fff;border-radius:50%\">"+i("check",13)+"</span>" if s else ""}</div></a>' for f,t,s in op)+f'''</div>
<div style="display:flex;gap:10px;margin-top:16px"><a class="btn" href="{L('c-inicio')}" style="flex:1;min-height:48px">Voltar</a><a class="btn p" href="{L('q-res')}" style="flex:2;min-height:48px">Próxima</a></div>
<p class="meta" style="text-align:center;margin-top:12px">Sem perguntas de saúde. Respostas anônimas até você decidir salvar o resultado.</p>'''
salvar(ARQ['q-perg'],pagina('Quiz: pergunta',mob(cq,sem_tab=True,fundo='#fff'),390))

# ---------- 65 QUIZ NO CELULAR: RESULTADO (Q03) ----------
cr=f'''<div style="text-align:center;margin:6px 0 12px"><div class="meta">Seu resultado</div><h1 style="font-size:24px;font-weight:600;line-height:1.25;margin-top:4px">Combina com você</h1></div>
<div class="card" style="padding:0;overflow:hidden;box-shadow:none;border:2px solid var(--vinho)"><div style="height:120px;background:url(../assets/fotos/trat-laser.jpg) center/cover"></div><div style="padding:14px"><span class="pill l">1ª sugestão</span><b style="display:block;font-size:18px;margin-top:6px">Depilação a laser</b><div class="muted" style="font-size:13px;margin-top:2px">Para reduzir pelos com sessões a cada 30 a 45 dias. A avaliação gratuita define o plano.</div></div></div>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px">'''+''.join(f'<div class="card" style="padding:12px;box-shadow:none"><span class="meta">{n}ª sugestão</span><b style="display:block;font-size:14px">{t}</b></div>' for n,t in [(2,'Limpeza de pele'),(3,'Peeling')])+f'''</div>
<div class="card" style="padding:12px 14px;margin-top:10px;box-shadow:none;display:flex;gap:10px;align-items:center"><span class="ic l">{i('pin',16)}</span><div style="flex:1"><b style="font-size:14px">GiO Alto da Lapa</b><div class="meta">1,2 km · aberta até 20h</div></div></div>
<a class="btn p" href="{L('c-horarios')}" style="width:100%;min-height:48px;margin-top:12px">Agendar avaliação gratuita</a>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px"><a class="btn" href="{L('c-ofertas')}" style="min-height:44px">Ver ofertas</a><a class="btn" href="{L('c-entrar')}" style="min-height:44px">Salvar resultado</a></div>
<p class="meta" style="margin-top:10px">Para salvar, você cria uma conta. O uso das respostas para personalizar ofertas depende do seu consentimento, que começa desmarcado.</p>'''
salvar(ARQ['q-res'],pagina('Quiz: resultado',mob(cr,sem_tab=True,fundo='#fff'),390))

# ---------- 66 INTELIGÊNCIA: DEMANDA (I01 + I05) ----------
fontes=['Quiz','Catálogo','Agenda','Busca','Trends']
idx={'Depilação a laser':[100,100,100,100,100],'Limpeza de pele':[61,72,58,66,54],'Ultraformer':[37,41,22,48,61],'Peeling':[29,33,26,31,27],'Criolipólise':[21,30,18,39,44],'Microagulhamento':[16,24,14,22,19]}
c=cabec('Demanda e quiz','O que os clientes mais procuram, por fonte. Toda recomendação mostra fonte, regra e amostra.',periodo())+tabs(TABS_INT,0)+f'''
<div style="display:flex;gap:8px;margin-bottom:14px">'''+''.join(f'<span class="chip">{t} {i("chevd",12)}</span>' for t in ['UF: todas','Cidade: todas','Faixa etária: todas','Unidade: todas'])+f'''</div>
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">
{kpi('sparkle','Quizzes começados',fmt(QZ_INI),'mesmo número do evento quiz_iniciado')}
{kpi('check','Quizzes concluídos',fmt(QZ_FIM),f'{QZ_PCT}% de conclusão')}
{kpi('user','Salvaram com conta',fmt(QZ_CONTA),f'{round(QZ_CONTA/QZ_FIM*100)}% dos concluídos')}
{kpi('users','Contas novas no período',fmt(CLI_NOVOS),f'base total {fmt(CLI_REDE)} clientes')}</div>
<div class="g" style="grid-template-columns:1fr 1fr;align-items:start">
<div class="card"><div class="hd"><h3>Procedimento mais indicado no quiz</h3><span class="meta" style="margin-left:auto">{fmt(QZ_FIM)} resultados</span></div>{barras_h(QZ_DEM,w=520,larg_rot=150,fmt=fmt)}
<div class="sep"></div><div class="hd" style="margin-bottom:6px"><h3>Índice por fonte</h3><span class="meta" style="margin-left:auto">laser = 100 em cada fonte</span></div>
<table class="t" style="font-size:13px" id="t-idx"><thead><tr><th>Procedimento</th>'''+''.join(f'<th class="num">{f.split(" ")[0]}</th>' for f in fontes)+'</tr></thead><tbody>'+''.join(f'<tr><td><b>{p}</b></td>'+''.join(f'<td class="num">{v}</td>' for v in vs)+'</tr>' for p,vs in idx.items())+f'''</tbody></table>
<div class="meta" style="margin-top:8px">Busca = Search Console. Fontes pagas desligadas (decisão de 21/11). Trends por exportação manual mensal.</div></div>
<div class="card"><div class="hd"><h3>{i('sparkle',16)} Recomendações</h3><span class="pill l" style="margin-left:auto">3 novas</span></div><div class="g" style="gap:12px">'''+''.join(f'''<div style="border:1px solid var(--linha);border-radius:12px;padding:14px"><div style="display:flex;gap:8px;align-items:center"><b style="flex:1">{t}</b><span class="pill {cl}">{tp}</span></div><p class="muted" style="font-size:13px;margin:4px 0 8px">{d}</p><div class="meta">Fonte: {f} · Regra: {r} · Amostra: {a}</div><div style="display:flex;gap:8px;margin-top:10px"><a class="btn s p" href="{L(l1)}">{b1}</a><a class="btn s" href="{L(l2)}">{b2}</a></div></div>''' for t,tp,cl,d,f,r,a,l1,b1,l2,b2 in [
 ('Laser em alta no Sul antes do verão','sazonal_clima','a','Quiz e agendamentos de laser subiram 24% na Regional Sul em 4 semanas, como nos últimos 2 anos.','quiz, agendamentos, INMET','alta acima de 20% em 4 semanas','1.146 respostas','camp-rede','Criar campanha','perf','Replicar campanha'),
 ('Ultraformer procurado e pouco agendado','demanda_quiz','l','Ultraformer aparece em 14% dos resultados, mas só 6% dos agendamentos.','quiz, agendamentos','diferença acima de 5 pontos','4.512 resultados','camp-rede','Criar campanha','quiz','Ver quiz'),
 ('Campinas com poucos clientes por mil habitantes','penetracao_baixa','b','Cambuí tem metade da média de clientes por mil mulheres de 20 a 49 anos das unidades de SP.','clientes, IBGE','abaixo de 50% da mediana','1 unidade','controles','Ver liberações','perf','Comparar')])+'''</div></div></div>'''
salvar(ARQ['intel'],pagina('Demanda e quiz',R('intel',c),extra_css='#t-idx td,#t-idx th{padding-left:7px;padding-right:7px}'))

# ---------- 67 SAZONALIDADE E CLIMA (I02 + I04) ----------
meses=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']
laser=[52,48,61,74,88,96,100,94,83,70,58,50]; temp=[31,31,30,28,26,25,25,26,27,28,29,30]
c=cabec('Demanda e quiz','Sazonalidade da demanda por procedimento, cruzada com clima e calendário comercial.',f'<span class="chip">Cidade: São Paulo {i("chevd",12)}</span><span class="chip">Procedimento: Depilação a laser {i("chevd",12)}</span>')+tabs(TABS_INT,1)+f'''
<div class="g" style="grid-template-columns:1fr 380px;align-items:start">
<div class="card"><div class="hd"><h3>Demanda de laser x temperatura máxima média</h3><span class="leg" style="margin-left:auto"><span><i style="background:#b0197e"></i>Demanda (índice, pico = 100)</span><span><i style="background:#2C5BC4"></i>Temperatura (°C, normal)</span></span></div>
{area([laser,[t*3 for t in temp]],['#b0197e','#2C5BC4'],w=700,h=260,labels=meses,ymax=110)}
<div class="meta">A demanda por laser sobe no inverno (junho e julho) para chegar pronta ao verão. A linha azul usa a temperatura vezes 3 para caber na mesma escala.</div>
<div class="sep"></div><div class="g" style="grid-template-columns:repeat(3,1fr)">
{kpi('trend','Pico de demanda','julho','índice 100, 2 anos de histórico')}{kpi('cal','Melhor janela de campanha','maio e junho','antes do pico, regra sazonal_clima')}{kpi('target','Amostra',fmt(EV[3][2]+QZ_FIM),'agendamentos e quizzes, mínimo 30 por célula')}</div></div>
<div class="g" style="align-content:start">
<div class="card"><div class="hd"><h3>{i('cal',16)} Calendário comercial</h3></div><div class="lista-i" style="font-size:13px">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="pill {cl}" style="width:62px;justify-content:center">{d}</span><div style="flex:1"><b>{t}</b><div class="meta">{s}</div></div></div>' for d,t,s,cl in [('28/11','Black Friday','nacional · campanha da rede planejada','l'),('01/12','Início do verão de campanhas','Verão sem pelos · SP e PR','l'),('25/01','Aniversário de São Paulo','municipal · SP','b'),('14/02','Carnaval','nacional · menos agendamentos','a'),('08/03','Dia da Mulher','nacional','l')])+f'''</div></div>
<div class="card"><div class="hd"><h3>{i('globe',16)} Fontes</h3></div><div class="lista-i" style="font-size:13px"><div class="it"><b style="flex:1">INMET, normais climatológicas</b><span class="pill v">ligada</span></div><div class="it"><b style="flex:1">Feriados e datas</b><span class="pill v">ligada</span></div><div class="it"><b style="flex:1">Google Trends</b><span class="pill a">manual</span></div><div class="it"><b style="flex:1">Previsão e UV comercial</b><span class="pill z">desligada</span></div><div class="it"><b style="flex:1">Concorrência (Places)</b><span class="pill z">desligada</span></div></div></div></div></div>'''
salvar(ARQ['sazon'],pagina('Sazonalidade e clima',R('intel',c)))

# ---------- 68 DICIONÁRIO DE EVENTOS (T02) ----------
DEST={'unidade_visualizada':'GA4','lead_iniciado':'GA4','lead_enviado':'GA4 · Meta · Ads · TikTok','agendamento_concluido':'GA4 · Meta · Ads','whatsapp_clicado':'GA4','telefone_clicado':'GA4','rota_clicada':'GA4','atendimento_compareceu':'GA4 · Ads (offline)','quiz_iniciado':'GA4','quiz_concluido':'GA4','cliente_cadastrado':'GA4 · Meta','campanha_clicada':'GA4'}
c=cabec('Tracking','Dicionário de eventos v1.3 · aprovado em 18/11 · dona do tracking: Marina C. (pessoa nomeada na Gio).',f'<span class="btn">{i("log",14)} Versões</span><span class="btn p">{i("edit",14)} Propor mudança</span>')+tabs(TABS_TR,1)+f'''
<div class="g" style="grid-template-columns:1fr 420px;align-items:start">
<div class="card" style="padding:0;overflow:hidden"><table class="t"><thead><tr><th>Evento</th><th>Quando dispara</th><th>Destinos</th><th class="num">01 a 21 nov</th></tr></thead><tbody>'''+''.join(f'<tr class="{"sel" if n=="lead_enviado" else ""}"><td><code style="font:600 13px ui-monospace,monospace;color:var(--roxo-700)">{n}</code></td><td><span class="trunc" style="display:block;max-width:190px">{d}</span></td><td class="meta"><span class="trunc" style="display:block;max-width:130px">{DEST[n]}</span></td><td class="num">{fmt(v)}</td></tr>' for n,d,v in EV)+f'''</tbody></table>
<div class="meta" style="padding:12px 16px">12 eventos ativos · padrão objeto_acao em português, no particípio · renomeados da spec 001 (ex.: view_unidade virou unidade_visualizada)</div></div>
<div class="card"><div class="hd"><div><code style="font:600 15px ui-monospace,monospace;color:var(--roxo-700)">lead_enviado</code><div class="meta">dono: Marina C. · versão 3 · origem: servidor</div></div><span class="pill v" style="margin-left:auto">ativo</span></div>
<p class="muted" style="font-size:13px;margin-bottom:10px">Dispara quando o servidor aceita o formulário (princípio III). Nunca no clique.</p>
<div class="meta" style="font-weight:600">PROPRIEDADES</div><table class="t" style="font-size:13px;margin:6px 0 12px"><tbody>'''+''.join(f'<tr><td><code style="font:12px ui-monospace,monospace">{p}</code></td><td class="meta">{t}</td><td>{"<span class=\"pill l\">obrigatória</span>" if o else ""}</td></tr>' for p,t,o in [('event_id','texto, deduplicação',True),('unidade_id','texto',True),('template','A, B ou C',True),('origem_canal','lista fechada',True),('consentimento','categorias aceitas',True),('procedimento','chave do catálogo',False)])+f'''</tbody></table>
<div class="meta" style="font-weight:600">MAPEAMENTO POR DESTINO</div><div class="lista-i" style="font-size:13px">'''+''.join(f'<div class="it" style="padding:7px 0"><b style="width:110px">{d}</b><code style="font:12px ui-monospace,monospace">{e}</code></div>' for d,e in [('GA4','generate_lead'),('Meta','Lead (servidor)'),('Google Ads','conversão Lead'),('TikTok','SubmitForm')])+'''</div>
<div class="aviso l" style="margin-top:10px"><div>'''+i('shield',16)+'''</div><div style="font-size:13px">Sem dado pessoal no evento. Dados para anúncios só com hash e base legal, enviados pelo servidor.</div></div></div></div>'''
salvar(ARQ['dic'],pagina('Dicionário de eventos',R('saude',c)))

# ---------- 69 GERADOR DE UTM (T07) ----------
links=[('2026-12_verao-laser_sp-pr','whatsapp','mensagem','Ingrid N.',2140),('2026-11_black-november_rede','instagram','social','Ingrid N.',1312),('2026-11_ultraformer_altodalapa','email','email','Renata F.',94),('2026-11_qr-recepcao_cambui','qr','offline','Paulo M.',57)]
c=cabec('Tracking','Links com UTM em listas fechadas. Nada de digitar fonte ou meio à mão.',f'<span class="btn p">{i("plus",14)} Novo link</span>')+tabs(TABS_TR,2)+f'''
<div class="g" style="grid-template-columns:1fr 360px;align-items:start;margin-bottom:16px">
<div class="card"><div class="hd"><h3>Gerar link</h3></div><div class="g" style="grid-template-columns:1fr 1fr;gap:12px">
{campo('Página de destino','giobatel.exemplo.com.br/depilacao-a-laser',ic='link')}{campo('Unidade','GiO Batel',ic='pin')}
{campo('Fonte (lista)','whatsapp',ic='chevd')}{campo('Meio (lista)','mensagem',ic='chevd')}
{campo('Campanha','2026-12_verao-laser_sp-pr','L','Gerada pelo padrão ano-mês_tema_alcance, minúsculas, sem acento')}{campo('Conteúdo','botao-agendar',ic='edit')}</div>
<div class="campo" style="margin-top:12px"><label>Link final</label><div class="in" style="font:13px ui-monospace,monospace;word-break:break-all">https://giobatel.exemplo.com.br/depilacao-a-laser?utm_source=whatsapp&amp;utm_medium=mensagem&amp;utm_campaign=2026-12_verao-laser_sp-pr&amp;utm_content=botao-agendar</div></div></div>
<div class="card" style="text-align:center"><div class="hd"><h3>Link curto e QR</h3></div>
<div style="width:150px;height:150px;margin:6px auto;background:repeating-conic-gradient(#1d1424 0 25%,#fff 0 50%) 0 0/18px 18px;border:10px solid #fff;outline:1px solid var(--linha);border-radius:8px"></div><div class="meta">QR ilustrativo</div>
<div class="in" style="justify-content:center;margin-top:10px;border:1px solid var(--linha-forte);border-radius:10px;padding:9px;font-weight:600">gio.exemplo.com.br/v3rao</div>
<div style="display:flex;gap:8px;justify-content:center;margin-top:10px"><span class="btn s" data-sem-rota="1">{i('copy',12)} Copiar</span><span class="btn s" data-sem-rota="1">{i('down',12)} Baixar QR</span></div></div></div>
<div class="card" style="padding:0;overflow:hidden"><table class="t"><thead><tr><th>Campanha</th><th>Fonte</th><th>Meio</th><th>Dono</th><th class="num">Cliques</th><th>Checagem</th></tr></thead><tbody>'''+''.join(f'<tr><td><code style="font:13px ui-monospace,monospace">{c_}</code></td><td>{s}</td><td>{m}</td><td>{d}</td><td class="num">{fmt(n)}</td><td><span class="pill v">{i("check",11)} padrão ok</span></td></tr>' for c_,s,m,d,n in links)+f'''<tr><td><code style="font:13px ui-monospace,monospace">Promo_Natal</code></td><td>Insta</td><td>sem dados</td><td>link externo</td><td class="num">38</td><td><span class="pill r">{i("alert",11)} UTM inválida</span></td></tr></tbody></table>
<div class="meta" style="padding:12px 16px">UTMs inválidas na chegada: {UTM_INVAL_PCT}% das visitas com UTM no período. A linha em vermelho veio de um link montado fora do gerador.</div></div>'''
salvar(ARQ['utm'],pagina('Gerador de UTM',R('saude',c)))

# ---------- 70 SAÚDE DO TRACKING (T04 + T05) ----------
dias=[f'{d:02d}' for d in range(1,22)]
rnd=random.Random(7); vol=[round(21.2+rnd.random()*3.4,1) for _ in dias]; vol[17]=12.4
c=cabec('Tracking','Coletor próprio da rede: cada evento validado, sem duplicados, gravado no nosso banco e enviado pelo servidor.',periodo())+tabs(TABS_TR,0)+f'''
<div class="g" style="grid-template-columns:repeat(5,1fr);margin-bottom:16px">
{kpi('zap','Eventos recebidos',fmt(TOT_EV),'01 a 21 nov, 12 eventos do dicionário')}
{kpi('alert','Inválidos',EV_INVAL_PCT+'%','limite de alerta: 1%')}
{kpi('shield','Dado pessoal detectado','0','bloqueio automático no coletor')}
{kpi('link','UTMs inválidas',UTM_INVAL_PCT+'%','alerta aberto acima de 3%')}
{kpi('refresh','Coletor x GA4',DIVERG_GA4+'%','diferença aceitável até 5%')}</div>
<div class="g" style="grid-template-columns:1fr 400px;align-items:start">
<div class="card"><div class="hd"><h3>Eventos por dia (mil)</h3><span class="meta" style="margin-left:auto">queda em 18/11: falha de deploy corrigida em 2 h</span></div>{area([vol],['#b0197e'],w=700,h=220,labels=dias,ymax=30)}
<div class="sep"></div><div class="hd" style="margin-bottom:6px"><h3>Destinos</h3></div>
<table class="t" style="font-size:13px"><thead><tr><th>Destino</th><th>Envio</th><th>Consentimento exigido</th><th>Situação</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{d}</b></td><td>{e}</td><td>{c_}</td><td><span class="pill {cl}">{s}</span></td></tr>' for d,e,c_,s,cl in [('Analytics da rede','servidor','Estatística','ok','v'),(f'Analytics de {UN_DOMINIO} unidades','cópia','Estatística','ok','v'),('Meta','servidor','Marketing','ok','v'),('Google Ads','servidor','Marketing','ok','v'),('TikTok','servidor','Marketing','desligado','z')])+f'''</tbody></table></div>
<div class="g" style="align-content:start">
<div class="card"><div class="hd"><h3>{i('alert',16)} Alertas abertos</h3><span class="pill r" style="margin-left:auto">2</span></div><div class="lista-i" style="font-size:13px">
<div class="it"><span class="ic r" style="width:30px;height:30px">{i('alert',14)}</span><div style="flex:1"><b>lead_enviado ausente há 3 dias</b><div class="meta">GiO Montes Claros · regra ausência por unidade</div></div></div>
<div class="it"><span class="ic a" style="width:30px;height:30px">{i('link',14)}</span><div style="flex:1"><b>UTMs inválidas acima de 3%</b><div class="meta">links montados fora do gerador</div></div><a class="btn s" href="{L('utm')}">Ver</a></div></div></div>
<div class="card"><div class="hd"><h3>{i('gear',16)} Regras da medição</h3></div><div class="lista-i" style="font-size:13px">
<div class="it"><b style="flex:1">Dono do tracking</b><span>Marina C. (Gio)</span></div>
<div class="it"><b style="flex:1">Eventos brutos guardados</b><span>25 meses</span></div>
<div class="it"><b style="flex:1">Duplicados removidos</b><span>por event_id em 48 h</span></div>
<div class="it"><b style="flex:1">Tag no navegador</b><span>uma só, da rede</span></div>
<div class="it"><b style="flex:1">Unidades sem conversão (7 dias)</b><span>4</span></div></div>
<div class="meta" style="margin-top:8px">Decisões do Osmar de 21/11: coletor próprio, Analytics da rede, 25 meses.</div></div></div></div>'''
salvar(ARQ['saude'],pagina('Saúde do tracking',R('saude',c)))
print('s9 ok')
