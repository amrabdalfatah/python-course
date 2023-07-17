# Lists
# Collection to store multiple values
# allow duplicate
# len() length list
fruits = ['apple', 34, True, 'banana', 'orange'] 
# Access Items
# Check if item exists
# Change List Items
# 1- change value or item
fruits[1] = 'kiwi'
print(fruits)

# 2- change range of items
"""
fruits[1:3] = ["kiwi", "lemon", 'apple']
print(fruits)
"""
# how to insert or add new items to list
fruits.insert(2, 'mango')
fruits.append('amr')
fruits.append('adel')
print(fruits)
# remove items
fruits.remove('amr')
fruits.pop(3)
del fruits[0]
fruits.clear()
print(fruits)
