import pytest
from flask import Flask
from app import app  # Supondo que o código da API esteja no arquivo `app.py`

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Teste 1: Testar o cálculo do IMC
def test_calcular_imc(client):
    body_imc = {
        "peso": "70",
        "altura": "1.75"
    }
    
    response = client.post('/imc', json=body_imc)
    
    assert response.status_code == 200
    assert 'imc' in response.json
    assert response.json['imc'] == 22.86  # Calculando manualmente o IMC: 70 / (1.75 * 1.75)

# Teste 2: Testar o cálculo de TMB para o perfil masculino
def test_calcular_tmb_masculino(client):
    body_tmb = {
        "perfil": "H",
        "peso": "70",
        "altura": "1.75",
        "idade": "30"
    }
    
    response = client.post('/tmb', json=body_tmb)
    
    assert response.status_code == 200
    assert 'tmb' in response.json
    # Calculando manualmente a TMB para um homem: 88.362 + (13.397 * 70) + (4.799 * 1.75) - (5.677 * 30)
    assert response.json['tmb'] == 1742.057

# Teste 3: Testar a ausência de dados no IMC
def test_calcular_imc_erro(client):
    body_imc = {
        "peso": "70"
        # Falta a altura
    }
    
    response = client.post('/imc', json=body_imc)
    
    assert response.status_code == 400
    assert 'erro' in response.json
    assert response.json['erro'] == 'Peso e altura são obrigatórios.'

# Teste 4: Testar a ausência de dados no TMB
def test_calcular_tmb_erro(client):
    body_tmb = {
        "peso": "70",
        "altura": "1.75",
        "idade": "30"
        # Falta o perfil
    }
    
    response = client.post('/tmb', json=body_tmb)
    
    assert response.status_code == 400
    assert 'erro' in response.json
    assert response.json['erro'] == 'Peso, altura, idade e perfil (H ou M) são obrigatórios.'

# Teste 5: Testar a resposta de requisição inválida (método GET) para um endpoint POST
def test_metodo_invalido(client):
    response = client.get('/imc')
    
    assert response.status_code == 405  # Método não permitido
    assert 'erro' in response.json
    assert response.json['erro'] == 'Method Not Allowed'
