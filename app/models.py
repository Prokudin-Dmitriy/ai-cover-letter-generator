from pydantic import BaseModel, Field
from uuid import uuid4, UUID


class PromptData(BaseModel):
    """ Model for promt.

    Keyword parameters: \n
    prompt -- base of the promt,\n
    info -- resume or job decsription text,\n
    is_job_info -- bolean value wether it is resume or job decsription.
    """

    id: UUID = Field(default_factory=uuid4)
    prompt: str | None = None
    info: str
    is_job_info: bool
