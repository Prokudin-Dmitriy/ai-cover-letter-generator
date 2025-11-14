import os
import pymupdf
from io import BytesIO
from docx import Document
from fastapi import HTTPException
from .models import PromptData


def get_structured_prompt(prompt: PromptData) -> str:
    """Function for structuring prompt"""

    default_prompt: str = "You are professional assistant in creating a cover letter.\n\
        Create a cover letter from this"
    info: str = prompt.info
    choice_info: str = "resume"

    if prompt.is_job_info:
        choice_info = "job description"

    final_prompt: str = default_prompt if prompt.prompt is None else prompt.prompt

    return f"${final_prompt} ${choice_info} info:\n ${info}"


def get_extracted_text(bytes_data: bytes, content_type: str, filename: str) -> str:
    """
    Extract text from a file.

    Parameters:
        bytes_data: raw bytes of the uploaded file.
        content_type: FastAPI-provided MIME type.
        filename: name of the file to detect extension.

    Returns:
        Extracted text as a string.

    Raises:
        HTTPException: If the file is not a valid PDF or contains no extractable text.
    """

    _, ext = os.path.splitext(filename.lower())
    ext: str = ext.strip()

    is_pdf: bool = (ext == ".pdf" or content_type == "application/pdf")

    is_docx: bool = (
        ext == ".docx"
        or content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

    if is_pdf:
        try:
            doc = pymupdf.open(stream=bytes_data, filetype="pdf")
        except Exception:
            raise HTTPException(400, "File is not a valid PDF.")
        else:
            extracted = "\n".join(page.get_text("text") for page in doc).strip()

        if not extracted:
            raise HTTPException(400, "PDF contains no extractable text.")

        return extracted
    elif is_docx:
        try:
            buffer = BytesIO(bytes_data)
            doc = Document(buffer)
        except Exception:
            raise HTTPException(400, "Invalid or corrupted DOCX file.")
        else:
            extracted = "\n".join(p.text for p in doc.paragraphs).strip()

        if not extracted:
            raise HTTPException(400, "DOCX file contains no readable text.")

        return extracted
    else:
        raise HTTPException(400, "File should be only of format PDF or DOCX.")
