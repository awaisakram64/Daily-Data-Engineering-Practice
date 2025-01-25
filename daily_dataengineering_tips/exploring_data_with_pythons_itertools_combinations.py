from itertools import combinations

# Sample dataset of product IDs
products = [101, 102, 103, 104]

# Find all 2-item combinations of the products
combos = list(combinations(products, 2))

print("All 2-item combinations of products:")
print(combos)