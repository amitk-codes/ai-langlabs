from decouple import config
from langchain_community.document_loaders import PDFMinerLoader

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

file_path = os.path.abspath("assets/pdf_doc.pdf")
loader = PDFMinerLoader(file_path)

parsedLoader = loader.load()
doc_content = parsedLoader[0].page_content

print(doc_content)
