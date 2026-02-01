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

#Scenario 1: Zoo Animals
print("-")
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Generic animal sound")

class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.fur_color = fur_color

    def give_birth(self):
        print(f"{self.name} is giving birth")

class Bird(Animal):
    def __init__(self, name, species, feather_color):
        super().__init__(name, species)
        self.feather_color = feather_color

    def fly(self):
        print(f"{self.name} is flying")

class flightless(Bird):
    def __init__(self, name, species, feather_color, flight_ability):
        super().__init__(name, species, feather_color)
        self.flight_ability = flight_ability

    def fly(self):
        print(f"{self.name}'s cannot fly")

pengin = flightless ("Penguin", "Penguin", "Black and White", "Cannot fly")

pengin.fly()

#Scenario 2: School Subjects
print("-")

class Subject:
    def __init__(self, name):
        self.name = name

    def study(self):
        print(f"Studying {self.name}")

class Math(Subject):
    def __init__(self, name, difficulty_level):
        super().__init__(name)
        self.difficulty_level = difficulty_level

    def solve_problem(self):
        print(f"Solving a {self.difficulty_level} math problem")

class Language(Subject):
    def __init__(self, name, language_type):
        super().__init__(name)
        self.language_type = language_type

    def practice_language(self):
        print(f"Practicing {self.language_type} language")

class pain(Math):
    def __init__(self, name, difficulty_level, pain_level):
        super().__init__(name, difficulty_level)
        self.pain_level = pain_level

    def info(self):
        print(f"{self.name} has a pain level of {self.pain_level}")

Mathness = pain ("Math", 10, 10,)

Mathness.info()