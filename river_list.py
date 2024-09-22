# river_list.py

# Create a list of 10 famous rivers
rivers = [
    "Colorado River",
    "Nile River",
    "Yangtze River",
    "Mississippi River",
    "Yellow River",
    "Ganges River",
    "Danube River",
    "Rio Grande",  # This will be updated
    "Volga River",
    "Zambezi River"
]
print(rivers)

print("the 6th index is",rivers[5])
print(rivers)

rivers[7]= "Nile River"
print(rivers)

del rivers[8]

print("the last index is",rivers[-1])
