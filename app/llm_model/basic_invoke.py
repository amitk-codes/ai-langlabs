from decouple import config
from langchain_openai import OpenAI

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

# setting up the llm_model using our langchain_openai
llm_model = OpenAI()

# calling the model with our question
input_question = "What is JavaScript ?"

response = llm_model.invoke(input_question)
print(response)

