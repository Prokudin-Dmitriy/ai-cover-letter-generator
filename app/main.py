from fastapi import FastAPI
from ollama import Client

from app.models import PromptData
from app.config import settings
from app.utils import get_structured_prompt

app = FastAPI()

ai_client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + settings.ollama_api_key}
)


@app.get("/")
def read_root():
    return {"The context": "I am the cover letter creation app"}


@app.get("/tags/")
def list_models():
    response = ai_client.list()
    return response


@app.post("/generate/")
def send_promt_data(prompt: PromptData):
    """Endpoint responsive for generating the cover letter"""

    content = get_structured_prompt(prompt)

    response = ai_client.generate("gpt-oss:20b-cloud", prompt=content, stream=False)

    return {"prompt": prompt, "generated answer": response.response}
