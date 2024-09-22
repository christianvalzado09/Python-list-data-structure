# recipe_list.py

# Create a list of 15 recipes
recipes = [
    "Spaghetti",
    "Tacos",
    "Sushi",
    "Pancakes",
    "Fried Rice",
    "Curry",
    "Grilled Cheese",
    "Chili",
    "Moussaka",
    "Caesar Salad",
    "Baked Ziti",
    "Chocolate Cake",
    "Apple Pie",
    "Meatloaf",
    "Beef Stroganoff"
]
print(recipes)

print("the 12th index is",recipes[11])
print(recipes)

recipes[8]= "Lasagna"
print(recipes)

del recipes[10]

print(recipes[5:10])

print("the last index is",recipes[-1])