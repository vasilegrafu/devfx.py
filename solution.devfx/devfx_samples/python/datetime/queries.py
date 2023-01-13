import datetime as dt

datetimes = []

datetime = dt.datetime.now()

i = 1
while(i <= 10):
    timedelta = dt.timedelta(days=1)
    datetime = datetime + timedelta
    datetimes.append(datetime)
    i += 1

print(datetimes)
print([datetime for datetime in datetimes if (datetime <= dt.datetime.now() + dt.timedelta(days=5))])
