# PYTHON STRINGS


#'hello' is the same as "hello".

print("Hello")
print('Hello')
# Result will be same "Hello"


# Quotes Inside Quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')
# Result:
 # It's alright
 # He is called 'Johnny'
 # He is called "Johnny"


 # Assign String to a Variable

a = "Hello"
print(a)
# Result:
 # Hello 


# Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Result:
"""Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""


# You can use single quotes result will be same
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#  in the result, the line breaks are inserted at the same position as in the code.


# Strings are Arrays

a = "Hello, World!"
print(a[1]) #res: e

#Loop through the letters in the word "banana":
for x in "banana":
  print(x)
# Result:
"""
b
a
n
a
n
a
"""

# String Length

# The len() function returns the length of a string:

a = "Hello, World!"
print(len(a))
# Result:
# 13

# Check String

txt = "The best things in life are free!"
print("free" in txt)
# Result: True

# Print only if "free" is present:

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
# Result: Yes, 'free' is present.

# Check if NOT

txt = "The best things in life are free!"
print("expensive" not in txt)
# Result: True

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
# Result: No, 'expensive' is NOT present.