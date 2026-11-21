from base import *
random.seed(7)
A=DEMO['altodalapa']
def tabs_unid(ativa):
    prim=[('dados','Dados','',L('unidade')),('hor','Horários','',L('unidade')),('trat','Tratamentos','6 de 12',L('unidade')),('fotos','Fotos','8',L('f-fotos')),('lp','Landing pages','4',L('lp')),('seo','SEO e Google','1',L('seo')),('leads','Leads','41',L('leadslista'))]
    h=''.join(f'<a href="{u}" class="{"on" if k==ativa else ""}">{t}{f" <span class=n>{n}</span>" if n else ""}</a>' for k,t,n,u in prim)
    return f'<div class="tabs tabs-u" style="padding:0 18px;margin:0">{h}<a>Mais {i("chevd",12)}</a><a style="margin-left:auto;align-self:center;white-space:nowrap" class="lk" href="{L("modelos")}">Menu: Padrão rede v3</a></div>'
def cab_unid(ativa,acoes=None):
    acoes=acoes or f'<a class="btn" href="{L("lpB")}">{i("eye",14)} Ver página</a><a class="btn" href="{L("f-inicio")}">{i("users",14)} Ver como unidade</a><span class="btn p">{i("check",14)} Salvar alterações</span>'
    return f'''<div class="migalha"><a href="{L('unidades')}">Unidades</a> {i('chev',12)} <a>São Paulo</a> {i('chev',12)} <b style="color:var(--tinta)">{A['nome']}</b></div>
<div class="card" style="padding:0;overflow:hidden;margin-bottom:16px">
 <div style="height:110px;background:url(../assets/fotos/recepcao.jpg) center 45%/cover;position:relative"><div style="position:absolute;inset:0;background:linear-gradient(90deg,rgba(76,20,85,.75),rgba(176,25,126,.35))"></div></div>
 <div style="display:flex;align-items:flex-start;gap:18px;padding:0 24px 16px;position:relative">
  <div style="flex:none;margin-top:-40px;width:92px;height:92px;border-radius:20px;border:4px solid #fff;background:url(../assets/fotos/fachada.jpg) center/cover;box-shadow:var(--sombra)"></div>
  <div style="padding-top:14px;min-width:0"><div style="display:flex;gap:8px;align-items:center;flex-wrap:wrap"><h1 style="font-size:22px;font-weight:600;white-space:nowrap">{A['nome']}</h1><span class="pill v"><i></i>Ativa</span><span class="pill l">Modelo B · Vitrine</span></div>
  <div class="muted" style="margin-top:4px">{i('pin',13)} {A['end']} · {A['bairro']} · {A['cidade']}/{A['uf']}</div><div class="meta">ID DocBiz 4127 · Regional São Paulo Capital</div></div>
  <div style="margin-left:auto;display:flex;gap:8px;padding-top:16px">{acoes}</div>
 </div>{tabs_unid(ativa)}</div>'''

# ---------- 07 DETALHE DA UNIDADE (rede edita direto, com motivo e aviso) ----------
check=[('v','Endereço e coordenadas'),('v','Telefone e WhatsApp'),('v','Horários'),('a','Tratamentos: 6 de 12 publicados'),('v','8 fotos distintas'),('a','FAQ local: 3 de 6'),('v','Equipe: 2 profissionais'),('r','Google diverge no telefone')]
cont=cab_unid('dados')+f'''
<div class="aviso a" style="margin-bottom:16px"><div>{i('shield',18)}</div><div style="flex:1"><b>Você está editando como rede (Marketing)</b><div style="font-size:13px;margin-top:2px">Pode alterar qualquer campo da ficha. Cada alteração pede um motivo, fica na auditoria e a unidade recebe um aviso com o antes e o depois. Campos marcados como Rede a unidade não altera.</div></div><a class="lk" href="{L('aud')}">Histórico desta unidade</a></div>
<div class="leg" style="margin-bottom:14px"><span><span class="pill t">{i('lock',11)} Rede</span> a unidade não altera</span><span><span class="pill ea">{i('shield',11)} Com aprovação</span> a unidade pede, a rede revisa</span><span><span class="pill e">{i('edit',11)} Editável</span> a unidade muda na hora</span><span><span class="pill z">{i('eye',11)} Somente leitura</span></span></div>
<div class="g" style="grid-template-columns:1fr 360px">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Identificação</h3><span class="sub" style="margin-left:auto">Política de campos v1.1</span></div>
   <div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:14px">{campo('Nome público',A['nome'],'T')}{campo('Endereço da ficha','/unidade/altodalapa/','T')}{campo('ID DocBiz','4127','T','Sincronizado há 6 min')}
   {campo('Razão social','Clínica Demonstração Ltda.','T')}{campo('CNPJ',A['cnpj'],'T')}{campo('Tipo de clínica','Full · laser e estética','T')}</div></div>
  <div class="card"><div class="hd"><h3>Contato e endereço</h3><span class="pill a" style="margin-left:auto">{i('google',11)} Telefone diverge do Google</span></div>
   <div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:14px">{campo('Telefone fixo',A['tel'],'EA','Troca passa pelo SEO; usado no schema e comparado com o Google','phone')}{campo('WhatsApp de atendimento',A['wa'],'E','Recebe o lead com mensagem pronta','wa')}{campo('E-mail da unidade',A['email'],'E','','mail')}
   {campo('CEP',A['cep'],'T')}{campo('Endereço',A['end'],'T','Mudança de endereço é por chamado')}{campo('Bairro',A['bairro'],'T')}</div></div>
  <div class="card" style="border:2px solid var(--vinho)"><div class="hd"><h3>{i('edit',16)} Alteração da rede em andamento</h3><span class="pill l" style="margin-left:auto">rascunho</span></div>
   <div class="g" style="grid-template-columns:1fr 1fr;gap:14px">
    {campo('Sábado · antes','9h às 15h','L')}{campo('Sábado · depois','9h às 17h','E')}
    <div class="campo"><label>Motivo (obrigatório)</label><div class="in">Campanha de fim de ano: horário estendido aos sábados {i('chevd',13)}</div></div>
    <div class="campo"><label>Detalhe para a unidade</label><div class="in" style="color:var(--tinta-2)">Vale de 22/11 a 20/12. Escala combinada no comitê.</div></div>
   </div>
   <div class="aviso l" style="margin-top:14px"><div>{i('bell',16)}</div><div style="font-size:13px"><b>A unidade será avisada</b> por e-mail e no portal assim que você salvar. Ela pode contestar em até 7 dias (decisão D7); a alteração vale enquanto isso.</div></div>
  </div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Completude da página</h3><b class="pop" style="margin-left:auto;font-size:22px">90%</b></div>
   <div class="lista-i">'''+''.join(f'<div class="it" style="padding:7px 0"><div class="ic {c}" style="width:26px;height:26px">{i("check" if c=="v" else "alert",13)}</div><span style="flex:1">{t}</span></div>' for c,t in check)+f'''</div></div>
  <div class="card"><div class="hd"><h3>{i('google',15)} Ficha x perfil do Google</h3></div>
   <p class="meta" style="margin:-6px 0 10px">O perfil do Google é da unidade. O sistema só compara e avisa; a correção é feita pela unidade no próprio Google.</p>
   <table class="t" style="font-size:13px"><thead><tr><th>Campo</th><th>Situação</th></tr></thead><tbody>
   <tr><td>Nome</td><td><span class="pill v">igual</span></td></tr><tr><td>Endereço</td><td><span class="pill v">igual</span></td></tr><tr><td>Telefone</td><td><span class="pill a">diverge</span></td></tr><tr><td>Site</td><td><span class="pill r">outra URL</span></td></tr></tbody></table>
   <a class="btn s" href="{L('seo')}" style="margin-top:12px">Ver comparação completa</a></div>
  <div class="card"><div class="hd"><h3>{i('target',15)} Dados estruturados e SEO</h3><span class="pill t" style="margin-left:auto">{i('lock',11)} Rede</span></div>
   <div class="lista-i" style="font-size:13px"><div class="it" style="padding:6px 0"><span style="flex:1">Schema base</span><b>MedicalClinic + BeautySalon</b></div><div class="it" style="padding:6px 0"><span style="flex:1">FAQPage</span><b>ativo · 3 perguntas</b></div><div class="it" style="padding:6px 0"><span style="flex:1">URL canônica</span><b>{A['dom']}</b></div></div></div>
 </div>
</div>'''
salvar(ARQ['unidade'],pagina('Unidade',app('admin','unidades',cont)))

# ---------- 08 LANDING PAGES E VARIANTES DA UNIDADE ----------
var=[('Principal','Modelo B · Vitrine','v','Publicada',f'{A["dom"]}/','Indexável','2.140','30','1,4%'),
('Teste A/B','Hero vídeo x foto','b','Em teste · 50/50',f'{A["dom"]}/','Mesma URL','1.068','24','2,2%'),
('Campanha','Fim de ano · laser','a','Agendada 22/11',f'{A["dom"]}/fim-de-ano','noindex, canônica','','',''),
('Serviço','Depilação a laser','v','Publicada',f'{A["dom"]}/depilacao-a-laser','Indexável','612','11','1,8%'),
('Serviço','Limpeza de pele','a','Em aprovação',f'{A["dom"]}/limpeza-de-pele','Indexável','','','')]
linhas=''.join(f'<tr><td><span class="pill {"l" if t=="Principal" else "z"}">{t}</span></td><td><b>{n}</b></td><td><span class="pill {c}">{st}</span></td><td><span class="trunc" style="display:block;max-width:190px;color:var(--azul)">{u}</span></td><td class="meta">{ix}</td><td class="num">{v or "sem dados"}</td><td class="num">{l or "sem dados"}</td><td class="num"><b>{cv or "sem dados"}</b></td><td>{i("more",16)}</td></tr>' for t,n,c,st,u,ix,v,l,cv in var)
ab_a=[1.6,1.8,1.7,2.0,1.9,2.1,1.8,2.0,1.9,2.0,1.9,1.9,2.0,1.9]; ab_b=[1.7,2.0,2.1,2.3,2.2,2.4,2.1,2.3,2.2,2.3,2.2,2.3,2.4,2.2]
cont=cab_unid('lp',f'<a class="btn" href="{L("f-ab")}">{i("layout",14)} Comparar modelos</a><span class="btn p">{i("plus",14)} Nova variante</span>')+f'''
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">
 {kpi('globe','Visitas 30d','2.752','principal 2.140 + serviço 612')}{kpi('inbox','Leads 30d','41','igual ao total da unidade')}{kpi('target','Conversão média','1,5%','<span class="up">+0,3 p.p.</span> vs. outubro')}{kpi('zap','Testes ativos','1','encerra com 95% de confiança')}
</div>
<div class="card" style="padding:0;margin-bottom:16px">
 <div class="hd" style="padding:16px 18px 0"><h3>Variantes da unidade</h3><span class="sub">regras de indexação aplicadas pela rede</span><div class="dir"><span class="chip on">Todas · 5</span><span class="chip">Publicadas · 3</span><span class="chip">Em aprovação · 1</span></div></div>
 <table class="t"><thead><tr><th>Tipo</th><th>Variante</th><th>Status</th><th>URL</th><th>Indexação</th><th class="num">Visitas</th><th class="num">Leads</th><th class="num">Conv.</th><th></th></tr></thead><tbody>{linhas}</tbody></table>
 <p class="meta" style="padding:10px 18px 14px">Visitas e leads somam só variantes com tráfego no período: principal 30 leads (já inclui as duas versões do teste) + serviço 11 = 41, o mesmo total da aba Leads.</p>
</div>
<div class="g" style="grid-template-columns:1.4fr 1fr">
 <div class="card"><div class="hd"><h3>Teste A/B · conversão diária</h3><div class="leg" style="margin-left:12px"><span><i style="background:#4c1455"></i>A · foto da fachada</span><span><i style="background:#b0197e"></i>B · vídeo</span></div><span class="pill b" style="margin-left:auto">confiança 88%</span></div>
 {area([ab_a,ab_b],['#4c1455','#b0197e'],w=620,h=200,labels=[f'{d:02d}/11' for d in range(8,22)],ymax=3)}</div>
 <div class="card"><div class="hd"><h3>Regras desta seção</h3></div>
  <div class="lista-i" style="font-size:13px">
   <div class="it"><div class="ic l">{i('globe',14)}</div><div><b>Campanha</b><div class="meta">URL própria, noindex e canônica para a principal. Expira na data final.</div></div></div>
   <div class="it"><div class="ic l">{i('zap',14)}</div><div><b>Teste A/B</b><div class="meta">Mesma URL, divisão de tráfego no servidor, sem conteúdo duplicado.</div></div></div>
   <div class="it"><div class="ic l">{i('target',14)}</div><div><b>Serviço</b><div class="meta">Indexável, com schema de serviço e FAQ próprio. Aprovação da rede.</div></div></div>
  </div></div>
</div>'''
salvar(ARQ['lp'],pagina('Landing pages da unidade',app('admin','unidades',cont),extra_css='table.t td,table.t th{padding-left:10px;padding-right:10px}'))

# ---------- 09 APROVAÇÕES ----------
fila=[('Banner de dezembro (fora do modelo)','GiO Batel','Carla T.','há 2 h','a','vence em 6 h',True),('Troca de modelo C para B','GiO Aldeota','Marcos P.','há 5 h','a','vence em 3 h',False),('Telefone fixo','GiO Cambuí','Paulo M.','há 1 dia','r','venceu há 2 h',False),('Registro profissional da equipe','GiO Salvador','Ana C.','há 1 dia','v','vence em 30 h',False),('Variante de serviço: limpeza de pele','GiO Alto da Lapa','Renata F.','há 2 dias','v','vence em 22 h',False),('Fotos de antes e depois','GiO Bom Fim','Lúcia A.','há 2 dias','v','vence em 20 h',False),('Telefone fixo','GiO Asa Sul','Diego R.','há 3 dias','v','vence em 12 h',False)]
cont=f'''
<div class="cab"><div><h1>Aprovações</h1><p>Campos com aprovação (EA) enviados pelas unidades. SLA de 48 h úteis. Campos editáveis publicam na hora e vão para Revisão posterior.</p></div>
<div class="dir"><span class="btn">{i('gear',14)} Regras de aprovação</span></div></div>
<div class="g" style="grid-template-columns:440px 1fr">
 <div class="card" style="padding:0">
  <div style="display:flex;gap:6px;padding:14px 16px;flex-wrap:wrap;border-bottom:1px solid var(--linha)"><span class="chip on">Pendentes · 7</span><span class="chip">{i('clock',13)} SLA vencido · 1</span><span class="chip">Vence hoje · 2</span><span class="chip">Revisão posterior · 12</span></div>
  <div>'''+''.join(f'<div style="display:flex;gap:12px;padding:12px 16px;border-bottom:1px solid var(--linha);{"background:#fbf3f8;border-left:3px solid var(--vinho)" if sel else ""}"><div style="flex:1;min-width:0"><b class="trunc" style="display:block">{t}</b><div class="meta">{u} · {p} · {q}</div></div><span class="pill {c}" style="align-self:center">{sla}</span></div>' for t,u,p,q,c,sla,sel in fila)+f'''</div>
  <p class="meta" style="padding:12px 16px">7 itens · ordenados por prazo do SLA</p>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><div><h3>Banner de dezembro · GiO Batel</h3><div class="meta">Enviado por Carla T. (admin da unidade) há 2 h · item 34 da política (promoção fora do modelo), aprova Marketing</div></div><span class="pill a" style="margin-left:auto">vence em 6 h</span></div>
   <div class="g" style="grid-template-columns:1fr 1fr">
    <div><div class="meta" style="font-weight:600;margin-bottom:6px">ANTES (publicado)</div><div style="background:var(--lilas-50);border:1px solid var(--linha);border-radius:12px;padding:14px;color:var(--tinta-2)">Promoção do modelo da rede: avaliação gratuita em depilação a laser, válida até 30/11.</div></div>
    <div><div class="meta" style="font-weight:600;margin-bottom:6px">DEPOIS (proposto)</div><div style="background:#fff;border:1px solid var(--linha-forte);border-radius:12px;padding:14px">Dezembro na GiO Batel: avaliação gratuita e <mark style="background:#fdf1dc">condição especial</mark> no pacote de axilas para quem agendar até o Natal.</div></div>
   </div>
   <div class="aviso l" style="margin-top:14px"><div>{i('sparkle',16)}</div><div style="font-size:13px"><b>Checagem automática:</b> sem preço e sem promessa de resultado. "Condição especial" sem descrição e sem data final exata; a regra da rede pede validade explícita.</div></div>
   <div style="display:flex;gap:8px;margin-top:16px"><span class="btn p">{i('check',14)} Aprovar e publicar</span><span class="btn">{i('edit',14)} Aprovar com ajuste</span><span class="btn perigo">Devolver com nota</span></div>
  </div>
  <div class="g" style="grid-template-columns:1fr 1fr">
   <div class="card"><div class="meta" style="font-weight:600;margin-bottom:8px">ESTADO · DEVOLVER COM NOTA</div>
    <div class="campo"><label>Nota para a unidade (obrigatória)</label><div class="in" style="min-height:70px;align-items:flex-start">Gostamos da ideia. Descreva a condição e coloque a data final (ex.: até 24/12) e reenviamos para publicar.</div></div>
    <div style="display:flex;gap:8px;margin-top:10px"><span class="btn s perigo">Devolver</span><span class="btn s ghost">Cancelar</span></div></div>
   <div class="card vazio"><div class="ilu">{i('check',34)}</div><b style="font-size:16px">Fila zerada</b><p class="meta" style="margin-top:4px">Estado quando não há pendências. Novos envios chegam por notificação.</p></div>
  </div>
 </div>
</div>'''
salvar(ARQ['aprov'],pagina('Aprovações',app('admin','aprov',cont)))

# ---------- 10 KANBAN DE LEADS ----------
nomes=['Mariana S.','Juliana P.','Fernanda L.','Camila R.','Beatriz M.','Larissa C.','Patrícia O.','Aline G.','Renata V.','Tatiane B.','Luana F.','Gabriela N.','Débora K.','Vanessa T.','Priscila A.','Carolina D.','Natália E.','Sabrina H.','Bruna I.','Elaine J.']
trat=['Depilação a laser','Limpeza de pele','Ultraformer','Depilação a laser','Peeling','Criolipólise']
cols=[('Novo',38,'l'),('Em contato',24,'b'),('Agendado',31,'a'),('Compareceu',19,'v'),('Não converteu',12,'z')]
def cartao(n,u,t,q,sla=None):
    return f'<a class="card" href="{L("lead")}" style="padding:12px;display:block;box-shadow:none"><div style="display:flex;gap:8px;align-items:center"><span class="av-s">{n[0]}{n.split()[1][0]}</span><b>{n}</b>{f"<span class=\"pill r\" style=\"margin-left:auto\">{sla}</span>" if sla else ""}</div><div class="meta" style="margin-top:6px">{t} · {u}</div><div class="meta" style="margin-top:2px">{i("clock",11)} {q}</div></a>'
un=['Alto da Lapa','Batel','Cambuí','Tatuapé','Bom Fim','Aldeota']
k=0; colh=''
for nome,tot,c in cols:
    cards=''
    for j in range(4):
        cards+=cartao(nomes[k%20],un[k%6],trat[k%6],['há 4 min','há 12 min','há 38 min','há 1 h','ontem'][j%5],'SLA' if (nome=='Novo' and j==2) else None); k+=1
    colh+=f'<div style="background:#f1ebf4;border-radius:14px;padding:10px;display:flex;flex-direction:column;gap:8px;min-width:0"><div style="display:flex;align-items:center;gap:8px;padding:4px 4px 6px"><span class="pill {c}">{nome}</span><b style="margin-left:auto">{tot}</b></div>{cards}<a class="btn s ghost" href="{L("leadslista")}">Ver mais {tot-4}</a></div>'
cont=f'''
<div class="cab"><div><h1>Central de leads</h1><p>124 leads em aberto ou recentes na rede. Novos aparecem no topo de cada coluna.</p></div>
<div class="dir">{periodo()}<span class="sw"><a class="on" href="{L('leads')}">Quadro</a><a href="{L('leadslista')}">Lista</a></span><span class="btn p">{i('down',14)} Exportar</span></div></div>
<div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap"><span class="chip">Unidade: <b>Todas</b> {i('chevd',12)}</span><span class="chip">Origem {i('chevd',12)}</span><span class="chip">Tratamento {i('chevd',12)}</span><span class="chip">{i('clock',13)} Só fora do SLA · 9</span><span class="meta" style="align-self:center;margin-left:auto">Totais: 38 + 24 + 31 + 19 + 12 = 124</span></div>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:12px">{colh}</div>'''
salvar(ARQ['leads'],pagina('Central de leads',app('admin','leads',cont)))

# ---------- 11 LISTA DE LEADS ----------
st=[('Novo','l'),('Em contato','b'),('Agendado','a'),('Compareceu','v'),('Não converteu','z')]
orig=['Google Ads','Orgânico','Meta Ads','Instagram','Direto']
linhas=''
for j in range(12):
    s,c=st[j%5]; sel=j in (0,3)
    linhas+=f'<tr class="{"sel" if sel else ""}"><td><span class="cx{" on" if sel else ""}"></span></td><td><a class="un" href="{L("lead")}"><span class="av-s">{nomes[j][0]}{nomes[j].split()[1][0]}</span><b>{nomes[j]}</b></a></td><td class="meta">(11) 9••••-••{10+j}</td><td>GiO {un[j%6]}</td><td>{trat[j%6]}</td><td><span class="trunc" style="display:block;max-width:110px">{orig[j%5]}</span></td><td><span class="pill {c}">{s}</span></td><td class="meta">{["há 4 min","há 12 min","há 38 min","há 1 h","há 3 h","ontem"][j%6]}</td><td>{"<span class=\"pill r\">fora do SLA</span>" if j in (2,7) else "<span class=\"meta\">no prazo</span>"}</td></tr>'
cont=f'''
<div class="cab"><div><h1>Central de leads</h1><p>Mesma base do quadro, em lista. 124 leads no período.</p></div>
<div class="dir">{periodo()}<span class="sw"><a href="{L('leads')}">Quadro</a><a class="on" href="{L('leadslista')}">Lista</a></span><span class="btn p">{i('down',14)} Exportar</span></div></div>
<div class="aviso l" style="margin-bottom:14px"><div>{i('lock',16)}</div><div style="font-size:13px">Seu perfil (Marketing da rede) vê telefone mascarado. Dados completos aparecem para call center e unidade, e cada abertura fica na auditoria. A rede é a controladora dos dados.</div></div>
<div class="card" style="padding:0">
 <div class="tb-bulk"><b>2 selecionados</b><span class="btn s">{i('users',13)} Atribuir</span><span class="btn s">{i('tag',13)} Mudar status</span><span class="btn s">{i('down',13)} Exportar sem dados pessoais</span></div>
 <table class="t"><thead><tr><th><span class="cx"></span></th><th>Nome</th><th>Telefone</th><th>Unidade</th><th>Tratamento</th><th>Origem</th><th>Status</th><th>Entrada</th><th>SLA</th></tr></thead><tbody>{linhas}</tbody></table>
 <div style="display:flex;align-items:center;padding:12px 16px;border-top:1px solid var(--linha)" class="muted"><span>12 de 124 · Novo 38 · Em contato 24 · Agendado 31 · Compareceu 19 · Não converteu 12</span><span style="margin-left:auto;display:flex;gap:6px"><span class="btn s">Anterior</span><span class="btn s">Próxima</span></span></div>
</div>'''
salvar(ARQ['leadslista'],pagina('Leads em lista',app('admin','leads',cont)))

# ---------- 12 DETALHE DO LEAD ----------
hist=[('Recebido pelo formulário da página','19/11 · 20:44','inbox'),('WhatsApp enviado pela unidade (botão)','19/11 · 20:51','wa'),('Ligação do call center · atendeu','20/11 · 09:12','phone'),('Agendado no DocBiz: avaliação','20/11 · 09:15','cal')]
cont=f'''
<div class="migalha"><a href="{L('leads')}">Central de leads</a> {i('chev',12)} <b style="color:var(--tinta)">Mariana S.</b></div>
<div class="cab"><div style="display:flex;gap:14px;align-items:center"><span class="av-s" style="width:52px;height:52px;font-size:18px">MS</span><div><h1>Mariana S.</h1><p>Lead de {A['nome']} · Depilação a laser · Google Ads</p></div></div>
<div class="dir"><span class="pill a" style="padding:6px 12px">Agendado</span><span class="btn">{i('wa',14)} WhatsApp</span><span class="btn">{i('phone',14)} Ligar</span><span class="btn p">{i('tag',14)} Mudar status</span></div></div>
<div class="g" style="grid-template-columns:1fr 360px">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Dados do lead</h3><span class="sub" style="margin-left:auto">{i('eye',12)} abertura registrada na auditoria</span></div>
   <div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:14px">{campo('Nome','Mariana S.','L')}{campo('Telefone','(11) 9••••-••10','L','Dado completo só para call center e unidade')}{campo('E-mail','m•••••@exemplo.com','L')}
   {campo('Tratamento','Depilação a laser','E')}{campo('Unidade',A['nome'],'E','Telefone da unidade: '+A['tel'])}{campo('Origem','Google Ads · campanha laser SP','L')}</div></div>
  <div class="card"><div class="hd"><h3>Linha do tempo</h3></div>
   <div class="lista-i">'''+''.join(f'<div class="it"><div class="ic l">{i(ic,15)}</div><div style="flex:1"><b>{t}</b><div class="meta">{q}</div></div></div>' for t,q,ic in hist)+f'''</div>
   <div class="aviso l" style="margin-top:12px"><div>{i('log',16)}</div><div style="font-size:13px">Ao tocar em Ligar ou WhatsApp o sistema registra quem acessou o contato e quando. Nada é exportado.</div></div>
  </div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card" style="background:var(--grad);color:#fff;border:0"><div style="font-size:13px">Próximo passo</div><div class="pop" style="font-size:18px;font-weight:600;margin:4px 0">Avaliação sáb. 22/11 · 15:30</div><div style="font-size:13px">Lembrete por WhatsApp 24 h antes, se a unidade ativou.</div></div>
  <div class="card"><div class="hd"><h3>Status no DocBiz</h3><span class="pill v" style="margin-left:auto">{i('refresh',11)} há 4 min</span></div>'''+''.join(f'<div style="display:flex;align-items:center;gap:10px;padding:6px 0"><span style="width:18px;height:18px;border-radius:50%;{"background:var(--vinho);color:#fff" if ok else "border:2px solid var(--linha-forte)"};display:grid;place-items:center">{i("check",10) if ok else ""}</span><span style="{"" if ok else "color:var(--tinta-3)"}">{t}</span></div>' for t,ok in [('Recebido',True),('Em contato',True),('Agendado',True),('Compareceu',False),('Não converteu',False)])+f'''</div>
  <div class="card"><div class="hd"><h3>{i('shield',15)} Consentimento</h3></div><div class="meta" style="line-height:1.6">Aceite do aviso de privacidade v3 em 19/11 às 20:44, página e data registradas. Marketing por WhatsApp: <b style="color:var(--verde)">sim</b>. Retenção até 19/11/2028, depois anonimização.</div><a class="btn s" href="{L('lgpd')}" style="margin-top:10px">Ver registro LGPD</a></div>
 </div>
</div>'''
salvar(ARQ['lead'],pagina('Lead',app('admin','leads',cont)))
print('s2 ok')
