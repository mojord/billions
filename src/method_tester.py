from datetime import datetime


date = "02.03.1867"

real_date = datetime.strptime(date, "%d.%m.%Y")

print(real_date)