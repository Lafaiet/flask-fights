from flask import Flask


app = Flask(__name__)


@app.route('/hello/<int:id>', methods=['GET'])
def hello_with_number(id):
    return {'message': f'Hello world. Provided number was {id}'}

@app.route('/hello', methods=['GET'])
def hello():
    return {'message': f'Hello world'}


if __name__ == '__main__':
    app.run(debug=True)