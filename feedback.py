# feedback.py

import os
import json

FEEDBACK_FILE = "feedback_data.json"

def load_feedback():
    """Load feedback data from a JSON file."""
    if not os.path.exists(FEEDBACK_FILE):
        return []
    with open(FEEDBACK_FILE, "r") as file:
        return json.load(file)

def save_feedback(question, ai_answer, feedback_text, user_correction=None):
    """Save feedback data to a JSON file."""
    feedback_entry = {
        "question": question,
        "ai_answer": ai_answer,
        "feedback": feedback_text,
        "user_correction": user_correction
    }
    data = load_feedback()
    data.append(feedback_entry)
    with open(FEEDBACK_FILE, "w") as file:
        json.dump(data, file, indent=4)

def display_feedback_summary():
    """Optional: Display past feedback entries (for internal inspection)."""
    data = load_feedback()
    return data[-5:]  # return the last 5 feedback entries
