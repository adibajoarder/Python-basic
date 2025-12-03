class Person:
    def __init__(self, name, age):
        self.name = name 
        self.age = age
        # print("hello")
        
p1 = Person("Adiba", 22)
print("Name:", p1.name)
print("Age:", p1.age)




class Student:
    def __init__(self, name):
        self.name = name
    
    def show(self):
        print("Student name is", self.name)

s = Student("Rahim")
s.show()






class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   
        
    def deposit(self, amount):
        self.__balance += amount
        
    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())





class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Bark"

for animal in (Cat(), Dog()):
    print(animal.sound())







class Car:
    wheels = 4    # class variable shared by all objects
    
    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
car2 = Car("BMW")

print(car1.brand, car1.wheels)
print(car2.brand, car2.wheels)





class Computer:
    def __init__(self):
        self.brand = "HP"
        self.cpu = self.CPU()   # creating inner class object

    class CPU:  # inner class
        def specs(self):
            print("CPU: Intel i7")

c = Computer()
print("Brand:", c.brand)
c.cpu.specs()