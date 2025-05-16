import os
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.docstore.document import Document as LangchainDocument
from openai import OpenAI
from web_search import web_search

load_dotenv()

# Initialize Groq (OpenAI-compatible) client
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# Load .txt files from /kb directory
def load_documents_from_kb(kb_dir="kb"):
    documents = []
    for filename in os.listdir(kb_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(kb_dir, filename), "r", encoding="utf-8") as file:
                content = file.read()
                documents.append(LangchainDocument(page_content=content))
    return documents

# Split and embed documents into FAISS vector store
def create_vectorstore(documents):
    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=20)
    split_docs = text_splitter.split_documents(documents)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(split_docs, embeddings)
    return vectorstore

# Wrapper to load and index KB
def load_and_index_kb():
    documents = load_documents_from_kb()
    return create_vectorstore(documents)

# LLM prompt execution using Groq (LLaMA3)
def run_llm_chain(question, docs):
    context = "\n".join([doc.page_content for doc in docs])
    prompt = f"""You are a math teacher. Use the following context to answer the question with step-by-step reasoning.

Context: {context}

Question: {question}

Answer:"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful math tutor."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
    )
    return response.choices[0].message.content.strip()

# Entry point for answering questions
def get_answer(query, use_web=True):
    index = load_and_index_kb()
    docs = index.similarity_search(query)

    if docs and docs[0].page_content.strip():
        return run_llm_chain(query, docs)

    elif use_web:
        web_docs = web_search(query)
        if web_docs:
            return run_llm_chain(query, web_docs)
        else:
            return "No relevant content found on the web."

    else:
        return "No relevant content found in KB or web."

print("✅ rag_pipeline.py loaded successfully.")
