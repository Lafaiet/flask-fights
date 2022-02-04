from flask import Flask, request
from flask_restful import Api, Resource 

app = Flask(__name__)
api = Api(app)


flights_data = [

    {
        'number': 'LH1343',
        'number_passengers': 55,
        'origin': 'Tallinn',
        'destination': 'Berlin'
    },

]


class FlightsList(Resource):
    def get(self):
        return flights_data


api.add_resource(FlightsList, '/flights/')

if __name__ == '__main__':
    app.run(debug=True)