import math
from model import Utilities
from persistence import persistence
from model import constants

class MeanTest:

    def __init__(self, fileRoute):
        self.acept = constants.ACCEPT
        self.error = constants.ALPHA / 100
        self.alpha = Utilities.calculateAlpha(self.error)
        self.z = Utilities.calculateDisNormEstInv(self.alpha)
        self.randomNumbers = persistence.generateNumbers(fileRoute)
        self.numberN = len(self.randomNumbers)
    
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
        
    def generateGrafic(self):
        return Utilities.generateGrafic(self.randomNumbers)