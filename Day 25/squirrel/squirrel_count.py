import pandas

data = pandas.read_csv("../Central_Park_Squirrel_Data.csv")

data_dict = {"Fur Color": [], "Count": []}

for color in ['Black', 'Gray', 'Cinnamon']:
    squirrel_count = data[data['Primary Fur Color'] == color].shape[0]
    data_dict["Fur Color"].append(color)
    data_dict["Count"].append(squirrel_count)

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("squirrel_count.csv")
