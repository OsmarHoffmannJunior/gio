"""Dados de demonstração do hub de relatórios da rede (tela 13 e subtelas 90 a 99). Tudo fictício e coerente
com as telas 04 (2.986 leads, 2.541 em contato, 1.733 agendados, 1.071 compareceram, 1º contato 11 min),
24 (Alto da Lapa 41/26/17, 9 min), 62 (campanhas para clientes: 214 agendamentos e 131 comparecimentos),
63 a 70 (quiz e eventos) e 84 (avaliações). Período 01 a 21 nov 2026; comparação 01 a 21 out 2026 e 01 a 21 nov 2025."""
from base import *
R=random.Random(90)
def dist(total,pesos):
    """Distribui um total inteiro proporcional aos pesos (maior resto): a soma bate exatamente."""
    s=sum(pesos) or 1; bruto=[total*p/s for p in pesos]; base=[int(b) for b in bruto]
    falta=total-sum(base)
    for k in sorted(range(len(pesos)),key=lambda k:bruto[k]-base[k],reverse=True)[:falta]: base[k]+=1
    return base
def brl(v,d=0):
    s=f'{v:,.{d}f}'.replace(',','X').replace('.',',').replace('X','.'); return 'R$ '+s
def pct(a,b,d=1):
    return (f'{a/b*100:.{d}f}'.replace('.',',')+'%') if b else '0%'
def var(a,b):
    v=(a/b-1)*100; s=('+' if v>=0 else '−')+f'{abs(v):.1f}'.replace('.',',')+'%'; return s,v
def br(x,d=1): return f'{x:.{d}f}'.replace('.',',')
PER='01 a 21 nov 2026'; PER_ANT='01 a 21 out 2026'; PER_AA='01 a 21 nov 2025'
ATU='hoje, 16:40'          # horário de Brasília, carimbo de atualização padrão do protótipo
# ---------- totais do período (iguais à tela 04) ----------
L,CT,AG,CP=2986,2541,1733,1071
REALIZ_FALTA=412; FUTUROS=AG-CP-REALIZ_FALTA   # agendamentos ainda por acontecer (data depois de 21/11)
SHOW=CP/(CP+REALIZ_FALTA)
VD=621; TICKET=1180       # vendas de pacote na DocBiz atribuídas (ilustrativo, depende da DocBiz)
ANT=dict(L=2615,AG=1578,CP=1009,VD=566,INV=58210,T1=13)
AA=dict(L=2290,AG=1270,CP=801,VD=455,INV=41300,T1=21)
DIAS=[f'{d:02d}/11' for d in range(1,22)]
LD=[118,131,125,140,152,98,87,144,151,160,149,171,120,102,166,174,180,169,188,140,121]   # mesmo da tela 04
AGD=dist(AG,[v*(0.55+0.08*R.random()) for v in LD]); CPD=dist(CP,[v*(0.58+0.08*R.random()) for v in AGD])
LD_ANT=dist(ANT['L'],[v*(0.8+0.4*R.random()) for v in [112,118,104,121,128,90,79,120,131,129,126,140,99,88,133,139,141,135,148,117,97]])
# ---------- fontes (canal) ----------
# (chave, nome, grupo, leads, cor)
FONTES=[('ga_pesq','Google Ads · Pesquisa','Mídia paga',846,'#4c1455'),('ga_pmax','Google Ads · Performance Max','Mídia paga',289,'#6f0052'),
 ('meta_form','Meta Ads · formulário e landing','Mídia paga',318,'#b0197e'),('meta_wa','Meta Ads · clique para WhatsApp','Mídia paga',190,'#d23c8f'),
 ('seo','Busca orgânica (SEO)','Orgânico',402,'#2C5BC4'),('gbp','Perfil no Google (GBP)','Orgânico',315,'#5b82d6'),('insta','Instagram orgânico','Orgânico',328,'#8fa9e6'),
 ('crm','Campanhas para clientes (e-mail e WhatsApp)','Relacionamento',232,'#0B7A54'),('ind','Indicação','Relacionamento',38,'#4fa784'),('dir','Direto e outros','Outros',28,'#9a8fa1')]
assert sum(f[3] for f in FONTES)==L
# ---------- campanhas pagas ----------
# (plataforma, fonte, nome, escopo, unidades, leads, CPL, tx_agend, status)
CAMP=[('Google Ads','ga_pesq','Marca Gio','Rede',130,214,18,0.66,'ativa'),('Google Ads','ga_pesq','Depilação a laser','SP',86,248,52,0.58,'ativa'),
 ('Google Ads','ga_pesq','Ultraformer','Rede',130,121,61,0.55,'ativa'),('Google Ads','ga_pesq','Avaliação gratuita','SP Capital',41,109,58,0.64,'ativa'),
 ('Google Ads','ga_pesq','Limpeza de pele','Sul',14,96,44,0.60,'ativa'),('Google Ads','ga_pesq','Depilação a laser','GO',7,58,49,0.57,'pausada 17/11'),
 ('Google Ads','ga_pmax','Verão sem pelos','SP e PR',93,176,38,0.50,'ativa'),('Google Ads','ga_pmax','Criolipólise','Rede',130,113,47,0.44,'ativa'),
 ('Meta Ads','meta_form','Verão sem pelos','SP e PR',93,141,27,0.43,'ativa'),('Meta Ads','meta_form','Quiz "Qual tratamento combina com você?"','Rede',130,97,22,0.52,'ativa'),
 ('Meta Ads','meta_form','Remarketing limpeza de pele','Rede',130,80,31,0.47,'ativa · CPL subiu'),('Meta Ads','meta_wa','Criolipólise no WhatsApp','SP',86,112,26,0.56,'ativa'),
 ('Meta Ads','meta_wa','Peeling no WhatsApp','MG e GO',15,78,23,0.53,'ativa')]
CTR={'ga_pesq':0.061,'ga_pmax':0.018,'meta_form':0.014,'meta_wa':0.012}; CVR={'ga_pesq':0.094,'ga_pmax':0.071,'meta_form':0.058,'meta_wa':0.081}
CAMPS=[]
for k,(pl,fo,nm,esc,un,ld,cpl,tx,st) in enumerate(CAMP):
    inv=ld*cpl; cl=round(ld/CVR[fo]); im=round(cl/(CTR[fo]*(1+((k*37)%11-5)/40))); ag=round(ld*tx)
    CAMPS.append(dict(id=k,pl=pl,fo=fo,nome=nm,esc=esc,un=un,imp=im,cli=cl,leads=ld,inv=inv,ag=ag,st=st))
for fo,_,_,ld,_ in FONTES[:4]: assert sum(c['leads'] for c in CAMPS if c['fo']==fo)==ld
# campanhas para clientes (spec 002, mesmos números da tela 62)
CRM=[dict(nome='Verão sem pelos (rede, WhatsApp)',esc='SP e PR',env=31800,cli=6120,leads=152,ag=141,cp=86),dict(nome='Campanhas locais das unidades (17)',esc='17 unidades',env=20600,cli=3750,leads=80,ag=73,cp=45)]
assert sum(c['ag'] for c in CRM)==PF[3][1] and sum(c['cp'] for c in CRM)==PF[4][1]
# ---------- agendamentos, comparecimentos e vendas por fonte ----------
ag_pago={fo:sum(c['ag'] for c in CAMPS if c['fo']==fo) for fo in CTR}
org=[f for f in FONTES if f[0] not in CTR and f[0]!='crm']
tx_org={'seo':0.58,'gbp':0.66,'insta':0.50,'ind':0.74,'dir':0.55}
rest=AG-sum(ag_pago.values())-sum(c['ag'] for c in CRM)
ag_org=dict(zip([f[0] for f in org],dist(rest,[f[3]*tx_org[f[0]] for f in org])))
AGF={**ag_pago,**ag_org,'crm':sum(c['ag'] for c in CRM)}
txc={'ga_pesq':.64,'ga_pmax':.58,'meta_form':.52,'meta_wa':.57,'seo':.63,'gbp':.68,'insta':.58,'ind':.76,'dir':.60}
nc=[f[0] for f in FONTES if f[0]!='crm']; restc=CP-sum(c['cp'] for c in CRM)
CPF=dict(zip(nc,dist(restc,[AGF[k]*txc[k] for k in nc]))); CPF['crm']=sum(c['cp'] for c in CRM)
txv={'ga_pesq':.60,'ga_pmax':.55,'meta_form':.50,'meta_wa':.56,'seo':.58,'gbp':.60,'insta':.54,'crm':.66,'ind':.70,'dir':.55}
VDF=dict(zip([f[0] for f in FONTES],dist(VD,[CPF[f[0]]*txv[f[0]] for f in FONTES])))
# por campanha: comparecimentos e vendas proporcionais dentro da fonte
for fo in CTR:
    cs=[c for c in CAMPS if c['fo']==fo]
    for c,v in zip(cs,dist(CPF[fo],[c['ag'] for c in cs])): c['cp']=v
    for c,v in zip(cs,dist(VDF[fo],[c['cp'] for c in cs])): c['vd']=v
for c in CAMPS: c['rec']=c['vd']*TICKET
INV=sum(c['inv'] for c in CAMPS)
INVF={fo:sum(c['inv'] for c in CAMPS if c['fo']==fo) for fo in CTR}
L_PAGO=sum(f[3] for f in FONTES[:4]); REC=VD*TICKET; REC_PAGO=sum(c['rec'] for c in CAMPS)
GRUPOS=['Mídia paga','Orgânico','Relacionamento','Outros']
# ---------- ponto de conversão, procedimentos ----------
PONTO=[('Formulário da página da unidade',1872),('Quiz',421),('WhatsApp identificado',512),('Telefone rastreado',181)]
PROC=[('Depilação a laser',1104),('Limpeza de pele',512),('Ultraformer',389),('Criolipólise',341),('Peeling',236),('Microagulhamento',168),('Outros',236)]
assert sum(v for _,v in PONTO)==L and sum(v for _,v in PROC)==L
# ---------- atendimento ----------
FAIXAS=[('até 5 min',1094,.71),('5 a 15 min',612,.64),('15 a 60 min',371,.55),('1 a 4 h',238,.41),('4 a 24 h',152,.30),('mais de 24 h',74,.19),('Agendou sozinho, sem contato',445,.45)]
assert sum(f[1] for f in FAIXAS)==L and sum(f[1] for f in FAIXAS[:-1])==CT
AG_FX=dist(AG,[n*t for _,n,t in FAIXAS])
DSEM=['Seg','Ter','Qua','Qui','Sex','Sáb','Dom']; HORAS=['0 a 7h','7 a 10h','10 a 13h','13 a 16h','16 a 19h','19 a 22h','22 a 24h']
pw_d=[1.15,1.12,1.08,1.05,0.98,0.72,0.55]; pw_h=[0.15,0.8,1.25,1.1,1.3,1.4,0.45]
HEAT=dist(L,[d*h*(0.9+0.2*R.random()) for d in pw_d for h in pw_h])
# ---------- unidades ----------
def regiao(u):
    uf=u['nome_uf']; return 'Regional SP' if uf=='SP' else ('Regional Sul' if uf in ('PR','RS','SC') else 'Demais regionais')
LEADS_UF={'SP':1984,'MG':214,'GO':171,'PR':236,'RS':101,'DF':78,'SC':84,'Demais':118}
FIX={'altodalapa':dict(l=41,ag=26,cp=17,t1=9),'curitiba':dict(l=58,ag=38,cp=26,t1=6),'campinas-cambui':dict(l=52,ag=33,cp=23,t1=7),
     'boulevardtatuape':dict(l=55,ag=35,cp=24,t1=8),'porto-alegre-bom-fim':dict(l=33,ag=21,cp=14,t1=9),
     'montes-claros':dict(t1=74),'go-catalao-centro':dict(t1=66),'ipiranga':dict(t1=61)}
UN=[]
for u in UNID:
    g=u['nome_uf'] if u['nome_uf'] in LEADS_UF else 'Demais'
    UN.append(dict(slug=u['url_site'],nome=nome_un(u,40),uf=u['nome_uf'],cid=u['nome_cidade'],reg=regiao(u),g=g,w=R.lognormvariate(0,0.45),ra=0.5+0.16*R.random(),rc=0.55+0.14*R.random(),rv=0.5+0.15*R.random()))
for g,tot in LEADS_UF.items():
    us=[x for x in UN if x['g']==g]; fx=[x for x in us if 'l' in FIX.get(x['slug'],{})]
    for x in fx: x['l']=FIX[x['slug']]['l']
    livres=[x for x in us if x not in fx]
    for x,v in zip(livres,dist(tot-sum(x['l'] for x in fx),[x['w'] for x in livres])): x['l']=v
def _fecha(chave,total,peso):
    fx=[x for x in UN if chave in FIX.get(x['slug'],{})]
    for x in fx: x[chave]=FIX[x['slug']][chave]
    livres=[x for x in UN if x not in fx]
    for x,v in zip(livres,dist(total-sum(x[chave] for x in fx),[peso(x) for x in livres])): x[chave]=v
_fecha('ag',AG,lambda x:x['l']*x['ra']); _fecha('cp',CP,lambda x:x['ag']*x['rc'])
for x,v in zip(UN,dist(VD,[x['cp']*x['rv'] for x in UN])): x['vd']=v
for x,v in zip(UN,dist(CT,[x['l']*(0.8+0.12*R.random()) for x in UN])): x['ct']=min(v,x['l'])
for x,v in zip(UN,dist(INV,[x['l']*(0.75+0.5*R.random()) for x in UN])): x['inv']=v
for x,v in zip(UN,dist(L_PAGO,[x['l']*(0.45+0.2*R.random()) for x in UN])): x['lp']=v
for x in UN:
    x['t1']=FIX.get(x['slug'],{}).get('t1') or max(3,round(R.lognormvariate(2.35,0.45)))
    x['nota']={'altodalapa':4.8,'curitiba':4.8,'campinas-cambui':4.9}.get(x['slug'],round(4.3+R.random()*0.6,1))
    x['l_ant']=max(1,round(x['l']/(0.95+0.4*R.random())))
    x['tx_ag']=x['ag']/x['l'] if x['l'] else 0
# comparecimento (definição única da spec 005): compareceram ÷ agendamentos já realizados (compareceram + faltas + cancelamentos); futuros ficam fora
for x,v in zip(UN,dist(FUTUROS,[x['ag'] for x in UN])): x['fut']=v
for x in UN:
    if x['fut']>x['ag']-x['cp']: x['fut']=x['ag']-x['cp']
_dif=FUTUROS-sum(x['fut'] for x in UN)
for x in sorted(UN,key=lambda x:-(x['ag']-x['cp']-x['fut'])):
    if not _dif: break
    x['fut']+=1; _dif-=1
assert sum(x['fut'] for x in UN)==FUTUROS
for x in UN: x['real']=x['ag']-x['fut']; x['tx_cp']=x['cp']/x['real'] if x['real'] else 0
assert sum(x['real'] for x in UN)==CP+REALIZ_FALTA
RK={'curitiba':96,'campinas-cambui':93,'boulevardtatuape':91,'altodalapa':90,'porto-alegre-bom-fim':88}
for x in UN: x['raw']=0.62*x['tx_ag']+0.38*x['tx_cp']+(0.04 if x['t1']<=10 else -0.05 if x['t1']>30 else 0)
_rs=[x['raw'] for x in UN if x['slug'] not in RK]; _lo,_hi=min(_rs),max(_rs)
for x in UN: x['idx']=RK.get(x['slug']) or round(34+(x['raw']-_lo)/(_hi-_lo)*52)
ORD=sorted(UN,key=lambda x:-x['idx'])
for k,x in enumerate(ORD): x['pos']=k+1; x['q']=1+k*4//len(ORD)
AL=next(x for x in UN if x['slug']=='altodalapa')
def mediana(v): v=sorted(v); n=len(v); return v[n//2] if n%2 else (v[n//2-1]+v[n//2])/2
REGS=['Regional SP','Regional Sul','Demais regionais']
def soma(us,k): return sum(x[k] for x in us)
UF_AG={}
for x in UN: UF_AG.setdefault(x['uf'],[]).append(x)
# ---------- mensal (sazonalidade, ano anterior, previsão) ----------
MESES=['dez/25','jan/26','fev/26','mar/26','abr/26','mai/26','jun/26','jul/26','ago/26','set/26','out/26','nov/26']
MES_L=[2710,3420,3150,3580,3390,3840,4120,4260,3980,3720,3760,None]
MES_AA=[2380,2950,2710,3020,2890,3260,3540,3610,3420,3190,3240,3290]   # mesmo mês do ano anterior (dez/24 a nov/25)
PREV=4264; PREV_LO=4080; PREV_HI=4430
METAS=[('Leads',L,4000,PREV,'Salus · meta comercial de novembro'),('Agendamentos',AG,2600,round(AG/21*30),'Salus'),('Comparecimentos',CP,1650,round(CP/21*30),'Salus'),('Investimento em mídia',INV,95000,round(INV/21*30),'Salus · orçamento aprovado')]
# ---------- área do cliente (spec 002) e quiz (003) ----------
CLI=dict(base=CLI_REDE,novos=CLI_NOVOS,ativos_30d=11840,cons=CONS_PCT,vitrine_exib=38400,vitrine_cli=4210,ag_online=486,remarc=131,cancel=74,
         pac_ativos=9620,sess_mes=7410,pac_acabando=812,venda_online=94,venda_online_val=94*1360,nps=71,nps_resp=1236,google_conv=1236,google_cliq=402,avisos_conf=MURAL_CONF)
QZ=dict(ini=QZ_INI,fim=QZ_FIM,conta=QZ_CONTA,leads=421,dem=QZ_DEM)
# ---------- Google: GBP Performance e Search Console (integração; ilustrativo) ----------
GBP=dict(imp_busca_mob=612400,imp_maps_mob=401300,imp_busca_desk=198200,imp_maps_desk=72600,lig=5140,rotas=8930,site=7460,msg=2310,vinculados=104)
GSC=dict(cliques=41200,imp=1904000,pos=9.4,ctr=2.16)
GSC_CONS=[('gio depilação a laser perto de mim',3120,6.1),('gio estética [cidade]',2870,1.8),('depilação a laser preço',1940,11.2),('ultraformer [cidade]',1210,8.7),('limpeza de pele [bairro]',990,7.4),('criolipólise preço',760,13.9)]
# ---------- avaliações (spec 004): lidas do próprio gerador da tela 84 para os números baterem ----------
try:
    _src=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'s11.py'),encoding='utf-8').read()
    _src=_src.split('# fila da unidade')[0]; _ns={}; exec(_src,_ns)
    AV=dict(tot=_ns['TOT'],media=_ns['MEDIA'],tx=_ns['TX_RESP'],medh=_ns['MED_H'],pend=len(_ns['PEND']),esc=len(_ns['ESC']),esc_pend=len(_ns['ESC_PEND']),ok=True)
except Exception as e:
    AV=dict(tot=1180,media=4.6,tx=78,medh=6.5,pend=260,esc=140,esc_pend=24,ok=False)

# ---------- por unidade (relatório da unidade, tela 97) ----------
import unicodedata as _ud, random as _rnd
_R2=_rnd.Random(97)
def _sem_acento(t): return ''.join(c for c in _ud.normalize('NFD',t) if _ud.category(c)!='Mn').lower()
_RVU={}
if AV.get('ok'):
    for _u,_rs in _ns['UNID_R'].items(): _RVU[_sem_acento(_u)]=(_u,_rs)
    _RV=_ns['RV']
    AV['r48']=round(sum(1 for r in _RV if r['resp'] and r['h'] is not None and r['h']<=48)/len(_RV)*100)
    _low=[r for r in _RV if r['e']<=2]; AV['n_baixas']=len(_low)
    AV['r24_baixas']=round(sum(1 for r in _low if r['resp'] and r['h'] is not None and r['h']<=24)/len(_low)*100) if _low else 0
else:
    AV.update(r48=77,n_baixas=87,r24_baixas=75)
_BASEQ={1:4.62,2:4.47,3:4.36,4:4.2}
for x in UN:
    k=_sem_acento(x['nome'])
    if k in _RVU:
        x['nome']=_RVU[k][0]; rs=_RVU[k][1]
        x['nav']=len(rs); x['pend']=sum(1 for r in rs if not r['resp']); x['nota']=round(sum(r['e'] for r in rs)/len(rs),1) if rs else None
    else:
        x['nav']=0; x['pend']=0; x['nota']=None
    x['nota_g']={'altodalapa':4.8,'curitiba':4.8,'campinas-cambui':4.9}.get(x['slug'],round(_BASEQ[x['q']]+_R2.uniform(-.15,.15),1))  # nota acumulada no Google
    if x['nota'] is None: x['nota']=x['nota_g']
_vistos={}
for x in UN:
    if x['slug'] in _vistos: _vistos[x['slug']]+=1; x['slug']=f"{x['slug']}-{_vistos[x['slug']]}"
    else: _vistos[x['slug']]=1
assert len({x['slug'] for x in UN})==len(UN)
def nota_media(us):
    n=sum(x['nav'] for x in us)
    return sum(x['nota']*x['nav'] for x in us)/n if n else sum(x['nota'] for x in us)/len(us)
# campanhas que alcançam a unidade (rateio que fecha com a mídia atribuída da unidade)
def _cobre(c,x):
    e=c['esc']
    return e=='Rede' or (e=='SP' and x['uf']=='SP') or (e=='SP Capital' and x['uf']=='SP' and x['cid']=='São Paulo') or (e=='Sul' and x['uf'] in ('PR','RS','SC')) \
        or (e=='GO' and x['uf']=='GO') or (e=='SP e PR' and x['uf'] in ('SP','PR')) or (e=='MG e GO' and x['uf'] in ('MG','GO'))
EVD_UN=next(e[2] for e in EV if e[0]=='unidade_visualizada')
for x,v in zip(UN,dist(EVD_UN,[x['l']*(0.8+0.4*_R2.random()) for x in UN])): x['vis']=v
for x,v in zip(UN,dist(GBP['lig'],[x['l']*(0.8+0.4*_R2.random()) for x in UN])): x['lig']=v
for x,v in zip(UN,dist(GBP['rotas'],[x['l']*(0.8+0.4*_R2.random()) for x in UN])): x['rotas']=v
_mods=['A']*46+['B']*52+['C']*32; _R2.shuffle(_mods)
for x,m in zip(UN,_mods): x['mod']=m
for x in UN:
    cs=[c for c in CAMPS if _cobre(c,x)]
    lds=dist(x['lp'],[c['leads']/c['un'] for c in cs]) if cs else []
    cus=dist(x['inv'],[l*c['inv']/c['leads'] for c,l in zip(cs,lds)]) if cs and sum(lds) else dist(x['inv'],[1]*len(cs)) if cs else []
    x['camps']=sorted([(c['pl'],c['nome'],c['esc'],l,v) for c,l,v in zip(cs,lds,cus) if l or v],key=lambda t:-t[3])
    assert sum(t[4] for t in x['camps'])==x['inv'] or not cs
    x['fon']=dist(x['l'],[f[3]*(0.7+0.6*_R2.random()) for f in FONTES])
    f=[0.71,0.80,0.76,0.88,0.90]; x['hist']=[max(1,round(x['l']*v*(0.9+0.2*_R2.random()))) for v in f]+[x['l']]

