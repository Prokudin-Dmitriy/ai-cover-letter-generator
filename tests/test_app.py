from app.models import PromptData
from app.utils import get_structured_prompt
from app.main import app
import pytest
from unittest.mock import patch
from pydantic import ValidationError
from fastapi.testclient import TestClient


@pytest.fixture
def client():
    return TestClient(app)


def test_structured_prompt_with_resume():
    data = PromptData(info="My experience...", is_job_info=False)

    result = get_structured_prompt(data)

    assert "resume" in result
    assert "My experience" in result


def test_structured_prompt_with_job_description():
    data = PromptData(info="Job involves AI", is_job_info=True)

    result = get_structured_prompt(data)

    assert "job description" in result
    assert "AI" in result


def test_structured_prompt_with_custom_prompt():
    data = PromptData(prompt="Write me a formal letter", info="details", is_job_info=False)
    result = get_structured_prompt(data)
    assert result.startswith("$Write me a formal letter")


def test_promptdata_validation_error():
    try:
        PromptData(is_job_info=True)
    except ValidationError as e:
        assert "info" in str(e)


def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "cover letter" in response.json()["The context"]


def test_list_models(client):
    with patch("app.main.ai_client.list", return_value={"models": ["model1", "model2"]}):
        response = client.get("/tags/")
        assert response.status_code == 200
        assert response.json() == {"models": ["model1", "model2"]}


def test_generate_endpoint(client):
    fake_response = type("FakeResp", (), {"response": "Some generated cover letter"})()
    content = {"info": "Job: Backend Engineer", "is_job_info": True}

    with patch("app.main.ai_client.generate", return_value=fake_response):
        response = client.post("/generate/", json=content)
        data = response.json()

        assert response.status_code == 200
        assert "Some generated cover letter" in data["generated answer"]
