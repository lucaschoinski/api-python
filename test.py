import requests

url = "http://127.0.0.1:5000"

url = "http://127.0.0.1:5000/imc"

body_imc = {
    "peso": "50",
    "altura": "1.70"
}

body_tmb = {
    "perfil": "H",
    "peso": "50",
    "altura": "1.60",
    "idade": "45"
}

# Envia a requisição POST com o JSON
resposta_tmb = requests.post(url + '/tmb', json=body_tmb)
# Envia a requisição POST com o JSON
resposta_imc = requests.post(url + '/imc', json=body_imc)

# Verifica se a requisição foi bem-sucedida
if resposta_imc.status_code == 200:
    print('IMC calculado:', resposta_imc.json()['imc'])
else:
    print('Erro:', resposta_imc.json())

if resposta_tmb.status_code == 200:
    print('TMB calculado:', resposta_tmb.json()['tmb'])
else:
    print('Erro:', resposta_tmb.json())


