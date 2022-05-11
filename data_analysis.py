import matplotlib
import csv
from Modules.sns_plots import sns_plot_line_picture_by_day
from Modules.utils import sns_figure_plot_bar, compute_max, compute_average
from data_cleaning import get_cleaned_data_list, get_all_list


matplotlib.use('TkAgg')
file_path = "./raw_data/vehicles.csv"

all_list = get_all_list()
data_list = get_cleaned_data_list()
brand_index = all_list[0].index('manufacturer')
price_index = all_list[0].index('price')
post_time_index = all_list[0].index('posting_date')
region_index = all_list[0].index('region')
region_url_index = all_list[0].index('region_url')
lat_index = all_list[0].index('lat')
long_index = all_list[0].index('long')

car_brands = []
for data in data_list:
    car_brands.append(data[brand_index])
no_repeat_car_brands = list(set(car_brands))
print(no_repeat_car_brands)

regions = []
for data in data_list:
    regions.append(data[region_index])
no_repeat_regions = list(set(regions))

price_map = {}
all_price_map = {}
for region in no_repeat_regions:
    price_map[region] = 0
    all_price_map[region] = []
for data in data_list:
    price = int(data[price_index])
    region = data[region_index]
    old_price = price_map[region]
    price_map[region] = old_price + price
    all_price_map[region].append(price)
average_price_map = {}
for region in all_price_map:
    average_price_map[region] = sum(all_price_map[region]) / len(all_price_map[region])


sorted_price_map = sorted(price_map.items(), key=lambda item: item[1], reverse=True)
sorted_average_price_map = sorted(average_price_map.items(), key=lambda item: item[1], reverse=True)
print("------------price---------------")
print(sorted_price_map)
print("-------------average_price-----------------")
print(sorted_average_price_map)

top_10_sum_regions = []
top_10_average_regions = []
top_10_sum_prices = []
top_10_average_prices = []

num = 0
for region in sorted_price_map:
    num = num + 1
    if num > 10:
        break
    top_10_sum_regions.append(region[0])
    top_10_sum_prices.append(region[1])

num = 0
for region in sorted_average_price_map:
    num = num + 1
    if num > 10:
        break
    top_10_average_regions.append(region[0])
    top_10_average_prices.append(region[1])


sns_figure_plot_bar(top_10_sum_regions, top_10_sum_prices, "sum-price vs region")
sns_figure_plot_bar(top_10_average_regions, top_10_average_prices, "average-price vs region")

first_wave = []
second_wave = []
for data in data_list:
    if data[post_time_index] == "":
        continue
    time = data[post_time_index].split('T')
    time_str = time[0]
    month = time_str.split('-')[1]
    if month == "04":
        first_wave.append(data)
    if month == "05":
        second_wave.append(data)

low_level = ['volkswagen', 'saturn', 'mini', 'datsun', 'pontiac', 'fiat']
mid_level = ['ford', 'jeep', 'lincoln', 'mazda', 'toyota', 'cadillac', 'infiniti', 'hyundai',
             'buick', 'alfa-romeo', 'subaru', 'nissan', 'chevrolet', 'volvo', 'chrysler',
             'mitsubishi', 'honda', 'ram', 'acura', 'gmc', 'dodge', 'kia', 'jaguar']
high_level = ['bmw', 'aston-martin', 'mercury', 'porsche', 'morgan', 'mercedes-benz',
              'lexus', 'audi', 'harley-davidson', 'ferrari', 'tesla', 'land rover', 'rover']
low_level_list = []
mid_level_list = []
high_level_list = []
for data in data_list:
    price = int(data[price_index])
    if 5000 <= price <= 20000:
        low_level_list.append(data)
    if 20000 <= price <= 40000:
        mid_level_list.append(data)
    if price > 40000:
        high_level_list.append(data)

compute_max(first_wave, price_index)
compute_average(first_wave, price_index)

compute_max(second_wave, price_index)
compute_average(second_wave, price_index)
all_list = low_level_list + mid_level_list + high_level_list
# sns_plot_line_picture_by_day(low_level_list, 'low level', post_time_index, price_index)
# sns_plot_line_picture_by_day(mid_level_list, 'mid level', post_time_index, price_index)
sns_plot_line_picture_by_day(high_level_list, 'High end', post_time_index, price_index)
sns_plot_line_picture_by_day(all_list, 'All level', post_time_index, price_index)

# sns_plot_line_picture_by_day(first_wave, 'first wave', post_time_index, price_index)
# sns_plot_line_picture_by_day(second_wave, 'second wave', post_time_index, price_index)
