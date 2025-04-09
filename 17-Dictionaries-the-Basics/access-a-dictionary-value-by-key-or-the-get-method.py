flight_prices = {
    "Chicago": 199,
    "Dember": 295,
    "San Francisco": 499
}

print(flight_prices["Chicago"])
print(flight_prices["Dember"])

gym_membership_packages = {
    29: ["Machines"],
    49: ["Machines", "Vitamin Supplements"],
    79: ["Machines", "Vitamin Supplements", "Sauna"]
}

print()

print(gym_membership_packages[79])

# If a KEY does not exists you get a KeyERROR

# There is a method called ".get()" this method accepts 2 arguments
# the first one is the key whose value you want to return and the
# second is going to be a default value to return if the key does not 
# exist in the dictionary.

print()

print(gym_membership_packages.get(29, "Hola pene"))
print(gym_membership_packages.get(99, ["Hola pene"]))
print(gym_membership_packages.get(99))