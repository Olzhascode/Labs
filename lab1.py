# PYTHON NUMBERS

# There are three numeric types in Python:
# int
# float
# complex


# Example
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.
x = 1
y = 35656222554887711
z = -3255522

print(type(x)) #res: class, int
print(type(y)) #res: class, int
print(type(z)) #res: class, int


# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = x = 1.10
y = 1.0
z = -35.59

print(type(x)) #res: class, float
print(type(y)) #res: class, float
print(type(z)) #res: class, float


# Float can also be scientific numbers with an "e" to indicate the power of 10.

x = 35e3
y = 12E4
z = -87.7e100

print(type(x)) #res: class, float
print(type(y)) #res: class, float
print(type(z)) #res: class, float


# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x)) #res: class, complex
print(type(y)) #res: class, complex
print(type(z)) #res: class, complex

# Note: You cannot convert complex numbers into another number type.


"""Python does not have a random() function to make a random number,
 but Python has a built-in module called random that can be used to make random numbers:"""

import random

print(random.randrange(1, 10))
# result random num [1, 10)