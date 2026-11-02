"""QR-код и плакат для кроссворда.

python3 tools/make_qr.py https://<логин>.github.io/kod-bezopasnosti/
-> qr/qr.svg (вектор, для печати любого размера), qr/qr.png (2000 px), qr/poster_a4.png (A4, 300 dpi)
"""
import sys
from pathlib import Path
import segno
from PIL import Image, ImageDraw, ImageFont

url = sys.argv[1]
assert url.startswith("https://"), "нужен https-адрес"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "qr"; OUT.mkdir(exist_ok=True)
DEEP, BLUE, GRAPH, MUTED = "#064B82", "#0089D7", "#243746", "#5E7180"

qr = segno.make(url, error="q")          # Q: читается даже с бликами и потёртостями на печати
qr.save(OUT / "qr.svg", scale=10, border=4, dark=DEEP)
qr.save(OUT / "qr.png", scale=max(1, 2000 // (qr.symbol_size()[0])), border=4, dark=DEEP)

# плакат A4 @300 dpi
W, H = 2480, 3508
F = "/usr/share/fonts/opentype/inter/Inter-"
f = lambda w, s: ImageFont.truetype(F + w + ".otf", s)
im = Image.new("RGB", (W, H), "white"); d = ImageDraw.Draw(im)
d.rectangle((0, 0, W, 900), fill="#EAF7FC")
logo = Image.open(ROOT / "tools/logo.png").convert("RGBA"); logo = logo.resize((1100, round(1100 * logo.height / logo.width)), Image.LANCZOS)
im.paste(logo, ((W - logo.width) // 2, (900 - logo.height) // 2), logo)
d.text((W / 2, 1120), "КОД БЕЗОПАСНОСТИ", font=f("ExtraBold", 190), fill=GRAPH, anchor="mm")
d.text((W / 2, 1300), "интерактивный кроссворд по производственной безопасности", font=f("Medium", 64), fill=MUTED, anchor="mm")
q = Image.open(OUT / "qr.png").convert("RGB").resize((1500, 1500), Image.NEAREST)
im.paste(q, ((W - 1500) // 2, 1450))
d.text((W / 2, 3060), "Наведите камеру телефона на код", font=f("Bold", 84), fill=DEEP, anchor="mm")
d.text((W / 2, 3190), "Удобнее всего играть с компьютера — откройте ссылку:", font=f("Medium", 56), fill=MUTED, anchor="mm")
d.text((W / 2, 3300), url.replace("https://", ""), font=f("Bold", 70), fill=BLUE, anchor="mm")
im.save(OUT / "poster_a4.png", dpi=(300, 300))
print("готово:", *sorted(p.name for p in OUT.iterdir()))
