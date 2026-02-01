#Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("The animal makes a sound")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print(f"{self.name} says: Woof!")

animal = Animal("Generic Animal")
dog = Dog("Completly normal dog trust")

animal.make_sound()
dog.make_sound()

#Multiple Inheritance
print("-")

class Person:
  def __init__(self, Name, Age):
    self.Name = Name
    self.Age = Age

class Skills(Person):
    def __init__(self, Name, Age, programming_skill, communication_skill):
        super().__init__(Name, Age)
        self.programming_skill = programming_skill
        self.communication_skill = communication_skill

class Employee(Skills):
    def __init__(self, Name, Age, programming_skill, communication_skill):
        super().__init__(Name, Age, programming_skill, communication_skill)
    
    def info(self):
        print(f"{self.Name} {self.Age} {self.programming_skill} {self.communication_skill}")

Human = Employee("Tim", 20, "Good", "Average")

Human.info()

#Multilevel Inhertiance
print("-")
class Vehicle:
    def __init__(self, type):
        self.type = type

    def start_engine(self):
        print(self.type + " engine has started")

class Car(Vehicle):
    def __init__(self, type, make, model, year):
        super().__init__(type)
        self.make = make
        self.model = model
        self.year = year

    def driving(self):
        print(self.type + " is now driving")

class Electric_Car(Car):
    def __init__(self, type, make, model, year, elecy):
        super().__init__(type, make, model, year)
        self.elecy = elecy

    def charge_battery(self):
        print(self.type + " is now charging")

CarObject = Car ("Car", "Destoryer 3000", "New Edition", 2025)

ElectricCarObject = Electric_Car ("Car", "Cybertruck", "Crap Edition", 2024, "Electric")

CarObject.driving()

ElectricCarObject.charge_battery()