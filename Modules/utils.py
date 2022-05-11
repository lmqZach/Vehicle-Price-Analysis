import time as tm
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

matplotlib.use('TkAgg')


def figure_plot_bar(x, y, name):
    fig = plt.figure()
    plt.bar(range(len(x)), y, tick_label=x)
    plt.title(name)
    plt.show()
    fig.savefig('./plots/' + name)


def bar_plot(x, y, name):
    plt.bar(x, y)
    plt.title(name)
    plt.show()
    plt.savefig('./plots/' + name)


def sns_figure_plot_bar(x, y, name):
    f, ax = plt.subplots(figsize=(12, 8))
    ax.set_title(name, pad=12)
    region = x
    price = y
    fig = sns.barplot(x=region, y=price)
    scatter_fig = fig.get_figure()
    plt.xticks(rotation=90)
    plt.show()
    scatter_fig.savefig('./plots/' + name, dpi=400)


def date2time(date_str, format='%Y-%m-%d %H:%M:%S'):
    dt = date_str
    timeArray = tm.strptime(dt, format)
    timestamp = int(tm.mktime(timeArray))
    return timestamp


def compute_average_data(ls):
    return sum(ls) / len(ls)


def compute_max(ls, price_index):
    max_price = 0
    for data in ls:
        if int(data[price_index]) > max_price:
            max_price = int(data[price_index])
    print(max_price)
    return max_price


def compute_average(ls, price_index):
    price_list = []
    for data in ls:
        price = int(data[price_index])
        price_list.append(price)
    average_price = sum(price_list) / len(price_list)
    print(average_price)
    return average_price
