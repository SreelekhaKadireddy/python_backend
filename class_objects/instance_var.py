class Account:
    def __init__(self,id,name,bal): #constructor method
        self.acc_Id=id
        self.acc_Name=name
        self.acc_Bal=bal
    def email(self,email): #instance method 
        self.Email=email
    @classmethod
    def loc(self,loc): #classmethod
        self.Location=loc
a1=Account(101,'Rahul',5000)
print(a1.__dict__)
a1.email('rahul@gmail.com')
print(a1.__dict__)
a2=Account(102,'Sonia',6000)
print(a2.__dict__)
a2.loc('New Delhi')
print(a2.__dict__)