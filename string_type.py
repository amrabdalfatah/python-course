# Strings
# collection of characters (list)
# single quote or double quote
x = 'Hello' # "Hello"
# Multiline Strings
info = '''
Hello,
My name is Amr
'''
# Looping through a string
#for i in info:
#   print(i)

# Check String
txt = "My name is Amr"
# if "Adel" not in txt:
#     print("Adel is in txt")

# Slicing 
b = 'Hello, World My name is Amr'
# print(b[2:5]) Slice part of text
# print(b[:5]) Slice from start text to specific part
# print(b[2:]) Slice from specific part to end
# print(b[-4:-1]) Slice from end using negative

# Method 
# 1- upper() => all capital
# 2- lower() => all small
# 3- strip() => remove any whitespace from the beginning or the end
# 4- replace() => replace('H', 'E')
# 5- split() => split(separator) may be whitespace or ,
# 6- format()
first_name = 'Amr'
last_name = 'Abdalfatah'
age = 30
height = 175
weight = 75
full_name = first_name + " " + last_name
bio = full_name + " and my age {1} and my height is {0} and my weight is {2} "
print(bio.format(height, age, weight))