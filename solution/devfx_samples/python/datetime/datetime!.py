import datetime as dt
import pytz as tz

print("----------------------------------------------------------------")

datetime = dt.datetime.now()
print(datetime)

datetime_str = datetime.strftime('%Y-%m-%d %H:%M:%S.%f')
print(datetime_str)

datetime = datetime.strptime(datetime_str, '%Y-%m-%d %H:%M:%S.%f')
print(datetime)


print("----------------------------------------------------------------")

timezone = tz.timezone('Europe/Bucharest')
print(timezone)


print("----------------------------------------------------------------")

# naive
datetime = dt.datetime.now()

datetime_str = datetime.strftime('%Y-%m-%dT%H:%M:%S.%f')
print(datetime_str)


# aware
datetime = datetime.now(timezone)

datetime_str = datetime.strftime('%Y-%m-%dT%H:%M:%S.%f%z')
print(datetime_str)

datetime_str = datetime.strftime('%Y-%m-%dT%H:%M:%S.%f%Z')
print(datetime_str)