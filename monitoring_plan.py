from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm, inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table, TableStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors

#get the size of the paper
width, height = landscape(A4)

#generate styles
styles = getSampleStyleSheet()

#wraps text
styleN = styles["BodyText"]
#aligns text to left
styleN.alignment = TA_LEFT
#normal text wrap
styleBH = styles["Normal"]
#aligns text to center
styleBH.alignment = TA_CENTER

# Headers
h_one = Paragraph('''<b>Project #</b>''', styleN)
h_two = Paragraph('''<b>Project Details</b>''', styleN)
h_three = Paragraph('''<b>Unit of measurement</b>''', styleN)
h_four = Paragraph('''<b>Financial Requirements</b>''', styleN)
h_five = Paragraph('''<b>Physical Requirements</b>''', styleN)

# Texts
one = Paragraph('long paragraph', styleN)
two = Paragraph('1', styleN)
three = Paragraph('120', styleN)
four = Paragraph('$52.00', styleN)
five = Paragraph('$6240.00', styleN)

#data for the table
data = [
    [h_one, h_two, h_three, h_four, '', '', '','', h_five, '', '', '', ''],
    ['one','two','three','Qaurter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4', 'Total', 'Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4', 'Total']
]

#create the table
table = Table(data)

table.setStyle(TableStyle([
    ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
    ('BOX', (0,0), (-1,-1), 0.25, colors.black),
    ('SPAN', (0, 0), (0, 1)),
    ('SPAN', (1, 0), (1, 1)),
    ('SPAN', (2, 0), (2, 1)),

    ('SPAN', (3, 0), (7, 0)),
    ('SPAN', (8, 0), (12, 0))
]))

def coord(x, y, unit=1):
    x, y = x * unit, height -  y * unit
    return x, y

c = canvas.Canvas("a.pdf", pagesize=landscape(A4))
table.wrap(height, width)
table.drawOn(c, *coord(1, 1, inch))
c.save()