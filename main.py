
# my first python program
# print("I like dogs!")
# print("Hello, world!")

# Vriables = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

# Strings
# first_name = "Novic"
# food = "chapati"
# email = "novikmuliro5@gmail.com"
# degree = "Computer Science"

# print(first_name)

# print(f"Hello {first_name}")
# print(f"You like {food}")
# print(f"Your email is {email}")
# print(f"You did {degree} in campus")

# Integers
# age = 25
# quantity = 3
# num_of_students = 30

# print(f"You are {age} years old")
# print(f"You are buying {quantity} items");
# print(f"Your class has {num_of_students} students")

#Float
# price = 10.99
# gpa = 3.2
# distance = 5.5

# print(f"The price is ${price}")
# print(f"Your gpa is: {gpa}")
# print(f"You ran {distance} km")

# Boolean
# is_student = False
# for_sale = False
# is_online = True


# print(f"Are you a student?: {is_student}")

# if is_student:
#     print("You are a student")
# else: 
#     print("You are not a student")

# if for_sale:
#     print("This car is for sale")
# else:
#     print("This car is not available for sale")

# if is_online:
#     print("You are online")
# else:
#     print("You are offline")

#Typecasting = The process of converting a variable from one data type to another
#               str(), int(), float(), bool()

# name = "Muliro"
# age = 25
# gpa = 3.2
# is_student = True

# # print(type(is_student))
# name = bool(name)
# gpa = int(gpa)
# print(type(gpa))



# age = float(age)
# print(type(age))
# print(age)

# print(name)

#input() = A function that prompts the user to enter data 
#            Returns the enetered data as string



# name = input("What is your name?: ")
# age = int(input("How old are you?: "))

# # age = int(age) # typecasting age from string to integerm
# age = age + 1

# print(f"Hello {name}!")
# print("Happy Birthday!")
# print(f"You are {age} years old")

# Exercise 1 Rectangle Area Calculator

# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))

# area = length * width

# print(f"The area of the rectangle is: {area}")

# Exercise 2 Shoping Cart Program


# Madlibs game
# word game where you create a story
# by filling in blanks with random words



# adjective1 = input("Enter an adjective (description): ")
# noun1 = input("Enter a noun (person, place, or thing): ")
# adjective2 = input ("Enter an adjective (description): ")
# verb1 = input("Enter a verb (action): ")
# adjective3 = input("Enter an adjective (description): ")


# print(f"Today I went to a {adjective1} zoo.")
# print(f"In an exhibit, I saw a {noun1}")
# print(f"{noun1} was {adjective2} and {verb1}")
# print(f"I was {adjective3}!")

#Arithmetic Operator

# friends = 5
# friends = friends + 1
# print(friends)

# friends = friends - 2
# print(friends)

# friends = friends * 3
# print(friends)

# friends = friends / 2
# print(friends)

# friends = friends ** 2
# print(friends)

# friends = friends % 2
# print(friends)

# x = 3.14
# y = -4
# z = 5

# results = round(x)
# results = abs(y)
# results = pow(z, 2)
# results = max(x, y, z)
# print(results)

# Functions from the math class
import math
# math.pi
# print(math.pi)

# x = 9.1 
# results = math.sqrt(x)
# results = math.ceil(x) # rounds up to the nearest integer
# results = math.floor(x) # rounds down to the nearest integer

# print(results)

# radius = float(input("Enter the radius of the circle: "))
# area = math.pi * math.pow(radius, 2)
# print(f"The area of the circle is: {area}")

# circumference = 2 * math.pi * radius
# print(f"The circumference of the circle is: {round(circumference, 2)}")


hyp = float(input("Enter the length of the hypotenuse: "))

b = float(input("enter the length of the base: "))

h = math.sqrt(math.pow(hyp, 2) - math.pow(b, 2))
print(f"The length of the height is: {round(h, 2)}")









