import time

start = time.time()
print(start)
print(type(start))

# evening = time(hour= 23, minute= 23, second= 45)
# print(evening)
# print(evening.hour, evening.minute, evening.second)

# print("\n --- Ejercicio --- \n")

# # Declare a titanic variable pointing to a date object representing April 14th, 1912
# # Declare an independence_day variable pointing to a date object representing July 4th, 1776
# # Declare an alarm_clock variable set to a time object representing 05:45:00AM
# # Declare a one_second_away variable set to a time object representing 11:59:59PM

# # titanic = date(month=4, day=14, year=1912)
# # print(titanic)

# # independence_day = date(month=7, day=4, year=1776)

# alarm_clock = time(hour= 5, minute= 45)

# one_second_away = time(23, 59, 59)

finish = time.time()
print(finish)


total_time = start - finish
print(total_time)