# Task: Calulate Price per meter square 


houses_columnwise = {
    "price_approx_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}

price = houses_columnwise["price_approx_usd"]
area = houses_columnwise["surface_covered_in_m2"]
price_per_m2=[]
for p, a in zip(price,area):
    price_m2= p/a
    price_per_m2.append(price_m2)
    
# Add "price_per_m2" key-value pair for `houses_columnwise`
    houses_columnwise['price_per_m2'] = price_per_m2


# Print `houses_columnwise` object type
print("houses_columnwise type:", type(houses_columnwise))

# Get output of `houses_columnwise`
print(houses_columnwise)