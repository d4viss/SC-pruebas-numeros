import statistics
from os import getcwd
from os.path import join

import matplotlib.pyplot as plt
from io import BytesIO


from werkzeug.utils import secure_filename


def calculateMean(randomNumbers):
    mean = statistics.mean(randomNumbers)
    return mean


def calculateAlpha(error):
    error = float(error) / 100
    alpha = 1 - (error / 2)
    return round(alpha, 5)
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


def read_file(path):
    numbers = []
    with open(path, 'r') as file:
        reading = file.readlines()
        for line in reading:
            value = line.strip()
            numbers.append(float(value))
    return numbers


def generateGrafic(data):
    fig, ax = plt.subplots()
    ax.hist(data, bins=10)
    buffer = BytesIO()
    fig.savefig(buffer, format='png')
    buffer.seek(0)
    return buffer


def get_ri_list(file, folder):
    file_route = secure_filename(file.filename)
    file.save(join(folder, file_route))
    path = getcwd() + "/files/" + file.filename
    ri_list = read_file(path)
    return ri_list
