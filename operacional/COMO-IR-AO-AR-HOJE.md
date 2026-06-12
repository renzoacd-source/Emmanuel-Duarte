# Como Ir ao Ar HOJE e Começar a Capturar Leads
## Guia de Execução em 3 Horas

---

## SITUAÇÃO ATUAL

O lead magnet está pronto. A página de lista de espera está pronta.
O que ainda não está no ar: o formulário integrado e a página publicada online.

**Estratégia: Turma Fundadora**

Você pode começar a vender o curso antes de gravar uma aula.
Como fazem todos os grandes lançamentos de infoprodutos:
- Vende com preço de fundador (R$ 247 — mais baixo que o lançamento)
- Define prazo de entrega: "acesso aos módulos liberados semana a semana"
- Grava e publica módulo a módulo enquanto a turma está dentro
- Usa a lista de espera já construída para a primeira oferta

**Por que funciona:**
- Você valida se as pessoas realmente pagam antes de gravar
- Os primeiros alunos moldam o conteúdo com as dúvidas deles
- Cria urgência real ("esse preço existe só porque estou construindo junto com você")

---

## HORA 1 — PUBLICAR A PÁGINA DE LISTA DE ESPERA (30–40 min)

### Opção A — Netlify (recomendado, gratuito)
1. Acesse netlify.com → criar conta gratuita
2. Clique em "Add new site" → "Deploy manually"
3. Arraste a pasta `09-emmanuel-duarte-comunicacao/` na tela do Netlify
4. Em segundos: site publicado em URL `https://NOME-ALEATORIO.netlify.app`
5. Opcional: ir em "Domain settings" para configurar um subdomínio próprio
   Ex: `comunicacao.locutoremmanuel.com.br`

**A página de lista de espera já está em:** `06-pagina-lista-espera.html`
**Acessível em:** `https://SEU-SITE.netlify.app/06-pagina-lista-espera`

---

## HORA 1B — INTEGRAR O FORMULÁRIO COM BREVO (gratuito)

### Passo 1: Criar conta no Brevo
1. Acesse brevo.com → "Sign up free"
2. Confirmar e-mail

### Passo 2: Criar a lista de contatos
1. Em "Contacts" → "Lists" → "Create a list"
2. Nome: "Lista de Espera — Aprenda a se Comunicar"

### Passo 3: Configurar o formulário
1. Em "Contacts" → "Forms" → "Create a new form"
2. Campos: Nome + E-mail
3. Após submissão: redirecionar para página de agradecimento OU mostrar mensagem

### Passo 4: Conectar no HTML
No arquivo `06-pagina-lista-espera.html`, localizar o comentário `// TODO: integrar Mailchimp/Brevo` e substituir pela chamada da API do Brevo.

*(Claude pode fazer isso — é uma substituição simples no JS da página)*

### Passo 5: Criar e-mail automático de entrega
1. Em "Automations" → "Create a workflow"
2. Trigger: "Contact subscribes to a list"
3. Ação: enviar e-mail com o guia gratuito em anexo ou link
4. **Assunto:** "Aqui está o seu guia, [nome] — 5 Erros que Destroem Sua Credibilidade"
5. **Body:**
   > "Oi [nome]!
   > Obrigado por se inscrever.
   > Aqui está o guia: [LINK DO PDF]
   >
   > Nos próximos dias vou te enviar mais conteúdo e, quando o curso abrir, você será o primeiro a saber.
   >
   > Qualquer dúvida, me chama no Instagram: @emmanuel_duarte.duarte
   >
   > — Emmanuel"

---

## HORA 2 — INSTAGRAM: LINK NA BIO + STORIES (30 min)

### Atualizar bio (copiar e colar)
```
Locutor | A voz da Rádio Itatiaia
Ensino você a se comunicar melhor
🎙️ Comunicação, Voz, Oratória
👇 Material gratuito no link
```

### Linktree / link único (criar em linktr.ee — gratuito)
Adicionar nesta ordem:
1. "Guia gratuito: 5 Erros que Destroem Sua Credibilidade" → link da `06-pagina-lista-espera.html`
2. "Lista de espera — Aprenda a se Comunicar" → mesma página ou seção da lista
3. "Locução profissional" → locutoremmanuel.com.br

### Primeiro story de captura (gravar agora — 30s)
> "Pessoal, acabei de colocar no ar um material gratuito que eu levei semanas organizando.
> É um guia com os 5 erros que destroem a credibilidade de qualquer pessoa ao falar — e como corrigir cada um.
> Completamente gratuito. Você recebe direto no e-mail.
> Link na bio."

---

## HORA 3 — TIKTOK: COMENTÁRIO FIXADO + VÍDEO (30 min)

### Nos 5 vídeos mais vistos do TikTok:
Fixar comentário:
> "Tenho um guia gratuito sobre isso — link na bio do Instagram"

### Gravar um TikTok de captura (60s — roteiro sugerido)
```
[0–5s] "Fiz um material gratuito que vou deixar no link da bio."
[6–25s] "São os 5 erros que destroem a credibilidade de qualquer pessoa ao falar.
Não é teoria — é o que eu vejo repetindo nas reuniões, apresentações e entrevistas que analiso."
[26–45s] "O primeiro erro? Pedir desculpa antes de começar.
'Bom, desculpa, não sou o especialista aqui...' — você acabou de me dizer para não te levar a sério.
E eu ainda vou te mostrar os outros 4."
[46–60s] "O guia é gratuito. Você recebe no e-mail. Link na bio do Instagram."
```

---

## CHECKLIST "AO AR HOJE"

- [ ] Página de lista de espera publicada online
- [ ] Formulário integrado com Brevo/Mailchimp
- [ ] E-mail automático de entrega do guia configurado
- [ ] PDF do guia disponível online (Google Drive ou Brevo Assets)
- [ ] Bio do Instagram atualizada
- [ ] Link da bio apontando para a página de lista de espera
- [ ] Story de lançamento do material gratuito postado
- [ ] Comentários fixados nos 5 vídeos do TikTok
- [ ] TikTok de captura gravado e publicado

**Tempo total estimado: 2 a 3 horas**

---

## EXPECTATIVA PARA OS PRIMEIROS 7 DIAS

Com audiência atual (TikTok principal, Instagram secundário):
- 20 a 100 e-mails capturados na primeira semana é resultado real e bom
- 100 e-mails = 100 pessoas que pediram para saber quando o curso abre
- Com taxa de conversão de 5–10%, isso já representa 5–10 vendas no lançamento

**O que fazer com o primeiro e-mail capturado:**
1. Mandar uma DM pessoal no Instagram: "Oi! Vi que você baixou o guia. O que achou até agora?"
2. Usar a resposta para entender melhor o público
3. Esse feedback molda os próximos conteúdos e os scripts do curso

---

## PRÓXIMOS PASSOS APÓS CAPTURAR OS PRIMEIROS 100 E-MAILS

1. Gravar o módulo de boas-vindas (10 min) — esse já é suficiente para abrir o checkout
2. Configurar Kiwify com o produto, order bump e upsell
3. Anunciar a abertura da Turma Fundadora para a lista de espera
4. Executar sequência de lançamento (scripts em `marketing/03-stories-lancamento.md`)
5. Gravar os módulos restantes enquanto a turma está dentro
