import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.title("Natural Language -> SQL (LLM + SQLite)")

question = st.text_input("Ask a question about the database")

if st.button("Generate & Run"):
    payload = {"question": question}

    response = requests.post(f"{API_URL}/query", json=payload)
    data = response.json()

    st.subheader("Generated SQL Query")
    st.code(data["sql"],language="sql")

    st.subheader("Results")
    result = data["result"]

    if isinstance(result,dict) and "rows" in result:
        st.dataframe(result["rows"])

    else:
        st.write(result)