import random, statistics

class MeanTest:

    def __init__(self, acept, error, numberN):
        self.acept = acept
        self.error = error
        self.numberN = numberN

    def generateNumbers(self):
        randomNumbers = []
        j = int(self.numberN)
        for i in range(j):
            randomNumbers.append(float(random.random()))
        return randomNumbers
    
    def calculateMean(self):
        randomNumbers = self.generateNumbers()
        mean = statistics.mean(randomNumbers)
        return mean
    
    def calculateAlpha(self):
        error = float(self.error)
        alpha = 1-(error/2)
        return alpha
    
    def calculateDisNormEstInv(self):
        alpha = self.calculateAlpha()
        dist = statistics.NormalDist.inv_cdf(alpha)
        return dist

    def printValues(self):
        print(self.acept, self.error, self.numberN)