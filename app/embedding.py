from langchain_openai import OpenAIEmbeddings
from decouple import config

embedding_model = OpenAIEmbeddings(api_key=config("OPENAI_API_KEY"))

query = "Hello, This is Amit Kumar"
document_query = [
  "Hello, This is Amit Kumar",
  "I am a developer",
  "I am a coder",
  "I am a programmer",
  "I am a techie"
]

embedding_query = embedding_model.embed_query(query)

embedding_document_query = embedding_model.embed_documents(document_query)

print(f"embedded query: {embedding_query}")
print(f"embedding document query: {embedding_document_query}")