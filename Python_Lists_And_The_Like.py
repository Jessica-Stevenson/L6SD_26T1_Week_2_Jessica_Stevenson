#Lists
#Excercise 1
shopping_list = ["apple", "banana", "orange"] 

print(shopping_list)

#Excercise 2
shopping_list.append("grapes")
shopping_list.remove("banana")

print(shopping_list)

#Tuples
#Excercise 1
print("-")

coordinates = (100, 200)

print(coordinates)

update = list(coordinates)
update[0] = 200
coordinates = tuple(update)
print(coordinates)

#Excercise 2
print("-")

fruits = ("Apple", "Banana", "Watermelon")

print(fruits[1])

if "Banana" in fruits:
    print("Banana is in the tuple")
else:
    print("Banana is not in the tuple")

#Dictionary
#Exercise 1
print("-")

library_catalogue = {
    "Eye of minds" : "James Dashner",
    "Le book" : "Le Author",
    "La book" : "La Author"
}

print(library_catalogue)

#Exercise 2
print("-")

def word_lengths(words):
    result = {}
    for word in words:
        result[word] = len(word)
    return result

words = ["Bonjour", "Whatislove", "ForThoseWhoComeAfter", "SHAW"]
output = word_lengths(words)
print(output)

#Sets
#Excercise 1
print("-")

def common_elements(list1, list2):
    return set(list1) & set(list2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = [4, 5, 6, 7, 9, 11, 13, 18]

result = common_elements(a, b)
print(result)

#Excercise 2
print("-")

Games_List = ["Silksong", "Expedition 33", "Baldur's Gate 3", "Silksong"]

Games_Set = set(Games_List)

print(Games_Set)

#Stacks
#Excercise 1
print("-")

def reverse_list(list):
    stack = []

    for item in list:
        stack.append(item)

    reversed_list = []

    while stack:
        reversed_list.append(stack.pop())

    return reversed_list

numbers = [1, 2, 3, 4, 5]
result = reverse_list(numbers)
print(result)

#Excercise 2
class UndoStack:
    def __init__(self):
        self.stack = []

    def do_action(self, action):
        self.stack.append(action)
        print(f"Action performed: {action}")

    def undo(self):
        if not self.stack:
            print("Nothing to undo")
        else:
            last_action = self.stack.pop()
            print(f"Undo action: {last_action}")

action = UndoStack()

action.do_action("Hello")
action.do_action("How art thou")

action.undo()

