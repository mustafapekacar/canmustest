import datetime
now = datetime.date.today()

with open("deneme.txt", "w") as f:
    f.write(now.strftime("%Y%m%d"))