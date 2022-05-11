import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from pandas import DataFrame

from Modules.utils import date2time, compute_average_data

matplotlib.use('TkAgg')


def plot_picture_by_day(ls, name_prefix, post_time_index, price_index):
    posting_time = []
    time_index_map = {}
    time_price_map = {}
    int_to_date_map = {}
    for data in ls:
        time = data[post_time_index].split('T')
        time_str = time[0]
        time_stamp = date2time(time_str, '%Y-%m-%d')
        if time_stamp not in int_to_date_map:
            int_to_date_map[time_stamp] = time_str

        if time_stamp not in posting_time:
            posting_time.append(time_stamp)
        time_index_map[time_stamp] = data[post_time_index]
        if time_stamp not in time_price_map:
            time_price_map[time_stamp] = [int(data[price_index])]
        else:
            time_price_map[time_stamp].append(int(data[price_index]))
    posting_time.sort()
    time_date = []
    for value in posting_time:
        time_date.append(int_to_date_map[value])
    price = []
    for data_index in posting_time:
        price.append(compute_average_data(time_price_map[data_index]))
    fig = plt.figure()
    plt.plot(time_date, price)
    plt.title(name_prefix)
    plt.show()
    file_name = name_prefix + "_vs_price.png"
    fig.savefig('./plots/' + file_name)


def sns_plot_picture_by_day(ls, name_prefix, post_time_index, price_index):
    posting_time = []
    time_index_map = {}
    time_price_map = {}
    int_to_date_map = {}
    for data in ls:
        time = data[post_time_index].split('T')
        time_str = time[0]
        time_stamp = date2time(time_str, '%Y-%m-%d')
        if time_stamp not in int_to_date_map:
            int_to_date_map[time_stamp] = time_str

        if time_stamp not in posting_time:
            posting_time.append(time_stamp)
        time_index_map[time_stamp] = data[post_time_index]
        if time_stamp not in time_price_map:
            time_price_map[time_stamp] = [int(data[price_index])]
        else:
            time_price_map[time_stamp].append(int(data[price_index]))
    posting_time.sort()
    time_date = []
    for value in posting_time:
        time_date.append(int_to_date_map[value])
    price = []
    for data_index in posting_time:
        price.append(compute_average_data(time_price_map[data_index]))

    f, ax = plt.subplots(figsize=(12, 8))
    ax.set_title('Price vs day', pad=12)
    fig = sns.barplot(x=time_date, y=price)
    scatter_fig = fig.get_figure()
    plt.xticks(rotation=90)
    plt.show()
    file_name = name_prefix + "_vs_price_sns.png"
    scatter_fig.savefig('./plots/' + file_name, dpi=400)


def sns_plot_line_picture_by_day(ls, name_prefix, post_time_index, price_index):
    posting_time = []
    time_index_map = {}
    time_price_map = {}
    int_to_date_map = {}
    for data in ls:
        time = data[post_time_index].split('T')
        time_str = time[0]
        time_stamp = date2time(time_str, '%Y-%m-%d')
        if time_stamp not in int_to_date_map:
            int_to_date_map[time_stamp] = time_str

        if time_stamp not in posting_time:
            posting_time.append(time_stamp)
        time_index_map[time_stamp] = data[post_time_index]
        if time_stamp not in time_price_map:
            time_price_map[time_stamp] = [int(data[price_index])]
        else:
            time_price_map[time_stamp].append(int(data[price_index]))
    posting_time.sort()
    time_date = []
    for value in posting_time:
        time_date.append(int_to_date_map[value])
    price = []
    for data_index in posting_time:
        price.append(compute_average_data(time_price_map[data_index]))

    f, ax = plt.subplots(figsize=(12, 10))
    ax.set_title(name_prefix + " cars " + 'price vs day', pad=12)

    summary = []
    for i in range(len(time_date)):
        x_t = time_date[i]
        y_t = price[i]
        summary.append([x_t, y_t])
    data = DataFrame(summary, columns=['Date', 'Price'])

    fig = sns.lineplot(x="Date", y="Price", data=data)
    scatter_fig = fig.get_figure()
    plt.xticks(rotation=90)
    plt.show()
    file_name = name_prefix + "_vs_price_line_sns.png"
    scatter_fig.savefig('./plots/' + file_name, dpi=400)
