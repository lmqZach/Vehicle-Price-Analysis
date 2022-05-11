# data cleaning
import matplotlib
import csv

file_path = "./raw_data/vehicles.csv"


def get_all_list():
    all_list = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            all_list.append(row)
    return all_list


def get_cleaned_data_list():
    all_list = []
    data_list = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        print(type(reader))
        for row in reader:
            all_list.append(row)
    print(all_list[0])
    data_list = all_list[1:]
    no_null_data_list = []
    brand_index = all_list[0].index('manufacturer')
    price_index = all_list[0].index('price')
    post_time_index = all_list[0].index('posting_date')
    region_index = all_list[0].index('region')
    region_url_index = all_list[0].index('region_url')
    lat_index = all_list[0].index('lat')
    long_index = all_list[0].index('long')
    for data in data_list:
        if data[price_index] == '0' or data[post_time_index] == '' or data[region_index] == '':
            continue
        price = int(data[price_index])
        if price > 400000 or price < 1000:
            continue
        no_null_data_list.append(data)
    data_list = no_null_data_list
    return data_list


cleaned_data_list = get_cleaned_data_list()
file = open("./cleaned_data/cleanedData.txt", 'w+')
for data in cleaned_data_list:
    file.write(str(data))
    file.write("\n")
file.close()
