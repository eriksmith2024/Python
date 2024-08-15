
#Write a program that asks for a data collection type from a user and creates a data collection with 3 data items and print it.
# Nested dictionary
thisdict = {
    "player 1": {
        "name": "Erik Smith",  #When doing the nested dictionary I had a comma in between the { that was causing a problem.
        "designation": "Worldclass",
        "year": 2024,               #interger
        "profession": "footballer",
        "position": "central midefielder",
        "speciality": "skills & goals", #Problem I had with colon in next line related to no comma at the end of this line
        "LFC player": "True",                      # boolean
        "Team colors":["red",  "white", "green"]   # (List)
    },
    "player 2": {
        "name": "Dave Miney",
        "designation": "Bang average",
        "year": 2024,               #interger
        "profession": "footballer",
        "position": "central defender",
        "speciality": "game reading", #Problem I had with colon in next line related to no comma at the end of this line
        "LFC player": "True",                      # boolean
        "Team colors":["red",  "white", "green"]   # (List)
    },
    "player 3": {
        "name": "Paul Miney",
        "designation": "Bang average",
        "year": 2024,               #interger
        "profession": "footballer",
        "position": "central defender",
        "speciality": "game reading", #Problem I had with colon in next line related to no comma at the end of this line
        "LFC player": "True",                      # boolean
        "Team colors":["red",  "white", "green"],   # (List)
    }
}
#print(thisdict) # to print everything for the full 3 dictionaries
print (thisdict["player 3"]) #  to print all the details for just player 3
for player in thisdict:
    print(f"{thisdict[player] ["name"]}'s designation is {thisdict[player]["designation"]}") # to print just the designation stauts world class / bang average for the 3 players.
for player in thisdict: 
    print(f"{thisdict[player] ["name"]}'s designation is {thisdict[player]["designation"]} {thisdict[player]["position"]}") #This combined designation and position.

#My go at task struggling to convert the user input to a list

# groceryList = input("tell me what 3 items you need from waitrose?")
# print (groceryList)
# userGroceryList = list(groceryList)
# userGroceryList.pop(1)
# print (groceryList)

#CHAT GPT correction
# Prompt user for input
groceryList = input("Tell me what items you need from Waitrose, separated by commas: ")

# Split the input string into a list of items
userGroceryList = groceryList.split(',')

# Remove any leading/trailing whitespace from each item
userGroceryList = [item.strip() for item in userGroceryList]

# Ensure there are exactly three items
if len(userGroceryList) == 3:
    # Remove the second item (index 1)
    userGroceryList.pop(1)
else:
    print("Please enter exactly 3 items separated by commas.")

# Print the modified list
print(userGroceryList)
