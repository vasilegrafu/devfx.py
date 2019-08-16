import numpy as np
import datetime as dt

print("----------------------------------------------------------------")

datetime = np.datetime64('2017-01-01')
print(datetime)

datetime = np.datetime64('2017-01-01T00')
print(datetime)

datetime = np.datetime64('2017-01-01T00:00')
print(datetime)

datetime = np.datetime64('2017-01-01T00:00:00')
print(datetime)

datetime = np.datetime64('2017-01-01T00:00:00Z')
print(datetime)

datetime = np.datetime64('2017-01-01T00:00:00+02:00')
print(datetime)

print("----------------------------------------------------------------")
datetimes = np.arange('2017-01-01', '2018-01-01', dtype='datetime64[D]')
print(datetimes)

print(datetimes[datetimes <= np.datetime64('2017-01-05')])

print(type(datetimes[0]))

print("----------------------------------------------------------------")
"""
The Datetime and Timedelta data types support a large number of time units, as well as generic units which can be coerced into any of the other units based on input data.

Datetimes are always stored based on POSIX time (though having a TAI mode which allows for accounting of leap-seconds is proposed), with a epoch of 1970-01-01T00:00Z.
This means the supported dates are always a symmetric interval around the epoch, called “time span” in the table below.

The length of the span is the range of a 64-bit integer times the length of the date or unit.
For example, the time span for ‘W’ (week) is exactly 7 times longer than the time span for ‘D’ (day), and the time span for ‘D’ (day) is exactly 24 times longer than the time span for ‘h’ (hour).

Here are the date units:
Code 	Meaning 	Time span (relative) 	Time span (absolute)
Y 	year 	+/- 9.2e18 years 	[9.2e18 BC, 9.2e18 AD]
M 	month 	+/- 7.6e17 years 	[7.6e17 BC, 7.6e17 AD]
W 	week 	+/- 1.7e17 years 	[1.7e17 BC, 1.7e17 AD]
D 	day 	+/- 2.5e16 years 	[2.5e16 BC, 2.5e16 AD]

And here are the time units:
Code 	Meaning 	Time span (relative) 	Time span (absolute)
h 	hour 	+/- 1.0e15 years 	[1.0e15 BC, 1.0e15 AD]
m 	minute 	+/- 1.7e13 years 	[1.7e13 BC, 1.7e13 AD]
s 	second 	+/- 2.9e11 years 	[2.9e11 BC, 2.9e11 AD]
ms 	millisecond 	+/- 2.9e8 years 	[ 2.9e8 BC, 2.9e8 AD]
us 	microsecond 	+/- 2.9e5 years 	[290301 BC, 294241 AD]
ns 	nanosecond 	+/- 292 years 	[ 1678 AD, 2262 AD]
ps 	picosecond 	+/- 106 days 	[ 1969 AD, 1970 AD]
fs 	femtosecond 	+/- 2.6 hours 	[ 1969 AD, 1970 AD]
as 	attosecond 	+/- 9.2 seconds 	[ 1969 AD, 1970 AD]
"""

datetime1 = dt.datetime.now()
print("[1.1]:", datetime1, type(datetime1))
datetime2 = datetime1 + dt.timedelta(days=1)
print("[1.2]:", datetime2, type(datetime2))

datetime_list = [datetime1, datetime2]
print("[2.1]:", datetime_list, type(datetime_list))
timedelta = datetime2 - datetime1
print("[2.2]:", timedelta, type(timedelta))

datetime_array1 = np.asarray(datetime_list)
print("[3.1]:", datetime_array1, type(datetime_array1))
timedelta0 = datetime_array1[1]-datetime_array1[0]
print("[3.2]:", timedelta0, type(timedelta0))
timedelta1 = np.timedelta64(timedelta0)
print("[3.3]:", timedelta1, type(timedelta1))
timedelta2 = np.timedelta64(timedelta0, 's')
print("[3.4]:", timedelta2, type(timedelta2))

datetime_array2 = np.asarray(datetime_list, dtype='datetime64[us]')
print("[4.1]:", datetime_array2, type(datetime_array2))
timedelta0 = datetime_array2[1]-datetime_array2[0]
print("[4.2]:", timedelta0, type(timedelta0))
timedelta1 = np.timedelta64(timedelta0)
print("[4.3]:", timedelta1, type(timedelta1))
timedelta2 = np.timedelta64(timedelta0, 's')
print("[4.4]:", timedelta2, type(timedelta2))

timedelta1 = timedelta1.astype(dt.timedelta)
print("[5.1]:", timedelta1, type(timedelta1))
timedelta2 = timedelta2.astype(dt.timedelta)
print("[5.2]:", timedelta2, type(timedelta2))

timedelta_array = np.asarray([timedelta, timedelta])
print("[6.1]:", timedelta_array, type(timedelta_array))
timedelta_array = timedelta_array.astype(dt.timedelta)
print("[6.2]:", timedelta_array, type(timedelta_array))

timedelta_array = np.asarray([timedelta, timedelta], dtype='timedelta64[us]')
print("[7.1]:", timedelta_array, type(timedelta_array))
timedelta_array = timedelta_array.astype(dt.timedelta)
print("[7.2]:", timedelta_array, type(timedelta_array))

timedelta_array_us = np.asarray([timedelta, timedelta], dtype='timedelta64[us]')
print("[8.1]:", timedelta_array_us, type(timedelta_array_us))
timedelta_array_h = timedelta_array_us/np.timedelta64(1, 'h')
print("[8.2]:", timedelta_array_h, type(timedelta_array_h))



