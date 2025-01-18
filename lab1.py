# PYTHON DATA TYPES

"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""


# Print the data type of the variable x:
x = 5
print(type(x))
# Result:
 # <class 'int'>


x = "Hello World"	#res: "str"	
x = 20	#res: "int"	
x = 20.5	#res: "float"	
x = 1j	#res: "complex"	
x = ["apple", "banana", "cherry"]	#res: "list"	
x = ("apple", "banana", "cherry")	#res: "tuple"	
x = range(6)	#res: "range"	
x = {"name" : "John", "age" : 36}	#res: "dict"	
x = {"apple", "banana", "cherry"}	#res: "set"	
x = frozenset({"apple", "banana", "cherry"})	#res: "frozenset"	
x = True	#res: "bool"	
x = b"Hello"	#res: "bytes"	
x = bytearray(5)	#res: "bytearray"	
x = memoryview(bytes(5))	#res: "memoryview"	
x = None	#res: "NoneType"


# If you want to specify the data type, you can use the following constructor functions:

x = str("Hello World")	#res: str	
x = int(20)	#res: int	
x = float(20.5)	#res: float	
x = complex(1j)	#res: complex	
x = list(("apple", "banana", "cherry"))	#res: list	
x = tuple(("apple", "banana", "cherry"))	#res: tuple	
x = range(6)	#res: range	
x = dict(name="John", age=36)	#res: dict	
x = set(("apple", "banana", "cherry"))	#res: set	
x = frozenset(("apple", "banana", "cherry"))	#res: frozenset	
x = bool(5)	#res: bool	
x = bytes(5)	#res: bytes	
x = bytearray(5)	#res: bytearray	
x = memoryview(bytes(5))	#res: memoryview