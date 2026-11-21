from base import *
# ---------- AVALIAÇÕES DO GOOGLE (spec 004), rev. 2 com a crítica de design ----------
# Dados 100% fictícios: nomes abreviados inventados e textos escritos para a demonstração.
A=DEMO['altodalapa']
TEMAS=['Atendimento','Resultado','Agendamento','Preço','Procedimento','Estrutura']
LEITURA='hoje às 15:40'
def fixn(n): return n.replace('Sao Paulo','São Paulo').replace('Sao ','São ')
def regiao(u):
    uf=u['nome_uf']
    return 'Regional SP' if uf=='SP' else ('Regional Sul' if uf in ('PR','RS','SC') else 'Demais regionais')
def gera(seed):
    rnd=random.Random(seed); out=[]
    for u in UNID:
        agil=rnd.choice([0.55,0.75,0.9,0.97])
        for _ in range(rnd.randint(3,15)):
            e=rnd.choices([1,2,3,4,5],[3,3,6,18,70])[0]
            t=rnd.choices(TEMAS,[34,22,16,10,12,6] if e>=4 else [22,14,24,22,12,6])[0]
            resp=rnd.random()<agil
            h=round(rnd.uniform(1,10)/agil*(1 if e>=3 else 0.7),1) if resp else None
            saude=e<=3 and rnd.random()<0.08
            out.append(dict(u=fixn(nome_un(u,60)),reg=regiao(u),e=e,t=t,resp=resp,h=h,saude=saude))
    return out
RV=gera(80); PREV=gera(79)
# GiO Alto da Lapa: as 7 avaliações desenhadas (4 sem resposta, 3 respondidas)
REVS=[
 dict(id='r2',n='Lu M.',e=1,q='há 9 h',t='Procedimento',s='negativo',saude=True,esc='Rede avisada · menciona saúde',st='sem resposta',
      txt='Fiquei com a pele vermelha e ardendo por dois dias depois da sessão. Ninguém me avisou que podia acontecer.',
      sug='Lu, obrigada por nos escrever e por contar como se sentiu. Queremos ouvir você com calma e cuidar disso com atenção. Por favor, chame a gente no WhatsApp da unidade ou ligue para (11) 90000-0000 e peça para falar com a responsável técnica. Equipe GiO Alto da Lapa',
      curta='Lu, obrigada por nos escrever. Queremos ouvir você com calma: chame a gente no WhatsApp da unidade ou ligue para (11) 90000-0000 e peça a responsável técnica. Equipe GiO Alto da Lapa',
      calorosa='Lu, obrigada de verdade por dividir isso com a gente. Sua tranquilidade é o que mais importa para nós, e queremos conversar com calma. Chame a gente no WhatsApp da unidade ou ligue para (11) 90000-0000 e peça para falar com a responsável técnica. Um abraço, Equipe GiO Alto da Lapa',
      porque='Agradece e demonstra cuidado sem citar a sessão, o procedimento nem a reação (regra bloqueante da US3). Leva a conversa para um canal privado com a responsável técnica e não discute o caso em público.',
      linha=[('09:02','Avaliação lida do Google'),('09:02','IA classificou: procedimento, negativo, menciona saúde'),('09:03','Rede avisada (menção a saúde)')]),
 dict(id='r1',n='Paula R.',e=2,q='há 3 h',t='Agendamento',s='negativo',saude=False,esc='Rede avisada · nota baixa',st='unidade respondendo',
      txt='Marquei pelo site e quando cheguei disseram que o horário não estava na agenda. Esperei 40 minutos. A recepcionista foi educada, mas faltou organização.',
      sug='Paula, obrigada por contar como foi. Sentimos muito pela espera de 40 minutos e pelo desencontro no horário: não é a experiência que queremos oferecer. Já revisamos com a equipe como os agendamentos do site chegam à nossa agenda. Se puder, fale com a gente pelo WhatsApp da unidade para combinarmos um novo horário do jeito que for melhor para você. Equipe GiO Alto da Lapa',
      curta='Paula, obrigada pelo retorno e desculpe pela espera de 40 minutos. Já revisamos com a equipe como os horários do site chegam à agenda. Fale com a gente pelo WhatsApp da unidade para combinarmos um novo horário. Equipe GiO Alto da Lapa',
      calorosa='Paula, muito obrigada por contar com tanto cuidado o que aconteceu, inclusive o elogio à recepção. Sentimos muito pela espera e pelo desencontro no horário. Já ajustamos com a equipe como os agendamentos do site chegam à agenda e vamos adorar receber você de novo: chame a gente pelo WhatsApp da unidade. Equipe GiO Alto da Lapa',
      porque='Cita a espera e o horário que a pessoa mencionou, pede desculpas sem discutir, diz o que mudou e convida para um canal privado. Não usa dados da agenda nem confirma atendimento.',
      linha=[('12:40','Avaliação lida do Google'),('12:40','IA classificou: agendamento, negativo'),('12:41','Rede avisada (nota baixa)'),('13:12','Ingrid N. (rede) está acompanhando')]),
 dict(id='r4',n='Rodrigo T.',e=3,q='há 2 dias',t='Preço',s='neutro',saude=False,esc='',st='sem resposta',
      txt='Gostei do lugar, mas achei o valor do pacote acima do que eu esperava.',
      sug='Rodrigo, obrigada pela sinceridade e por ter gostado do espaço. Temos condições diferentes conforme o plano escolhido, e a avaliação é gratuita. Se quiser, nossa equipe monta uma simulação sem compromisso pelo WhatsApp da unidade. Equipe GiO Alto da Lapa',
      curta='Rodrigo, obrigada pelo retorno! As condições variam conforme o plano escolhido. Fale com a gente pelo WhatsApp da unidade para uma simulação sem compromisso. Equipe GiO Alto da Lapa',
      calorosa='Rodrigo, que bom que você gostou do nosso espaço, e obrigada pela sinceridade sobre o valor. As condições mudam conforme o plano escolhido, e queremos achar a melhor para você. Chame a gente no WhatsApp da unidade para uma simulação sem compromisso. Equipe GiO Alto da Lapa',
      porque='Agradece o elogio ao espaço, explica que as condições variam sem citar valores nem prometer desconto e convida para uma simulação no canal privado.',
      linha=[('19/11 10:20','Avaliação lida do Google'),('19/11 10:20','IA classificou: preço, neutro')]),
 dict(id='r3',n='Fernanda S.',e=5,q='há 1 dia',t='Atendimento',s='positivo',saude=False,esc='',st='sem resposta',
      txt='Equipe muito atenciosa, explicaram cada etapa e a sala é super limpa. Recomendo!',
      sug='Fernanda, que alegria ler isso! Ficamos felizes que a explicação de cada etapa e o cuidado com a sala fizeram diferença. Obrigada pela recomendação, vamos passar o seu recado para a equipe. Até a próxima! Equipe GiO Alto da Lapa',
      curta='Fernanda, obrigada pela recomendação! Vamos passar o seu recado para a equipe. Equipe GiO Alto da Lapa',
      calorosa='Fernanda, que alegria! Ler que a explicação de cada etapa e a sala limpa fizeram diferença deixou a equipe toda feliz. Obrigada pela recomendação e pelo carinho. Equipe GiO Alto da Lapa',
      porque='Agradece citando o que a pessoa elogiou (explicação de cada etapa e limpeza), sem confirmar atendimento nem citar procedimento.',
      linha=[('20/11 16:05','Avaliação lida do Google'),('20/11 16:05','IA classificou: atendimento, positivo')]),
 dict(id='r5',n='Cris L.',e=5,q='há 4 dias',t='Atendimento',s='positivo',saude=False,esc='',st='respondida',txt='Equipe explica tudo antes e a recepção é muito simpática.',
      pub='Cris, obrigada pelo carinho com a nossa recepção e por notar o cuidado em explicar tudo. Vamos passar o recado para a equipe! Equipe GiO Alto da Lapa',quando='17/11 às 11:20 por Renata F. (respondida em 2 h)',linha=[('17/11 09:15','Avaliação lida do Google'),('17/11 11:20','Resposta publicada por Renata F.')]),
 dict(id='r6',n='Joana M.',e=4,q='há 5 dias',t='Resultado',s='positivo',saude=False,esc='',st='respondida',txt='Gostei bastante, só demorou um pouco para começar.',
      pub='Joana, obrigada pelo retorno! Que bom que gostou, e anotamos o ponto sobre o começo: queremos que tudo flua desde a chegada. Equipe GiO Alto da Lapa',quando='16/11 às 15:02 por Renata F. (respondida em 5 h)',linha=[('16/11 10:00','Avaliação lida do Google'),('16/11 15:02','Resposta publicada por Renata F.')]),
 dict(id='r7',n='Bia F.',e=5,q='há 6 dias',t='Sem texto',s='positivo',saude=False,esc='',st='respondida',txt='',
      pub='Bia, obrigada pelas cinco estrelas! Equipe GiO Alto da Lapa',quando='15/11 às 10:40 por Renata F. (respondida em 1 h)',linha=[('15/11 09:38','Avaliação lida do Google (só nota, sem texto)'),('15/11 10:40','Resposta publicada por Renata F.')]),
]
RV_BY={r['id']:r for r in REVS}
AL=[r for r in RV if r['u']=='GiO Alto da Lapa']
for k,x in enumerate(AL):
    if k<len(REVS):
        rv=REVS[k]; x.update(e=rv['e'],t=(rv['t'] if rv['t'] in TEMAS else 'Atendimento'),resp=rv['st']=='respondida',saude=rv['saude'],id=rv['id'],n=rv['n'])
        x['h']={'r5':2.0,'r6':5.0,'r7':1.0}.get(rv['id']) if x['resp'] else None
    else: x.update(resp=True,h=x['h'] or 3.5)
NOMES=['Ana C.','Bruna L.','Carla M.','Débora S.','Elaine R.','Fabiana T.','Gabi N.','Helena P.','Isabela F.','Joyce A.','Karina D.','Larissa V.','Mônica B.','Natália G.','Olívia H.','Patrícia K.','Raquel Q.','Sabrina E.','Tânia J.','Vanessa O.']
rr=random.Random(84)
for k,r in enumerate(RV):
    r.setdefault('id',f'a{k}')
    r.setdefault('n',rr.choice(NOMES))
    r['esp']=rr.choice([2,4,6,9,14,20,27,33,41,52,63,71]) if not r['resp'] else None
ESP_AL={'r1':3,'r2':9,'r4':50,'r3':26}
for r in AL:
    if r['id'] in ESP_AL: r['esp']=ESP_AL[r['id']]
def esc_motivo(r): return 'menciona saúde' if r['saude'] else ('nota baixa' if r['e']<=2 else '')
for k,r in enumerate(RV):
    r['esc']=bool(r['e']<=2 or r['saude'])
    if r['esc'] and not r['resp']:
        r['sit']='unidade respondendo' if (r['id']=='r1' or (r['id']!='r2' and k%3==0)) else 'sem resposta'
    elif r['esc']: r['sit']='respondida pela rede' if k%7==0 else 'respondida pela unidade'
    elif not r['resp']: r['sit']='sem resposta'
    else: r['sit']='respondida'
TOT=len(RV); MEDIA=sum(r['e'] for r in RV)/TOT
RESP=[r for r in RV if r['resp']]; PEND=[r for r in RV if not r['resp']]
hs=sorted(r['h'] for r in RESP); MED_H=hs[len(hs)//2]
ESC=[r for r in RV if r['esc']]; ESC_PEND=[r for r in ESC if not r['resp']]
ESC_SEM=[r for r in ESC_PEND if r['sit']=='sem resposta']
EM48=round(sum(1 for r in RV if r['resp'] and r['h']<=48)/TOT*100)
BAIXAS=[r for r in RV if r['e']<=2]; B24=round(sum(1 for r in BAIXAS if r['resp'] and r['h']<=24)/len(BAIXAS)*100)
P_TOT=len(PREV); P_MED=sum(r['e'] for r in PREV)/P_TOT; P_48=round(sum(1 for r in PREV if r['resp'])/P_TOT*100)
P_PEND=sum(1 for r in PREV if not r['resp']); P_ESC=sum(1 for r in PREV if r['e']<=2 or r['saude'])
P_B=[r for r in PREV if r['e']<=2]; P_B24=round(sum(1 for r in P_B if r['resp'] and r['h']<=24)/len(P_B)*100)
SAUDE3=sum(1 for r in ESC if r['e']>=3)
def br(x,d=1): return f'{x:.{d}f}'.replace('.',',')
def delta(a,b,suf=' p.p.',d=0,bom_maior=True):
    v=round(a-b,d) if d else round(a-b); ok=(v>=0)==bom_maior
    s=('+' if v>0 else ('−' if v<0 else '±'))+(br(abs(v),d) if d else str(abs(v)))
    return f'<span class="{"up" if ok else "down"}">{s}{suf}</span> vs out'
def estrelas(n):
    return '<span class="num estr" role="img" aria-label="'+str(n)+' de 5 estrelas">'+'★'*n+'☆'*(5-n)+'</span>'
def pill_sent(s): return {'positivo':'<span class="pill v">positivo</span>','neutro':'<span class="pill z">neutro</span>','negativo':'<span class="pill r">negativo</span>'}[s]
SIT_COR={'sem resposta':'r','unidade respondendo':'a','respondida pela unidade':'v','respondida pela rede':'v','respondida':'v','rede acompanhando':'b'}
def pill_sit(s): return f'<span class="pill {SIT_COR[s]}">{s}</span>'
UNID_R={}
for r in RV: UNID_R.setdefault(r['u'],[]).append(r)
TXT_NEG={'Agendamento':'Cheguei no horário e tive que esperar bastante para ser atendida.','Preço':'O valor final ficou diferente do que me passaram pelo WhatsApp.','Atendimento':'Fui atendida com pressa e não tiraram minhas dúvidas.','Resultado':'Esperava mais depois de várias sessões.','Procedimento':'Senti bastante desconforto e não me explicaram o que era normal.','Estrutura':'A sala estava fria e a recepção bem cheia.'}
TXT_POS={'Agendamento':'Consegui horário rápido e no dia certo.','Preço':'Condições justas e tudo bem explicado.','Atendimento':'Equipe atenciosa do começo ao fim.','Resultado':'Estou gostando bastante do resultado.','Procedimento':'Explicaram cada etapa com calma.','Estrutura':'Lugar limpo e confortável.'}
def texto(r):
    if r['id'] in RV_BY: return RV_BY[r['id']]['txt']
    if r['saude']: return 'Fiquei com irritação depois e gostaria de uma orientação.'
    return TXT_NEG[r['t']] if r['e']<=3 else TXT_POS[r['t']]
def compacto(r): return [r['id'],r['u'],r['reg'],r['e'],r['t'],r['n'],texto(r),r['sit'],esc_motivo(r),r['esp'] if r['esp'] is not None else -1,r['h'] if r['h'] is not None else -1]
SEL=[]
for u,rs in UNID_R.items():
    SEL+=[r for r in rs if (not r['resp']) or r['esc']]+[r for r in rs if r['resp'] and not r['esc']][:3]
DADOS=json.dumps([compacto(r) for r in SEL],ensure_ascii=False,separators=(',',':'))
SUG_REDE={x['id']:x['sug'] for x in REVS if 'sug' in x}
def lk_un(u): return L('aval-un')+'?u='+u.replace(' ','+')
TX_RESP=round(len(RESP)/TOT*100)
# fila da unidade: a partir daqui, HTML (rel_dados.py lê só a parte de dados acima deste marcador)
JS_UTIL=r'''<script>
function qp(k){var m=new RegExp('[?&]'+k+'=([^&#]*)').exec(location.search);return m?decodeURIComponent(m[1].replace(/\+/g,' ')):''}
function toast(t){var d=document.getElementById('toast');if(!d){d=document.createElement('div');d.id='toast';d.className='toast';d.setAttribute('role','status');document.body.appendChild(d)}d.textContent=t;d.classList.add('on');clearTimeout(window._tt);window._tt=setTimeout(function(){d.classList.remove('on')},2600)}
function estr(n){return '<span class="num estr" role="img" aria-label="'+n+' de 5 estrelas">'+'★★★★★'.slice(0,n)+'☆☆☆☆☆'.slice(0,5-n)+'</span>'}
function esc(s){return String(s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
function hm(){var h=new Date();return String(h.getHours()).padStart(2,'0')+':'+String(h.getMinutes()).padStart(2,'0')}
function lerAgora(b){b.disabled=true;var t=b.innerHTML;b.textContent='Lendo o Google…';setTimeout(function(){b.disabled=false;b.innerHTML=t;var l=document.getElementById('leitura');if(l)l.textContent='agora, às '+hm();toast('Leitura concluída: nenhuma avaliação nova')},900)}
</script>'''
# validador ao vivo (FR-404): mesma lista no compositor da unidade e no workspace da rede
JS_VALID=r'''<script>
window.PROIB=[[/\b(laser|depila\w*|sess(ão|ões|ao|oes)|procedimento|tratamento|peeling|criolip\w*|microagulh\w*)\b/i,'cita procedimento ou sessão'],[/\b(vermelh\w*|ard(e|ência|endo)|alergi\w*|irrita\w*|rea(ção|ções|cao)|queimad\w*|mancha\w*|inflama\w*)\b/i,'cita dado de saúde'],[/\b(paciente|nossa cliente|quando você esteve|sua sessão|seu pacote|seu prontuário)\b/i,'confirma que a pessoa é cliente'],[/\b(desconto|grátis|garantimos|resultado garantido)\b/i,'promete desconto ou resultado']];
function valida(txt){for(var i=0;i<PROIB.length;i++){if(PROIB[i][0].test(txt))return 'Esta frase '+PROIB[i][1]+'. Tire isso antes de publicar. Assuntos de saúde vão para o WhatsApp ou o telefone da unidade.'}return ''}
</script>'''
JS_COMP=r'''<script>
(function(){
window.addEventListener('hashchange',function(){location.reload()});
var R=window.REVS||{},id=(location.hash||'').replace('#','')||qp('r')||window.PADRAO;var r=R[id]||R[window.PADRAO];
var est=qp('estado'),perfil=qp('perfil');
function $(s){return document.getElementById(s)}
function set(k,v){var e=$(k);if(e)e.innerHTML=v}
if(!r)return;
set('rv-nome',esc(r.n));set('rv-av',esc(r.n.split(' ').map(function(x){return x[0]}).join('').slice(0,2)));set('rv-estr',estr(r.e));set('rv-quando',esc(r.q));
set('rv-txt',r.txt?esc(r.txt):'<span class="meta">Só nota, sem texto. A sugestão agradece de forma breve.</span>');
set('rv-pills','<span class="pill b">Tema: '+esc(r.t)+'</span>'+({positivo:'<span class="pill v">positivo</span>',neutro:'<span class="pill z">neutro</span>',negativo:'<span class="pill r">negativo</span>'}[r.s]||'')+(r.esc?'<span class="pill r">⚑ '+esc(r.esc)+'</span>':''));
set('rv-porque',esc(r.porque||'Resposta já publicada pela unidade.'));
set('rv-linha',(r.linha||[]).map(function(l){return '<div class="it"><span class="meta num">'+esc(l[0])+'</span><span>'+esc(l[1])+'</span></div>'}).join(''));
var mig=$('rv-mig');if(mig)mig.textContent=r.n;
var tema=$('rv-tema');if(tema){tema.value=r.t;}
var t=$('resp-txt'),n=$('resp-n'),aj=$('resp-aj'),pub=$('resp-pub'),dr=$('resp-rasc'),tit=$('resp-tit'),box=$('resp-box'),ok=$('resp-ok'),pubd=$('resp-pubd'),dlg=$('resp-conf');
function limite(){var c=t.innerText.trim().length;n.textContent=c.toLocaleString('pt-BR');var msg=valida(t.innerText),bad=!!msg;
 if(!bad&&c>4096){msg='O Google aceita no máximo 4.096 caracteres.';bad=true}
 if(!bad&&c===0){msg='Escreva a resposta ou peça uma sugestão.';bad=true}
 var aviso=!bad&&c>=3900;
 aj.className='ajuda'+(bad?' erro':'')+(aviso?' alerta':'');
 aj.textContent=bad?('⚠ '+msg):((aviso?'Perto do limite do Google. ':'')+'Validador: sem dado de saúde, sem confirmar atendimento.');
 if(pub){pub.disabled=bad;pub.classList.toggle('off',bad)}}
function poe(txt,aviso){t.innerText=txt;limite();if(aviso)toast('Sugestão atualizada. Revise antes de publicar.')}
function trava(s){document.querySelectorAll('[data-atalho]').forEach(function(b){b.disabled=s})}
function gerando(cb){box.classList.add('gerando');t.setAttribute('contenteditable','false');t.innerHTML='<span class="meta">A IA está sugerindo uma resposta no tom da Gio…</span>';if(pub){pub.disabled=true;pub.classList.add('off')}trava(true);
 setTimeout(function(){box.classList.remove('gerando');t.setAttribute('contenteditable','true');trava(false);cb()},900)}
if(!t)return;
t.addEventListener('input',limite);
document.querySelectorAll('[data-atalho]').forEach(function(b){b.addEventListener('click',function(){var a=b.getAttribute('data-atalho');
 if(a==='curta')gerando(function(){poe(r.curta,1)});
 else if(a==='calorosa')gerando(function(){poe(r.calorosa,1)});
 else if(a==='convidar')gerando(function(){poe(r.sug.indexOf('WhatsApp')>=0?r.sug:r.sug.replace(/ Equipe/,' Se quiser, chame a gente no WhatsApp da unidade. Equipe'),1)});
 else if(a==='outra')gerando(function(){poe(r.calorosa===t.innerText?r.sug:r.calorosa,1)});
 else if(a==='zero'){t.innerText='';tit.textContent='Sua resposta';limite();t.focus()}})});
if(dr)dr.addEventListener('click',function(){set('resp-rascok','Rascunho salvo às '+hm()+'.');toast('Rascunho salvo')});
function publicar(){pub.disabled=true;pub.textContent='Publicando…';setTimeout(function(){box.style.display='none';ok.style.display='flex';set('resp-okh','Publicada às '+hm()+'. Aparece no Google em alguns minutos. Registrada na auditoria da rede.');set('resp-pubtxt',esc(t.innerText))},700)}
if(pub)pub.addEventListener('click',function(e){e.preventDefault();e.stopPropagation();if(pub.disabled)return;if(r.esc||r.saude){dlg.style.display='flex';$('conf-sim').focus()}else publicar()});
if(dlg){$('conf-sim').addEventListener('click',function(){dlg.style.display='none';publicar()});$('conf-nao').addEventListener('click',function(){dlg.style.display='none';pub.focus()})}
if(r.st==='respondida'||est==='publicada'){box.style.display='none';pubd.style.display='block';set('resp-pubq','Publicada '+esc(r.quando||('hoje às '+hm())));set('resp-pubtxt2',esc(r.pub||r.sug||''));tit.textContent='Resposta publicada'}
else if(est==='gerando'){gerando(function(){poe(r.sug)})}
else if(est==='falha'){t.innerText='';tit.textContent='Sua resposta';set('resp-falha','<div class="aviso r" style="margin-bottom:10px"><div>⚠</div><div style="font-size:13px"><b>Não foi possível sugerir uma resposta.</b><div class="meta">Você pode escrever a sua ou tentar de novo.</div><button type="button" class="btn s" id="resp-tenta" style="margin-top:8px">Tentar de novo</button></div></div>');$('resp-tenta').addEventListener('click',function(){set('resp-falha','');tit.textContent='Resposta sugerida';gerando(function(){poe(r.sug)})});limite();t.focus()}
else if(est==='assumida'){t.innerText=r.sug;t.setAttribute('contenteditable','false');tit.textContent='Resposta da rede';set('resp-assum','<div class="aviso b" style="margin-bottom:10px"><div>ⓘ</div><div style="font-size:13px"><b>A rede assumiu esta resposta.</b><div class="meta">Você está vendo o texto antes de ele sair.</div></div></div>');document.querySelectorAll('[data-atalho],#resp-pub,#resp-rasc').forEach(function(b){b.style.display='none'});limite()}
else if(est==='validador'){poe(r.sug.replace(/ Equipe/,' Esperamos você na sua próxima sessão. Equipe'))}
else if(est==='limite'){poe((r.sug+' ').repeat(Math.ceil(4150/(r.sug.length+1))).slice(0,4150))}
else {poe(r.sug)}
if(perfil==='recepcao'&&pub){pub.style.display='none';dr.classList.add('p');set('resp-rec','Quem publica é a gerência da unidade. Você pode editar e salvar o rascunho.')}
})();
</script>'''
JS_FILA=r'''<script>
(function(){var f=qp('f')||'sem',tema=qp('tema'),est=qp('estado');
document.querySelectorAll('[data-chip]').forEach(function(c){var on=(c.getAttribute('data-chip')===f&&!tema);c.classList.toggle('on',on);if(on)c.setAttribute('aria-current','true')});
document.querySelectorAll('[data-tema-lk]').forEach(function(c){var on=c.getAttribute('data-tema-lk')===tema;c.classList.toggle('on',on);if(on)c.setAttribute('aria-current','true')});
var vis=0;document.querySelectorAll('.fila-it,[data-f="resp"]').forEach(function(e){var fs=e.getAttribute('data-f'),ok;
 if(tema)ok=e.getAttribute('data-tema')===tema;else if(f==='todas')ok=true;else if(f==='resp')ok=fs==='resp';else if(f==='baixa')ok=fs.indexOf('baixa')>=0;else if(f==='rede')ok=fs.indexOf('rede')>=0;else ok=fs!=='resp';
 if(fs==='resp'&&!tema&&f==='sem')ok=true;
 e.style.display=ok?'':'none';if(ok&&fs!=='resp')vis++});
document.querySelectorAll('[data-lista="resp"]').forEach(function(c){var any=[].some.call(c.querySelectorAll('[data-f="resp"]'),function(x){return x.style.display!=='none'});c.style.display=any?'':'none'});
var rt=document.getElementById('rot-filtro');if(rt)rt.textContent=tema?('Tema: '+tema):({sem:'Sem resposta, mais urgentes primeiro',baixa:'Notas 1 e 2',rede:'Avisadas à rede',resp:'Respondidas',todas:'Todas'}[f]||'');
if(est){document.querySelectorAll('[data-estado="'+est+'"]').forEach(function(e){e.hidden=false});if(est==='vazia'||est==='desvinculado'){document.querySelectorAll('.fila-it').forEach(function(e){e.style.display='none'})}}
else if(vis===0&&f!=='resp'&&f!=='todas'&&!tema){document.querySelectorAll('[data-estado="vazia"]').forEach(function(e){e.hidden=false})}
})();</script>'''
CSV_JS=r'''<script>
function exportaCSV(){var D=window.DADOS||[];var l=['avaliacao;unidade;regiao;nota;tema;situacao;motivo;espera_h;resposta_h'];D.forEach(function(r){l.push([r[0],r[1],r[2],r[3],r[4],r[7],r[8],r[9]<0?'':r[9],r[10]<0?'':r[10]].join(';'))});
var b=new Blob(['\ufeff'+l.join('\n')],{type:'text/csv'});var a=document.createElement('a');a.href=URL.createObjectURL(b);a.download='avaliacoes-rede-01-21nov2026.csv';document.body.appendChild(a);a.click();a.remove();toast('CSV gerado com '+(l.length-1)+' linhas. A exportação fica na auditoria da rede.')}
function lembrar(b){b.disabled=true;b.textContent='Lembrete enviado';toast('Lembrete enviado às unidades com pendências (e-mail e sino). Registrado na auditoria.')}
(function(){var p=qp('p');document.querySelectorAll('[data-per]').forEach(function(c){c.classList.toggle('on',c.getAttribute('data-per')===(p||'nov'))})})();
</script>'''
REVS_JS='<script>window.REVS='+json.dumps({x['id']:{k:x.get(k) for k in ('id','n','e','q','t','s','saude','esc','st','txt','sug','curta','calorosa','porque','linha','pub','quando')} for x in REVS},ensure_ascii=False)+';</script>'
DADOS_JS='<script>window.DADOS='+DADOS+';</script>'
regras='<div class="aviso l"><div>'+i('shield',16)+'</div><div style="font-size:13px"><b>Cuidados da resposta</b><div class="meta" style="margin-top:2px">Não confirme que a pessoa é cliente, não cite procedimento, data de sessão nem dado de saúde. Assuntos de saúde vão para um canal privado. A IA sugere, quem publica é a unidade.</div></div></div>'
R0=REVS[0]
def compositor(mob=False):
    """Compositor (81 e 83). O conteúdo troca pelo hash (#r1 a #r7) ou ?r=; estados por ?estado=."""
    volta=L('m-aval' if mob else 'f-aval')
    atalhos=''.join(f'<button type="button" class="chip" data-atalho="{k}">{t}</button>' for k,t in [('curta','Mais curta'),('calorosa','Mais calorosa'),('convidar','Convidar para conversar'),('outra','Gerar outra')])
    return f'''<div class="card" id="resp-card"><div class="hd" style="flex-wrap:wrap;row-gap:6px"><h3>{i('sparkle',15)} <span id="resp-tit">Resposta sugerida</span></h3><span class="pill z" style="margin-left:auto;white-space:normal">tom da Gio · cita o que a pessoa disse</span></div>
 <div id="resp-assum"></div><div id="resp-falha"></div>
 <div id="resp-box">
  <div class="campo"><label id="resp-lbl" for="resp-txt"><span class="lt">Texto da resposta</span><span class="pill e" style="padding:2px 8px">{i('edit',11)}<span class="tx"> Editável</span></span></label>
   <div class="in" id="resp-txt" contenteditable="true" role="textbox" aria-multiline="true" aria-labelledby="resp-lbl" aria-describedby="resp-aj" style="min-height:{180 if mob else 150}px;align-items:flex-start;line-height:1.55;white-space:pre-wrap;display:block">{R0['sug']}</div>
   <div class="info"><div class="ajuda" id="resp-aj">Validador: sem dado de saúde, sem confirmar atendimento.</div><div class="meta" style="white-space:nowrap"><span class="num" id="resp-n">{len(R0['sug'])}</span> de 4.096</div></div></div>
  <div class="atalhos">{atalhos}<button type="button" class="btn ghost s" data-atalho="zero">Escrever do zero</button></div>
  <div class="acoes-resp"><button type="button" class="btn p" id="resp-pub">{i("send",14)} Publicar no Google</button><button type="button" class="btn" id="resp-rasc">Salvar rascunho</button></div>
  <div class="meta" id="resp-rascok" role="status"></div><div class="meta" id="resp-rec"></div>
 </div>
 <div class="aviso v" id="resp-ok" style="display:none" role="status"><div>{i('check',16)}</div><div style="font-size:13px"><b>Resposta enviada ao Google</b><div class="meta" id="resp-okh"></div><p style="margin-top:6px" id="resp-pubtxt"></p><a class="lk" href="{volta}" style="display:inline-block;margin-top:6px">Voltar para a fila</a></div></div>
 <div id="resp-pubd" style="display:none"><div class="aviso v"><div>{i('check',16)}</div><div style="font-size:13px"><b>Resposta publicada</b><div class="meta" id="resp-pubq"></div><p style="margin-top:6px" id="resp-pubtxt2"></p><a class="lk" href="{volta}" style="display:inline-block;margin-top:6px">Voltar para a fila</a></div></div></div>
</div>
<div class="modal" id="resp-conf" role="dialog" aria-modal="true" aria-labelledby="conf-t" style="display:none"><div class="card modal-c"><h3 id="conf-t">Publicar mesmo?</h3><p class="muted" style="margin:8px 0 14px">Esta avaliação foi avisada à rede. A resposta vai aparecer no Google em alguns minutos e não pode confirmar que a pessoa é cliente nem discutir o caso em público.</p><div class="acoes-resp"><button type="button" class="btn p" id="conf-sim">Publicar no Google</button><button type="button" class="btn" id="conf-nao">Voltar e revisar</button></div></div></div>'''
def avaliacao_card():
    return f'''<div class="card"><div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><span class="av-s" id="rv-av">LM</span><div><b id="rv-nome">{R0['n']}</b><div class="meta">Google · <span id="rv-quando">{R0['q']}</span> · {A['nome']}</div></div><span style="margin-left:auto" id="rv-estr">{estrelas(R0['e'])}</span></div>
 <p style="margin-top:10px" id="rv-txt">{R0['txt']}</p>
 <div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap" id="rv-pills"><span class="pill b">Tema: {R0['t']}</span>{pill_sent(R0['s'])}<span class="pill r">{i('flag',11)} {R0['esc']}</span></div>
 <div class="tema-fix"><label for="rv-tema" class="meta">Tema errado? Corrija:</label><select id="rv-tema" class="in" onchange="toast('Tema corrigido. Isso ajuda a IA a acertar nas próximas.')">{''.join(f'<option>{t}</option>' for t in TEMAS+['Sem texto','Outro'])}</select></div></div>'''
# ---------- 80 FILA (franqueado, computador) ----------
ORD=[RV_BY[k] for k in ('r2','r1','r4','r3')]  # mais urgente primeiro: saúde, notas 1 e 2, depois por data
AL_TOT=len(AL); AL_MED=sum(r['e'] for r in AL)/AL_TOT
al_h=sorted(r['h'] for r in AL if r['resp']); AL_MEDH=al_h[len(al_h)//2]
def fila_card(r,link):
    cor='var(--vermelho)' if r['e']<=2 else ('var(--ambar)' if r['e']==3 else 'var(--verde)')
    filt=' '.join(x for x in ['sem','baixa' if r['e']<=2 else '','rede' if r['esc'] else ''] if x)
    return f'''<a class="card fila-it" href="{link}#{r['id']}" data-f="{filt}" data-tema="{r['t']}" style="display:block;border-left:4px solid {cor};padding:14px 16px">
 <div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><b>{r['n']}</b>{estrelas(r['e'])}<span class="meta">{r['q']}</span><span style="margin-left:auto;display:flex;gap:6px;flex-wrap:wrap"><span class="pill b">{r['t']}</span>{pill_sent(r['s'])}</span></div>
 <p class="muted" style="margin-top:6px">{r['txt']}</p>
 <div style="display:flex;gap:8px;align-items:center;margin-top:8px;flex-wrap:wrap">{f'<span class="pill r">{i("flag",11)} {r["esc"]}</span>' if r['esc'] else ''}<span class="meta">{i('sparkle',12)} Sugestão de resposta pronta</span><span class="lk" style="margin-left:auto">Revisar e responder {i('chev',12)}</span></div></a>'''
def resp_linha(r,link):
    q=r['quando'].split('(')[1].rstrip(')')
    return f'<a class="it" href="{link}#{r["id"]}" data-f="resp" data-tema="{r["t"]}" style="flex-wrap:wrap;row-gap:4px"><b style="min-width:96px">{r["n"]}</b>{estrelas(r["e"])}<span class="pill b">{r["t"]}</span><span class="meta" style="margin-left:auto;white-space:nowrap">{q}</span></a>'
TEMA_AL=[(t,sum(1 for r in REVS if r['t']==t)) for t in TEMAS+['Sem texto']]
TEMA_AL=sorted([x for x in TEMA_AL if x[1]],key=lambda z:-z[1])
mx_al=max(n for _,n in TEMA_AL)
def estados_fila():
    return f'''<div class="estado" data-estado="vazia" hidden><div class="card vazio">{i('check',22)}<h3>Tudo respondido neste recorte</h3><p class="muted">O tempo mediano desta unidade está em {br(AL_MEDH)} h. Avaliações novas aparecem aqui em até 4 horas.</p><a class="btn" href="?f=todas">Ver todas</a></div></div>
<div class="estado" data-estado="desvinculado" hidden><div class="aviso a" style="margin-bottom:12px"><div>{i('alert',16)}</div><div><b>Perfil do Google não vinculado</b><div class="meta">A leitura parou em 18/11 às 09:40. Para voltar, quem é dono do perfil no Google adiciona a conta da rede como gerente.</div></div></div></div>
<div class="estado" data-estado="falha" hidden><div class="aviso r" style="margin-bottom:12px"><div>{i('alert',16)}</div><div><b>Não conseguimos ler o Google agora</b><div class="meta">Última leitura bem sucedida {LEITURA}. Tentamos de novo a cada 30 minutos; a fila pode estar desatualizada.</div><button type="button" class="btn s" onclick="lerAgora(this)" style="margin-top:6px">Tentar agora</button></div></div></div>'''
def chips():
    it=[('sem','Sem resposta','4'),('baixa','Nota baixa','2'),('rede','Avisadas à rede','2'),('resp','Respondidas','3'),('todas','Todas','7')]
    return '<nav class="chips" aria-label="Filtros da fila">'+''.join(f'<a class="chip" data-chip="{k}" href="?f={k}">{t} <b>{n}</b></a>' for k,t,n in it)+'</nav>'
def temas_lk():
    return '<div style="display:flex;flex-direction:column;gap:8px">'+''.join(f'<a class="tema-lk" data-tema-lk="{t}" href="?tema={t.replace(" ","+")}"><div style="display:flex;font-size:13px"><span>{t}</span><span class="meta num" style="margin-left:auto">{n}</span></div><span class="barra" style="display:block;width:auto"><i style="width:{round(n/mx_al*100)}%"></i></span></a>' for t,n in TEMA_AL)+'</div>'
cont=cabec('Avaliações do Google',f'{A["nome"]} · avaliações lidas do seu perfil no Google a cada 4 horas. Responda por aqui: a resposta é publicada no Google.',f'<span class="meta">{i("refresh",13)} Última leitura <span id="leitura">{LEITURA}</span></span><button type="button" class="btn s" onclick="lerAgora(this)">Ler agora</button>')+f'''
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">
 {kpi('star','Nota no Google',A['nota'],f'{A["aval"]} avaliações no total (ilustrativo)')}
 {kpi('inbox','Sem resposta','4','2 com nota baixa, 1 menciona saúde')}
 {kpi('clock','Tempo de resposta',f'{br(AL_MEDH)} h','mediana em novembro · meta 48 h')}
 {kpi('trend','Avaliações em novembro',str(AL_TOT),f'média {br(AL_MED)} no período')}
</div>
{estados_fila()}
<div class="g" style="grid-template-columns:minmax(0,1fr) 320px;align-items:start">
 <div>
  {chips()}
  <div class="meta" style="margin:0 0 10px">Ordem: <b id="rot-filtro">Sem resposta, mais urgentes primeiro</b></div>
  <div style="display:flex;flex-direction:column;gap:10px">{''.join(fila_card(r,L('f-aval-det')) for r in ORD)}</div>
  <div class="card" style="margin-top:14px" data-lista="resp"><div class="hd"><h3>Respondidas recentemente</h3></div><div class="lista-i">'''+''.join(resp_linha(RV_BY[k],L('f-aval-det')) for k in ('r5','r6','r7'))+f'''</div></div>
 </div>
 <div style="display:flex;flex-direction:column;gap:12px">
  <div class="card"><div class="hd"><h3>{i('sparkle',15)} O que mais aparece</h3></div>{temas_lk()}
   <p class="meta" style="margin-top:10px">Temas das 7 avaliações de novembro mostradas aqui, classificados por IA. Toque em um tema para filtrar.</p></div>
  <div class="card"><div class="hd"><h3>{i('flag',15)} Quando a rede entra</h3></div>
   <p class="muted" style="font-size:13px">Avaliações com 1 ou 2 estrelas, ou que falem de problema de saúde, também aparecem para a rede. A rede pode acompanhar ou assumir a resposta.</p></div>
  {regras}
 </div>
</div>{JS_UTIL}{JS_FILA}'''
salvar(ARQ['f-aval'],pagina('Avaliações do Google',app('franq','f-aval',cont,placeholder='Buscar avaliação, lead ou artigo')))
# ---------- 81 RESPONDER (franqueado, computador) ----------
cont=f'''<div class="migalha"><a href="{L('f-aval')}">Avaliações</a> {i('chev',12)} <b style="color:var(--tinta)" id="rv-mig">{R0['n']}</b></div>'''+cabec('Responder avaliação','Revise a sugestão, ajuste o que quiser e publique. A resposta aparece no Google em alguns minutos.')+f'''
<div class="g" style="grid-template-columns:minmax(0,1fr) 340px;align-items:start">
 <div style="display:flex;flex-direction:column;gap:14px">{avaliacao_card()}{compositor()}</div>
 <div style="display:flex;flex-direction:column;gap:12px">
  <div class="card"><div class="hd"><h3>{i('flag',15)} Linha do tempo</h3></div><div class="lista-i" id="rv-linha"></div>
   <p class="meta" style="margin-top:8px">Notas 1 e 2 e menções a saúde também chegam à rede, que pode acompanhar ou assumir. Se a rede assumir, você vê o texto antes de sair.</p></div>
  {regras}
  <div class="card"><div class="hd"><h3>Por que esta sugestão</h3></div><p class="muted" style="font-size:13px" id="rv-porque">{R0['porque']}</p></div>
 </div>
</div>{JS_UTIL}{JS_VALID}{REVS_JS}<script>window.PADRAO='r2';</script>{JS_COMP}'''
salvar(ARQ['f-aval-det'],pagina('Responder avaliação',app('franq','f-aval',cont,placeholder='Buscar avaliação, lead ou artigo')))
# ---------- 82 e 83 CELULAR ----------
def sbar(): return '<div style="height:44px;display:flex;align-items:center;padding:0 22px;font:600 15px Inter;color:var(--tinta)"><span>9:41</span><span style="flex:1;display:flex;justify-content:center">'+selo()+'</span><span style="width:18px;height:10px;border:1.5px solid var(--tinta);border-radius:3px"></span></div>'
def tabbar_f(on):
    it=[('home','Início','f-inicio'),('inbox','Leads','m-leads'),('cal','Agenda',None),('star','Avaliações','m-aval'),('more','Mais','f-notif')]
    return '<nav class="tabbar">'+''.join(f'<a class="{"on" if k==on else ""}" href="{L(lk) if lk else "#docbiz"}"{" aria-current=page" if k==on else ""}>{i(ic,22)}<span>{t}{"" if lk else " ↗"}</span></a>' for k,(ic,t,lk) in enumerate(it))+'</nav>'
corpo=f'''<div class="mob longo" style="background:#fbf7f9">{sbar()}<div class="rolagem com-tab" style="padding:0 16px">
 <div style="margin:4px 0 6px"><div class="meta">{A['nome']}</div><h1 style="font-size:24px;font-weight:600">Avaliações</h1></div>
 <div class="meta" style="display:flex;gap:8px;align-items:center;margin-bottom:10px;flex-wrap:wrap">{i('refresh',12)} Última leitura <span id="leitura">{LEITURA}</span><button type="button" class="btn ghost s" onclick="lerAgora(this)" style="margin-left:auto">Ler agora</button></div>
 <div class="g" style="grid-template-columns:1fr 1fr;gap:8px;margin-bottom:12px"><div class="card" style="padding:12px"><div class="meta">Nota no Google</div><b class="pop num" style="font-size:22px">{A['nota']}</b><div class="meta">{br(AL_MEDH)} h para responder</div></div><div class="card" style="padding:12px"><div class="meta">Sem resposta</div><b class="pop num" style="font-size:22px">4</b><div class="meta">2 com nota baixa</div></div></div>
 {estados_fila()}
 {chips()}
 <div class="meta" style="margin:0 0 8px">Ordem: <b id="rot-filtro">Sem resposta, mais urgentes primeiro</b></div>
 <nav class="chips rolavel" aria-label="Temas">{''.join(f'<a class="chip" data-tema-lk="{t}" href="?tema={t.replace(" ","+")}">{t} <b>{n}</b></a>' for t,n in TEMA_AL)}</nav>
 <div style="display:flex;flex-direction:column;gap:10px">{''.join(fila_card(r,L('m-aval-det')) for r in ORD)}</div>
 <div class="card" style="margin-top:12px;padding:14px" data-lista="resp"><b>Respondidas recentemente</b><div class="lista-i">'''+''.join(resp_linha(RV_BY[k],L('m-aval-det')) for k in ('r5','r6','r7'))+f'''</div></div>
</div>{tabbar_f(3)}</div>{JS_UTIL}{JS_FILA}'''
salvar(ARQ['m-aval'],pagina('Avaliações no celular',corpo,390))
corpo=f'''<div class="mob longo" style="background:#fbf7f9">{sbar()}<div class="rolagem com-tab" style="padding:0 16px">
 <a href="{L('m-aval')}" class="lk" style="display:inline-flex;align-items:center;gap:4px;min-height:40px">{i('chev',14)} Avaliações</a>
 <div style="display:flex;flex-direction:column;gap:10px">{avaliacao_card()}{compositor(True)}</div>
 <details open class="card" style="padding:14px;margin-top:10px"><summary><b>Linha do tempo e rede</b></summary><div class="lista-i" id="rv-linha" style="margin-top:8px"></div></details>
 <details open class="card" style="padding:14px;margin-top:10px"><summary><b>Por que esta sugestão</b></summary><p class="muted" style="font-size:13px;margin-top:8px" id="rv-porque">{R0['porque']}</p></details>
 <div style="margin-top:10px">{regras}</div>
</div>{tabbar_f(3)}</div>{JS_UTIL}{JS_VALID}{REVS_JS}<script>window.PADRAO='r2';</script>{JS_COMP}'''
salvar(ARQ['m-aval-det'],pagina('Responder avaliação no celular',corpo,390))
# ---------- 84 INSIGHTS DA REDE (acionável) ----------
POR_REG={}
for r in RV: POR_REG.setdefault(r['reg'],[]).append(r)
def med_h(rs):
    h=sorted(x['h'] for x in rs if x['resp']); return h[len(h)//2] if h else None
UNS=[(u,len(rs),sum(x['e'] for x in rs)/len(rs),sum(1 for x in rs if not x['resp']),med_h(rs),max([x['esp'] for x in rs if not x['resp']] or [0])) for u,rs in UNID_R.items()]
RAPIDAS=sorted([x for x in UNS if x[4] is not None and x[1]>=5],key=lambda z:(z[4],-z[1]))[:5]
ACUM=sorted(UNS,key=lambda z:(-z[3],-z[5]))[:6]
TEMA_N=sorted(((t,sum(1 for r in RV if r['t']==t),sum(1 for r in RV if r['t']==t and r['e']<=2)) for t in TEMAS),key=lambda z:-z[1])
mx_t=TEMA_N[0][1]
regs=['Regional SP','Regional Sul','Demais regionais']
def grav(r): return (0 if r['saude'] else 1, r['e'], -(r['esp'] or 0))
ESC_ORD=sorted(ESC_SEM,key=grav)+sorted([r for r in ESC_PEND if r['sit']!='sem resposta'],key=grav)
def lin_esc(r):
    acao='Assumir' if r['sit']=='sem resposta' else ('Acompanhar' if r['sit']=='unidade respondendo' else 'Ver')
    espera=f"espera há {r['esp']} h" if r['esp'] is not None else f"respondida em {br(r['h'])} h"
    return f'''<div class="linha" data-saude="{1 if r['saude'] else 0}" data-sit="{r['sit']}" data-tema="{r['t']}" data-reg="{r['reg']}" data-u="{r['u']}" data-e="{r['e']}">
 <div class="c-u"><a class="lk-forte trunc" href="{lk_un(r['u'])}" title="{r['u']}">{r['u']}</a><div class="meta">{r['n']} · {espera}</div></div>
 <div class="c-n">{estrelas(r['e'])}</div><div class="c-t"><span class="rot">Tema</span> {r['t']}</div><div class="c-m"><span class="rot">Motivo</span> {esc_motivo(r)}</div>
 <div class="c-s">{pill_sit(r['sit'])}</div><div class="c-a"><a class="btn s{" p" if acao=="Assumir" else ""}" href="{L('aval-ws')}#{r['id']}">{acao}</a></div></div>'''
CAB='<div class="linha cab"><div class="c-u">Unidade</div><div class="c-n">Nota</div><div class="c-t">Tema</div><div class="c-m">Motivo</div><div class="c-s">Situação</div><div class="c-a"></div></div>'
per='<span class="sw" role="group" aria-label="Período"><a data-per="7d" href="?p=7d">7 dias</a><a data-per="30d" href="?p=30d">30 dias</a><a data-per="nov" href="?p=nov" class="on">01 a 21 nov</a></span>'
def kpi_a(href,ic,rot,val,det,cls=''):
    return f'<a class="card kpi kpi-a {cls}" href="{href}"><div class="l">{i(ic,15)} {rot}</div><div class="v num">{val}</div><div class="d">{det}</div></a>'
cont=cabec('Avaliações da rede',f'Avaliações do Google das {len(UNID_R)} unidades, lidas a cada 4 horas. Última leitura <span id="leitura">{LEITURA}</span>. Temas e sentimento classificados por IA.',per+f'<button type="button" class="btn s" onclick="lerAgora(this)">{i("refresh",13)} Ler agora</button><button type="button" class="btn s" onclick="exportaCSV()">{i("down",13)} Exportar CSV</button>')+f'''
<div class="g kpis5" style="grid-template-columns:repeat(5,1fr);margin-bottom:16px">
 {kpi_a(L('aval-esc')+'?f=pend','flag','Escaladas sem resposta',str(len(ESC_PEND)),f'{len(ESC_SEM)} sem rascunho · {len(ESC_PEND)-len(ESC_SEM)} com a unidade respondendo · de {len(ESC)} no período','alerta')}
 {kpi_a('#pendentes','inbox','Sem resposta',fmt(len(PEND)),f'em {sum(1 for x in UNS if x[3])} unidades · {delta(len(PEND),P_PEND,"",0,False)}','alerta')}
 {kpi_a(L('aval-esc')+'?f=todas','check','Respondidas em 48 h',f'{EM48}%',f'meta 90% · {delta(EM48,P_48)}')}
 {kpi_a(L('aval-esc')+'?f=baixas','clock','Notas 1 e 2 em 24 h',f'{B24}%',f'meta 95% · {delta(B24,P_B24)}')}
 {kpi_a('#temas','star','Nota média',br(MEDIA),f'{fmt(TOT)} avaliações · mediana {br(MED_H)} h · {delta(MEDIA,P_MED,"",1)}')}
</div>
<div class="g" style="grid-template-columns:minmax(0,1.7fr) minmax(0,1fr);margin-bottom:16px;align-items:start">
 <div class="card"><div class="hd" style="flex-wrap:wrap"><h3>{i('flag',15)} Escaladas que pedem ação</h3><div style="margin-left:auto;display:flex;gap:6px;flex-wrap:wrap"><a class="chip" href="{L('aval-esc')}?f=saude">Só saúde</a><a class="btn s" href="{L('aval-esc')}">Ver todas as {len(ESC)}</a></div></div>
  <p class="meta" style="margin:-6px 0 8px">As {len(ESC_PEND)} sem resposta: primeiro as {len(ESC_SEM)} sem rascunho (saúde e nota 1 na frente), depois as que a unidade está respondendo.</p>
  <div class="linhas">{CAB}{''.join(lin_esc(r) for r in ESC_ORD[:6])}</div>
  <p class="meta" style="margin-top:10px">Mostrando 6 de {len(ESC_PEND)} pendentes. Escaladas são as notas 1 e 2 ({len(ESC)-SAUDE3}) mais as notas 3 com menção a saúde ({SAUDE3}).</p></div>
 <div class="card" id="pendentes"><div class="hd" style="flex-wrap:wrap"><h3>{i('alert',15)} Acumulam pendentes</h3><button type="button" class="btn s p" style="margin-left:auto" onclick="lembrar(this)">{i('send',12)} Lembrar unidades</button></div>
  <div class="lista-i">'''+''.join(f'<a class="it" href="{lk_un(u)}"><div style="flex:1;min-width:0"><b class="trunc" style="display:block" title="{u}">{u}</b><div class="meta">mais antiga espera há {esp} h · nota {br(m)}</div></div><span class="pill r num">{p} sem resposta</span></a>' for u,n,m,p,h,esp in ACUM)+f'''</div></div>
</div>
<div class="g" style="grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);margin-bottom:16px;align-items:start">
 <div class="card" id="temas"><div class="hd"><h3>{i('sparkle',15)} Temas recorrentes</h3><span class="sub" style="margin-left:auto">volume e notas 1 e 2</span></div>
  <div style="display:flex;flex-direction:column;gap:10px">'''+''.join(f'<a class="tema-lk" href="{L("aval-esc")}?f=todas&tema={t}"><div style="display:flex;font-size:13px;gap:8px;flex-wrap:wrap"><b>{t}</b><span class="meta" style="margin-left:auto"><span class="num">{n}</span> avaliações · <span class="num" style="color:var(--vermelho)">{b}</span> com nota 1 ou 2</span></div><span class="barra" style="display:block;width:auto;margin-top:4px"><i style="width:{round(n/mx_t*100)}%"></i></span></a>' for t,n,b in TEMA_N)+f'''</div>
  <p class="meta" style="margin-top:10px">Agendamento e preço concentram as notas baixas: <a class="lk" href="{L('aval-esc')}?f=todas&tema=Agendamento">ver agendamento</a> · <a class="lk" href="{L('aval-esc')}?f=todas&tema=Preço">ver preço</a>.</p></div>
 <div class="card"><div class="hd"><h3>{i('pin',15)} Por região</h3><span class="sub" style="margin-left:auto">toque para ver as escaladas</span></div>
  <div class="linhas reg"><div class="linha cab"><div>Região</div><div>Nota</div><div>Respondidas</div><div>Mediana</div><div>Sem resposta</div></div>'''+''.join(f'<a class="linha" href="{L("aval-esc")}?f=todas&reg={g.replace(" ","+")}"><div><b>{g}</b></div><div class="num"><span class="rot">Nota</span> {br(sum(x["e"] for x in POR_REG[g])/len(POR_REG[g]))}</div><div class="num"><span class="rot">Respondidas</span> {round(sum(1 for x in POR_REG[g] if x["resp"])/len(POR_REG[g])*100)}%</div><div class="num"><span class="rot">Mediana</span> {br(med_h(POR_REG[g]))} h</div><div class="num"><span class="rot">Sem resposta</span> {sum(1 for x in POR_REG[g] if not x["resp"])}</div></a>' for g in regs)+f'''</div></div>
</div>
<div class="card" id="rapidas"><div class="hd"><h3>{i('zap',15)} Respondem mais rápido</h3><span class="sub" style="margin-left:auto">mediana, 5 avaliações ou mais</span></div>
 <div class="lista-i">'''+''.join(f'<a class="it" href="{lk_un(u)}"><span class="num meta" style="width:22px">{k+1}º</span><b style="flex:1;min-width:0" class="trunc" title="{u}">{u}</b><span class="pill v num">{br(h)} h</span></a>' for k,(u,n,m,p,h,esp) in enumerate(RAPIDAS))+f'''</div>
 <p class="meta" style="margin-top:8px">{i('log',12)} Respostas publicadas, edições, assunções pela rede e exportações ficam na auditoria da rede.</p></div>
{JS_UTIL}{DADOS_JS}{CSV_JS}'''
salvar(ARQ['aval-rede'],pagina('Avaliações da rede',app('admin','aval-rede',cont)))
# ---------- 85 LISTA COMPLETA DE ESCALADAS ----------
JS85=r'''<script>(function(){var f=qp('f')||'todas',tema=qp('tema'),reg=qp('reg'),u=qp('u');
document.querySelectorAll('[data-chip]').forEach(function(c){var on=c.getAttribute('data-chip')===f;c.classList.toggle('on',on);if(on)c.setAttribute('aria-current','true')});
var n=0;document.querySelectorAll('.linha[data-sit]').forEach(function(e){var s=e.getAttribute('data-sit'),ok=true;
 if(f==='pend')ok=s==='sem resposta'||s==='unidade respondendo';else if(f==='sem')ok=s==='sem resposta';else if(f==='resp')ok=s==='unidade respondendo';else if(f==='saude')ok=e.getAttribute('data-saude')==='1';else if(f==='baixas')ok=+e.getAttribute('data-e')<=2;
 if(tema)ok=ok&&e.getAttribute('data-tema')===tema;if(reg)ok=ok&&e.getAttribute('data-reg')===reg;if(u)ok=ok&&e.getAttribute('data-u')===u;e.style.display=ok?'':'none';if(ok)n++});
document.getElementById('n-vis').textContent=n;document.getElementById('vazio85').hidden=n>0;
var x=[];if(tema)x.push('tema '+tema);if(reg)x.push(reg);if(u)x.push(u);x.push({pend:'sem resposta',sem:'sem rascunho',resp:'unidade respondendo',saude:'menciona saúde',baixas:'notas 1 e 2',todas:'todas as situações'}[f]);
document.getElementById('rot-filtro').textContent=x.join(' · ');
if(tema||reg||u){var l=document.getElementById('limpa');l.hidden=false}
document.querySelectorAll('[data-chip]').forEach(function(c){var h=c.getAttribute('href');if(tema)h+='&tema='+encodeURIComponent(tema);if(reg)h+='&reg='+encodeURIComponent(reg);c.setAttribute('href',h)})})();</script>'''
cont=f'''<div class="migalha"><a href="{L('aval-rede')}">Avaliações da rede</a> {i('chev',12)} <b style="color:var(--tinta)">Escaladas</b></div>'''+cabec('Escaladas para a rede',f'Notas 1 e 2 e menções a saúde de 01 a 21 nov 2026: {len(ESC)} no período, {len(ESC_PEND)} sem resposta ({len(ESC_SEM)} sem rascunho).',f'<button type="button" class="btn s" onclick="exportaCSV()">{i("down",13)} Exportar CSV</button>')+'''
<nav class="chips" aria-label="Filtros">'''+''.join(f'<a class="chip" data-chip="{k}" href="?f={k}">{t}</a>' for k,t in [('pend','Sem resposta'),('sem','Sem rascunho'),('resp','Unidade respondendo'),('saude','Menciona saúde'),('baixas','Notas 1 e 2'),('todas','Todas')])+f'''</nav>
<div class="meta" style="margin:0 0 10px">Recorte: <b id="rot-filtro">todas as situações</b> · <span id="n-vis" class="num">{len(ESC)}</span> avaliações <a class="lk" id="limpa" href="?f=todas" hidden>limpar recorte</a></div>
<div class="card"><div class="linhas">{CAB}'''+''.join(lin_esc(r) for r in ESC_ORD+sorted([r for r in ESC if r['resp']],key=grav))+f'''</div>
<div class="estado" id="vazio85" hidden><div class="vazio">{i('check',22)}<h3>Nada neste recorte</h3><p class="muted">Nenhuma escalada com esses filtros no período.</p><a class="btn" href="?f=todas">Ver todas</a></div></div></div>
{JS_UTIL}{DADOS_JS}{CSV_JS}{JS85}'''
salvar(ARQ['aval-esc'],pagina('Escaladas para a rede',app('admin','aval-rede',cont)))
# ---------- 86 WORKSPACE DA REDE ----------
JS86=r'''<script>(function(){var D=window.DADOS,id=(location.hash||'').replace('#','')||qp('r')||'r2',r=null,k;
for(k=0;k<D.length;k++)if(D[k][0]===id){r=D[k];break}if(!r){id='r2';for(k=0;k<D.length;k++)if(D[k][0]==='r2'){r=D[k];break}}
function $(s){return document.getElementById(s)}
var nome=r[5],un=r[1],fila='@UN@?u='+encodeURIComponent(un).replace(/%20/g,'+');
$('ws-mig').textContent=nome;$('ws-nome').textContent=nome;$('ws-av').textContent=nome.split(' ').map(function(x){return x[0]}).join('').slice(0,2);
$('ws-un').textContent=un;$('ws-un').href=fila;$('ws-fila').href=fila;$('ws-reg').textContent=r[2];$('ws-estr').innerHTML=estr(r[3]);
$('ws-txt').innerHTML=r[6]?esc(r[6]):'<span class="meta">Só nota, sem texto.</span>';
$('ws-pills').innerHTML='<span class="pill b">Tema: '+esc(r[4])+'</span>'+(r[8]?'<span class="pill r">⚑ '+esc(r[8])+'</span>':'')+(r[9]>=0?'<span class="pill a">espera há '+r[9]+' h</span>':'');
var sitEl=$('ws-sit');function poeSit(s,c){sitEl.innerHTML='<span class="pill '+c+'">'+esc(s)+'</span>'}
var cl={'sem resposta':'r','unidade respondendo':'a','respondida pela unidade':'v','respondida pela rede':'v','respondida':'v'},sit=r[7];poeSit(sit,cl[sit]||'z');
var sug=window.SUG[id]||('Obrigada por nos contar. Queremos entender melhor e cuidar disso com atenção. Por favor, chame a gente no WhatsApp ou no telefone da unidade. Equipe '+un);
var t=$('ws-txtr'),lin=window.LIN[id]||[['hoje','Avaliação lida do Google'],['hoje','IA classificou: '+r[4].toLowerCase()+(r[3]<=2?', negativo':'')],['hoje','Rede avisada ('+(r[8]||'nota baixa')+')']];
$('ws-linha').innerHTML=lin.map(function(l){return '<div class="it"><span class="meta num">'+esc(l[0])+'</span><span>'+esc(l[1])+'</span></div>'}).join('');
if(sit==='unidade respondendo'){t.textContent=sug;$('ws-autor').textContent=id==='r1'?'rascunho de Renata F., 13:20':'rascunho da unidade'}
else if(sit.indexOf('respondida')===0){t.textContent=sug;$('ws-tit').textContent='Resposta publicada';$('ws-autor').textContent=sit;$('ws-acoes').style.display='none';$('ws-aj').textContent='Publicada no Google.'}
else{t.innerHTML='<span class="meta">A unidade ainda não escreveu. Se a rede assumir, começa pela sugestão da IA.</span>'}
var outras=D.filter(function(x){return x[1]===un&&x[0]!==id&&(x[7]==='sem resposta'||x[7]==='unidade respondendo')}).slice(0,4);
$('ws-outras').innerHTML=outras.length?outras.map(function(x){return '<a class="it" href="#'+x[0]+'"><b>'+esc(x[5])+'</b>'+estr(x[3])+'<span class="meta" style="margin-left:auto">'+esc(x[4])+'</span></a>'}).join(''):'<div class="meta">Nenhuma outra pendente.</div>';
window.addEventListener('hashchange',function(){location.reload()});
function val(){var m=valida(t.innerText);$('ws-aj').className='ajuda'+(m?' erro':'');$('ws-aj').textContent=m?('⚠ '+m):'Validador: sem dado de saúde, sem confirmar atendimento. A unidade vê o texto antes de sair.';$('ws-pub').disabled=!!m;$('ws-pub').classList.toggle('off',!!m)}
$('ws-acomp').addEventListener('click',function(){poeSit('rede acompanhando','b');this.disabled=true;this.textContent='Você está acompanhando';toast('Você vai ver o rascunho da unidade antes de sair.')});
$('ws-assumir').addEventListener('click',function(){poeSit('rede assumiu','b');$('ws-acoes').style.display='none';$('ws-pubrow').style.display='flex';t.classList.remove('lock');t.setAttribute('contenteditable','true');t.textContent=sug;$('ws-tit').textContent='Resposta da rede';$('ws-autor').textContent='Ingrid N. · rede';t.addEventListener('input',val);val();t.focus();toast('Você assumiu. A unidade foi avisada.')});
$('ws-devolver').addEventListener('click',function(){poeSit('devolvida à unidade','a');toast('Devolvida à unidade, com aviso no sino.')});
$('ws-cancel').addEventListener('click',function(){location.reload()});
$('ws-pub').addEventListener('click',function(){if(this.disabled)return;$('ws-conf').style.display='flex';$('wc-sim').focus()});
$('wc-nao').addEventListener('click',function(){$('ws-conf').style.display='none'});
$('wc-sim').addEventListener('click',function(){$('ws-conf').style.display='none';$('ws-pubrow').style.display='none';$('ws-ok').style.display='flex';t.setAttribute('contenteditable','false');poeSit('respondida pela rede','v')});
})();</script>'''.replace('@UN@',L('aval-un'))
cont=f'''<div class="migalha"><a href="{L('aval-rede')}">Avaliações da rede</a> {i('chev',12)} <a href="{L('aval-esc')}">Escaladas</a> {i('chev',12)} <b style="color:var(--tinta)" id="ws-mig">Lu M.</b></div>'''+cabec('Escalada para a rede','A rede acompanha ou assume a resposta. A unidade vê o texto antes de sair.','<span id="ws-sit"></span>')+f'''
<div class="g" style="grid-template-columns:minmax(0,1fr) 340px;align-items:start">
 <div style="display:flex;flex-direction:column;gap:14px">
  <div class="card"><div style="display:flex;gap:10px;align-items:center;flex-wrap:wrap"><span class="av-s" id="ws-av">LM</span><div><b id="ws-nome">Lu M.</b><div class="meta">Google · <a class="lk" id="ws-un" href="{lk_un('GiO Alto da Lapa')}">GiO Alto da Lapa</a> · <span id="ws-reg">Regional SP</span></div></div><span style="margin-left:auto" id="ws-estr">{estrelas(1)}</span></div>
   <p style="margin-top:10px" id="ws-txt">{RV_BY['r2']['txt']}</p><div style="display:flex;gap:6px;margin-top:10px;flex-wrap:wrap" id="ws-pills"></div></div>
  <div class="card"><div class="hd" style="flex-wrap:wrap"><h3>{i('edit',15)} <span id="ws-tit">Rascunho da unidade</span></h3><span class="pill z" style="margin-left:auto" id="ws-autor">ainda sem rascunho</span></div>
   <div class="campo"><label id="ws-lbl"><span class="lt">Texto</span></label><div class="in lock" id="ws-txtr" role="textbox" aria-multiline="true" aria-labelledby="ws-lbl" aria-describedby="ws-aj" style="min-height:130px;line-height:1.55;white-space:pre-wrap;display:block"></div>
    <div class="info"><div class="ajuda" id="ws-aj">Somente leitura enquanto a rede acompanha.</div></div></div>
   <div class="acoes-resp" id="ws-acoes"><button type="button" class="btn" id="ws-acomp">Acompanhar</button><button type="button" class="btn p" id="ws-assumir">Assumir a resposta</button><button type="button" class="btn ghost" id="ws-devolver">Devolver à unidade</button></div>
   <div class="acoes-resp" id="ws-pubrow" style="display:none"><button type="button" class="btn p" id="ws-pub">{i('send',14)} Publicar como rede</button><button type="button" class="btn" id="ws-cancel">Cancelar</button></div>
   <div class="aviso v" id="ws-ok" style="display:none;margin-top:12px" role="status"><div>{i('check',16)}</div><div style="font-size:13px"><b>Publicada como rede</b><div class="meta">A unidade foi avisada e viu o texto antes de sair. Registrada na auditoria da rede.</div><a class="lk" href="{L('aval-esc')}" style="display:inline-block;margin-top:6px">Voltar para as escaladas</a></div></div>
  </div>
 </div>
 <div style="display:flex;flex-direction:column;gap:12px">
  <div class="card"><div class="hd"><h3>{i('log',15)} Linha do tempo</h3></div><div class="lista-i" id="ws-linha"></div></div>
  {regras.replace('quem publica é a unidade','quem publica é a unidade ou, se assumir, a rede')}
  <div class="card"><div class="hd"><h3>Outras pendentes da unidade</h3></div><div class="lista-i" id="ws-outras"></div><a class="btn s" id="ws-fila" href="{lk_un('GiO Alto da Lapa')}" style="margin-top:8px">Ver a fila da unidade</a></div>
 </div>
</div>
<div class="modal" id="ws-conf" role="dialog" aria-modal="true" aria-labelledby="wc-t" style="display:none"><div class="card modal-c"><h3 id="wc-t">Publicar como rede?</h3><p class="muted" style="margin:8px 0 14px">A resposta aparece no Google em alguns minutos, assinada pela unidade. A unidade é avisada e o texto fica na auditoria da rede.</p><div class="acoes-resp"><button type="button" class="btn p" id="wc-sim">Publicar no Google</button><button type="button" class="btn" id="wc-nao">Voltar e revisar</button></div></div></div>
{JS_UTIL}{JS_VALID}{DADOS_JS}<script>window.SUG={json.dumps(SUG_REDE,ensure_ascii=False)};window.LIN={json.dumps({k:RV_BY[k]['linha'] for k in ('r1','r2','r3','r4')},ensure_ascii=False)};</script>{JS86}'''
salvar(ARQ['aval-ws'],pagina('Escalada para a rede',app('admin','aval-rede',cont)))
# ---------- 87 FILA DA UNIDADE NO CASCO DA REDE ----------
JS87=r'''<script>(function(){var u=qp('u')||'GiO Alto da Lapa',est=qp('estado');
var D=window.DADOS.filter(function(x){return x[1]===u});if(!D.length){u='GiO Alto da Lapa';D=window.DADOS.filter(function(x){return x[1]===u})}
document.getElementById('un-mig').textContent=u;document.getElementById('un-tit').textContent=u;
var cl={'sem resposta':'r','unidade respondendo':'a','respondida pela unidade':'v','respondida pela rede':'v','respondida':'v'};
function pend(x){return x[7]==='sem resposta'||x[7]==='unidade respondendo'?1:0}
D.sort(function(a,b){return (pend(b)-pend(a))||((b[8]==='menciona saúde')-(a[8]==='menciona saúde'))||(a[3]-b[3])||(b[9]-a[9])});
var p=D.filter(pend),e=p.filter(function(x){return x[8]}),h=D.filter(function(x){return x[10]>=0}).map(function(x){return x[10]}).sort(function(a,b){return a-b});
function s(id,v){document.getElementById(id).textContent=v}
s('un-k1',D.length);s('un-k1d','média '+(D.reduce(function(a,x){return a+x[3]},0)/D.length).toFixed(1).replace('.',',')+' entre as listadas');
s('un-k2',p.length);s('un-k2d',p.length?('mais antiga espera há '+Math.max.apply(null,p.map(function(x){return x[9]}))+' h'):'nenhuma');
s('un-k3',e.length);s('un-k4',h.length?(String(h[Math.floor(h.length/2)]).replace('.',',')+' h'):'sem dado');
document.getElementById('un-lista').innerHTML='<div class="linha cab"><div class="c-u">Quem avaliou</div><div class="c-n">Nota</div><div class="c-t">Tema</div><div class="c-m">Avaliação</div><div class="c-s">Situação</div><div class="c-a"></div></div>'+D.map(function(x){var ac=x[7]==='sem resposta'&&x[8]?'Assumir':(pend(x)?'Acompanhar':'Ver');
 return '<div class="linha"><div class="c-u"><b>'+esc(x[5])+'</b><div class="meta">'+(x[9]>=0?'espera há '+x[9]+' h':'respondida em '+String(x[10]).replace('.',',')+' h')+'</div></div><div class="c-n">'+estr(x[3])+'</div><div class="c-t"><span class="rot">Tema</span> '+esc(x[4])+'</div><div class="c-m"><span class="rot">Avaliação</span> '+(x[6]?esc(x[6]):'<span class="meta">só nota, sem texto</span>')+(x[8]?' <span class="pill r">⚑ '+esc(x[8])+'</span>':'')+'</div><div class="c-s"><span class="pill '+(cl[x[7]]||'z')+'">'+esc(x[7])+'</span></div><div class="c-a"><a class="btn s'+(ac==='Assumir'?' p':'')+'" href="@WS@#'+x[0]+'">'+ac+'</a></div></div>'}).join('');
if(est){document.querySelectorAll('[data-estado="'+est+'"]').forEach(function(x){x.hidden=false});if(est==='vazia'){document.getElementById('un-lista').style.display='none';document.getElementById('un-vazio').hidden=false}}
else if(!p.length)document.getElementById('un-vazio').hidden=false;})();</script>'''.replace('@WS@',L('aval-ws'))
cont=f'''<div class="migalha"><a href="{L('aval-rede')}">Avaliações da rede</a> {i('chev',12)} <b style="color:var(--tinta)" id="un-mig">GiO Alto da Lapa</b></div>'''+cabec('<span id="un-tit">GiO Alto da Lapa</span>','Fila da unidade vista pela rede. A unidade responde; a rede acompanha ou assume as escaladas.',f'<a class="btn s" href="{L("seo")}">{i("target",13)} SEO local</a>')+f'''
<div class="g" style="grid-template-columns:repeat(4,1fr);margin-bottom:16px">
 <div class="card kpi"><div class="l">{i('star',15)} Avaliações listadas</div><div class="v num" id="un-k1">0</div><div class="d" id="un-k1d"></div></div>
 <div class="card kpi"><div class="l">{i('inbox',15)} Sem resposta</div><div class="v num" id="un-k2">0</div><div class="d" id="un-k2d"></div></div>
 <div class="card kpi"><div class="l">{i('flag',15)} Escaladas pendentes</div><div class="v num" id="un-k3">0</div><div class="d">notas 1 e 2 ou saúde</div></div>
 <div class="card kpi"><div class="l">{i('clock',15)} Tempo de resposta</div><div class="v num" id="un-k4">0</div><div class="d">mediana no período · meta 48 h</div></div>
</div>
<div class="estado" data-estado="desvinculado" hidden><div class="aviso a" style="margin-bottom:12px"><div>{i('alert',16)}</div><div><b>Perfil do Google não vinculado</b><div class="meta">A leitura desta unidade parou em 18/11 às 09:40. A rede pode lembrar a unidade de vincular o perfil.</div></div></div></div>
<div class="estado" data-estado="falha" hidden><div class="aviso r" style="margin-bottom:12px"><div>{i('alert',16)}</div><div><b>Falha na leitura do Google</b><div class="meta">Última leitura bem sucedida {LEITURA}. Nova tentativa a cada 30 minutos.</div></div></div></div>
<div class="card"><div class="hd"><h3>Avaliações da unidade</h3><span class="sub" style="margin-left:auto">mais urgentes primeiro</span></div><div class="linhas" id="un-lista"></div>
<div class="estado" id="un-vazio" hidden><div class="vazio">{i('check',22)}<h3>Tudo respondido</h3><p class="muted">Nenhuma avaliação sem resposta nesta unidade no período.</p></div></div></div>
{JS_UTIL}{DADOS_JS}{JS87}'''
salvar(ARQ['aval-un'],pagina('Avaliações da unidade (rede)',app('admin','aval-rede',cont)))
print('s11 ok',TOT,br(MEDIA),EM48,B24,MED_H,len(PEND),len(ESC),len(ESC_PEND),len(ESC_SEM),len(DADOS)//1024,'KB')
