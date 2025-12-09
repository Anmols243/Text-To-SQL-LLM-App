from fastapi import FastAPI, UploadFile, File
import os
import shutil
from pydantic import BaseModel
from sql import generate_sql, run_query

app = FastAPI()
UPLOAD_DIR = "uploaded_dbs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class QueryRequest(BaseModel):
    question : str

@app.get("/")
def root():
    return {
        "message" : "Your SQL LLM API is running"
    }

@app.post("/upload_db")
def upload_db(file: UploadFile = File(...)):
    global LATEST_DB_PATH

    db_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(db_path,"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    LATEST_DB_PATH = db_path

    return {
        "message" : "Database uploaded Successfully",
        "db_path" : db_path
    }

@app.post("/generate")
def generate(req: QueryRequest):
    if not LATEST_DB_PATH:
        return {"error": "No Database Uploaded Yet."}
    response = generate_sql(req.question)
    return response

LATEST_DB_PATH = None
@app.post("/query")
def query(req: QueryRequest):
    global LATEST_DB_PATH

    if not LATEST_DB_PATH:
        return {"error": "No database uploaded yet."}
    
    generated = generate_sql(req.question, LATEST_DB_PATH)
    sql = generated.get("sql_query")
    
    if not sql:
        return {"error":"Failed to generate SQL from the model."}

    result = run_query(sql, LATEST_DB_PATH)
    return {
        "sql": sql,
        "explanation": generated.get("explanation"),
        "result": result
    }