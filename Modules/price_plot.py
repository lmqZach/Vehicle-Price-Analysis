import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_csv("./cleaned_data/Cleaned10GB.csv", nrows=1000000, low_memory=False)
print(df.shape)

# pick only used cars
df = df[df["is_new"] == False]

# remove columbus
df1 = df.drop(['power', 'width', 'transmission_display', 'savings_amount', 'vin', 'latitude',
               'maximum_seating', 'longitude', 'length', 'back_legroom', 'Unnamed: 0', 'city',
               'city_fuel_economy', 'dealer_zip', 'engine_type', 'franchise_dealer', 'fuel_tank_volume',
               'front_legroom', 'fuel_type', 'height', 'highway_fuel_economy'], axis=1)

# remove NaN price
df2 = df1.dropna(axis=0, subset=['price', 'listed_date', 'salvage', 'theft_title'])

# pick price range above 3000
df3 = df2.loc[df2['price'] >= 5000]

# pick the data after 09/01/2019
df4 = df3.loc[df3.listed_date >= "2019-12-01"]
print(df4.shape)
print(df4.head())
# add a short format of date (only by 1/3 month)
datelist = df4.listed_date.tolist()
newdate = []
for ele in datelist:
    temp = ele[0:7]
    newdate.append(temp)
# df4['listed_date'] = newdate
df4.insert(0, "listed_month", newdate, True)
# SUV/AWD cars vs coupe/ convertible
df5 = df3.loc[df3.listed_date >= "2019-05-01"]

datelist = df5.listed_date.tolist()
newdate = []
for ele in datelist:
    temp = ele[0:7]
    newdate.append(temp)
# df4['listed_date'] = newdate
df5.insert(0, "listed_month", newdate, True)

cond1, cond2 = pd.Series(dtype=object), pd.Series(dtype=object)
cond1 = (df5.body_type == 'SUV / Crossover') | (df5.body_type == 'Pickup Truck') | (
            df5.wheel_system_display == 'All-Wheel Drive') | (df5.wheel_system_display == 'Four-Wheel Drive')
cond2 = (df5.body_type == 'Coupe') | (df5.wheel_system_display == 'Front-Wheel Drive') | (
            df5.wheel_system_display == 'Rear-Wheel Drive')
print(sum(cond1))
print(sum(cond2))

winterPick = df5[cond1].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price', aggfunc='mean'))
antiWinter = df5[cond2].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price', aggfunc='mean'))

winterPick = winterPick.reset_index()
antiWinter = antiWinter.reset_index()

winterPick.to_csv('winterpick.csv', index=False)
antiWinter.to_csv('antiWinter.csv', index=False)


def date_bar_plot():
    aveTime = df5.groupby('listed_month').agg(AVEtime=pd.NamedAgg(column='daysonmarket', aggfunc='mean'))
    aveTime = aveTime.reset_index()
    print(aveTime)

    f = plt.figure(figsize=(10, 6))
    plt.bar(aveTime.listed_month, aveTime.AVEtime)
    f.savefig('./plots/tenGB_date_price_bar.png')


def ten_GB_month_plot():
    # better conditioned cars vs most commomly used cars
    cond1, cond2, cond3 = pd.Series(dtype=object), pd.Series(dtype=object), pd.Series(dtype=object)
    cond1 = (df4.price > 50000) & (df4.mileage <= 35000) & (df4.year >= 2016) & (df4.owner_count <= 3) & (
            df4.salvage == False) & (df4.theft_title == False)
    cond2 = (df4.price <= 50000) & (df4.mileage <= 35000) & (df4.year >= 2016) & (df4.owner_count <= 3) & (
            df4.salvage == False) & (df4.theft_title == False)
    cond3 = df4.price >= 5000

    """print(sum(cond1))
    print(sum(cond2))
    print(sum(cond3))"""

    best = df4[cond1].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price', aggfunc='mean'))
    better = df4[cond2].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price', aggfunc='mean'))
    comm = df4[cond3].groupby('listed_month').agg(AVEprice=pd.NamedAgg(column='price', aggfunc='mean'))

    best = best.reset_index()
    better = better.reset_index()
    comm = comm.reset_index()

    better.to_csv('better.csv', index=False)
    comm.to_csv('common.csv', index=False)

    f = plt.figure(figsize=(10, 6))
    # plt.plot(best.listed_month, best.AVEprice, color = 'r')
    plt.plot(better.listed_month, better.AVEprice, color='g')
    plt.plot(comm.listed_month, comm.AVEprice, color='b')
    plt.xticks(rotation=30)
    plt.show()
    f.savefig("./plots/tenGB_month_price_line.png")


def accident_condition_plot():
    accidentFree = df4[df4.has_accidents == False].groupby('listed_month').agg(
        AVEprice=pd.NamedAgg(column='price', aggfunc='mean'))
    accidentCar = df4[df4.has_accidents == True].groupby('listed_month').agg(
        AVEprice=pd.NamedAgg(column='price', aggfunc='mean'))

    accidentFree = accidentFree.reset_index()
    accidentCar = accidentCar.reset_index()

    accidentFree.to_csv('noA.csv', index=False)
    accidentCar.to_csv('Acci.csv', index=False)

    f = plt.figure(figsize=(10, 6))
    plt.plot(accidentCar.listed_month, accidentCar.AVEprice)
    plt.plot(accidentFree.listed_month, accidentFree.AVEprice)
    plt.xticks(rotation=30)
    plt.show()
    f.savefig("./plots/accident_condition.png")


def ten_GB_correlation():
    f = plt.figure(figsize=(19, 15))
    plt.matshow(df.corr(), fignum=f.number)
    plt.xticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14,
               rotation=45)
    plt.yticks(range(df.select_dtypes(['number']).shape[1]), df.select_dtypes(['number']).columns, fontsize=14)
    cb = plt.colorbar()
    cb.ax.tick_params(labelsize=14)
    plt.title('Correlation Matrix', fontsize=16)
    f.savefig("./plots/correlation.png")
