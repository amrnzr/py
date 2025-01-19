#Python Home
print("Hello, World!")

#Python Intro
print("Hello World!")

#Python Get Started
print("Hello, World!")
#Check the Python version of the editor:
import sys
print(sys.version)

#Python Syntax
if 5 > 2:
    print("Five is greater than two!")
if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")

#Python Comments
#This is a comment
print("Hello, World!")
print("Hello, World!") #This is a comment
"""
This is a commment
written in 
more than just one line
"""
print("Hello, World!")

#Python Variables
x = 5
y = "John"
print(x)
print(y)

x = 4
x = "Sally"
print(x)   #Sally

x = str(3)    # '3'
y = int(3)    # 3
z = float(3)  # 3.0

x = 5
y = "John"
print(type(x))
print(type(y))
"""
<class 'int'>
<class 'str'>
"""

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#Python - Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Python Variables - Assign Multiple Values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
x = y = z = "Orange"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""
apple
banana
cherry
"""

#Python - Output Variables
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
x = 5
y = 10
print(x + y)
x = 5
y = "John"
print(x, y)

#Python - Global Variables
x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)
"""
Python is fantastic
Python is awesome
"""
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x) #Python is fantastic

#Python Data Types
"""
x = "Hello World"	str	
x = 20	int	
x = 20.5	float	
x = 1j	complex	
x = ["apple", "banana", "cherry"]	list	
x = ("apple", "banana", "cherry")	tuple	
x = range(6)	range	
x = {"name" : "John", "age" : 36}	dict	
x = {"apple", "banana", "cherry"}	set	
x = frozenset({"apple", "banana", "cherry"})	frozenset	
x = True	bool	
x = b"Hello"	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	
x = None	NoneType
"""

#Python Numbers
x = 1    # int
y = 2.8  # float
z = 1j   # complex
a = float(x)
b = int(y)
c = complex(x)
print(a)    # 1.0
print(b)    # 2
print(c)    # (1+0j)
#You cannot convert complex numbers into another number type.
#Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10))

#Python Casting
z = int("3") # z will be 3
z = float("3")   # z will be 3.0
z = str(3.0)  # z will be '3.0'

#Python Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
#or '''
a = "Hello, World!"
print(a[1])   #e
for x in "banana":
  print(x)
"""
b
a
n
a
n
a
"""
a = "Hello, World!"
print(len(a))    #13
txt = "The best things in life are free!"
print("free" in txt)    #True
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  #The same with not

#Python - Slicing Strings
b = "Hello, World!"
print(b[2:5])   #llo
print(b[:5])   #Hello
print(b[2:])   #llo, World!
print(b[-5:-2])   #orl

#Python - Modify Strings
a = "Hello, World!"
print(a.upper())   #HELLO, WORLD!
print(a.lower())
print(a.strip())   #returns "Hello, World!"
print(a.replace("H", "J"))  #Jello
print(a.split(","))  # returns ['Hello', ' World!']

#Python - Format - Strings
price = 59
txt = f"The price is {price} dollars"
txt = f"The price is {price:.2f} dollars"  #59.00
txt = f"The price is {20 * 59} dollars"  #1180
print(txt)

#Python - Escape Characters
txt = "We are the so-called \"Vikings\" from the north."
'''
\ooo	Octal value	
\xhh	Hex value
'''