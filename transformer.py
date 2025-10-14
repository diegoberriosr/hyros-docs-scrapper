from fpdf import FPDF
import os

class Transformer():

  @staticmethod
  def convert_to_pdf(text: str, filename: str, destination: str = './documentation'):
    pdf = FPDF()
    pdf.add_page()

    pdf.add_font('DejaVu', '', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', uni=True)
    pdf.set_font('DejaVu', '', 12)

    pdf.multi_cell(0, 10, text)

    os.makedirs(destination, exist_ok=True)

    pdf.output(os.path.join(destination, filename))
