
class SA(Account):
    min_amount=500
    def __init__(self,id,name,amount):
        super().__init__(id,name)
        self.amount=amount
    def cal_bal(self):
        return self.amount-self.min_amount
a1=SA(10,"a",4000)
