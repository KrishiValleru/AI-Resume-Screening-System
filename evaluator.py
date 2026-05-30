import re

from dotenv import load_dotenv

load_dotenv()

from agno.agent import Agent
from agno.models.google import Gemini


def evaluate_answer(question, answer):

    agent = Agent(
        model=Gemini(id="gemini-2.5-flash-lite")
    )

    prompt = f"""
Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer.

Return exactly:

Score: XX

Feedback: short feedback
"""

    response = agent.run(prompt)

    result = response.content

    score_match = re.search(r"Score:\s*(\d+)", result)

    score = 0

    if score_match:
        score = int(score_match.group(1))

    return score, result