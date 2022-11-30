"""
Prompt the user for their name and outputs


Using fpdf2, create a shirtificate.pdf file with the following steps
    The orientation should be a portrait
    Format should be A4 (210mm wide by 297mm tall)
    Top of the PDF should say "CS50 Shirtificate" as text (centered horizontally)
    Shirt image should be centered horizontally
    User's name should be on top of the shirt in white text (Look at example.PNG for example)
"""

from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("helvetica", "B", 42)
pdf.cell(200, 20, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=0.5, y=50)
pdf.ln(100)
pdf.set_text_color(255,255,255)
pdf.set_font("helvetica", "B", 24)
pdf.cell(200, 10, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")