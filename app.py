from flask import Flask, request


app = Flask(__name__)


@app.route('/hello/<int:id>', methods=['GET'])
def hello_with_number(id):
    return {'message': f'Hello world. Provided number was {id}'}

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')

    if name is None:
        return 'ops! Name is something', 400

    return {'message': f'Hello world. {name}'}


if __name__ == '__main__':
    app.run(debug=True)