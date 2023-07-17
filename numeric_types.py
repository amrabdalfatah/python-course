# Numeric Types:
# int, float, complex
# int
x = 10
y = -200
z = 100000000
# float
x = 10.0 
y = 12.6
z = -14.9
x = 35e3
# complex
x = 3 + 5j
# Type Conversion
# convert from int to float
x = 1
a = float(x)
# conver from float to int
x = 1.9
a = int(x)
# convert from int to complex
x = 10
a = complex(x)
# convert from float to complex
x = 12.8
a = complex(x)
# convert from complex to int or float(not acceptable)

# Random Numbers
# Python doesn't have random()
# Python has a random Module
import random
x = random.randrange(1, 100)
print(x)