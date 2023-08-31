class Employees:
    org_Name='TCS'
    def __init__(self,id,name,loc):
        self.eId=id
        self.eName=name
        self.eLoc=loc
        Employees.designation='developers'
        print(Employees.__dict__)
    def emp_sal(self,esal):
        print(self.org_Name)
        self.eSal=esal
    @classmethod
    def get_details(cls):
        print(cls.__dict__)
emp1=Employees(101,'rahul','bangalore')
print(emp1.__dict__)
print(Employees.__dict__)
emp1.emp_sal(45000)
print(emp1.__dict__)
Employees.get_details()