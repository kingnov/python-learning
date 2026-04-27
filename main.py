
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


# hyp = float(input("Enter the length of the hypotenuse: "))

# b = float(input("enter the length of the base: "))

# h = math.sqrt(math.pow(hyp, 2) - math.pow(b, 2))
# print(f"The length of the height is: {round(h, 2)}")


# if = Do some code only if some condition id True
#.    Else = Do somethoing else


# age = int(input("Enter your age: "))
# if age >= 18:
#     print("You are now signed up for the newsletter!")
# elif age < 0:
#     print("Invalid age")
# elif age >= 100:
#     print("You are too old to sign up for the newsletter")
# else:
#     print("Sorry, you must be atleast 18 years and above")

# response = input("Would you like food? (yes/no): ")
# if response.lower() == "yes":
#     print("Here is some food for you: ")
# elif response.lower() == "no":
#     print("Okay, maybe next time!")
# else:
#     print("Invalid response please enter yes or no")

# name = input("Enter your name: ")
# if name == "":
#     print("You did not enter a name!")
# else:
#     print(f"Hello {name}!")

# for_sale = input("Is this item for sale? (yes/no):")
# if for_sale.lower() == "yes":
#     price = float(input("Enter the price of the item: "))
#     print(f"The price of the item is: ${price}")
# elif for_sale.lower() == "no":
#     print("This item is not for sale")
# else:
#     print("Invalid response please enter yes or no")

# online = False
# if online:
#     print("The user is online")
# else:
#     print("The user is offline")

# Python Calculator

# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operator = input("Enter an operator (+, -, *, /): ")

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     result = num1 / num2
# else:
#     print("Invalid operator")

# print(f"The result is: {result}")

#Python weight converter
# weight = float(input("Enter your weight: "))
# unit = input("Kilogram or Pounds? (K or lb): ")

# if unit.lower() == "k":
#     converted_weight = weight * 2.205
#     print(f"Your weight is: {converted_weight} lbs")

# elif unit.lower() == "lb":
#     converted_weight = weight / 2.205
#     print(f"Your weight is: {converted_weight} kg")

# else:
#     print("Invalid unit")


# temp = float(input("Enter temperature: "))
# unit = input("Is tis temperature in celcius or fahrenheit? (C or F): ")
# if unit.lower() == "c":
#     converted_temperature = (temp * 9/5) + 32
#     print(f"The temperature in fahrenheit is: {converted_temperature} F")
# elif unit.lower() == "f":
#     converted_temperature = (temp - 32) * 5/9
#     print(f"The temperature in celcius is: {converted_temperature} C")
# else:
#     print("Invalid unit")

# logial operators = evaluate multiple conditions at the same time (and, or, not)
#                    or = at least one condition is true
#                    and = all conditions must be true
#                    not = reverses the result, returns false if the result is true

# temp = 25
# is_raining = False
# if temp > 35 or temp < 0 or is_raining:
#     print("the outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled to take place")

# temp = 25
# is_sunny = True
# if temp >+ 30 and is_sunny:
#     print("Its a great day for the picnic")
#     print("It is SUNNY 🌞")
# elif temp <= 0 and is_sunny:
#     print("Its cold outside")
#     print("It is CLOUDY ☁️")
# elif temp < 30 and temp > 0 and is_sunny:
#     print("It's a nice day for the picnic")
#     print("It is PARTLY CLOUDY 🌤️")
# elif temp <= 0 and not is_sunny:
#     print("Its cold outside")
#     print("It is CLOUDY ☁️")
# elif temp < 30 and temp > 0 and not is_sunny:
#     print("It's a nice day for the picnic")
#     print("It is CLOUDY ☁️")

# conditional expression = A one-line shortcut for the if-else statement (ternary operator)
#.                         print or assign one of two values based on a condition
#.                         X if condition else Y

# num = 5
# print("Positive" if num > 0 else "Negative")

# num = 6
# a = 6
# b = 7
# age = 25
# temp = 30
# user_role = "admin"

# print("EVEN" if num % 2 == 0 else "ODD")
# max_num = a if a > b else b
# print(f"The maximum number is: {max_num}")
# status = "Adult" if age >= 18 else "Minor"
# print(f"You are an {status}")
# weather = "HOT" if temp >+ 27 else "COLD"
# print(f"The weather is: {weather}")
# access_level = "Full Access" if user_role == "admin" else "Limited Access"
# print(f"Your access level is: {access_level}")

# strings
# name = input("Enter your full name: ")
# result = len(name)
# print(f"Your name has {result} characters")
# result = name.find(" ") # find the index of the first space character
# print(f"The index of the space character is: {result}")
# result = name.rfind("i") # find the index of the last space character
# print(f"The index of the last space character is: {result}")
# name = name.capitalize() # capitalize the first letter of each word

# name = name.upper() # convert the name to uppercase
# name = name.lower()
# result = name.isdigit() # check if the name contains only digits
# print(result)

# result = name.isalpha() # check if the name contains only letters
# print(result)
# print(f"Hello {name}!")

# phone_number = input("Enter your phone number: ")
# # result = phone_number.count("-") # count the number of dashes in the phone number
# print(f"The number of dashes in the phone number is: {result}")
# phone_number = phone_number.replace("-", " ") # replace dashes with spaces
# print(f"Your phone number is: {phone_number}")

# validate user input exercise
# username is not more than 12 characters
#username must not contain spaces
#username must not contain digits

# username = input("Enter a username: ")
# if len(username) > 12:
#     print("Username must not be more than 12 characters")
# elif " " in username:
#     print("The username must not contain spaces")
# elif any(char.isdigit() for char in username):
#     print("The username must not contain digits")
# else:
#     print(f"username {username} is valid!")

# String indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]
# credit_number = "1234-5678-9012-3456"
# print(credit_number[0])
# print(credit_number[0:4])
# print(credit_number[5:9])
# print(credit_number[5:])
# print(credit_number[-1])
# print(credit_number[::2]) # print every other character
# last_digits = credit_number[-4:]
# print(f"XXXX-XXXX-XXXX-{last_digits}")
# credit_number = credit_number[::-1] # reverse the string
# print(credit_number)


# format specifiers = {:flags} format a value based on what 
#                               flags are inserted

# .(number)f = format a number to a fixed number of decimal places
# :(number) = format a number to a fixed width (padding with spaces)
# :03 = format a number to a fixed width and pad with zeros
# :< = left align the value within the specified width
# :> = right align the value within the specified width
# :^ = center align the value within the specified width
# :+ = include a plus sign for positive numbers
# :, = include a comma as a thousand separator
# := = place the sign before the number and any padding after the sign
# :  = insert a space before positive numbers and a minus sign before negative numbers

# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34

# print(f"Price 1 is: {price1:.2f}")
# print(f"Price 2 is: {price2:+.2f}")
# print(f"Price 3 is: {price3:10.2f}")

# while loop = execute some code WHILE some condition remain true
# name = input("Enter your name: ")
# while name == "": #while this condition remains true,
#     print("You did not enter a name!")# execute this code forever
#     name = input("Enter your name: ")
# print(f"Hello {name}!")

# age = int(input(f"Enter your age: "))
# while age < 0:
#     print("Invalid age! Age cannot be negative.")
#     age = int(input(f"Enter your age: "))
# print(f"You are {age} years old!")

# food = input("What is your favorite food? (q to quit): ")
# while not food.lower() == "q":
#     print(f"You like {food}")
#     food = input("What is your another favorite food? (q to quit): ")
# print("bye!")

# num = int(input("Enter a number between 1 - 10: "))
# while num < 1 or num > 10:
#     print("Invalid number! Please enter a number between 1 and 10.")
#     num = int(input("Enter a number between 1 - 10: "))
# print(f"You entered: {num}")

# Python compound interest calculator

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle cant be less than or equal to zero")
while rate <= 0:
    rate = float(input("Enter the interest rate (as a percentage): "))
    if rate <= 0:
        print("Rate cant be less than or equal to zero")
while time <= 0:
    time = int(input("Enter the time (in years): "))
    if time <= 0:
        print("Time cant be less than or equal to zero")
# print(f"Principle: ${principle}")
# print(f"Rate: {rate}%")
# print(f"Time: {time} years")

Total_amount = principle * pow(1 + (rate / 100), time)
# Total_amount = principle * (1 + (rate / 100)) ** time
print(f"The total amount after {time} years is: ${Total_amount:.2f}")



