# utils.py

import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get API key from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not set in .env file")

# Common constants
CHUNK_SIZE = 300
CHUNK_OVERLAP = 50

# Sample helper: get absolute path to a knowledge base file
def get_kb_file_path(filename):
    return os.path.join("kb", filename)
