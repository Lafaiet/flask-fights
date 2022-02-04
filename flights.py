from flask import Flask, request
from flask_restful import Api, Resource 


app = Flask(__name__)
api = Api(app)



flights_data = [

    {
        'number': 'LH123',
        'number_passengers': 55,
        'origin': 'Tallinn',
        'destination': 'Berlin',
        'departing_time': '2022/02/04 18:00',
        'arrival_time': '2022/02/04 22:00',
        'departing_airport': 'TTL airport',
        'arrival_airport': 'Berlin airport',
        'base_ticket_prices': {
            'economy': 100,
            'busines': 200
        }
    },

    {
        'number': 'TY323',
        'number_passengers': 65,
        'origin': 'Rio de Janeiro',
        'destination': 'Paris',
        'departing_time': '2022/05/07 18:00',
        'arrival_time': '2022/02/04 22:00',
        'departing_airport': 'TTL airport',
        'arrival_airport': 'Berlin airport',
        'base_ticket_prices': {
            'economy': 54,
            'busines': 76
        }
    },

]


class FlightsList(Resource):
    def get(self):
        return flights_data


api.add_resource(FlightsList, '/flights/')

if __name__ == '__main__':
    app.run(debug=True)