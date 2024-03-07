import fitz 
import os



def is_password_protected_pdf(pdf_file_path):
    doc = fitz.Document(pdf_file_path)
    if doc.needs_pass:
        return True
    return False



# pdf_file_path = openPath()
pdf_file_path = os.path.join(os.getcwd(), 'pdfs', 'test.pdf')
print(is_password_protected_pdf(pdf_file_path))
