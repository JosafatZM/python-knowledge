
birthday = ( 1, 3, 2002)

print(len(birthday))
# We can print index positions like...
print(birthday[2])
# Or negative index positions like...
print(birthday[-2])
# And so on and so on...

# But we can't add or change an index
# birthday[1] = 3 # We get a  TypeError

addresses = (
    ['Av. Santo Domingo', 'Centro', 'Tab'],
    ['Calle Pitahaya', 'Cardenas', 'Tab']
)

# We can change if the element is a mutable element just like a list
addresses[0][1] = 'Villahermosa'

print(addresses)

print(dir(addresses))

# To understand lets say that
# A "tuple" is immutable, but if the objects it contains are mutable, those 
# internal objects can be changed
