# function = a block of code which is executed only when it is called

# def hello(first_name, last_name, age):
#     print("hello", first_name, last_name)
#     print(f"You are {age} years old")
#     print("How are you?")

# hello("Oleksii", "Fedorenko", 31)

# -----------------------------------------------------

# return statement

# def multiply(num1, num2):
#     result = num1 * num2
#     return result


# x = multiply(6, 8)
# print(x)

# ------------------------------------------------------

# keyword arguments

# def hello(first, middle, last):
#     print("Hello " + first + " " + middle + " " + last)

# hello(middle = "Oleksii", last = "Dude", first = "Bro")

#------------------------------------------------------

# nested function calls function calls inside other func

# num = input("Enter a whole positive number: ")
# num = float(num)
# num = abs(num)
# num = round(num)
# print(num)

# print(round(abs(float(input("Enter a whole positive number: ")))))

# -------------------------------

# *args = parameter that willl pack all arguments into a tuple

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(1, 2, 3))

# -------------------------------------------------

# **kwargs = parameter that will pack all arguments into a dictioinary

# def hello(**kwargs):
    # print("Hello", kwargs['first'], kwargs['last'])

#     print("Hello", end=" ")

#     for key, value in kwargs.items():
#         print(value, end=" ")

# hello(title = "Mr.", first = "Oleksii", middle="Dude", last = "Fedorenko")