from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route('/hello/<int:id>', methods=['GET'])
def hello_with_number(id):
    return {'message': f'Hello world. Provided number was {id}'}

@app.route('/hello', methods=['GET', 'POST'])
def hello():

    if request.method == 'POST':
        data = request.json

        secret_password = 'superSecret'

        if data['password'] != secret_password:
            return {'message': 'wrong password!'}, 401

        return {'message': 'This was a post request'}

    
    if request.method == 'GET':
        name = request.args.get('name')

        if name is None:
            return {'message': 'ops! Name is something'}, 400

        messages = [
            {'message': f'Hello {name}'},
            {'message': f'This is my awesome restapi'}
        ]

        return jsonify(messages)


if __name__ == '__main__':
    app.run(debug=True)