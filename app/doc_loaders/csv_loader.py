from decouple import config
from langchain_community.document_loaders.csv_loader import CSVLoader

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

file_path = os.path.abspath("assets/csv_doc.csv")

loader = CSVLoader(file_path)

parsedLoader = loader.load()

print(parsedLoader)
