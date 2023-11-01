import os
import PyPDF2
import json

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text

def pdfs_to_jsonl(directory_name, output_file):
    directory = os.path.join(SCRIPT_DIR, directory_name)
    with open(output_file, 'w') as f:
        for filename in os.listdir(directory):
            if filename.endswith('.pdf'):
                pdf_path = os.path.join(directory, filename)
                text = extract_text_from_pdf(pdf_path)
                json_line = json.dumps({"text": text})
                f.write(json_line + '\n')

pdfs_to_jsonl("arxiv_pdfs", "arxiv_pdfs.jsonl")

