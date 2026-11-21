/* Protótipo navegável (demonstração). Comportamentos locais, nada é enviado a servidor algum. */
(function(){
var B=document.body, perfil=B.dataset.perfil||'', par=B.dataset.parMobile;
var fixo=location.search.indexOf('fixo')>=0;
if(par && !fixo && window.innerWidth<700){location.replace(par+location.search+location.hash);return;}
var pard=B.dataset.parDesktop; if(pard && !fixo && window.innerWidth>=700){location.replace(pard+location.search+location.hash);return;}
function toast(t){var e=document.querySelector('.ptoast');if(!e){e=document.createElement('div');e.className='ptoast';document.body.appendChild(e);}e.textContent=t;e.classList.add('on');clearTimeout(e._t);e._t=setTimeout(function(){e.classList.remove('on')},2200);}
var cli=(window.innerWidth>=1100)?'52-cliente-inicio-desktop.html':'46-cliente-mobile-inicio.html';
var bar=document.createElement('div');bar.className='pbar';
bar.innerHTML='<button class="pmenu" type="button">Menu</button><span class="ps">● <span>Ambiente de demonstração · dados fictícios</span></span>'+
 '<nav><a data-p="rede" href="04-admin-dashboard-rede.html">Rede</a><a data-p="franqueado" href="24-franqueado-dashboard.html">Franqueado</a><a data-p="cliente" href="'+cli+'">Cliente</a><a data-p="todas" href="../index.html">Todas as telas</a></nav>';
B.insertBefore(bar,B.firstChild);
if(B.classList.contains('p-mob')){ // fundo contínuo: a cor da tela de celular ocupa toda a largura
 var alvo=document.querySelector('.mob'); var cor=alvo?getComputedStyle(alvo).backgroundColor:'#ffffff'; if(cor==='rgba(0, 0, 0, 0)')cor='#ffffff';
 B.style.background=cor; document.documentElement.style.background=cor;
}

bar.querySelectorAll('nav a').forEach(function(a){if(a.dataset.p===perfil)a.classList.add('on');a.addEventListener('click',function(){try{localStorage.setItem('perfil-demo',a.dataset.p)}catch(e){}});});
var mb=bar.querySelector('.pmenu'),sd=document.querySelector('.side');if(document.querySelector('.top .menu-btn')){mb.style.display='none';sd=null;mb.remove();}else if(sd){mb.addEventListener('click',function(){sd.classList.toggle('aberta')});}else{mb.style.display='none';}
document.addEventListener('click',function(ev){
 var t=ev.target.closest('[data-toggle],.cx,.tabs a,.sw span,.btn,a,[data-confirma]');if(!t)return;
 if(t.closest('[data-acao-propria]'))return;
 if(t.matches('.cx')){t.classList.toggle('on');libera();return;}
 if(t.matches('[data-libera]')){if(t.classList.contains('off')){ev.preventDefault();toast('Marque os itens obrigatórios para continuar.');}return;}
 if(t.matches('[data-confirma]')){ev.preventDefault();if(confirm(t.dataset.confirma))toast('Simulado: nada foi apagado no protótipo.');return;}
 if(t.matches('[data-toggle]')){if(t.dataset.toggle==='0')return;ev.preventDefault();t.classList.toggle('on');return;}
 if(t.matches('.sw span')){t.parentNode.querySelectorAll('span').forEach(function(x){x.classList.remove('on')});t.classList.add('on');return;}
 var h=t.getAttribute('href');
 if(t.matches('.tabs a') && (!h||h==='#')){ev.preventDefault();t.parentNode.querySelectorAll('a').forEach(function(x){x.classList.remove('on')});t.classList.add('on');toast('Aba ilustrativa: o conteúdo desta aba não foi desenhado nesta rodada.');return;}
 if(t.tagName==='A' && h && h.charAt(0)==='#' && h.length>1 && document.querySelector(h))return;
 if((t.tagName!=='A'||!h||h.charAt(0)==='#') && (t.matches('.btn,[data-sem-rota]')||t.tagName==='A')){ev.preventDefault();toast('Ação simulada no protótipo: nada é enviado ou gravado.');}
});
function libera(){document.querySelectorAll('[data-libera]').forEach(function(b){var ok=Array.prototype.every.call(document.querySelectorAll('[data-obrig]'),function(c){return c.classList.contains('on')});
 if(ok){b.classList.remove('off');b.classList.add('p');b.setAttribute('href',b.dataset.href);}else{b.classList.add('off');b.classList.remove('p');b.removeAttribute('href');}});}
})();
