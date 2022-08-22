# list = used to store multiple items in a single variable

# food = ["pizza", "hamburger", "eggs", "sushi"]
# food[0] = "french fries"
# food.append("ice cream")
# food.remove("eggs")
# food.pop()
# food.insert(0, ["bread, beer"])
# food.sort()
# food.clear()

# print(food)

# for x in food:
#     print(x)

# -----------------------------------------------------

# 2D lists = a list of lists

# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "eggs", "sushi"]
# dessert = ["cake", "ice cream"]

# food = [drinks, dinner, dessert]

# print(food[2][0])

# -----------------------------------------------------

# tuple = collection which is ordered and unchangeable

# student = ("Oleksii", 31, "male")

# print(student.count("Oleksii"))
# print(student.index("male"))

# for x in student:
#     print(x)

# if "Oleksii" in student:
#     print("Oleksii is here")

#------------------------------------------------------

# set = collection wich is unordered, unindexed. Without duplicate values

# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = utensils.union(dishes)
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))

# for x in dinner_table:
#     print(x)

#------------------------------------------------------

# dictionary = a changeable, unordered collection of unique key: value pairs

# capitals = {'USA': 'Washington DC', 'India': 'New Dehli', 'China': 'Beijing', 'Ukraine': 'Kyiv'}

# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
# print(capitals['Ukraine'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

# for key, value in capitals.items():
    # print(key + ':', value)
