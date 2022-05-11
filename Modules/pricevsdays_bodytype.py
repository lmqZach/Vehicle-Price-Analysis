#plot price vs days on market according to body type
#John Malgeri 2/23/2022

import csv
import matplotlib.pyplot as plt

#Desired body type (use one of the values in possible_types)
TYPE = 'Hatchback'

possible_types = [
    'SUV / Crossover',      #0  -
    'Sedan',                #1  -
    'Coupe',                #2
    'Hatchback',            #3
    'Pickup Truck',         #4
    'Wagon',                #5
    'Minivan',              #6
    'Van',                  #7
    'Convertible',          #8
    '']                     #9  empty, disregard
type_index = possible_types.index(TYPE)

file = open('Cleaned10GB.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

daysonmarket = []
prices = []

for nextline in csvreader:              #   populate lists from csv
    if(nextline[3] == TYPE):                #   appends only if body_type is same as chosen type
        if(float(nextline[29]) < 500000):           #   ignore outliers
            daysonmarket.append(int(nextline[6]))   #   append while typecasting for plt
            prices.append(int(float(nextline[29])))      #   append while typecasting for plt

plt.plot(daysonmarket, prices, 'bo')  #   plot
plt.title(TYPE)
plt.xlabel('Days on Market')
plt.ylabel('Price')
plt.show()
