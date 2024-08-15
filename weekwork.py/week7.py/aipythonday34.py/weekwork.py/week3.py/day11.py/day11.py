# DATABASES

# when using length it will have polymorphism for example
# name = "Erik Smith" 
# number = "5, 6, 7, 8, 9, " 

# x = len(name)#length = 10
# y = len (number)#length = 15

# print (x)
# print (y)


# Moved on to data bases with mostly conceptual work today.

#Not much need to use VS Code today.

x = int(input("Enter a number: "))

output = 1

while x > 0:
    output = output * x
    x = x -1

print(output)