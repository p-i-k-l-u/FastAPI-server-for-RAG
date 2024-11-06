from pydantic import BaseModel
from typing import List

class DocumentRequest(BaseModel):
    document_name: str
    document_content: str

class QueryRequest(BaseModel):
    query: str

class QueryResult(BaseModel):
    query: str
    results: List[str]
