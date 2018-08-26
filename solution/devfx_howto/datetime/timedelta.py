import datetime as dt

datetime1 = dt.datetime.now()
print(datetime1)

datetime2 = datetime1 + dt.timedelta(days=1)
print(datetime2)

print(datetime2-datetime1)