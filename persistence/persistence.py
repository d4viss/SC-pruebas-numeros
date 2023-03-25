def generateNumbers(fileRoute):
    list = []
    file = open(fileRoute, 'r')
    reading = file.readlines()
    for i in range(len(reading)):
        str = reading[i].replace('/n', '')
        list.append(float(str))
    print(list)
    return list