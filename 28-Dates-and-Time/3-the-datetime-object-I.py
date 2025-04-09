from datetime import datetime

inicio = datetime.now()
print(datetime(year=2002, month= 3, day= 1, hour= 5, minute=0, second= 32))


today = datetime.now()
print(today)
print(today.weekday())

same_time_twenty_years_ago = today.replace(year= 2004)
print(same_time_twenty_years_ago)


final = datetime.now()

print(inicio - final)