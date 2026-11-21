"""Componentes compartilhados para gerar as telas estáticas (dados fictícios)."""
import json, math, random, os
D=os.path.dirname(os.path.abspath(__file__))+'/..'
random.seed(21)
IC={
'menu':'<path d="M4 7h16M4 12h16M4 17h16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>',
'home':'<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
'pin':'<path d="M12 21s-7-6.2-7-11.5A7 7 0 0 1 19 9.5C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
'map':'<path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
'users':'<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20a6.5 6.5 0 0 1 13 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 14a6 6 0 0 1 3.5 6"/>',
'inbox':'<path d="M3 13l3-8h12l3 8v6a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1z"/><path d="M3 13h5l1.5 3h5L16 13h5"/>',
'chart':'<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
'file':'<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5M9 13h6M9 17h6"/>',
'help':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3.5"/><path d="M5.6 5.6l3.9 3.9M14.5 14.5l3.9 3.9M18.4 5.6l-3.9 3.9M9.5 14.5l-3.9 3.9"/>',
'gear':'<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
'shield':'<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
'layout':'<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/>',
'globe':'<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
'search':'<circle cx="11" cy="11" r="7"/><path d="M20 20l-3.5-3.5"/>',
'bell':'<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
'filter':'<path d="M3 5h18l-7 8v6l-4 2v-8z"/>',
'plus':'<path d="M12 5v14M5 12h14"/>',
'down':'<path d="M12 4v12M6 10l6 6 6-6M4 20h16"/>',
'check':'<path d="M5 12l5 5L20 7"/>',
'clock':'<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
'phone':'<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/>',
'wa':'<path d="M21 11.5a8.4 8.4 0 0 1-12.4 7.4L3 21l2.1-5.5A8.4 8.4 0 1 1 21 11.5z"/><path d="M9 9.5c.5 2 2 3.6 4.5 4.5l1.2-1.2 2 1-.4 1.6c-3.6.4-7.6-3.4-7.3-7l1.6-.4 1 2z"/>',
'star':'<path d="M12 3l2.8 5.7 6.2.9-4.5 4.4 1.1 6.2L12 17.3 6.4 20.2l1.1-6.2L3 9.6l6.2-.9z"/>',
'chev':'<path d="M9 6l6 6-6 6"/>','chevd':'<path d="M6 9l6 6 6-6"/>',
'cal':'<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
'edit':'<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4z"/>',
'eye':'<path d="M2 12s3.5-7 10-7 10 7 10 7-3.5 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/>',
'lock':'<rect x="4" y="11" width="16" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>',
'phone2':'<rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/>',
'monitor':'<rect x="2" y="4" width="20" height="13" rx="2"/><path d="M8 21h8M12 17v4"/>',
'image':'<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="M21 15l-5-5L5 21"/>',
'list':'<path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/>',
'grid':'<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/>',
'zap':'<path d="M13 2L4 14h7l-1 8 9-12h-7z"/>',
'alert':'<path d="M10.3 3.9L1.8 18a2 2 0 0 0 1.7 3h17a2 2 0 0 0 1.7-3L13.7 3.9a2 2 0 0 0-3.4 0z"/><path d="M12 9v4M12 17h.01"/>',
'trend':'<path d="M23 6l-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/>',
'link':'<path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/>',
'drag':'<circle cx="9" cy="6" r="1"/><circle cx="15" cy="6" r="1"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><circle cx="9" cy="18" r="1"/><circle cx="15" cy="18" r="1"/>',
'more':'<circle cx="5" cy="12" r="1"/><circle cx="12" cy="12" r="1"/><circle cx="19" cy="12" r="1"/>',
'send':'<path d="M22 2L11 13M22 2l-7 20-4-9-9-4z"/>',
'clip':'<path d="M21.4 11l-9.2 9.2a6 6 0 0 1-8.5-8.5l9.2-9.2a4 4 0 0 1 5.7 5.7l-9.2 9.2a2 2 0 0 1-2.8-2.8l8.5-8.5"/>',
'book':'<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20V3H6.5A2.5 2.5 0 0 0 4 5.5z"/><path d="M4 19.5V21h16"/>',
'x':'<path d="M18 6L6 18M6 6l12 12"/>',
'sparkle':'<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/><path d="M19 17l.7 2 2 .7-2 .7-.7 2-.7-2-2-.7 2-.7z"/>',
'target':'<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/>',
'mouse':'<rect x="6" y="3" width="12" height="18" rx="6"/><path d="M12 7v4"/>',
'cursor':'<path d="M4 3l7 17 2.5-7.5L21 10z"/>',
'refresh':'<path d="M21 12a9 9 0 0 1-15.4 6.4L3 16M3 12a9 9 0 0 1 15.4-6.4L21 8"/><path d="M21 3v5h-5M3 21v-5h5"/>',
'log':'<path d="M12 8v4l3 3"/><path d="M3.05 11a9 9 0 1 1 .5 4"/><path d="M3 4v5h5"/>',
'tag':'<path d="M20.6 13.4l-7.2 7.2a2 2 0 0 1-2.8 0L2 12V2h10l8.6 8.6a2 2 0 0 1 0 2.8z"/><circle cx="7" cy="7" r="1.5"/>',
'mail':'<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/>',
'video':'<rect x="2" y="6" width="14" height="12" rx="2"/><path d="M16 10l6-3v10l-6-3z"/>',
'copy':'<rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h8"/>',
'key':'<circle cx="8" cy="15" r="4"/><path d="M11 12l9-9M17 6l3 3M14 9l2 2"/>',
'flag':'<path d="M4 21V4M4 4h12l-2 4 2 4H4"/>',
'user':'<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>',
'google':'<path d="M21 12.2c0-.7-.1-1.3-.2-1.9H12v3.6h5a4.3 4.3 0 0 1-1.9 2.8v2.3h3A9 9 0 0 0 21 12.2z"/><path d="M12 21a8.9 8.9 0 0 0 6.1-2.2l-3-2.3a5.5 5.5 0 0 1-8.2-2.9H3.8v2.4A9 9 0 0 0 12 21z"/><path d="M6.9 13.6a5.4 5.4 0 0 1 0-3.4V7.8H3.8a9 9 0 0 0 0 8.1z"/><path d="M12 6.6a4.9 4.9 0 0 1 3.5 1.4l2.6-2.6A8.8 8.8 0 0 0 12 3a9 9 0 0 0-8.2 4.8l3.1 2.4A5.4 5.4 0 0 1 12 6.6z"/>',
}
def i(n,s=16,cls=''): return f'<svg class="i {cls}" viewBox="0 0 24 24" style="width:{s}px;height:{s}px">{IC[n]}</svg>'
U=json.load(open(f'{D}/../raw/api-listagem.json'))['unidades']
UNID=[v for v in U.values()]
ARQ={ # chave de navegação -> arquivo (protótipo estático)
 'login':'01-login','2fa':'02-2fa','senha':'03-primeiro-acesso-senha',
 'rede':'04-admin-dashboard-rede','unidades':'05-admin-unidades-tabela','mapa':'06-admin-unidades-mapa','unidade':'07-admin-unidade-detalhe','lp':'08-admin-unidade-landing-pages',
 'aprov':'09-admin-aprovacoes','leads':'10-admin-leads-kanban','leadslista':'11-admin-leads-lista','lead':'12-admin-lead-detalhe','rel':'13-admin-relatorios','insights':'14-admin-relatorios-inteligentes',
 'suporte':'15-admin-suporte','users':'16-admin-usuarios-perfis','aud':'17-admin-auditoria','lgpd':'18-admin-lgpd','seo':'19-admin-seo-local','tpl':'20-admin-templates-marca',
 'modelos':'21-admin-modelos-ficha','modulos':'22-admin-modulos','ajuda':'23-central-ajuda',
 'f-inicio':'24-franqueado-dashboard','f-unidade':'25-franqueado-minha-unidade','f-fotos':'26-franqueado-fotos','f-faq':'27-franqueado-faq','f-tpl':'28-franqueado-templates',
 'f-ab':'29-franqueado-comparativo-ab','f-editor':'30-franqueado-editor','f-dominio':'31-franqueado-dominio','f-nova':'32-franqueado-unidade-nova','f-leads':'33-franqueado-leads-primeiro-dia',
 'f-notif':'34-franqueado-notificacoes','m-leads':'35-mobile-leads','m-lead':'36-mobile-lead',
 'lpA':'37-landing-a-desktop','lpAm':'38-landing-a-mobile','lpB':'39-landing-b-desktop','lpBm':'40-landing-b-mobile','lpC':'41-landing-c-desktop','lpCm':'42-landing-c-mobile',
 # rodada 3: área do cliente (002)
 'c-entrar':'43-cliente-mobile-entrar','c-dados':'44-cliente-mobile-dados','c-interesses':'45-cliente-mobile-interesses','c-inicio':'46-cliente-mobile-inicio','c-ofertas':'47-cliente-mobile-ofertas',
 'c-horarios':'48-cliente-mobile-agendar-horarios','c-confirma':'49-cliente-mobile-agendar-confirmacao','c-pacote':'50-cliente-mobile-pacote','c-privacidade':'51-cliente-mobile-privacidade','c-inicio-d':'52-cliente-inicio-desktop',
 'f-procs':'53-franqueado-procedimentos-precos','f-promos':'54-franqueado-promocoes','f-camps':'55-franqueado-campanhas','f-camp':'56-franqueado-campanha-assistente','f-tags':'57-franqueado-tags-medicao',
 'controles':'58-admin-controles-liberacoes','mural':'59-admin-mural-aviso','camp-rede':'60-admin-campanha-rede','camp-aprov':'61-admin-campanhas-aprovacao','perf':'62-admin-performance-campanhas',
 # 003
 'quiz':'63-admin-quiz-gerador','q-perg':'64-quiz-mobile-pergunta','q-res':'65-quiz-mobile-resultado','intel':'66-admin-inteligencia-demanda','sazon':'67-admin-inteligencia-sazonalidade',
 'dic':'68-admin-tracking-dicionario','utm':'69-admin-tracking-utm','saude':'70-admin-tracking-saude',
 # 002 · área do cliente no computador (crítica da tela 52) e perfil no celular
 'c-ofertas-d':'71-cliente-ofertas-desktop','c-agendar-d':'72-cliente-agendar-desktop','c-pacote-d':'73-cliente-pacote-desktop','c-avaliar-d':'74-cliente-avaliar-desktop',
 'c-privacidade-d':'75-cliente-privacidade-desktop','c-perfil-d':'76-cliente-perfil-desktop','c-unidade-d':'77-cliente-unidade-desktop','c-avisos-d':'78-cliente-avisos-desktop','c-perfil':'79-cliente-mobile-perfil',
 # avaliações do Google (monitoramento e resposta)
 'f-aval':'80-franqueado-avaliacoes','f-aval-det':'81-franqueado-avaliacao-detalhe','m-aval':'82-mobile-avaliacoes','m-aval-det':'83-mobile-avaliacao-detalhe','aval-rede':'84-admin-avaliacoes-rede',
 'aval-esc':'85-admin-avaliacoes-escaladas','aval-ws':'86-admin-avaliacao-escalada','aval-un':'87-admin-avaliacoes-unidade',
 'rel-camp':'90-admin-relatorios-campanhas','rel-funil':'91-admin-relatorios-leads-funil','rel-atend':'92-admin-relatorios-atendimento','rel-trafego':'93-admin-relatorios-quiz-landings','rel-google':'94-admin-relatorios-seo-avaliacoes','rel-cliente':'95-admin-relatorios-area-cliente','rel-unidades':'96-admin-relatorios-unidades','rel-unidade':'97-admin-relatorios-unidade','rel-metas':'98-admin-relatorios-metas-alertas','rel-export':'99-admin-relatorios-exportar','rel-config':'89-admin-relatorios-metas-regras','f-rel':'97-franqueado-relatorio-unidade'}
def L(k): return ARQ[k]+'.html'
SELO_TXT='Ambiente de demonstração. Números e pessoas são ilustrativos, salvo quando a fonte é citada.'
def pagina(titulo,corpo,largura=1440,extra_css=''):
    vp='width=390' if largura==390 else 'width=device-width, initial-scale=1'
    bw='body{width:390px}' if largura==390 else ''
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="{vp}"><title>{titulo} · Sistema de Unidades Gio (demonstração)</title>
<link rel="stylesheet" href="estilo.css"><style>{bw}{extra_css}</style></head><body>{corpo}</body></html>"""
NAV_ADMIN=[('sec','Rede'),('home','Visão geral','rede'),('pin','Unidades','unidades','130'),('shield','Aprovações','aprov','7'),
 ('sec','Relacionamento'),('inbox','Central de leads','leads','38'),('send','Campanhas','camp-aprov','4'),('flag','Mural de avisos','mural'),('help','Suporte','suporte','12'),
 ('sec','Inteligência'),('chart','Relatórios','rel'),('sparkle','Relatórios inteligentes','insights','3'),('trend','Demanda e quiz','intel'),('target','SEO local','seo'),('star','Avaliações','aval-rede','26'),('zap','Tracking','saude','2'),
 ('sec','Plataforma'),('key','Controles da rede','controles'),('layout','Templates e marca','tpl'),('file','Modelos de ficha','modelos'),('grid','Módulos','modulos'),('users','Usuários e perfis','users'),('log','Auditoria','aud'),('lock','LGPD','lgpd','4'),
 ('sec','Ajuda'),('book','Central de ajuda','ajuda')]
NAV_FRANQ=[('sec','Minha operação'),('home','Início','f-inicio'),('pin','Minha unidade','f-unidade'),('image','Fotos','f-fotos'),('help','Perguntas frequentes','f-faq'),('layout','Página da unidade','f-tpl'),('globe','Domínio','f-dominio'),('zap','Tags e medição','f-tags'),
 ('sec','Clientes e vendas'),('inbox','Leads','leads','9'),('star','Avaliações','f-aval','4'),('tag','Procedimentos','f-procs'),('send','Campanhas','f-camps'),('bell','Notificações','f-notif','3'),
 ('sec','Apoio'),('chart','Relatórios','f-rel'),('send','Suporte da rede','suporte','1'),('book','Central de ajuda','ajuda')]
def side(modo,ativo,ctx=None,sem_badges=False):
    nav=NAV_ADMIN if modo=='admin' else NAV_FRANQ
    h=['<aside class="side"><a class="logo" href="'+L('rede' if modo=='admin' else 'f-inicio')+'" style="padding:0 8px 16px;min-height:0"><img src="../assets/'+('logo-gio-branco.png' if modo=='admin' else 'logo-gio.png')+'" alt="Gio"><span>'+('Portal da<br>Rede' if modo=='admin' else 'Portal do<br>Franqueado')+'</span></a>']
    if modo=='admin':
        h.append('<div class="ctx"><div class="av">GR</div><div><b>Rede Gio</b><small>130 unidades · Brasil</small></div>'+i('chevd',14)+'</div>')
    else:
        c=ctx or ('AL','GiO Alto da Lapa','São Paulo/SP · Full')
        h.append(f'<div class="ctx"><div class="av">{c[0]}</div><div><b>{c[1]}</b><small>{c[2]}</small></div>'+i('chevd',14)+'</div>')
    for it in nav:
        if it[0]=='sec': h.append(f'<div class="sec">{it[1]}</div>'); continue
        n=f'<span class="n">{it[3]}</span>' if len(it)>3 and not sem_badges else ''
        h.append(f'<a href="{L(it[2])}" class="{"on" if it[2]==ativo else ""}">{i(it[0],17)}{it[1]}{n}</a>')
    pessoa=('IN','Ingrid N.','Marketing da rede') if modo=='admin' else ('RF','Renata F.','Franqueada')
    h.append(f'<div class="rodape"><div class="av">{pessoa[0]}</div><div><b>{pessoa[1]}</b><small>{pessoa[2]}</small></div><a href="{L("login")}" style="margin-left:auto;min-height:0;padding:0" title="Sair">{i("gear",16)}</a></div></aside>')
    return ''.join(h)
def selo(): return f'<span class="selo" title="{SELO_TXT}">{i("eye",13)} Ambiente de demonstração</span>'
def topo(modo,placeholder):
    return f"""<div class="top"><button type="button" class="ib menu-btn" aria-label="Abrir menu" aria-expanded="false" onclick="var s=document.querySelector('.side');s.classList.toggle('aberta');this.setAttribute('aria-expanded',s.classList.contains('aberta'))">{i('menu')}</button><div class="busca">{i('search')}<span>{placeholder}</span><kbd>Ctrl K</kbd></div>
<div class="acoes">{selo()}<a class="ib" href="{L('ajuda')}" title="Central de ajuda">{i('help')}</a><a class="ib" href="{L('f-notif') if modo=='franq' else L('insights')}" title="Notificações">{i('bell')}<span class="dot"></span></a></div></div>"""
def periodo(txt='01 a 21 nov 2026'):
    """Controle de período: só nas telas em que ele filtra o conteúdo (C09), um por tela."""
    return f'<span class="sw"><span>7 dias</span><span>30 dias</span><span class="on">{i("cal",13)} {txt}</span></span>'
def app(modo,ativo,conteudo,placeholder=None,ctx=None,sem_badges=False):
    ph=placeholder or ("Buscar unidade, lead, ticket ou pessoa" if modo=="admin" else "Buscar lead, ticket ou artigo")
    return f'<div class="app {modo}">{side(modo,ativo,ctx,sem_badges)}<main class="main">{topo(modo,ph)}{conteudo}<div class="demo-rod">{i("eye",13)} {SELO_TXT}</div></main></div>'
def campo(l,v,estado='',aj='',ic='',err=''):
    """estado: T travado pela rede, E editável, EA com aprovação, L leitura."""
    tag={'T':'<span class="pill t" style="padding:2px 8px" title="Rede: só a rede altera">'+i('lock',11)+'<span class="tx"> Rede</span></span>','EA':'<span class="pill ea" style="padding:2px 8px" title="Com aprovação: a rede revisa">'+i('shield',11)+'<span class="tx"> Com aprovação</span></span>','E':'<span class="pill e" style="padding:2px 8px" title="Editável: muda na hora">'+i('edit',11)+'<span class="tx"> Editável</span></span>','L':'<span class="pill z" style="padding:2px 8px" title="Somente leitura">'+i('eye',11)+'<span class="tx"> Somente leitura</span></span>'}.get(estado,'')
    cls=' lock' if estado in ('T','L') else (' err' if err else '')
    return f'<div class="campo"><label><span class="lt" title="{l}">{l}</span>{tag}</label><div class="in{cls}">{i(ic,15) if ic else ""}{v}</div><div class="info">{f"<div class=erro>{err}</div>" if err else ""}{f"<div class=ajuda>{aj}</div>" if aj else ""}</div></div>'
def kpi(ic,rot,val,det):
    return f'<div class="card kpi"><div class="l">{i(ic,15)} {rot}</div><div class="v">{val}</div><div class="d">{det}</div></div>'
def fmt(n): return f'{n:,}'.replace(',','.')
# ---------- dados de demonstração (fictícios, exceto nome de bairro e cidade) ----------
DEMO={
 'altodalapa':dict(nome='GiO Alto da Lapa',bairro='Alto da Lapa',cidade='São Paulo',uf='SP',ddd='11',end='Rua Demonstração, 100',dom='gioaltodalapa.exemplo.com.br',ig='@gio.demo.altodalapa',nota='4,8',aval=120,tpl='B'),
 'curitiba':dict(nome='GiO Batel',bairro='Batel',cidade='Curitiba',uf='PR',ddd='41',end='Rua Demonstração, 200',dom='giobatel.exemplo.com.br',ig='@gio.demo.batel',nota='4,8',aval=210,tpl='A'),
 'campinas-cambui':dict(nome='GiO Cambuí',bairro='Cambuí',cidade='Campinas',uf='SP',ddd='19',end='Rua Demonstração, 300',dom='giocambui.exemplo.com.br',ig='@gio.demo.cambui',nota='4,9',aval=180,tpl='C'),
}
for k,v in DEMO.items():
    v['tel']=f"({v['ddd']}) 90000-0000"; v['wa']=f"({v['ddd']}) 90000-0001"; v['cep']='00000-000'; v['cnpj']='00.000.000/0001-00'
    v['email']=f"contato@{v['dom']}"
CNPJ_DEMO='00.000.000/0001-00'
IP_DEMO='192.0.2.10'
# completude e índice de conversão: uma única fonte para todas as telas (C14, C17)
COMPL_FIX={'altodalapa':90,'curitiba':96,'campinas-cambui':93,'boulevardtatuape':91,'porto-alegre-bom-fim':81,'ribeirao-preto-centro':78,'aldeota':74,'asa-sul':69,'salvador':62,'vila-madalena':58,'londrina':55,'montes-claros':41,'ipiranga':37,'go-catalao-centro':28}
def completude(u):
    c=COMPL_FIX.get(u['url_site'], score(u))
    return c if (u['latitude'] and u['longitude']) else min(c,54)  # sem coordenadas: schema e mapa quebrados, teto 54
def classe(c): return 'v' if c>=80 else ('a' if c>=55 else 'r')
COR_CL={'v':'#0B7A54','a':'#C77A00','r':'#B4234A'}
RANKING=[('curitiba','Batel · Curitiba',96,'+12'),('campinas-cambui','Cambuí · Campinas',93,'+8'),('boulevardtatuape','Boulevard Tatuapé · São Paulo',91,'+5'),('altodalapa','Alto da Lapa · São Paulo',90,'+3'),('porto-alegre-bom-fim','Bom Fim · Porto Alegre',88,'+1')]
# ---------- gráficos SVG ----------
def area(series,cores,w=640,h=200,labels=None,ymax=None,grade=4):
    n=len(series[0]); ymax=ymax or max(max(s) for s in series)*1.15
    px=lambda k: 36+k*(w-46)/(n-1); py=lambda v: h-24-(v/ymax)*(h-40)
    out=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}">','<defs>']
    for k,c in enumerate(cores):
        out.append(f'<linearGradient id="ga{k}{w}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{c}" stop-opacity=".28"/><stop offset="1" stop-color="{c}" stop-opacity="0"/></linearGradient>')
    out.append('</defs>')
    for g in range(grade+1):
        y=16+g*(h-40)/grade; v=ymax*(1-g/grade)
        out.append(f'<line x1="36" x2="{w-10}" y1="{y:.1f}" y2="{y:.1f}" stroke="#eee6f1"/><text x="28" y="{y+4:.1f}" font-size="12" fill="#5E5566" text-anchor="end" font-family="Inter">{int(v)}</text>')
    for k,(s,c) in enumerate(zip(series,cores)):
        pts=' '.join(f'{px(j):.1f},{py(v):.1f}' for j,v in enumerate(s))
        out.append(f'<polygon points="{px(0):.1f},{h-24} {pts} {px(n-1):.1f},{h-24}" fill="url(#ga{k}{w})"/><polyline points="{pts}" fill="none" stroke="{c}" stroke-width="2.4" stroke-linejoin="round"/>')
    if labels:
        step=max(1,n//7)
        for j in range(0,n,step): out.append(f'<text x="{px(j):.1f}" y="{h-6}" font-size="12" fill="#5E5566" text-anchor="middle" font-family="Inter">{labels[j]}</text>')
    out.append('</svg>'); return ''.join(out)
def barras_h(itens,cor='url(#gb)',w=300,larg_rot=120,alt=26,fmt=str):
    mx=max(v for _,v in itens); h=len(itens)*alt
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}"><defs><linearGradient id="gb" x1="0" x2="1"><stop offset="0" stop-color="#4c1455"/><stop offset="1" stop-color="#b0197e"/></linearGradient></defs>']
    for k,(r,v) in enumerate(itens):
        y=k*alt; bw=(w-larg_rot-46)*v/mx
        o.append(f'<text x="0" y="{y+16}" font-size="12" fill="#463b4e" font-family="Inter">{r}</text><rect x="{larg_rot}" y="{y+6}" width="{w-larg_rot-46}" height="12" rx="6" fill="#f3eaf6"/><rect x="{larg_rot}" y="{y+6}" width="{bw:.1f}" height="12" rx="6" fill="{cor}"/><text x="{w}" y="{y+16}" font-size="12" fill="#1d1424" text-anchor="end" font-weight="600" font-family="Inter">{fmt(v)}</text>')
    o.append('</svg>'); return ''.join(o)
def donut(partes,cores,tam=150,esp=20,centro='',sub=''):
    tot=sum(partes); r=(tam-esp)/2; c=tam/2; ang=-math.pi/2; o=[f'<svg viewBox="0 0 {tam} {tam}" width="{tam}" height="{tam}">']
    for v,cor in zip(partes,cores):
        a2=ang+2*math.pi*v/tot; large=1 if a2-ang>math.pi else 0
        x1,y1=c+r*math.cos(ang),c+r*math.sin(ang); x2,y2=c+r*math.cos(a2-0.02),c+r*math.sin(a2-0.02)
        o.append(f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 {large} 1 {x2:.1f} {y2:.1f}" stroke="{cor}" stroke-width="{esp}" fill="none" stroke-linecap="butt"/>'); ang=a2
    o.append(f'<text x="{c}" y="{c+2}" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="22" fill="#1d1424">{centro}</text><text x="{c}" y="{c+20}" text-anchor="middle" font-family="Inter" font-size="12" fill="#5E5566">{sub}</text></svg>')
    return ''.join(o)
def spark(vals,cor='#b0197e',w=90,h=28):
    mx,mn=max(vals),min(vals); pts=' '.join(f'{k*(w-4)/(len(vals)-1)+2:.1f},{h-3-(v-mn)/(mx-mn or 1)*(h-6):.1f}' for k,v in enumerate(vals))
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}"><polyline points="{pts}" fill="none" stroke="{cor}" stroke-width="2" stroke-linejoin="round"/></svg>'
def funil(etapas,w=520):
    mx=etapas[0][1]; o=['<div style="display:flex;flex-direction:column;gap:8px">']
    for k,(r,v,extra) in enumerate(etapas):
        pct=v/mx*100
        o.append(f'<div style="display:grid;grid-template-columns:150px 1fr 64px 130px;align-items:center;gap:12px"><span style="font-weight:500;color:#463b4e">{r}</span><div style="background:#f3eaf6;border-radius:9px;height:26px"><div style="width:{pct:.1f}%;height:100%;border-radius:9px;background:linear-gradient(90deg,#4c1455,#b0197e)"></div></div><b style="text-align:right">{fmt(v)}</b><span class="meta">{extra}</span></div>')
    o.append('</div>'); return ''.join(o)
# ---------- mapa do Brasil (malha de UFs do IBGE, embutida localmente) ----------
SIGLA={'11':'RO','12':'AC','13':'AM','14':'RR','15':'PA','16':'AP','17':'TO','21':'MA','22':'PI','23':'CE','24':'RN','25':'PB','26':'PE','27':'AL','28':'SE','29':'BA','31':'MG','32':'ES','33':'RJ','35':'SP','41':'PR','42':'SC','43':'RS','50':'MS','51':'MT','52':'GO','53':'DF'}
GEO=json.load(open(f'{D}/assets/geo/br-ufs-ibge.json'))
def _aneis(g):
    if g['type']=='Polygon': return [g['coordinates'][0]]
    return [p[0] for p in g['coordinates']]
def mapa_geo(w,h,pontos,box,cont_uf=None,sel=None,rotulos=True,uid='m',escala=None):
    """box=(lat_min,lat_max,lng_min,lng_max). Projeção equirretangular com correção de cosseno da latitude média."""
    la0,la1,lo0,lo1=box; cosl=math.cos(math.radians((la0+la1)/2))
    sx=w/((lo1-lo0)*cosl); sy=h/(la1-la0); k=min(sx,sy)
    ox=(w-(lo1-lo0)*cosl*k)/2; oy=(h-(la1-la0)*k)/2
    P=lambda lat,lng:(ox+(lng-lo0)*cosl*k, oy+(la1-lat)*k)
    esc=escala or (lambda n: '#f7f1f9' if not n else ('#ead9f0' if n<3 else ('#d8bde3' if n<8 else ('#c39ad3' if n<40 else '#a877bd'))))
    o=[f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="display:block" role="img" aria-label="Mapa do Brasil por UF">']
    labs=[]
    for f in GEO['features']:
        sg=SIGLA[f['properties']['codarea']]; n=(cont_uf or {}).get(sg,0)
        d=''; maior=None
        for ring in _aneis(f['geometry']):
            pts=[P(b,a) for a,b in ring]
            d+='M'+' '.join(f'{x:.1f},{y:.1f}' for x,y in pts)+'Z'
            if maior is None or len(ring)>len(maior): maior=pts
        cls='uf sel' if sg==sel else 'uf'
        o.append(f'<path id="BR-{sg}" class="{cls}" d="{d}" fill="{esc(n)}" stroke="#fff" stroke-width="1"><title>{sg} · {n} unidade{"s" if n!=1 else ""}</title></path>')
        if rotulos and n:
            cx=sum(p[0] for p in maior)/len(maior); cy=sum(p[1] for p in maior)/len(maior)
            labs.append((sg,cx,cy,n))
    for (lat,lng,cor,r) in pontos:
        x,y=P(lat,lng)
        if -5<x<w+5 and -5<y<h+5: o.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{cor}" stroke="#fff" stroke-width="1.4"/>')
    for sg,cx,cy,n in labs:
        if sg in ('DF','AL','SE'): continue
        o.append(f'<text x="{cx:.1f}" y="{cy:.1f}" text-anchor="middle" font-family="Inter" font-size="12" font-weight="700" fill="#33103d" stroke="#fff" stroke-width="3" paint-order="stroke">{sg}</text>')
    o.append('</svg>'); return ''.join(o)
BOX_BR=(-34.0,5.4,-74.1,-34.6)
def mapa_br(w,h,pontos,cont_uf=None,sel=None,rotulos=True):
    return mapa_geo(w,h,pontos,BOX_BR,cont_uf,sel,rotulos)
def pontos_unidades(r=5):
    pts=[]
    for u in UNID:
        if u['latitude'] and u['longitude']:
            pts.append((float(u['latitude']),float(u['longitude']),COR_CL[classe(completude(u))],r))
    return pts
# ---------- "Como chegar": recorte OSM do bairro, em cores da marca ----------
def mapa_osm(nome,w,h,raio=None,pin=True):
    d=json.load(open(f'{D}/assets/geo/osm-{nome}.json')); lat,lng=d['centro']; dd=d['d']
    la0,la1,lo0,lo1=lat-dd*0.6,lat+dd*0.6,lng-dd,lng+dd
    cosl=math.cos(math.radians(lat)); k=max(w/((lo1-lo0)*cosl),h/(la1-la0))
    P=lambda a,b:(w/2+(b-lng)*cosl*k, h/2-(a-lat)*k)
    larg={'motorway':9,'trunk':8,'primary':7,'secondary':6,'tertiary':5,'primary_link':4,'secondary_link':4,'residential':3.6,'unclassified':3.4,'living_street':3,'service':2,'busway':3}
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" preserveAspectRatio="xMidYMid slice" style="display:block;background:#f4eef6">']
    for e in d['elements']:
        t=e.get('tags',{})
        if t.get('leisure')=='park' or t.get('natural')=='water':
            pts=' '.join('%.1f,%.1f'%P(g['lat'],g['lon']) for g in e.get('geometry',[]))
            if pts: o.append(f'<polygon points="{pts}" fill="{"#cfe8dc" if t.get("leisure") else "#cfe0f2"}"/>')
    vias=[e for e in d['elements'] if e.get('tags',{}).get('highway') in larg]
    for camada in ('borda','miolo'):
        for e in sorted(vias,key=lambda e:larg[e['tags']['highway']]):
            wd=larg[e['tags']['highway']]
            pts=' '.join('%.1f,%.1f'%P(g['lat'],g['lon']) for g in e.get('geometry',[]))
            cor='#ffffff' if wd<5 else '#fbe3f0'
            if camada=='borda': o.append(f'<polyline points="{pts}" fill="none" stroke="#dccfe2" stroke-width="{wd+2}" stroke-linecap="round" stroke-linejoin="round"/>')
            else: o.append(f'<polyline points="{pts}" fill="none" stroke="{cor}" stroke-width="{wd}" stroke-linecap="round" stroke-linejoin="round"/>')
    if raio: o.append(f'<circle cx="{w/2}" cy="{h/2}" r="{raio}" fill="#b0197e" fill-opacity=".08" stroke="#b0197e" stroke-dasharray="6 5" stroke-width="1.5"/>')
    if pin: o.append(f'<g transform="translate({w/2-14},{h/2-36})"><path d="M14 36s-12-10.5-12-20A12 12 0 0 1 26 16c0 9.5-12 20-12 20z" fill="#b0197e" stroke="#fff" stroke-width="2"/><circle cx="14" cy="15" r="4.5" fill="#fff"/></g>')
    o.append('</svg>'); return ''.join(o)
OSM_CRED='© colaboradores do OpenStreetMap'
def score(u):
    rnd=random.Random(u['url_site']); base=40+rnd.random()*55
    return int(base)
def salvar(nome,html):
    open(f'{D}/telas/{nome}.html','w',encoding='utf-8').write(html)

import re as _re
def nome_un(u, curto=30):
    n=u['unidade']
    n=_re.sub(r'^(Sp|Rj|Mg|Pr|Rs|Sc|Go|Df|Ba|Ce|Pe|Ma|Es|Ms|Mt|Pa|Am|Rn|Pb|Al|Se|Pi|To|Ro)\s+','',n)
    n=n.replace(' Da ',' da ').replace(' Do ',' do ').replace(' De ',' de ')
    return ('GiO '+n)[:curto]

from collections import Counter as _C
UF_CONT=_C(u['nome_uf'] for u in UNID)
COM_COORD=[u for u in UNID if u['latitude'] and u['longitude']]
SEM_COORD=[u for u in UNID if not (u['latitude'] and u['longitude'])]
CL_MAPA=_C(classe(completude(u)) for u in COM_COORD)
CL_TOT=_C(classe(completude(u)) for u in UNID)
COMPL_MEDIA=round(sum(completude(u) for u in UNID)/len(UNID))
def uf_top(n=7):
    top=UF_CONT.most_common(n); resto=UF_CONT.most_common()[n:]
    return top+[(f'Demais {len(resto)} UFs',sum(v for _,v in resto))]

# ---------- rodada 3: dados de demonstração da área do cliente, campanhas, quiz e tracking ----------
# Uma única fonte para todas as telas novas (os números se repetem entre telas e no protótipo).
CLI_REDE=48312                      # clientes com conta na marca
CLI_NOVOS=3184                      # novos no período 01 a 21 nov
CONS_PCT={'E-mail':61,'WhatsApp':47,'Push':22,'Área do cliente':100}
CONS_REDE={k:round(CLI_REDE*v/100) for k,v in CONS_PCT.items()}
CLI_AL=1284                         # clientes vinculados ao Alto da Lapa
CONS_AL={k:round(CLI_AL*v/100) for k,v in CONS_PCT.items()}
SP_UN=UF_CONT['SP']                 # unidades em SP (regional SP)
COTA_UN=2; COTA_USADA_AL=1          # campanhas por mês por unidade (aprovado em 21/11)
# campanha da rede "Verão sem pelos" (SP e PR), funil de alcance calculado
CR_BASE=21400; CR_CANAL=round(CR_BASE*CONS_PCT['WhatsApp']/100); CR_FREQ=1112; CR_FINAL=CR_CANAL-CR_FREQ
CR_UN=SP_UN+UF_CONT['PR']
# aprovação de campanhas: 4 pendentes
# mural: público de um aviso para as 130 unidades
MURAL_PERF={'Admin da unidade':130,'Gerente':141,'Recepção':141}; MURAL_TOT=sum(MURAL_PERF.values())
MURAL_CONF=97                       # unidades que confirmaram o aviso anterior
# quiz "Qual tratamento combina com você?"
QZ_INI=6940; QZ_FIM=4512; QZ_PCT=round(QZ_FIM/QZ_INI*100); QZ_CONTA=1388
QZ_DEM=[('Depilação a laser',1715),('Limpeza de pele',1038),('Ultraformer',631),('Peeling',496),('Criolipólise',361),('Microagulhamento',271)]
# tracking (01 a 21 nov): mesmos números da tela 04 (2.986 leads, 1.733 agendados, 1.071 compareceram)
EV=[('unidade_visualizada','Página da unidade aberta',412880),('lead_iniciado','Formulário começou a ser preenchido',4630),('lead_enviado','Lead aceito pelo servidor',2986),('agendamento_concluido','Agendamento confirmado',1733),
    ('whatsapp_clicado','Clique no WhatsApp',18240),('telefone_clicado','Clique no telefone',3912),('rota_clicada','Clique em como chegar',6205),('atendimento_compareceu','Comparecimento vindo da DocBiz',1071),
    ('quiz_iniciado','Quiz começou',6940),('quiz_concluido','Quiz terminou',4512),('cliente_cadastrado','Conta de cliente criada',3184),('campanha_clicada','Clique em campanha',9870)]
EV_INVAL_PCT='0,4'; UTM_INVAL_PCT='3,1'; DIVERG_GA4='2,8'
def status_bar(escuro=False,com_selo=True):
    c='#fff' if escuro else 'var(--tinta)'
    sl=f'<span style="flex:1;display:flex;justify-content:center">{selo()}</span>' if com_selo else ''
    return f'<div style="height:44px;display:flex;align-items:center;padding:0 22px;font:600 15px Inter;color:{c}"><span>9:41</span>{sl}<span style="margin-left:{"0" if com_selo else "auto"};display:flex;gap:6px;align-items:center"><span style="width:18px;height:10px;border:1.5px solid {c};border-radius:3px"></span></span></div>'
def tab_cli(on):
    it=[('home','Início','c-inicio'),('tag','Ofertas','c-ofertas'),('cal','Agendar','c-horarios'),('grid','Pacotes','c-pacote'),('user','Perfil','c-perfil')]
    return '<nav class="tabbar">'+''.join(f'<a class="{"on" if n==on else ""}" href="{L(lk)}"{" aria-current=page" if n==on else ""}>{i(ic,22)}<span>{t}</span></a>' for n,(ic,t,lk) in enumerate(it))+'</nav>'
def mob(conteudo,tab=None,fundo='#fbf7f9',sem_tab=False,longo=False):
    tb='' if sem_tab else tab_cli(tab)
    if longo:  # tela que rola: a captura mostra a página inteira e a barra de abas fica presa no rodapé
        return f'<div class="mob longo" style="background:{fundo}">{status_bar()}<div class="rolagem" style="padding:0 16px 24px">{conteudo}</div>{tb}</div>'
    alt='754px' if not sem_tab else '800px'
    return f'<div class="mob" style="background:{fundo}">{status_bar()}<div class="rolagem" style="height:{alt};padding:0 16px">{conteudo}</div>{tb}</div>'
# funis de alcance de campanha de unidade (calculados; usados em 56 e 61)
def funil_un(interesse):
    c=round(interesse*CONS_PCT['WhatsApp']/100); f=round(c*0.08); return [('Clientes vinculados',CLI_AL),('Com interesse no procedimento',interesse),('Com consentimento de WhatsApp',c),('Sem mensagem nos últimos 7 dias',c-f)]
INT_LIMPEZA=412; INT_ULTRA=236
CAMP_ULTRA=funil_un(INT_ULTRA)[-1][1]; CAMP_LIMP=funil_un(INT_LIMPEZA)[-1][1]
# regionais e controles da rede
REG={'Regional SP':SP_UN,'Regional Sul':UF_CONT['PR']+UF_CONT['RS']+UF_CONT['SC']}
REG['Demais regionais']=len(UNID)-sum(REG.values())
UN_DOMINIO=12                       # unidades com domínio próprio (tags da unidade liberadas por exceção)
# performance de campanhas (01 a 21 nov): agendamentos de campanha dentro dos 1.733 da rede; comparecimentos dentro dos 1.071
PF=[('Entregues',52400),('Abertas',31900),('Cliques',9870),('Agendamentos',214),('Compareceram',131)]
def cabec(t,p,dir=''): return f'<div class="cab"><div><h1>{t}</h1><p>{p}</p></div><div class="dir">{dir}</div></div>'
def tabs(itens,on):
    return '<div class="tabs">'+''.join(f'<a class="{"on" if k==on else ""}" href="{L(lk) if lk else "#"}"{"" if lk else " data-sem-rota=1"}>{t}</a>' for k,(t,lk) in enumerate(itens))+'</div>'
