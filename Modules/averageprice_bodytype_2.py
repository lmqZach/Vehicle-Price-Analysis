# plot price vs month posted according to body type
# John Malgeri 2/23/2022

import csv
import matplotlib.pyplot as plt

WAVE = 'First Wave'  # uncomment desired wave to plot
# WAVE = 'Second Wave'

if (WAVE == 'First Wave'):
    possible_months = [  # all possible months in csv for covid first wave
        '2020-01',
        '2020-02',
        '2020-03',
        '2020-04',
        '2020-05'
    ]
elif (WAVE == 'Second Wave'):
    possible_months = [  # all possible months in csv for covid second wave
        '2020-06',
        '2020-07',
        '2020-08',
        '2020-09',
    ]

possible_types_2 = [  # all possible body types in csv
    'SUV / Crossover', 'Minivan',  # 0,1
    'Convertible', 'Coupe',  # 2,3
    'Hatchback', 'Wagon',  # 4,5
    'Pickup Truck', 'Van',  # 6,7
    'Sedan'  # 8
]

possible_types_3 = [  # all possible body types in csv, grouped for better visualization
    'SUV / Minivan',
    'Convertible / Coupe',
    'Hatchback / Wagon',
    'Pickup Truck / Van',
    'Sedan'
]


def stripdate(longdate):  # strips year-month from full date
    shortdate = ''
    for i in range(7):
        shortdate = shortdate + longdate[i]
    return shortdate


file = open('Cleaned10GB.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)

monthdata_lists = [[], [], [], [],
                   []]  # list of lists, grouped by car type, each list contains months for specified car type
pricedata_lists = [[], [], [], [],
                   []]  # list of lists, grouped by car type, each list contains prices for specified car type

averages_lists = []  # list of lists, grouped by car type, each list contains average price for specified car, grouped by year

for nextline in csvreader:  # populates monthdata_lists and pricedata_lists with lists of months and prices, grouped by type of car
    currentdate = stripdate(nextline[21])
    if (currentdate[2] == '2' and currentdate[3] == '0'):  # only true for 2020
        #   SUV / Minivan
        if ((nextline[3] == possible_types_2[0]) or (nextline[3] == possible_types_2[1])):
            if (float(nextline[29]) < 500000 and float(nextline[29]) > 500):  # ignore outliers
                monthdata_lists[0].append(currentdate)  # append date
                pricedata_lists[0].append(float(nextline[29]))  # append price
        #   Convertible / Coupe
        if ((nextline[3] == possible_types_2[2]) or (nextline[3] == possible_types_2[3])):
            if (float(nextline[29]) < 500000 and float(nextline[29]) > 500):  # ignore outliers
                monthdata_lists[1].append(currentdate)  # append date
                pricedata_lists[1].append(float(nextline[29]))  # append price
        #   Hatchback / Wagon
        if ((nextline[3] == possible_types_2[4]) or (nextline[3] == possible_types_2[5])):
            if (float(nextline[29]) < 500000 and float(nextline[29]) > 500):  # ignore outliers
                monthdata_lists[2].append(currentdate)  # append date
                pricedata_lists[2].append(float(nextline[29]))  # append price
        #   Pickup Truck / Van
        if ((nextline[3] == possible_types_2[6]) or (nextline[3] == possible_types_2[7])):
            if (float(nextline[29]) < 500000 and float(nextline[29]) > 500):  # ignore outliers
                monthdata_lists[3].append(currentdate)  # append date
                pricedata_lists[3].append(float(nextline[29]))  # append price
        #   Sedan
        if (nextline[3] == possible_types_2[8]):
            if (float(nextline[29]) < 500000 and float(nextline[29]) > 500):  # ignore outliers
                monthdata_lists[4].append(currentdate)  # append date
                pricedata_lists[4].append(float(nextline[29]))  # append price

for i in range(
        len(possible_types_3)):  # calculates average price per month for each body type and populates averages_lists with calculated averages
    temp1 = []  # list for one car type, each entry is average of prices for a particular year
    for j in range(len(possible_months)):  # once for every year
        temp_prices = []  # all prices for one year of one car type
        temp_prices.append(0)
        for k in range(
                len(monthdata_lists[i])):  # each item in monthdata_lists is list of years for a particular type of car
            if (possible_months[j] == monthdata_lists[i][k]):
                temp_prices.append(float(pricedata_lists[i][k]))

        current_average = 0.0
        if (len(temp_prices) > 1):
            current_average = sum(temp_prices) / (len(temp_prices) - 1)
        current_average = int(current_average)
        temp1.append(current_average)

    averages_lists.append(
        temp1)  # list, each entry is list for one car type, containing average price per year for that car type

for i in range(len(possible_types_3)):  # creates plot for each body type
    plt.plot(possible_months, averages_lists[i], label=possible_types_3[i])

plt.title('Average Price by Body Type, ' + WAVE)
plt.xlabel('Month Posted')
plt.ylabel('Average Price')
plt.legend(loc='upper right')
plt.show()
