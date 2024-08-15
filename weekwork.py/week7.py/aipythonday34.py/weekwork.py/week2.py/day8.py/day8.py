# Day 8 Python Fundamentals on GitHub
# Review of day before Object Oriented Programming
#Palindome of a string reverses it  word [::-1] can also do .reverse  edcba abcde
#Procedural Programming
# Constants i.e. pi 3.149 & gravitational force - Python does not suppport constants

class Car:
     def __init__(self, model, year, engine, doors, transmission, price) -> None:
          pass
     
# Properties of the car
carModel = ""
Year = ""
Engine = ""
Doors = ""
Transmission = ""
Price = ""

# Functions for a car vehicle using functional programming Take these and put them after class above,
def drive():
     pass
def reverse():
     pass
def park():
     pass
 
# Putting the actions into a car class - see code below

class Car: 
     def __init__(self, model, year, engine) -> None:# From here to line 32 is a constructor
          self.model = model 
          self.year = year
          self.engine =engine

     def drive(self):# It all was not working because it was not indented properly. 
          print(self.model + " is driving")

     def fly(self):
          print(self.model + " back to the future take off")

     def reverse(self):
          print(self.model + " can't reverse but will find a way")

     def park(self):
          print(self.model + " is parked in the park way")

honda = "my car" # string data type
honda = Car("Civic", 2024, "2000cc") # user defined data type = car
bmw = Car("520D", 2020, "2.0")
mercedes = Car("E400", 2024,"2.5")
               
honda.drive()
honda.park()
honda.reverse()

bmw.park()
bmw.drive()
bmw.reverse()

mercedes.drive()
mercedes.park()
mercedes.reverse()
mercedes.fly()

#C = create = settter
#R = Read = getter
#U = Update = setter
#D = Delete = setter

#A GETTER is like a Window can peek through the windown to view the date but cannot change it. 
#A SETTER is like a door that lets us change values. 
# GETTERS & SETTERS ARE USED FOR INTERACTING WITH EXTERNAL CODE i.e. setting permissions to change code these can set restrictions 
name = "Lorem" # setting
name = "Nick"  # Setting
name = "James" # Setting 
print (name) # getting

#balance = 1 million # a bank holder would be allowed to view but maybe not just ammend the bank balance
#balance = 2 million# so people cant just change the account need to have access rights on who can change it using getter and setter (set permissions) 


# class Rectangle:
#      def __init__(self, width, height):
#           self.width = width
#           self.height = height

# #Getter method
# def get_width(self):
#      return self._width

# def get_height (self, height):
#      return self._height

# # Setter methods
# def set_width(self, width):
#      self._width = width

# def set_height(self, height):
#      self._height = height

# # Method to calculate area
# def calculate_area(self):
#      return self._width * self._height

# # Create a rectangle with width 5 and height 3
# rectangle = Rectangle(5, 3)

class Rectangle:
    def __init__(self,width,height) -> None:
        self._width = width
        self._height = height
     
     #getter me = Reading = Window
    def get_width(self):
        return self._width # could make this print rather than return but limits the function to print and cant do further actions on it SEE BELOW
    
    def get_height(self):
        return self._height
     
r = Rectangle(20,30)

print("Width is "+str(r.get_width()))
print("Height is "+str(r.get_height()))

class Rectangle:
    def __init__(self,width,height) -> None:
        self._width = width
        self._height = height
     
     #getter me = Reading = Window
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def set_width(self, new_width):
        self._width = new_width
     
r = Rectangle(20,30)

print("Width is "+str(r.get_width() +5 / 2))# cant add the + 5 / 2 on the width if have print rather thab return on the above def section
r.set_width(50)
print("Width is "+str(r.get_width()))#needed to ammend all this line had an issue not spotting the get_height which needed to be get_width stopped the update happening.


#Ammended 3
class Rectangle:
    def __init__(self,width,height) -> None:
        self._width = width
        self._height = height # without this first section of code is not object oriented programming
     
     #getter me = Reading = Window
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height
    
    def calculate_area(self):  # To work This had to be placed before the definition with the if else clause below to
        return self._width * self._height
    
    def set_width(self, new_width):
        if new_width > 0:
            self.width = new_width
        else:
            print("Invalid") 
     
r = Rectangle(20,30)

print("Width is "+str(r.get_width()))
r.set_width(50)
print("Width is "+str(r.get_width()))#needed to ammend all this line had an issue not spotting the get_height which needed to be get_width stopped the update happening.
print(r.calculate_area ()) # Figured this one on my own the r being rectangle and .calculate_area to method to calculate area.

# Can change with
#r.width = 1000 but allows anyone to change it
#Use the above formula to restrict who can ammend the object i.e. in the case of a bank account
# if user is manager:
#     r.set_width(50)
#else:
#     print("invalid access")



#Ammended 4
class Rectangle:
    def __init__(self,width,height) -> None:
        self._width = width
        self._height = height # without this first section of code is not object oriented programming
     
     #getter me = Reading = Window
    def get_width(self):
        width = self._width # Here the return self._width was changed to width = self._width that is now a new variable
        return width # need to add return width for ut to function
    
    def get_height(self):
        return self._height
    
    def calculate_area(self):  # To work This had to be placed before the definition with the if else clause below to
        return self._width * self._height
    
    def set_width(self, new_width):
        if new_width > 0:
            self.width = new_width
        else:
            print("Invalid") 
     
r = Rectangle(20,30)

print("Width is "+str(r.get_width()))
r.set_width(50)
print("Width is "+str(r.get_width()))#needed to ammend all this line had an issue not spotting the get_height which needed to be get_width stopped the update happening.
print(r.calculate_area ()) # Figured this one on my own the r being rectangle and .calculate_area to method to calculate area.

#INHERITANCE
class Parent:# The parent class is the base / super class
    def __init__(self,name, relatiion) -> None:
        self.name = name
        self.relation = relatiion 

    def property1():
        pass
    
    def method_property2():
        pass
    
    def love_food():
        pass
# Can have multiple inheritance i.e. off two parent classes but not recommended normally just keep one super class as makes the proggram too complex.
#A Child Class This would be the derived / sub class inheriting properties from the parent class
class Child(Parent):   # It is as simple as adding the super class after the colons inside brackets () to add a super class to inherit from.
    def __init__(self) -> None: 
        pass
    
    def child_property1():
        pass
    
   # def love_food():         # we dont need to retype this here we can inherit it from the parent (base / super class)
    #    passs
        
class Relatives(Parent):
     def __init__(self, name, relatiion) -> None:
         super().__init__(name, relatiion)  # after doing the def __init hit enter and pulls these line from the base / super class

#Ammendment for multiple inheritance
class Parent1:# The parent class is the base / super class
    def __init__(self,name, relatiion) -> None:
        self.name = name
        self.relation = relatiion 

    def property1():
        pass
    
    def method_property2():
        pass
    
    def love_food():
        pass
# Can have multiple inheritance i.e. off two parent classes but not recommended normally just keep one super class as makes the proggram too complex.
# Better to have one parent class with multiple sub classes.
#A Child Class This would be the derived / sub class inheriting properties from the parent class
class Parent2(Parent):   # It is as simple as adding the super class after the colons inside brackets () to add a super class to inherit from.
    def __init__(self) -> None: 
        pass
    
    def child_property1():
        pass
    
class Child(Parent1, Parent2):# Can have multiple Super Class - 
     def __init__(self, name, relatiion) -> None:
         super().__init__(name, relatiion)  # after doing the def __init hit enter and pulls these line from the base / super class

# now can have multiple level inheritance

class Mother:   # It is as simple as adding the super class after the colons inside brackets () to add a super class to inherit from.
    def __init__(self) -> None: 
        pass
    
    def child_property1():
        pass
    
class Kids(Mother):# Can have multiple Super Class - 
     def __init__(self, name, relatiion) -> None:
         super().__init__(name, relatiion)  

class School(Kids):# Can have multiple Super Class -  School inherits from Kids class - Kids class inherits from mother class - 2 levels multi level
     def __init__(self, name, relatiion) -> None:
         super().__init__(name, relatiion)  

schoolObject. # Could not get this to work- should up the mthods options for the above classes with the .



class Musicalinstruments:
    def __init__(self,name) -> None:
        self.name = name
    
    def play(self):
        print(self.name + " is playing")   # Changed from return to print for an output to the screen
#End
#Sub Class / Derived Class
class Guitar(Musicalinstruments):
    def __init__(self, name) -> None:
        super().__init__(name) # super means call from the above paent class for return self.name + "is playing"
        super().play()

#Creating an object
ge = Guitar("Gipsum")# Here prints Gipsum is playing where print was inserted in the musicalinstruments class
gr = Guitar ("abc") #Here prints Gipsum is playing where print was inserted in the musicalinstruments class


# Musical code Inheritance SAMPLE 2
class Musicalinstruments:
    def __init__(self,name) -> None:
        self.name = name
    
    def play(self):
        return self.name + " is playing"   # Changed from return to print for an output to the screen
#End
#Sub Class / Derived Class
class Guitar(Musicalinstruments):
    def __init__(self, name, size) -> None: # size property added here
        self.size = size # This is now not a common property just a property of the guitar
        super().__init__(name) # super means call from the above paent class for return self.name + "is playing"
        super().play()

class Wilson(Musicalinstruments):
    def __init__(self, name) -> None:
        super().__init__(name)
        super().play()

#Creating an object
ge = Guitar("Gipsum")
gr = Guitar ("abc")



