from flask import Flask, request
from flask_restful import Api, Resource, abort
import random
import requests
from copy import deepcopy

app = Flask(__name__)
api = Api(app)



flights_data = {

    1 : {
        'id': 1,
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

    2: {
        'id': 2,
        'number': 'LH123',
        'number_passengers': 55,
        'origin': 'Tallinn',
        'destination': 'Berlin',
        'departing_time': '2022/03/04 18:00',
        'arrival_time': '2022/03/04 22:00',
        'departing_airport': 'TTL airport',
        'arrival_airport': 'Berlin airport',
        'base_ticket_prices': {
            'economy': 34,
            'busines': 67
        }
    },

    3: {
        'id': 3,
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

}


def abort_if_flight_missing(flight_id):
    if flight_id not in flights_data:
        abort(404, message='No flight found with this id')


class FlightsList(Resource):
    def get(self):
        return flights_data
    
    def post(self):
        new_flight = request.json
        flight_id = random.randint(4, 100000000) # this can generate repeated ids!!!!!
        new_flight['id'] = flight_id

        flights_data[flight_id] = new_flight

        return new_flight, 201
        
    

class Flight(Resource):
    def get(self, flight_id):
        abort_if_flight_missing(flight_id)

        flight = flights_data[flight_id]

        return flight
    
    def put(self, flight_id):
        data = request.json
        flights_data[flight_id] = data

        return data


class FlightUSD(Resource):
    def get(self, flight_id):
        abort_if_flight_missing(flight_id)

        resp = requests.get('https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/eur.json')
        currency_rates = resp.json()
        eur_usd = currency_rates['eur']['usd']

        flight = flights_data[flight_id]

        flight_usd = deepcopy(flight)

        flight_usd['base_ticket_prices']['economy'] = flight_usd['base_ticket_prices']['economy'] * eur_usd
        flight_usd['base_ticket_prices']['busines'] = flight_usd['base_ticket_prices']['busines'] * eur_usd
           

        return flight_usd
    


api.add_resource(FlightsList, '/flights/')
api.add_resource(FlightUSD, '/flights/usd/<int:flight_id>')
api.add_resource(Flight, '/flights/<int:flight_id>')


if __name__ == '__main__':
    app.run(debug=True)