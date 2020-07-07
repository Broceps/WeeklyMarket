from PyPDF2 import PdfFileReader
from pathlib import Path

pdf_path = "../_files/letter.pdf"
pdf = PdfFileReader(pdf_path)
pdf.getPage(0)