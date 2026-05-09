from pathlib import Path

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas


MD_PATH = Path('docs/top5-teaching-bad-repos.md')
PDF_PATH = Path('docs/top5-teaching-bad-repos.pdf')
FONT_NAME = 'STSong-Light'


def wrap_text_by_width(text: str, font_size: int, max_width: float) -> list[str]:
    if not text:
        return ['']

    lines: list[str] = []
    current = ''
    for ch in text:
        candidate = current + ch
        if pdfmetrics.stringWidth(candidate, FONT_NAME, font_size) <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = ch

    if current:
        lines.append(current)

    return lines


def build_pdf() -> None:
    text = MD_PATH.read_text(encoding='utf-8').splitlines()

    pdfmetrics.registerFont(UnicodeCIDFont(FONT_NAME))

    c = canvas.Canvas(str(PDF_PATH), pagesize=A4)
    width, height = A4
    left = 20 * mm
    right = 20 * mm
    top = height - 20 * mm
    bottom = 20 * mm
    max_width = width - left - right
    line_h = 7 * mm
    y = top

    c.setFont(FONT_NAME, 12)

    for raw_line in text:
        line = raw_line.strip()
        if line.startswith('# '):
            font_size = 16
            payload = line[2:].strip()
        elif line.startswith('## '):
            font_size = 14
            payload = line[3:].strip()
        else:
            font_size = 12
            payload = line

        c.setFont(FONT_NAME, font_size)
        wrapped = wrap_text_by_width(payload, font_size, max_width)

        for part in wrapped:
            if y < bottom:
                c.showPage()
                c.setFont(FONT_NAME, font_size)
                y = top
            c.drawString(left, y, part)
            y -= line_h

        y -= 1 * mm

    c.save()


if __name__ == '__main__':
    build_pdf()
    print(f'Generated: {PDF_PATH}')
