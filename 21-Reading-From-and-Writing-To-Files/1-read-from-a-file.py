# you have to pass the path as the argument 
# if you want to do it with the code runner
# if you do it with the cmd you just write your
# code like the one above

# NOTE: I recoment you to run this kind of things always on terminal
# and also use either the whole path or just the name but always run 
# this thing with TERMINAL.

with open("cupcakes.txt", "r") as cupcake_file:
    print("The file has been opened!!")
    content = cupcake_file.read()
    print(content)

print("\nThe file has been closed!!")

print("\nNow is your turn to open it manually!!")

with open("first_file.txt", "r") as first_file:
    content = first_file.read()
    print(content)

file_name = input("\nInsert the name of the file that \
you want to open: ")

with open(file_name, "r") as file_object:
    print(file_object.read())

