# Task 1.1.4: Calculate the price per square meter for house_0 and add it 
# to the dictionary under the key "price_per_m2".

house_0_dict = {
    "price_approx_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}

# Add "price_per_m2" key-value pair to `house_0_dict`
house_0_dict["price_per_m2"] = house_0_dict["price_approx_usd"] / house_0_dict["surface_covered_in_m2"]

# Get output of `house_0_dict`
print(house_0_dict)