from fastapi import Form
from pydantic import BaseModel, Field
from uuid import uuid4, UUID


class PromptData(BaseModel):
    """
    Model for promt.

    Attributes:
        id: unique identifier.
        prompt: base of the promt.
        info: resume or job decsription text.
        is_job_info: bolean value wether it is resume or job decsription.
    """

    id: UUID = Field(default_factory=uuid4)
    prompt: str | None = None
    info: str
    is_job_info: bool

    @classmethod
    def as_form(
        cls,
        prompt: str | None = Form(None),
        info: str | None = Form(None),
        is_job_info: bool = Form(...)
    ):
        """Allows FastAPI to build the model from form data."""
        return cls(prompt=prompt, info=info, is_job_info=is_job_info)
