class Employee:
    def __init__(self,name,current_salary):
        self.name =name 
        self.current_salary =current_salary
        print(f"{self.name} current salary is {self.current_salary}")
        self.bonus()
        self.tax()

    def bonus(self):
        bonus =100
        self.bonus_with_salary =bonus
        print(f"bonus is added to {self.name},self.bonus_with_salary")

    def tax(self):
        tax=0.2
        self.tax_with_salary = tax/100 *self.current_salary
        print(f"******\n tax is deducted from {self.name}",self.tax_with_salary)

    def total_salary(self):
        self.total_salary =self.current_salary +self.bonus_with_salary -self.tax_with_salary
        print("total salary",self.total_salary,"\n*************")

ram_obj =Employee("ram",5000)
ram_obj.total_salary()