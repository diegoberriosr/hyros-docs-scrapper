from fpdf import FPDF
import os

class Transformer():

  def convert_to_pdf(text: str, filename: str, destination: str = '/'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(0, 10, text)

    os.makedirs(destination, exist_ok=True)

    pdf.output(os.path.join(destination, filename))
