from datetime import datetime, timedelta
from flight_data import FlightData

import requests
from dotenv import dotenv_values

env_values = dotenv_values("../.env")


class FlightSearch:

    def __init__(self):
        self.base_url = 'https://api.tequila.kiwi.com/'
        self.headers = {
            'apikey': env_values.get("KIWI_FLIGHT_API_KEY")
        }

    def get_iata_code(self, city):
        url = self.base_url + 'locations/query'
        params = {
            'term': city,
            'location_types': 'city'
        }
        response = requests.get(url=url, params=params, headers=self.headers)
        return response.json()['locations'][0]['code']

    def search_flight(self, to_code):
        url = 'https://api.tequila.kiwi.com/v2/search'
        today = datetime.now()
        next_day = today + timedelta(days=(6*30))
        params = {
            'fly_from': 'LON',
            'fly_to': to_code,
            'date_from': today.strftime('%d/%m/%Y'),
            'date_to': next_day.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'flight_type': "round",
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'GBP'
        }

        response = requests.get(
            url=url,
            headers=self.headers,
            params=params,
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
