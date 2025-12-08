from fastapi import FastAPI
from pydantic import BaseModel
from sql import generate_sql, run_query

app = FastAPI()

class QueryRequest(BaseModel):
    question : str

@app.get("/")
def root():
    return {
        "message" : "Your SQL LLM API is running"
    }

@app.post("/generate")
def generate(req: QueryRequest):
    response = generate_sql(req.question)
    return response

@app.post("/query")
def query(req: QueryRequest):
    generated = generate_sql(req.question)
    sql = generated.get("sql_query")

    result = run_query(sql)
    return {
        "sql": sql,
        "explanation": generated.get("explanation"),
        "result": result
    }