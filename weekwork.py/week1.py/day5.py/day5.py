# Author Erik Smith 7th June 2024 (Day 5)

#CRUD Operations CREATE READ UPDATE DELETE 
# Lists are created with [ ] brackets Tuples are created with ( ) brackets
#Lists ordred & changeable allows duplicates
fruit1 = "Apple"
fruit2 = "bannana"
fruit3 = "cherry"   #This method would be ridiculous having hundreds of lines for hundreds of fruit so use a list. 

fruit = ["apple", "bannana", "cherry"] # In a list items are ordered, changeable allow duplicates i.e. "cherry" "cherry" & are indexed starting from 0.
print (fruit)
number = [3, 5, 9, 2, 7, 1] #Integer(int) list full numvers
digital = [True, False, True, True] #Boolean List
salaries = [500.50, 5345.33] # Float list - flost meaning number to decimal

print (digital) #    This reference to the defined variable list will now print the contents of the digital list on screen
print (number)  #   To print to screen remember needs ()
print (salaries)
number.sort ()
print (number)
number.reverse ()
print (number)

fruit = ["Mango, Pineapple", "Cherry"] # This changes the list fruit to the new list in these brackets superceding the previous details of the fruit list
print (fruit) # I made a mistake including print = (fruit) did not show as wrong but then wont print. Now this prints the fuit list as reffered to in the above line 19.

fruit = ["Apple", "Banana", "Cherry", " Apple", "Apple"] # Once again now changes the list fruit to this. Also you can have duplicates in the list. 
print (fruit) # The 2nd apple in the list has a space between speechmarks and apple which means it prints with a space before it. 

fruit = ["Apple", "Banana", "Cherry", " Apple", "Apple", "Mango"] # Once again now changes the list fruit to this. Also you can have duplicates in the list. 
print (fruit) # The 2nd apple in the list has a space between speechmarks and apple which means it prints with a space before it. 
fruit.sort()
print(fruit)
fruit.reverse () # sorts the list in the reverse order i.e. z to a
print (fruit)
#Indexed - Each variable in the list is indexed with a number starting from 0 i.e. print (fruit[1]) prints banana or print (fruit[3]) prints Apple  print (fruit[0]) is also apple. 
print (fruit[1])
print (fruit[3])
print (fruit[0])

#There are many ways methods/ functions to add to the list. Can start by pressing list name and then. after the list
fruit.extend("Cocunut") # If you do list.addeded method / function such as extend then have empty brackets () if you hover over the function it will tell you what it will do
print (fruit) # The extend function adds cocunut in but with each letter as a seperate variable in the list.
fruit.sort ()
fruit.append("Orange") # This will then add orange at the end of the list
print (fruit) # To see the new list need to print again.
fruit.remove('t')
fruit.remove("c")
fruit.remove('u') #Careful when there are multiple items in the list with the same value i.e. the u it removes only the first one.
fruit.remove("C")
fruit.remove("u")
fruit.remove('n')
fruit.insert(2, "mango") #insert function needs the index number for the list then new item as to what point you want to insert the new item
print (fruit)
fruit.sort() # Sorts the fruit alphabetically
print(fruit) # Need to print to see the result of the sort.
fruit = ["apple", "bannana", "cherry"] # changed the list here to the original list
print( "initial list ", fruit) # Typing the text into print will not print the initial list just a way to track it
fruit = ["Mango", "Pineapple", "Cherry"]# Changed the list again here
print ("changed list ", fruit) # This just prints the now ammended list with the text changed list
print("initial list ", fruit) # For example here it will print the text initial list with the the same ammended list- it does not recall the orginal list
fruit.remove('Pineapple') # removes one item that you must specify.
print (fruit)
fruit.pop() # removes an item from the end of the list
print (fruit)
#MERGE LISTS BELOW - second list goes on the end 
fruit = ["Apple", "Banana", "Cherry"]
fruit1 = ["Lorem", "Lipsum", "Dummy"]
fruit.extend (fruit1) # Adds fruit 1 Lorem etc to fruit. At this stage fruit 1 is the same 
print (fruit1) # This remains the same as it was the list fruit that was extended with fruit 1. Nothing was done to fruit1
print (fruit)
fruit1.extend (fruit) # fruit1 was now extended with fruit which already has been exednded with fruit 1 lorem lipsum etc. 
print (fruit1) #Now will print appended fruit 1 with the latest fruit list that already includes lorem etc
fruit1.pop(1) # Removes the indexed item from the list 1 being the second item so lipsum will go.
print (fruit1)
print(len(fruit)) # returns the lenth of the list in terms of number of items
del fruit1 # This deletes the list


# TUPLE collection is ordered unchangeable and allows duplicate.
fruitTuple = ("Apple", "Banana", "Cherry") # Limited actions as a TUPLE is a list that cannot be changed.
dobTuple = ("1985-05-05", "1995-05-02", "1990-05-05") # Tuple best used with items like date of birth where you dont want it to be changed.
dob = ("1983-05-05",) # stores one item as a tuple but needs , after speechmarks for one item. Can be forcefully changed ONLY with type casting i.e. stating int to act as float
print (dob) #TUPLE PRINTS WITH (,)
dob2 = ("1983-05-05") # This is just string not a string Tuple which cannot be changed. 
print (dob2) # Normal string prints as just the date text not surrounded by brackets.
newList = list(dobTuple) # CASTING changing TUPLE to list
dobTuple = tuple(newList) # CASTING changing the list back to TUPLE
fruit = ["apple", "bannana", "cherry"] #  This is a STRING LIST. To create a list need to create the list variable name then = and open with square brackets []

x =("apple", "apple", "apple", "banana", "banana", "cherry")
print(x)
print (x.count("apple")) # prints the count of apple in the tuple which is three occasions
y =list(x) # Effectively changes the Tuple x into list y that can be ammended.
y[1] ="kiwi" # On list y substitutes [1] on the list which is apple to kiwi
x = tuple(y) # now type casts making tuple x the details of list y with the ammendment of apple for kiwi.
print (x) # prints ammended tuple 
print (x.count("apple")) #prints the ammended count of apple in the Tuple which is now 2 following the tuple to list and change of an apple for a kiwi.
print (x.index("cherry")) # gives the index of an item. Careful as just gives the first index reference of an item but where there are two occasions say of banana only shos the first index and not the second.

#SETS - No duplicates Unordered, unchangeable and unindexed - used for random operations in Casinos uses {} brackets for a set collection
mySet = {1,4,5,6,6,6,7,9} # Can delete and insert new values but cannot change an existing set value. 
print (mySet) # Does not allow duplicate values only prints 1, 4, 5, 6, does not detail teh three sixes.
thisset = {"apple", "banana", "cherry", True, 1, 2} # Does not print the 1 as True = 1 and False = 0 in programming - as wrote true means 2. Wont print 1 as true represents 1 already.
print (thisset)# The order will be  be changed each time. 
thisset.add("orange") # adds orange to the set
print (thisset)
thisset.remove ("banana") # removes banana / DISCARD can also be used to remove a specific item
print(thisset)

#DICTIONARIES - operates on values pairs i.e. name = Erik Smith profession = M&A etc does not alloa duplicates but can be changes and is ordered
#key : value pair
thisdict ={
    "name": "Erik Smith", # key is name : value is Erik Smith
    "designation": "Worldclass", # key is designation value is worldclass
    "year": 2024}
print(thisdict) # prints the key and value for all the this dict on one line
print(thisdict ["name"]) #This will just print the key for name and value of Erik Smith.

thisdict ={
    "name": "Erik Smith",
    "designation": "Worldclass",
    "year": 2024,               #interger
    "profession": "footballer",
    "position": "central midefielder",
    "speciality": "skills & goals", #Problem I had with colon in next line related to no comma at the end of this line
    "LFC player": "True",                      # boolean
    "Team colors":["red",  "white", "green"],   # (List)
    }
print(thisdict)
thisdict["name"] = "Erik James Smith"
print (thisdict)
thisdict["Salary"] = "£200k per week" # this is adding not append for dictionaries
print (thisdict)
thisdict.pop("year") # if use pop with no listem item will delete all the values and keys in the dictionary which are seen as one item. 
print(thisdict)


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