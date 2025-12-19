from PyPDF2 import PdfReader, PdfWriter

PDF_PATH = r"C:\Users\david.frieri\Documents\4th YEAR UFT\PDF encription\MIE 491 - Project Requirements - BWH.pdf"

reader = PdfReader(PDF_PATH)
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.encrypt("BWH2025")

with open("MIE 491 - Project Requirements - BWH.pdf", "wb") as f:
    writer.write(f)