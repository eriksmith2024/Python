# print("Hello, world!")

# # Request user input and convert it to an integer
# number = int(input("Enter a number: "))

# # Divide the number by 2 and check if it is even or odd
# if number % 2 == 0:
#     print("You chose an EVEN number")
# else:
#     print("You chose an ODD number")


# salary = int(input("Enter your annual salary?")) 
# service = int(input("Enter your years of service?"))
        
# if service > 3:
#     bonus = int(salary * 0.07)
#     print("You will receive a bonus of", bonus)
# else:
#     print("You are not entitled to a bonus")



tuple1 = ("apple", "banana", "cherry")

print(tuple1)

# Convert tuple to list
list1 = list(tuple1)

# Append an item to the list
list1.append("mango")

# Convert the list back to tuple
tuple1 = tuple(list1)

print(tuple1)
