import streamlit as st
import requests

API_URL = "https://text-to-sql-llm-app-backend.onrender.com"

st.title("Natural Language → SQL (LLM + SQLite)")


question = st.text_input("Ask a question about the database")


st.sidebar.title("Upload Your Database")

uploaded_file = st.sidebar.file_uploader(
    "Upload SQLite Database",
    type=["sqlite", "db"]
)

if uploaded_file:
    response = requests.post(
        f"{API_URL}/upload_db",
        files={"file": uploaded_file}   
    )

    if response.status_code == 200:
        st.sidebar.success("Database uploaded successfully")
    else:
        st.sidebar.error("Database upload failed.")

if st.button("Generate & Run"):

    if not question.strip():
        st.warning("Please enter a question.")
        st.stop()

    payload = {"question": question}

    response = requests.post(f"{API_URL}/query", json=payload)

    data = response.json()   

    if "error" in data:
        st.error(data["error"])
        st.stop()


    if "sql" in data:
        st.subheader("Generated SQL Query")
        st.code(data["sql"], language="sql")


    if "result" in data:
        st.subheader("Results")

        result = data["result"]


        if isinstance(result, dict) and "error" in result:
            st.error(result["error"])

        elif isinstance(result, dict) and "rows" in result:
            st.dataframe(result["rows"], width="stretch")

        else:
            st.json(result)
