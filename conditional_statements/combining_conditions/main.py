# The item's discount and stock status have been defined
discounted = False
lowStock = True

# Boolean whether a moving product
movingProduct = not discounted or lowStock
promotion = discounted and not lowStock

# Promotion Output
print("Is the item eligible for promotion?", promotion)