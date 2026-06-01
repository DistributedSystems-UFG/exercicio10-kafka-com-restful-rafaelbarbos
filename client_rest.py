import requests

response = requests.get("http://localhost:5000/media")

if response.status_code == 200:
    print("Média recebida:", response.json()["media"])
else:
    print("Erro ao consultar API")
