class  CA(Account):
    min_bal=50000
    def __init__(self,a,b,c):
        super().__init(a,b)
        self.c=c
    def cal_bal(self):
        return self.c-self.min_bal
a2=CA(11,"b",100000)
