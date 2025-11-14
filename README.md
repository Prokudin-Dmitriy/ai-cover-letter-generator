# AI-Powered Cover Letter Generator
![Tests](https://github.com/Prokudin-Dmitriy/ai-cover-letter-generator/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green?logo=open-source-initiative&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi)
![pytest](https://img.shields.io/badge/pytest-tested-blue?logo=pytest)

## 🚀 What is this?

An API that uses AI to automatically generate a tailored cover letter based on either a job description/resume **or** an uploaded resume/job description file (PDF or DOCX).  
Built with FastAPI, Pydantic, and integrates text extraction for PDF/DOCX (via PyMuPDF / python-docx) and an AI model endpoint.

## 🧩 Key Features

- Accepts **plain text input** (job description/resume) or **file upload** (.pdf or .docx)
- Validates file type, extracts text, and feeds into AI prompt pipeline
- Structured API via FastAPI with endpoints for prompt generation
- Lightweight FastAPI service that can be integrated into any backend or microservice

## 🛠️ Tech Stack

| Layer       | Technology                         |
|-------------|------------------------------------|
| Backend     | FastAPI                            |
| Data Models | Pydantic                           |
| File I/O    | PyMuPDF (PDF) / python-docx (DOCX) |
| AI Client   | Ollama / customizable              |
| Testing     | pytest, pytest-asyncio, httpx      |
| DevOps      | GitHub Actions, CI                 |

## 📦 Installation

```bash
git clone https://github.com/Prokudin-Dmitriy/ai-cover-letter-generator.git
cd ai-cover-letter-generator
pip install -r requirements.txt
cp .env.example .env
# edit .env with your API keys
```

## 🧪 Testing & Coverage

Run the full test suite with coverage:

```bash
pytest --cov=app --cov-report=html
```