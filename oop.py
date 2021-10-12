# class BankApp():
#     def __init__(self, name, balance):
#         if not isinstance(balance, (int, float)):
#             raise TypeError(f'Expected int or float but got {type(balance)}')
#         self.name = name
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
        
#         return self.balance
    
#     def name_tolower(self):
#         self.name = self.name.lower()
#         return self.name
        
# customer1 = BankApp('Tunde', 105.44)
# print(customer1.name_tolower())
# print(customer1.deposit(1000))

# class vehicle():
#     def __init__(self, max_speed, mileage):
#         self.max_speed = max_speed
#         self.mileage = mileage
        
#     def acceleration(self, time):
#         a = self.mileage*2/time**2
#         return a
    
# car = vehicle(15, 20)    

# print(car.acceleration(10))
# print(car.max_speed)
# print(car.mileage)


# st = "I am"
# print(isinstance(st, BankApp))


class Employee():
    def __init__(self, name, salary,designation):
        self.name = name
        self.salary = salary
        self.designation = designation
    
    @property    
    def bonus(self):
        return (self.salary * 0.1 ) + self.salary
    
    def report(self):
        return f"Hi {self.name}. You take home salary is {self.bonus}"

class Supervisor(Employee):
    def __init__(self, name, salary, designation, branch):
        self.branch  = branch
        super().__init__(name, salary, designation)
        
        
st = Employee("John", 1000, "Barman")
print(st.report())

st2 = Supervisor("Bode", 12000, "Accountant", "Sabo")
print(st2.bonus)