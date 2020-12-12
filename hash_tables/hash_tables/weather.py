import random
import csv

#VARIABLES
weather_cast = {}
#FUNCTIONS
def printAllWeatherMonth():
    for key,value in weather_cast.items():
        print(key,":",value)
#*****CALCULATE AVERAGE FIRST WEEK************************
def calculate_average_firstWeek():
    total = 0
    TempList = list(weather_cast.values())
    for value in TempList[0:7]:
            total += int(value)
    return total/7
#****CALCULATE MAX IN TEN DAYS****************************
def calculate_MAX_in_ten_days():
    MAX = -1
    for value in weather_cast.values():
        MAX = max(MAX,int(value))
    return MAX
#****CALCULATE MAX IN TEN DAYS****************************
#****GET DAY TEMPERATURE**********************************
def get_day_temperature(day):
    return weather_cast[day]
#****READ THE CSV FILE OF THE MONTH JANUARY**********************************
with open('weatherFiles.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} was  {row[1]} degrees')
            weather_cast[row[0]] = row[1]
            line_count += 1
    print(f'Processed {line_count} lines.')
#CONSTRUCTION---ADD THE DATAS TO OUR DICTIONARY
printAllWeatherMonth()
print("Maximum in Ten Days is: ",calculate_MAX_in_ten_days())
print("The Average of the First 7 days is: ",calculate_average_firstWeek())
print(list(weather_cast.values())[0:7])



