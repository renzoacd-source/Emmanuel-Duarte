"""
Gerador da capa do lead magnet - tema "NO AR" (broadcast editorial)
Paleta: preto-quase / branco / vermelho-sinal. Tipografia grotesca em caixa-alta.
Gera: 01-cover-lead-magnet.png (800 x 1130)
"""

from PIL import Image, ImageDraw, ImageFont
import math, os

OUT = os.path.dirname(os.path.abspath(__file__))

# ── Paleta NO AR ──────────────────────────────────────────────
INK      = (10, 10, 11)
WHITE    = (244, 244, 242)
RED      = (255, 68, 56)
RED_DEEP = (170, 40, 30)
GRAY     = (52, 52, 58)
GRAY_LT  = (150, 150, 158)
FAINT    = (22, 22, 24)

def font_sans(size, bold=True):
    cands = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "C:/Windows/Fonts/calibrib.ttf" if bold else "C:/Windows/Fonts/calibri.ttf",
        "C:/Windows/Fonts/segoeui.ttf",
    ]
    for p in cands:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def font_mono(size):
    for p in ["C:/Windows/Fonts/consola.ttf", "C:/Windows/Fonts/cour.ttf", "C:/Windows/Fonts/lucon.ttf"]:
        if os.path.exists(p):
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def center(d, text, y, fnt, color, W, tracking=0):
    if tracking:
        # render com espaçamento entre letras
        widths = [d.textbbox((0, 0), c, font=fnt)[2] for c in text]
        total = sum(widths) + tracking * (len(text) - 1)
        x = (W - total) / 2
        for c, w in zip(text, widths):
            d.text((x, y), c, font=fnt, fill=color)
            x += w + tracking
        return
    bbox = d.textbbox((0, 0), text, font=fnt)
    d.text(((W - (bbox[2] - bbox[0])) / 2, y), text, font=fnt, fill=color)

def rule(d, x0, x1, y, color, w=1):
    d.line([(x0, y), (x1, y)], fill=color, width=w)

def waveform(d, cx, cy, w, h, color, lw=2):
    pts = []
    for i in range(201):
        t = i / 200
        x = cx - w / 2 + t * w
        amp = h / 2 * math.sin(t * math.pi)
        y = cy + amp * math.sin(t * 2 * math.pi * 6)
        pts.append((x, y))
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=color, width=lw)

def make_cover():
    W, H = 800, 1130
    img = Image.new("RGB", (W, H), INK)
    d = ImageDraw.Draw(img, "RGBA")
    M = 56

    # marca d'água "5" gigante e discreta
    d.text((W - 300, H - 540), "5", font=font_sans(440), fill=FAINT)
    d.text((M - 20, 96), "5", font=font_sans(330), fill=(16, 16, 18))

    # linhas de espectro sutis (terço inferior)
    for i in range(60):
        t = i / 59
        y = int(H * 0.52 + t * H * 0.36)
        a = int(18 + 26 * math.sin(t * math.pi))
        d.line([(M, y), (W - M, y)], fill=(*GRAY, a), width=1)

    # régua vermelha topo
    rule(d, M, W - M, 72, RED, w=3)

    # label superior (tracking largo)
    center(d, "MATERIAL GRATUITO", 90, font_sans(13), GRAY_LT, W, tracking=6)

    # título grotesco caixa-alta
    title = [
        ("5 ERROS QUE",   WHITE),
        ("DESTROEM",      WHITE),
        ("SUA",           RED),
        ("CREDIBILIDADE", RED),
        ("AO FALAR",      WHITE),
    ]
    fnt = font_sans(66)
    y = 176
    for text, color in title:
        center(d, text, y, fnt, color, W)
        y += 74

    # subtítulo
    center(d, "e como corrigir cada um deles", y + 8, font_sans(19, bold=False), GRAY_LT, W)
    y += 46

    # divisória + onda vermelha
    rule(d, M * 2, W - M * 2, y + 30, RED_DEEP, w=1)
    waveform(d, W // 2, y + 96, W - M * 3, 50, RED, lw=2)

    # bloco autor
    ay = H - 224
    rule(d, M, W - M, ay, GRAY, w=1)
    center(d, "EMMANUEL DUARTE", ay + 24, font_sans(24), WHITE, W)
    center(d, "A VOZ DA RÁDIO ITATIAIA", ay + 60, font_sans(13), RED, W, tracking=4)

    # rodapé
    rule(d, M, W - M, H - 58, RED, w=3)
    center(d, "www.locutoremmanuel.com.br", H - 42, font_mono(12), GRAY_LT, W)

    out = os.path.join(OUT, "01-cover-lead-magnet.png")
    img.save(out, "PNG", dpi=(150, 150))
    print("OK", out)

if __name__ == "__main__":
    make_cover()
