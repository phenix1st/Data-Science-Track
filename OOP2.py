# ------------------ @property in OOP -----------------------
class Circle:
    def __init__(self, radius):
        self._radius = radius  # Internal attribute

    @property
    def radius(self):
        """The radius property."""
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self._radius = value

    @radius.deleter
    def radius(self):
        del self._radius

# Usage
my_circle = Circle(5)
print(my_circle.radius)  # Calls the getter

my_circle.radius = 10   # Calls the setter
print(my_circle.radius)

# my_circle.radius = -2 # This would raise a ValueError

del my_circle.radius    # Calls the deleter
# print(my_circle.radius) # This would raise an AttributeError now


# ---------------- OOP ABC Abstract Base Classes ------------------------ 
# Class is called abstract class if it has one or more abstract methods
# abc module in python provides infrustracture by defining abstract base classes
# By Adding @abstractMethod Decorator on the Methods
# ABCMeta Class is a metaclass used for defining absract classes 
# ------------------- Example & explination -------------------------------

from abc import ABCMeta, abstractmethod

# Define an abstract class
class Animal(classmethod = ABCMeta): 
    
    @abstractmethod
    def sound(self):
        pass  # This is an abstract method, no implementation here.

# Concrete subclass of Animal
class Dog(Animal):
    
    def sound(self):
        return "Bark"  # Providing the implementation of the abstract method

# Create an instance of Dog
dog = Dog()
print(dog.sound())  # Output: Bark