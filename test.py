import requests


url = "http://127.0.0.1:5000/imc"

body = {
    "peso": "50",
    "altura": "1.70"
}

# Envia a requisição POST com o JSON
resposta = requests.post(url, json=body)

# Verifica se a requisição foi bem-sucedida
if resposta.status_code == 200:
    print('IMC calculado:', resposta.json()['imc'])
else:
    print('Erro:', resposta.json())