import numpy as np
import pandas as pd

print("Create a DatetimeIndex of dates between the two specified dates (inclusive):")
date_range = pd.date_range('2014-07-01', '2014-07-06')
print(date_range)

print("Create a Series with values (representing temperatures) for each date in the index:")
temps1 = pd.Series([80, 82, 85, 90, 83, 87], index = date_range)
print(temps1)

print("Create a second Series of values using the same index:")
temps2 = pd.Series([70, 75, 69, 83, 79, 77], index = date_range)
print(temps2)

print("Create a DataFrame from the two series objects temps1 and temps2 and give them column names:")
temps_df = pd.DataFrame({'Missoula': temps1, 'Philadelphia': temps2})
print(temps_df)

print("Get the column with the name Missoula:")
print(temps_df['Missoula'])

print("Get the column with the index:")
print(temps_df.iloc[:, 0])

print("Return both columns in a different order:")
print(temps_df[['Philadelphia', 'Missoula']])

print("Retrieve the Missoula column through property syntax:")
print(temps_df.Missoula)

print("Calculate the temperature difference between the two cities:")
temp_diffs = temps_df.Missoula - temps_df.Philadelphia
print(temp_diffs)

print("Add a column to temp_df that contains the difference in temps:")
temps_df['Difference'] = temp_diffs
print(temps_df)

print("Get the columns, which is also an Index object:")
print(temps_df.columns)

print("Slice the rows at location 1 through 4 (as though it is an array):")
print(temps_df[1:4])

print("Slice the differences column for the rows at location 1 through 4 (as though it is an array):")
print(temps_df.Difference[1:4])

print("Get some row:")
print(temps_df.iloc[1])

print("Get some rows:")
print(temps_df.iloc[1])
print(temps_df.iloc[1:3])

print("Get some row:")
print(temps_df.loc['2014-07-03'])

print("Get some rows:")
print(temps_df.loc[[np.datetime64('2014-07-03'), np.datetime64('2014-07-04')]])

print("Which values in the Missoula column are > 82:")
print(temps_df.Missoula > 82)

print("Return the rows where the temps for Missoula > 82:")
print(temps_df[temps_df.Missoula > 85])