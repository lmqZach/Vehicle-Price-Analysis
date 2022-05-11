# Necessary imports
import pandas as pd
import csv
import matplotlib.pyplot as plt

nrows = 1000000
df = pd.read_csv("./cleaned_data/Cleaned10GB.csv", low_memory=False, nrows=nrows)
df.shape
df = df[df["is_new"] == False]

datelist = df.listed_date.tolist()
newdate = []
for ele in datelist:
    temp = ele[0:7]
    newdate.append(temp)
df.insert(0, "listed_month", newdate, True)

from collections import Counter
cities = list(df['city'])
names=Counter(cities).keys() # equals to list(set(words)
#Counter(cities).values() # counts the elements' frequency

# set1 set2 set3 are 3 different brands in 3 different price ranges
set1, set2, set3 = pd.Series(dtype=object), pd.Series(dtype=object), pd.Series(dtype=object)
set1 = (df.franchise_make == 'Audi') & (df.year > 2019) & (df.price >=40000) &(df.listed_month != '2019-07')
set2 = (df.franchise_make == 'Ford') & (df.year > 2019) & (df.price<=40000) &(df.price>=20000)
set3 = (df.franchise_make == 'Hyundai') &(df.year > 2019) &(df.price<=20000)

# Group according to their listed month and evaluate the average price
high = df[set1].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price',aggfunc='mean'))
mid = df[set2].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price',aggfunc='mean'))
low = df[set3].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price',aggfunc='mean'))

high = high.reset_index()
mid = mid.reset_index()
low = low.reset_index()

f = plt.figure(figsize=(15, 6))

#plt.plot(np.unique(best.AVEprice), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.plot(mid.listed_month, mid.AVEprice,'-o', color = 'g',label = "Ford - Mid Range")
plt.plot(low.listed_month, low.AVEprice,'-o', color = 'b',label = "Hyundai - Low Range")
plt.plot(high.listed_month, high.AVEprice,'-o', color = 'r',label = "Audi - High Range")


plt.xticks(rotation=30)
plt.legend(loc='upper left')
plt.xlabel("Year-Month")
plt.ylabel("Price ($)")
plt.title("Trend in cost of used cars according to brand price ranges")
plt.ylim([5000,80000])
plt.show()

plt.savefig('Car_brands_vs_price.png')

"""Analysis according two impact of COVID-19"""

# set1 consists of cities with large number cases, set2 of cities with relatively less cases of COVID-19
set1, set2 = pd.Series(dtype=object), pd.Series(dtype=object)
set1 = ((df.city == 'New York') | (df.city == 'Boston')) & (df.price<=50000) &(df.year >= 2015)
#cond2 = (df.city == 'Boston') & (df.price<=50000)&(df.year >= 2019) 
set2 = ((df.city == 'Houston') | (df.city == "San Jose")) & (df.price<=50000)&(df.year >= 2015) & (df.listed_month != '2020-03')

high = df[set1].groupby('year').agg(AVEprice=pd.NamedAgg(column='price',aggfunc='mean'))
#others = df[cond2].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price',aggfunc='mean'))
low = df[set2].groupby('year').agg(AVEprice=pd.NamedAgg(column='price',aggfunc='mean'))

high = high.reset_index()
low = low.reset_index()

value = ['2016','2017','2018','2019','2020','2021']

f = plt.figure(figsize=(15, 6))

#plt.plot(np.unique(best.AVEprice), np.poly1d(np.polyfit(x, y, 1))(np.unique(x)))
plt.plot(high.year, high.AVEprice, color = 'r')
plt.plot(low.year, low.AVEprice, color = 'g')

#plt.plot(others.listed_month, others.AVEprice, color = 'g')
#plt.xticks(rotation=30)
plt.xticks(high.year,value)
plt.legend(["New York + Boston (More Affected)","Houston + San Jose (Less Affected)"],loc='upper right')
plt.xlabel("Year")
plt.ylabel("Price ($)")
plt.title("Trend in cost of used cars according to COVID-19 effect")
plt.ylim([5000,50000])
plt.show()

plt.savefig('Cities_affected_vs_price.png')

