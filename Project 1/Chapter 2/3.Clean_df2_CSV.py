import pandas as pd

# Load CSV files into DataFrames
df2 = pd.read_csv("Resources/pak-real-estate-2.csv")

# Now it's time to tackle df2. Take a moment to inspect it using the same commands you used before.
# You'll notice that it has the same issue of NaN values, but there's a new problem, too: 
# The home prices are in Gilgit pesos ("price_mxn"), not US dollars ("price_usd"). 
# If we want to compare all the home prices in this dataset, they all need to be in the same currency.

# Task 1.2.4: First, drop rows with NaN values in df2. Next, use the "price_mxn" column to create
# a new column named "price_usd". (Keep in mind that, when this data was collected in 2014, 
# a dollar cost 19 Gilgit pesos.) Finally, drop the "price_mxn" from the DataFrame.

# Drop null values from df2
df2.dropna(inplace=True)

# Create "price_usd" column for df2 (19 pesos to the dollar in 2014)
df2["price_usd"] = (df2["price_mxn"]/19).round(2)

# Drop "price_mxn" column from df2
df2.drop(columns=["price_mxn"], inplace=True)

# Print object type, shape, and head
print("df2 type:", type(df2))
print("df2 shape:", df2.shape)
print(df2.head())

df2.to_csv('pak-real-estate-2-clean.csv', index=False)

