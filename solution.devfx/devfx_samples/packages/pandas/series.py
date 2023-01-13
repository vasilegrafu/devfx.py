import pandas as pd

print("Create a four item DataFrame:")
s = pd.Series([1, 2, 3, 4])
print(s)

print("Return a Series with the rows with labels 1 and 3:")
print(s[[1, 3]])

print("Create a series using an explicit index:")
s = pd.Series([1, 2, 3, 4], index = ['a', 'b', 'c', 'd'])
print(s)

print("Return a Series with the rows with labels 1 and 3:")
print(s[[1, 3]])

print("Look up items the series having index 'a' and 'd':")
print(s[['a', 'd']])

print("Passing a list of integers to a Series that has non-integer index labels will look up based upon 0-based index like an array:")
print(s[[1, 2]])

print("Get only the index of the Series:")
print(s.index)

print("Create a Series who's index is a series of dates between the two specified dates (inclusive):")
date_range = pd.date_range('2014-07-01', '2014-07-06')
print(date_range)

print("Create a Series with values (representing temperatures) for each date in the index:")
temps1 = pd.Series([80, 82, 85, 90, 83, 87], index = date_range)
print(temps1)

print("Calculate the mean of the values in the Series:")
print(temps1.mean())

print("Create a second series of values using the same index:")
temps2 = pd.Series([70, 75, 69, 83, 79, 77], index = date_range)
print(temps2)

print("The following aligns the two by their index values and calculates the difference at those matching labels:")
temp_diffs = temps1 - temps2
print(temp_diffs)

print("Lookup a value by date using the index:")
print(temp_diffs['2014-07-03'])

print("And also possible by integer position as if the series was an array:")
print(temp_diffs[2])

