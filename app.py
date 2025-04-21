from flask import Flask, jsonify, request

app = Flask(__name__)


tarefas = []

def calc_imc(peso: float, altura: float):
    imc = peso / (altura * altura)
    return round(imc, 2)

def calc_tmb(perfil: str, peso: float, altura: float, idade: int):
    if perfil == "H":
        tmb = 88.362 + (13.397 * peso) + (4.799 * altura) - (5.677 * idade)
    if perfil == "M":
        tmb = 447.593 + (9.247 * peso) + (3.098 * altura) - (4.330 * idade)

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

@app.route('/tmb', methods=['POST'])
def calcular_tmb():
    data = request.json
    peso = data.get('peso')
    altura = data.get('altura')
    idade = data.get('idade')
    perfil = data.get('perfil')
    
    if not peso or not altura or not idade or not perfil:
        return jsonify({'erro': 'Peso, altura, idade e perfil (H ou M) são obrigatórios.'}), 400
    
    try:
        tmb = calc_tmb(str(perfil), float(peso), float(altura), int(idade))
        return jsonify({'tmb': tmb})
    except Exception as e:
        return jsonify({'erro': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
