from decouple import config
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate


import os

OPENAI_API_KEY = config("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# setting up the chat_model using our langchain_openai
chat_model = ChatOpenAI()

prompt_template = ChatPromptTemplate([
    (
        "system",
        "You are an standup comedian.",
    ),
    ("human", "Tell me about the {topic}"),
])

formatted_prompt_template = prompt_template.format(topic="OpenAI")

print(formatted_prompt_template)

# response = chat_model.invoke(formatted_prompt_template)
# print(response)

