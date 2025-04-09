students = ["Bob", "Sally", "Sue"]
athletes =  students
nerds = ["Bob", "Sally", "Sue"]

print(students == athletes)
print(students == nerds)

print(students is athletes)
print(students is nerds)

# Python treats immutable types differently 
print()

a = 1
b = 1 
print(a is b)

nombre = "Josafat"
name = "Josafat"

print(nombre is name)