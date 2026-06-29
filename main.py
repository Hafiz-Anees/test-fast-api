from fastapi import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel


class QueryRequest(BaseModel):
    query: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/query")
def get_query(request: QueryRequest):
    return {"query": request.query}