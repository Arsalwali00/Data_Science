# Declare variable `house_0_list`
house_0_list = [115910.26, 128, 4]

# Declare variable `house_0_price_m2`
house_0_price_m2 = house_0_list[0]/house_0_list[1]

# Append price / sq. meter to `house_0_list`
house_0_list.append(house_0_price_m2)

# Print object type of `house_0_list`
print("house_0_list type:", type(house_0_list))

# Print length of `house_0_list`
print("house_0_list length:", len(house_0_list))

# Get output of `house_0_list`
print(house_0_list)