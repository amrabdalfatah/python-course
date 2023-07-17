# Variables
# are containers for storing data values
# creating a variable 
name = 'amr'
# to see the data type of any variable you can use 
# type(name_variable)
type(name)
# single or double qoute when defined a string
x = "ahmed"
# case sensitive
a = 4
A = 5
# name of variables
# 1- must start with a letter or underscore(_)
# 2- cannot start with a number
# 3- contain a number or underscore
# 4- cannot include space when define 2 words in the name 
first_name = 'amr'
# Many values to multiple variables 
first_name, second_name = 'amr', 'adel'
# one value to multiple variables 
x = y = z =  'orange'
# unpack collection {list, tuple, set, dict}
fruits = ['apple', 'banana', 'orange']
x, y, z = fruits
# output variables
# print()
x = 5
y = 'amr'
# Global Variables
address = 'Cairo'

def info():
    x = 5 # Local Variable 
    global address_two
    address_two = 'Egypt' 
    print(address_two)

info()
print(address_two)