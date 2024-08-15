#Erik Smith week 2 Day 10.

# name = "lorem lipsum"
# myList =[1,3,5,7,9]
# myDict ={
#     "name": "my name",
#     "designation": "Instructor"  #name list dictionary - threee kinds of variable
# }

# #Changed mylist see below
# name = "lorem lipsum"
# myList =["bannana", "orange", "apple"]
# myDict ={
#     "name": "my name",
#     "designation": "Instructor"  #name list dictionary - threee kinds of variable
# }
# len(name) # 12returns the length of the given argument
# len(myList) # now 3 as list changed from
# len(myDict) # 2 two key values name & designation

# Polymorphism ability of any function to change i.e. within class of Car Plane & Boat all have method "to move" but this changes to fly sail drive allows to be done with less code.
#Car Class
class Transport:
    def __init__(self, name, brand) -> None:
        pass
    def move (self, behaviour):
        print(behaviour)

class Car(Transport):  # car is an object within class
    def __init__(self, name, brand) -> None:
        self.name = name     # properties
        self.brand = brand   # properties

    def move(self):# initially did not work producing an erro because self was not included here
        print("Drive")  # method
#Plane class
class Plane (Transport):
    def __init__(self, name, brand) -> None:
        self.name = name   # There was also a comma here rather than a .
        self.brand = brand

    def move(self):
        print("Fly)")

# Boat class
class Boat:
    def __init__(self, name, brand) -> None:
        self.name = name
        self.brand = brand

    def move(self):
        print("Sail")

#Run
car1 = Car("320D", "BMW")
plane1 = Plane("Boeing", "787 Dreamliner")
boat1 = Boat("Titanic", "XYZ")

for x in (car1, plane1, boat1):
    x.move()


#Useful note select all command shift moves to the right tab on its own moves to the right

# OOP        =  James
# Classes    = Efosa
# objects   =  Efosa
# data members (properties + methods ) = Aidan
# inheritance  = Salamatu
# polymorphisim  = Erik
# encapsulation   = Neil

#Need to go to google colab and download Teabag exercise to complete and submit.