from dotenv import load_dotenv
import uuid

load_dotenv()

from agno.knowledge.document.base import Document
from agno.knowledge.embedder.google import GeminiEmbedder
from agno.vectordb.pgvector import PgVector

DB_URL = "postgresql+psycopg://Krishi.Valleru@localhost/resume_screening"

vector_db = PgVector(
    table_name="resume_embeddings",
    db_url=DB_URL,
    embedder=GeminiEmbedder()
)

def initialize_vector_db():
    vector_db.create()

def store_resume(resume_text):
    document = Document(
        content=resume_text,
        name="resume"
    )

    vector_db.insert(
        content_hash=str(uuid.uuid4()),
        documents=[document]
    )

def search_resume(query):
    return vector_db.search(
        query=query,
        limit=5
    )