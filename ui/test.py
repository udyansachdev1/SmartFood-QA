import requests

API_URL = (
    "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
)
headers = {"Authorization": "Bearer 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"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query(
    {
        "inputs": "How does it taste tiramisu",
    }
)
print("Response:" + output)
