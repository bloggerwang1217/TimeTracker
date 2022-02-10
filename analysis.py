import csv
import matplotlib.pyplot as plt
import datetime
import numpy as np

plt.rcParams['figure.dpi'] = 125
plt.rcParams['savefig.dpi'] = 125

def read_csv(filename):
    data = []

    with open(filename, mode='r') as csv_fh:
        csv_reader = csv.DictReader(csv_fh)
        for row in csv_reader:
            data.append(row)

    return data


def one_day_status(data, start_time, end_time):
    time_accumulation = {}
    for item in data:
        time = datetime.datetime.strptime(item["time-of-completion"], "%Y-%m-%d-%H-%M")
        if time >= start_time and time <= end_time:
            if item["label"] not in time_accumulation:
                time_accumulation[item["label"]] = int(item["duration"])
            else:
                time_accumulation[item["label"]] += int(item["duration"])

    accumulated_time = list(time_accumulation.values())
    labels = list(time_accumulation.keys())

    x = np.arange(len(labels))

    for i in range(len(labels)):
        plt.text(i, accumulated_time[i], accumulated_time[i], ha = 'center')

    plt.bar(x, accumulated_time)
    plt.xticks(x, labels, font = "lihsianti")
    plt.xlabel("Label", font = "lihsianti")
    plt.ylabel("Accumulated Time(min)", font = "lihsianti")
    plt.savefig("one_day_status.png")

    return "one_day_status.png"
