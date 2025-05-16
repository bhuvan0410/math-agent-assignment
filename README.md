
# 🧠 Math Professor Agent (Human-in-the-Loop: Feedback-Based Learning)

This project is part of the AI Planet Assignment titled "Human-in-the-Loop: Feedback-Based Learning – Math Agent".  
It demonstrates a system that replicates a math professor using an Agentic-RAG architecture, providing step-by-step educational responses to math queries.

---

## 🚀 Features

- ✅ **Agentic-RAG Architecture**  
- 📚 **Knowledge Base Retrieval using FAISS + HuggingFace Embeddings**  
- 🌐 **Web Search Fallback via Serper API**  
- 📩 **Input & Output Guardrails**  
- ✍️ **Human-in-the-loop Feedback Collection**  
- 🖥️ **Streamlit UI for User Interaction**

---

## 📂 Project Structure

```
math-agent-assignment/
├── main.py                # Streamlit UI
├── rag_pipeline.py        # RAG logic (KB + Serper search + LLM)
├── feedback.py            # Feedback handling
├── kb/                    # Folder with knowledge base .txt files
├── .env.example           # Environment variable sample
├── requirements.txt       # Python dependencies
├── jee_benchmark.py       # Optional benchmarking script (if used)
└── README.md              # Project documentation
```

---

## 📦 Setup Instructions

1. Clone the Repository
```bash
git clone https://github.com/bhuvan0410/math-agent-assignment.git
cd math-agent-assignment
```

2. Create and Activate Virtual Environment (Python 3.9+)
```bash
python3.9 -m venv venv
source venv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Configure Environment Variables
```bash
cp .env.example .env
# Then add your GROQ_API_KEY and SERPER_API_KEY to the .env file
```

5. Run the Streamlit App
```bash
streamlit run main.py
```

---

## 🧪 Sample Questions to Try

### From Knowledge Base:
- What is the derivative of x^2?
- How do you integrate x^3?
- What is the quadratic formula?

### From Web Search:
- What is Euler’s identity?
- What is the integral of sin(x)/x?
- What is the Taylor series of e^x?

---

## 📝 Feedback Example
Users can provide feedback on generated answers and optionally suggest corrections. Feedback is stored for future use and review.

---

## 📃 License
Apache 2.0 License  
© 2025 Bhuvan Pagilla

