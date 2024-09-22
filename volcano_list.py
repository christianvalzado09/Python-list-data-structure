# volcano_list.py

# Create a list of 7 famous volcanoes
volcanoes = [
    "Mount St. Helens",
    "Kilauea",
    "Mount Fuji",
    "Mount Kilimanjaro",  # This will be updated
    "Mauna Loa",
    "Mount Etna",
    "Mount Apo"
]
print(volcanoes)

print("the 4th index is",volcanoes[3])
print(volcanoes)

volcanoes[2]= "Mount Vesuvius"
print(volcanoes)

del volcanoes[4]

print("the last index is",volcanoes[-1])