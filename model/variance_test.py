import statistics
from model import constants
from scipy.stats import chi2


class VarianceTest:
    def __init__(self, ri_list):
        self.ri_list = ri_list
        self.degrees_freedom = len(ri_list)-1

    def calculate_variables(self):
        chi_inv1 = self.calculate_chi_inv(constants.ALPHA_HALF)
        chi_inv2 = self.calculate_chi_inv(constants.ONE_MINUS_ALPHA_HALF)
        lower_limit = self.calculate_limit(chi_inv1)
        upper_limit = self.calculate_limit(chi_inv2)
        variables = [chi_inv1, chi_inv2, lower_limit, upper_limit]
        return variables

    def calculate_average(self):
        return statistics.mean(self.ri_list)

    def calculate_variance(self):
        return statistics.variance(self.ri_list)

    def calculate_chi_inv(self, probability):
        return chi2.isf(probability, self.degrees_freedom)

    def calculate_limit(self, chi_inv):
        return chi_inv/(12 * self.degrees_freedom)

    def is_valid_test(self, lower_limit, upper_limit, variance):
        return upper_limit <= variance <= lower_limit

