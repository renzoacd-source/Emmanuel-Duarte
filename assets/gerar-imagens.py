"""
Gerador de assets visuais — Emmanuel Duarte
Filosofia: Voz Negra — minimalismo premium, preto/branco/dourado

Gera:
  01-cover-lead-magnet.png   — capa do PDF "5 Erros"     (800 x 1130 px)
  02-hero-banner.png         — hero da landing page        (1200 x 630 px)
"""

from PIL import Image, ImageDraw, ImageFont
import math, os, sys

OUT = os.path.dirname(os.path.abspath(__file__))

# ── Paleta ──────────────────────────────────────────────────────────────────
BLACK   = (10, 10, 10)
WHITE   = (255, 255, 255)
GOLD    = (196, 160, 72)
GOLD_DIM = (120, 96, 42)
GRAY    = (60, 60, 60)
GRAY_LT = (130, 130, 130)

# ── Fontes ──────────────────────────────────────────────────────────────────
def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/GeorgiaBold.ttf"   if bold else "C:/Windows/Fonts/Georgia.ttf",
        "C:/Windows/Fonts/timesbd.ttf"        if bold else "C:/Windows/Fonts/times.ttf",
        "C:/Windows/Fonts/arialbd.ttf"        if bold else "C:/Windows/Fonts/arial.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def font_mono(size):
    candidates = [
        "C:/Windows/Fonts/cour.ttf",
        "C:/Windows/Fonts/consola.ttf",
        "C:/Windows/Fonts/lucon.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def font_sans(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
    ]
    for p in candidates:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

# ── Helpers ──────────────────────────────────────────────────────────────────
def center_text(draw, text, y, fnt, color, canvas_w):
    bbox = draw.textbbox((0, 0), text, font=fnt)
    w = bbox[2] - bbox[0]
    draw.text(((canvas_w - w) / 2, y), text, font=fnt, fill=color)

def draw_waveform(draw, cx, cy, w, h, color, alpha_steps=12, line_w=1):
    """Desenha uma onda senoidal estilizada como acento gráfico."""
    pts = []
    steps = 200
    for i in range(steps + 1):
        t = i / steps
        x = cx - w/2 + t * w
        amp = h/2 * math.sin(t * math.pi)           # envelope gaussiano suave
        y = cy + amp * math.sin(t * 2 * math.pi * 6)
        pts.append((x, y))
    for i in range(len(pts) - 1):
        draw.line([pts[i], pts[i+1]], fill=color, width=line_w)

def draw_fine_lines(draw, x0, y0, x1, y1, n, color, width=1):
    """Linhas horizontais finas — evocam espectro de frequência."""
    for i in range(n):
        t = i / (n - 1)
        y = y0 + t * (y1 - y0)
        alpha = int(80 + 80 * math.sin(t * math.pi))
        c = (*color[:3], alpha) if len(color) == 4 else color
        draw.line([(x0, y), (x1, y)], fill=c, width=width)

def draw_rule(draw, x0, x1, y, color, width=1):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)

def wrap_text(text, fnt, max_w, draw):
    words = text.split()
    lines, line = [], []
    for w in words:
        test = " ".join(line + [w])
        bbox = draw.textbbox((0, 0), test, font=fnt)
        if bbox[2] - bbox[0] <= max_w:
            line.append(w)
        else:
            if line:
                lines.append(" ".join(line))
            line = [w]
    if line:
        lines.append(" ".join(line))
    return lines


# ═══════════════════════════════════════════════════════════════════════════
# IMAGEM 1 — CAPA DO LEAD MAGNET  (800 × 1130)
# ═══════════════════════════════════════════════════════════════════════════
def make_cover():
    W, H = 800, 1130
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img, "RGBA")

    M = 56   # margem base

    # ── fundo: linhas de frequência sutis no terço inferior ──────────────
    for i in range(60):
        t = i / 59
        y = int(H * 0.52 + t * H * 0.38)
        alpha = int(25 + 30 * math.sin(t * math.pi))
        d.line([(M, y), (W - M, y)], fill=(*GRAY[:3], alpha), width=1)

    # ── régua dourada no topo ─────────────────────────────────────────────
    draw_rule(d, M, W - M, 72, GOLD, width=2)

    # ── label superior ────────────────────────────────────────────────────
    lbl_fnt = font_sans(13)
    lbl = "MATERIAL GRATUITO  ·  EMMANUEL DUARTE"
    center_text(d, lbl, 84, lbl_fnt, GRAY_LT, W)

    # ── número grande como elemento gráfico ──────────────────────────────
    num_fnt = font(320, bold=True)
    d.text((M - 18, 90), "5", font=num_fnt, fill=(25, 25, 25))

    # ── título principal ──────────────────────────────────────────────────
    t1_fnt = font(62, bold=True)
    t2_fnt = font(62, bold=False)

    title_lines = [
        ("ERROS QUE",   t1_fnt, WHITE),
        ("DESTROEM",    t1_fnt, WHITE),
        ("SUA",         t2_fnt, GOLD),
        ("CREDIBILIDADE", t2_fnt, GOLD),
        ("AO FALAR",    t1_fnt, WHITE),
    ]
    y_cursor = 168
    line_gap = 70
    for text, fnt, color in title_lines:
        center_text(d, text, y_cursor, fnt, color, W)
        y_cursor += line_gap

    # ── subtítulo ─────────────────────────────────────────────────────────
    sub_fnt = font_sans(18)
    sub = "e como corrigir cada um deles"
    center_text(d, sub, y_cursor + 10, sub_fnt, GRAY_LT, W)
    y_cursor += 44

    # ── régua divisória central ───────────────────────────────────────────
    draw_rule(d, M * 2, W - M * 2, y_cursor + 28, GOLD_DIM, width=1)

    # ── waveform central ─────────────────────────────────────────────────
    wave_y = y_cursor + 90
    draw_waveform(d, W // 2, wave_y, W - M * 3, 48, GOLD, line_w=2)

    # ── linhas de espectro abaixo da onda ────────────────────────────────
    spec_top = wave_y + 80
    draw_fine_lines(d, M, spec_top, W - M, spec_top + 120, 20, GRAY_LT)

    # ── bloco autor ───────────────────────────────────────────────────────
    author_y = H - 220
    draw_rule(d, M, W - M, author_y, GRAY, width=1)

    name_fnt = font_sans(22, bold=True)
    cred_fnt = font_sans(14)

    center_text(d, "EMMANUEL DUARTE", author_y + 22, name_fnt, WHITE, W)
    center_text(d, "Locutor  ·  A voz da Rádio Itatiaia  ·  Especialista em Comunicação",
                author_y + 56, cred_fnt, GOLD_DIM, W)

    # ── régua dourada no rodapé ───────────────────────────────────────────
    draw_rule(d, M, W - M, H - 58, GOLD, width=2)

    site_fnt = font_mono(12)
    center_text(d, "www.locutoremmanuel.com.br", H - 42, site_fnt, GRAY_LT, W)

    # ── marca d'água numérica discreta ────────────────────────────────────
    wm_fnt = font(420, bold=True)
    d.text((W - 290, H - 520), "5", font=wm_fnt, fill=(18, 18, 18))

    out_path = os.path.join(OUT, "01-cover-lead-magnet.png")
    img.save(out_path, "PNG", dpi=(150, 150))
    print(f"  OK  {out_path}")
    return img


# ═══════════════════════════════════════════════════════════════════════════
# IMAGEM 2 — HERO BANNER  (1200 × 630)
# ═══════════════════════════════════════════════════════════════════════════
def make_hero():
    W, H = 1200, 630
    img = Image.new("RGB", (W, H), BLACK)
    d = ImageDraw.Draw(img, "RGBA")

    M = 70

    # ── grade de linhas verticais sutis (à direita) ───────────────────────
    grid_x0 = W // 2 + 40
    n_grid = 22
    for i in range(n_grid):
        t = i / (n_grid - 1)
        x = int(grid_x0 + t * (W - M - grid_x0))
        alpha = int(15 + 25 * (1 - t))
        d.line([(x, M), (x, H - M)], fill=(*GRAY[:3], alpha), width=1)

    # ── linhas horizontais finas (esquerda) ───────────────────────────────
    draw_fine_lines(d, M, H * 0.62, W // 2 - 20, H - M - 10, 18, GRAY)

    # ── régua dourada esquerda vertical ──────────────────────────────────
    d.line([(M, M + 10), (M, H - M - 10)], fill=GOLD, width=3)

    # ── label badge ───────────────────────────────────────────────────────
    badge_fnt = font_sans(13)
    badge_txt = "EM BREVE  ·  LISTA DE ESPERA ABERTA"
    bx, by = M + 22, M + 10
    bbox = d.textbbox((bx, by), badge_txt, font=badge_fnt)
    pad = 10
    d.rectangle([bbox[0]-pad, bbox[1]-6, bbox[2]+pad, bbox[3]+6],
                fill=(0, 0, 0, 0), outline=GOLD_DIM, width=1)
    d.text((bx, by), badge_txt, font=badge_fnt, fill=GOLD_DIM)

    # ── headline principal ────────────────────────────────────────────────
    h1_fnt = font(100, bold=True)
    h2_fnt = font(100, bold=False)

    line1 = "Aprenda a"
    line2 = "se Comunicar"

    y1 = by + 56
    d.text((M + 22, y1), line1, font=h1_fnt, fill=WHITE)
    y2 = y1 + 108
    d.text((M + 22, y2), line2, font=h2_fnt, fill=GOLD)

    # ── tagline ───────────────────────────────────────────────────────────
    tag_fnt = font_sans(17)
    tag = "Comunicação clara, autêntica e de impacto."
    d.text((M + 24, y2 + 116), tag, font=tag_fnt, fill=GRAY_LT)

    # ── waveform decorativo (à direita) ───────────────────────────────────
    draw_waveform(d, W * 0.78, H * 0.42, 340, 120, GOLD, line_w=2)

    # segundo waveform mais suave
    draw_waveform(d, W * 0.78, H * 0.42 + 28, 280, 60, GOLD_DIM, line_w=1)

    # ── régua dourada inferior ────────────────────────────────────────────
    draw_rule(d, M, W - M, H - 72, GOLD, width=1)

    # ── autor no rodapé ───────────────────────────────────────────────────
    aut_fnt = font_sans(15, bold=True)
    crd_fnt = font_sans(13)
    d.text((M + 24, H - 58), "EMMANUEL DUARTE", font=aut_fnt, fill=WHITE)
    d.text((M + 24, H - 38), "Locutor · A voz da Rádio Itatiaia", font=crd_fnt, fill=GOLD_DIM)

    # ── site à direita do rodapé ──────────────────────────────────────────
    site_fnt = font_mono(12)
    site = "locutoremmanuel.com.br"
    bbox = d.textbbox((0, 0), site, font=site_fnt)
    sw = bbox[2] - bbox[0]
    d.text((W - M - sw, H - 46), site, font=site_fnt, fill=GRAY_LT)

    out_path = os.path.join(OUT, "02-hero-banner.png")
    img.save(out_path, "PNG", dpi=(150, 150))
    print(f"  OK  {out_path}")
    return img


# ═══════════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("\nGerando assets - Voz Negra - Emmanuel Duarte\n")
    make_cover()
    make_hero()
    print("\nPronto. Arquivos salvos em:", OUT)
