"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, bonus=False, bonus_type="",amount=0, contracts = 1):
        self.name = name
        self.total_pay = 0
        self.bonus = bonus
        self.bonus_type = bonus_type
        self.amount = amount
        self.contracts = contracts

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

    def calc_bonus(self):
        if self.bonus:
            return self.amount * self.contracts
        else:
            return 0

class MonthlyEmployee(Employee):
    def __init__(self, salary, name, bonus=False, bonus_type="",amount=0, contracts = 1):
        self.salary = salary
        super().__init__(name, bonus, bonus_type, amount, contracts)

    def get_pay(self):
        self.total_pay = self.salary + self.calc_bonus()
        return self.total_pay

    def __str__(self):
        if self.bonus:
            if self.bonus_type == "bonus":
                return(f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.amount}.  Their total pay is {self.total_pay}.")
            elif self.bonus_type == "contract":
                return(f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.contracts} contract(s) at {self.amount}/contract.  Their total pay is {self.total_pay}.")
        else:
            return(f"{self.name} works on a monthly salary of {self.salary}.  Their total pay is {self.total_pay}.")

class ContractEmployee(Employee):
    def __init__(self, name, hours, rate, bonus=False, bonus_type="",amount=0, contracts = 1):
        super().__init__(name, bonus, bonus_type, amount, contracts)
        self.hours = hours
        self.rate = rate

    def get_pay(self):
        self.total_pay = (self.hours * self.rate) + self.calc_bonus()
        return self.total_pay

    def __str__(self):
        if self.bonus:
            if self.bonus_type == "bonus":
                return(f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a bonus commission of {self.amount}.  Their total pay is {self.total_pay}.")
            elif self.bonus_type == "contract":
                return(f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour and receives a commission for {self.contracts} contract(s) at {self.amount}/contract.  Their total pay is {self.total_pay}.")
        else:
            return f"{self.name} works on a contract of {self.hours} hours at {self.rate}/hour.  Their total pay is {self.total_pay}."


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = MonthlyEmployee(4000,"Billie")

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = MonthlyEmployee(3000, 'Renee', True, "contract", 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 150, 25, True, "contract", 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = MonthlyEmployee(2000, 'Robbie', True, "bonus", 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee("Ariel", 120, 30, True, "bonus", 600)
