# Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
thirty = "Thirty "
days = "Days "
of = "of "
python = "Python"

concantinated = thirty + days + of + python
# print(concantinated)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
single = "Coding " + "For" + " All"
# print(single)
# Declare a variable named company and assign it to an initial value "Coding For All".
company = single
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
company.upper()
# Change all the characters to lowercase letters using lower() method.
company.lower()
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company.capitalize()
print(company.title())
# Cut(slice) out the first word of Coding For All string.
print(company[0:7])
# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company.startswith("Coding"))
# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace("Coding For All","Python"))
# Split the string 'Coding For All' using space as the separator (split()) .
print(company.split(" "))
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(", "))
# What is the character at index 0 in the string Coding For All.
# C
# What is the last index of the string Coding For All.
# l
# What character is at index 10 in "Coding For All" string.
# 
# Create an acronym or an abbreviation for the name 'Python For Everyone'.
pfe = 'Python For Everyone'
# Create an acronym or an abbreviation for the name 'Coding For All'.
cfa = 'Coding For All'
# Use index to determine the position of the first occurrence of C in Coding For All.
cfa.find("C")
# Use index to determine the position of the first occurrence of F in Coding For All.
cfa.find("F")
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
cfa.rfind("l")
# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.rfind('because'))
# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'[31:54])
# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print('You cannot end a sentence with because because because is a conjunction'.find("because"))
# Does ''Coding For All' start with a substring Coding?
print("Coding For All".startswith("Coding"))
# Does 'Coding For All' end with a substring coding?
print("Coding For All".endswith("coding"))
# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
print('   Coding For All      '.strip())
# Which one of the following variables return True when we use the method isidentifier():
# 30DaysOfPython
# thirty_days_of_python -> this
# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
web_tech = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = "# ".join(web_tech)
print(result)
# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")
# Use a tab escape sequence to write the following lines.
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
print(f"The area of a circle with radius {radius} is {area} meters square.")
# Make the following using string formatting methods:
# 8 + 6 = 14
print("{} + {} = {}".format(8,6,14))
# 8 - 6 = 2
print("{} - {} = {}".format(8,6,2))
# 8 * 6 = 48
print("{} * {} = {}".format(8,6,48))
# 8 / 6 = 1.33
print("{} / {} = {}".format(8,6,1.33))
# 8 % 6 = 2
print("{} % {} = {}".format(8,6,2))
# 8 // 6 = 1
print("{} // {} = {}".format(8,6,1))
# 8 ** 6 = 262144
print("{} ** {} = {}".format(8,6,262144))
# 🎉 CONGRATULATIONS ! 🎉

