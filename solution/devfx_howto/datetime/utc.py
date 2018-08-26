import datetime as dt
import pytz as tz

timezone = tz.timezone(tz.country_timezones('ro')[0])
datetime = dt.datetime.now(timezone)
print(datetime)

datetime = datetime.astimezone(tz.utc)
print(datetime)

