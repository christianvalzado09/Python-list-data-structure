# building_list.py

# Create a list of 8 famous buildings
buildings = [
    "Taj Mahal",
    "Empire State Building",
    "Burj Khalifa",  # This will be replaced
    "Colosseum",
    "Louvre Museum",
    "Sydney Opera House",
    "Petra",
    "Big Ben"
]
print(buildings)

print("the 5th index is",buildings[4])
print(buildings)

buildings[1]= "Eifell tower"
print(buildings)

del buildings[5]

print("the last index is",buildings[-1])