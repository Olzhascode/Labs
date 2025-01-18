# Python - Slicing Strings

# Slicing
b = "Hello, World!"
print(b[2:5])
# result: llo

# Slice From the Start
b = "Hello, World!"
print(b[:5])
# result: Hello

# Slice To the End
b = "Hello, World!"
print(b[2:])
# result: llo, World!

# Negative Indexing

#Get the characters:
#From: "o" in "World!" (position -5)
#To, but not included: "d" in "World!" (position -2):
b = "Hello, World!"
print(b[-5:-2])
# result: orl



# Modify Strings

# Upper Case
a = "Hello, World!"
print(a.upper())
# result: HELLO WORLD

# Lower Case
a = "Hello, World!"
print(a.lower())
# result: hello world

# Remove Whitespace
a = " Hello, World! "
print(a.strip())
# result: "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))
# result: Jello, World!

# Split String
a = "Hello, World!"
print(a.split(",")) 
# result: ['Hello', ' World!'] 



# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)
# Result: HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c)
# Result: Hello World



# Format - Strings
age = 36
#txt = "My name is John, I am " + age
#print(txt)
# Result: TypeError we can't concatenate a string with int

#F-Strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# Result: My name is John, I am 36

# Placeholders and Modifiers
price = 59
txt = f"The price is {price} dollars"
print(txt)
# Result: The price is 59 dollars

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)
# Result: The price is 59.00 dollars

txt = f"The price is {20 * 59} dollars"
print(txt)
# Result: The price is 1180 dollars



# Escape Character
txt = "We are the so-called \"Vikings\" from the north."
# Result: We are the so-called "Vikings" from the north.
# Escape sequences in Python

# Single Quote
print('It\'s a sunny day')  # res: It's a sunny day

# Backslash
print("This is a backslash: \\")  # res: This is a backslash: \

# New Line
print("Hello\nWorld")  # res:
# Hello
# World

# Carriage Return
print("Hello\rWorld")  # res: World  (The text "Hello" is overwritten by "World")

# Tab
print("Hello\tWorld")  # res: Hello    World (with a tab space between)

# Backspace
print("Hello\b World")  # res: Hell World (removes the character before \b)

# Form Feed
print("Hello\fWorld")  # res: Hello
#        World (Page feed: moves to the next line with spacing)

# Octal Value
print("\110\145\154\154\157")  # res: Hello (Octal representation of ASCII codes)

# Hex Value
print("\x48\x65\x6C\x6C\x6F")  # res: Hello (Hexadecimal representation of ASCII codes)





# String methods

# Examples of all string methods in Python
s = "hello world"
s2 = "HELLO"
s3 = "123"
s4 = "   hello   "
s5 = "hello\tworld"
s6 = "hello\nworld"
s7 = "hello world python"

# 1. capitalize()
print(s.capitalize())  # res: "Hello world"

# 2. casefold()
print(s2.casefold())  # res: "hello"

# 3. center()
print(s.center(20, '-'))  # res: "-----hello world-----"

# 4. count()
print(s.count("hello"))  # res: 1

# 5. encode()
print(s.encode())  # res: b'hello world'

# 6. endswith()
print(s.endswith("world"))  # res: True

# 7. expandtabs()
print(s5.expandtabs(4))  # res: "hello   world"

# 8. find()
print(s.find("world"))  # res: 6

# 9. format()
print("Hello, {}!".format("Kesha"))  # res: "Hello, Kesha!"

# 10. format_map()
data = {"name": "Kesha"}
print("Hello, {name}!".format_map(data))  # res: "Hello, Kesha!"

# 11. index()
print(s.index("world"))  # res: 6

# 12. isalnum()
print("hello123".isalnum())  # res: True

# 13. isalpha()
print("hello".isalpha())  # res: True

# 14. isascii()
print(s.isascii())  # res: True

# 15. isdecimal()
print(s3.isdecimal())  # res: True

# 16. isdigit()
print(s3.isdigit())  # res: True

# 17. isidentifier()
print("hello_world".isidentifier())  # res: True

# 18. islower()
print(s.islower())  # res: True

# 19. isnumeric()
print(s3.isnumeric())  # res: True

# 20. isprintable()
print(s.isprintable())  # res: True

# 21. isspace()
print("   ".isspace())  # res: True

# 22. istitle()
print("Hello World".istitle())  # res: True

# 23. isupper()
print(s2.isupper())  # res: True

# 24. join()
print("-".join(["hello", "world"]))  # res: "hello-world"

# 25. ljust()
print(s.ljust(20, '-'))  # res: "hello world--------"

# 26. lower()
print(s2.lower())  # res: "hello"

# 27. lstrip()
print(s4.lstrip())  # res: "hello   "

# 28. maketrans() and translate()
trans = str.maketrans("h", "j")
print(s.translate(trans))  # res: "jello world"

# 29. partition()
print(s.partition(" "))  # res: ('hello', ' ', 'world')

# 30. replace()
print(s.replace("world", "Python"))  # res: "hello Python"

# 31. rfind()
print(s.rfind("o"))  # res: 7

# 32. rindex()
print(s.rindex("o"))  # res: 7

# 33. rjust()
print(s.rjust(20, '-'))  # res: "--------hello world"

# 34. rpartition()
print(s.rpartition(" "))  # res: ('hello', ' ', 'world')

# 35. rsplit()
print(s7.rsplit(" ", 1))  # res: ['hello world', 'python']

# 36. rstrip()
print(s4.rstrip())  # res: "   hello"

# 37. split()
print(s.split())  # res: ['hello', 'world']

# 38. splitlines()
print(s6.splitlines())  # res: ['hello', 'world']

# 39. startswith()
print(s.startswith("hello"))  # res: True

# 40. strip()
print(s4.strip())  # res: "hello"

# 41. swapcase()
print(s2.swapcase())  # res: "hello"

# 42. title()
print(s.title())  # res: "Hello World"

# 43. translate() (already shown in maketrans)
print(s.translate(trans))  # res: "jello world"

# 44. upper()
print(s.upper())  # res: "HELLO WORLD"

# 45. zfill()
print(s3.zfill(5))  # res: "00123"
