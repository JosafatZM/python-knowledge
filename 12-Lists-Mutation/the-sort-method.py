# this method sorts the list 

temperatures = [1, 45, 89, 35, 26, 23, 90, 76, 100]
temperatures.sort()
print(temperatures[0])

print()
# if you wanna do it in reverse order you have to...
temperatures.sort()
temperatures.reverse()
print(temperatures)

# The same if you are working with strings
coffees = ["Latte", "Nespresso", "Macchiato", "Frappucino"]
coffees.sort()
print(coffees)

# Python cares about the characterization so it sorts the capital 
# letters first
coffees = ["Latte", "nespresso", "Macchiato", "frappucino"]
coffees.sort()
print(coffees)

coffees = ["Latte", "Nespresso", "Macchiato", "Frappucino"]
print(sorted(coffees))

print()
numbers = [1, 4, 5, 7, 9]
numbers[1:3] = [6, 8]
print(numbers)