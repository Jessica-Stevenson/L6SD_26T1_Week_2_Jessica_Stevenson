#Class Creation
print("-")
class Car:
    #the Init part allows me to group everything together
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def start_engine(self):
        print(self.make + " engine has started")
    
    def __del__(self):
        print(f"The car {self.year} {self.make} {self.model} has been deleted.")

leCar = Car("Destoryer 3000", "New Edition", 2025)

laCar = Car("Cybertruck", "Crap Edition", 2024)

UneCar = Car ("Une vie a t'aimer", "Tight", 33)

leCar.start_engine()

laCar.start_engine()

UneCar.start_engine()

del laCar

#Destructor and Cleanup
print("-")
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def PersonPrint(self):
        print(self.name)
        print(self.age)
    
    def __del__(self):
        print(f"The person {self.name} has been deleted.")

Human = Person("Mr Invisible", 52)

Human.PersonPrint()

del Human

print("-")

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def Complete(self):
        print(f"The task {self.name} has been completed.")
    
    def __del__(self):
        print(f"The task {self.name} has been cleaned up.")

LeTask = Task("Flareon", "Hey guys, did you know that in terms of human companionship, Flareon is objectively the most huggable Pokémon? While their maximum temperature is likely too much for most, they are capable of controlling it, so they can set themselves to the perfect temperature for you. Along with that, they have a lot of fluff, making them undeniably incredibly soft to touch. But that's not all, they have a very respectable special defense stat of 110, which means that they are likely very calm and resistant to emotional damage. Because of this, if you have a bad day, you can vent to it while hugging it, and it won't mind. It can make itself even more endearing with moves like Charm and Baby Doll Eyes, ensuring that you never have a prolonged bout of depression ever again. ")

LeTask.Complete

del LeTask

#Constructors and Initialization
print("-")

class Rectangle:
    def __init__(self, length=1, width=1):
        self.length = length
        self.width = width

LeRectangle = Rectangle(10, 5)
LeDefault = Rectangle()


print("Length:", LeRectangle.length)
print("Width:", LeRectangle.width)

print("Length:", LeDefault.length)
print("Width:", LeDefault.width)