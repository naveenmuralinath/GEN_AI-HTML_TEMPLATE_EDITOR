import os
import asyncio
from huggingface_hub import InferenceClient
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()


client = InferenceClient(model="mistralai/Mistral-7B-Instruct-v0.2", token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

async def modify_html(html_content: str, prompt_text: str):
    """Returns an async generator that streams modified HTML using Hugging Face's Inference API."""

    prompt_template = PromptTemplate.from_template(
        """You are an AI that modifies existing HTML based on user instructions.
        The user will provide an HTML document, and you should apply the changes described.

        HTML:
        {html}

        Changes requested:
        {changes}

        Return the entire modified HTML document."""
    )

    full_prompt = prompt_template.format(html=html_content, changes=prompt_text)

    
    response = await asyncio.to_thread(client.text_generation, full_prompt, max_new_tokens=500)

    async def response_generator():
        for chunk in response.split("\n"):  
            if chunk:
                await asyncio.sleep(0.05)  
                yield chunk  

    return response_generator()  