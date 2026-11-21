from base import *
A=DEMO['altodalapa']
def cabec(t,p,dir=''): return f'<div class="cab"><div><h1>{t}</h1><p>{p}</p></div><div class="dir">{dir}</div></div>'
def code(txt): return f'<pre style="background:#24082c;color:#f3eaf6;border-radius:12px;padding:14px 16px;font:500 12px/1.6 ui-monospace,Menlo,monospace;overflow-x:auto;white-space:pre">{txt}</pre>'
# ---------- 19 SEO LOCAL DA UNIDADE ----------
js=f'''{{
  "@type": ["MedicalClinic","BeautySalon"], <span style="color:#E3D3EA">// rede</span>
  "name": "{A['nome']}",              <span style="color:#E3D3EA">// rede</span>
  "telephone": "{A['tel']}",         <span style="color:#ffd27a">// unidade</span>
  "address": {{ "streetAddress": "{A['end']}",
               "addressLocality": "{A['cidade']}" }},
  "openingHours": "Mo-Fr 09:00-20:00, Sa 09:00-17:00",
  "url": "https://{A['dom']}/", <span style="color:#E3D3EA">// rede</span>
  "aggregateRating": <span style="color:#E3D3EA">não usado (política Google)</span>
}}'''
nap=[('Nome',A['nome'],A['nome'],'v','igual'),('Endereço',A['end'],A['end'],'v','igual'),('Telefone',A['tel'],'(11) 90000-0009','a','diverge'),('Site',A['dom'],'outrosite.exemplo.com','r','outra URL'),('Horário de sábado','9h às 17h','9h às 15h','a','diverge'),('Categoria','Clínica de estética','Depilação a laser','z','sugestão')]
rev=[('Ana P.','5','Atendimento atencioso e a sala é muito limpa.','há 2 dias'),('Joana M.','4','Gostei do resultado, só demorou um pouco para começar.','há 5 dias'),('Cris L.','5','Equipe explica tudo antes da sessão.','há 1 semana')]
rev_pend=[('r2','Lu M.',1,'Fiquei com a pele vermelha e ardendo por dois dias depois da sessão.','há 9 h','r','sem resposta · saúde'),('r1','Paula R.',2,'Marquei pelo site e o horário não estava na agenda. Esperei 40 minutos.','há 3 h','a','unidade respondendo'),('r4','Rodrigo T.',3,'Gostei do lugar, mas achei o valor do pacote acima do que eu esperava.','há 2 dias','r','sem resposta'),('r3','Fernanda S.',5,'Equipe muito atenciosa, explicaram cada etapa e a sala é super limpa.','há 1 dia','r','sem resposta')]
faq=[('Quanto tempo dura a sessão de laser?','Rede · base','T'),('A unidade tem estacionamento?','Unidade · local','E'),('Atendem aos sábados?','Unidade · local','E'),('Precisa raspar antes?','Rede · base','T')]
cont=f'''<div class="migalha"><a href="{L('seo')}">SEO local</a> {i('chev',12)} <b style="color:var(--tinta)">{A['nome']}</b></div>
'''+cabec(f'SEO local · {A["nome"]}','Dados estruturados, comparação com o perfil do Google, avaliações e perguntas frequentes da unidade.',f'<span class="chip">Unidade: <b>{A["nome"]}</b> {i("chevd",12)}</span><span class="btn">{i("refresh",14)} Comparar agora</span>')+f'''
<div class="g" style="grid-template-columns:1fr 1fr;margin-bottom:16px">
 <div class="card"><div class="hd"><h3>{i('target',16)} Schema base</h3><span class="pill t" style="margin-left:auto">{i('lock',11)} definido pela rede</span></div>
  {code(js)}
  <p class="meta" style="margin-top:10px">A rede define tipos, campos e regras. A unidade só alimenta os campos marcados como dela, e cada publicação passa por validação automática.</p>
  <div style="display:flex;gap:8px;margin-top:10px"><span class="pill v">{i('check',11)} Validação sem erros</span><span class="pill a">1 aviso: horário do Google diferente</span></div></div>
 <div class="card"><div class="hd"><h3>{i('google',16)} Ficha x perfil do Google</h3><span class="sub" style="margin-left:auto">última leitura hoje às 12:40</span></div>
  <div class="aviso l" style="margin-bottom:12px"><div>{i('shield',16)}</div><div style="font-size:13px">O perfil do Google pertence à unidade. O sistema não edita o perfil: compara, avisa e mostra como corrigir no próprio Google.</div></div>
  <table class="t" style="font-size:13px;table-layout:fixed"><thead><tr><th style="width:24%">Campo</th><th>Ficha</th><th>Google</th><th style="width:22%">Situação</th></tr></thead><tbody>'''+''.join(f'<tr><td style="white-space:normal"><b>{c}</b></td><td style="white-space:normal;overflow-wrap:anywhere">{f}</td><td style="white-space:normal;overflow-wrap:anywhere">{g}</td><td><span class="pill {s}">{t}</span></td></tr>' for c,f,g,s,t in nap)+f'''</tbody></table>
  <div style="display:flex;gap:8px;margin-top:12px"><span class="btn s p">{i('send',12)} Avisar a unidade</span><a class="btn s" href="{L('ajuda')}">{i('book',12)} Guia: corrigir no Google</a></div></div>
</div>
<div class="g" style="grid-template-columns:1fr 1fr">
 <div class="card"><div class="hd" style="flex-wrap:wrap"><h3>{i('star',16)} Avaliações do Google</h3><div style="margin-left:auto;display:flex;gap:6px;flex-wrap:wrap"><a class="btn s p" href="{L('aval-un')}?u=GiO+Alto+da+Lapa">{i('inbox',12)} Ver a fila desta unidade</a><a class="btn s" href="{L('aval-rede')}">{i('chart',12)} Insights da rede</a></div></div>
  <div style="display:flex;gap:20px;align-items:center;margin-bottom:12px"><div><div class="pop" style="font-size:34px;font-weight:600">{A['nota']}</div><div class="meta">{A['aval']} avaliações (ilustrativo)</div></div>
  <div style="flex:1">'''+''.join(f'<div style="display:flex;gap:8px;align-items:center;font-size:12px"><span style="width:10px">{n}</span><span class="barra" style="flex:1;width:auto"><i style="width:{p}%"></i></span><span class="meta" style="width:30px;text-align:right">{p}%</span></div>' for n,p in [(5,82),(4,12),(3,4),(2,1),(1,1)])+f'''</div></div>
  <div class="meta" style="margin-bottom:4px"><b style="color:var(--tinta)">4 sem resposta, 2 com nota baixa</b> · mais urgentes primeiro</div><div class="lista-i">'''+''.join(f'<a class="it" href="{L("aval-ws")}#{k}" style="align-items:flex-start;color:inherit"><span class="av-s">{n[0]}{n.split()[1][0]}</span><div style="flex:1;min-width:0"><b>{n}</b> <span class="meta">{e} {"estrela" if e==1 else "estrelas"} · {q}</span> <span class="pill {c}">{s}</span><p class="muted" style="margin-top:2px">{t}</p></div></a>' for k,n,e,t,q,c,s in rev_pend)+f'''</div>
  <div class="aviso a" style="margin-top:10px"><div>{i('flag',16)}</div><div style="font-size:13px"><b>As avaliações de Lu M. e Paula R. foram avisadas à rede</b><div class="meta" style="margin-top:2px">A unidade responde pelo painel com sugestão da IA e a resposta é publicada no Google. A rede pode acompanhar ou assumir as notas 1 e 2 e as menções a saúde.</div><a class="lk" href="{L('aval-esc')}?f=todas&u=GiO+Alto+da+Lapa" style="display:inline-block;margin-top:6px">Escaladas desta unidade</a></div></div>
  <p class="meta" style="margin-top:8px">Avaliações não entram no schema da página (política do Google).</p></div>
 <div class="card"><div class="hd"><h3>{i('help',16)} Perguntas frequentes</h3><span class="pill v" style="margin-left:auto">FAQPage ativo</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it"><span style="color:var(--tinta-3)">{i("drag",16)}</span><div style="flex:1"><b>{p}</b><div class="meta">{o}</div></div><span class="pill {"t" if e=="T" else "e"}">{"Rede" if e=="T" else "Unidade · revisão posterior"}</span></div>' for p,o,e in faq)+f'''</div>
  <a class="btn s" href="{L('f-faq')}" style="margin-top:12px">Ver FAQ da unidade</a></div>
</div>'''
salvar(ARQ['seo'],pagina('SEO local',app('admin','seo',cont)))

# ---------- 20 TEMPLATES E MARCA ----------
tpls=[('A','Clássico','Formulário no topo, ideal para mídia paga','37-landing-a-desktop.png',58),('B','Vitrine','Fotos e equipe antes do formulário','39-landing-b-desktop.png',41),('C','Autoridade local','Mapa de bairros, FAQ local longo','41-landing-c-desktop.png',30)]
pol=[('Nome público','T','T','L'),('Telefone fixo','EA','EA','L'),('WhatsApp de leads','E','E','L'),('Endereço','T','T','L'),('Texto Sobre a unidade','E','E','L'),('Fotos','E','E','L'),('FAQ local','E','E','L'),('Promoção fora do modelo','EA','EA','O'),('Schema e canônica','T','T','O'),('Escolha do modelo A, B, C','EA','EA','L')]
nome={'T':('t','Rede'),'E':('e','Editável'),'EA':('ea','Com aprovação'),'L':('z','Leitura'),'O':('z','Oculto')}
cont=cabec('Templates e marca','Modelos de página, identidade da rede e o que cada perfil de unidade pode mudar.',f'<span class="btn">{i("eye",14)} Prévia</span><span class="btn p">{i("check",14)} Publicar para a rede</span>')+f'''
<div class="tabs"><a class="on">Modelos de página</a><a>Identidade</a><a>Política de campos</a><a>Blocos</a></div>
<div class="g" style="grid-template-columns:repeat(3,1fr);margin-bottom:16px">'''+''.join(f'<div class="card" style="padding:0;overflow:hidden"><div style="height:200px;background:#efe7f2 url(../png/{img}) top center/cover;border-bottom:1px solid var(--linha)"></div><div style="padding:14px 16px"><div style="display:flex;gap:8px;align-items:center"><b class="pop" style="font-size:16px">Modelo {k} · {n}</b><span class="pill l" style="margin-left:auto">{q} unidades</span></div><p class="meta" style="margin-top:4px">{d}</p></div></div>' for k,n,d,img,q in tpls)+f'''</div>
<p class="meta" style="margin:-6px 0 16px">58 + 41 + 30 = 129 unidades com modelo · 1 sem modelo (GiO Catalão Centro)</p>
<div class="g" style="grid-template-columns:1fr 1.3fr">
 <div class="card"><div class="hd"><h3>Identidade da rede</h3><span class="pill t" style="margin-left:auto">{i('lock',11)} só a rede edita</span></div>
  <div style="display:flex;gap:10px;margin-bottom:14px">'''+''.join(f'<div style="flex:1"><div style="height:46px;border-radius:10px;background:{c};border:1px solid var(--linha)"></div><div class="meta" style="margin-top:4px">{n}<br>{c}</div></div>' for n,c in [('Roxo','#4c1455'),('Vinho','#6f0052'),('Magenta','#b0197e'),('Rosa (só detalhe)','#e5559f'),('Lilás','#f3eaf6')])+f'''</div>
  <div class="lista-i" style="font-size:13px"><div class="it"><span style="flex:1">Títulos</span><b class="pop">Poppins</b></div><div class="it"><span style="flex:1">Texto</span><b>Inter</b></div><div class="it"><span style="flex:1">Contraste mínimo</span><b>AA 4,5:1, checado no build</b></div></div></div>
 <div class="card"><div class="hd"><h3>Política de campos (resumo)</h3><a class="lk" style="margin-left:auto;font-size:13px">Ver os 83 itens</a></div>
  <table class="t" style="font-size:13px"><thead><tr><th>Campo</th><th>Admin da unidade</th><th>Gerente</th><th>Recepção</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{c}</b></td>'+''.join(f'<td><span class="pill {nome[x][0]}">{nome[x][1]}</span></td>' for x in xs)+'</tr>' for c,*xs in pol)+f'''</tbody></table></div>
</div>'''
salvar(ARQ['tpl'],pagina('Templates e marca',app('admin','tpl',cont)))

# ---------- 21 MODELOS DE FICHA ----------
mods=[('Padrão rede v3','Principal · 112 unidades',True),('Clínica compacta','9 unidades',False),('Unidade em shopping','8 unidades',False),('Inauguração','1 unidade · temporário',False)]
menu=[('Dados e contato','#dados',True,'T'),('Horários','#horarios',True,'T'),('Tratamentos','#tratamentos',True,'T'),('Fotos','#fotos',True,'T'),('Landing pages','#landing-pages',True,'T'),('SEO e Google','#seo',True,'T'),('Leads','#leads',True,'T'),('Equipe','#equipe',True,'E'),('Promoções','#promocoes',False,'E'),('Domínio','#dominio',True,'T')]
cont=cabec('Modelos de ficha','Cada unidade usa um modelo. O modelo define as seções da ficha, a ordem do menu e as âncoras.',f'<span class="btn">{i("copy",14)} Duplicar</span><span class="btn">{i("star",14)} Definir como principal</span><span class="btn p">{i("check",14)} Salvar modelo</span>')+f'''
<div class="g" style="grid-template-columns:250px 1fr 290px">
 <div class="card" style="padding:12px">'''+''.join(f'<div style="padding:12px;border-radius:12px;margin-bottom:6px;{"background:var(--lilas-100);border:1px solid var(--lilas-300)" if on else "border:1px solid var(--linha)"}"><div style="display:flex;gap:8px;align-items:center"><b>{n}</b>{"<span class=\"pill l\" style=\"margin-left:auto\">principal</span>" if on else ""}</div><div class="meta">{d}</div></div>' for n,d,on in mods)+f'''<span class="btn s" style="margin-top:6px">{i('plus',12)} Novo modelo</span></div>
 <div class="card"><div class="hd"><div><h3>Menu da ficha · Padrão rede v3</h3><div class="meta">Arraste para reordenar. A âncora vira o endereço da seção.</div></div></div>
  <table class="t"><thead><tr><th></th><th>Item</th><th>Âncora</th><th>Quem edita</th><th>Visível</th></tr></thead><tbody>'''+''.join(f'<tr class="{"sel" if t=="Landing pages" else ""}"><td style="color:var(--tinta-3)">{i("drag",16)}</td><td><b>{t}</b>{" <span class=\"pill b\">novo</span>" if t=="Landing pages" else ""}</td><td><code style="font-size:13px;color:var(--vinho)">{a}</code></td><td><span class="pill {"t" if e=="T" else "e"}">{"Rede" if e=="T" else "Unidade"}</span></td><td><span class="tog{" on" if v else ""}"></span></td></tr>' for t,a,v,e in menu)+f'''</tbody></table>
  <span class="btn s" style="margin-top:12px">{i('plus',12)} Adicionar item</span></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Prévia do menu</h3></div>
   <div style="border:1px solid var(--linha);border-radius:12px;padding:8px">'''+''.join(f'<div style="display:flex;gap:8px;align-items:center;padding:8px 10px;border-radius:8px;{"background:var(--lilas-100);color:var(--roxo-700);font-weight:600" if t=="Landing pages" else ""}">{t}<span class="meta" style="margin-left:auto">{a}</span></div>' for t,a,v,e in menu if v)+f'''</div></div>
  <div class="aviso a"><div>{i('alert',16)}</div><div style="font-size:13px">Trocar o modelo de 112 unidades gera aviso para cada uma e fica na auditoria. Campos preenchidos nunca são apagados: seções ocultas guardam os dados.</div></div>
 </div>
</div>'''
salvar(ARQ['modelos'],pagina('Modelos de ficha',app('admin','modelos',cont)))

# ---------- 22 MÓDULOS (feature toggles) ----------
mrows=[('Central de leads','núcleo',['on','on','on','on']),('Página da unidade','núcleo',['on','on','on','on']),('Landing pages e variantes','',['on','on','on','her-on']),('Testes A/B','',['on','on','off','her-on']),('Relatórios inteligentes','',['on','on','on','her-on']),('Chat ao vivo','piloto',['off','on','off','her-on']),('Agenda online (DocBiz)','',['on','on','on','off']),('Promoções na página','',['on','on','on','her-on']),('Avaliações do Google (leitura)','',['on','on','on','her-on'])]
def tg(x):
    if x=='on': return '<span class="tog on"></span>'
    if x=='off': return '<span class="tog"></span>'
    if x=='her-on': return '<span class="tog her on" title="herdado"></span>'
    return '<span class="tog her" title="herdado"></span>'
cont=cabec('Módulos','Liga e desliga recursos por rede, regional e unidade. A unidade herda da regional, que herda da rede.',f'<span class="btn">{i("log",14)} Histórico</span><span class="btn p">{i("check",14)} Aplicar mudanças</span>')+f'''
<div style="display:flex;gap:8px;margin-bottom:14px;align-items:center"><span class="chip on">Escopo: <b>Rede › Regional SP Capital › GiO Alto da Lapa</b> {i('chevd',12)}</span><span class="meta">Mudanças pendentes: 1 · afeta 1 unidade</span></div>
<div class="g" style="grid-template-columns:1fr 320px">
 <div class="card" style="padding:0"><table class="t"><thead><tr><th>Módulo</th><th>Rede</th><th>Regional SP</th><th>Regional Sul</th><th>Alto da Lapa</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{m}</b>{f" <span class=\"pill z\">{tag}</span>" if tag else ""}</td>'+''.join(f'<td>{tg(x) if tag!="núcleo" else "<span class=\"pill v\">sempre</span>"}</td>' for x in xs)+'</tr>' for m,tag,xs in mrows)+f'''</tbody></table></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Mudança pendente</h3></div>
   <div class="lista-i" style="font-size:13px"><div class="it"><div class="ic a">{i('cal',15)}</div><div><b>Agenda online desligada na GiO Alto da Lapa</b><div class="meta">Motivo: unidade em troca de sistema até 05/12. Volta a herdar da regional na data.</div></div></div></div>
   <div class="aviso l" style="margin-top:10px"><div>{i('bell',16)}</div><div style="font-size:13px">A unidade recebe aviso. O botão Agendar da página vira "Fale no WhatsApp" enquanto o módulo estiver desligado.</div></div></div>
  <div class="card"><div class="hd"><h3>Legenda</h3></div><div class="lista-i" style="font-size:13px"><div class="it"><span class="tog on"></span> definido neste nível</div><div class="it"><span class="tog her on"></span> herdado do nível acima</div><div class="it"><span class="pill v">sempre ativo</span> núcleo, não desliga</div></div></div>
 </div>
</div>'''
salvar(ARQ['modulos'],pagina('Módulos',app('admin','modulos',cont)))

# ---------- 23 CENTRAL DE AJUDA (WIKI) ----------
trilhas=[('Franqueado','Primeiros passos, ficha, fotos, leads',12,'users'),('Recepção','Atender lead pelo botão, status, agenda',6,'phone'),('Marketing da rede','Campanhas, variantes, insights',9,'chart'),('SEO','Schema base, comparação com Google, canônicas',8,'target'),('Call center','Fila, SLA, registro de ligação',5,'inbox'),('Gestor regional','Aprovações e relatórios da regional',4,'map')]
gbp=[('Reivindicar e verificar o perfil no Google',True),('Usar o mesmo nome, endereço e telefone da ficha',True),('Colocar o link da página oficial da unidade',False),('Escolher a categoria recomendada pela rede',False),('Subir 10 fotos reais (fachada, recepção, salas)',False),('Responder avaliações em até 48 h',False),('Publicar um post por semana',False)]
cont=cabec('Central de ajuda','Guias por perfil, vídeos e novidades do sistema. Busca em todos os artigos.','')+f'''
<div class="card" style="background:var(--grad);color:#fff;border:0;margin-bottom:16px;padding:26px 28px">
 <h2 style="font-size:22px;font-weight:600">Como podemos ajudar?</h2>
 <div style="display:flex;align-items:center;gap:10px;background:#fff;color:var(--tinta-3);border-radius:12px;padding:12px 14px;margin-top:12px;max-width:640px">{i('search',16)} Busque: domínio, fotos, perfil do Google, LGPD…</div>
 <div style="display:flex;gap:8px;margin-top:12px;flex-wrap:wrap">'''+''.join(f'<span class="pill" style="background:rgba(255,255,255,.18);color:#fff">{t}</span>' for t in ['Primeiro acesso','Convidar equipe','Apontar domínio','Corrigir dados no Google'])+f'''</div>
</div>
<div class="g" style="grid-template-columns:1.4fr 1fr">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Trilhas por perfil</h3><span class="sub" style="margin-left:auto">mostramos primeiro a do seu perfil</span></div>
   <div class="g" style="grid-template-columns:repeat(3,1fr);gap:12px">'''+''.join(f'<div style="border:1px solid var(--linha);border-radius:12px;padding:14px;{"background:var(--lilas-50);border-color:var(--lilas-300)" if k==2 else ""}"><div class="ic l" style="margin-bottom:8px">{i(ic,16)}</div><b>{t}</b><div class="meta" style="margin-top:2px">{d}</div><div class="meta" style="margin-top:6px;font-weight:600">{n} artigos</div></div>' for k,(t,d,n,ic) in enumerate(trilhas))+f'''</div></div>
  <div class="card"><div class="hd"><h3>{i('google',16)} Trilha: perfil do Google da sua unidade</h3><span class="pill l" style="margin-left:auto">2 de 7</span></div>
   <p class="meta" style="margin:-6px 0 10px">O perfil é da unidade, que cuida dele no Google. O sistema compara com a ficha e avisa quando algo diverge.</p>
   <div class="lista-i">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="cx{" on" if ok else ""}"></span><span style="flex:1;{"color:var(--tinta-3)" if ok else ""}">{t}</span>{i("chev",14)}</div>' for t,ok in gbp)+f'''</div></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('video',16)} Vídeos curtos</h3></div>
   <div class="lista-i">'''+''.join(f'<div class="it"><div style="width:96px;height:56px;border-radius:10px;background:url(../assets/fotos/{f}.jpg) center/cover;position:relative;flex:none"><span style="position:absolute;inset:0;display:grid;place-items:center;background:rgba(36,8,44,.35);border-radius:10px;color:#fff">{i("zap",16)}</span></div><div><b>{t}</b><div class="meta">{d}</div></div></div>' for f,t,d in [('recepcao','Primeiros passos no portal','3 min'),('sala-laser','Fotos que vendem a unidade','4 min'),('equipe','Atender lead pelo botão','2 min')])+f'''</div></div>
  <div class="card"><div class="hd"><h3>{i('bell',16)} Novidades</h3></div>
   <div class="lista-i" style="font-size:13px"><div class="it"><span class="pill b">novo</span><span>Seção Landing pages na ficha</span></div><div class="it"><span class="pill b">novo</span><span>Relatórios inteligentes por e-mail</span></div><div class="it"><span class="pill z">ajuste</span><span>Verificação em duas etapas obrigatória</span></div></div></div>
  <div class="card"><div class="hd"><h3>Não achou?</h3></div><p class="meta">Abra um chamado para a rede. Buscas sem resultado viram sugestão de artigo.</p><a class="btn s p" href="{L('suporte')}" style="margin-top:10px">Abrir chamado</a></div>
 </div>
</div>'''
salvar(ARQ['ajuda'],pagina('Central de ajuda',app('admin','ajuda',cont)))
print('s4 ok')
