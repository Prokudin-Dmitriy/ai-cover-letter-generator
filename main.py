from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import uuid4, UUID

app = FastAPI()


class PromptData(BaseModel):
    """ Model for promt.

    Keyword arguments: \n
    prompt -- base of the promt,\n
    info -- resume or job decsription text,\n
    is_job_info -- bolean value wether it is resume or job decsription.
    """

    id: UUID = Field(default_factory=uuid4)
    prompt: str | None = None
    info: str
    is_job_info: bool


@app.get("/")
def read_root():
    return {"The context": "I am the cover letter creation app"}


@app.post("/dispatch/")
def send_promt_data(prompt: PromptData):
    return {"prompt": prompt}
