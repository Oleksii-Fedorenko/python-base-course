# if statement = a block of code that will execute if it's condition is true

# age = int(input("How old are you?: "))

# if age == 100:
#     print("You are a century old")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You haven't been born yet!")
# else:
#     print("Your are a child!")

# logical operators(and, or, not)

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today!")
    print("go outside!")
elif temp < 0 or temp > 30:
    print("the temperature is bad taday!")
    print("stay home!")