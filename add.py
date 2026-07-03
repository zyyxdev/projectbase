from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from datetime import datetime
import json

app = Flask(__name__)
app.secret_key = 'zyyx_base_project_2026'

USUARIOS = {
    'admin': {'senha': '123', 'nivel': 'admin', 'nome': 'Administrador'},
    'zyyx': {'senha': '123', 'nivel': 'user', 'nome': 'Zyyx'},
    'sniper': {'senha': '123', 'nivel': 'user', 'nome': 'Sniper'},
}

PRODUTOS = [
    {'id': 1, 'nome': 'CS2 Aimbot', 'icone': 'fa-crosshairs', 'preco': 49.90, 'desc': 'Aimbot profissional para CS2'},
    {'id': 2, 'nome': 'CS2 Wallhack', 'icone': 'fa-eye', 'preco': 39.90, 'desc': 'Veja através das paredes'},
    {'id': 3, 'nome': 'Standoff2 Pro', 'icone': 'fa-gamepad', 'preco': 29.90, 'desc': 'Aimbot + ESP para Standoff2'},
    {'id': 4, 'nome': 'PUBG Radar', 'icone': 'fa-map', 'preco': 59.90, 'desc': 'Radar 100% seguro para PUBG'},
]

USUARIOS_CADASTRADOS = [
    {'nome': 'zyyx', 'email': 'zyyx@mail.com', 'status': 'Ativo', 'assinatura': '12/2026'},
    {'nome': 'sniper', 'email': 'sniper@mail.com', 'status': 'Ativo', 'assinatura': '01/2027'},
    {'nome': 'ghost', 'email': 'ghost@mail.com', 'status': 'Inativo', 'assinatura': '08/2026'},
    {'nome': 'proplayer', 'email': 'pro@mail.com', 'status': 'Ativo', 'assinatura': '11/2026'},
    {'nome': 'hacker', 'email': 'hacker@mail.com', 'status': 'Ativo', 'assinatura': '09/2026'},
]

LOGS = [
    {'usuario': 'zyyx', 'acao': 'Login', 'data': '10/07 14:32', 'status': 'Sucesso'},
    {'usuario': 'sniper', 'acao': 'Compra', 'data': '10/07 13:10', 'status': 'Sucesso'},
    {'usuario': 'ghost', 'acao': 'Falha no login', 'data': '10/07 12:45', 'status': 'Falha'},
    {'usuario': 'proplayer', 'acao': 'Ativação', 'data': '10/07 11:22', 'status': 'Sucesso'},
    {'usuario': 'hacker', 'acao': 'Download', 'data': '10/07 10:05', 'status': 'Sucesso'},
]

NOTICIAS = [
    {'titulo': 'Novo cheat para CS2', 'data': '12/07/2026', 'texto': 'Wallhack e aimbot atualizados com suporte à nova versão.'},
    {'titulo': 'Promoção de aniversário', 'data': '11/07/2026', 'texto': '30% de desconto em todos os produtos por tempo limitado.'},
    {'titulo': 'Atualização Standoff 2', 'data': '10/07/2026', 'texto': 'Suporte completo à versão 0.39.1 do jogo.'},
]

TICKETS = [
    {'usuario': 'zyyx', 'assunto': 'Problema com ativação', 'status': 'Aberto', 'solucao': 'Reative sua licença no painel.'},
    {'usuario': 'sniper', 'assunto': 'Dúvida sobre pagamento', 'status': 'Fechado', 'solucao': 'Pagamento confirmado via PIX.'},
    {'usuario': 'ghost', 'assunto': 'Bug no menu', 'status': 'Aberto', 'solucao': 'Atualize o cliente para a versão mais recente.'},
]

carrinho = {}
tickets = []
ticket_id_counter = 1

@app.route('/')
def index():
    if 'usuario' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('usuario')
        senha = request.form.get('senha')
        if user in USUARIOS and USUARIOS[user]['senha'] == senha:
            session['usuario'] = user
            session['nivel'] = USUARIOS[user]['nivel']
            session['nome'] = USUARIOS[user]['nome']
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', erro='Usuário ou senha inválidos.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    dados = {
        'usuarios_ativos': 1284,
        'licencas_ativas': 342,
        'vendas_mes': 'R$ 4.560',
        'logs_hoje': 89,
    }
    return render_template('dashboard.html', dados=dados)

@app.route('/usuarios')
def usuarios():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('usuarios.html', usuarios=USUARIOS_CADASTRADOS)

@app.route('/remover_usuario/<int:index>')
def remover_usuario(index):
    if 'usuario' not in session or session.get('nivel') != 'admin':
        return redirect(url_for('login'))
    if 0 <= index < len(USUARIOS_CADASTRADOS):
        USUARIOS_CADASTRADOS.pop(index)
    return redirect(url_for('usuarios'))

@app.route('/logs')
def logs():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('logs.html', logs=LOGS)

@app.route('/loja')
def loja():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('loja.html', produtos=PRODUTOS)

@app.route('/carrinho')
def carrinho_view():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    user = session['usuario']
    items = carrinho.get(user, [])
    total = sum(p['preco'] for p in items)
    return render_template('carrinho.html', items=items, total=total)

@app.route('/adicionar_carrinho/<int:produto_id>')
def adicionar_carrinho(produto_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    user = session['usuario']
    produto = next((p for p in PRODUTOS if p['id'] == produto_id), None)
    if produto:
        if user not in carrinho:
            carrinho[user] = []
        carrinho[user].append(produto.copy())
    return redirect(url_for('loja'))

@app.route('/remover_carrinho/<int:produto_id>')
def remover_carrinho(produto_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    user = session['usuario']
    if user in carrinho:
        carrinho[user] = [p for p in carrinho[user] if p['id'] != produto_id]
    return redirect(url_for('carrinho_view'))

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    user = session['usuario']
    if request.method == 'POST':
        carrinho[user] = []
        return render_template('checkout.html', sucesso=True)
    items = carrinho.get(user, [])
    total = sum(p['preco'] for p in items)
    return render_template('checkout.html', items=items, total=total, sucesso=False)

@app.route('/noticias')
def noticias():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    return render_template('noticias.html', noticias=NOTICIAS)

@app.route('/suporte')
def suporte():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    user = session['usuario']
    nivel = session.get('nivel', 'user')
    if nivel == 'admin':
        lista = tickets
    else:
        lista = [t for t in tickets if t['usuario'] == user]
    return render_template('suporte.html', tickets=lista, nivel=nivel)

@app.route('/suporte/novo', methods=['GET', 'POST'])
def novo_ticket():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        assunto = request.form.get('assunto')
        mensagem = request.form.get('mensagem')
        if assunto and mensagem:
            global ticket_id_counter
            tickets.append({
                'id': ticket_id_counter,
                'usuario': session['usuario'],
                'assunto': assunto,
                'mensagem': mensagem,
                'status': 'Aberto',
                'respostas': []
            })
            ticket_id_counter += 1
            return redirect(url_for('suporte'))
    return render_template('novo_ticket.html')

@app.route('/suporte/<int:ticket_id>', methods=['GET', 'POST'])
def suporte_detalhe(ticket_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    if not ticket:
        return redirect(url_for('suporte'))
    user = session['usuario']
    nivel = session.get('nivel', 'user')
    if nivel != 'admin' and ticket['usuario'] != user:
        return redirect(url_for('suporte'))
    if request.method == 'POST' and nivel == 'admin':
        resposta = request.form.get('resposta')
        if resposta:
            ticket['respostas'].append({'admin': True, 'texto': resposta, 'data': datetime.now().strftime('%d/%m %H:%M')})
            if ticket['status'] == 'Aberto':
                ticket['status'] = 'Respondido'
        return redirect(url_for('suporte_detalhe', ticket_id=ticket_id))
    return render_template('suporte_detalhe.html', ticket=ticket, nivel=nivel)

@app.route('/suporte/fechar/<int:ticket_id>')
def fechar_ticket(ticket_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    if not ticket:
        return redirect(url_for('suporte'))
    user = session['usuario']
    nivel = session.get('nivel', 'user')
    if nivel != 'admin' and ticket['usuario'] != user:
        return redirect(url_for('suporte'))
    if ticket['status'] != 'Fechado':
        ticket['status'] = 'Fechado'
    return redirect(url_for('suporte_detalhe', ticket_id=ticket_id))

@app.route('/suporte/reabrir/<int:ticket_id>')
def reabrir_ticket(ticket_id):
    if 'usuario' not in session:
        return redirect(url_for('login'))
    ticket = next((t for t in tickets if t['id'] == ticket_id), None)
    if not ticket:
        return redirect(url_for('suporte'))
    user = session['usuario']
    nivel = session.get('nivel', 'user')
    if nivel != 'admin' and ticket['usuario'] != user:
        return redirect(url_for('suporte'))
    if ticket['status'] == 'Fechado':
        ticket['status'] = 'Aberto'
    return redirect(url_for('suporte_detalhe', ticket_id=ticket_id))

@app.route('/admin')
def admin():
    if 'usuario' not in session or session.get('nivel') != 'admin':
        return redirect(url_for('dashboard'))
    return render_template('admin.html', usuarios=USUARIOS_CADASTRADOS, logs=LOGS)

@app.route('/api/atividade')
def api_atividade():
    return jsonify([45, 60, 75, 90, 85, 70, 50])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)