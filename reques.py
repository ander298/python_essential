import requests

texto = None
try:
    requisição = requests.get("https://g1.globo.com/")
    texto = requisição.text
except Exception as e:
    print("Deu erro", e)
    exit()

print(texto)
