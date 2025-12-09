from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import JsonOutputParser
import sqlite3

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

def get_schema(db_path):
    connect=sqlite3.connect(db_path)
    cursor=connect.cursor()
    cursor.execute("SELECT sql from sqlite_master WHERE type='table';")
    schema= "\n".join([row[0] for row in cursor.fetchall()])
    connect.close()
    return schema

def build_chain(schema_text):
    prompt=ChatPromptTemplate.from_template("""
    You are an expert SQL generator. Use ONLY the provided schema.

    SCHEMA:
    {schema}
                                            
    USER_QUESTION:
    {question}
                                            
    Return JSON ONLY:
    {{
       "sql_query": "...",
       "explaination":"..."
    }}
    
    """)
    parser = JsonOutputParser()

    chain = (
        {
            "schema": lambda x : schema_text,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | parser
    )

    return chain

def generate_sql(question, db_path):
    schema_text= get_schema(db_path)
    chain = build_chain(schema_text)
    return chain.invoke(question)

def run_query(sql, db="mydb.sqlite"):
    if not sql:
        return {"error": "No SQL was generated"}
    
    forbidden = ["drop", "delete", "update", "insert", "alter"]

    if any(word in sql.lower() for word in forbidden):
        return "Dangerous SQL opetation blocked"
    
    try:
        connection = sqlite3.connect(db)
        cursor = connection.cursor()

        cursor.execute(sql)
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]
        connection.close()


        return{
            "columns": columns,
            "rows": rows
        }
    except Exception as e:
        return {"error": str(e)}