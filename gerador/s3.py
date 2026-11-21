from base import *
random.seed(11)
def cabec(t,p,dir=''): return f'<div class="cab"><div><h1>{t}</h1><p>{p}</p></div><div class="dir">{dir}</div></div>'
# ---------- 13 RELATÓRIOS ----------
# A tela 13 virou o hub de relatórios da rede (spec 005) e é gerada em s12.py, junto com as subtelas 90 a 99.

# ---------- 14 RELATÓRIOS INTELIGENTES ----------
ins=[('r','trend','Leads de Goiás caíram 31% na semana','7 unidades em GO. A queda começou no dia em que a campanha de Google Ads da região pausou (17/11).','Ver campanha','alta'),
('a','image','Unidades sem foto convertem 0,6 p.p. menos','Comparação entre 70 unidades sem foto e 60 com fotos, mesmo período. Sugestão: mutirão de fotos em dezembro.','Ver unidades','média'),
('v','star','Página de serviço aumentou leads no Alto da Lapa','A variante "Depilação a laser" trouxe 11 leads em 30 dias, 27% do total da unidade.','Ver variante','informativo')]
regras=[('Queda de leads acima de 25% na semana','Por UF e por unidade','Marketing, regional',True),('Lead sem 1º contato em 15 min','Por unidade','Call center, unidade',True),('Perfil do Google diverge da ficha','Diário','SEO, unidade',True),('Completude abaixo de 55%','Semanal','Regional',False)]
ass=[('Resumo semanal da rede','Segunda, 8h','Diretoria, Marketing · 6 pessoas'),('Insights da regional SP Capital','Segunda, 9h','Gestor regional · 1'),('Resumo da unidade','Segunda, 8h','Admins das 130 unidades')]
cont=cabec('Relatórios inteligentes','Insights gerados a partir dos dados da rede, alertas por regra e envio por e-mail.',f'<span class="btn">{i("gear",14)} Regras</span><span class="btn p">{i("plus",14)} Nova assinatura</span>')+f'''
<div class="g" style="grid-template-columns:1.5fr 1fr">
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('sparkle',16)} Insights desta semana</h3><span class="pill l" style="margin-left:auto">3 novos</span></div>
   <div class="lista-i">'''+''.join(f'<div class="it" style="align-items:flex-start;padding:14px 0"><div class="ic {c}">{i(ic,16)}</div><div style="flex:1"><div style="display:flex;gap:8px;align-items:center"><b>{t}</b><span class="pill {c}">{p}</span></div><p class="muted" style="margin-top:4px">{d}</p><div style="display:flex;gap:8px;margin-top:8px"><span class="btn s">{a}</span><span class="btn s ghost">Útil</span><span class="btn s ghost">Dispensar</span></div></div></div>' for c,ic,t,d,a,p in ins)+f'''</div>
   <p class="meta" style="margin-top:8px">Cada insight mostra a base de cálculo e o período. Nenhum insight usa dados pessoais de clientes.</p></div>
  <div class="card"><div class="hd"><h3>{i('alert',16)} Regras de alerta</h3></div>
   <table class="t"><thead><tr><th>Regra</th><th>Frequência</th><th>Ativa</th></tr></thead><tbody>'''+''.join(f'<tr><td style="white-space:normal"><b>{r}</b><div class="meta">Recebe: {q}</div></td><td>{f}</td><td><span class="tog{" on" if on else ""}"></span></td></tr>' for r,f,q,on in regras)+f'''</tbody></table></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('mail',16)} Envios por e-mail</h3></div>
   <div class="lista-i">'''+''.join(f'<div class="it"><div class="ic l">{i("cal",15)}</div><div style="flex:1"><b>{t}</b><div class="meta">{q} · {p}</div></div>{i("more",16)}</div>' for t,q,p in ass)+f'''</div></div>
  <div class="card"><div class="hd"><h3>Prévia do e-mail semanal</h3></div>
   <div style="border:1px solid var(--linha);border-radius:12px;overflow:hidden"><div style="background:var(--grad);padding:12px 14px"><img src="../assets/logo-gio-branco.png" alt="Gio" style="height:24px"></div>
   <div style="padding:14px"><b>Semana de 17 a 23/11</b><div class="g" style="grid-template-columns:1fr 1fr 1fr;gap:8px;margin:10px 0"><div><div class="meta">Leads</div><b>1.010</b></div><div><div class="meta">Agendados</div><b>586</b></div><div><div class="meta">1º contato</div><b>11 min</b></div></div><p class="meta">3 insights e 2 alertas. Abra o portal para ver os detalhes.</p></div></div></div>
 </div>
</div>'''
salvar(ARQ['insights'],pagina('Relatórios inteligentes',app('admin','insights',cont)))

# ---------- 15 SUPORTE ----------
tk=[('#2291','Domínio não aponta para a página','GiO Asa Sul','Domínio','a','Em andamento','há 2 h',True),('#2290','Como trocar a foto da fachada?','GiO Cambuí','Ficha','l','Aberto','há 3 h',False),('#2288','Lead duplicado no quadro','GiO Batel','Leads','l','Aberto','há 5 h',False),('#2285','Contestação de horário alterado','GiO Alto da Lapa','Override','a','Em andamento','ontem',False),('#2283','Acesso de nova recepcionista','GiO Aldeota','Usuários','l','Aberto','ontem',False)]
cont=cabec('Suporte','Chamados das unidades para a rede. SLA de primeira resposta: 4 h úteis.',f'<span class="btn p">{i("plus",14)} Novo chamado</span>')+f'''
<div class="tabs"><a class="on">Abertos <span class="n">12</span></a><a>Em andamento <span class="n">5</span></a><a>Resolvidos</a><a>Base de respostas</a></div>
<div class="g" style="grid-template-columns:460px 1fr">
 <div class="card" style="padding:0">'''+''.join(f'<div style="padding:12px 16px;border-bottom:1px solid var(--linha);{"background:#fbf3f8;border-left:3px solid var(--vinho)" if sel else ""}"><div style="display:flex;gap:8px;align-items:center"><span class="meta">{n}</span><b class="trunc">{t}</b><span class="pill {c}" style="margin-left:auto">{s}</span></div><div class="meta" style="margin-top:4px">{u} · {cat} · {q}</div></div>' for n,t,u,cat,c,s,q,sel in tk)+f'''<p class="meta" style="padding:12px 16px">5 de 12 abertos. Resolvidos ficam só na aba Resolvidos.</p></div>
 <div class="card"><div class="hd"><div><h3>#2291 · Domínio não aponta para a página</h3><div class="meta">GiO Asa Sul · aberto por Diego R. (admin da unidade) · categoria Domínio</div></div><span class="pill a" style="margin-left:auto">Em andamento</span></div>
  <div class="lista-i">
   <div class="it" style="align-items:flex-start"><span class="av-s">DR</span><div><b>Diego R.</b> <span class="meta">há 2 h</span><p style="margin-top:4px">Configurei o domínio gioasasul.exemplo.com.br ontem e a página ainda não abre.</p></div></div>
   <div class="it" style="align-items:flex-start"><span class="av-s">TS</span><div><b>Tiago S.</b> <span class="pill l">SEO da rede</span> <span class="meta">há 1 h</span><p style="margin-top:4px">O registro A está apontando para um IP antigo. O correto é <b>{IP_DEMO}</b>. A propagação pode levar até 24 h depois da troca.</p></div></div>
  </div>
  <div class="aviso b" style="margin-top:12px"><div>{i('book',16)}</div><div style="font-size:13px">Artigo sugerido: <a class="lk" href="{L('ajuda')}">Como apontar o domínio próprio</a> (Central de ajuda)</div></div>
  <div style="display:flex;gap:10px;margin-top:14px"><div class="campo" style="flex:1"><div class="in" style="color:var(--tinta-3)">Responder para a unidade…</div></div><span class="btn">{i('clip',14)}</span><span class="btn p">{i('send',14)} Responder</span></div>
 </div>
</div>'''
salvar(ARQ['suporte'],pagina('Suporte',app('admin','suporte',cont)))

# ---------- 16 USUÁRIOS E PERFIS ----------
perfis=[('Rede',[('Admin da rede','2'),('Marketing','4'),('SEO','2'),('Comercial','3'),('Call center','14'),('Financeiro','2'),('Agência parceira','3')]),('Regional',[('Gestor regional','5')]),('Unidade',[('Admin da unidade','130'),('Gerente da unidade','96'),('Recepção','212')]),('Personalizados',[('SEO de agência, só leitura','2')])]
mods=[('Unidades e ficha','V E','Rede toda'),('Aprovações','V A','Rede toda'),('Landing pages','V E A','Rede toda'),('Leads','V','Sem dados pessoais'),('Relatórios','V D','Sem dados pessoais'),('SEO local','V','Leitura'),('Templates e marca','V E','Rede toda'),('Usuários e perfis','','Sem acesso'),('Auditoria','V','Próprias ações'),('LGPD','','Sem acesso')]
acoes=['V','E','A','D']
def celula(m,a):
    on=a in m.split()
    return f'<td style="text-align:center">{"<span class=\"cx on\"></span>" if on else "<span class=\"cx\"></span>"}</td>'
cont=cabec('Usuários e perfis','Perfis por escopo (rede, regional, unidade). Contas internas só existem por convite: não há cadastro aberto.',f'<span class="btn">{i("eye",14)} Ver como</span><span class="btn p">{i("plus",14)} Convidar pessoa da rede</span>')+f'''
<div class="tabs"><a>Pessoas <span class="n">475</span></a><a class="on">Perfis e permissões</a><a>Convites <span class="n">6</span></a><a>Provisionar unidade</a></div>
<div class="g" style="grid-template-columns:220px 1fr 290px">
 <div class="card" style="padding:12px">'''+''.join(f'<div class="meta" style="font-weight:600;text-transform:uppercase;letter-spacing:.06em;padding:10px 8px 4px">{g}</div>'+''.join(f'<div style="display:flex;padding:8px;border-radius:9px;{"background:var(--lilas-100);color:var(--roxo-700);font-weight:600" if n=="Marketing" else ""}"><span>{n}</span><span class="meta" style="margin-left:auto">{q}</span></div>' for n,q in it) for g,it in perfis)+f'''<span class="btn s" style="margin:10px 8px 4px">{i('plus',12)} Perfil personalizado</span></div>
 <div class="card"><div class="hd"><div><h3>Marketing</h3><div class="meta">Perfil padrão de rede · 4 pessoas · teto do nível rede</div></div><div class="dir"><span class="sw"><span class="on">Rede</span><span>Regional</span><span>Unidade</span></span></div></div>
  <table class="t"><thead><tr><th>Módulo</th><th style="text-align:center">Ver</th><th style="text-align:center">Editar</th><th style="text-align:center">Aprovar</th><th style="text-align:center">Exportar</th><th>Limite</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{m}</b></td>{"".join(celula(a,x) for x in acoes)}<td class="meta">{e}</td></tr>' for m,a,e in mods)+f'''</tbody></table>
  <div class="aviso l" style="margin-top:14px"><div>{i('shield',16)}</div><div style="font-size:13px"><b>Verificação em duas etapas obrigatória</b> para todo perfil que vê dados pessoais ou edita a ficha: todos os perfis da rede, gestor regional, admin e gerente da unidade. Recepção usa 2FA se a rede ativar.</div></div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>{i('pin',15)} Como uma unidade ganha acesso</h3></div>
   <div class="lista-i" style="font-size:13px">'''+''.join(f'<div class="it" style="align-items:flex-start"><span style="width:26px;height:26px;border-radius:50%;background:var(--lilas-100);color:var(--roxo-700);display:grid;place-items:center;font:600 13px Poppins;flex:none">{n}</span><div><b>{t}</b><div class="meta">{d}</div></div></div>' for n,t,d in [(1,'Rede provisiona a unidade','Cadastro, modelo de ficha e módulos ativos.'),(2,'Convite do admin da unidade','E-mail com link de 72 h. Conta já pronta.'),(3,'Primeiro acesso','Troca de senha e ativação do 2FA.'),(4,'Admin da unidade monta a equipe','Convida gerente e recepção dentro dos perfis que a rede liberou.')])+f'''</div></div>
  <div class="card"><div class="hd"><h3>Visão do admin da unidade</h3><span class="pill z" style="margin-left:auto">prévia</span></div>
   <div class="campo" style="margin-bottom:10px"><label>E-mail da pessoa</label><div class="in">{i('mail',14)} carla.r@exemplo.com.br</div></div>
   <div class="campo" style="margin-bottom:10px"><label>Perfil</label><div class="in">Recepção {i('chevd',13)}</div><div class="ajuda">Opções liberadas pela rede: Gerente da unidade, Recepção. Não é possível criar perfis.</div></div>
   <span class="btn p" style="width:100%">{i('send',14)} Enviar convite</span></div>
 </div>
</div>'''
salvar(ARQ['users'],pagina('Usuários e perfis',app('admin','users',cont),extra_css='table.t td{height:44px}table.t td,table.t th{padding-left:8px;padding-right:8px}'))

# ---------- 17 AUDITORIA GERAL (só rede; pedido do Osmar 21/11 09h52) ----------
import json as _json
AUD=[ # id, quando, quem, perfil, escopo, ação, tipo, módulo, onde, status, solicitante, aprovador, motivo, antes, depois, ip, dispositivo
('A-90412','21/11 09:31','Ingrid N.','Marketing','Rede','Alterou campo da ficha','Alteração','Ficha da unidade','GiO Alto da Lapa · Horário de sábado','Direto (rede)','Ingrid N.','não se aplica','Campanha de fim de ano','9h às 15h','9h às 17h','192.0.2.•••','Chrome · Windows'),
('A-90407','21/11 09:12','Paula C.','Call center','Rede','Viu telefone completo do lead','Dado pessoal','Leads','Lead Mariana S. · GiO Alto da Lapa','Direto','Paula C.','não se aplica','Retorno de ligação','(11) 9••••-••00','(11) 90000-0000 exibido','192.0.2.•••','Chrome · Windows'),
('A-90399','21/11 08:58','Tiago S.','SEO','Rede','Aprovou tag da unidade','Tags','Tracking e tags','GiO Alto da Lapa · GA4 próprio','Aprovado','Renata F. (Admin da unidade)','Tiago S.','Formato e domínio conferidos','sem tag','G-DEMO12345','192.0.2.•••','Firefox · macOS'),
('A-90388','21/11 08:40','Lúcia A.','Admin da rede','Rede','Mudou permissão de perfil','Permissão','Usuários e perfis','Perfil Gerente da unidade · Campanhas','Direto (rede)','Lúcia A.','não se aplica','Liberação da Regional SP','Campanhas: ver','Campanhas: ver e editar','192.0.2.•••','Chrome · macOS'),
('A-90371','21/11 08:15','Ingrid N.','Marketing','Rede','Reprovou campanha','Campanha','Campanhas','GiO Aldeota · Volta às aulas','Rejeitado','Marcos P. (Admin da unidade)','Ingrid N.','Texto promete resultado; ajustar e reenviar','em aprovação','reprovada','192.0.2.•••','Chrome · Windows'),
('A-90360','21/11 07:59','Sistema','Integração','Rede','Enviou campanha','Campanha','Campanhas','Rede · Avaliação gratuita de laser','Aprovado','Ingrid N.','Lúcia A.','Envio agendado','agendada','8.946 mensagens na fila','servidor','coletor da rede'),
('A-90342','20/11 19:03','Carla T.','Admin da unidade','GiO Batel','Enviou para aprovação','Alteração','Ficha da unidade','GiO Batel · Banner de dezembro','Pendente','Carla T.','aguardando','Promoção fora do modelo','Promoção do modelo da rede','Condição especial no pacote de axilas','192.0.2.•••','Safari · iPhone'),
('A-90331','20/11 17:40','Tiago S.','SEO','Rede','Publicou schema base','Configuração','Dados estruturados','Rede · MedicalClinic v4','Direto (rede)','Tiago S.','não se aplica','Ajuste de horário especial','v3','v4','192.0.2.•••','Firefox · macOS'),
('A-90318','20/11 15:22','Renata F.','Admin da unidade','GiO Alto da Lapa','Convidou usuário','Permissão','Usuários e perfis','GiO Alto da Lapa · Recepção','Direto','Renata F.','não se aplica','Nova recepcionista','sem conta','convite para recepcao@exemplo.com.br','192.0.2.•••','Chrome · Android'),
('A-90302','20/11 11:05','Ingrid N.','Marketing','Rede','Exportou CSV','Exportação','Relatórios','Funil por UF','Direto','Ingrid N.','não se aplica','Reunião de diretoria','não se aplica','arquivo agregado, sem dados pessoais','192.0.2.•••','Chrome · Windows'),
('A-90288','20/11 10:30','Lúcia A.','Admin da rede','Rede','Liberou função','Configuração','Controles da rede','Regional SP · Campanhas para clientes','Direto (rede)','Lúcia A.','não se aplica','Regras aprovadas pelo Osmar','bloqueada','liberada (86 unidades)','192.0.2.•••','Chrome · macOS'),
('A-90274','19/11 21:10','Sistema','Integração','Rede','Sincronizou DocBiz','Configuração','Integrações','128 unidades','Direto','Sistema','não se aplica','Rotina diária','sem dados','2 falhas para reprocessar','servidor','rotina agendada')]
COR_ST={'Aprovado':'v','Rejeitado':'r','Pendente':'a','Direto':'z','Direto (rede)':'l'}
TIPOS=['Alteração','Dado pessoal','Permissão','Tags','Campanha','Configuração','Exportação']
def _fil(t,n): return f'<span class="chip">{t} <b>{n}</b> {i("chevd",12)}</span>'
linhas=''.join(f'<tr class="{"sel" if k==0 else ""}" data-id="{r[0]}" data-tipo="{r[6]}" style="cursor:pointer"><td class="meta">{r[1]}</td><td><b>{r[2]}</b><div class="meta trunc" style="max-width:130px">{r[3]}</div></td><td><span class="trunc" style="display:block;max-width:170px">{r[5]}</span><div class="meta">{r[6]}</div></td><td><span class="trunc" style="display:block;max-width:170px">{r[8]}</span><div class="meta trunc" style="max-width:170px">{r[7]}</div></td><td><span class="pill {COR_ST[r[9]]}">{r[9]}</span></td></tr>' for k,r in enumerate(AUD))
def det(r):
    lin=lambda a,b: f'<div class="it" style="padding:7px 0"><span class="meta" style="width:104px;flex:none">{a}</span><span>{b}</span></div>'
    return (f'<div class="hd" style="margin-bottom:8px"><div><div class="meta">{r[0]} · {r[1]}/2026</div><h3 style="margin-top:2px">{r[5]}</h3></div><span class="pill {COR_ST[r[9]]}" style="margin-left:auto">{r[9]}</span></div>'
     f'<div class="meta" style="margin-bottom:10px">{r[8]} · módulo {r[7]}</div>'
     f'<div class="g" style="grid-template-columns:1fr 1fr;gap:8px"><div><div class="meta" style="font-weight:600">ANTES</div><div style="background:var(--vermelho-50);border-radius:10px;padding:10px;font-size:13px;color:#5c1024;margin-top:4px">{r[13]}</div></div><div><div class="meta" style="font-weight:600">DEPOIS</div><div style="background:var(--verde-50);border-radius:10px;padding:10px;font-size:13px;color:#063f2b;margin-top:4px">{r[14]}</div></div></div>'
     f'<div class="lista-i" style="font-size:13px;margin-top:10px">{lin("Quem fez","<b>"+r[2]+" · "+r[3]+"</b>")}{lin("Quem pediu",r[10])}{lin("Quem decidiu",r[11])}{lin("Motivo",r[12])}{lin("IP e aparelho",r[15]+" · "+r[16])}</div>')
dados=_json.dumps({r[0]:det(r) for r in AUD},ensure_ascii=False).replace('</','<\\/')
csvj=_json.dumps([['id','quando','quem','perfil','escopo','acao','tipo','modulo','onde','status','solicitante','aprovador','motivo','antes','depois','ip','dispositivo']]+[list(r) for r in AUD],ensure_ascii=False)
JS="""<script>(function(){var D=__D__,C=__C__,tipo='';
function f(){var n=0;document.querySelectorAll('#aud-tab tbody tr').forEach(function(t){var ok=!tipo||t.dataset.tipo===tipo;t.style.display=ok?'':'none';if(ok)n++;});document.getElementById('aud-cont').textContent=n+(tipo?' eventos com o filtro "'+tipo+'"':' de 14.302 eventos no período');}
document.querySelectorAll('#aud-tipos .chip').forEach(function(c){c.addEventListener('click',function(){document.querySelectorAll('#aud-tipos .chip').forEach(function(x){x.classList.remove('on')});c.classList.add('on');tipo=c.dataset.tipo;f();});});
document.querySelectorAll('#aud-tab tbody tr').forEach(function(t){t.addEventListener('click',function(){document.querySelectorAll('#aud-tab tr.sel').forEach(function(x){x.classList.remove('sel')});t.classList.add('sel');document.getElementById('aud-det').innerHTML=D[t.dataset.id];});});
document.getElementById('aud-csv').addEventListener('click',function(e){e.stopPropagation();var vis=[C[0]];document.querySelectorAll('#aud-tab tbody tr').forEach(function(t){if(t.style.display!=='none'){C.slice(1).forEach(function(r){if(r[0]===t.dataset.id)vis.push(r)})}});
var txt=vis.map(function(r){return r.map(function(v){return '"'+String(v).replace(/"/g,'""')+'"'}).join(';')}).join('\\n');var a=document.createElement('a');a.href=URL.createObjectURL(new Blob(['\\ufeff'+txt],{type:'text/csv'}));a.download='auditoria-demonstracao.csv';document.body.appendChild(a);a.click();a.remove();});})();</script>""".replace('__D__',dados).replace('__C__',csvj)
cont=cabec('Auditoria geral','Tudo o que todos alteram no sistema: rede, regionais, unidades e perfis. Visível só para perfis da rede.',f'{periodo()}<span class="btn p" id="aud-csv" data-acao-propria="1" style="cursor:pointer">{i("down",14)} Exportar CSV</span>')+f'''
<div style="display:flex;gap:8px;margin-bottom:10px;flex-wrap:wrap">{_fil('Pessoa','todas')}{_fil('Perfil','todos')}{_fil('Unidade','todas')}{_fil('Módulo','todos')}{_fil('Status de aprovação','todos')}</div>
<div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap" id="aud-tipos"><span class="chip on" data-tipo="" data-acao-propria="1">Todos os tipos <b>{len(AUD)}</b></span>'''+''.join(f'<span class="chip" data-tipo="{t}" data-acao-propria="1">{t} <b>{sum(1 for r in AUD if r[6]==t)}</b></span>' for t in TIPOS)+f'''</div>
<div class="g" style="grid-template-columns:1fr 380px;align-items:start">
<div class="card" style="padding:0;overflow:hidden"><table class="t" id="aud-tab"><thead><tr><th>Quando</th><th>Quem</th><th>Ação</th><th>Onde</th><th>Status</th></tr></thead><tbody>{linhas}</tbody></table>
<div style="display:flex;padding:12px 16px;border-top:1px solid var(--linha)" class="meta"><span id="aud-cont">{len(AUD)} de 14.302 eventos no período</span><span style="margin-left:auto">IPs mascarados na tela</span></div></div>
<div class="g" style="align-content:start"><div class="card" id="aud-det">{det(AUD[0])}</div>
<div class="card"><div class="hd"><h3>{i('lock',16)} Registro imutável</h3></div><div class="lista-i" style="font-size:13px"><div class="it">{i('check',14)} Só inclusão: ninguém edita nem apaga, nem a rede</div><div class="it">{i('check',14)} Cada registro guarda o resumo do anterior (cadeia verificável)</div><div class="it">{i('clock',14)} Retenção: alterações 5 anos · acessos a dados pessoais 2 anos</div></div></div></div></div>'''+JS
salvar(ARQ['aud'],pagina('Auditoria geral',app('admin','aud',cont),extra_css='table.t td,table.t th{padding-left:10px;padding-right:10px}#aud-tipos .chip{cursor:pointer}'))

# ---------- 18 LGPD ----------
ped=[('#L-118','Eliminação de dados','Titular via formulário','GiO Batel','a','vence em 4 dias'),('#L-117','Acesso aos dados','Titular via e-mail','GiO Cambuí','v','vence em 9 dias'),('#L-116','Revogação de marketing','Titular via WhatsApp','GiO Alto da Lapa','v','vence em 12 dias'),('#L-114','Correção de dados','Unidade encaminhou','GiO Bom Fim','r','vence amanhã')]
bases=[('Atendimento ao lead','Procedimentos preliminares de contrato','2 anos sem contrato, depois anonimiza'),('Marketing por WhatsApp e e-mail','Consentimento (opcional, desmarcado)','até revogar'),('Prontuário e agenda (DocBiz)','Tutela da saúde · fora deste sistema','regras do DocBiz'),('Auditoria de acessos','Obrigação legal e legítimo interesse','5 anos escritas · 2 anos leituras')]
cont=cabec('LGPD','A rede é a controladora. Unidades atuam como operadoras, com o mínimo de acesso necessário.',f'<span class="btn">{i("file",14)} Aviso de privacidade v3</span><span class="btn p">{i("plus",14)} Registrar pedido</span>')+f'''
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">{kpi('inbox','Pedidos abertos','4','prazo interno de 15 dias')}{kpi('clock','Tempo médio de resposta','6 dias','últimos 90 dias')}{kpi('shield','Leads com consentimento de marketing','61%','opt-in desmarcado por padrão')}{kpi('lock','Anonimizações no mês','312','fim do prazo de retenção')}</div>
<div class="g" style="grid-template-columns:1.2fr 1fr">
 <div class="card" style="padding:0"><div class="hd" style="padding:16px 18px 0"><h3>Pedidos de titulares</h3><span class="sub">centralizados na rede</span></div>
  <table class="t"><thead><tr><th>Pedido</th><th>Tipo</th><th>Unidade</th><th>Prazo</th></tr></thead><tbody>'''+''.join(f'<tr><td><b>{n}</b></td><td>{t}<div class="meta">{o}</div></td><td>{u}</td><td><span class="pill {c}">{p}</span></td></tr>' for n,t,o,u,c,p in ped)+f'''</tbody></table>
  <div class="aviso l" style="margin:14px 18px 18px"><div>{i('users',16)}</div><div style="font-size:13px">Pedido que chega na unidade é encaminhado para a rede com um botão. A unidade não exclui nem exporta dados por conta própria.</div></div></div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Bases legais e retenção</h3></div>
   <div class="lista-i" style="font-size:13px">'''+''.join(f'<div class="it" style="align-items:flex-start"><div style="flex:1"><b>{f}</b><div class="meta">{b}</div></div><span class="meta" style="text-align:right;max-width:150px">{r}</span></div>' for f,b,r in bases)+f'''</div></div>
  <div class="card"><div class="hd"><h3>Mascaramento por perfil</h3></div>
   <table class="t" style="font-size:13px;table-layout:fixed"><thead><tr><th style="width:38%">Perfil</th><th>Telefone</th><th style="width:28%">Exporta</th></tr></thead><tbody>
   <tr><td>Call center</td><td>completo</td><td>não</td></tr><tr><td style="white-space:normal">Admin e gerente</td><td style="white-space:normal">completo, só da unidade</td><td style="white-space:normal">sem dados pessoais</td></tr><tr><td>Recepção</td><td style="white-space:normal">mascarado, age por botão</td><td>não</td></tr><tr><td style="white-space:normal">Marketing, SEO, regional</td><td>mascarado</td><td style="white-space:normal">sem dados pessoais</td></tr></tbody></table></div>
 </div>
</div>'''
salvar(ARQ['lgpd'],pagina('LGPD',app('admin','lgpd',cont)))
print('s3 ok')
