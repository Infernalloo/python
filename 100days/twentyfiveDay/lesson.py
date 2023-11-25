# import csv
#
# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# temp_avg = sum(temp_list) / len(temp_list)
# print(round(temp_avg, 2))

# print(data["temp"].mean())
# print(data["temp"].max())

# Get data in row
# print(data[data["day"] == "Monday"])

# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp
# temp_convert = round((monday_temp * (9/5)) + 32)
# print(temp_convert)

# Create a dataframe from scratch

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")

