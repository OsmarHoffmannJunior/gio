"""Rodada 3: painel da unidade e da rede para a área do cliente (spec 002), telas 53 a 62. Dados fictícios."""
from base import *
A=DEMO['altodalapa']
def F(ativo,c): return app('franq',ativo,c)
def R(ativo,c): return app('admin',ativo,c)
LOCK=lambda t='Rede': f'<span class="pill t">{i("lock",11)} {t}</span>'
TABS_VENDAS=[('Procedimentos e preços','f-procs'),('Promoções','f-promos'),('Pacotes · fase 2',None)]
def liberou():
    it=[('v','Promoções','Liberada · dentro dos modelos da rede'),('v','Campanhas para clientes',f'Liberada na Regional SP · {COTA_UN} por mês'),('v','Canal WhatsApp','Liberado · 1 mensagem por semana por cliente'),('v','Tags da unidade','GA4 próprio com aprovação (domínio próprio)'),
        ('r','Preço por procedimento','Bloqueado · política de preço da rede'),('r','Procedimentos locais','Bloqueado'),('r','Quiz da unidade','Bloqueado · fase 1 só modelos da rede'),('r','Exportar clientes','Bloqueado')]
    return f'''<div class="card"><div class="hd"><h3>{i('key',16)} O que a rede liberou</h3></div><div class="lista-i" style="font-size:13px">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="ic {c}" style="width:28px;height:28px">{i("check" if c=="v" else "lock",13)}</span><div><b>{t}</b><div class="meta">{d}</div></div></div>' for c,t,d in it)+f'''</div><a class="btn s" href="{L('suporte')}" style="margin-top:10px">Pedir liberação</a></div>'''

# ---------- 53 PROCEDIMENTOS E PREÇOS (U03) ----------
pr=[('Depilação a laser',True,'30 min','Só logado','EA','Aprovado'),('Limpeza de pele',True,'60 min','Só logado','EA','Pedir'),('Ultraformer',True,'45 min','Só logado','EA','Pedir'),('Peeling',True,'40 min','Só logado','EA','Pedir'),
    ('Criolipólise',True,'60 min','Só logado','EA','Pedir'),('Microagulhamento',True,'50 min','Só logado','EA','Pedir'),('Toxina',False,'sem dados','Oculto','','Bloqueado'),('Preenchimento',False,'sem dados','Oculto','','Bloqueado')]
c=cabec('Procedimentos e promoções','O que a sua unidade oferece aos clientes, dentro do que a rede liberou.',f'<a class="btn" href="{L("lpB")}">{i("eye",14)} Ver na página</a><span class="btn p">{i("check",14)} Salvar</span>')+tabs(TABS_VENDAS,0)+f'''
<div class="g" style="grid-template-columns:1fr 330px;align-items:start">
<div class="card" style="padding:0;overflow:hidden"><div style="padding:14px 18px;display:flex;align-items:center;gap:10px"><b>6 de 12 do catálogo da rede ativos</b><span class="meta">Preço público: não exibido (política da rede, decisão D1 pendente com o grupo)</span></div>
<table class="t" style="table-layout:fixed"><thead><tr><th style="width:190px">Procedimento</th><th style="width:90px">Ativo</th><th style="width:120px">Duração local</th><th style="width:130px">Preço</th><th style="width:130px">Visibilidade</th><th>Venda online</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{n}</b></td><td><span class="tog{" on" if a else ""}" data-toggle="1"></span></td><td>{d if a else "<span class=meta>sem dados</span>"}</td><td>{LOCK()}</td><td><span class="pill {"l" if a else "z"}">{v}</span></td><td>{("<span class=\"pill v\">"+i("check",11)+" aprovado</span>") if o=="Aprovado" else (f"<a class=\"btn s\" href=\"{L("suporte")}\">{i("shield",12)} Pedir</a>" if o=="Pedir" else LOCK("Bloqueado"))}</td></tr>' for n,a,d,v,e,o in pr)+f'''</tbody></table>
<div class="meta" style="padding:12px 18px">Mostrando 8 de 12. Duração local é editável; preço e procedimentos locais dependem de liberação da rede.</div></div>
{liberou()}</div>'''
salvar(ARQ['f-procs'],pagina('Procedimentos e preços',F('f-procs',c)))

# ---------- 54 PROMOÇÕES (U05) ----------
pm=[('Limpeza de pele de verão','Condição em pacote','01/12 a 15/12','v','No ar','Com aprovação · aprovada em 19/11'),('Semana do Ultraformer','Avaliação gratuita','01/12 a 07/12','a','Em aprovação','Enviada há 2 h · SLA 48 h'),('Avaliação gratuita de laser','Promoção da rede','até 30/11','l','Aderiu','Adesão em 05/11')]
c=cabec('Procedimentos e promoções','Crie promoções a partir dos modelos da rede ou participe das promoções nacionais.',f'<span class="btn p" data-sem-rota="1">{i("plus",14)} Nova promoção</span>')+tabs(TABS_VENDAS,1)+f'''
<div class="g" style="grid-template-columns:1fr 330px;align-items:start"><div class="g">
<div class="card" style="padding:0;overflow:hidden"><table class="t"><thead><tr><th>Promoção</th><th>Modelo</th><th>Período</th><th>Situação</th><th>Detalhe</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{n}</b></td><td>{m}</td><td>{p}</td><td><span class="pill {cl}">{s}</span></td><td class="meta" style="white-space:normal">{d}</td></tr>' for n,m,p,cl,s,d in pm)+f'''</tbody></table></div>
<div class="card"><div class="hd"><h3>{i('flag',16)} Promoções da rede abertas para adesão</h3></div>
<div class="aviso l"><div>{i('sparkle',18)}</div><div style="flex:1"><b>Black November da rede</b><div class="meta">Avaliação gratuita em todos os procedimentos faciais · adesão opcional até 25/11 · regulamento da rede</div></div><span class="btn s p" data-sem-rota="1">Aderir</span></div></div>
<div class="card"><div class="hd"><h3>Criar a partir de um modelo</h3></div><div class="g" style="grid-template-columns:repeat(4,1fr)">'''+''.join(f'<div class="card" style="box-shadow:none;padding:14px;{"background:var(--lilas-50)" if lk else ""}"><b>{t}</b><div class="meta" style="margin:4px 0 10px">{d}</div>{"<span class=\"btn s\" data-sem-rota=\"1\">Usar</span>" if not lk else LOCK("Bloqueado")}</div>' for t,d,lk in [('Avaliação gratuita','Sem preço, validade obrigatória',False),('Condição em pacote','Texto validado, com aprovação',False),('Brinde','Sem preço, estoque informado',False),('Percentual','Depende da liberação de preço',True)])+f'''</div></div></div>
{liberou()}</div>'''
salvar(ARQ['f-promos'],pagina('Promoções',F('f-procs',c)))

# ---------- 55 CAMPANHAS DA UNIDADE (U06) ----------
cp=[('Limpeza de pele: lembrete de verão','Rascunho','z','WhatsApp',f'{CAMP_LIMP}','sem dados'),('Semana do Ultraformer','Em aprovação','a','WhatsApp e e-mail',f'{CAMP_ULTRA}','01/12 a 07/12'),('Limpeza de pele de verão','No ar','v','E-mail','652','01/12 a 15/12'),('Volta da primavera','Encerrada','z','WhatsApp','188','01/10 a 10/10')]
c=cabec('Campanhas','Mensagens para os clientes da sua unidade, dentro dos limites da rede.',f'<a class="btn p" href="{L("f-camp")}">{i("plus",14)} Nova campanha</a>')+f'''
<div class="g" style="grid-template-columns:repeat(3,1fr);margin-bottom:16px">
{kpi('send','Campanhas em novembro',f'{COTA_USADA_AL} de {COTA_UN}','Mais 1 em aprovação: se aprovada, a cota fecha')}
{kpi('users','Clientes que você alcança',fmt(CLI_AL),f'{fmt(CONS_AL["WhatsApp"])} com WhatsApp · {fmt(CONS_AL["E-mail"])} com e-mail')}
{kpi('clock','Frequência por cliente','1 por semana','Somando rede e unidade; o sistema pula quem já recebeu')}</div>
<div class="g" style="grid-template-columns:1fr 330px;align-items:start">
<div class="card" style="padding:0;overflow:hidden"><div style="padding:12px 16px;display:flex;gap:8px">'''+''.join(f'<span class="chip{" on" if k==0 else ""}" data-toggle="1">{t} <b>{n}</b></span>' for k,(t,n) in enumerate([('Todas',4),('Rascunho',1),('Em aprovação',1),('No ar',1),('Encerradas',1)]))+f'''</div>
<table class="t"><thead><tr><th>Campanha</th><th>Situação</th><th>Canais</th><th class="num">Alcance</th><th>Período</th></tr></thead><tbody>'''+''.join(f'<tr><td><a class="lk" href="{L("f-camp")}">{n}</a></td><td><span class="pill {cl}">{s}</span></td><td>{ch}</td><td class="num">{a}</td><td>{p}</td></tr>' for n,s,cl,ch,a,p in cp)+f'''</tbody></table></div>
<div class="card"><div class="hd"><h3>{i('copy',16)} Usar campanha da rede</h3></div><div class="lista-i" style="font-size:13px">
<div class="it"><div style="flex:1"><b>Avaliação gratuita de laser</b><div class="meta">Modelo da rede · textos aprovados</div></div><a class="btn s" href="{L("f-camp")}">Usar</a></div>
<div class="it"><div style="flex:1"><b>Aniversário do cliente</b><div class="meta">Modelo da rede · envio automático</div></div><a class="btn s" href="{L("f-camp")}">Usar</a></div></div>
<div class="aviso a" style="margin-top:12px"><div>{i('lock',16)}</div><div style="font-size:13px">Alcance máximo: só clientes da sua unidade. Raio, cidade e base nacional não estão liberados.</div></div></div></div>'''
salvar(ARQ['f-camps'],pagina('Campanhas',F('f-camps',c)))

# ---------- 56 ASSISTENTE DE CAMPANHA (U07), passo 4 alcance ----------
passos=['Objetivo','Oferta','Público','Alcance','Conteúdo','Período','Prévia','Revisão']
fl=funil_un(INT_LIMPEZA)
def stepper(on):
    return '<div class="card passos" style="padding:14px 18px;margin-bottom:16px;display:flex;gap:6px;align-items:center">'+''.join(f'<div class="passo{" on" if k==on else ""}" style="display:flex;align-items:center;gap:6px;flex:1;min-width:0"><span style="width:26px;height:26px;border-radius:50%;display:grid;place-items:center;font:600 12px Inter;flex:none;background:{"var(--verde)" if k<on else ("var(--vinho)" if k==on else "var(--lilas-100)")};color:{"#fff" if k<=on else "var(--roxo-700)"}">{i("check",13) if k<on else k+1}</span><span class="trunc" style="font-size:13px;font-weight:{600 if k==on else 500};color:{"var(--tinta)" if k<=on else "var(--tinta-3)"}">{p}</span></div>' for k,p in enumerate(passos))+'</div>'
opc=[('Clientes da minha unidade',f'{fmt(CLI_AL)} clientes vinculados',True,''),('Raio de 5 km','Acima do limite da unidade',False,'Bloqueado pela rede'),('Cidade de São Paulo','Acima do limite da unidade',False,'Bloqueado pela rede'),('Base nacional','Nunca disponível para unidades',False,'Teto da plataforma')]
c=f'<div class="migalha"><a href="{L("f-camps")}">Campanhas</a>{i("chev",12)}<span>Limpeza de pele: lembrete de verão</span><span class="pill z" style="margin-left:8px">rascunho salvo há 1 min</span></div>'+cabec('Nova campanha','Passo 4 de 8: quem pode receber.',f'<a class="btn" href="{L("f-camps")}">Salvar e sair</a><a class="btn p" href="{L("f-camps")}">Continuar</a>')+stepper(3)+f'''
<div class="g" style="grid-template-columns:1fr 380px;align-items:start">
<div class="card"><div class="hd"><h3>Alcance</h3><span class="meta">a rede define o limite da sua unidade</span></div><div class="g" style="gap:10px">'''+''.join(f'<div style="display:flex;gap:12px;align-items:center;padding:14px;border-radius:12px;border:1px solid {"var(--vinho)" if on else "var(--linha)"};background:{"#fbf3f8" if on else ("#fff" if not lk else "var(--lilas-50)")}"><span style="width:20px;height:20px;border-radius:50%;border:2px solid {"var(--vinho)" if on else "#8f8198"};display:grid;place-items:center;flex:none">{"<span style=\"width:10px;height:10px;border-radius:50%;background:var(--vinho)\"></span>" if on else ""}</span><div style="flex:1"><b>{t}</b><div class="meta">{d}</div></div>{LOCK(lk) if lk else "<span class=\"pill v\">dentro do limite</span>"}</div>' for t,d,on,lk in opc)+f'''</div>
<div class="sep"></div><b>Público escolhido no passo 3</b><div class="meta" style="margin-top:2px">Interesse em Limpeza de pele (cadastro, quiz ou agendamentos) · todas as idades acima de 18</div></div>
<div class="card"><div class="hd"><h3>{i('users',16)} Quem vai receber</h3></div>'''+''.join(f'<div style="display:flex;align-items:center;padding:9px 0;border-bottom:1px dashed var(--linha)"><span style="flex:1;font-size:13px">{t}</span><b style="font-variant-numeric:tabular-nums">{fmt(v)}</b></div>' for t,v in fl)+f'''
<div style="margin-top:12px;padding:12px;border-radius:12px;background:var(--lilas-50)"><div class="meta">Alcance estimado</div><div style="font:600 26px Poppins;color:var(--vinho)">{fmt(fl[-1][1])} clientes</div><div class="meta">Quem já recebeu mensagem da rede ou da unidade nos últimos 7 dias fica de fora.</div></div>
<div class="aviso l" style="margin-top:12px"><div>{i('shield',16)}</div><div style="font-size:13px">Depois da revisão, a campanha vai para aprovação da rede. Ela conta na cota de novembro ({COTA_USADA_AL} de {COTA_UN} usada).</div></div></div></div>'''
salvar(ARQ['f-camp'],pagina('Nova campanha',F('f-camps',c)))

# ---------- 57 TAGS E MEDIÇÃO DA UNIDADE (T11) ----------
c=cabec('Tags e medição','Uma única tag da rede mede a sua página. Você não cola scripts: só preenche os campos liberados.',f'<a class="btn" href="{L("ajuda")}">{i("book",14)} Guia de configuração</a><span class="btn p">{i("check",14)} Enviar para aprovação</span>')+f'''
<div class="card" style="margin-bottom:16px"><div class="hd"><h3>{i('zap',16)} Como os dados chegam</h3><span class="meta">cada evento é coletado uma vez e enviado pelo servidor da rede</span></div>
<div style="display:grid;grid-template-columns:1fr 40px 1.2fr 40px 1.4fr;align-items:center;gap:6px">
<div class="card" style="box-shadow:none;padding:12px;text-align:center"><b>Sua página</b><div class="meta">{A['dom']}</div></div><div style="text-align:center;color:var(--tinta-3)">{i('chev',20)}</div>
<div class="card" style="box-shadow:none;padding:12px;text-align:center;background:var(--lilas-50)"><b>Coletor da rede</b><div class="meta">valida, remove duplicados e grava</div></div><div style="text-align:center;color:var(--tinta-3)">{i('chev',20)}</div>
<div class="g" style="gap:6px"><div class="pill v" style="justify-content:flex-start">{i('check',11)} Analytics da rede (sempre)</div><div class="pill v" style="justify-content:flex-start">{i('check',11)} Seu Analytics (cópia dos mesmos eventos)</div><div class="pill z" style="justify-content:flex-start">{i('lock',11)} Meta, Google Ads, TikTok (bloqueados)</div></div></div>
<p class="meta" style="margin-top:10px">Você e a rede veem os mesmos números, sem duplicar scripts: a página carrega só a tag da rede e o servidor faz a cópia para o seu Analytics.</p></div>
<div class="g" style="grid-template-columns:1fr 1fr 330px;align-items:start">
<div class="card"><div class="hd"><h3>Google</h3></div><div class="g" style="gap:12px">
{campo('ID de medição do seu Analytics','G-DEMO12345','EA','Aprovado em 18/11 · formato validado','globe')}
{campo('Chave do envio pelo servidor','•••••••••••• salva em 18/11','EA','Não é exibida depois de salva','key')}
{campo('Meta tag do Search Console','google-site-verification=demo…','EA','Impressa só na página inicial do seu domínio','search')}</div></div>
<div class="card"><div class="hd"><h3>Anúncios e outros</h3></div><div class="g" style="gap:12px">
{campo('Google Ads','Bloqueado pela rede','T','Pedir liberação por chamado','lock')}
{campo('Meta (pixel e envio pelo servidor)','Bloqueado pela rede','T','','lock')}
{campo('TikTok','Bloqueado pela rede','T','','lock')}
{campo('Script livre','Não permitido para unidades','T','Pedidos especiais passam por revisão de segurança, peso e LGPD','lock')}</div></div>
<div class="g" style="align-content:start">
<div class="card"><div class="hd"><h3>{i('key',16)} Acesso da rede</h3><span class="pill a" style="margin-left:auto">1 de 2</span></div><p class="meta" style="margin-bottom:8px">Sua unidade tem domínio próprio, então a rede precisa de acesso ao seu Analytics e ao seu Search Console.</p>
<div class="lista-i" style="font-size:13px"><div class="it"><span class="ic v" style="width:28px;height:28px">{i('check',13)}</span><div style="flex:1"><b>Analytics</b><div class="meta">leitura concedida em 18/11</div></div></div>
<div class="it"><span class="ic a" style="width:28px;height:28px">{i('clock',13)}</span><div style="flex:1"><b>Search Console</b><div class="meta">adicione medicao@rede.exemplo.com.br</div></div><a class="btn s" href="{L('f-dominio')}">Domínio</a></div></div></div>
<div class="card"><div class="hd"><h3>Impacto na página</h3></div><div class="lista-i" style="font-size:13px"><div class="it"><b style="flex:1">Peso extra no navegador</b><span>0 KB</span></div><div class="it"><b style="flex:1">Lighthouse celular</b><span class="pill v">93</span></div><div class="it"><b style="flex:1">Consentimento exigido</b><span>Estatística</span></div></div>
<div class="meta" style="margin-top:8px">Guia em texto e vídeo: em preparação pela rede.</div></div></div></div>'''
salvar(ARQ['f-tags'],pagina('Tags e medição',F('f-tags',c)))

# ---------- 58 CONTROLES DA REDE (R02 + R03) ----------
cols=['Rede',f'Regional SP · {REG["Regional SP"]}',f'Regional Sul · {REG["Regional Sul"]}',f'Demais · {REG["Demais regionais"]}']
B=('r','Bloqueada'); Lb=('v','Liberada'); H=('hv','Herda'); HB=('hr','Herda')
fn=[('Promoções',[Lb,H,H,H],'0',130),('Campanhas para clientes',[B,Lb,HB,HB],'1 (GiO Batel)',REG['Regional SP']+1),('Canal WhatsApp',[B,Lb,HB,HB],'1 (GiO Batel)',REG['Regional SP']+1),('Canal e-mail',[Lb,H,H,H],'0',130),('Canal push',[B,HB,HB,HB],'0',0),
    ('Preço por procedimento',[B,HB,HB,HB],'0',0),('Procedimentos locais',[B,HB,HB,HB],'0',0),('Pacotes locais',[B,HB,HB,HB],'0',0),('Avisos regionais',[B,Lb,HB,HB],'0',REG['Regional SP']),
    ('Ver base de clientes',[Lb,H,H,H],'0',130),('Exportar clientes',[B,HB,HB,HB],'0',0),('Quiz da unidade',[B,HB,HB,HB],'0',0),('Tags da unidade',[B,HB,HB,HB],f'{UN_DOMINIO} (domínio próprio)',UN_DOMINIO)]
def cel(e):
    k,t=e
    if k=='v': return f'<span class="pill v">{i("check",11)} {t}</span>'
    if k=='r': return f'<span class="pill r">{i("lock",11)} {t}</span>'
    cor='var(--verde)' if k=='hv' else 'var(--vermelho)'
    return f'<span class="pill z" title="herda {"liberada" if k=="hv" else "bloqueada"}"><i style="background:{cor}"></i> herda</span>'
c=cabec('Controles da rede','O que cada unidade pode fazer. Tudo nasce bloqueado; a rede libera por escopo, com herança e exceções.',f'<a class="btn" href="{L("aud")}">{i("log",14)} Histórico</a><span class="btn p">{i("check",14)} Salvar com motivo</span>')+tabs([('Liberações',None),('Limites e alcance',None),('Pedidos das unidades · 3',L and 'suporte')],0)+f'''
<div class="g">
<div class="card" style="padding:0;overflow:hidden"><table class="t" style="table-layout:fixed"><thead><tr><th style="width:220px">Função</th>'''+''.join(f'<th style="white-space:normal;line-height:1.3">{c_}</th>' for c_ in cols)+'''<th style="width:200px">Exceções</th><th class="num" style="width:80px">Unidades</th></tr></thead><tbody>'''+''.join(f'<tr class="{"sel" if n=="Campanhas para clientes" else ""}"><td><b>{n}</b></td>'+''.join(f'<td>{cel(e)}</td>' for e in es)+f'<td class="meta trunc">{x}</td><td class="num"><b>{u}</b></td></tr>' for n,es,x,u in fn)+f'''</tbody></table>
<div class="meta" style="padding:12px 16px">Unidades = quantas das 130 têm a função liberada, somando herança e exceções. Teto: nenhuma unidade alcança a base nacional.</div></div>
<div class="g" style="grid-template-columns:1fr 1fr;align-items:start">
<div class="card"><div class="hd"><h3>{i('gear',16)} Limites · Regional SP</h3></div><div class="lista-i" style="font-size:13px">
<div class="it"><b style="flex:1">Campanhas por unidade</b><span>{COTA_UN} por mês</span></div>
<div class="it"><b style="flex:1">Mensagens por cliente</b><span>1 por semana</span></div>
<div class="it"><b style="flex:1">Janela de envio</b><span>9h às 20h</span></div>
<div class="it"><b style="flex:1">WhatsApp por unidade</b><span>1.500 por mês</span></div>
<div class="it"><b style="flex:1">Alcance máximo</b><span>própria unidade</span></div>
<div class="it"><b style="flex:1">Aprovação da rede</b><span class="pill v">obrigatória</span></div></div>
<div class="meta" style="margin-top:8px">Regras aprovadas em 21/11/2026. A frequência soma rede e unidades.</div></div>
<div class="card"><div class="hd"><h3>{i('alert',16)} Impacto ao bloquear</h3></div><p class="meta" style="margin-bottom:10px">Se você bloquear Campanhas para clientes na Regional SP agora:</p>
<div class="lista-i" style="font-size:13px"><div class="it"><b style="flex:1">Campanhas no ar</b><span>3</span></div><div class="it"><b style="flex:1">Em aprovação</b><span>2</span></div></div>
<div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap"><span class="chip on" data-toggle="1">Manter até o fim</span><span class="chip" data-toggle="1">Pausar</span><span class="chip" data-toggle="1">Despublicar</span></div></div></div></div>'''
salvar(ARQ['controles'],pagina('Controles da rede',R('controles',c)))

# ---------- 59 MURAL: CRIAR AVISO (R04 + R05) ----------
c=cabec('Mural de avisos','Comunicados da rede para as unidades, com confirmação de leitura.',f'<span class="btn">Salvar rascunho</span><span class="btn p">{i("send",14)} Publicar aviso</span>')+tabs([('Novo aviso',None),('Publicados · 12',None),('Relatório de leitura',None)],0)+f'''
<div class="g" style="grid-template-columns:1fr 400px;align-items:start">
<div class="card"><div class="g" style="gap:14px">
{campo('Título','Campanha de verão: materiais e prazos',ic='edit')}
<div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:12px">{campo('Categoria','Marketing',ic='tag')}{campo('Prioridade','Alta',ic='flag')}{campo('Confirmar leitura até','28/11/2026',ic='cal')}</div>
<div class="campo"><label>Mensagem</label><div class="in" style="min-height:110px;align-items:flex-start;line-height:1.6">Os materiais da campanha "Verão sem pelos" estão no guia em anexo. As unidades da Regional SP e da Regional Sul recebem a campanha da rede em 01/12. Confirme a leitura e confira se os horários de sábado estão atualizados na ficha.</div></div>
<div style="display:flex;gap:10px;align-items:center"><span class="chip">{i('clip',14)} guia-verao.pdf · 1,8 MB</span><span class="chip">{i('book',14)} Artigo da Wiki</span></div>
<div class="sep" style="margin:4px 0"></div>
<b>Público</b>
<div style="display:flex;gap:8px;flex-wrap:wrap"><span class="chip on" data-toggle="1">Todas as unidades · 130</span><span class="chip" data-toggle="1">Por regional</span><span class="chip" data-toggle="1">Por UF</span><span class="chip" data-toggle="1">Unidades específicas</span></div>
<div style="display:flex;gap:8px;flex-wrap:wrap">'''+''.join(f'<span class="chip on" data-toggle="1">{i("check",13)} {p} · {n}</span>' for p,n in MURAL_PERF.items())+f'''</div>
<b>Canais</b><div style="display:flex;gap:18px;flex-wrap:wrap;font-size:14px">'''+''.join(f'<span style="display:flex;gap:8px;align-items:center"><span class="tog{" on" if on else ""}" data-toggle="1"></span>{t}</span>' for t,on in [('Mural e sino',True),('E-mail',True),('WhatsApp interno',False),('Fixar no topo',True)])+f'''</div></div></div>
<div class="g" style="align-content:start">
<div class="card" style="background:var(--lilas-50)"><div class="meta">Alcance</div><div style="font:600 28px Poppins;color:var(--vinho)">{MURAL_TOT} pessoas</div><div class="meta">130 unidades · {" + ".join(str(v) for v in MURAL_PERF.values())} por perfil</div></div>
<div class="card"><div class="hd"><h3>Prévia no portal da unidade</h3></div><div class="aviso a"><div>{i('flag',16)}</div><div><b>Campanha de verão: materiais e prazos</b><div style="font-size:13px;margin-top:2px">Fixado · confirmar até 28/11</div><span class="btn s" style="margin-top:8px" data-sem-rota="1">Li e confirmo</span></div></div></div>
<div class="card"><div class="hd"><h3>{i('chart',16)} Aviso anterior</h3><span class="meta" style="margin-left:auto">Novo fluxo de aprovação</span></div>
<div style="display:flex;align-items:center;gap:14px">{donut([MURAL_CONF,130-MURAL_CONF],['#0B7A54','#e6d3ec'],tam=96,esp=14,centro=f"{round(MURAL_CONF/130*100)}%")}<div style="font-size:13px"><b>{MURAL_CONF} de 130</b> unidades confirmaram<div class="meta">{130-MURAL_CONF} pendentes · prazo venceu em 20/11</div><span class="btn s" style="margin-top:8px" data-sem-rota="1">{i('send',12)} Reenviar a pendentes</span></div></div></div></div></div>'''
salvar(ARQ['mural'],pagina('Mural de avisos',R('mural',c)))

# ---------- 60 CAMPANHA DA REDE (R07), passo 7 prévia ----------
fr=[('Clientes em SP e PR com interesse em laser',CR_BASE),('Com consentimento de WhatsApp',CR_CANAL),('Já receberam mensagem nos últimos 7 dias',-CR_FREQ),('Alcance final',CR_FINAL)]
TABS_CAMP=[('Fila de aprovação · 4','camp-aprov'),('Nova campanha da rede','camp-rede'),('Performance','perf')]
c=cabec('Campanhas','Campanha da rede "Verão sem pelos" · passo 7 de 8: prévia de alcance e custo.',f'<a class="btn" href="{L("camp-aprov")}">Salvar rascunho</a><a class="btn p" href="{L("camp-aprov")}">Ir para revisão</a>')+tabs(TABS_CAMP,1)+f'''
<div class="g" style="grid-template-columns:1fr 1fr 360px;align-items:start">
<div class="card"><div class="hd"><h3>{i('map',16)} Onde</h3><span class="meta" style="margin-left:auto">SP e PR · {CR_UN} unidades</span></div>{mapa_geo(380,330,[],BOX_BR,cont_uf={'SP':UF_CONT['SP'],'PR':UF_CONT['PR']},escala=lambda n:'#b0197e' if n else '#efe6f2',rotulos=True)}
<div class="meta">As {CR_UN} unidades afetadas recebem aviso automático no mural, com a data de início.</div></div>
<div class="card"><div class="hd"><h3>{i('users',16)} Quem</h3></div>'''+''.join(f'<div style="display:flex;align-items:center;padding:10px 0;border-bottom:1px dashed var(--linha)"><span style="flex:1;font-size:13px">{t}</span><b style="font-variant-numeric:tabular-nums;{"color:var(--vermelho)" if v<0 else ""}">{"−"+fmt(-v) if v<0 else fmt(v)}</b></div>' for t,v in fr[:-1])+f'''
<div style="margin-top:12px;padding:12px;border-radius:12px;background:var(--lilas-50)"><div class="meta">Alcance final</div><div style="font:600 28px Poppins;color:var(--vinho)">{fmt(CR_FINAL)} clientes</div><div class="meta">{fmt(CR_BASE)} × {CONS_PCT["WhatsApp"]}% com consentimento, menos a regra de 1 mensagem por semana</div></div>
<div class="lista-i" style="font-size:13px;margin-top:10px"><div class="it"><b style="flex:1">Mensagens de marketing</b><span>{fmt(CR_FINAL)}</span></div><div class="it"><b style="flex:1">Custo</b><span>tabela vigente da Meta no envio</span></div><div class="it"><b style="flex:1">Janela</b><span>01/12, 9h às 20h</span></div></div></div>
<div class="card"><div class="hd"><h3>{i('phone2',16)} Prévia no WhatsApp</h3></div>
<div style="background:#efe7dd;border-radius:14px;padding:14px"><div style="background:#fff;border-radius:10px;padding:10px 12px;font-size:13px;line-height:1.5;box-shadow:0 1px 1px rgba(0,0,0,.08)"><b>Gio Estética Avançada</b><br>Oi, {{nome}}! O verão chegou e a avaliação de depilação a laser é gratuita na {{unidade}} até 15/12. Quer agendar?<div style="border-top:1px solid var(--linha);margin-top:8px;padding-top:8px;text-align:center;color:var(--azul);font-weight:600">Agendar avaliação</div></div>
<div class="meta" style="margin-top:8px;color:#4d3f33">Modelo de mensagem aprovado pela Meta · categoria marketing</div></div>
<div class="aviso v" style="margin-top:12px"><div>{i('check',16)}</div><div style="font-size:13px">Validador: sem preço, validade explícita, CTA "avaliação gratuita".</div></div></div></div>'''
salvar(ARQ['camp-rede'],pagina('Campanha da rede',R('camp-aprov',c)))

# ---------- 61 FILA DE APROVAÇÃO DE CAMPANHAS (R08) ----------
fu=funil_un(INT_ULTRA)
fila=[('Semana do Ultraformer','GiO Alto da Lapa','WhatsApp e e-mail',CAMP_ULTRA,'vence em 46 h','v'),('Black November facial','GiO Batel','E-mail',540,'vence em 30 h','v'),('Aniversário de 3 anos','GiO Cambuí','WhatsApp',318,'vence em 6 h','a'),('Volta às aulas','GiO Aldeota','E-mail',212,'venceu há 1 h','r')]
c=cabec('Campanhas','Campanhas das unidades aguardando a rede. SLA de 48 h úteis.',f'<a class="btn" href="{L("controles")}">{i("key",14)} Limites</a>')+tabs(TABS_CAMP,0)+f'''
<div class="g" style="grid-template-columns:360px 1fr;align-items:start">
<div class="card" style="padding:6px 0">'''+''.join(f'<div style="padding:12px 16px;border-bottom:1px solid var(--linha);{"background:#fbf3f8;border-left:3px solid var(--vinho)" if k==0 else ""}"><div style="display:flex;align-items:center;gap:8px"><b class="trunc">{n}</b><span class="pill {cl}" style="margin-left:auto">{s}</span></div><div class="meta">{u} · {ch} · {fmt(a)} clientes</div></div>' for k,(n,u,ch,a,s,cl) in enumerate(fila))+f'''<div class="meta" style="padding:10px 16px">4 itens · ordenados por prazo</div></div>
<div class="card"><div class="hd"><div><h3>Semana do Ultraformer · GiO Alto da Lapa</h3><div class="meta">Enviada por Renata F. (admin da unidade) há 2 h · modelo "Avaliação gratuita" · 01/12 a 07/12</div></div></div>
<div class="g" style="grid-template-columns:1fr 1fr;gap:16px">
<div><div class="sw" style="margin-bottom:10px"><span class="on" data-toggle="1">WhatsApp</span><span data-toggle="1">E-mail</span></div>
<div style="background:#efe7dd;border-radius:14px;padding:14px"><div style="background:#fff;border-radius:10px;padding:10px 12px;font-size:13px;line-height:1.5"><b>GiO Alto da Lapa</b><br>Oi, {{nome}}! De 01 a 07/12 é a Semana do Ultraformer na GiO Alto da Lapa: avaliação gratuita e horário estendido até 21h. Quer agendar?<div style="border-top:1px solid var(--linha);margin-top:8px;padding-top:8px;text-align:center;color:var(--azul);font-weight:600">Agendar avaliação</div></div></div></div>
<div><b style="font-size:14px">Alcance</b>'''+''.join(f'<div style="display:flex;padding:8px 0;border-bottom:1px dashed var(--linha);font-size:13px"><span style="flex:1">{t}</span><b>{fmt(v)}</b></div>' for t,v in fu)+f'''
<div class="lista-i" style="font-size:13px;margin-top:8px"><div class="it">{i('check',14)} Dentro do teto: só clientes da unidade</div><div class="it">{i('check',14)} Cota: vira {COTA_USADA_AL+1} de {COTA_UN} em novembro</div><div class="it">{i('check',14)} Validador: sem preço, validade explícita</div><div class="it" style="color:var(--ambar)">{i('alert',14)} "Até 21h": conferir horário na ficha (hoje fecha às 20h)</div></div></div></div>
<div class="sep"></div><div style="display:flex;gap:8px;align-items:center"><a class="btn p" href="{L("perf")}">{i("check",14)} Aprovar</a><span class="btn" data-sem-rota="1">{i("edit",14)} Pedir ajuste</span><span class="btn perigo" data-sem-rota="1">Reprovar com motivo</span><span class="meta" style="margin-left:auto">Quem envia não aprova a própria campanha.</span></div></div></div>'''
salvar(ARQ['camp-aprov'],pagina('Aprovação de campanhas',R('camp-aprov',c)))

# ---------- 62 PERFORMANCE (R09) com replicar (R13) ----------
cps=[('Avaliação gratuita de laser','Rede',18200,3120,74,46),('Limpeza de pele de verão','GiO Alto da Lapa',652,141,9,6),('Black November facial','GiO Batel',4100,690,21,12),('Aniversário do cliente','Rede (automática)',2900,410,18,11)]
c=cabec('Campanhas','Resultado das campanhas de 01 a 21 nov, do envio ao comparecimento.',periodo())+tabs(TABS_CAMP,2)+f'''
<div style="display:flex;gap:8px;margin-bottom:14px">'''+''.join(f'<span class="chip">{t} {i("chevd",12)}</span>' for t in ['Regional: todas','UF: todas','Canal: todos','Objetivo: todos','Procedimento: todos'])+f'''</div>
<div class="g" style="grid-template-columns:repeat(5,1fr);margin-bottom:16px">'''+''.join(kpi(ic,t,fmt(v),d) for (t,v),ic,d in zip(PF,['send','eye','cursor','cal','check'],['mensagens no período',f'{round(PF[1][1]/PF[0][1]*100)}% das entregues',f'{round(PF[2][1]/PF[1][1]*100)}% das abertas',f'de {fmt(EV[3][2])} agendamentos da rede',f'{round(PF[4][1]/PF[3][1]*100)}% dos agendamentos']))+f'''</div>
<div class="g" style="grid-template-columns:1fr 380px;align-items:start">
<div class="card" style="padding:0;overflow:hidden"><table class="t"><thead><tr><th>Campanha</th><th>Origem</th><th class="num">Entregues</th><th class="num">Cliques</th><th class="num">Agend.</th><th class="num">Compar.</th></tr></thead><tbody>'''+''.join(f'<tr class="{"sel" if k==0 else ""}"><td><b>{n}</b></td><td>{o}</td><td class="num">{fmt(e)}</td><td class="num">{fmt(cl)}</td><td class="num">{a}</td><td class="num">{cm}</td></tr>' for k,(n,o,e,cl,a,cm) in enumerate(cps))+f'''</tbody></table>
<div class="meta" style="padding:12px 16px">Agendamentos e comparecimentos vêm da agenda da unidade (DocBiz), atribuídos pelo coletor da rede.</div></div>
<div class="card"><div class="hd"><h3>{i('copy',16)} Replicar "Avaliação gratuita de laser"</h3></div>
<div class="campo"><label>Destino</label><div class="in">Regional Sul · {REG['Regional Sul']} unidades</div></div>
<div class="meta" style="margin:10px 0 6px;font-weight:600">Prévia por unidade (ajustada ao teto de cada uma)</div>
<div class="lista-i" style="font-size:13px">'''+''.join(f'<div class="it" style="padding:7px 0"><b style="flex:1">{u}</b><span>{fmt(v)} clientes</span></div>' for u,v in [('GiO Batel',512),('GiO Porto Alegre Bom Fim',388),('GiO Florianópolis Centro',301)])+f'''<div class="it" style="padding:7px 0"><span class="meta">mais 11 unidades</span></div></div>
<div style="display:flex;gap:8px;margin-top:12px"><span class="btn p" data-sem-rota="1">Propor às unidades</span><span class="btn" data-sem-rota="1">Publicar pela rede</span></div></div></div>'''
salvar(ARQ['perf'],pagina('Performance de campanhas',R('camp-aprov',c)))
print('s8 ok')
