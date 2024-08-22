# While you've shown that you can wrangle data using lists and dictionaries, 
# it's not as intuitive as working with, say, a spreadsheet. Fortunately, 
# there are lots of libraries for Python that make it an even better tool 
# for tabular data — way better than spreadsheet applications like Microsoft Excel 
# or Google Sheets! One of the best known data science libraries is pandas, 
# # which allows you to organize data into DataFrames 


houses_columnwise = {
    "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}

# Import pandas library, aliased as `pd`
import pandas as pd

# Declare variable `df_houses`
df_houses = pd.DataFrame(houses_columnwise)

# Print `df_houses` object type
print("df_houses type:", type(df_houses))

# Print `df_houses` shape
print("df_houses shape:", df_houses.shape)

# Get output of `df_houses`
print(df_houses)