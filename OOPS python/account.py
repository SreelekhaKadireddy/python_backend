from bank import *
class Account(Bank):
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def cal_bal(self):
        pass