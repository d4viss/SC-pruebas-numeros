import math
from model import Utilities

class MeanTest:

    def __init__(self, acept, fileRoute):
        self.acept = int(acept)
        self.error = 100 - self.acept
        self.alpha = Utilities.calculateAlpha(self.error)
        self.z = Utilities.calculateDisNormEstInv(self.alpha)
        self.randomNumbers = Utilities.generateNumbers(fileRoute)
        self.numberN = len(self.randomNumbers)
    
    def calculateMean(self):
        return Utilities.calculateMean(self.randomNumbers)
    
    def calculateLI(self):
        return round(float(1/2-self.z *(1/(math.sqrt(12*self.numberN)))), 5)
    
    def calculateLS(self):
        return round(float(1/2+self.z *(1/(math.sqrt(12*self.numberN)))), 5)
    
    def verifyTest(self):
        mean = self.calculateMean() 
        if mean >= self.calculateLI() and mean <= self.calculateLS():
            return True
        else:
            return False
        
    def generateGrafic(self):
        return Utilities.generateGrafic(self.randomNumbers)