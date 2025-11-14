from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Depends,
    HTTPException
)
from ollama import Client

from app.models import PromptData
from app.config import settings
from app.utils import (
    get_structured_prompt,
    get_extracted_text
)

app = FastAPI()

ai_client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + settings.ollama_api_key}
)


@app.get("/")
def read_root():
    return {"The context": "I am the cover letter creation app."}


@app.get("/tags/")
def list_models():
    response = ai_client.list()
    return response


@app.post("/generate/")
async def send_promt_data(
    prompt: PromptData = Depends(PromptData.as_form),
    file: UploadFile = File(None)
):
    """Endpoint responsive for generating the cover letter."""

    if file:
        content_bytes = await file.read()
        prompt.info = get_extracted_text(content_bytes, file.content_type, file.filename)

    if not prompt.info:
        raise HTTPException(400, "Either 'info' text or a file must be provided.")

    content = get_structured_prompt(prompt)

    response = ai_client.generate("gpt-oss:20b-cloud", prompt=content, stream=False)

    return {"prompt": prompt, "generated answer": response.response, "file": file}
