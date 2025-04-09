from datetime import datetime, timedelta

birthday = datetime(2002, 3, 1)
today = datetime.now()

my_life_span = today - birthday
print(my_life_span)

print()
print(my_life_span.total_seconds())

one_year = timedelta(days= 365)

print()
# What date is it going to be in one year
print(today + one_year)




time1 = datetime.now()

seconds = time1 - birthday

print(seconds.total_seconds())