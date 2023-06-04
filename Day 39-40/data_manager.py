import requests
from dotenv import dotenv_values


class DataManager:
    def __init__(self):
        self.url = 'https://api.sheety.co/dba10091bfc1ae6449190f47dae2f0a5/flightDeals/prices'
        self.env_values = dotenv_values("../.env")
        self.headers = {
            'Authorization': 'Bearer ' + self.env_values.get("SHEETY_TOKEN"),
            "Content-Type": "application/json"
        }

    def get_flight_info(self):
        response = requests.get(url=self.url, headers=self.headers)
        return response.json()

    def change_flight_info(self, _id, data):
        url = self.url + '/' + _id
        new_data = {'price': data}
        response = requests.put(url=url, json=new_data, headers=self.headers)
        return response.text
