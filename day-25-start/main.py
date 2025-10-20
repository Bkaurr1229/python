# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)


import pandas
import pandas as pd
from pandas import read_csv
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrels)

