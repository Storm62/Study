import datetime

date = datetime.date.isoformat(datetime.date.today())
day = "2021-07-18"

if date in day:
    print("Сегодня " + date)
else:
    print("Cегодня другая дата")
