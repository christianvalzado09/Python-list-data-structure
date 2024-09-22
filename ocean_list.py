# ocean_list.py

# Create a list of 5 oceans
oceans = [
    "Atlantic Ocean",
    "Indian Ocean",
    "Arctic Ocean",  # This will be updated
    "Southern Ocean",
    "Mediterranean Sea"
]
print(oceans)

print("the 3rd index is",oceans[2])
print(oceans)

oceans[1]= "Pacific Ocean"
print(oceans)

del oceans[3]

print("the last index is",oceans[-1])
