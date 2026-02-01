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
