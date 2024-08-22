houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

# Create for loop to iterate through `houses_nested_list`

for house in houses_nested_list:
    # For each observation, append price / sq. meter
    price_m2=house[0] / house[1]
    house.append(price_m2)


# Print `houses_nested_list` type
print("houses_nested_list type:", type(houses_nested_list))

# Print `houses_nested_list` length
print("houses_nested_list length:", len(houses_nested_list))

# Get output of `houses_nested_list`
print(houses_nested_list)