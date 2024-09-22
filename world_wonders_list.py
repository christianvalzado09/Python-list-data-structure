# world_wonders_list.py

# Create a list of 7 wonders of the world
wonders = [
    "Great Pyramid of Giza",
    "Hanging Gardens of Babylon",
    "Statue of Zeus at Olympia",
    "Temple of Artemis at Ephesus",
    "Mausoleum at Halicarnassus",
    "Colossus of Rhodes",
    "Lighthouse of Alexandria"
]
print(wonders)

print("the 4th index is",wonders[3])
print(wonders)

wonders[1]= "Great Wall of China"
print(wonders)

del wonders[4]

print("the last index is",wonders[-1])