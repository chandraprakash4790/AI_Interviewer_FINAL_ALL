
import os, ast
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class InterviewSession:
    def __init__(self):
        self.context = ""
        self.answers = []

    def ask(self):
        return "Please explain your project. Upload slides/audio or share screen."

    def add_context(self, text):
        self.context += "\n" + text

    def follow_up(self, answer):
        self.answers.append(answer)
        prompt = f"Ask a follow-up based on: {self.context}"
        try:
            r = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[{"role":"user","content":prompt}]
            )
            return r.choices[0].message.content
        except:
            return "Explain your architecture."

    def report(self):
        return {
            "Technical Depth": 8,
            "Clarity": 8,
            "Originality": 7,
            "Implementation": 8,
            "Confidence": 7
        }
