import pandas as pd

# Load CSV files into DataFrames
df1 = pd.read_csv("Clean_Csv/pak-real-estate-1-clean.csv")
df2 = pd.read_csv("Clean_Csv/pak-real-estate-2-clean.csv")
df3 = pd.read_csv("Clean_Csv/pak-real-estate-3-clean.csv")

# Task 1.2.7: Use pd.concat to concatenate df1, df2, df3 as 
# new DataFrame named df. Your new DataFrame should have 1,736 rows and 6 columns:
# "property_type", "state", "lat", "lon", "area_m2", and "price_usd"

# Concatenate df1, df2, and df3
df = pd.concat([df1,df2,df3])

# Print object type, shape, and head
print("df type:", type(df))
print("df shape:", df.shape)
print(df.head())

# Save df
# The data is clean and in a single DataFrame, and now you need to save it as 
# a CSV file so that you can examine it in your exploratory data analysis.

df.to_csv('Clean & Concatenate-Final.csv', index=False)