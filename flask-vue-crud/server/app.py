import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Rapido e devagar',
        'author': 'Daniel Kahneman',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter e a pedra\ Filosofal',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'O poder do Habito',
        'author': 'Charles Duhigg',
        'read': True
    }
]

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'Titulo': post_data.get('title'),
            'Autor': post_data.get('author'),
            'Lido': post_data.get('read')
        })
        response_object['message'] = 'Livro Adicionado!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'Titulo': post_data.get('title'),
            'Autor': post_data.get('author'),
            'Lido': post_data.get('read')
        })
        response_object['message'] = 'Livro Atualizado!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Livro Removido!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
