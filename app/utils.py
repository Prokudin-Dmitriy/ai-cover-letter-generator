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
