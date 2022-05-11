import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None  # default='warn'


def season_plot():
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

    winterPick.to_csv('./cleaned_data/winterpick.csv', index=False)
    antiWinter.to_csv('./cleaned_data/antiWinter.csv', index=False)

    f = plt.figure(figsize=(15, 8))
    plt.plot(winterPick.listed_month, winterPick.AVEprice, color='g')
    plt.plot(antiWinter.listed_month, antiWinter.AVEprice, color='r')
    plt.xticks(rotation=30)
    plt.show()
    f.savefig('./plots/car_season_plot.png')