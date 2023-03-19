from model import Utilities
from persistence import persistence
from model.set import set
from model.hand import hand
from scipy.stats import chi2
from model import constants

class poker_test:

    def __init__(self, file_route):
        self.random_numbers = persistence.generateNumbers(file_route)
        self.sets = self.generate_sets()
        self.number_n = len(self.random_numbers)
        self.list_prob = [0.3024, 0.504, 0.108, 0.072, 0.009, 0.0045, 0.0001]
        self.hands = [hand.HIGH_CARD.value, hand.PAIR.value, hand.TWO_PAIR.value, hand.TREE_OF_A_KIND.value, hand.FULL_HOUSE.value, hand.FOUR_OF_A_KIND.value, hand.FIVE_OF_A_KIND.value]
        self.ei = self.gen_ei()
        self.quan_sets = self.count_quan()
        self.ob_ei = self.gen_ob_ei()
        self.matrix = self.gen_matrix()
        self.sum = self.sum()
        self.chi2 = self.calculate_chi_inv()

    def generate_sets(self):
        sets = []
        for i in self.random_numbers:
            set_n = set(int(round(i * 100000)))
            sets.append(set_n)
        return sets

    def count_quan(self):
        quan_sets = [0, 0, 0, 0, 0, 0, 0]
        for i in self.sets:
            if (i.cat == hand.HIGH_CARD):
                quan_sets[0] += 1
            if (i.cat == hand.PAIR):
                quan_sets[1] += 1
            if (i.cat == hand.TWO_PAIR):
                quan_sets[2] += 1
            if (i.cat == hand.TREE_OF_A_KIND):
                quan_sets[3] += 1
            if (i.cat == hand.FULL_HOUSE):
                quan_sets[4] += 1
            if (i.cat == hand.FOUR_OF_A_KIND):
                quan_sets[5] += 1
            if (i.cat == hand.FIVE_OF_A_KIND):
                quan_sets[6] += 1
        return quan_sets

    def gen_ei(self):
        list_ei = []
        n = len(self.random_numbers)
        for i in range(len(self.list_prob)):
            list_ei.append(self.list_prob[i] * n)
        return list_ei

    def gen_ob_ei(self):
        list_ob_ei = []
        for i in range(len(self.hands)):
            ei = self.ei[i]
            oi = self.quan_sets[i]
            list_ob_ei.append(((ei - oi)**2) / ei)
        return list_ob_ei

    def gen_list(self, i):
        row = []

        set = self.hands[i]
        oi = self.quan_sets[i]
        prob = self.list_prob[i]
        ei = self.ei[i]
        ob_ei = self.ob_ei[i]

        row.extend([set, oi, constants.FORMAT_NUMBER.format(prob), constants.FORMAT_NUMBER.format(ei), constants.FORMAT_NUMBER.format(ob_ei)])
        return row
    
    def gen_matrix(self):
        matrix = [[]]
        for i in range(len(self.ei)):
            matrix.append(self.gen_list(i))
        return matrix
    
    def sum(self):
        return sum(self.ob_ei)
    
    def generateGrafic(self):
        return Utilities.generateGrafic(self.random_numbers)
    
    def calculate_chi_inv(self):
        return chi2.isf(0.05, 6)
    
    def verify(self):
        if(self.chi2 > self.sum):
            return True
        return False
