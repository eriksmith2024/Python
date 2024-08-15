# author Erik Smith 06.06.24 
# Action go to W3 schools & work through Python tab & exercises
# Yesterdays exercise:
# x = 7
# print (x % 2) # 7 divided by two leaves 1 which gets printed & means odd number
# print (x % 1) # 7 divided by 1 = 0 meaning an even number as their is no remainder it divides by 1 once. 

# Python comments use the # which then makes a comment 
"""Python apparently does not do multi line comments wwith text over multiple lines 
but can be worked around by utilising 3 x spechmarks staring on first line 
and closing on last line."""
# SHORTCUT TO UNCOMMENT use COMMAND + K + U 
# Lorem Ipsum - dummy text with no meaning

# Python Keywords
# and as break class continue def del for can see  # Use chat GPT ask for list of Python keywords & definitions

# Python Commands

# Python Input
#Variables
#name = "Erik" # This is saving a variabkle by name /  Where I had this live it messed the rest of the live text for the Ben and Ignacio option showing as Invalid
# Dynamically asking for name 
# input built in functiom for requesting user input.
name = input('please enter your name')
print(' You have entered your name ')
print(name)

# Conditional statements: These statements are used to compare and check values of certain logic  using comparison operators 
#'if' statementscheck i.e. check if name is equals to Muhamed then print otherwise dont print 
    #if condition:
    #statement

number = input('please enter a number. ')
print('You have entered the number', number)
print('You have entered your name', name, 'and your chosen number', number) # Concatenation "text" , space varaiblename combines these things items together  
if name == "Erik":                         # if any of condition matches will only execute the first condition it matches.
    print("Welcome ", name)                # Always indented on second line -  use lines that generate showing where they aliigb with the code block.
elif name == "Ben":                        # elif basically as if statements can have as many as you like going on and on
    print("Warm Welcome", name)
elif name == "Ignacio":                    # On the elif remember it does not need the brackets () BUT does need the : on the end before the next line that lists the action
    print(" Bienvenido ", name)            # space at begginning between " Bienvenido " leaves space when printed on the terminal. 
elif name == "Juan":                       # if the user hits space then enters the name it is a different variable with space before the name and the computer does not recognse it printing invalid instead of greeting.
    print(" Great to see you", name)       # Can do a greeting in another language i.e. Bienvenido Python just prints that.
else:
    print("Invalid")

               
# 5 + 5 = 10 sum
# 5 + 5 = 55 concatenation

# Python Conditional statments - Comparison operators needs two values to operate
#   ==    Equals a == b 
#   !=    Not Equals a != b
#   <     Less than a < b
#   <=    Less than or equal to a <= b
#   >     Greater than a > b
#   >=    Greater than or equal to a >= b

# Arithmetic Operators can operate with one value i.e. - 5
#   + addition
#   - subtraction
#   * multiplicatopn
#   / division
#   % remainder / modular   5 % 2 = 1  when divide five by two has a remainder of one

num1 = 5
num2 = 7

if num1 > num2:
    print("Number1 is greater than number 2")
elif num1 < num2:
    print()
elif num1 <= num2:
    print()
elif num1 >= num2:
    print()
elif num1 != num2:     #From here
    print("message1")
    print("message2")
    print("message3")  #to here all same clock under that elif printing those staments if that elif is true 
else:
    print("Number is invalid")


# Nested conditional statements - nested 

if num1 > num2:                                     # block is from here line 88 
    print("number 1 is greater than number 2")
    if num1 >= num2:                                #This if is inside the previous if - #nested if where you pass the first if but then a second if needs to be met for the action / out of printing to happen
        print(" Number is also equals to")    
        if num1 == num2:
            print("number is lorem message")        # to here line 93 which is last in nested block


if num1 > num2:                                     # This block is line 96 to line 101 
    print("number 1 is greater than number 2")
if num1 >= num2:                                    # This if is now not inside the previos if statement so only the one if statement has to be met ti print.
    print(" Number is also equals to")    
    if num1 == num2:                                # This if part of the upper if on line 98. Will not get to this if unless the first if is met
        print("number is lorem message")



if num1 > num2:                                     # This block is line 105 to line 106 only two line block seperated from the others whereas above part of the same block.



if num1 >= num2:                                    # This if is now a seperate block.
    print(" Number is also equals to") 

if num1 == num2:                                     # This is still part of the other upper block.
    print("number is lorem message")

# username = input("Please enter your username")
# password = input(" Please enter your password")

# if username  == "admin":
#     print("your username is correct")
#     if password =="password":
#         print("yourpassword is correct")
# else:
#     print("invalid credentials")

# # EXERCISE: Optimise the username code above - take code and input to AI to optimise

# name = input("Please enter your username: ")
# password = input("Please enter your password: ")

# if name == "admin" and password == "password":
#     print("welcome, ' , name")
#     print("Your credentials are correct!")
# else:
#     print("Your credentials are incorrect")
#     print("Please try again")

# #optimised version
# name = input("Please enter your username: ")

# if name == "admin":
#     print("Your username is correct")
#     password =input("Please enter your password")
#     if password =="password":
#         print("your password is correct")
# else:
#     print("Invalid Credentials")
 
#James version of.
if (input("Please enter your username: ") == "admin") and (input("Please enter your password: ") == "password)"):
    print("Correct Credentials")
else:
    print("Invalid credentials")
name = input("Please enter your username: ")

if name == "admin":
    print("Your username is correct")
    password =input("Please enter your password")
    if password =="password":
        print("your password is correct")
else:
    print("Invalid Credentials")

# LOGICAL OPERATORS
# and  - All conditions should be true to proceed
# or   - Only one condition needs to be true to proceed
# not  - Reverse of the and result.

# username = input("Please enter your username")
# password = input(" Please enter your password")
# if username  == "admin":                         # Using the and here to add the if password statement on same line see edit below END
#     print("your username is correct")
#     if password =="password":                    # With the above and statement added means can delete this line and one below see amded code after end.
#         print("yourpassword is correct")
# else:
#     print("invalid credentials")
# END -  BELOW IS THE ABOVE CODE UTILISING LOGICAL OPERATOR AND

username = input("Please enter your username")
password = input(" Please enter your password")

if username  == "admin" and password == "password":
    print("welcome")
else:
    print("invalid credentials")

# NOW USING LOGICAL OPERATOR OR STATEMENT AMMENDED BELOW # It means if either password or the username are correct will show welcome one can now be wrong.
username = input("Please enter your username")
password = input(" Please enter your password")

if username  == "admin" or password == "password":          #This line had and substituted with or statement
    print("welcome")
else:
    print("invalid credentials")

#AMMENDED OR & AND STATEMENTS BELOW TO INCLUDE BOTH
username = input("Please enter your username")
password = input(" Please enter your password")
userID = input("Please enter your user ID")         # added this additional variable to use with additional or statement condition

if username  == "erik" or password == "got it" or userID == "Me": #This line had and substituted with or statement added a second or statement which worked
    print("welcome")  # but could not get a 4th and or stament in the line above for date of birth variable to work
else:
    print("invalid credentials") # only prints if all the above variabkes are entered wrong


#AMMENDED OR & AND STATEMENTS BELOW TO NOT STATEMENT - now needs to have details entered that are not erik got it or me in order to print welcome.
username = input("Please enter your username")
password = input(" Please enter your password")
userID = input("Please enter your user ID")         # added this additional variable to use with additional or statement condition

if not username  == "erik" or password == "got it" or userID == "Me": #This line had and substituted with or statement added a second or statement which worked
    print("welcome")  # but could not get a 4th and or stament in the line above for date of birth variable to work
else:
    print("invalid credentials") # only prints if all the above variabkes are entered wrong
# In the if not username == can use and >greater than < less than >= greater than or equal to for a number of different if not statements
# Pass Statement
if username == "lorem":
    pass # to pass on this to next code -  used whilst we may be waiting on a adiition to add to the code- stops the rest of the code then being incorrect to work on the rest
else:
    print("you are in else statement")

#Ask user for salary & years of service

salary =  int (input("please enter your salary details."))
lengthOfService = int (input("Please enter your years of service"))
#Calculate the bonus if years of service is more than 3 years
if lengthOfService > 3:
    bonus = 0.7 * salary
    print ("You will receive a bonus of", bonus, "for your", lengthOfService, "years of service" )
else:
    print ("You are not eligible for a bonus")
