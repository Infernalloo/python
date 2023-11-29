# csv is used for tabula data
# comma separated value

# Open the file and make every line into a list
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# Open the file, read the file and for every row
# we append every item at index 1 that is not "temp"
# import csv
# with open("weather_data.csv") as data_file:
#     # created an object
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data frame is equivalent to the full table
# series is equivalent to column of a table
data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

data_temp = data["temp"].to_list()
# print(data_temp)

avg_temp = data["temp"].mean()
# print(round(avg_temp))

maximum_temp = data["temp"].max()
# print(maximum_temp)

# Get data from columns
# data["temp"]
# data.temp

# Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# Get a value from a row
monday = data[data.day == "Monday"]
# print(monday.condition)
temp_farh = (monday.temp * (9/5)) + 32
# print(temp_farh)

# Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")
