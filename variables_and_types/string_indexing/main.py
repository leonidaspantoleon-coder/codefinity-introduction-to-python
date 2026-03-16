grocery_item = "Grilled Chicken Salad"

# Accessing first and last character using indexing
first_character = grocery_item[0] # 'G'
last_character = grocery_item[-1] # 'd' using negative indexing
print(first_character, last_character)
print("First character:", first_character)
print("Last character:", last_character)

# Setting length of Grocery Item
length_of_item = (len(grocery_item)) # '21' characters

# Setting first letter of each word
first_char = grocery_item[0] # 'G'
second_char = grocery_item[8] # 'C'
third_char = grocery_item[-5] # 'S'

print("First character first word:", first_char)
print("First character second word:", second_char)
print("First character third world:", third_char)

# Setting last character of each word
last_char1 = grocery_item[6] # 'd'
last_char2 = grocery_item[-7] # 'n'
last_char3 = grocery_item[-1] # 'd'

print("Last character first word:", last_char1)
print("Last character second word:", last_char2)
print("Last character third word:", last_char3)

# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)