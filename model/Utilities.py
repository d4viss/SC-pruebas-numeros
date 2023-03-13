import statistics
import matplotlib.pyplot as plt
from io import BytesIO


def calculateMean(randomNumbers):
    mean = statistics.mean(randomNumbers)
    return round(mean, 5)


def calculateAlpha(error):
    error = float(error) / 100
    alpha = 1-(error/2)
    return round(alpha, 5)


def calculateDisNormEstInv(alpha):
    dist = statistics.NormalDist(0, 1)
    return round(dist.inv_cdf(float(alpha)), 5)


def generateNumbers(fileRoute):
    list = []
    file = open(fileRoute, 'r')
    reading = file.readlines()
    for i in range(len(reading)):
        str = reading[i].replace('/n', '')
        list.append(float(str))
    print(list)
    return list


def generateGrafic(data):
    fig, ax = plt.subplots()
    ax.hist(data, bins=50)
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer
