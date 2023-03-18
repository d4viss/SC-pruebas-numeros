from model.hand import hand
import math

class set():

    def __init__(self, number):
        self.number = number
        self.set = self.gen_set()
        self.cat = self.gen_cat()
        print(self.cat)

    def gen_set(self):
        str_num = str(self.number)
        list_num = []
        for i in str_num:
            list_num.append(int(i))
        return list_num
    
    def gen_cat(self):
        list_repet = self.identify_repet()
        if( self.is_five(list_repet) ):
            return hand.FIVE_OF_A_KIND
        if(self.is_four(list_repet)):
            return hand.FOUR_OF_A_KIND
        if(self.is_full(list_repet)):
            return hand.FULL_HOUSE
        if(self.is_trio(list_repet)):
            return hand.TREE_OF_A_KIND
        if(self.is_two_pair(list_repet)):
            return hand.TWO_PAIR
        if(self.is_pair(list_repet)):
            return hand.PAIR
        if(self.is_not(list_repet)):
            return hand.HIGH_CARD
        return hand.ERROR

    def identify_repet(self):
        list_repet = []
        list_num = self.gen_set()
        for i in range(len(list_num)):
            count = list_num.count(list_num[i])
            list_repet.append(count)
        print(list_repet)
        return list_repet
    
    def is_not(self, list_repet):
        if(list_repet.count(1) == 5):
            return True
        return False
    
    def is_pair(self, list_repet):
        if(list_repet.count(2) == 2):
            return True
        return False
    
    def is_two_pair(self, list_repet):
        if(list_repet.count(2) == 4):
            return True
        return False
    
    def is_trio(self, list_reped):
        if(list_reped.count(3) == 3):
            return True
        return False
    
    def is_full(self, list_repet):
        if(list_repet.count(3) == 3 and list_repet.count(2) == 2):
            return True
        return False
    
    def is_four(self, list_repet):
        if(list_repet.count(4) == 4):
            return True
        return False
    
    def is_five(self, list_repet):
        if(list_repet.count(5) == 5):
            return True
        return False
