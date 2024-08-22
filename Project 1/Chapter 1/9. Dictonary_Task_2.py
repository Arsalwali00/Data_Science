# Using a for loop, calculate the price per square meter and store the result under 
# a "price_per_m2" key for each observation in houses_rowwise.

houses_rowwise = [
    {
        "price_approx_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_approx_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_approx_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_approx_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_approx_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]

# Create for loop to iterate through `houses_rowwise`
for house in houses_rowwise:
    # For each observation, add "price_per_m2" key-value pair
    house["price_per_m2"] = house["price_approx_usd"] / house["surface_covered_in_m2"]
    

# Print `houses_rowwise` object type
print("houses_rowwise type:", type(houses_rowwise))

# Print `houses_rowwise` length
print("houses_rowwise length:", len(houses_rowwise))

# Get output of `houses_rowwise`
print(houses_rowwise)