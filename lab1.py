# PYTHON VARIABLES

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Variable names

    #Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

    #Illegal variable names:
"""
2myvar = "John"
my-var = "John"
my var = "John
"""

    # Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# Result:
 # Orange
 # Banana  
 # Cherry

    # One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)
# Result:
 # Orange
 # Orange
 # Orange

    # Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
# Result:
 #apple
 #banana
 #cherry
 


    # Output Variables
x = "Python is awesome"
print(x)
# Result:
 # Python is awesome

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
# Result:
 # Python is awesome

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
# Result:
 # Python is awesome

#Notice the space character after "Python " and "is ", without them the result would be "Pythonisawesome"

x = 5
y = 10
print(x + y)
# Result:
 # 15

"""
x = 5
y = 10
print(x + y)
"""
# Result:
 # TypeError: unsupported operand type(s) for +: 'int' and 'str'

x = 5
y = "John"
print(x, y)
# Result:
 # 5 John



    #Global Variables
x = "awesome" # global variable

def myfunc():
  print("Python is " + x)

myfunc()
# Result:
 #Python is awesome


#Create a variable inside a function, with the same name as the global variable
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
# Result:
 #Python is fantastic
 #Python is awesome
 

#If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# Result:
 # Python is fantastic


#To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
# Result:
 # Python is fantastic

