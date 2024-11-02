from decouple import config
from langchain_openai import ChatOpenAI

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# setting up the chat_model using our langchain_openai
chat_model = ChatOpenAI()

input_question = [
    (
        "system",
        "You are an standup commedian.",
    ),
    ("human", "Tell me about the OpenAI"),
]

response = chat_model.invoke(input_question)
print(response)

