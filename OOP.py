# ----------------- CLASSES -----------------

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"You drove {miles} miles")

    def describe_car(self):
        print(f"This car is a {self.year} {self.brand} {self.model} with {self.mileage}")

# class EmailClient : #this is a class with two names to name a class with two words we use pascal case so we capitalize the first char of each word we dont use "_"
class EmailClient:
    pass

class Point:
    def Move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
point1.Move()
point1.draw()
print(point1.x)  # this will print 10
print(point1.y)  # this will print 20
point1.draw()  # this will print draw

# to call a method we use the dot operator and the name of the method
# to access an attribute we use the dot operator and the name of the attribute
# to create an object we use the class name and the parentheses

# Constructors

class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point6 = Point2(20, 1)

# example

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):
        print(f"hello world {self.name}")

jhon = person("hamdi adem", 10)
jhon.talk()  # this will print hello world

# inheritance
# we use inheritance so we dont rewrite or duplicate or write again the same code in different classes
# we can inherit from one class to another class
# there is a lot of types of inheritance in python
# the easiest one is single inheritance

class Mamall():
    def walk(self):
        print("walk")

class Animal(Mamall):
    def eat(self):
        print("eat")
    # we can either use pass if we dont want to add anything else or we create another special method for this class
    pass  # here we used pass

dog = Animal()
dog.walk()  # this will print walk which he iherited it from Mamall class
dog.eat()  # this will print eat

# ----------------- Part TWO -----------------------
# Polymorphism ( multi faces)

# --------------- Al Zero OOP course --------------------------

class Member:
    def __init__(self, name):
        print(f"hello member {name} ")

Member("jack")  # calling the function in jack as a class of member
# printing hello member jack
print(dir(Member))

member21 = Member("jack")
print(member21.__class__)

# ------------- instance attributes and methods ------------------
# it is the same written up there just creating method(functions) inside class

# -------------- Class Attributes ----------------------------------

class car:
    # this type of this are always defined outside the constructor
    not_allowed_names = ["9awd", "ta7an", "rkhis"]
    users_number = 0

    def __init__(self, name, number, price):
        self.name = name
        self.price = price
        self.number = number
        car.users_number += 1

    def speak(self):
        if self.name in car.not_allowed_names:
            raise ValueError("this name is not allowed ")
            # we always use 'raise ' to raise an error
        else:
            print(f"hi {self.name}")
            print(f"the number of users is {car.users_number}")

# ---------- class method and static method ----------------------------
# usong this method it means we are declaring a method function that takes cls(class) as an argument not a any argument that u take the instance that u created
    @classmethod
    # in this way we are creating methods and no need to create your own object
    def show_user_count(cls):
        print(f"hello this the number of users {cls.users_number} in the system")
        # this way we user users_number with creating a method

    @staticmethod
    # this is a method that does not take any argument and does not use the class or instance
    def show_info():  # we didnt use arguments because it had relation to class not to instance
        print("this is a static method ")

# -------------------------------- Magic Methods -------------------------------
# Everything in python is an Object
# __str__ give u a human readable output of the object
# __len__ return the length of the container or the object of type class
# ---------it is called when we use built in function len() on the object

class skill:
    def __init__(self):
        self.Skills = ["html", "jack", "9ador"]

    def __str__(self):
        return f"skill name is {self.Skills}"
    # we can use this method to print the object like this

    def __len__(self):
        return len(self.Skills)

profile = skill()
print(profile)
print(len(profile))  # this will print the number of skills in the list

profile.Skills.append("PHP")
profile.Skills.append("MySql")
print(len(profile))

# ------------------------ inheritance -----------------------

class Mamalll():
    def __init__(self, name):
        self.name = name

    def walk4(self):
        print(f"walk {self.name}")

class Animal2(Mamalll):
    def __init__(self, name):
        # Mamall.__init__(self,name) # create instance from base class
        super().__init__(name)  # this does the same thing as the line in front of it
        print(f"eat {self.name}")

# this way we can iherit the name used in first class to second class and result :
food_two = Animal2("jack")
food_two.walk4()  # the result is walk jack

