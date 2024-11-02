# In few shot prompt templates, we actually provide some input-output examples and it will
# generate the responses based on those examples if question related to those examples' input is asked

from decouple import config
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

examples = [
    {"input": "2 ➕ 2", "output": "4"},
    {"input": "2 ➕ 3", "output": "5"},
]

example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{input}"),
        ("ai", "{output}"),
    ]
)

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

final_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an amazing math solver"),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)


chat_model = ChatOpenAI()

response = chat_model.invoke(final_prompt.format(input="What is 2 ➕ 24?"))

print(response)
