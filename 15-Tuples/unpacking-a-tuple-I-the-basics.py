
employee = ("Bob", "Jhonson", "Manger" , 50)

# firs_name = employee[0]
# last_name = employee[1]
# position = employee[2]
# age = employee[3]

# print(firs_name, last_name, position, age)

# Different Syntax
first_name, last_name, position, age = employee
print(first_name, last_name, position, age)

# We can do that with a list
# nombre, apellido_1, apellido_2 = ['Josafat', 'Zamora', "Munoz"]
# print(nombre, apellido_1, apellido_2)

# # Potential Errors
# first_name, last_name, position = employee    # Not giving enough variables
# first_name, last_name, position, salary = employee    # Giving too much variables

# Swap Variables Like on C 
Cristiano = 7
Messi = 10
Cristiano, Messi = Messi, Cristiano

print(f"Messi ahora es el numero {Messi} y\n\
Cristiano ahora es el numero {Cristiano}")