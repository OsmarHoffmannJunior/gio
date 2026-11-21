import os,base64,io
from PIL import Image
D=os.path.dirname(os.path.abspath(__file__))+'/..'
T=[('01-login','Todos','Login','Entrada única por papel (franqueado, rede, parceiro), Google da rede e 2FA obrigatório para rede e call center.'),
('02-admin-dashboard-rede','Admin Gio','Visão geral da rede','KPIs do funil, leads por dia, origem por UTM, ranking de conversão, unidades por estado e alertas de SEO e tracking.'),
('03-admin-unidades-tabela','Admin Gio','Unidades em tabela','Busca por nome, CEP ou ID DocBiz, 9 filtros, visões salvas, completude, template, domínio, leads 30d, nota e alertas.'),
('04-admin-unidades-mapa','Admin Gio','Unidades no mapa','117 unidades com coordenadas reais coloridas por completude, zoom da Grande SP e lista das 13 sem coordenadas.'),
('05-admin-unidade-detalhe','Admin Gio','Detalhe da unidade','11 abas, campos travados pela rede, NAP conferido com o Google, raio de bairros, horários, completude e acessos.'),
('06-admin-aprovacoes','Admin Gio','Aprovações','Fila de mudanças das unidades, diff de texto, checagem automática das regras da marca, galeria e histórico de versões.'),
('07-leads-kanban','Admin Gio e call center','Central de leads (quadro)','Kanban com SLA de 1º contato, fila call center x unidade, origem, falhas de envio ao DocBiz e filtros.'),
('08-lead-detalhe','Admin Gio e call center','Lead com jornada','Do clique no anúncio ao agendamento, UTMs, status DocBiz, dados mascarados e consentimento LGPD.'),
('09-relatorios','Admin Gio e agência','Relatórios','Modelos prontos, construtor com prévia, exportação PDF e planilha, envios agendados por perfil.'),
('10-suporte','Admin Gio e franqueado','Suporte','Fila de chamados com prazo, conversa, artigo da base sugerido e verificação automática de domínio.'),
('11-usuarios-permissoes','Admin Gio','Usuários e permissões','Matriz por papel e escopo, isolamento por unidade, 2FA, acessos que expiram e auditoria do dia.'),
('12-franqueado-dashboard','Franqueado','Início do franqueado','Posição no ranking contra a mediana, KPIs comparados à rede, leads recentes e tarefas que sobem o ranking.'),
('13-franqueado-minha-unidade','Franqueado','Minha unidade','Edição de contato, texto Sobre com regras da marca, tratamentos da lista da rede, completude e status de aprovação.'),
('14-franqueado-templates','Franqueado','Escolha de modelo','Três modelos (A Conversão direta, B Vitrine da clínica, C Autoridade local) com métrica de cada um e recomendação.'),
('15-franqueado-editor','Franqueado','Editor de blocos','Blocos fixos, editáveis e automáticos, prévia ao vivo, paleta travada e verificação da marca antes de enviar.'),
('16-franqueado-dominio','Franqueado','Domínio próprio','Assistente de DNS em 5 passos, verificação automática e estratégia de uma URL canônica por unidade.'),
('17-mobile-leads','Franqueado (celular)','Leads no celular','Leads esperando com cronômetro de SLA e ação direta de WhatsApp ou ligação.'),
('18-mobile-lead','Franqueado (celular)','Lead no celular','Ações rápidas, próximo passo e jornada resumida do lead.'),
('19-landing-publica-desktop','Cliente final','Página da unidade (computador)','Modelo A para a GiO Curitiba Batel: formulário na primeira dobra, tratamentos, avaliações, como chegar e FAQ.'),
('20-landing-publica-mobile','Cliente final','Página da unidade (celular)','O mesmo modelo A em 390 px, com formulário logo após o título.')]
def thumb(n):
    im=Image.open(f'{D}/png/{n}.png').convert('RGB')
    w=360 if im.width>500 else 150
    h=int(im.height*w/im.width); im=im.resize((w,h),Image.LANCZOS)
    if h>420: im=im.crop((0,0,w,420))
    b=io.BytesIO(); im.save(b,'JPEG',quality=82); return base64.b64encode(b.getvalue()).decode()
linhas=''.join(f'''<tr><td class="n">{k+1:02d}</td><td class="th"><img src="data:image/jpeg;base64,{thumb(n)}"></td><td><div class="p">{p}</div><h3>{t}</h3><p>{d}</p><code>png/{n}.png</code></td></tr>''' for k,(n,p,t,d) in enumerate(T))
html=f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Gio · Sistema de unidades · telas</title><style>
@font-face{{font-family:Poppins;src:url(assets/fonts/Poppins-SemiBold.ttf);font-weight:600}}@font-face{{font-family:Inter;src:url(assets/fonts/Inter.ttf)}}
@page{{size:A4 landscape;margin:10mm}}*{{-webkit-print-color-adjust:exact;print-color-adjust:exact}}body{{font-family:Inter;margin:0;background:#f6f2f8;color:#1d1424}}.cap{{background:linear-gradient(120deg,#4c1455,#6f0052 55%,#b0197e);color:#fff;padding:40px 56px}}
.cap img{{height:46px}}.cap h1{{font:600 30px Poppins;margin:18px 0 6px}}.cap p{{color:#fff;opacity:.88;margin:0;max-width:820px;line-height:1.5}}
table{{width:100%;margin:20px 0;table-layout:fixed;border-collapse:separate;border-spacing:0 14px}}td{{background:#fff;vertical-align:top;padding:18px}}
td:first-child{{border-radius:16px 0 0 16px}}td:last-child{{border-radius:0 16px 16px 0}}tr{{page-break-inside:avoid}}
.n{{font:600 22px Poppins;color:#b0197e;width:46px}}.th{{width:320px}}.th img{{border-radius:10px;border:1px solid #ece4ef;display:block;max-width:320px;max-height:300px;object-fit:cover;object-position:top}}
.p{{display:inline-block;font-size:11px;font-weight:600;color:#4c1455;background:#f1e6f3;padding:3px 10px;border-radius:20px}}h3{{font:600 18px Poppins;margin:10px 0 6px}}p{{color:#5b5163;line-height:1.55;margin:0 0 10px}}code{{font-size:12px;color:#86106b}}
</style></head><body><div class="cap"><img src="assets/logo-gio-branco.png"><h1>Sistema de unidades · telas de proposta</h1><p>20 telas em alta fidelidade: versão da rede (Admin Gio, call center, agência), versão do franqueado (computador e celular) e a página pública da unidade. Dados fictícios. Nomes de unidades reais usados só como exemplo.</p></div>
<table>{linhas}</table></body></html>'''
open(f'{D}/galeria.html','w').write(html); print('galeria ok')
