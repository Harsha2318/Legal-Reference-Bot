from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from .gemini_utils import get_legal_response

app = FastAPI()

# Allow CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

class LegalQuery(BaseModel):
    query: str

@app.post("/search/")
async def search(query: LegalQuery):
    response = get_legal_response(query.query)
    return response
