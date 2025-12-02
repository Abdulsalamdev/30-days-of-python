# Questions 
# Exercises - Day 1
# 1. Check the python version you are using
# 2. Open the python interactive shell and do the following operations. The operands are 3 and 4.
#       addition(+)
#       subtraction(-)
#       multiplication(*)
#       modulus(%)
#       division(/)
#       exponential(**)
#       floor division operator(//)
# 3. Write strings on the python interactive shell. The strings are the following:
#       Your name
#       Your family name
#       Your country
#       I am enjoying 30 days of python
# 4. Check the data types of the following data:
#       10
#       9.8
#       3.14
#       4 - 4j
#       ['Asabeneh', 'Python', 'Finland']
#       Your name
#       Your family name
#       Your country
# 5. Write an example for different Python data types such as Number(Integer, Float, Complex), String, Boolean, List, Tuple, Set and Dictionary.
# 6. Find an Euclidian distance between (2, 3) and (10, 8)
import math
print("Welcome to 30 days of python")
# Solution 
# 1 python --version
# 2
# addition
print(3+4)
# subtraction
print(4-1)
# multiplication
print(3*4)
# modulus
print(3 % 2)
# didsion
print(3 / 2)
# exponential
print(2**3)
# floor division operator
print(5 // 3)

# 3
name = "Abdulsalam"
familyName = "Akinyoola"
country = "Nigeria"
current = "i am enjoying 30 days of pyhon"

# 4 
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4 - 4j))
print(type(["Asabeneh","python","finland"]))
print(name)
print(familyName)
print(country)

# 5
string = "Silent Architect"
integer = 9
floats = 3.55
complexs = 4 - 4j
boolean  = True
List = ["Abdul", "salam", "silent", "Architect"]
Tuple = ("Abdul", "salam", "silent", "architect")
Set = {"name", "school", "level"}
Dictionalry = {
    "name": "Abdulsalam",
    "school": "FUTA",
    "nickname": "Silent Architect"
}

# 6 Find an Euclidian distance between (2, 3) and (10, 8)
distance1 = (2,3)
distance2 = (10,8)

dx = distance2[0] - distance1[0]
dy = distance2[1] - distance1[1]

sum_square = dx**2 + dy**2

result = math.sqrt(sum_square)
print(result)