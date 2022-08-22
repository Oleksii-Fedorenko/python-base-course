# string methods

# name = 'Alex'
# age = 31
# attractive = True

# name, age, attractive = 'Alex', 31, True

# print(name)
# print(age)
# print(attractive)


# Spongebob = 30
# Patrick = 30
# Sandy = 30
# Squidward = 30

# Spongebob = Patrick = Sandy = Squidward = 30

# print(Spongebob)
# print(Patrick)
# print(Sandy)
# print(Squidward)


# name = 'Oleksii Fedorenko'

# print(len(name))
# print(name.find('e'))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count('o'))
# print(name.replace('o', 'yo'))
# print(name * 2)

# ------------------------------------------------------

# STRING SLICING

# name = "Oleksii Fedorenko"

# first_name = name[:7]
# last_name = name[8:]
# funky_name = name[::2]
# reversed_name = name[::-1]

# print(first_name)
# print(last_name)
# print(funky_name)
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://widipedia.com"
# slice = slice(7, -4)

# print(website1[slice])
# print(website2[slice])

# ------------------------------------------------------

# index operator []

# name = "oleksii Fedorenko"
# if(name[0].islower()):
# name = name.title()
# first_name = name[:7].upper()
# last_name = name[8:].lower()
# last_character = name[-1]

# print(first_name)
# print(last_name)
# print(last_character)

# -----------------------------------------------------

# format method

# animal = "cow"
# item = "moon"

# print("The " +animal+" jumped over the "+item)
# print("The {} jumped over the {}".format("cow", "moon"))
# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {0}".format(animal, item)) # position argument
# print("The {animal} jumped over the {item}".format(animal = "cow", item = "moon")) # keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))


# name = "Oleksii"

# print("Hello, my name is {}".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))



# number = 3.14159
# number1 = 1000
# number2 = 14
# number3 = 10000

# print("the number pi is {:.2f}".format(number)) # left only 2 signs after point
# print("the number1 is {:,}".format(number1)) # make float
# print("the number2 is {:b}".format(number2)) # transform to binary(2)
# print("the number2 is {:o}".format(number2)) # transform to octal(8)
# print("the number3 is {:X}".format(number3)) # transform to hexedacimal(16)
# print("the number3 is {:e}".format(number3)) # transform to scientific notation

