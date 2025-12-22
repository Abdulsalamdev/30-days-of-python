#  Exercises - Day 3
# Declare your age as integer variable
age = 19
# Declare your height as a float variable
height = 166.9
# Declare a variable that store a complex number
complexNumber = (1 + 1j) # type: ignore
# Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base = int(input("Enter base: "))
height = int(input("Enter height: "))

area = 0.5 * base * height
print(f"The area of a triangle is : {area}")
#     Enter base: 20
#     Enter height: 10
#     The area of the triangle is 100
# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))
perimeter = a + b+ c
print(f"The perimeter of a trinagle is {perimeter}")
# Enter side a: 5
# Enter side b: 4
# Enter side c: 3
# The perimeter of the triangle is 12
# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input("Enter the Length: "))
width = int(input("Enter the width: "))
area = length * width
perimeter = 2 * (length * width)
# Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.14
r = int(input("Enter the radius: "))
area = pi * r * r 
circumference = 2 * pi * r
# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
print(len("python") == len("dragon"))
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print("on" in "python" and "dragon")
# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
print("jargon" in "I hope this course in not full of jargon")
# Find the length of the text python and convert the value to float and convert it to string
pyLength = len("python")
toFloat = float(pyLength)
toString = str(toFloat)
# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
numbers = int(input("enter number: "))
checkEven = numbers % 2 == 0
print(checkEven)
# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
div = 7 // 3
print(int(div))
# Check if type of '10' is equal to type of 10
print(type(10))
# Check if int('9.8') is equal to 10
print(type(int(9.8)) == type(10))
# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
hours = int(input("Enter Hours: "))
rate = int(input("enter rate per hours: "))
weekEarn = hours * rate
print(f"Your weekly earning is {weekEarn}")
# Enter hours: 40
# Enter rate per hour: 28
# Your weekly earning is 1120
# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
years = int(input("Enter number of years you have lived: "))
# Enter number of years you have lived: 100
convertYearToSecond = years * 365 * 24 * 60 * 60 
# You have lived for 3153600000 seconds.
# Write a Python script that displays the following table
for i in range(1,6):
    print(i,1, i, i**2, i**3)
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# 🎉 CONGRATULATIONS ! 🎉