from data_manager import DataManager
from flight_search import FlightSearch

data = DataManager()
# print(data.get_flight_info())
flight = FlightSearch()

sheet_data = [{'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 2}, {'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 3}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 4}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 5}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 6}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 7}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 8}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 9}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 10}]

for index, item in enumerate(sheet_data):
    if not item.get('iataCode'):
        iata = flight.get_iata_code(item['city'])
        new_data = {'iataCode': iata}
        sheet_data[index].update({'iataCode': iata})
        # data.change_flight_info(str(item['id']), new_data)

for item in sheet_data:
    new_flight = flight.search_flight(item['iataCode'])
