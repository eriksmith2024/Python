from room import Room

kitchen = Room("kitchen")
kitchen.set_description("Adank and dirty rooom buzzin with flies")
ballroom = Room ("ballroom")
ballroom.setdescription("A vast room with a shiny wooden floor")
dining_hall = Room("Dining room")
dining_hall.setdescription("A large room with ornate golden decorations")

print(kitchen.get_description())

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dining_hall.get_details()