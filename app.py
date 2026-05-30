import streamlit as st
import tempfile

from resume_parser import extract_text_from_pdf
from vector_store import initialize_vector_db, store_resume
from quiz_generator import generate_questions
from evaluator import evaluate_answer


st.set_page_config(page_title="AI Resume Screening System")

st.title("AI Resume Screening & Interview Quiz System")

initialize_vector_db()

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

job_description = st.text_area(
    "Enter Job Description"
)

if uploaded_file and job_description:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    resume_text = extract_text_from_pdf(pdf_path)

    store_resume(resume_text)

    st.success("Resume processed successfully!")

    if st.button("Generate Questions"):

        questions_text = generate_questions(
            resume_text,
            job_description
        )

        questions = [
            q.strip()
            for q in questions_text.split("\n")
            if q.strip()
        ]

        st.session_state.questions = questions

if "questions" in st.session_state:

    st.subheader("Interview Questions")

    answers = []

    for i, question in enumerate(st.session_state.questions):

        st.write(question)

        answer = st.text_area(
            f"Answer {i+1}",
            key=f"answer_{i}"
        )

        answers.append(answer)

    if st.button("Evaluate Candidate"):

        total_score = 0

        for question, answer in zip(
            st.session_state.questions,
            answers
        ):

            score, feedback = evaluate_answer(
                question,
                answer
            )

            total_score += score

        average_score = total_score / len(
            st.session_state.questions
        )

        st.subheader("Final Result")

        st.write(
            f"Candidate Score: {average_score:.2f}%"
        )

        if average_score >= 70:
            st.success("Selected")
        else:
            st.error("Not Selected")