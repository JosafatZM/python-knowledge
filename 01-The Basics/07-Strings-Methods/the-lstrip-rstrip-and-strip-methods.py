emty_space = "          content         "

print(emty_space.rstrip()) #Remove empty spacefrom the right side
print(len(emty_space.rstrip()))

print(emty_space.lstrip())
print(len(emty_space.lstrip()))#Remove empty spacefrom the left side

print(emty_space.strip()) #Clean up all the white spaces from both the beginning and the end
print(len(emty_space.strip()))

website = "www.josaescool.com"

print(website.lstrip("w"))
print(website.rstrip("com"))
print(website.strip("woj.")) 
# The point of strip is that it is focusing
# in the beginning and the end of the string