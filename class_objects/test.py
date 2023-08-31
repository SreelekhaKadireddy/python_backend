class Test:
    a=100 #static variable
    def __init__(self): #constuctor method
        Test.b=200
    def m1(self): #instance method
        Test.c=300
    @classmethod
    def m2(cls): #class method
        cls.d=400
        Test.e=500
    @staticmethod
    def m3(): #static method
        Test.f=600
t1=Test()
t1.m1()
t1.m2()
t1.m3()
Test.g=700
print(Test.__dict__)
        