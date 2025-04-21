from flask import Flask, jsonify, request

app = Flask(__name__)

tarefas = []

def calc_imc(peso: float, altura: float):
    imc = peso / (altura * altura)
    return round(imc, 2)

def calc_tmb(perfil: str, peso: float, altura: float, idade: float):
    if perfil == "H":
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
        return tmb

@app.route('/')
def home():
    return 'Bem-vindo à API de tarefas!'

@app.route('/tarefas', methods=['GET'])
def listar_tarefas():
    return jsonify(tarefas)

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    descricao = request.json.get('descricao')
    nova_tarefa = {'id': len(tarefas) + 1, 'descricao': descricao}
    tarefas.append(nova_tarefa)
    return jsonify(nova_tarefa), 201

@app.route('/imc', methods=['POST'])
def calcular_imc():
    data = request.json
    peso = data.get('peso')
    altura = data.get('altura')
    
    if not peso or not altura:
        return jsonify({'erro': 'Peso e altura são obrigatórios.'}), 400
    
    try:
        imc = calc_imc(float(peso), float(altura))
        return jsonify({'imc': imc})
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
