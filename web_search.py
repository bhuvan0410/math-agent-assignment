import os
import requests
from dotenv import load_dotenv
from langchain.docstore.document import Document as LangchainDocument

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")

def web_search(query: str, max_results: int = 3):
    try:
        url = "https://google.serper.dev/search"
        headers = {
            "X-API-KEY": SERPER_API_KEY,
            "Content-Type": "application/json"
        }
        payload = {
            "q": query,
            "num": max_results
        }

        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        results = response.json()

        if "organic" not in results:
            return []

        contents = [item["snippet"] for item in results["organic"] if "snippet" in item]
        combined = "\n".join(contents)
        return [LangchainDocument(page_content=combined)] if combined else []

    except Exception as e:
        print(f"Web search failed: {e}")
        return []
