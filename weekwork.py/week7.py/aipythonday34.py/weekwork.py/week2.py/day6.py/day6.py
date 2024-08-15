# Class Monday 10th June 2024
# Interview Questions - Recap
# what is SDLC stand for? It stands for software development lifecycle
# what is the difference between compiler and interpreter? Compiler all at once & interpreter one line at a time
# What type of compiler does Python use ? it doesn't use a compiler it uses an interpreter. 
# What is the difference between dynamic  & statically typed languages?
# Dynamic typed checked at run time & can change the variables dynamically)  Python is dynamically typed. statically typed(checked at compile time of code variables must be declared with a type). 
# Can get questions around TUPLES SETS LISTS i.e. name some keywords remove, pop, append, push 
# #camelcase myNameIs
# import math as m - imports maths module and changes its name to m

#DAY 6 Session - HAVE LEARNT DATA TPYPES & CONDITIONAL STATEMENTS - NOW NEED TO LEARN LOOPS CONSTRUCT

# fruit = ["banana", "mango", "apple", "banana", "mango", "apple", "banana", "mango", "apple", "banana", "mango", "apple" ] 
# print (fruit[0])
# print (fruit[5])
# print (fruit[7])
# print (fruit[1])
# print (fruit[2])
# print (fruit[1])
# print (fruit[3])
# print (fruit[4])
# print (fruit[2]) # to print like this each one at a time is painful especially with lists with 1000s of items - instead use loops.

# # #First type of loop is FOR LOOP 
# fruit = ["banana", "mango", "apple", "banana", "mango", "apple"] 
# for f in fruit: # f means  go through the fruit list unless it finishes
#     print (f) #This now prints the items line after line going through the items one at a time rather than print (fruit[3])

# coffee_order = ["americano", "cortado', 'espresso", "capucino"]
# for c in coffee_order: # structure is for letter in whatever the list name is
#     print (c)

# #Second type of loop is WHILE LOOP 

# Original for loop to print each item in the list
# fruit = ["banana", "mango", "apple", "banana", "mango", "apple"] 
# for f in fruit:  # Iterate through the fruit list
#     print(f)  # Print each item line by line

# Corrected version needs a while loop instead of for to avoid the infinity loop.
fruit = ["banana", "mango", "apple", "banana", "mango", "apple"] #THIS IS LIST WHICH IS WHY IT RUNS TGHROUGH THE LIST ITEMS
name = "skill city boot camp" # THIS IS STRING  WHICH IS WHY IT can loop through the STRING characters if this single item s,k,i,l,l, ETC going down the page.
for n in name:
    print(n)
index = 0  # Initialize a counter
while index < len(fruit):  # Loop until the counter reaches the length of the list
    print(fruit[index])  # Print the item at the current index
    index += 1  # Increment the counter to move to the next item

x = 1
while x < 10: # while x is less than 10
    print (x)
    x = x + 1 # without this line does an infinity loop - prints the value 1-9. Adds one until it gets greater than 10

x = 10
while x > 1: #While x = greater than 1
    print (x)
    x = x - 1 # without this line does an infinity loop - prints the value 10 down to 2.

x = 10
while x >= 1: #While x = greater than or equal to 1 to make it countdown to 1.
    print (x)
    x = x - 1 # without this line does an infinity loop - prints the value 10 down to 2.

# LOOPS CAN BE USED ON SETS LISTS AND TUPLES. 
# FOR LOOPS are used when we dont the length of the iterable statement
# WHY LOOPS are used when we know the length of the iterable statement
# Pass 
# Break - Break means take me out of the loop usef for WHILE Loop
# Continue - means continue with the loop used in WHILE Loop

x = 10
while x >= 1:
    print(x)
    x = x - 1
# At this stage the above loop will run to 10

x = 10
while x >= 1:
    print(x) # Now will count down from 10 to 5 because of the break below on the formula
    if x == 5: #inserted line to use BREAK if x equals five
        break # It means if x gets to equal five break the loop
    x=  x - 1


# WHILE loop infinite
# x = 10
# while x >= 1:
#     print(x) # Now will count down from 10 to 5 because of the break below on the formula
#     if x == 5: #inserted line to use BREAK if x equals five
#         continue # If change to continue will get a infinity loop printing 5 over and over
#     x=  x - 1

# When a infinite loop will have practical use in mobile phones menu
# TEACHER EXAMPLE OF WHERE IT WOULD HAVE PRACTICAL USE BUT DOES NOT FUNCTION TO LOOP BACK MY ATTEMPT FOLLOWS TO CORRECT
print("Enter 1 to go to main menu.")
print("Enter 2 to go to sub menu.")
print("Enter 3 to go to accounts.")
print("Enter 4 to go to exit.")
print("Enter 5 to go to continue")  # I managed to get this loop back for option 5 but only 1 time.

userInput = input ("Enter your choice")

while userInput == 5:
    continue
while userInput == 4:
    break

# MY VERSION OF TRYING TO MAKE THE PHONE LOOP WORK & REPEAT BACK 
# print("Enter 1 to go to main menu.")
# print("Enter 2 to go to sub menu.")
# print("Enter 3 to go to accounts.")
# print("Enter 4 to go to exit.")
# print("Enter 5 to go to continue")  # I managed to get this loop back for option 5 but only 1 time.
# userInput = input ("Enter your choice")
# while userInput == 5:
#     continue
# print("Enter 1 to go to main menu.")
# print("Enter 2 to go to sub menu.")
# print("Enter 3 to go to accounts.")
# print("Enter 4 to go to exit.")
# print("Enter 5 to go to continue")
# userInput = input ("Enter your choice")
# while userInput == 4:
#     break

# CORRECTED VERSION USING CHAT GPT THAT FUNCTIONS UTILISES IF STATEMENTS (TIP when printed was all indented. select all & then up / shift key plus tab takes it all one indent to the left)
while True:
    print("Enter 1 to go to main menu.")
    print("Enter 2 to go to sub menu.")
    print("Enter 3 to go to accounts.")
    print("Enter 4 to exit.")
    print("Enter 5 to continue")
    
    userInput = input("Enter your choice: ")

    if userInput == "1":
        print("You chose to go to the main menu.")
    elif userInput == "2":
        print("You chose to go to the sub menu.")
    elif userInput == "3":
        print("You chose to go to accounts.")
    elif userInput == "4":
        print("Exiting the program.")
        break
    elif userInput == "5":
        print("Continuing...")
    else:
        print("Invalid choice. Please try again.")

# if know the 3 following things if else loops and sequence can basically do anything. Most hangs on these.
# If-Else conditional statememts 
# Loops Iterable statements
# Sequence 
# Used for all program langauges and go to chat GPT tell me how to do if else for HTML etc

while True: # true is true so will print infinitely
    print("Welcome")
    break # without this break will print infinity loop. Break makes it print once

while False: # Will never run as loop only runs when condition is true
    print("Welcome")
    break # without this break will print infinity loop. Break makes it print once

#Factorial = find factorial of 5 = 5 * 4 * 3 * 2 * 1 = 120

# # write a program that takes an input and return the factorial of the input
# input ("enter a number")
# while not int:
#     input("Please enter a whole number")
#     break

#Utilising Chat GPT
# # write a program that takes an input and return the factorial of the input
import math #Main part I forgot to get maths functions for .factorial option

#Function to get valid integer
def get_valid_integer():# needed to use define function for this
    while True:
        try:# Never come across try function before - what I was looking for in using "when" which doesnt exist
            user_number = int(input("Enter a whole number to find its factorial."))
            return user_number
        except ValueError: # Except what I needed for when experiement with try and except
            print("Invalid input. Please enter a whole number.")

user_number = get_valid_integer()
factorial = math.factorial(user_number)
print(f"The factorial of the {user_number} is {factorial}")

#Kian solution also works for getting the factorial but not if they dont enter a integer number
number = int(input("Enter your number: "))
factorial = 1

for f in range(1, number+1):
    factorial *= f
    print(factorial)

# James exercise solution
x = int(input("Enter a number: "))

output = 1

while x > 0:
    output = output * x
    x = x - 1

print(output)

#teacher resolution - I could not get to work without going to chat gpt.
# result = 1
# num = input("please enter a number")

# if type(num) ==int:
     
#     while num > 0:
#      result = result * num

#     print(result)
# else:
#     print("Invalid number")

result = 1
num = input("Please enter a number: ")

# Try to convert the input to an integer and handle the case where conversion fails
try:
    num = int(num)
    
    # Ensure the input number is non-negative
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        while num > 0:
            result = result * num
            num = num - 1
        print(result)
        
except ValueError:
    print("Invalid number")

#Functions
print("Good morning " + "Lorem lupsum")

name = "Nick"
print("Good Morning"+ name)

name = "Nick"
print("Good Morning"+ name)

name = "Nick"
print("Good Morning"+ name)

# Where we have functions are used to save a block of code we can reuse
# define a function use: 
#def functioname ():
    #function definition /function statement

def greet (name, day): #Add parameters to the function name first parameter and then day for the second
    print("Good morning" + name + "This is " + day)

# call a function - just write the name of the function greet()
greet("Muhammed", "Monday") # will then print good mormning Muhammed Good morrning Nick Goor morning James.
greet("Nick", "Friday")
greet("James", "a lovely day")

# Built in function - print is built in
# User defined function - Greet was one we defined above


def greet (): #function without paramneters when you remiove day and name
    print("Good morning" + name + "This is " + day)

def greet (name, day): # a user defined function with parameters name and day
    print("Good morning" + name + "This is " + day)

def factorial(num): # Define the function once here for factorial that you can then defer back to in lines 282-284 factorial
    result = 1
    while num > 0:
        result = result * num
        num = num -1
    print (result)

factorial(5) # find me the factorial of 5 (120)
factorial(100) # find me the factorial of 100 (933262.. & continues)
factorial (7) # find me the factorial of 7 (5040)

#CREATE A FUNCTION THAT TAKES TWO PARAMETERS FOR NAME & AGE & OUTPUTS A BIRTHDAY MESSAGE HAPPY BIRTHDAY 'NAME' I HEAR YOU ARE "AGE" TODAY
# def bday_message (username, age):
#     username = input (" please enter your name") 
#     age = input (" please enter your age")
#     print ("happy birthday" , username , "I hear you are" , age, "today")

# bday_message ("erik",  25 "danny" 27)

# Simple ATM code that teacher liked

cash_in = 100
pin = int(input("enter your pin"))
if pin != 1234:
    print("the pin is incorrect, try again")
else:
    amount = int(input("Enter the amount you wish to withdraw"))
    if amount <= cash_in:
        cash_in = cash_in - amount
        print("your cash is being wthdrawn")
    else: 
        print("It cannot proceed as the amount is high than the cash in")


# Library or module is ready developed code & functions in python that can be imported i.e. random or maths. Often been done by developers and shared with everyone else. 


   

  








   

