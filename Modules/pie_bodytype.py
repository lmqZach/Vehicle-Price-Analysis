#plot pie chart of body types
#John Malgeri 2/23/2022

import csv
import matplotlib.pyplot as plt

possible_types = [                  #   all possible body types in csv
    'SUV / Crossover',      #0  -
    'Sedan',                #1  -
    'Coupe',                #2
    'Hatchback',            #3
    'Pickup Truck',         #4
    'Wagon',                #5
    'Minivan',              #6
    'Van',                  #7
    'Convertible',          #8
    ]

file = open('Cleaned10GB.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

type_counts = [0,0,0,0,0,0,0,0,0]       #   list to hold number of occurrences of each body type

for nextline in csvreader:              #   count occurrences of each body type and populate type_counts
    for i in range(len(possible_types)):
        if(nextline[3] == possible_types[i]):
            type_counts[i] = type_counts[i] + 1

fig1, ax1 = plt.subplots()
ax1.pie(type_counts, labels=possible_types, startangle=35)      #   plot
ax1.axis('equal')
plt.title('Car Body Types')
plt.show()
