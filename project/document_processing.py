import PyPDF2
import docx
from io import BytesIO

# Function to extract text from PDF files
def extract_text_from_pdf(pdf_file: BytesIO) -> str:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text

# Function to extract text from DOCX files
def extract_text_from_docx(docx_file: BytesIO) -> str:
    doc = docx.Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

# Function to extract text from TXT files
def extract_text_from_txt(txt_file: BytesIO) -> str:
    return txt_file.read().decode('utf-8')
