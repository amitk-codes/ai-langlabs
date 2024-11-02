from decouple import config
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm_model = OpenAI()

prompt_template = PromptTemplate.from_template("What is {topic} in {subject} ?")
formatted_prompt = prompt_template.format(topic="hoisting", subject="JavaScript")

reponse = llm_model.invoke(formatted_prompt)

print(reponse)
