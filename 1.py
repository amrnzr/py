#HOME
print ("Hello, world!")

#SYNTAX
if 5>2:
    print ("Five is a greater than two!")

#COMMENTS
"""
This is a comment
written in more than just one line
"""
print ("Hello, world!")

#VARIABLES
x = 5
y = "John"
print (x)
print (y)

x=5
y = "John"
print(type(x))
print(type(y))

#VARIABLE NAMES
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#ASSIGN MULTIPLE VALUES
fruits = ["apple", "banana", "cherry"]
x, y, z =fruits
print (x)
print (y)
print (z)

#OUTPUT VARIABLES 
x=5
y=10
print (x+y)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#GLOBAL VARIABLE
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


x="awesome"

def myfunc():
    global x
    x ="fantastic"
myfunc()

print ("Python is " + x)

#DATA TYPE
x=5
print (type(x))

#NUMBERS
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

#STRINGS
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print (a)

#SLICING STRING
b = "Hello, World!"
print(b[2:5])

#MODIFY 
#upper 
a = "Hello, World!"
print(a.upper())
#lower
a = "Hello, World!"
print(a.lower())
#remove
a = " Hello, World!   "
print (a.strip())
#replace
a = "Hello, World!"
print (a.replace("H", "J"))
#split
a = "Hello, World!"
print (a.split(","))

#STRING CONCATENATION
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#FORMAT STRING 
age = 36
txt = f"My name is John, I am {age}"
print(txt)

#ESCAPE
txt = "We are the so-called \"Vikings\" from the north."
print(txt) 