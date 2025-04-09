breakfasts = ["Eggs", "Cereal", "Banana"]
lunches = ["Sushi", "Chiken Teriyaki", "Soup"]
dinners = ["Steak", "Meat balls", "Pasta"]

print(type(zip(breakfasts, lunches, dinners)))
print(list(zip(breakfasts, lunches, dinners)))

print()

for breakfast, lunch, dinner in zip(breakfasts, lunches, dinners):
    print(f"My meal of today was {breakfast}, {lunch} and {dinner}\n")