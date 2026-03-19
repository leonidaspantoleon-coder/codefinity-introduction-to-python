seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100

# Overstock boolean
overstock_risk = seasonal and (current_stock > high_stock_threshold)

# discount eligibility
discount_eligible = not selling_well and not on_sale

# make discount
make_discount = overstock_risk or discount_eligible

# Discount decision output
print("Should the item be discounted?", make_discount)