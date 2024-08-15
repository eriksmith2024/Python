#Day 7 Tuesday 11th June 
#RECAP
# a = "abc" is the same as a = 'abc' double single qoutes the same only matters when need an apostrophe in text included i.e. it's
# Why we need multiple loops. 
# Iterations are doing something repeatedly FOR loops are ideal when the number of iterations are known.
# WHILE loops are more flexible for scenarios where the iteration depends on a condition that might change.
# FOR loop goes through a list of items one by one. WHILE loops keep doing something as long as a condition is true.
# Python string maniplulations are operations on string i.e. concatenation joining two or more strings together.
     # Other string manipulations include repitition, indexing & slicing finding & replacing etc lots more of them.     

#def functionName():# Function v procedure - 
# function always returns something while procedure oes nnot return anything Research further
# functionName()# wont detail outcome on terminal unless use print inbuilt function.
def functionName():# Function v procedure - function always returns something while procedure does nnot return anything Research further
    return 5 + 6

print(functionName())# print(functionName()) # add print and extra brackets for the are to be printed then returns 11 the outcome of the function definition.

def functionName():# Function v procedure - function always returns something while procedure does nnot return anything Research further
    if True:
        return True
    else:
        return False

print(functionName()) # This now oprints the value it is true as without any other conditional statement true is true

# TODAYS CONTENT - INNTRODUCING OBJECT ORIENTED PROGRAMMING (OOP)
# UNDERSTANDING CLASSES & OBJECTS
# CREATING CLASSES & INSTANTIATING OBJECTS
# DEFINING & USING VARIABLES & METHODS
# HANDS ON EXERCISE BUILD A LIBRARY

# In PYTHON everything is an object String & integer
name = "My Name" # This name is now an object
age = 15 # an object
def func(): # This is an object
    pass
#name.count this .count only available for objects such as name or age or colours below. The box symbol means it is a method on the object. list of options 
for n in name: # cannot loop through its items if not an object ( in is a function / method)
    print(n) # prints each of the letters on a line seperately going down
# What is an object - an object is a defined data type. Whatever data you define becomes an object.
colours = ["red", "green", "orange", "yellow "] # colours is an object - a list object
# a defined data type
# User defined functions
# User defined objects (data types + functions/ methods) are the classes
# + - = % * are operators not objects  / 'while' 'for' 'in' 'print' etc are keywords not objects - all used tio process something 
     # Objects when you add the . which gives a list of options i.e. name.append only available for objects ( The .list includes both properties and methods / functions)
     # Classes
     # Functions
     # Methods

myList = list() # this is an empty list add the . will bring up all the object function options
# Procedural programming - line by line sequence and Functional programming - creating and useing functions
# code line 1 # Like this line 4 will not execute before line 1 & runs in sequence
# code line 2
# code line 3
# code line 4 With object oriented programing this can execute before line 2

# Save information for students  3 differrnt data types
# first name will be string
# surname will be string
# date of birth string or integer
# student ID will be integer
# Enrolles (True / False) Boolean
# FOR 100S of students not productive to copy past repeating these variables over and over.
# Define the student type and common variables one time and just use them over and over
# student { # use the brackets { } for this with the data insides see below
# first name will be string
# surname will be string
# date of birth string or integer
# student ID will be integer
# Enrolles (True / False) Boolean
# FOR 100S of students not productive to copy past repeating these variables over and over.

# student { 
# firstName = string
# surName =  string
# dateOfBirth = integer
# studentID = integer
# Enrolled = Boolean
# }

# student1 = student
# student2 = student
# student3 = student

# a= int(4) # both different data types even though both using integer 4
# b =int(4)

# a = student (4) # same principles that both of these are different students different spaces in the memory
# b = student (4)

# Object Oriented Programing are based on four pillars of inheritance polymorphism, abstraction and encapsulation KEY INTERVIEW QUESTION ALONG WITH WHAT EACH OF THEM ARE
# Steps to solve problems in OOP - 
    # Data input: data read from somewhere like a file or data base
    # Processing:  Data is interpreted and possibly altered for display
    # Data output: Data is presented so that it can be read or interacted with either by a physical user or a system.

#class = car {
#     engine = string       # Properties
#     transmission
#     dateOfProduction
#     seats

#     drive                 #Methods are functions defined within a class.
#     Stop
#     reverse
# }
# Student Class
class Student:
    pass

class Teacher:
    pass

# an object of the class student
student1 = student()
student2 = student()
# an object of the class teacher
teacher1 = teacher()
teacher2 = teacher()

myList = list()
# A class is a combination of objects -  A object is a combination of methods/functions & Attribues
class Student: # In class we use title case where word has a capital at the front
    def greet ():  # this is just adding the Methods (actions) that can be carried out by the student
        print ("Welcome")
    def welcome ():# this is just adding the Methods (actions) that can be carried out by the student
        print("Welcome to the bootcamp")

# an object of class student
student1 = Student() # remember when referring to a class the class has a capital at the front of its name.
student1.welcome

student2 = Student()
student2.greet()

#greet() # cant just do greet as it is a method associated with the student. You could if you put it outside the class which would then be a function. 


# A class is a combination of objects -  A object is a combination of methods/functions & Attribues
class Student: # In class we use title case where word has a capital at the front
    #Constructor def __init__ (self, name etc )
    def __init__(self, firstName, lastName, enrolled):# Can remove the -> None studio code autmatically adds this
        self.firstname = firstName # Attributes which are part of the constructor where we save attributes of student object
        self.lastname = lastName
        self.enrolled = enrolled

    def greet (self):
        print ("Welcome "+self.firstname+" "+self.lastname)
    def welcome ():
        print("Welcome to the bootcamp")

# an object of class student
student1 = Student() # remember when referring to a class the class has a capital at the front of its name.
student1.welcome
#student1 = student("Nick", "James", True) 


#an object of class student
student1 =Student("Nick", "James", True) # Object with initial values
print(student1.firstname) # This will now show Nick
student1.welcome()
student1.greet()

student3 = Student
student4 = Student
student5 = Student # could have 1000s of students who can all then utilise all the Methods/actions defined in the student class

# same as doing below
# num = 3.14 #in normal programming but using the different attribute points of the class to supply multiple data.

# Purpose of the -> None that was deleted above on tghe __init__ constructor line to define the return type of the function
def functionName()-> str: # MAKES IT STRING
     return 2 + 4  # 6

def functionName()-> int: # Makes it Integer
     return 2 + 4  # 6

def functionName()-> bool: # Makes it boolean
     return 2 + 4  # 6

result = functionName() # now stores the result of the above coode depending on whether we made it string boolean integer etc



# On library system - 
    # members borrow and return books are methods
    # attributes are members and books
