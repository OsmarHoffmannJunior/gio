// Versão advanced mode de functions/_middleware.js, usada no envio direto pela API do Cloudflare Pages.
// Basic Auth da demonstração (Cloudflare Pages Functions).
// Usuário "gio"; a senha vem do secret GIO_DEMO_SENHA do projeto (nunca no código).
// Sem secret configurado, nega tudo (falha fechada). X-Robots-Tag noindex em todas as respostas.
const USUARIO = "gio";
const NOINDEX = "noindex, nofollow, noarchive";

function igual(a, b) {
  const ea = new TextEncoder().encode(a), eb = new TextEncoder().encode(b);
  let d = ea.length ^ eb.length;
  for (let i = 0; i < Math.max(ea.length, eb.length); i++) d |= (ea[i] || 0) ^ (eb[i] || 0);
  return d === 0;
}

function negar(status, texto) {
  const h = new Headers({ "Content-Type": "text/plain; charset=utf-8", "X-Robots-Tag": NOINDEX, "Cache-Control": "no-store" });
  if (status === 401) h.set("WWW-Authenticate", 'Basic realm="Demonstracao Gio", charset="UTF-8"');
  return new Response(texto, { status, headers: h });
}

async function protege(request, env, proximo) {
  if (new URL(request.url).pathname === "/robots.txt") {
    return new Response("User-agent: *\nDisallow: /\n", { headers: { "Content-Type": "text/plain; charset=utf-8", "X-Robots-Tag": NOINDEX } });
  }
  const senha = env.GIO_DEMO_SENHA;
  if (!senha) return negar(503, "Ambiente indisponível: proteção ainda não configurada.");
  const auth = request.headers.get("Authorization") || "";
  let ok = false;
  if (auth.startsWith("Basic ")) {
    try {
      const dec = atob(auth.slice(6));
      const i = dec.indexOf(":");
      ok = i > 0 && igual(dec.slice(0, i), USUARIO) && igual(dec.slice(i + 1), senha);
    } catch (e) { ok = false; }
  }
  if (!ok) return negar(401, "Acesso restrito ao ambiente de demonstração.");
  const r = await proximo();
  const resp = new Response(r.body, r);
  resp.headers.set("X-Robots-Tag", NOINDEX);
  resp.headers.set("Cache-Control", "private, no-store");
  return resp;
}


export default { fetch: (request, env) => protege(request, env, () => env.ASSETS.fetch(request)) };
