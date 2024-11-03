from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

file_path = os.path.abspath('assets/long_text_doc.txt')

loader = TextLoader(file_path)
loaded_content = loader.load()

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

document = text_splitter.split_documents(loaded_content)