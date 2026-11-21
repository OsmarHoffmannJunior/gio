from base import *
random.seed(21)
# ---------- 01 LOGIN (sem "criar conta": contas internas são provisionadas pela rede) ----------
def painel_marca(titulo,texto,foto='recepcao.jpg'):
    return f'''<div class="acesso-marca" style="background:var(--grad);position:relative;overflow:hidden;color:#fff;padding:56px 64px;display:flex;flex-direction:column">
 <div style="position:absolute;inset:0;background:url(../assets/fotos/{foto}) center/cover;opacity:.18;mix-blend-mode:luminosity"></div>
 <div style="position:absolute;right:-140px;top:-140px;width:520px;height:520px;border-radius:50%;border:1px solid rgba(255,255,255,.18)"></div>
 <img class="logo" src="../assets/logo-gio-branco.png" alt="Gio" style="height:64px;width:auto;align-self:flex-start;position:relative">
 <div style="margin-top:auto;position:relative;max-width:620px">
  <h1 style="font-size:42px;line-height:1.12;font-weight:600;margin:0 0 14px">{titulo}</h1>
  <p style="font-size:17px;max-width:540px">{texto}</p>
 </div></div>'''
papeis=[('Franqueado','Acesse com o e-mail do convite que a rede enviou quando sua unidade foi ativada.'),('Rede Gio','Equipes da franqueadora: marketing, SEO, comercial, call center e financeiro.'),('Parceiro','Agências e fornecedores autorizados pela rede, com acesso por tempo limitado.')]
corpo=f'''<div class="acesso">
{painel_marca('Cada unidade com página própria, leads no lugar certo e a rede inteira em um painel.','Franqueadora, franqueados, call center e parceiros trabalhando sobre os mesmos dados, cada um no seu escopo.')}
<div class="acesso-form">
 <div style="display:flex;align-items:center;gap:10px;margin-bottom:6px"><h2 style="font-size:26px;font-weight:600">Entrar</h2><span style="margin-left:auto">{selo()}</span></div>
 <p class="muted" style="margin:0 0 22px">Não existe cadastro aberto. Sua conta é criada pela rede (ou pelo admin da sua unidade) e chega por convite no seu e-mail.</p>
 <div class="sw" role="tablist" style="margin-bottom:10px;width:100%;display:grid;grid-template-columns:1fr 1fr 1fr">'''+''.join(f'<span class="{"on" if k==0 else ""}" style="justify-content:center">{p}</span>' for k,(p,_) in enumerate(papeis))+f'''</div>
 <p class="meta" style="margin-bottom:20px">{papeis[0][1]}</p>
 <div class="campo" style="margin-bottom:14px"><label>E-mail</label><div class="in">{i('mail',15)} renata.f@exemplo.com.br</div></div>
 <div class="campo" style="margin-bottom:8px"><label>Senha</label><div class="in">{i('lock',15)} ••••••••••<span style="margin-left:auto" title="Mostrar senha">{i('eye',15)}</span></div></div>
 <div style="display:flex;flex-wrap:wrap;gap:10px 16px;justify-content:space-between;align-items:center;margin:8px 0 22px;font-size:14px"><span style="display:flex;gap:8px;align-items:center"><span class="cx" style="flex:none"></span> Manter conectado neste aparelho</span><a class="lk" href="{L('senha')}">Esqueci a senha</a></div>
 <a class="btn p" href="{L('2fa')}" style="padding:13px">Entrar no portal {i('chev',14)}</a>
 <div style="display:flex;align-items:center;gap:12px;margin:20px 0;color:var(--tinta-3);font-size:13px"><span style="flex:1;height:1px;background:var(--linha)"></span>ou<span style="flex:1;height:1px;background:var(--linha)"></span></div>
 <a class="btn" href="{L('2fa')}" style="padding:12px">{i('google',16)} Entrar com conta Google da rede</a>
 <div class="aviso l" style="margin-top:24px"><div class="ic l">{i('mail',16)}</div><div><b>Primeiro acesso?</b><div class="meta" style="margin-top:2px">Abra o convite enviado pela rede e defina sua senha. O convite vale 72 horas. <a class="lk" href="{L('senha')}">Ver como funciona</a></div></div></div>
 <p class="meta" style="margin-top:22px">Ao entrar você concorda com os <a class="lk">Termos de Uso</a> e a <a class="lk">Política de Privacidade</a> da rede. Acessos e exportações ficam registrados na auditoria.</p>
</div></div>'''
salvar(ARQ['login'],pagina('Entrar',corpo))

# ---------- 02 2FA (código, erro, bloqueio) ----------
def digitos(vals,err=False,peq=False):
    at=len([v for v in vals if v])
    return f'<div class="otp{" err" if err else ""}{" p" if peq else ""}" role="group" aria-label="Código de 6 números">'+''.join(f'<div class="{"at" if (k==at and not err) else ""}">{v}</div>' for k,v in enumerate(vals))+'</div>'
corpo=f'''<div class="acesso">
{painel_marca('Verificação em duas etapas','Obrigatória para todos os perfis com acesso a dados de clientes. Protege leads, consentimentos e a página da sua unidade.','espera.jpg')}
<div class="acesso-form" style="gap:18px">
 <div style="display:flex;align-items:center"><a class="lk" href="{L('login')}">{i('chev',12)} Voltar</a><span style="margin-left:auto">{selo()}</span></div>
 <div class="card" style="box-shadow:none">
  <div class="ic l" style="margin-bottom:12px">{i('phone2',16)}</div>
  <h2 style="font-size:22px;font-weight:600">Digite o código do aplicativo</h2>
  <p class="muted" style="margin:4px 0 18px">Abra o autenticador cadastrado para <span class="num">renata.f@exemplo.com.br</span> e digite os 6&nbsp;números.</p>
  {digitos(['4','8','1','','',''])}
  <div style="display:flex;gap:8px;align-items:center;margin:16px 0 18px"><span class="cx" style="flex:none"></span> Confiar neste aparelho por 30&nbsp;dias</div>
  <a class="btn p" href="{L('f-inicio')}" style="width:100%;padding:12px">Confirmar</a>
  <div class="alt2fa">
   <div class="meta" style="font-weight:600;color:var(--tinta-2)">Sem acesso ao aplicativo?</div>
   <div class="it"><span>Receber por SMS no <span class="num">(11) •••••-4821</span></span><span class="meta num">reenviar em 0:28</span></div>
   <div class="it"><span>Usar um código de recuperação<span class="meta" style="display:block">Formato <span class="num">4F7K-92QD</span>, cada código vale uma vez</span></span><a class="lk" href="{L('f-inicio')}">Usar código</a></div>
  </div>
 </div>
 <div class="meta" style="font-weight:600;text-transform:uppercase;letter-spacing:.06em">Estados de erro</div>
 <div class="g" style="grid-template-columns:1fr 1fr">
  <div class="card" style="box-shadow:none;padding:16px">{digitos(['4','8','1','9','0','2'],True,True)}
   <div class="campo" style="margin-top:10px"><div class="erro">{i('alert',12)} Código incorreto. Restam 2&nbsp;tentativas.</div></div></div>
  <div class="card" style="box-shadow:none;padding:16px"><div class="aviso r" style="padding:10px"><div>{i('lock',16)}</div><div><b>Acesso bloqueado por <span class="num">15 min</span></b><div style="font-size:12px;margin-top:2px">5 tentativas erradas. Avisamos o admin da unidade e a rede.</div></div></div></div>
 </div>
</div></div>'''
salvar(ARQ['2fa'],pagina('Verificação em duas etapas',corpo))

# ---------- 03 PRIMEIRO ACESSO (convite) E ESQUECI A SENHA ----------
def etapa(n,t,on):
    return f'<div style="display:flex;gap:10px;align-items:center"><span style="width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font:600 13px Poppins;{"background:var(--vinho);color:#fff" if on else "background:var(--lilas-100);color:var(--roxo-700)"}">{n}</span><span style="font-weight:{600 if on else 500}">{t}</span></div>'
crit=[('Mínimo de 12 caracteres',True),('Uma letra maiúscula e um número',True),('Diferente das 5 últimas senhas',True),('Não contém seu nome ou e-mail',False)]
corpo=f'''<div class="acesso-pg" style="width:100%;min-height:100vh;background:var(--fundo);padding:40px var(--cli-pad)">
 <div style="display:flex;flex-wrap:wrap;align-items:center;gap:10px 14px;margin-bottom:26px"><img src="../assets/logo-gio.png" alt="Gio" style="height:44px"><span class="muted" style="font-weight:600">Portal do Franqueado</span><span style="margin-left:auto">{selo()}</span></div>
 <h1 style="font-size:26px;font-weight:600">Primeiro acesso e recuperação de senha</h1>
 <p class="muted" style="margin:4px 0 22px;max-width:900px">Não há cadastro aberto. A rede provisiona a unidade e envia o convite da conta de admin da unidade. No primeiro acesso a pessoa define a senha, ativa a verificação em duas etapas e depois convida a própria equipe dentro dos perfis permitidos.</p>
 <div class="g" style="grid-template-columns:1.05fr 1fr 1fr;align-items:start">
  <div class="card">
   <div class="meta" style="font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-bottom:12px">1 · E-mail de convite</div>
   <div style="border:1px solid var(--linha);border-radius:12px;overflow:hidden">
    <div style="background:var(--grad);padding:16px 18px"><img src="../assets/logo-gio-branco.png" alt="Gio" style="height:30px"></div>
    <div style="padding:18px">
     <div class="meta">De: Rede Gio &lt;acesso@exemplo.com.br&gt;</div>
     <h3 style="font-size:17px;font-weight:600;margin:8px 0">Sua unidade GiO Alto da Lapa está pronta</h3>
     <p style="color:var(--tinta-2)">Olá, Renata. A rede criou o acesso de <b>admin da unidade</b> para você. Defina sua senha para começar.</p>
     <a class="btn p" href="#definir" style="margin:14px 0">Definir minha senha</a>
     <p class="meta">O link vale 72 horas e só funciona uma vez. Se você não esperava este e-mail, ignore e avise suporte@exemplo.com.br.</p>
    </div></div>
  </div>
  <div class="card" id="definir">
   <div class="meta" style="font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-bottom:12px">2 · Definir senha e ativar 2FA</div>
   <div style="display:flex;flex-direction:column;gap:8px;margin-bottom:16px">{etapa(1,'Criar senha',True)}{etapa(2,'Ativar verificação em duas etapas',False)}{etapa(3,'Convidar sua equipe (opcional)',False)}</div>
   <div class="campo" style="margin-bottom:12px"><label>E-mail da conta</label><div class="in lock">{i('lock',14)} renata.f@exemplo.com.br</div><div class="ajuda">Definido pela rede no convite. Para trocar, fale com o suporte.</div></div>
   <div class="campo" style="margin-bottom:10px"><label>Nova senha</label><div class="in">{i('lock',15)} ••••••••••••••<span style="margin-left:auto">{i('eye',15)}</span></div></div>
   <div style="display:flex;gap:4px;margin-bottom:6px">'''+''.join(f'<span style="flex:1;height:5px;border-radius:4px;background:{"var(--verde)" if k<3 else "var(--lilas-200)"}"></span>' for k in range(4))+'''</div><div class="meta" style="margin-bottom:10px">Força da senha: <b style="color:var(--verde)">boa</b></div>
   <div style="display:flex;flex-direction:column;gap:6px;margin-bottom:16px">'''+''.join(f'<div style="display:flex;gap:8px;align-items:center;font-size:13px;color:{"var(--verde)" if ok else "var(--vermelho)"}">{i("check" if ok else "x",14)}<span style="color:var(--tinta-2)">{t}</span></div>' for t,ok in crit)+f'''</div>
   <span class="btn off" style="width:100%">Continuar para o 2FA</span>
   <div class="meta" style="margin-top:8px">O botão libera quando todos os critérios forem atendidos.</div>
  </div>
  <div class="g" style="align-content:start">
   <div class="card">
    <div class="meta" style="font-weight:600;text-transform:uppercase;letter-spacing:.06em;margin-bottom:12px">Esqueci a senha</div>
    <div class="campo" style="margin-bottom:12px"><label>E-mail da conta</label><div class="in">{i('mail',15)} renata.f@exemplo.com.br</div></div>
    <a class="btn p" style="width:100%">Enviar link de redefinição</a>
    <p class="meta" style="margin-top:10px">Por segurança, mostramos a mesma mensagem exista ou não a conta.</p>
   </div>
   <div class="card" style="background:var(--verde-50);border-color:#b5e2cf"><div style="display:flex;gap:12px"><div class="ic v">{i('send',16)}</div><div><b>Se o e-mail estiver cadastrado, o link chega em instantes</b><div class="meta" style="margin-top:4px;color:#063f2b">Vale 30 minutos. Depois de redefinir, a verificação em duas etapas continua ativa e todas as sessões abertas são encerradas.</div></div></div></div>
   <div class="card"><div style="display:flex;gap:12px"><div class="ic a">{i('alert',16)}</div><div><b>Link expirado</b><div class="meta" style="margin-top:4px">Peça um novo link. Convites de primeiro acesso vencidos só a rede reenvia, em Usuários e perfis.</div><a class="lk" href="{L('login')}" style="display:inline-block;margin-top:8px">Voltar para o login</a></div></div></div>
  </div>
 </div>
</div>'''
salvar(ARQ['senha'],pagina('Primeiro acesso e senha',corpo))

# ---------- 04 DASHBOARD DA REDE ----------
dias=[f'{d:02d}/11' for d in range(1,22)]
leads=[118,131,125,140,152,98,87,144,151,160,149,171,120,102,166,174,180,169,188,140,121]
agend=[int(v*0.58+random.randint(-6,6)) for v in leads]
comp=[int(v*0.62+random.randint(-4,4)) for v in agend]
alerts=[('r','alert','17 unidades com GTM próprio','Conversões fora do padrão da rede','seo'),('a','image','70 unidades sem foto','Completude média cai 18 pontos','unidades'),('a','pin',f'{len(SEM_COORD)} unidades sem coordenadas','Fora do mapa e do schema','mapa'),('r','google','3 perfis do Google divergem da ficha','Comparação NAP. A unidade corrige no Google','seo'),('a','clock','9 leads fora do SLA agora','Call center Sul e Nordeste','leads')]
mapa=mapa_br(360,350,pontos_unidades(4),UF_CONT,'SP')
cont=f'''
<div class="cab"><div><h1>Visão geral da rede</h1><p>Leads, agendamentos e saúde das 130 unidades.</p></div>
<div class="dir">{periodo()}<span class="btn">{i('filter',14)} Filtros</span><span class="btn p">{i('down',14)} Exportar</span></div></div>
<div class="g" style="grid-template-columns:repeat(5,1fr);margin-bottom:16px">
 {kpi('inbox','Leads','2.986','<span class="up">+14,2%</span> vs. outubro')}
 {kpi('cal','Agendados','1.733','<span class="up">+9,8%</span> · 58% dos leads')}
 {kpi('check','Compareceram','1.071','<span class="up">+6,1%</span> · fonte DocBiz')}
 {kpi('clock','1º contato (mediana)','11 min','<span class="up">−2 min</span> vs. outubro · meta 15')}
 {kpi('target','Completude média',f'{COMPL_MEDIA}%',f'<span class="down">{CL_TOT["r"]+CL_TOT["a"]} unidades</span> abaixo de 80%')}
</div>
<div class="g" style="grid-template-columns:1.55fr 1fr;margin-bottom:16px">
 <div class="card"><div class="hd"><h3>Funil diário da rede</h3><div class="leg" style="margin-left:14px"><span><i style="background:#4c1455"></i>Leads</span><span><i style="background:#b0197e"></i>Agendados</span><span><i style="background:#e5559f"></i>Compareceram</span></div></div>
 {area([leads,agend,comp],['#4c1455','#b0197e','#e5559f'],w=700,h=250,labels=dias)}</div>
 <div class="card"><div class="hd"><h3>{i('trend',16)} Índice de conversão</h3><a class="lk" href="{L('rel')}" style="margin-left:auto;font-size:13px">Como é calculado</a></div>
 <p class="meta" style="margin:-6px 0 8px">Mesmo índice mostrado no painel do franqueado. 0 a 100, pondera agendamento e comparecimento.</p>
 <div class="lista-i">'''+''.join(f'<a class="it" href="{L("unidade")}"><span class="pop" style="width:20px;font-weight:600;color:var(--vinho)">{k+1}º</span><div style="flex:1;min-width:0"><b class="trunc" style="display:block">{n}</b><span class="barra" style="width:100%;margin-top:5px"><i style="width:{v}%"></i></span></div><b style="width:28px;text-align:right">{v}</b><span class="up" style="width:30px;text-align:right;font-size:13px">{d}</span></a>' for k,(_,n,v,d) in enumerate(RANKING))+f'''</div></div>
</div>
<div class="g" style="grid-template-columns:1.25fr 1fr">
 <div class="card"><div class="hd"><h3>{i('map',16)} Unidades por estado</h3><span class="sub">clique no estado para filtrar</span><a class="btn s" href="{L('mapa')}" style="margin-left:auto">Abrir mapa completo {i('chev',12)}</a></div>
  <div style="display:grid;grid-template-columns:360px 1fr;gap:16px;align-items:start">
   <div style="position:relative">{mapa}
    <div style="display:flex;gap:8px;align-items:center;margin-top:6px"><span class="pill l">{i('pin',11)} SP selecionado · {UF_CONT['SP']} unidades</span><span class="credito">Malha: IBGE</span></div></div>
   <div><table class="t" style="font-size:13px"><thead><tr><th>UF</th><th class="num">Unidades</th></tr></thead><tbody>'''+''.join(f'<tr class="{"sel" if uf=="SP" else ""}"><td>{uf}</td><td class="num"><b>{v}</b></td></tr>' for uf,v in uf_top())+f'''<tr><td><b>Total</b></td><td class="num"><b>{sum(UF_CONT.values())}</b></td></tr></tbody></table>
   <div class="leg" style="flex-direction:column;gap:6px;margin-top:14px"><span><i style="background:{COR_CL['v']}"></i>80% ou mais · {CL_MAPA['v']}</span><span><i style="background:{COR_CL['a']}"></i>55% a 79% · {CL_MAPA['a']}</span><span><i style="background:{COR_CL['r']}"></i>abaixo de 55% · {CL_MAPA['r']}</span><span class="meta">{sum(CL_MAPA.values())} no mapa + {len(SEM_COORD)} sem coordenadas = 130</span></div></div>
  </div></div>
 <div class="card"><div class="hd"><h3>{i('alert',16)} Alertas da rede</h3><span class="pill r" style="margin-left:auto">5 abertos</span></div>
 <div class="lista-i">'''+''.join(f'<a class="it" href="{L(lk)}"><div class="ic {c}">{i(ic,15)}</div><div style="flex:1;min-width:0"><b class="trunc" style="display:block">{t}</b><span class="muted trunc" style="display:block;font-size:13px">{s}</span></div>{i("chev",14)}</a>' for c,ic,t,s,lk in alerts)+f'''</div>
 <a class="aviso l" href="{L('insights')}" style="margin-top:14px"><div class="ic l">{i('sparkle',15)}</div><div><b>3 insights novos</b><div class="meta">Queda de leads em Goiás e mais 2. Ver relatórios inteligentes.</div></div></a></div>
</div>'''
salvar(ARQ['rede'],pagina('Visão geral da rede',app('admin','rede',cont)))

# ---------- 05 TABELA DE UNIDADES ----------
ordem=['altodalapa','curitiba','campinas-cambui','boulevardtatuape','porto-alegre-bom-fim','ribeirao-preto-centro','aldeota','asa-sul','salvador','vila-madalena','londrina','montes-claros','ipiranga','go-catalao-centro']
amostra=sorted([u for u in UNID if u['url_site'] in ordem],key=lambda u: -completude(u))
info={'altodalapa':('B','Próprio',41),'curitiba':('A','Próprio',63),'campinas-cambui':('C','Ficha',58),'boulevardtatuape':('C','Ficha',49),'porto-alegre-bom-fim':('A','Ficha',37),'ribeirao-preto-centro':('B','Ficha',33),'aldeota':('A','Ficha',29),'asa-sul':('C','Ficha',31),'salvador':('A','Ficha',22),'vila-madalena':('A','Ficha',26),'londrina':('B','Ficha',18),'montes-claros':('A','Ficha',9),'ipiranga':('A','Ficha',14),'go-catalao-centro':('Sem','Ficha',4)}
alertas={'altodalapa':['GBP diverge da ficha'],'curitiba':[],'campinas-cambui':['GBP diverge da ficha'],'boulevardtatuape':['GTM próprio'],'porto-alegre-bom-fim':['GBP sem telefone'],'ribeirao-preto-centro':['GTM próprio'],'aldeota':[],'asa-sul':['GBP sem site'],'salvador':['Poucas fotos'],'vila-madalena':['Sem FAQ'],'londrina':['Texto padrão'],'montes-claros':['Texto padrão','Sem fotos'],'ipiranga':['Sem coordenadas'],'go-catalao-centro':['Sem tratamentos','Sem fotos']}
fotos=['fachada','recepcao','sala-laser','sala-facial','espera','equipe']
linhas=''
for k,u in enumerate(amostra):
    s=u['url_site']; c=completude(u); tpl,dom,ln=info[s]; al=alertas[s]
    alh=(''.join(f'<span class="pill {"r" if a in ("Sem coordenadas","GTM próprio","Sem tratamentos") else "a"}">{a}</span>' for a in al[:1])+(f' <span class="pill z">+{len(al)-1}</span>' if len(al)>1 else '')) or '<span class="pill v"><i></i>Tudo certo</span>'
    sel=k in (1,2)
    linhas+=f'''<tr class="{"sel" if sel else ""}"><td><span class="cx{" on" if sel else ""}"></span></td>
<td><a class="un" href="{L('unidade')}"><div class="ft" style="background-image:url(../assets/fotos/{fotos[k%6]}.jpg)"></div><div><b class="trunc" style="max-width:170px">{nome_un(u)}</b><small>{u["bairro"][:24]}</small></div></a></td>
<td><span class="trunc" style="display:block;max-width:140px">{u["nome_cidade"]}/{u["nome_uf"]}</span></td>
<td><span class="barra"><i style="width:{c}%"></i></span> <b style="margin-left:6px">{c}%</b></td>
<td>{"<span class='pill z'>Sem modelo</span>" if tpl=="Sem" else f"<span class='pill l'>Modelo {tpl}</span>"}</td>
<td>{"<span class='pill b'>"+i('globe',11)+" Próprio</span>" if dom=="Próprio" else "<span class='muted'>Ficha oficial</span>"}</td>
<td class="num"><b>{ln}</b></td><td>{alh}</td><td><a href="{L('unidade')}" title="Abrir">{i('chev',16)}</a></td></tr>'''
cont=f'''
<div class="cab"><div><h1>Unidades</h1><p>130 ativas em {len(UF_CONT)} estados. Clique numa linha para abrir a unidade.</p></div>
<div class="dir"><span class="sw"><a class="on" href="{L('unidades')}">{i('list',13)} Tabela</a><a href="{L('mapa')}">{i('map',13)} Mapa</a></span><span class="btn">{i('down',14)} Exportar</span><span class="btn p">{i('plus',14)} Provisionar unidade</span></div></div>
<div class="g" style="grid-template-columns:repeat(6,1fr);margin-bottom:14px">'''+''.join(f'<div class="card" style="padding:13px 15px"><div class="muted" style="font-weight:500">{a}</div><div class="pop" style="font-size:22px;font-weight:600;margin-top:2px;color:{c}">{b}</div></div>' for a,b,c in [('Ativas','130','var(--tinta)'),('Completude 80% ou mais',CL_TOT['v'],'var(--verde)'),('55% a 79%',CL_TOT['a'],'var(--ambar)'),('Abaixo de 55%',CL_TOT['r'],'var(--vermelho)'),('Com domínio próprio','9','var(--azul)'),('Sem coordenadas',len(SEM_COORD),'var(--vermelho)')])+f'''</div>
<div class="card" style="padding:0">
 <div style="display:flex;gap:8px;align-items:center;padding:14px 16px;flex-wrap:wrap;border-bottom:1px solid var(--linha)">
  <div style="display:flex;align-items:center;gap:8px;border:1px solid var(--linha-forte);border-radius:10px;padding:7px 10px;width:270px;color:var(--tinta-3);min-height:36px">{i('search',14)} Nome, cidade, CEP ou ID DocBiz</div>
  <span class="chip on">Estado: <b>Todos</b> {i('chevd',12)}</span><span class="chip">Completude {i('chevd',12)}</span><span class="chip">Modelo {i('chevd',12)}</span><span class="chip">Domínio {i('chevd',12)}</span><span class="chip">Alertas {i('chevd',12)}</span><span class="chip">Regional {i('chevd',12)}</span>
  <span style="margin-left:auto" class="muted">{i('eye',14)} Visão salva: <b style="color:var(--roxo-700)">Prioridade SEO do mês</b></span>
 </div>
 <div class="tb-bulk" style="border-radius:0"><b>2 selecionadas</b><span class="btn s">{i('edit',13)} Editar em lote</span><span class="btn s">{i('layout',13)} Trocar modelo</span><span class="btn s">{i('send',13)} Notificar unidades</span><span class="btn s">{i('down',13)} Exportar</span><span style="margin-left:auto;font-size:13px">Edições em lote exigem motivo e geram aviso às unidades</span></div>
 <table class="t"><thead><tr><th><span class="cx"></span></th><th>Unidade</th><th>Cidade</th><th>Completude</th><th>Modelo</th><th>Domínio</th><th class="num">Leads 30d</th><th>Alertas</th><th></th></tr></thead><tbody>{linhas}</tbody></table>
 <div style="display:flex;align-items:center;padding:12px 16px;border-top:1px solid var(--linha)" class="muted"><span>Mostrando 14 de 130 · ordenado por completude · leads 30d somam 2.986 na rede</span><span style="margin-left:auto;display:flex;gap:6px"><span class="btn s">Anterior</span><span class="btn s" style="background:var(--lilas-100);color:var(--roxo-700)">1</span><span class="btn s">2</span><span class="btn s">3</span><span class="btn s">10</span><span class="btn s">Próxima</span></span></div>
</div>'''
salvar(ARQ['unidades'],pagina('Unidades',app('admin','unidades',cont),extra_css='table.t td,table.t th{padding-left:10px;padding-right:10px}'))

# ---------- 06 MAPA DE UNIDADES ----------
mapa=mapa_br(760,720,pontos_unidades(6),UF_CONT,'SP')
box_sp=(-24.05,-23.25,-47.05,-46.25)
zoom=mapa_geo(380,270,[(a,b,c,7) for a,b,c,_ in pontos_unidades()],box_sp,UF_CONT,None,rotulos=False)
dentro=sum(1 for u in COM_COORD if box_sp[0]<=float(u['latitude'])<=box_sp[1] and box_sp[2]<=float(u['longitude'])<=box_sp[3])
cont=f'''
<div class="cab"><div><h1>Unidades no mapa</h1><p>{len(COM_COORD)} unidades com coordenadas no mapa. {len(SEM_COORD)} sem coordenadas ficam na lista ao lado.</p></div>
<div class="dir"><span class="sw"><a href="{L('unidades')}">{i('list',13)} Tabela</a><a class="on" href="{L('mapa')}">{i('map',13)} Mapa</a></span><span class="btn">{i('layout',14)} Camadas</span></div></div>
<div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap"><span class="chip on">Colorir por: <b>Completude</b> {i('chevd',12)}</span><span class="chip">Estados: <b>unidades por UF</b> {i('chevd',12)}</span><span class="chip">Modelo {i('chevd',12)}</span><span class="chip">Domínio próprio {i('chevd',12)}</span><span class="chip">Regional {i('chevd',12)}</span></div>
<div class="g" style="grid-template-columns:1fr 390px">
 <div class="card" style="padding:0;position:relative;overflow:hidden">
  <div style="display:flex;justify-content:center;padding:16px 0 4px;margin-left:120px">{mapa}</div>
  <div class="card" style="position:absolute;left:18px;top:18px;padding:14px"><div class="leg" style="flex-direction:column;gap:7px"><b style="font-size:13px">Completude da página</b><span><i style="background:{COR_CL['v']};border-radius:50%"></i>80% ou mais · {CL_MAPA['v']}</span><span><i style="background:{COR_CL['a']};border-radius:50%"></i>55% a 79% · {CL_MAPA['a']}</span><span><i style="background:{COR_CL['r']};border-radius:50%"></i>abaixo de 55% · {CL_MAPA['r']}</span>
   <span style="border-top:1px solid var(--linha);padding-top:7px"><b>{sum(CL_MAPA.values())}</b> no mapa + <b>{len(SEM_COORD)}</b> fora = <b>130</b></span>
   <b style="font-size:13px;margin-top:6px">Unidades por UF</b>'''+''.join(f'<span><i style="background:{c}"></i>{t}</span>' for c,t in [('#a877bd','40 ou mais'),('#c39ad3','8 a 39'),('#d8bde3','3 a 7'),('#ead9f0','1 a 2'),('#f7f1f9;border:1px solid #d9c3e1','nenhuma')])+f'''</div></div>
  <div style="position:absolute;right:18px;top:18px;display:flex;flex-direction:column;gap:6px"><div class="ib">{i('plus')}</div><div class="ib"><svg class="i" viewBox="0 0 24 24"><path d="M5 12h14"/></svg></div><div class="ib">{i('target')}</div></div>
  <div class="card" style="position:absolute;left:380px;top:470px;width:300px;padding:14px;box-shadow:0 10px 30px rgba(36,8,44,.18)">
   <div class="un"><div class="ft" style="background-image:url(../assets/fotos/fachada.jpg);width:44px;height:44px"></div><div><b>GiO Alto da Lapa</b><small>Alto da Lapa · São Paulo/SP</small></div></div>
   <div class="g" style="grid-template-columns:repeat(3,1fr);gap:8px;margin:12px 0"><div><div class="meta">Completude</div><b>90%</b></div><div><div class="meta">Leads 30d</div><b>41</b></div><div><div class="meta">Índice</div><b>90 · 4º</b></div></div>
   <div style="display:flex;gap:6px"><a class="btn s p" href="{L('unidade')}">Abrir unidade</a><a class="btn s" href="{L('lpB')}">Ver página</a></div></div>
  <div class="credito" style="position:absolute;right:18px;bottom:12px">Malha: IBGE</div>
 </div>
 <div class="g" style="align-content:start">
  <div class="card"><div class="hd"><h3>Grande São Paulo</h3><span class="sub" style="margin-left:auto">{dentro} unidades no recorte</span></div><div style="background:#fbf8fc;border-radius:12px;overflow:hidden">{zoom}</div></div>
  <div class="card"><div class="hd"><h3>{i('alert',15)} Fora do mapa</h3><span class="pill r" style="margin-left:auto">{len(SEM_COORD)}</span></div>
  <div class="lista-i">'''+''.join(f'<div class="it"><div style="flex:1;min-width:0"><b class="trunc" style="display:block">{nome_un(u)}</b><div class="meta">{u["nome_cidade"]}/{u["nome_uf"]} · CEP cadastrado</div></div><span class="btn s">{i("pin",12)} Geocodificar</span></div>' for u in SEM_COORD[:5])+f'''<div class="it muted">e mais {len(SEM_COORD)-5} unidades · <a class="lk" href="{L('unidades')}">ver na tabela</a></div></div></div>
 </div>
</div>'''
salvar(ARQ['mapa'],pagina('Mapa de unidades',app('admin','unidades',cont)))
print('s1 ok')
