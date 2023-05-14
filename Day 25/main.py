# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(data)

# import csv

# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = [int(row[1]) for row in data if row[1] != 'temp']
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = data["temp"].mean()
# print(round(average, 2))
# maximum = data["temp"].max()
# print(maximum)
# print(data["condition"])
# print(data.condition)
# print(data[data.day == "Monday"])
# print(data[data.temp == data["temp"].max()])
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
#
# monday_fahr_temp = monday_temp * 9/5 + 32
# print(monday_fahr_temp)

# data_dict = {
#     "students": ["Amy", "James", "Amgela"],
#     "scores": [76, 56, 65]
# }
#
# new_data = pandas.DataFrame(data_dict)
# print(new_data)
# data.to_csv("new_data.csv")
