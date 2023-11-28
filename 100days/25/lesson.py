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
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
