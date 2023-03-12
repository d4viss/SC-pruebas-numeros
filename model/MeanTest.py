import math
from model import Utilities

class MeanTest:

    def __init__(self, acept, seed, numberN):
        self.acept = int(acept)
        self.error = 100 - self.acept
        self.numberN = int(numberN)
        self.seed = seed
        self.alpha = Utilities.calculateAlpha(self.error)
        self.z = Utilities.calculateDisNormEstInv(self.alpha)
        self.randomNumbers = Utilities.generateNumbers(self.seed, self.numberN)
    
    def calculateMean(self):
        return Utilities.calculateMean(self.randomNumbers)
    
    def calculateLI(self):
        return float(1/2-self.z *(1/(math.sqrt(12*self.numberN))))
    
    def calculateLS(self):
        return float(1/2+self.z *(1/(math.sqrt(12*self.numberN))))
    
    def verifyTest(self):
        mean = self.calculateMean() 
        if mean >= self.calculateLI() and mean <= self.calculateLS():
            return True
        else:
            return False