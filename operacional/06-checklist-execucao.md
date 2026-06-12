# Checklist de Execução — Do Zero ao Lançamento
> Todas as ações necessárias, em ordem. Última atualização: 11/06/2026.

---

## FASE 1 — Estrutura de Captura (Semanas 1–2)

### 1.1 Instagram — corrigir urgente
- [ ] Remover link uaipet.com da bio
- [ ] Atualizar bio com o texto reformulado:
  ```
  Locutor | A voz da Rádio Itatiaia
  Ensino você a se comunicar melhor
  🎙️ Comunicação, Voz, Oratória
  👇 Material gratuito no link
  ```
- [ ] Parar de seguir novas contas aleatórias (congelar follow-for-follow)
- [ ] Adicionar link do lead magnet / lista de espera no link da bio

### 1.2 TikTok
- [ ] Adicionar link do Instagram/lead magnet na bio do TikTok
- [ ] Fixar comentário nos vídeos mais vistos: "Tenho um guia gratuito sobre isso — link na bio do Instagram"

### 1.3 Formulário e entrega do lead magnet
- [ ] Criar conta no Mailchimp ou Brevo (gratuito até 500–2.000 contatos)
- [ ] Conectar formulário da `06-pagina-lista-espera.html` ao Mailchimp/Brevo
  - No arquivo HTML: substituir o comentário `// TODO: integrar Mailchimp/Brevo` pela chamada de API real
- [ ] Configurar e-mail automático de entrega:
  - Assunto: "Aqui está o seu guia gratuito, [nome]"
  - Body: apresentação + link do PDF + teaser do que está por vir
  - Incluir link do PDF do lead magnet (fazer upload no Google Drive ou Brevo Assets)
- [ ] Gerar PDF do lead magnet a partir do arquivo `vendas/01-lead-magnet.md`
  - Usar a capa `assets/01-cover-lead-magnet.png`
  - Ferramenta: Canva, Adobe Express, ou converter o HTML em PDF

### 1.4 Publicar página de lista de espera
- [ ] Hospedar a `06-pagina-lista-espera.html` online (Netlify, Vercel, ou GitHub Pages — gratuito)
  - Instrução Netlify: arrastar a pasta `09-emmanuel-duarte-comunicacao/` na tela de deploy
  - Ou usar domínio próprio: ex. `comunicacao.locutoremmanuel.com.br`
- [ ] Copiar o link da página publicada e colocar como link da bio

---

## FASE 2 — Produto (Semanas 3–12)

### 2.1 Kiwify — configurar
- [ ] Criar conta em kiwify.com.br
- [ ] Criar produto: "Aprenda a se Comunicar — Emmanuel Duarte"
  - Tipo: Curso online
  - Preço: R$ 297 (lançamento) com parcelamento em 12x
  - Garantia: 7 dias
- [ ] Ativar Order Bump: "Masterclass 30 Dias de Exercícios de Voz — R$ 47"
  - Criar esse conteúdo: áudios de aquecimento vocal + plano de 30 dias em PDF
- [ ] Configurar Upsell: "Mentoria em Grupo 30 Dias — R$ 197"
- [ ] Copiar link do checkout e substituir em todas as páginas

### 2.2 Gravação do curso — ordem recomendada
- [ ] Módulo de Boas-vindas (10 min) ← gravar primeiro — abre a Turma Fundadora
- [ ] Módulo 1: A Base (3 aulas, ~35 min)
- [ ] Módulo 2: Voz e Corpo (5 aulas, ~55 min)
- [ ] Módulo 3: Falar em Público (4 aulas, ~45 min)
- [ ] Módulo 4: Reuniões e Apresentações (3 aulas, ~35 min)
- [ ] Módulo 5: Comunicação em Crise (3 aulas, ~35 min)
- [ ] Módulo 6: Negociação (3 aulas, ~30 min)
- [ ] Módulo 7: Produção — mini estúdio (2 aulas, ~25 min)
- [ ] Módulo 8: Treino de Voz (3 aulas + áudios, ~40 min)
- [ ] Módulo 9: Media Training (3 aulas, ~35 min)
- [ ] Módulo 10: Encerramento (1 aula, ~10 min)
- **Total estimado:** ~340 min (5h40) | 3–4 dias de gravação

### 2.3 Página de vendas completa
- [ ] Criar `pagina-de-vendas/index.html` usando a copy de `vendas/02-pagina-de-vendas.md`
- [ ] Adicionar foto profissional do Emmanuel (pasta `pagina-de-vendas/fotos/`)
- [ ] Substituir depoimentos placeholder por depoimentos reais
- [ ] Adicionar Meta Pixel (ID do pixel do Facebook)
- [ ] Publicar (Netlify — mesmo projeto ou subpágina)
- [ ] Substituir `[LINK DA PÁGINA DE LISTA DE ESPERA]` no lead magnet pelo link real

---

## FASE 3 — Lançamento (Semana do Lançamento)

### 3.1 Preparação (3 dias antes)
- [ ] Confirmar que checkout Kiwify está funcionando (fazer compra-teste)
- [ ] Confirmar que e-mail de boas-vindas chega corretamente
- [ ] Preparar 30+ DMs para enviar no Dia 1 (lista da espera + leads quentes)
- [ ] Exportar lista de e-mails do Mailchimp/Brevo

### 3.2 Sequência de lançamento (5 dias)
- [ ] Dia 0: stories de véspera (script em `marketing/03-stories-lancamento.md`)
- [ ] Dia 1: abertura + 30+ DMs manuais + post no feed
- [ ] Dia 2: stories quebra de objeção #1 + DMs de follow-up
- [ ] Dia 3: prova social + depoimento
- [ ] Dia 4: stories quebra de objeção #2
- [ ] Dia 5: urgência + contagem regressiva

### 3.3 Pós-lançamento (D+30)
- [ ] Agradecer alunos por DM individualmente
- [ ] Pedir feedback dos primeiros módulos
- [ ] Iniciar upsell de mentoria para alunos que concluíram módulos 1–3
- [ ] Avaliar métricas: taxa de conversão da lista → compra, ticket médio

---

## FASE 4 — Evergreen (Mês 3+)

- [ ] 3–5 posts/semana no TikTok (formato bullet points validado)
- [ ] 2 posts/semana no Instagram (carrossel + Reels)
- [ ] CTA para o lead magnet em todo conteúdo
- [ ] E-mail semanal para a lista (nurturing + novo conteúdo)
- [ ] Abrir vagas de mentoria individual (formulário de aplicação)
- [ ] Montar proposta de palestra corporativa (1 página PDF)
- [ ] Avaliar tráfego pago (Meta Ads) com R$ 500–1.000 de teste

---

## Indicadores para Acompanhar

| Métrica | Meta Fase 1 | Meta Fase 2 | Meta Fase 3 |
|---------|-------------|-------------|-------------|
| E-mails na lista | 100–300 | 300–1.000 | 1.000+ |
| Taxa abertura e-mail | > 30% | > 25% | > 20% |
| Seguidores TikTok | +500/mês | +1.000/mês | +3.000/mês |
| Seguidores Instagram | Crescimento orgânico | +200/mês | +500/mês |
| Vendas do curso | – | 10–50 (beta) | 50–200/mês |
| Clientes mentoria | – | 2–5 | 5–10 |
