import random 

print(random.choice(["Josafat", "Josa", "Peque"]))
print(random.choice((1, 2, 3, 4)))
print(random.choice("jirafa"))


lottery_numbers = [random.randint(1, 50) for value in range(50)]
print(lottery_numbers)

print()
print(random.sample(lottery_numbers, 4))