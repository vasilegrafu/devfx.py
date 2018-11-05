import pytz as tz

print([tz.timezone(_) for _ in tz.all_timezones])
print([_ for _ in tz.all_timezones])
print([tz.timezone(_) for _ in tz.country_timezones('us')])
print([tz.timezone(_) for _ in tz.country_timezones('cn')])
print([tz.timezone(_) for _ in tz.country_timezones('ru')])
print([tz.timezone(_) for _ in tz.country_timezones('ro')])


