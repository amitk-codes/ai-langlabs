from decouple import config
from langchain_community.document_loaders import TextLoader
from langchain.prompts import ChatPromptTemplate
from langchain_openai import OpenAI

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

file_path = os.path.abspath("assets/text_doc.txt")
loader = TextLoader(file_path)

parsedLoader = loader.load()
doc_content = parsedLoader[0].page_content

prompt_template = ChatPromptTemplate.from_messages([
  ("human", "Give the title to the {file_content}")
])

formatted_prompt = prompt_template.format_messages(file_content = doc_content)

chat_model = OpenAI()

response = chat_model.invoke(formatted_prompt)
print(response)