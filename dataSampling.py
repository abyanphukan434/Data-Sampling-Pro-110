import plotly.figure_factory as gx
import plotly.graph_objects as fx
import pandas as pd
import random
import csv
import statistics

df = pd.read_csv('data.csv')
data = df['reading_time'].tolist()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data) - 1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = gx.create_distplot([df], ['reading_time'], show_hist = False)
    fig.add_trace(fx.Scatter(x = [mean, mean], y = [0, 1], mode = 'lines', name = 'MEAN'))
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.appen(set_of_means)
    show_fig(mean_list)

    mean = statistics.mean(mean_list)
    print('Mean of sampling distribution :-', mean)

setup()

population_mean = statistics.mean(data)
print('Population mean :-', population_mean)

def standard_deviation():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    
    std_deviation = statistics.stdev(mean_list)
    print('Sampling mean :-', std_deviation)

standard_deviation()