import os
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()  # Load API keys from .env

# Initialize Mistral-7B model via Hugging Face Inference API
llm = HuggingFaceEndpoint(
    endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    temperature=0.7,
    model_kwargs={"max_length": 500}
)


# async def modify_html(html_content: str, prompt: str):
#     """Generates AI-modified HTML based on user instructions using Hugging Face API."""
    
#     prompt_template = PromptTemplate.from_template(
#         "Modify this HTML: {html}. Apply the following changes: {changes}."
#     )
#     full_prompt = prompt_template.format(html=html_content, changes=prompt)
    
#     response = llm.stream(full_prompt)  # Streaming AI response

#     async for chunk in response:  
#         if chunk.text:
#             yield chunk.text  # Ensure only valid text chunks are sent
import asyncio

async def modify_html(html_content: str, prompt_text: str):
    """
    Simulates an AI-based HTML modification using async generation.
    """
    modified_html = f"<h1>{prompt_text}</h1>\n{html_content}"
    
    # Simulating a streaming response
    for chunk in modified_html.split("\n"):
        await asyncio.sleep(0.5)  # Simulate processing delay
        yield chunk
