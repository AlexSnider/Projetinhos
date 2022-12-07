# # Itens de uma API:
# # 1. Objetivo;
#     - Criar uma api que disponibiliza a consulta, criação, edição e exclusão de livros.
# # 2. URL base;
#     - localhost
# # 3. Endpoints;
#     - localhost/livros (GET)
#     - localhost/livros/id (POST)
#     - localhost/livros/id (GET)
#     - localhost/livros/id (PUT)
#     - localhost/livros (DELETE)
# # 4. Quais recursos.
#     - livros

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'O senhor dos aneis - a sociedade do anel',
        'autor': 'J.R.R Tolkien'
    },
    {
        'id': 2,
        'titulo': 'harry potter e a pedra filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'james clear',
        'autor': 'habitos atomicos'
    },
]

# Consultar (todos)
@app.route('/livros')
def obter_livros():
    return jsonify(livros)
# Consultar (id)
# Editar
# Excluir
app.run(port=5000, host='localhost', debug=True)
