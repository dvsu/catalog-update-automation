#!/usr/bin/env python3

from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.pagesizes import A4
from reportlab.platypus.paragraph import Paragraph
from reportlab.platypus import SimpleDocTemplate, Spacer
from reportlab.lib.units import cm
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont


def generate_report(attachment:str, title:str, paragraph:list):

    # font_dir = 'C:/Windows/Fonts/'
    # pdfmetrics.registerFont(TTFont('Rubik-Regular', font_dir + 'Rubik-Regular.ttf', subfontIndex=0))
    # font_name = "Rubik-Regular"

    h1 = PS(name = 'Heading1', fontSize= 22) #, fontName=font_name)
    body = PS(name = 'body', fontSize= 12, leading=13) #, fontName=font_name)

    content = []

    content.append(Paragraph('{}<br/><br/>'.format(title), h1))
    content.append(Spacer(1, 20))

    for item in paragraph:
        for param in item:
            content.append(Paragraph('{}<br/>'.format(param), body))
        content.append(Spacer(1, 20))

    doc = SimpleDocTemplate(attachment,pagesize=A4,
                            rightMargin=2*cm,leftMargin=2*cm,
                            topMargin=2*cm,bottomMargin=2*cm)

    doc.build(content)
