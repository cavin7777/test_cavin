x = int(3)
x = 5
y = str(3)
y = "John"

x = 8 # x is now 5
print(x)
print(y)

z = float(3)

print(z)

print(type(x))

c = 'cavin'
#same
c = "cavin"

b = 'hello'
#is not same
B = 'world'

print(b, B)

#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" 

#Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John" 

x, y, z = 'Orange', 'Banana', 'Apple'
print(x, y, z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
# x = 5
# y = "John"
# print(x + y)

x = 5
y = "John"
print(x, y)

a = 'Hello'
b = 'World'
print(a + b)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function. The global variable with the same name will remain as it was, 
# global and with the original value.

x = "great"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x) 

# If you use the global keyword, the variable belongs to the global scope:
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 

x = list(("apple", "banana", "cherry"))
y = tuple(("apple", "banana", "cherry"))
z = set(("apple", "banana", "cherry"))

print(x)
print(y)
print(z)

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z)) 

"""
Random Number

Python does not have a random() function to make a random number, but Python has a built-in module called
random that can be used to make random numbers:

Example
Import the random module, and display a random number from 1 to 9:
import random

print(random.randrange(1, 10))
""" 