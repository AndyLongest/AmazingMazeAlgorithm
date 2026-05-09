from pathlib import Path
import textwrap

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfgen import canvas


MD_PATH = Path('docs/top5-teaching-bad-repos.md')
PDF_PATH = Path('docs/top5-teaching-bad-repos.pdf')


def build_pdf() -> None:
    text = MD_PATH.read_text(encoding='utf-8').splitlines()

    pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))

    c = canvas.Canvas(str(PDF_PATH), pagesize=A4)
    width, height = A4
    left = 20 * mm
    top = height - 20 * mm
    bottom = 20 * mm
    line_h = 7 * mm
    max_chars = 46

    y = top
    c.setFont('STSong-Light', 12)

    for raw_line in text:
        line = raw_line.strip()
        if line.startswith('# '):
            c.setFont('STSong-Light', 16)
            wrapped = textwrap.wrap(line[2:].strip(), width=max_chars - 4) or ['']
        elif line.startswith('## '):
            c.setFont('STSong-Light', 14)
            wrapped = textwrap.wrap(line[3:].strip(), width=max_chars - 2) or ['']
        else:
            c.setFont('STSong-Light', 12)
            wrapped = textwrap.wrap(line, width=max_chars) or ['']

        for part in wrapped:
            if y < bottom:
                c.showPage()
                c.setFont('STSong-Light', 12)
                y = top
            c.drawString(left, y, part)
            y -= line_h

        y -= 1 * mm

    c.save()


if __name__ == '__main__':
    build_pdf()
    print(f'Generated: {PDF_PATH}')
