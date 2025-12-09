# 🔥 Natural Language → SQL (LLM + SQLite)

A full-stack AI-powered application that allows users to upload any SQLite database and query it using plain English.  
The system uses an LLM to generate SQL, executes it safely, and displays results in a clean web UI.

---

## 🚀 Features

- ✅ Upload any SQLite database
- ✅ Automatic schema extraction
- ✅ Natural Language → SQL using LLM
- ✅ Safe SQL execution
- ✅ FastAPI backend
- ✅ Streamlit frontend
- ✅ Full error handling (no crashes)
- ✅ Dynamic database switching

---

## 🏗️ Tech Stack

- **Backend:** FastAPI, SQLite, Python
- **Frontend:** Streamlit
- **LLM:** Google Gemini (via LangChain)
- **Deployment:** Render (backend), Streamlit Cloud (frontend)

---

## 🗂️ Project Structure

Text-To-SQL-LLM-App/
├── backend/
│ ├── app.py
│ └── sql.py
│
├── frontend/
│ └── streamlit_app/
│ └── app.py
│
├── .gitignore
├── requirements.txt
└── README.md


---

## ⚙️ How It Works

1. User uploads a SQLite database (`.db` or `.sqlite`).
2. Backend extracts the table schema automatically.
3. User enters a natural language query.
4. LLM converts it to SQL using the schema.
5. SQL runs safely on the uploaded database.
6. Results are returned and displayed in the UI.

---

## 🖥️ Local Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/Anmols243/Text-To-SQL-LLM-App.git
cd Text-To-SQL-LLM-App
```

### 2️⃣ Start Backend (FastAPI)
```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

### 3️⃣ Start Frontend (Streamlit)
```bash
cd frontend/streamlit_app
pip install -r requirements.txt
streamlit run app.py
```

### 4️⃣ Open in Browser

Streamlit UI: http://localhost:8501

FastAPI Docs: http://localhost:8000/docs

### 🌍 Deployment

Backend deployed on Render

Frontend deployed on Streamlit Cloud

Both using the same GitHub repo

### 📌 Example Use Cases

Business analytics on structured databases

Data exploration without SQL knowledge

AI-powered internal reporting tools

Education: learning SQL via natural language

### 🧠 Author

Anmol Singh
AI / Backend Engineer
GitHub: https://github.com/Anmols243

## ⭐ If you like this project, consider starring the repo!