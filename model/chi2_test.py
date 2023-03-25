from model import Utilities
from persistence import persistence
from scipy.stats import chi2
from model import constants

class chi2_test:

    def __init__(self, file_route):
        self.random_numbers = persistence.generateNumbers(file_route)
        self.quan_intervals = self.generate_intervals()
        self.number_n = len(self.random_numbers)
        self.list_intervals = ['0.0-0.1', '0.1-0.2', '0.2-0.3', '0.3-0.4', '0.4-0.5', '0.5-0.6', '0.6-0.7', '0.7-0.8', '0.8-0.9', '0.9-1']
        self.ei = self.number_n / 10
        self.ob_ei = self.gen_ob_ei()
        self.matrix = self.gen_matrix()
        self.sum = self.sum()
        self.chi2 = self.calculate_chi_inv()

    def generate_intervals(self):
        quan_intervals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in self.random_numbers:
            if (i < 0.1):
                quan_intervals[0] += 1
            if (i >= 0.1 and i < 0.2):
                quan_intervals[1] += 1
            if (i >= 0.2 and i < 0.3):
                quan_intervals[2] += 1
            if (i >= 0.3 and i < 0.4):
                quan_intervals[3] += 1
            if (i >= 0.4 and i < 0.5):
                quan_intervals[4] += 1
            if (i >= 0.5 and i < 0.6):
                quan_intervals[5] += 1
            if (i >= 0.6 and i < 0.7):
                quan_intervals[6] += 1
            if (i >= 0.7 and i < 0.8):
                quan_intervals[7] += 1
            if (i >= 0.8 and i < 0.9):
                quan_intervals[8] += 1
            if (i >= 0.9 and i < 1):
                quan_intervals[9] += 1
        return quan_intervals

    def gen_ob_ei(self):
        list_ob_ei = []
        for i in range(len(self.list_intervals)):
            ei = self.ei
            oi = self.quan_intervals[i]
            list_ob_ei.append(((ei - oi)**2) / ei)
        return list_ob_ei

    def gen_list(self, i):
        row = []

        set = self.list_intervals[i]
        oi = self.quan_intervals[i]
        ei = self.ei
        ob_ei = self.ob_ei[i]

        row.extend([set, oi, constants.FORMAT_NUMBER.format(ei), constants.FORMAT_NUMBER.format(ob_ei)])
        return row

    def gen_matrix(self):
        matrix = [[]]
        for i in range(len(self.list_intervals)):
            matrix.append(self.gen_list(i))
        return matrix

    def sum(self):
        return sum(self.ob_ei)

    def generateGrafic(self):
        return Utilities.generateGrafic(self.random_numbers)

    def calculate_chi_inv(self):
        return chi2.isf(0.05, 9)

    def verify(self):
        if (self.chi2 > self.sum):
            return True
        return False
