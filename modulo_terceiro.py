import requests

url = "https://www.example.com"
response = requests.get(url)

print(f"Solicitando HTTP para {url} retornou o status {response.status_code}")