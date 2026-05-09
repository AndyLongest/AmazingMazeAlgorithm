from pathlib import Path
import textwrap

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas


MD_PATH = Path('docs/top5-teaching-bad-repos.md')
PDF_PATH = Path('docs/top5-teaching-bad-repos.pdf')
# Approximate wrap width for A4 with 20mm margins and 12pt STSong-Light text.
MAX_CHARS_PER_LINE = 46
# Larger heading fonts need fewer characters per visual line to avoid overflow.
H1_WRAP_ADJUST = 4
H2_WRAP_ADJUST = 2


def build_pdf() -> None:
    text = MD_PATH.read_text(encoding='utf-8').splitlines()

    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

    c = canvas.Canvas(str(PDF_PATH), pagesize=A4)
    _, height = A4
    left = 20 * mm
    top = height - 20 * mm
    bottom = 20 * mm
    line_h = 7 * mm
    y = top
    c.setFont('STSong-Light', 12)

    for raw_line in text:
        line = raw_line.strip()
        if line.startswith('# '):
            font_size = 16
            c.setFont('STSong-Light', font_size)
            wrapped = textwrap.wrap(line[2:].strip(), width=MAX_CHARS_PER_LINE - H1_WRAP_ADJUST) or ['']
        elif line.startswith('## '):
            font_size = 14
            c.setFont('STSong-Light', font_size)
            wrapped = textwrap.wrap(line[3:].strip(), width=MAX_CHARS_PER_LINE - H2_WRAP_ADJUST) or ['']
        else:
            font_size = 12
            c.setFont('STSong-Light', font_size)
            wrapped = textwrap.wrap(line, width=MAX_CHARS_PER_LINE) or ['']

        for part in wrapped:
            if y < bottom:
                c.showPage()
                c.setFont('STSong-Light', font_size)
                y = top
            c.drawString(left, y, part)
            y -= line_h

        y -= 1 * mm

    c.save()


if __name__ == '__main__':
    build_pdf()
    print(f'Generated: {PDF_PATH}')
