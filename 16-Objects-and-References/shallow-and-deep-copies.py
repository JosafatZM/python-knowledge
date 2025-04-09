# shallow copy 
# Creates a new list and inserts references into it 
# for the objects found in the original list
import copy

# a = [1, 2, 3]
# b = a[:]

# c = a.copy()
# # False because the computer is storing
# # the a and c objects in different locations

# print(a is c)

# d = copy.copy(a)
# print(a is d)

# Deep copy
# You need it when you have an object like a list
# storing complex nested objects like other list 

numbers = [2, 3, 4]
a = [1, numbers, 5]

c = copy.copy(a)
b = copy.deepcopy(a)

print()
print(a[1] is b[1]) # DEEP COPY
print(a[1] is c[1]) # SHALLOW COPY

a[1].append(100) # MUTATE THE ORIGINAL LIST 
print(a) # ORIGINAL
print(c) # SHALLOW COPY
print(b) # DEEP COPY


print()
print("---- Ejercicio de la tarea ----")
web_dev = ["HTML", "CSS", "JavaScript"]

frontend = web_dev



web_dev.append("React")

print(frontend)