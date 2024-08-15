# author: Erik Smith - these comments dont print. If highlight active code & command k command c it will make it all hash and not readable like this
# Dynamically typed language vs statically typed language  
# we dont need to tell python what data will be saved in the memory. 
# Python decides it self what data will be saved in the memory why Dynamically typed language. Types are defined by Python
print("Hello world")
print("Hello world")
a = 5 #number Integer which is a whole number
b = 3.14159 # decimal number which is called float
c = -5.5 # negative #number
d = "Skills city" # a string which always comes inside  " " double qoute marks g that follows is a character which can have single qoute marks ''
e = True # Boolean
f = False # Boolean
g = 'a' # character which has single qoutemarks around it ' '
print(a) 
#End
x = 5 # x is a variable the number 5 is the data value
x = 10
print (x)
x = 5
x = 5 - 2
print (x)
x = 5
y = x + 8 # y is now 13
x = y - (x + 5)  # 13 take away (x which is 5 + 5)
print(x) # results in printing 13-10 which equals 3

print(var) # Cannot print var as not yet defined. Need to define what var is above it.  remove this line with error for code that follows to work. 
#ANY CODE AFTER A INCORRECT LINE WILL NOT WORK
var = 3.14159 # PI
print (var)
var = "Welcome to skills city" # Dynamically Typed Example # changed from number 3.14159 number to string possible because dynamically typed language - not possible in all languages
print (var) # All that follows wont run due to this line

namevariable = # create/define a variable if line 32 & this line 34 which are both incorrect are reomoved will print on terminal welcome to skill city. 
nameVariable = True # initialized the variable by = True # giving the value True 

#Variable cannot start with a number can be underscore then number _6 but not start with a number _name_my is also fine
#A variable name can only use alpha numeric chracteristics & underscores (A-z 0-9 and _)
# variable will start with letter or underscore
# we will normall use the variable convention in python of Camcel case using capitals for each word except for beggining word myFirstName
# camcel case i.e. myFisrtName
myFirstName = "Erik" # myFirstName is the variable Erik is the value.
# Variable names are case sensitive i.e. below are 3 different variables
myFirstName = "Erik"
myFIRSTName = "Erik"
myFiRSTName = "Erik"
#another example below with a = 5    &    A = 5 thar appear the same but are different variables due to the A capital and a lowercase.
a = 5
A = 5

x, y, z = "Orange", "Banana", "Cherry" # Assign multiple variables in one line by seperating xyz with a comma. x is assigned Orange y Banana z will be Cherry.
x, y, z = "Orange", "Banana", "5"  # Can have string & number together - can also change data type saved for variables - rarely done as not great for readability.
nyFirstName, myMiddleName, myLastName, myAnyOtherName = "Erik" # Rarely do this as makes difficult to read  as a programmer so put on single lines but can be done.
print (x)
print (y)
print (z)
# Arithematic Operators = Maths + - * /
x = 5
y = 2
print(x + y) = 7 # none of these will work as above Arithematic are numerous active code with variables names x y z
print(x - y) = 3  # to make code work for these four sums delete all code above Arithematic Operators
print(x * y) = 10 # to make code work for these four sums delete all = and sum calculation
print(x / y) = 2.5 
# Operator Precedence - the order in which you should do the some below i.e. do brackets first then multiplcation then division followed by + and -
print(x/y*(x-y)*y-(x/y)) = 12.5 # Operator Precedence parentheses will take highest precedence superceding maths operators & calculation for this should be done first
                                # 2nd Operator Precedence ** which means 2**2
                                # 3rd Operator Precedence multiplication * & divisoin /
                                # 4th Operator Precedence addition + and subtraction -

print(x + y - (x * y)/ x) = 5.0  # FOR THIS SUM
                                # X(5) * Y(2) = 10                           First Operator Precedence parentheses will take highest precedence superceding maths operators & calculation for this should be done first
                                # 10 / x(5) = 2                              Second Operator Precedence multiplication * & divisoin /
                                # x (5) + y(2) = 7 - 2(above line) = 5       Third Operator Precedence addition + and subtraction -

#Importance of data types for variables i.e. cannot multiply lorem but can print 7 times
x = "lorem"
y = 2
print(x + y) # does not make sense lorem + 2
print(x * y) # 2 times Lorem will print lorem twice i.e. lorem lorem

print(type(x)) # will return the variable type i.e. string integer etc of x

x = 1j # complex data type mix of both integer 1 & string j

 # casting a data type 
x = str('lorem') # do not need to here but specifying that lorem is string when casting it needs the constructor for example int then whatever it is in brackets
y = bool(True) # cast / specify boolean with bool
z = float(3) # 3 would be integer with no decimal but you can force it to float with decimal

x = "loram lipsum" # string
y = 5 #integer
print(x+y) #produces error message as can only concatinate string not integer cant add them together.

x = "loram lipsum" # string
y = str(5) #This forces the integer to string
print(x+y) # which results in this producing loram lipsum5

# EXERCISE create a variable, initialize with some numerical value and print if it is even or odd

X = 4
if X % 2 == 0:# The code if Y % 2 == 0: bascially the % is an operator that returns the remainder of y the variable divided by 2
    print("even number")
else:
    print('odd number')

Y = 5
if Y % 2 == 0: # The code if Y % 2 == 0: it checks if y is an even number. If y equals 0 it means is is divisible by 2 (no remainder) so y is an even number. if y is not equal to 0 then it is odd number
    print("even number")
else:
    print('odd number')


 