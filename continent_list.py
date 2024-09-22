# continent_list.py

# Create a list of 7 continents
continents = [
    "Asia",
    "North America",
    "South America",
    "Europe",
    "Africa",
    "Australia",
    "Antarctica"
]
print(continents)

print("the 4th index is",continents[3])
print(continents)

continents[1] = "Africa"
print(continents)

del continents[5]

print("the last index is", continents[-1])