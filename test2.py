import datetime
now = datetime.date.today()

tarih = open("deneme.txt").read()
bugun = (now.strftime("%Y%m%d"))
tarih1 = int(tarih)
bugun1 = int(bugun)
fark = bugun1 - tarih1
print(fark)

if fark > 0:
    print("bugun oynayabilirsiniz")
else:
    print("bugun zaten oynadın")