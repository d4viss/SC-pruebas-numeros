from model import Utilities, constants
from scipy.stats import ksone


class KolmogorovSmirnovTest:
    def __init__(self, ri_list, minimum, maximum):
        self.ri_list = ri_list
        self.len_ri = len(ri_list)
        self.mean = Utilities.calculateMean(ri_list)
        self.minimum = minimum
        self.maximum = maximum
        self.initial_list = []
        self.final_list = []
        self.freq_obt_list = []

    def calculate_intervals(self):
        self.initial_list.append(self.minimum)
        for i in range(constants.INTERVALS):
            value = self.initial_list[-1] + (self.maximum - self.minimum) / constants.INTERVALS
            self.final_list.append(round(value, 1))
            self.initial_list.append(round(value, 1))
        self.initial_list = self.initial_list[:-1]

    def get_frequency_obt(self):
        f_list = []
        for i in range(constants.INTERVALS):
            count = 0
            for j in range(len(self.ri_list)):
                if self.initial_list[i] <= self.ri_list[j] <= self.final_list[i]:
                    count += 1
            f_list.append(count)
        return f_list

    def get_freq_obt_acc(self, freq_obt_list):
        f_acc_list = [freq_obt_list[0]]
        for i in range(1, constants.INTERVALS):
            f_acc_list.append(freq_obt_list[i]+f_acc_list[i-1])
        return f_acc_list

    def get_prob_obt(self, freq_obt_acc):
        prob_obt = []
        for i in range(constants.INTERVALS):
            prob_obt.append(round(freq_obt_acc[i]/self.len_ri, 4))
        return prob_obt

    def get_exp_freq_acc(self):
        exp_freq_acc = [self.len_ri / constants.INTERVALS]
        add = self.len_ri/constants.INTERVALS
        for i in range(1, constants.INTERVALS):
            exp_freq_acc.append(round(exp_freq_acc[i-1]+add, 1))
        return exp_freq_acc

    def get_exp_prob_acc(self, exp_freq_acc):
        exp_prob_acc = []
        for i in range(constants.INTERVALS):
            exp_prob_acc.append(round(exp_freq_acc[i]/self.len_ri, 2))
        return exp_prob_acc

    def get_abs_diff(self, prob_obt, exp_prob_acc):
        diff_list = []
        for i in range(constants.INTERVALS):
            diff_list.append(round(abs(exp_prob_acc[i]-prob_obt[i]), 2))
        return diff_list

    def get_critic_value(self):
        return constants.KS_TABLE[str(self.len_ri)] if self.len_ri <= len(constants.KS_TABLE) else round(constants.CRITIC_VALUE/(self.len_ri**0.5), 5)
