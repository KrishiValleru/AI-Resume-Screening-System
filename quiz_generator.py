from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.models.google import Gemini

def generate_questions(resume_text, job_description):

    agent = Agent(
        model=Gemini(id="gemini-2.5-flash-lite")
    )

    prompt = f"""
Resume:
{resume_text}

Job Description:
{job_description}

Generate exactly 5 interview questions.

Return only the questions.

One question per line.
"""

    response = agent.run(prompt)

    return response.content