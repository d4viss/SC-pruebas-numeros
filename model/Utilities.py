import statistics
import matplotlib.pyplot as plt
from io import BytesIO

def calculateMean(randomNumbers):
    mean = statistics.mean(randomNumbers)
    return mean


def calculateAlpha(error):
    error = float(error) / 100
    alpha = 1-(error/2)
    return alpha


def calculateDisNormEstInv(alpha):
    dist = statistics.NormalDist(0, 1)
    return dist.inv_cdf(float(alpha))


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
    ax.hist(data, bins=10)
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer
