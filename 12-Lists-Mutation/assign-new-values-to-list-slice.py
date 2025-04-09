coworkers = ["Lili", "Angela", "Martin", "Juana", "Matias"]
coworkers2 = ["Lili", "Angela", "Martin", "Juana", "Matias"]

coworkers[3:] = ["Oscar", "Ryan"]
print(coworkers)

coworkers[3:] = ["Oscar"]
print(coworkers)

coworkers[3:] = ["Oscar", "Ryan", "Joaquin", "Karla", "Gerardo"]
print(coworkers)

print()
coworkers2[-4:] = ["Oscar", "Ryan", "Joaquin", "Karla", "Gerardo"]
print(coworkers2)
# A python le vale, el disminuye o aumenta los vectores sin problema no como C

print()
# Given the great_directors list below, overwrite the “Steven Spielberg” string with a string of “Michael Bay”.
great_directors = ["Martin Scorsese", "Steven Spielberg", "Francis Ford Coppola"]

great_directors[-2] = "Miclael Bay"
print(great_directors)

print()
# Given the transformers list below, overwrite “Bumblebee” with “Grimlock”.
transformers = ["Optimus Prime", "Megatron", "Bumblebee", "Starscream"]

transformers[-2] = "Grimlock"
print(transformers)

print()
# Given the camping_trip_supplies list below, overwrite "Socks" with "Food".
camping_trip_supplies = ["Socks", "Flashlight", "Tent", "Blanket"]

camping_trip_supplies[0] = "Food"
print(camping_trip_supplies)

print()
# Given the tech_companies list below, overwrite the Microsoft, Blueberry, and IBM strings 
# with the strings “Facebook” and “Apple”. Use list slicing syntax.
tech_companies = ["Google", "Microsoft", "Blackberry", "IBM", "Yahoo"]

tech_companies[1:4] = ["Facebook", "Apple"]
print(tech_companies)