import pandas as pd

# Load CSV files into DataFrames
df1 = pd.read_csv("Resources/pak-real-estate-1.csv")
df2 = pd.read_csv("Resources/pak-real-estate-2.csv")
df3 = pd.read_csv("Resources/pak-real-estate-3.csv")

# Print object type and shape for DataFrames
print("df1 type:", type(df1))
print("df1 shape:", df1.shape)
print("df2 type:", type(df2))
print("df2 shape:", df2.shape)
print("df3 type:", type(df3))
print("df3 shape:", df3.shape)
