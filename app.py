import os
import requests
import gradio as gr
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")

# קריאה מהקובץ prompt.txt
with open("prompt.txt", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

def generate_command(user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    return result["choices"][0]["message"]["content"].strip()

iface = gr.Interface(
    fn=generate_command,
    inputs="text",
    outputs="text",
    title="Natural Language → CLI"
)

iface.launch()