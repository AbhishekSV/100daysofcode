from os import sys, path
# import csv
import pandas

# # Work with python files to view the csv data
# with open (path.join(sys.path[0], "Data/weather_data.csv"), "r") as weather_data:
#     weather_list = weather_data.readlines()
# print(weather_list)

# # Work with python csv module to view the csv data
# with open (path.join(sys.path[0], "Data/weather_data.csv"), "r") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

# # Work with pandas
# data = pandas.read_csv(path.join(sys.path[0], "Data/weather_data.csv"))
# print(data)
# print(data['temp'])

# temp_list = data['temp'].to_list()
# avg_of_temps = round(sum(temp_list) / len(temp_list),2)
# print(avg_of_temps)

# print(data['temp'].mean())
# print(data['temp'].max())

# # Get data in a column
# print(data['temp'])
# print(data.temp)

# # Get data in a row
# print(data[data.day == "Monday"])
# for row in data.iterrows():
#     print(row)

# # Get row data with max temperature
# print(data[data.temp == data.temp.max()])

# # Convert temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# print((monday.temp * 1.8) + 32)

# # Create dataframes from scratch
# data_dict = {
#     "students": ["Amy", "James", "Jack"],
#     "scores": [76, 65, 54]
#     }
# data_frame = pandas.DataFrame(data_dict)
# data._to_csv(data_frame)

# Squirrel data challenge
data = pandas.read_csv(path.join(sys.path[0], "Data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"))

gray_squrriels_count = len(data[data['Primary Fur Color'] == "Gray"])
red_squrriels_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
black_squrriels_count = len(data[data['Primary Fur Color'] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squrriels_count, red_squrriels_count, black_squrriels_count]
    }

df = pandas.DataFrame(data_dict)
df.to_csv(path.join(sys.path[0], "Data/squirrel_count.csv"))

# fur_list = data['Primary Fur Color']
#print(fur_list.unique())
# df = fur_list.value_counts()
# df.to_csv(path.join(sys.path[0], "Data/squirrel_count.csv"))