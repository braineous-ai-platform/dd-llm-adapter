# prototyping llm integration and studying response drift

import json
import urllib.request


def generate_with_ollama(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "stream": False,
        "prompt": prompt
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        url=url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")

    return body


def generate_with_ollama_json(prompt, model="llama3"):
    url = "http://localhost:11434/api/generate"

    payload = {
        "model": model,
        "stream": False,
        "prompt": prompt
    }

    data = json.dumps(payload).encode("utf-8")

    request = urllib.request.Request(
        url=url,
        data=data,
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        body = response.read().decode("utf-8")

    return json.loads(body)


# ------driver---------------------
response = generate_with_ollama("Why is the sky blue?")
print(response)

print("*" * 15)

response = generate_with_ollama_json("Why is the sky blue?")
print(response["response"])
