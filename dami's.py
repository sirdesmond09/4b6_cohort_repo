# # class Student():
# #     def __init__(self, name, id):
# #         self.name = name
# #         self.id = id
    
    
# #     def say_name(self):
# #         return self.name
    
    

        
        

# # st1 = Student("John", "009")
# # st2 = Student("Mary", "093")


# # name = st1.say_name()
# # print(name)


# class Order():
    
#     vendor = "Ebere Stores"
    
#     def __init__(self, quantity, price, coupon=""):
#         self.quantity = quantity
#         self.price = price
#         self.coupon = coupon
        
#     def get_grand_total(self):
#         total = self.quantity*self.price
#         if self.coupon:
#             discount = total*0.05
#             total-=discount

#         vat = total *0.05
        
#         return total + vat
    
#     def get_discount(self):
#         if self.coupon: 
#             return "You have a 5 percent discount"
#         else: 
#             return "You have no discount"
        
    
#     @classmethod
#     def get_vendor(cls):
#         return cls.vendor
        
# order1 = Order(2, 146)
# order2 = Order(5, 30, coupon="tey222")
# # print(order1.get_grand_total())
# # print(order2.get_grand_total())
# print(order1.get_vendor())
# # print(order2.vendor)



class Employee():
    
    def __init__(self, id, salary, years_of_service):
        
        self.id = id
        self.salary = salary
        self.years_of_service=years_of_service
        
    @property
    def bonus(self):
        if self.years_of_service >=5:
            return self.salary *0.1
        else:
            return 0
    
    
    def my_total_salary(self):
        return self.salary + self.bonus
    
    
        
        
class Manager(Employee):
    
    def __init__(self, id, salary, years_of_service, branch):
        self.branch=branch
        super().__init__(id, salary, years_of_service)
    
    def assign_intern(self, intern_name):
        self.intern = intern_name 
    
    @property
    def bonus(self):
        return self.salary * 0.15

employee1 = Employee("94", 12000, 5,)
print(employee1.bonus)

manager1 = Manager("044", 12000, 5, 'Sabo')
print(manager1.bonus)
print(manager1.my_total_salary())
# print(manager1.my_total_salary())
# manager1.assign_intern("Rachael")

# print(manager1.intern)