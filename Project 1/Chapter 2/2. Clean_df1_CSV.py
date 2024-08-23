import pandas as pd 

# Task 1.2.2: Inspect df1 by looking at its shape attribute. Then use the info method to see the data 
# types and number of missing values for each column. Finally, use the head method to determine to 
# look at the first five rows of your dataset.
# Load CSV files into DataFrames
df1 = pd.read_csv("Resources/pak-real-estate-1.csv")
# Print df1 shape
print(df1.shape)

# Print df1 info
print(df1.info())

# Get output of df1 head
print(df1.head())

# It looks like there are a couple of problems in this DataFrame that you need to solve. First,
# there are many rows with NaN values in the "lat" and "lon" columns. Second, the 
# data type for the "price_usd" column is object when it should be float.

print("_______________Cleaning CSV__________________________")
# Drop null values from df1
df1.dropna(inplace=True)

# Clean "price_usd" column in df1
df1["price_usd"]= (
       df1["price_usd"]
      .str.replace("$","")
      .str.replace(",","")
      .astype(float)           
                   )

# Print object type, shape, and head
print("df1 type:", type(df1))
print("df1 shape:", df1.shape)
print(df1.head())


df1.to_csv('pak-real-estate-1-clean.csv', index=False)