# In few shot prompt templates, we actually provide some input-output examples and it will
# generate the responses based on those examples if question related to those examples' input is asked

from decouple import config
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate, FewShotPromptTemplate

import os

OPENAI_API_KEY = config("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

llm_model = OpenAI()

examples = [
    {
        "input": "Write a response to a customer asking for a product refund due to a defect.",
        "output": "Dear [Customer Name],\n\nThank you for reaching out to us regarding your experience with [Product Name]. We apologize for any inconvenience caused. We understand how important it is for our customers to receive high-quality products. Please provide us with your order number and a brief description of the issue, and we’ll be happy to initiate the refund process.\n\nBest regards,\n[Your Company Name]",
    },
    {
        "input": "Respond to a client requesting a meeting to discuss project updates.",
        "output": "Hello [Client Name],\n\nThank you for your interest in discussing the latest updates on the project. We would be happy to schedule a meeting at your convenience. Please let us know your preferred time, and we’ll do our best to accommodate. Looking forward to our discussion!\n\nWarm regards,\n[Your Name]",
    },
    {
        "input": "Reply to a customer asking about product availability.",
        "output": "Dear [Customer Name],\n\nThank you for your inquiry about [Product Name]. We’re pleased to inform you that this item is currently available. If you’d like to place an order or need further assistance, please feel free to reach out. We look forward to serving you soon!\n\nBest,\n[Your Company Name]",
    },
]


example_prompt = PromptTemplate.from_template("Input: {input}\n Output: {output}")

prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    suffix="Question: {input}",
    input_variables=["input"],
)

formatted_template = prompt.format(
    input="Could you help me with tracking my recent order?"
)

response = llm_model.invoke(formatted_template)

print(response)
