from datetime import datetime 


today = datetime.today()
print(today)
print(today.strftime("%d/%m/%Y"))
print(today.strftime("%d/%m/%y"))


print(today.strftime("%A"))
print(today.strftime("%B"))
print(today.strftime("%a"))

formatted_time_with_milliseconds = today.strftime("%I:%M:%S.%f %p")  # %f for milliseconds

print(f"The formatted time with milliseconds for is {formatted_time_with_milliseconds}.")


print("\n --- Ejercicio ---")

# Define a one_from_two function that accepts a date object and a time object
# It should return a datetime object consisting of 
#     - the year, month and day from the date object 
#     - the hour, minutes, and seconds from the time object
#
# EXAMPLE:
#
from datetime import date, time, datetime
some_date = date(2002, 2, 22)
some_time = time(9, 45, 23)


def one_from_two(some_date, some_time):

    formated_date = some_date.strftime("%Y-%m-%d")
    formated_time = some_time.strftime("%I:%M:%S")

    print(f"{formated_time} {formated_date}")

one_from_two(some_date, some_time) # datetime object representing 2002-02-22 09:45:23


# RETURNING A DATETIME OBJECT

def one_from_two(some_date, some_time):

    year = some_date.year
    month = some_date.month
    day = some_date.day 

    hour = some_time.hour
    minute = some_time.minute
    second = some_time.second

    return datetime(year, month, day, hour, minute, second)
