"""
Python Classes/Objects

Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.
"""
# Create a Class
# To create a class, use the keyword class:

class MyClass:
    x = 5

# Create Object
# Now we can use the class named MyClass to create objects:

# Example
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)

"""
The __init__() Method

The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
To understand the meaning of classes we have to understand the built-in __init__() method.
All classes have a method called __init__(), which is always executed when the class is being initiated.
Use the __init__() method to assign values to object properties, or other operations that are necessary to do when the 
object is being created:
"""
# Example

# Create a class named Person, use the __init__() method to assign values for name and age:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
p1 = Person("John", 36)

print(p1.name)
print(p1.age)

# Note: The __init__() method is called automatically every time the class is being used to create a new object.

"""
The __str__() Method

The __str__() method controls what should be returned when the class object is represented as a string.
If the __str__() method is not set, the string representation of the object is returned:
"""
# Example
# The string representation of an object WITHOUT the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1)

# Example
# The string representation of an object WITH the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1) 

