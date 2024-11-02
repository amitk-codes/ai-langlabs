from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser
from decouple import config
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

chat_model = ChatOpenAI()


# Creating the format of the parser
class MyFormattedData(BaseModel):
    name: str = Field(description="Name of the footballer")
    records: list = Field(description="Python list of records")


# setting the pydantic parser
pydantic_parser = PydanticOutputParser(pydantic_object=MyFormattedData)

template = "{request}\n{format_instruction}"

prompt = ChatPromptTemplate.from_messages([("human", template)])

formatted_prompt = prompt.format_messages(
    request="tell me about a footballer",
    format_instruction=pydantic_parser.get_format_instructions(),
)

response = chat_model.invoke(formatted_prompt)
print(response)
