import random, statistics

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

def generateNumbers(seed, iterations):
    iterations = int(iterations)
    seed_extension = len(str(seed))
    x_i = int(seed)
    data = []
    i = 0
    while i < iterations:
        x_i_square = pow(x_i, 2)
        square_seed = str(x_i_square)
        square_extension = len(square_seed)
        primerc = (square_extension - seed_extension) / 2
        extraction = square_seed[int(primerc):int(primerc + seed_extension)]
        data.append(int(extraction) / pow(10, seed_extension))
        x_i = int(extraction)
        i += 1
    return data