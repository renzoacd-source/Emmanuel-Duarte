# Projeto Emmanuel Duarte — Contexto Completo para Claude Chat

> Use este documento como Project Knowledge no Claude.ai para consultas rápidas sobre o projeto.

---

## Quem é o cliente

| Campo | Detalhe |
|-------|---------|
| Nome | Emmanuel Duarte |
| Credencial âncora | A voz da Rádio Itatiaia (BH) |
| Produto | Curso online "Aprenda a se Comunicar" |
| Instagram | @emmanuel_duarte.duarte |
| TikTok | @locutorduarte (24% engajamento) |
| Site pessoal | locutoremmanuel.com.br |

---

## Links do projeto

| Recurso | URL |
|---------|-----|
| **Página de lista de espera (ao vivo)** | https://aprendaasecomunicar.netlify.app/06-pagina-lista-espera.html |
| **Repositório GitHub** | https://github.com/renzoacd-source/Emmanuel-Duarte |
| **Planilha de leads (Google Sheets)** | https://docs.google.com/spreadsheets/d/1GztQ-YyfXwOmesEJz15AXXA2vU-lc9E32fK6wVK1-tw/edit |
| **Apps Script (backend do formulário)** | https://script.google.com/macros/s/AKfycbw6MiVLoBXSiAPzBBG48mIqZba_2JASjcIEuPYJaTl057mRKedRrthb2XSWNLBeAi241A/exec |

---

## Estrutura de pastas — todos os arquivos

```
09-emmanuel-duarte-comunicacao/
│
├── 06-pagina-lista-espera.html       ← PÁGINA PRINCIPAL (lista de espera ao vivo)
├── index.html                         ← Redireciona para 06-pagina-lista-espera.html
├── CLAUDE.md                          ← Contexto mestre do projeto (completo)
├── README.md                          ← Status e estrutura do projeto
├── PROJETO-CONTEXT.md                 ← Este arquivo
│
├── estrategia/
│   ├── 00-estrategia-geral.md         ← Funil completo, 3 fases, bio reformulada
│   └── perfil-voz-emmanuel-duarte.md  ← Tom, voz, o que NÃO é, frases marcantes
│
├── marketing/
│   ├── 01-conteudo-instagram.md       ← 4 semanas de calendário + scripts
│   ├── 02-conteudo-tiktok.md          ← 6 roteiros prontos [0-3s / 4-50s / 51-60s]
│   ├── 03-stories-lancamento.md       ← Scripts Dia 0 ao Dia 5 (horários inclusos)
│   └── 04-dm-followup.md              ← 5 fluxos de DM + 9 objeções respondidas
│
├── vendas/
│   ├── 01-lead-magnet.md              ← Resumo do guia gratuito (5 erros)
│   ├── 02-pagina-de-vendas.md         ← Copy completa do curso (H1, módulos, FAQ)
│   └── 05-upsell-mentoria.md          ← Oferta mentoria + scripts de fechamento
│
├── operacional/
│   ├── 06-checklist-execucao.md       ← Checklist das 4 fases do projeto
│   ├── COMO-IR-AO-AR-HOJE.md          ← Guia de 3h: Netlify + Brevo + Instagram
│   └── apps-script-sheets.gs          ← Código do Google Apps Script (backend leads)
│
├── roteiros-curso/
│   ├── modulo-1-base-comunicacao.md   ← Aulas 0.1, 1.1, 1.2, 1.3 (roteiros completos)
│   └── modulos-2-a-10.md              ← Outline de todos os módulos
│
├── assets/
│   ├── 01-cover-lead-magnet.png       ← Capa do guia gratuito (800x1130px)
│   ├── 02-hero-banner.png             ← Banner hero da landing page
│   ├── design-philosophy.md           ← Filosofia visual "Voz Negra"
│   └── gerar-imagens.py               ← Script Python para gerar assets
│
├── pagina-de-vendas/
│   └── fotos/
│       ├── hero.jpg                   ← Emmanuel frente/gesto (hero + CTA final)
│       ├── studio.jpg                 ← Perfil no console Itatiaia (seção "Quem ensina")
│       ├── console.jpg                ← Close dramático (seção "Por que aprender")
│       └── palco.jpg                  ← Emmanuel em palco (seção quote)
│
└── .claude/
    ├── launch.json                    ← Servidor local porta 3091
    └── skills/
        ├── SKILLS-INDEX.md
        ├── marketing-emmanuel/SKILL.md
        ├── copywriter-comunicacao/SKILL.md
        ├── estrategista-conteudo/SKILL.md
        └── pesquisa-mercado/SKILL.md
```

---

## A oferta (preços)

| Produto | Preço |
|---------|-------|
| Curso — preço de lançamento | R$ 297 |
| Curso — preço normal (pós-lançamento) | R$ 497 |
| Order Bump (bônus complementar) | R$ 47 |
| Upsell — Mentoria em grupo | R$ 197 |
| Mentoria individual (sessão única) | R$ 500 |
| Mentoria individual (pacote 4 sessões) | R$ 1.500 |

---

## Status atual dos entregáveis

| Entregável | Status |
|-----------|--------|
| Análise de perfis (Instagram + TikTok) | ✅ Pronto |
| Estratégia e posicionamento | ✅ Pronto |
| Lead magnet — conteúdo | ✅ Pronto |
| Capa do lead magnet (PNG) | ✅ Pronto |
| Hero banner (PNG) | ✅ Pronto |
| Página de lista de espera | ✅ **AO VIVO** |
| Fotos profissionais integradas | ✅ Pronto (4 fotos) |
| Formulário → Google Sheets | ✅ Funcionando |
| 6 roteiros de TikTok | ✅ Pronto |
| Roteiros do curso — Módulo 1 | ✅ Pronto |
| Outline módulos 2–10 | ✅ Pronto |
| Copy da página de vendas | ✅ Pronto (md) |
| PDF do lead magnet | ❌ Pendente |
| Página de vendas (HTML) | ❌ Pendente |
| Integração de e-mail (Brevo) | ❌ Pendente |
| Configuração Kiwify | ❌ Pendente |

---

## O funil completo

```
TikTok / Instagram
       ↓
  Link na bio
       ↓
Página de lista de espera (ao vivo)
       ↓
Lead capturado → Google Sheets
       ↓
[FUTURO] E-mail automático + PDF lead magnet
       ↓
[FUTURO] Página de vendas → Kiwify
       ↓
Curso R$297 + Order Bump R$47
       ↓
Upsell Mentoria em grupo R$197
```

---

## Tom de voz — regras

**USE:**
- Frases curtas, diretas
- "você" (informal)
- Situações reais do cotidiano profissional
- Técnicas com nomes simples (não jargão)
- "Comunicação não é dom — é técnica"

**NÃO USE:**
- Coach-speak ("potencial", "jornada", "transformação")
- Promessas milagrosas
- Linguagem de "alta performance"
- Frases longas e complexas

---

## Projeção financeira — 1ª turma

| Cenário | Vendas | Receita estimada |
|---------|--------|-----------------|
| Pessimista | 10 alunos | ~R$ 3.200 |
| Realista | 25 alunos | ~R$ 7.900 |
| Otimista | 50 alunos | ~R$ 15.800 |

*(incluindo order bump 40% + upsell mentoria 20%)*

---

## Próximos passos prioritários

1. **PDF do lead magnet** — gerar a partir de `05-lead-magnet.md` + capa
2. **Integração Brevo** — e-mail automático entregando o PDF ao lead
3. **Bio do Instagram** — atualizar com link da landing page
4. **Página de vendas HTML** — converter `vendas/02-pagina-de-vendas.md`
5. **Configurar Kiwify** — cadastrar o curso e conectar checkout
