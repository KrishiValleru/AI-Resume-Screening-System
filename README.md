# AI Resume Screening & Interview Quiz System

## Live Demo

🔗 Website: https://ai-resume-screening-system-3cvypksg5mqfuqndd7uqgu.streamlit.app

## Overview

An AI-powered resume screening and interview assessment system that evaluates candidates against job requirements using Large Language Models, vector embeddings, and semantic search.

The application allows recruiters to:

* Upload resume PDFs
* Enter job requirements
* Generate interview questions automatically
* Evaluate candidate responses using Gemini AI
* Calculate candidate scores
* Determine selection status

---

## Features

### Resume Analysis

* PDF resume upload
* Resume text extraction
* Resume embedding generation using Agno + Gemini

### Vector Database

* Embeddings stored in PostgreSQL using PgVector
* Semantic similarity search

### Interview Assessment

* AI-generated interview questions
* Candidate answer submission
* Automated answer evaluation using Gemini API

### Final Decision

* Candidate scoring
* Selection / Rejection recommendation

---

## Technologies Used

* Python
* Streamlit
* Agno
* Gemini API
* PostgreSQL
* PgVector
* pdfplumber
* SQLAlchemy
* Psycopg

---

## Project Structure

```text
app.py
database.py
evaluator.py
quiz_generator.py
resume_parser.py
vector_store.py
requirements.txt
```

---

## Workflow

1. Upload Resume PDF
2. Enter Job Description
3. Generate Interview Questions
4. Submit Candidate Answers
5. Evaluate Responses
6. View Candidate Score
7. Display Final Result

---

## Author

Krishi Valleru
