grocery_items = "milk cheese bread apples oranges chicken"
# Slicing Grocery items into components
G_item1 = grocery_items[0:4] # milk
G_item2 = grocery_items[5:11] # cheese
G_item3 = grocery_items[12:17] # bread
G_item4 = grocery_items[18:24] # apples
G_item5 = grocery_items[25:32] # oranges
G_item6 = grocery_items[33:] # chicken

# Using concatenation to build a string
print(G_item1 + " " + G_item2) # milk cheese
print(G_item3 + " " + G_item4) # bread apples
print(G_item5 + " " + G_item6) # oranges chicken

_1st_pair_items = f"{G_item1} and {G_item2}" # milk and cheese
_2nd_pair_items = f"{G_item3} and {G_item4}" # bread and apples
_3rd_pair_items = f"{G_item5} and {G_item6}" # oranges and chicken

print("Items 1 and 2:", _1st_pair_items)
print("Items 3 and 4:", _2nd_pair_items)
print("Items 5 and 6:", _3rd_pair_items)

#Slicing string
dairy1 = grocery_items[0:4] # milk
dairy2 = grocery_items[5:11] # cheese
bakery1 = grocery_items[12:17] # bread
aisle = 5
message = dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle " + str(aisle) + "."

# Output requirements
print("We have dairy and bakery items:", message)

print(f"We have dairy and bakery items: {dairy1}, {dairy2}, and {bakery1} in aisle {aisle}.")