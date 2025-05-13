import requests
import os
from google import genai


def get_code_snippet_requests(model="gemini-2.0-flash", prompt=None):

    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={os.getenv('API_KEY')}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Errore {response.status_code}: {response.text}")


def get_code_snippet(model="gemini-2.0-flash", prompt=None):
    client = genai.Client(api_key=os.getenv('API_KEY'))

    response = client.models.generate_content(
        model=model,
        contents=f"Sei un esperto sviluppatore Python, mi serve la parte mancante del seguente codice python: {prompt}",
    )

    print(response.text)


get_code_snippet(prompt="print('ciao mondo)")
