from base import *
random.seed(5)
LAPA=[u for u in UNID if u['url_site']=='altodalapa'][0]
def campo(l,v,lock=False,aj='',ic=''):
    return f'<div class="campo"><label>{l}{" "+i("lock",11) if lock else ""}</label><div class="in{" lock" if lock else ""}">{i(ic,14) if ic else ""}{v}</div>{f"<div class=ajuda>{aj}</div>" if aj else ""}</div>'
# 05 DETALHE UNIDADE (ADMIN)
horas=[('Segunda','9h às 20h'),('Terça','9h às 20h'),('Quarta','9h às 20h'),('Quinta','9h às 20h'),('Sexta','9h às 20h'),('Sábado','9h às 15h'),('Domingo','Fechado')]
check=[('v','Endereço e coordenadas'),('v','Telefone e WhatsApp'),('v','Horários'),('v','12 tratamentos'),('v','8 fotos'),('a','FAQ local: 3 de 6'),('v','2 profissionais'),('r','GBP aponta para outro site')]
cont=f'''
<div style="display:flex;align-items:center;gap:6px;color:var(--tinta-3);margin-bottom:12px;font-size:12px">Unidades {i('chev',12)} São Paulo {i('chev',12)} <b style="color:var(--tinta)">GiO Alto da Lapa</b></div>
<div class="card" style="padding:0;overflow:hidden;margin-bottom:16px">
 <div style="height:120px;background:var(--grad);position:relative"><div style="position:absolute;inset:0;background:url(../assets/fachada.jpg) center 40%/cover;opacity:.35;mix-blend-mode:luminosity"></div></div>
 <div style="display:flex;align-items:flex-start;gap:18px;padding:0 24px 16px;position:relative">
  <div style="flex:none;margin-top:-44px;width:96px;height:96px;border-radius:20px;border:4px solid #fff;background:url(../assets/fachada.jpg) center/cover;box-shadow:var(--sombra)"></div>
  <div style="padding-top:14px"><div style="display:flex;gap:8px;align-items:center"><h1 style="font-size:22px;font-weight:600;white-space:nowrap">GiO Alto da Lapa</h1><span class="pill v"><i></i>Ativa</span><span class="pill l">Template B</span><span class="pill b">{i('globe',11)} gioaltodalapa.com.br</span></div>
  <div class="muted" style="margin-top:4px">{i('pin',13)} Av. São Gualter, 53 · Vila Ida · São Paulo/SP &nbsp;·&nbsp; ID DocBiz 4127</div></div>
  <div style="margin-left:auto;display:flex;gap:8px;padding-top:16px"><span class="btn">{i('eye',14)} Ver página</span><span class="btn">{i('users',14)} Entrar como unidade</span><span class="btn p">{i('check',14)} Salvar alterações</span></div>
 </div>
 <div class="tabs" style="padding:0 18px;margin:0">'''+''.join(f'<a class="{"on" if k==0 else ""}">{t}{f" <span class=n>{n}</span>" if n else ""}</a>' for k,(t,n) in enumerate([('Dados e contato',''),('Horários',''),('Tratamentos','12'),('Fotos','8'),('Página',''),('Domínio',''),('SEO e Google','1'),('Integrações',''),('Leads','41'),('Usuários','3'),('Histórico','')]))+f'''</div>
</div>
<div class="g" style="grid-template-columns:1fr 340px">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Identificação</h3><span class="sub" style="margin-left:auto">{i('lock',12)} campos com cadeado são da rede</span></div>
   <div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:14px">{campo('Nome público','GiO Alto da Lapa',True)}{campo('Slug da ficha','/unidade/altodalapa/',True)}{campo('ID DocBiz','4127',True,'Sincronizado há 6 min')}
   {campo('Razão social','Estética Lapa Ltda.',True)}{campo('CNPJ','12.345.678/0001-90',True)}{campo('Tipo de clínica','Full · laser e estética',True)}</div></div>
  <div class="card"><div class="hd"><h3>Contato e endereço</h3><span class="pill v" style="margin-left:auto">{i('check',11)} NAP igual ao Google</span></div>
   <div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:14px">{campo('Telefone','(11) 3832 4410','',"Usado no schema e no GBP",'phone')}{campo('WhatsApp de atendimento','(11) 94587 2210','','Recebe o lead com mensagem pronta','wa')}{campo('E-mail da unidade','altodalapa@exemplo.com.br','','','inbox')}
   {campo('CEP','05071 000')}{campo('Endereço','Av. São Gualter, 53')}{campo('Bairro','Vila Ida')}</div>
   <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:14px">
    <div style="height:150px;border-radius:12px;background:#f1eaf4;position:relative;overflow:hidden">
     <svg width="100%" height="150" viewBox="0 0 400 150"><g stroke="#e2d6e8" stroke-width="10" fill="none"><path d="M0 40 L400 70"/><path d="M120 0 L160 150"/><path d="M280 0 L250 150"/><path d="M0 120 L400 105"/></g><g stroke="#fff" stroke-width="4" fill="none"><path d="M0 40 L400 70"/><path d="M120 0 L160 150"/></g></svg>
     <div style="position:absolute;left:46%;top:32%;color:var(--vinho)">{i('pin',34)}</div><span class="pill" style="position:absolute;left:10px;bottom:10px;background:#fff">-23,5361 · -46,7203</span></div>
    <div class="card" style="box-shadow:none;background:var(--lilas-50)"><b>Raio de atendimento</b><div class="muted" style="font-size:12px;margin:4px 0 10px">Bairros citados na página e no schema areaServed</div>
    <div style="display:flex;gap:6px;flex-wrap:wrap">'''+''.join(f'<span class="chip" style="padding:4px 9px">{b}</span>' for b in ['Alto da Lapa','Vila Ida','Lapa','Vila Romana','Pompeia','Perdizes','Alto de Pinheiros'])+f'''<span class="chip" style="padding:4px 9px">{i('plus',11)} bairro</span></div></div></div></div>
  <div class="card"><div class="hd"><h3>Horários</h3><span class="sub">feriados e exceções entram no Google e na página</span><div class="dir"><span class="btn s">{i('cal',12)} Exceções <span class="pill l">2</span></span></div></div>
   <div class="g" style="grid-template-columns:repeat(7,1fr);gap:10px">'''+''.join(f'<div style="border:1px solid var(--linha);border-radius:12px;padding:10px;{"background:var(--lilas-50);" if h=="Fechado" else ""}"><div class="muted" style="font-size:11px;font-weight:600">{d}</div><b style="font-size:12px">{h}</b></div>' for d,h in horas)+f'''</div></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Completude da página</h3></div>
   <div style="display:flex;align-items:center;gap:16px">{donut([90,10],['#b0197e','#f1e6f3'],tam=110,esp=14,centro='90%',sub='de 100')}<div class="muted" style="font-size:12px">7º lugar na rede. Falta 1 item para entrar no grupo verde do mapa.</div></div>
   <div class="lista-i" style="margin-top:10px">'''+''.join(f'<div class="it" style="padding:7px 0"><span class="ic {c}" style="width:22px;height:22px;border-radius:7px">{i("check" if c=="v" else "alert",12)}</span><span style="flex:1">{t}</span></div>' for c,t in check)+f'''</div></div>
  <div class="card"><div class="hd"><h3>Últimos 30 dias</h3></div>
   <div class="g" style="grid-template-columns:1fr 1fr;gap:12px"><div><div class="muted" style="font-size:11px">Leads</div><b class="pop" style="font-size:20px">41</b> <span class="up" style="font-size:12px">+18%</span></div><div><div class="muted" style="font-size:11px">Agendados</div><b class="pop" style="font-size:20px">27</b></div><div><div class="muted" style="font-size:11px">1º contato</div><b class="pop" style="font-size:20px">8 min</b></div><div><div class="muted" style="font-size:11px">Nota Google</div><b class="pop" style="font-size:20px">4,9</b> <span class="muted" style="font-size:12px">312 av.</span></div></div>
   <div style="margin-top:10px">{spark([3,5,4,6,2,7,5,8,6,9,7,8],w=290,h=46)}</div></div>
  <div class="card"><div class="hd"><h3>Pessoas com acesso</h3><span class="btn s" style="margin-left:auto">{i('plus',12)} Convidar</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="av-s" style="background:{c}">{a}</span><div style="flex:1"><b>{n}</b><div class="muted" style="font-size:11px">{r}</div></div></div>' for a,n,r,c in [('RF','Renata F.','Franqueada · dona','#f3c6e0'),('JM','Juliana M.','Recepção · leads','#e4d4f0'),('CC','Call center SP','Fila compartilhada','#dbe7ff')])+'''</div></div>
 </div>
</div>'''
salvar('05-admin-unidade-detalhe',pagina('Unidade',app('admin','unidades',cont),extra_css='.tabs a{padding:10px 10px;white-space:nowrap}'))

# 06 APROVAÇÕES
fila=[('GiO Alto da Lapa','Texto do bloco Sobre e 2 fotos','há 12 min','l',True),('GiO Batel','Troca de template para C','há 1 h','b',False),('GiO Cambuí','Novo tratamento: Bioestimulador','há 3 h','l',False),('GiO Asa Sul','Domínio próprio gioasasul.com.br','ontem','a',False),('GiO Aldeota','FAQ local com 4 perguntas','ontem','l',False),('GiO Salvador','Horário de sábado','2 dias','l',False),('GiO Bom Fim','Banner promocional','2 dias','r',False)]
cont=f'''
<div class="cab"><div><h1>Aprovações</h1><p>Mudanças pedidas pelas unidades que mexem em texto, imagem ou domínio. Meta da rede: responder em até 1 dia útil.</p></div>
<div class="dir"><span class="chip on">Pendentes <b>7</b></span><span class="chip">Aprovadas</span><span class="chip">Devolvidas</span><span class="btn">{i('gear',14)} Regras automáticas</span></div></div>
<div class="g" style="grid-template-columns:360px 1fr">
 <div class="card" style="padding:8px">'''+''.join(f'<div style="display:flex;gap:10px;padding:12px;border-radius:12px;{"background:var(--lilas-50);border:1px solid var(--lilas-300)" if s else "border:1px solid transparent"}"><div class="un"><div class="ft" style="background-image:url(../assets/fachada.jpg)"></div></div><div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between"><b>{n}</b><span class="muted" style="font-size:11px">{t}</span></div><div class="muted trunc" style="font-size:12px">{d}</div><span class="pill {c}" style="margin-top:6px">{"Conteúdo" if c=="l" else ("Template" if c=="b" else ("Domínio" if c=="a" else "Fora da regra"))}</span></div></div>' for n,d,t,c,s in fila)+f'''</div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><div><h3>GiO Alto da Lapa · Sobre e galeria</h3><div class="sub">Enviado por Renata F. · 21/11/2026 às 10:42 · versão 14</div></div><div class="dir"><span class="btn">{i('eye',14)} Pré-visualizar</span><span class="btn">{i('x',14)} Devolver com nota</span><span class="btn p">{i('check',14)} Aprovar e publicar</span></div></div>
  <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap"><span class="pill v">{i('check',11)} Sem preço</span><span class="pill v">{i('check',11)} Sem marca de equipamento</span><span class="pill v">{i('check',11)} NAP intacto</span><span class="pill a">{i('alert',11)} 1 termo para revisar</span><span class="pill v">{i('check',11)} Fotos 1600 px, com texto alternativo</span></div>
  <div class="g" style="grid-template-columns:1fr 1fr;gap:14px">
   <div style="border:1px solid var(--linha);border-radius:14px;padding:16px"><div class="muted" style="font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px">Publicado hoje</div>
   <p style="line-height:1.7">A GiO Alto da Lapa fica na Av. São Gualter e atende a região com depilação a laser e tratamentos faciais e corporais. <span style="background:#fde7ee;text-decoration:line-through;color:#a3243f">Venha conhecer nossa clínica.</span></p></div>
   <div style="border:1px solid var(--lilas-300);border-radius:14px;padding:16px;background:#fdfbfe"><div style="font-size:11px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px;color:var(--vinho)">Proposta da unidade</div>
   <p style="line-height:1.7">A GiO Alto da Lapa fica na Av. São Gualter e atende a região com depilação a laser e tratamentos faciais e corporais. <span style="background:#e3f6ec">Estamos a 5 minutos da Praça Cornélia, com estacionamento conveniado na rua Tito.</span> <span style="background:#fff3d6;border-bottom:2px dotted #d98a00">Resultados garantidos</span> <span style="background:#e3f6ec">desde a primeira sessão de avaliação gratuita.</span></p>
   <div class="card" style="box-shadow:none;background:var(--ambar-50);border-color:#f6dfa6;margin-top:10px;padding:10px 12px;font-size:12px">{i('alert',13)} <b>"Resultados garantidos"</b> fere a regra 5 da marca (promessa de resultado). Sugestão: "acompanhamento em todas as sessões".</div></div>
  </div>
  <div class="sep"></div>
  <div class="hd"><h3>Galeria</h3><span class="sub">2 fotos novas, 1 removida</span></div>
  <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px">'''+''.join(f'<div style="height:96px;border-radius:12px;background:url(../assets/fachada.jpg) {p}/cover;position:relative;{o}"><span class="pill {c}" style="position:absolute;left:6px;top:6px">{t}</span></div>' for p,c,t,o in [('20% 30%','z','Mantida',''),('60% 50%','z','Mantida',''),('80% 20%','r','Removida','opacity:.45;filter:grayscale(1)'),('40% 70%','v','Nova',''),('10% 60%','v','Nova','')])+f'''</div></div>
  <div class="card"><div class="hd"><h3>{i('log',15)} Histórico desta página</h3></div><div class="lista-i">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="pill {c}">{s}</span><span style="flex:1">{t}</span><span class="muted" style="font-size:12px">{d}</span></div>' for c,s,t,d in [('v','Aprovada','v13 · Troca do telefone do WhatsApp por Ingrid N.','18/11 às 16:20'),('r','Devolvida','v12 · Banner com preço promocional','12/11 às 09:05'),('v','Aprovada','v11 · Template B ativado','02/11 às 11:47')])+'''</div></div>
 </div>
</div>'''
salvar('06-admin-aprovacoes',pagina('Aprovações',app('admin','aprov',cont)))

# 07 KANBAN
nomes=['Mariana S.','Beatriz L.','Carla M.','Fernanda R.','Juliana P.','Patrícia A.','Aline C.','Camila T.','Larissa O.','Gabriela N.','Renan F.','Bruna D.','Tatiane V.','Priscila G.','Vanessa K.','Letícia H.','Daniela E.','Rafaela B.']
trat=['Depilação a laser','Limpeza de pele','Criolipólise','Microagulhamento','Depilação a laser','Bioestimulador','Peeling','Depilação a laser']
orig=[('Google Ads','l'),('Orgânico','v'),('Meta Ads','b'),('GBP','a'),('Instagram','b')]
und=['Alto da Lapa','Batel','Cambuí','Tatuapé','Vila Madalena','Aldeota','Asa Sul','Bom Fim']
cols=[('Novo','#6b4f78',5,True),('Em contato','#2f6fe0',4,False),('Agendado','#b0197e',4,False),('Compareceu','#0e9f6e',3,False),('Perdido','#a39aaa',2,False)]
k=0;html_cols=''
for nome,cor,qt,sla in cols:
    cards=''
    for j in range(qt):
        n=nomes[k%len(nomes)];o,oc=orig[k%5];t=trat[k%8];un=und[k%8];k+=1
        slat=''
        if nome=='Novo':
            m=[3,9,14,22,41][j]; cl='v' if m<10 else ('a' if m<=15 else 'r')
            slat=f'<span class="pill {cl}">{i("clock",11)} {m} min</span>'
        elif nome=='Agendado': slat=f'<span class="pill l">{i("cal",11)} {["Hoje 15:30","Amanhã 10:00","Seg 18:00","Ter 09:30"][j]}</span>'
        elif nome=='Compareceu': slat='<span class="pill v">'+i('check',11)+' DocBiz</span>'
        elif nome=='Perdido': slat='<span class="pill z">'+['Sem resposta','Outra unidade'][j]+'</span>'
        else: slat=f'<span class="pill b">{i("wa",11)} {["2 msgs","Ligação","1 msg","Retornar 17h"][j]}</span>'
        fila_='Call center' if (k%3==0) else 'Unidade'
        cards+=f'''<div class="card" style="padding:12px;border-radius:13px;{"border-left:3px solid "+cor if j==0 and nome=="Novo" else ""}">
<div style="display:flex;justify-content:space-between;align-items:center"><b>{n}</b>{slat}</div>
<div class="muted" style="font-size:12px;margin:3px 0 8px">{t} · GiO {un}</div>
<div style="display:flex;gap:5px;flex-wrap:wrap"><span class="pill {oc}">{o}</span><span class="pill z">{fila_}</span></div></div>'''
    html_cols+=f'''<div style="background:#f1ebf4;border-radius:16px;padding:10px;display:flex;flex-direction:column;gap:9px">
<div style="display:flex;align-items:center;gap:8px;padding:4px 4px 2px"><i style="width:8px;height:8px;border-radius:50%;background:{cor}"></i><b>{nome}</b><span class="muted">{ {"Novo":38,"Em contato":61,"Agendado":112,"Compareceu":74,"Perdido":29}[nome] }</span><span style="margin-left:auto;color:var(--tinta-3)">{i('more',14)}</span></div>{cards}
<div class="muted" style="text-align:center;font-size:12px;padding:4px">Ver mais</div></div>'''
cont=f'''
<div class="cab"><div><h1>Central de leads</h1><p>Leads de todas as páginas. Status sincronizado com o DocBiz a cada 5 minutos.</p></div>
<div class="dir"><span class="sw"><span class="on">{i('grid',13)} Quadro</span><span>{i('list',13)} Lista</span></span><span class="btn">{i('down',14)} Exportar</span><span class="btn p">{i('gear',14)} Regras de distribuição</span></div></div>
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:14px">
 <div class="card" style="display:flex;gap:12px;align-items:center"><div class="ic r">{i('clock',16)}</div><div><b class="pop" style="font-size:20px">9</b> <span class="muted">fora do SLA agora</span><div class="muted" style="font-size:12px">meta: 1º contato em 15 min</div></div></div>
 <div class="card" style="display:flex;gap:12px;align-items:center"><div class="ic l">{i('phone',16)}</div><div><b class="pop" style="font-size:20px">64%</b> <span class="muted">com call center</span><div class="muted" style="font-size:12px">36% direto na unidade</div></div></div>
 <div class="card" style="display:flex;gap:12px;align-items:center"><div class="ic v">{i('check',16)}</div><div><b class="pop" style="font-size:20px">11 min</b> <span class="muted">mediana 1º contato</span><div class="muted" style="font-size:12px">ontem: 13 min</div></div></div>
 <div class="card" style="display:flex;gap:12px;align-items:center"><div class="ic a">{i('refresh',16)}</div><div><b class="pop" style="font-size:20px">3</b> <span class="muted">sem ID DocBiz</span><div class="muted" style="font-size:12px">envio falhou, nova tentativa em 2 min</div></div></div>
</div>
<div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap"><span class="chip on">Fila: <b>Todas</b> {i('chevd',12)}</span><span class="chip">Unidade {i('chevd',12)}</span><span class="chip">Origem {i('chevd',12)}</span><span class="chip">Campanha {i('chevd',12)}</span><span class="chip">Tratamento {i('chevd',12)}</span><span class="chip">Responsável {i('chevd',12)}</span><span class="chip on">SLA: <b>estourado</b> {i('x',12)}</span><span class="chip">{i('cal',12)} Últimos 7 dias</span></div>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px">{html_cols}</div>'''
salvar('07-leads-kanban',pagina('Leads',app('admin','leads',cont)))

# 08 LEAD DETALHE
jornada=[('cursor','l','Clique no anúncio','Google Ads · campanha "laser_sp_zona_oeste" · termo "depilação a laser lapa"','19/11 · 20:41'),
('globe','l','Entrou na página da unidade','gioaltodalapa.com.br · template B · celular Android','19/11 · 20:41'),
('eye','l','Leu tratamentos e FAQ','2 min 40 s na página · rolou 85% · abriu "Dói?" no FAQ','19/11 · 20:42'),
('send','v','Formulário enviado','Depilação a laser · consentimento LGPD v3 registrado','19/11 · 20:44'),
('refresh','v','Confirmado pelo DocBiz','ID 88231 · conversão enviada ao GA4 e Ads pelo servidor','19/11 · 20:44'),
('wa','b','WhatsApp aberto com a unidade','Mensagem pronta para (11) 94587 2210','19/11 · 20:44'),
('phone','b','1º contato pela recepção','Juliana M. · 7 min depois · SLA cumprido','19/11 · 20:51'),
('cal','v','Avaliação agendada','DocBiz: 22/11 às 15:30 · avaliação gratuita','19/11 · 20:58')]
cont=f'''
<div style="display:flex;align-items:center;gap:6px;color:var(--tinta-3);margin-bottom:12px;font-size:12px">Central de leads {i('chev',12)} Agendado {i('chev',12)} <b style="color:var(--tinta)">Mariana S.</b></div>
<div class="g" style="grid-template-columns:330px 1fr 300px">
 <div class="g" style="align-content:start">
  <div class="card"><div style="display:flex;gap:12px;align-items:center"><span class="av-s" style="width:48px;height:48px;font-size:16px;background:#f3c6e0">MS</span><div><h3 style="font-size:17px">Mariana S.</h3><div class="muted">Lead #L-20931 · criado há 2 dias</div></div></div>
  <div style="display:flex;gap:6px;margin:14px 0"><span class="pill l">{i('cal',11)} Agendado</span><span class="pill v">{i('check',11)} SLA 7 min</span><span class="pill b">Unidade</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="muted" style="width:104px;font-size:12px">{a}</span><b style="flex:1;font-weight:500">{b}</b></div>' for a,b in [('Telefone','(11) 9•••• ••18'),('E-mail','mar•••@•••.com'),('Tratamento','Depilação a laser'),('Unidade','GiO Alto da Lapa'),('Responsável','Juliana M.'),('ID DocBiz','88231')])+f'''</div>
  <div style="display:flex;gap:6px;margin-top:12px"><span class="btn s p">{i('wa',12)} WhatsApp</span><span class="btn s">{i('phone',12)} Ligar</span><span class="btn s">{i('users',12)} Transferir</span></div>
  <div class="muted" style="font-size:11px;margin-top:10px">{i('lock',11)} Dados mascarados. Ver completo fica registrado na auditoria.</div></div>
  <div class="card"><div class="hd"><h3>Atribuição</h3><span class="sub" style="margin-left:auto">último clique não direto</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it" style="padding:7px 0"><span class="muted" style="width:104px;font-size:12px">{a}</span><code style="font-size:12px;color:var(--roxo-700)">{b}</code></div>' for a,b in [('utm_source','google'),('utm_medium','cpc'),('utm_campaign','laser_sp_zona_oeste'),('utm_term','depilacao a laser lapa'),('gclid','Cj0KCQ…x8w'),('Página','template B · bloco hero')])+f'''</div></div>
 </div>
 <div class="card"><div class="hd"><h3>Jornada do lead</h3><div class="dir"><span class="sw"><span class="on">Tudo</span><span>Site</span><span>Atendimento</span></span></div></div>
  <div style="position:relative;padding-left:6px">'''+''.join(f'''<div style="display:flex;gap:14px;position:relative;padding-bottom:{0 if n==len(jornada)-1 else 18}px">{'' if n==len(jornada)-1 else '<span style="position:absolute;left:15px;top:34px;bottom:0;width:2px;background:var(--linha)"></span>'}<div class="ic {c}" style="border-radius:50%;position:relative">{i(ic,15)}</div><div style="flex:1;padding-top:2px"><div style="display:flex;justify-content:space-between"><b>{t}</b><span class="muted" style="font-size:12px">{d}</span></div><div class="muted" style="font-size:12px;margin-top:2px">{s}</div></div></div>''' for n,(ic,c,t,s,d) in enumerate(jornada))+f'''</div>
  <div class="sep"></div>
  <div style="display:flex;gap:10px;align-items:center"><div class="in" style="flex:1;border:1px solid var(--linha);border-radius:10px;padding:10px 12px;color:var(--tinta-3)">Adicionar nota interna para a unidade e o call center…</div><span class="btn p">{i('send',14)} Salvar nota</span></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card" style="background:var(--grad);color:#fff;border:0"><div style="font-size:12px;opacity:.8">Próximo passo</div><div class="pop" style="font-size:18px;font-weight:600;margin:4px 0">Avaliação sáb. 22/11 · 15:30</div><div style="font-size:12px;opacity:.85">Lembrete por WhatsApp sai 24 h antes, se a unidade ativou.</div></div>
  <div class="card"><div class="hd"><h3>Status no DocBiz</h3><span class="pill v" style="margin-left:auto">{i('refresh',11)} há 4 min</span></div>
  '''+''.join(f'<div style="display:flex;align-items:center;gap:10px;padding:6px 0"><span style="width:16px;height:16px;border-radius:50%;{"background:var(--vinho)" if ok else "border:2px solid var(--linha)"};display:grid;place-items:center;color:#fff">{i("check",10) if ok else ""}</span><span style="{"" if ok else "color:var(--tinta-3)"}">{t}</span></div>' for t,ok in [('Recebido',True),('Contatado',True),('Agendado',True),('Compareceu',False),('Fechou pacote',False)])+f'''</div>
  <div class="card"><div class="hd"><h3>{i('shield',15)} Consentimento</h3></div><div class="muted" style="font-size:12px;line-height:1.6">Aceite do aviso de privacidade v3 em 19/11 às 20:44, IP e página registrados. Marketing por WhatsApp: <b style="color:var(--verde)">sim</b>. Retenção até 19/11/2028.</div><span class="btn s" style="margin-top:10px">Ver registro</span></div>
 </div>
</div>'''
salvar('08-lead-detalhe',pagina('Lead',app('admin','leads',cont)))
print('p2 ok')
