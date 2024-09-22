# festival_list.py
# Create a list of 15 festivals around the world
festivals = [
    "Carnival",
    "Oktoberfest",
    "Holi",
    "Mardi Gras",
    "Thanksgiving",
    "Bastille Day",
    "Chinese New Year",
    "Harbin Ice Festival",
    "La Tomatina",
    "Gion Matsuri",
    "Day of the Dead",
    "Burning Man",
    "Songkran",
    "Rio Carnival",
    "Sapporo Snow Festival"
]
print(festivals)

print("the 7th index is",festivals[6])
print(festivals)

festivals[10]= "Diwali"
print(festivals)

del festivals[8]

print(festivals[5:12])

print("the last index is",festivals[-1])