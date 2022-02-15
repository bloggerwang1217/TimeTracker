import csv
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import datetime
import numpy as np
import os

plt.rcParams['figure.dpi'] = 125
plt.rcParams['savefig.dpi'] = 125
f = "lihsianti"

# path = os.getcwd()
# f = fm.FontProperties(fname=f"{path}/TaipeiSansTCBeta-Regular.ttf")

def read_csv(filename):
    data = []

    with open(filename, mode='r') as csv_fh:
        csv_reader = csv.DictReader(csv_fh)
        for row in csv_reader:
            data.append(row)

    return data


def one_day_status(data, start_time, end_time):
    time_accumulation = {}
    total_time = 0
    for item in data:
        time = datetime.datetime.strptime(item["time-of-completion"], "%Y-%m-%d-%H-%M")
        if time >= start_time and time <= end_time:
            total_time += int(item["duration"])
            if item["label"] not in time_accumulation:
                time_accumulation[item["label"]] = int(item["duration"])
            else:
                time_accumulation[item["label"]] += int(item["duration"])

    accumulated_time = list(time_accumulation.values())
    labels = list(time_accumulation.keys())

    time_ratio = []

    for value in accumulated_time:
        time_ratio.append(value/total_time*100)

    ratio = np.array(time_ratio)

    for i in range(len(labels)):
        labels[i] = f"{labels[i]}: {accumulated_time[i]} mins\n(about {round(accumulated_time[i]/60, 1)} hrs)"

    plt.pie(ratio, labels = labels, startangle = 90, autopct='%1.2f%%', textprops={"font": f})
    plt.title(f"Total Time: {total_time} mins (about {round(total_time/60, 1)} hrs)", loc='right', font = f, fontsize = 12)
    plt.savefig("one_day_status.png", bbox_inches="tight")
    plt.clf()

    return "one_day_status.png"


def average_status(data, start_time, end_time):
    time_accumulation = {}
    total_time = 0
    for item in data:
        time = datetime.datetime.strptime(item["time-of-completion"], "%Y-%m-%d-%H-%M")
        if time >= start_time and time <= end_time:
            total_time += int(item["duration"])
            if item["label"] not in time_accumulation:
                time_accumulation[item["label"]] = int(item["duration"])
            else: 
                time_accumulation[item["label"]] += int(item["duration"])

    delta_time = end_time.date()-start_time.date()
    days = int(delta_time.days)
    days += 1

    for key in time_accumulation.keys():
        time_accumulation[key] = round(time_accumulation[key]/days, 0)

    total_average_time = round(total_time/days, 0)

    average_time = list(time_accumulation.values())
    labels = list(time_accumulation.keys())

    time_ratio = []

    for value in average_time:
        time_ratio.append(value/total_time*100)

    ratio = np.array(time_ratio)

    for i in range(len(labels)):
        labels[i] = f"{labels[i]}: {average_time[i]} mins\n(about {round(average_time[i]/60, 1)} hrs)"

    plt.pie(ratio, labels = labels, startangle = 90, autopct='%1.2f%%', textprops={"font": f})
    plt.title(f"Average Time in {days} days: {total_average_time} mins (about {round(total_average_time/60, 1)} hrs)", loc='right', font = f, fontsize = 12)
    plt.savefig("average_status.png", bbox_inches="tight")
    plt.clf()

    return "average_status.png"


def trend_in_days(data, start_time, end_time):
    pass
