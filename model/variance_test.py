import random
import statistics
from scipy.stats import chi2

class VarianceTest:
    def __init__(self, ri_list):
        self.ri_list = ri_list
        self.degrees_freedom = len(ri_list)-1

    def calculate_average(self):
        return statistics.mean(self.ri_list)

    def calculate_variance(self):
        return statistics.variance(self.ri_list)

    def calculate_chi_inv(self, probability):
        return chi2.isf(probability, self.degrees_freedom)

    def calculate_limit(self, is_lower_limit, chi_inv):
        if is_lower_limit:
            return chi_inv/(12 * self.degrees_freedom)
        else:
            return chi_inv/(12 * self.degrees_freedom)

    def is_valid_test(self, lower_limit, upper_limit, variance):
        return upper_limit <= variance <= lower_limit

    def generate_values(self):
        numbers = []
        for i in range(50):
            numbers.append(random.random())
        return numbers
