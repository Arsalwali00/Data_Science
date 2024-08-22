# Lists are a good way to organize data, but one drawback is that we can only represent values. 
# Why is that a problem? For example, someone looking at [115910.26, 128.0, 4] wouldn't know
# which values corresponded to price, area, etc. A better option might be a dictionary, where each 
# value is associated with a key. Here's what house_0 looks like as a dictionary instead of a list.

# Declare variable `house_0_dict`
house_0_dict = {
    "price_approx_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}

# Print `house_0_dict` type
print("house_0_dict type:", type(house_0_dict))

# Get output of `house_0_dict`
print(house_0_dict)