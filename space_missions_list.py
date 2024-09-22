# space_missions_list.py

# Create a list of 10 space missions
space_missions = [
    "Apollo 1",
    "Apollo 7",
    "Apollo 8",
    "Mars Pathfinder",
    "Apollo 12",
    "Apollo 13",
    "Skylab 1",
    "Voyager 1",
    "Challenger STS-51-L",
    "Mars Rover Curiosity"
]
print(space_missions)

print("the 7th index is",space_missions[6])
print(space_missions)

space_missions[3]= "Apollo 11"
print(space_missions)

del space_missions[5]

print("the last index is",space_missions[-1])