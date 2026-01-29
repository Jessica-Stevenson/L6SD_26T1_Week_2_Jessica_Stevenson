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