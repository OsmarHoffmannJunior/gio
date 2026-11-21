# Sistema de unidades Gio

Protótipo e especificações do sistema de unidades da Gio Estética Avançada (rede Salus). O material cobre o portal da rede, o portal do franqueado, a área do cliente, quiz, inteligência de demanda e tracking.

Este repositório é interno. Não publique o conteúdo nem compartilhe o endereço do protótipo fora do grupo de trabalho.

## Estrutura

- `.specify/`: constituição do projeto e ferramentas do Spec Kit (memória, templates e fluxos).
- `specs/001-sistema-unidades/`: especificação do sistema de unidades (rede e franqueado), modelo de dados, permissões, política de campos e inventário de telas.
- `specs/002-area-cliente/`: especificação da área do cliente, decisões e impacto na 001.
- `specs/003-quiz-inteligencia-tracking/`: quiz, inteligência de demanda e tracking, com decisões e impacto nas specs anteriores.
- `telas/`: HTML e CSS navegáveis das telas (79 telas nesta versão).
- `png/`: capturas oficiais das telas.
- `galeria.html` e `galeria.pdf`: galeria das telas para revisão.
- `assets/`: logos, fotos e fontes usadas nas telas e no protótipo.
- `gerador/`: scripts em Python que geram as telas, a galeria, o protótipo e as checagens de layout.
- `prototipo/`: site estático do protótipo, pronto para o Cloudflare Pages.
- `deploy-pages/`: worker e função de proteção do protótipo (Basic Auth e `noindex`).
- `arquivo-rodada1/`: telas e capturas da primeira rodada, só como histórico.
- `PROGRESSO.md`: diário do que já foi feito.

## Como regenerar as telas e o protótipo

Os geradores rodam com Python 3, a partir da pasta `gerador/`. A renderização das capturas pede Playwright.

```bash
cd gerador
for p in s1 s2 s3 s4 s5 s6 s7 s8 s9 s10; do python3 $p.py; done
python3 render.py
python3 render.py
python3 galeria.py
python3 prototipo.py
python3 verifica_prototipo.py
```

O `render.py` roda duas vezes de propósito: algumas telas usam capturas geradas na primeira passagem. A checagem automática de layout e de formulários fica em `checa_layout.py` e grava saídas locais que não entram neste repositório.

## Protótipo publicado

O protótipo fica no Cloudflare Pages, com autenticação Basic Auth (usuário `gio`). A senha não fica neste repositório: o worker em `deploy-pages/` lê o secret `GIO_DEMO_SENHA` do ambiente. Sem o secret, o acesso é negado. Todas as respostas levam `X-Robots-Tag: noindex`.

Para ver o protótipo no computador, sem a proteção do worker:

```bash
cd prototipo
python3 -m http.server 8080
```

Abra http://localhost:8080.
