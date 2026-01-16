import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def gerar_resposta(history):
    return client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=history,
        config=types.GenerateContentConfig(
            temperature=0.7,
            top_p=0.9,
            max_output_tokens=1024
        )
    )
