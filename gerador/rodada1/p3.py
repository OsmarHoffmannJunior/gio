from base import *
random.seed(9)
# 09 RELATÓRIOS
salvos=[('Desempenho mensal da rede','Diretoria Salus','Todo dia 1 às 08:00','PDF + planilha','v'),('Leads por unidade e origem','Franqueados (cada um vê o seu)','Toda segunda às 07:00','E-mail','v'),('SLA do call center','Coordenação call center','Diário às 18:00','Planilha','v'),('Saúde SEO local','Agência e marketing','Quinzenal','PDF','a'),('Campanhas Google Ads x agendamentos','Marketing da rede','Toda sexta','Planilha','v')]
modelos=[('chart','Funil por unidade','Leads, contato, agendamento e comparecimento'),('target','SEO local','Posições no mapa, GBP, avaliações'),('clock','SLA de atendimento','Tempo de 1º contato por fila e pessoa'),('tag','Campanhas e UTM','Custo por agendamento quando houver custo'),('star','Avaliações Google','Nota, volume e respostas por unidade'),('file','Completude das páginas','O que falta em cada ficha')]
meses=['jun','jul','ago','set','out','nov']
cont=f'''
<div class="cab"><div><h1>Relatórios</h1><p>Monte, salve e agende. Cada pessoa recebe só os dados que o perfil dela permite ver.</p></div>
<div class="dir"><span class="btn">{i('cal',14)} Agendados <span class="pill l">5</span></span><span class="btn p">{i('plus',14)} Novo relatório</span></div></div>
<div class="g" style="grid-template-columns:repeat(6,1fr);margin-bottom:16px">'''+''.join(f'<div class="card" style="padding:14px"><div class="ic l" style="margin-bottom:10px">{i(ic,16)}</div><b>{t}</b><div class="muted" style="font-size:12px;margin-top:3px">{d}</div></div>' for ic,t,d in modelos)+f'''</div>
<div class="g" style="grid-template-columns:1.5fr 1fr">
 <div class="card"><div class="hd"><div><h3>Prévia · Funil por estado</h3><div class="sub">jun a nov de 2026 · agrupado por estado · comparação com mesmo período</div></div><div class="dir"><span class="btn s">{i('filter',12)} Filtros</span><span class="btn s">{i('down',12)} PDF</span><span class="btn s">{i('down',12)} Planilha</span></div></div>
  <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap"><span class="chip on">Linhas: <b>Estado</b></span><span class="chip on">Colunas: <b>Mês</b></span><span class="chip on">Métrica: <b>Agendamentos</b></span><span class="chip">{i('plus',12)} Métrica</span></div>
  <div class="muted" style="font-size:12px;margin-bottom:4px">Taxa de agendamento sobre leads (%)</div>{area([[55,56,57,58,59,61],[50,53,52,57,60,63],[44,47,51,50,54,57]],['#4c1455','#b0197e','#e5559f'],w=700,h=190,labels=meses,ymax=70)}
  <div class="leg" style="margin:8px 0 14px"><span><i style="background:#4c1455"></i>SP</span><span><i style="background:#b0197e"></i>PR</span><span><i style="background:#e5559f"></i>MG</span></div>
  <table class="t"><thead><tr><th>Estado</th>'''+''.join(f'<th class="num">{m}</th>' for m in meses)+'''<th class="num">Var.</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{uf}</b> <span class="muted">{n} un.</span></td>'+''.join(f'<td class="num">{v:,}</td>'.replace(',','.') for v in vals)+f'<td class="num"><span class="up">+{round((vals[-1]/vals[0]-1)*100)}%</span></td></tr>' for uf,n,vals in [('SP',86,[980,1040,1120,1210,1390,1530]),('PR',7,[120,130,128,141,150,166]),('MG',8,[90,94,102,108,121,130]),('GO',7,[71,70,79,84,88,97]),('RS',4,[44,47,45,52,55,61])])+f'''</tbody></table></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('cal',15)} Relatórios agendados</h3></div>
  <div class="lista-i">'''+''.join(f'<div class="it"><div class="ic {c}">{i("file",15)}</div><div style="flex:1;min-width:0"><b class="trunc" style="display:block">{t}</b><div class="muted trunc" style="font-size:12px">{q} · {p}</div><div class="muted" style="font-size:12px">{d}</div></div>{i("more",15)}</div>' for t,p,q,d,c in salvos)+f'''</div></div>
  <div class="card" style="background:var(--lilas-50);box-shadow:none"><div class="hd"><h3>{i('shield',15)} Exportação com dados pessoais</h3></div><div class="muted" style="font-size:12px;line-height:1.6">Planilhas com nome e telefone só saem para perfis com permissão de exportar leads. Cada download fica na auditoria e o link expira em 24 h.</div></div>
 </div>
</div>'''
salvar('09-relatorios',pagina('Relatórios',app('admin','rel',cont)))

# 10 SUPORTE
tk=[('#1482','Domínio não abre depois da troca de DNS','GiO Asa Sul','Domínio','a','Em andamento','2 h',True),('#1481','Lead não chegou no WhatsApp da recepção','GiO Batel','Leads','r','Urgente','35 min',False),('#1479','Como trocar a foto principal da página?','GiO Bom Fim','Página','l','Aguardando unidade','1 dia',False),('#1477','Avaliação falsa no Google','GiO Cambuí','Google','a','Em andamento','1 dia',False),('#1475','Novo usuário para recepção','GiO Salvador','Acessos','v','Resolvido','2 dias',False),('#1474','Relatório mensal veio vazio','GiO Aldeota','Relatórios','v','Resolvido','3 dias',False)]
msgs=[('JF','Juliano F.','GiO Asa Sul','Troquei o DNS ontem às 18h seguindo o passo a passo, mas o endereço gioasasul.com.br ainda abre a página antiga da hospedagem.','ontem 18:42',False),
('PS','Paula S.','Suporte da rede','Oi, Juliano. Vi aqui: o registro A está certo, mas ficou um CNAME antigo no "www". Já deixei o passo exato abaixo. Depois de salvar, a verificação roda sozinha a cada 10 minutos.','hoje 09:10',True)]
cont=f'''
<div class="cab"><div><h1>Suporte</h1><p>Chamados das unidades com prazo de resposta. Antes de abrir, a unidade vê artigos da base que resolvem o assunto.</p></div>
<div class="dir"><span class="btn">{i('book',14)} Base de conhecimento</span><span class="btn p">{i('plus',14)} Novo chamado</span></div></div>
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">
 <div class="card kpi"><div class="l">{i('inbox',15)} Abertos</div><div class="v">12</div><div class="d">3 urgentes</div></div>
 <div class="card kpi"><div class="l">{i('clock',15)} 1ª resposta</div><div class="v">42 min</div><div class="d">meta 2 h úteis</div></div>
 <div class="card kpi"><div class="l">{i('check',15)} Resolvidos no mês</div><div class="v">87</div><div class="d"><span class="up">94%</span> no prazo</div></div>
 <div class="card kpi"><div class="l">{i('book',15)} Resolvidos pela base</div><div class="v">31%</div><div class="d">sem abrir chamado</div></div>
</div>
<div class="g" style="grid-template-columns:440px 1fr">
 <div class="card" style="padding:0">
  <div style="display:flex;gap:6px;padding:12px;border-bottom:1px solid var(--linha)"><span class="chip on">Abertos <b>12</b></span><span class="chip">Meus</span><span class="chip">Urgentes</span><span class="chip">Resolvidos</span></div>
  '''+''.join(f'<div style="padding:13px 16px;border-bottom:1px solid var(--linha);{"background:var(--lilas-50);box-shadow:inset 3px 0 0 var(--vinho)" if s else ""}"><div style="display:flex;gap:8px;align-items:center"><span class="muted" style="font-size:12px">{n}</span><span class="pill {c}">{st}</span><span class="muted" style="margin-left:auto;font-size:12px">{i("clock",11)} {t}</span></div><b class="trunc" style="display:block;margin:4px 0 2px">{tt}</b><div class="muted" style="font-size:12px">{u} · {cat}</div></div>' for n,tt,u,cat,c,st,t,s in tk)+f'''</div>
 <div class="card"><div class="hd"><div><h3>#1482 · Domínio não abre depois da troca de DNS</h3><div class="sub">GiO Asa Sul · Domínio · aberto ontem às 18:42 · prazo de solução hoje às 18:00</div></div><div class="dir"><span class="btn s">{i('users',12)} Atribuir</span><span class="btn s p">{i('check',12)} Resolver</span></div></div>
  <div style="display:flex;gap:8px;margin-bottom:16px"><span class="pill a">Em andamento</span><span class="pill l">Responsável: Paula S.</span><span class="pill z">Prioridade média</span></div>
  '''+''.join(f'<div style="display:flex;gap:12px;margin-bottom:16px;{"flex-direction:row-reverse" if me else ""}"><span class="av-s" style="width:34px;height:34px;background:{"#f3c6e0" if me else "#e4d4f0"}">{a}</span><div style="max-width:560px;{"text-align:right" if me else ""}"><div style="font-size:12px" class="muted"><b style="color:var(--tinta)">{n}</b> · {o} · {d}</div><div style="margin-top:5px;padding:12px 14px;border-radius:14px;line-height:1.6;text-align:left;{"background:var(--lilas-100)" if me else "background:#f7f4f9"}">{t}</div></div></div>' for a,n,o,t,d,me in msgs)+f'''
  <div style="margin:0 0 16px 46px;border:1px solid var(--linha);border-radius:12px;padding:12px 14px;display:flex;gap:12px;align-items:center"><div class="ic l">{i('book',15)}</div><div style="flex:1"><b>Artigo: Como apontar o domínio próprio da unidade</b><div class="muted" style="font-size:12px">Base de conhecimento · 4 min de leitura · útil para 92% de quem leu</div></div><span class="btn s">Abrir</span></div>
  <div class="card" style="box-shadow:none;background:#fbf8fc;margin-left:46px;padding:12px 14px"><div class="muted" style="font-size:12px;margin-bottom:6px"><b>Verificação automática do domínio</b></div>
   <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:8px">'''+''.join(f'<div style="display:flex;gap:6px;align-items:center"><span class="ic {c}" style="width:22px;height:22px;border-radius:7px">{i("check" if c=="v" else "alert",12)}</span><span style="font-size:12px">{t}</span></div>' for c,t in [('v','Registro A'),('r','CNAME www'),('a','Certificado SSL'),('a','Redirect 301')])+f'''</div></div>
  <div class="sep"></div>
  <div style="display:flex;gap:8px"><span class="sw"><span class="on">Responder</span><span>Nota interna</span></span><div style="flex:1;border:1px solid var(--linha);border-radius:10px;padding:9px 12px;color:var(--tinta-3)">Escreva para a unidade. Use / para inserir um artigo…</div><span class="btn p">{i('send',14)}</span></div>
 </div>
</div>'''
salvar('10-suporte',pagina('Suporte',app('admin','suporte',cont)))

# 11 USUÁRIOS E PERMISSÕES
perfis=['Admin Gio','Marketing rede','Call center','Agência','Multi franq.','Franqueado','Recepção']
perms=[('Ver unidades','T T R T P P P'),('Editar dados da unidade','T T N N P P N'),('Aprovar conteúdo','T T N N N N N'),('Editar página e blocos','T T N T P P N'),('Ver leads com dados pessoais','T R F N P P P'),('Exportar leads','T N N N P P N'),('Domínio e DNS','T N N T N P N'),('Relatórios da rede','T T R R N N N'),('Usuários e acessos','T N N N P P N'),('Auditoria','T N N N N N N')]
sym={'T':('v','check','Tudo'),'R':('b','eye','Ler'),'P':('l','pin','Próprias'),'F':('a','phone','Fila'),'N':('z','x','Não')}
usuarios=[('IN','Ingrid N.','Admin Gio','Rede inteira','agora','2FA'),('PS','Paula S.','Admin Gio','Rede inteira','há 1 h','2FA'),('CO','Carlos O.','Call center','Fila Sul e Sudeste','há 3 min','2FA'),('AG','Equipe SEO','Agência','Rede · sem dados pessoais','ontem','2FA'),('MV','Marcos V.','Multifranqueado','4 unidades em SP','há 2 h','2FA'),('RF','Renata F.','Franqueado','GiO Alto da Lapa','há 10 min','SMS'),('JM','Juliana M.','Recepção','GiO Alto da Lapa','há 5 min','Não')]
aud=[('Renata F.','publicou a página após aprovação','GiO Alto da Lapa','10:44'),('Carlos O.','viu o telefone completo de um lead','Fila Sul','10:31'),('Ingrid N.','exportou 2.986 leads (planilha)','Rede','09:58'),('Marcos V.','convidou Juliana M. como Recepção','GiO Alto da Lapa','09:12'),('Sistema','revogou acesso inativo há 90 dias','GiO Ipiranga','03:00')]
cont=f'''
<div class="cab"><div><h1>Usuários e acessos</h1><p>Perfis por papel e escopo. Ninguém vê lead de outra unidade, e cada acesso a dado pessoal fica registrado.</p></div>
<div class="dir"><span class="btn">{i('log',14)} Auditoria completa</span><span class="btn p">{i('plus',14)} Convidar pessoa</span></div></div>
<div class="tabs"><a>Pessoas <span class="n">214</span></a><a class="on">Perfis e permissões</a><a>Solicitações LGPD <span class="n">2</span></a><a>Segurança</a></div>
<div class="g" style="grid-template-columns:1.8fr 1fr">
 <div class="card" style="padding:0">
  <div style="padding:16px 16px 6px" class="hd"><h3>Matriz de permissões</h3><div class="leg" style="margin-left:auto">'''+''.join(f'<span><span class="pill {c}" style="padding:2px 6px">{i(ic,10)}</span> {t}</span>' for c,ic,t in sym.values())+'''</div></div>
  <table class="t"><thead><tr><th>Permissão</th>'''+''.join(f'<th style="text-align:center;white-space:normal;line-height:1.3">{p}</th>' for p in perfis)+'</tr></thead><tbody>'+''.join(f'<tr><td><b style="font-weight:500">{n}</b></td>'+''.join(f'<td style="text-align:center"><span class="pill {sym[x][0]}" style="padding:3px 7px">{i(sym[x][1],11)}</span></td>' for x in v.split())+'</tr>' for n,v in perms)+f'''</tbody></table>
  <div style="margin:8px 16px 16px;display:grid;grid-template-columns:1fr 1fr;gap:12px">'''+''.join(f'<div style="border:1px solid var(--linha);border-radius:12px;padding:12px;display:flex;gap:10px"><div class="ic {c}">{i(ic,15)}</div><div><b>{t}</b><div class="muted" style="font-size:12px;margin-top:2px">{d}</div></div></div>' for c,ic,t,d in [('l','lock','Isolamento por unidade','Regra no banco (RLS), não só na tela. Multifranqueado vê só as unidades dele.'),('a','eye','Dado pessoal mascarado','Telefone e e-mail aparecem parciais. Ver completo pede motivo e gera registro.'),('v','shield','2FA obrigatório','Rede, call center e agência. Franqueado pode usar SMS ou app.'),('b','clock','Acesso que expira','Agência e temporários perdem acesso na data. Inativos há 90 dias são revogados.')])+f'''</div></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Pessoas recentes</h3><span class="sub" style="margin-left:auto">214 ativas</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="av-s" style="background:#efe3f4">{a}</span><div style="flex:1;min-width:0"><b>{n}</b> <span class="pill l" style="margin-left:4px">{p}</span><div class="muted trunc" style="font-size:12px">{e} · ativo {t}</div></div><span class="pill {"v" if f!="Não" else "a"}">{i("shield",10)} {f}</span></div>' for a,n,p,e,t,f in usuarios)+f'''</div></div>
  <div class="card"><div class="hd"><h3>{i('log',15)} Auditoria de hoje</h3><span class="btn s" style="margin-left:auto">{i('down',12)} Exportar</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it" style="padding:8px 0"><span class="muted" style="width:40px;font-size:12px">{h}</span><div style="flex:1;min-width:0"><b>{q}</b> <span>{o}</span><div class="muted" style="font-size:12px">{w}</div></div></div>' for q,o,w,h in aud)+'''</div></div>
 </div>
</div>'''
salvar('11-usuarios-permissoes',pagina('Usuários',app('admin','users',cont),extra_css='table.t th,table.t td{padding:9px 7px} table.t th:first-child,table.t td:first-child{padding-left:16px;white-space:normal} table.t{table-layout:fixed} table.t th{letter-spacing:.02em;font-size:10px} table.t th:first-child{width:175px}'))
print('p3 ok')
