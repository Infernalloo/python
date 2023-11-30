import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
grey = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Cinnamon", "Grey", "Black"],
    "Count": [cinnamon, grey, black],
}

# print(data_dict)
new_dataframe = pandas.DataFrame(data_dict)
new_dataframe.to_csv("Fur Color")

