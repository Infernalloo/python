import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_color = data["Primary Fur Color"]

cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])

print(cinnamon)
print(gray)
print(black)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}

data_frame = pandas.DataFrame(data_dict)
data_frame.to_csv("Fur Color")
