# Clean df3
# Great work! We're now on the final DataFrame. Use the same shape, info and head commands to
# inspect the df3. Do you see any familiar issues?

# You'll notice that we still have NaN values, but there are two new problems:

# Instead of separate "lat" and "lon" columns, there's a single "lat-lon" column.
# Instead of a "state" column, there's a "place_with_parent_names" column.
# We need the resolve these problems so that df3 has the same columns in the same format as df1 and df2.

import pandas as pd

# Load CSV files into DataFrames
df3 = pd.read_csv("Resources/pak-real-estate-3.csv")

# Task 1.2.5: Drop rows with NaN values in df3. Then use the split method to create two new columns 
# from "lat-lon" named "lat" and "lon", respectively.

print("___________Task 1.2.5_____________________")

# Drop null values from df3
df3.dropna(inplace=True)

# Create "lat" and "lon" columns for df3
df3[["lat", "lon"]] = df3["lat-lon"].str.split(",", expand=True)

# Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
print(df3.head())

# Task 1.2.6: Use the split method again, this time to extract the state for every house. 
# (Note that the state name always appears after "Paksitan|" in each string.) Use this information 
# to create a "state" column. Finally, drop the 
# "place_with_parent_names" and "lat-lon" columns from the DataFrame.


print("___________Task 1.2.6_____________________")

# Create "state" col from "place_with_parent_names"
df3["state"]=df3["place_with_parent_names"].str.split("|", expand=True)[2]

#drop col
df3.drop(columns=["place_with_parent_names","lat-lon"], inplace=True)


# Print object type, shape, and head
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
print(df3.head())

df3.to_csv('pak-real-estate-3-clean.csv', index=False)

