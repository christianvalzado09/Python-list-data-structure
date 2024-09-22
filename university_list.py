# university_list.py

# Create a list of 10 universities
universities = [
    "Stanford University",
    "Massachusetts Institute of Technology",
    "University of California, Berkeley",
    "California Institute of Technology",  # This will be updated to Harvard University
    "University of Oxford",
    "University of Cambridge",
    "Columbia University",
    "University of Chicago",
    "Yale University",                      # This will be deleted
    "University of Pennsylvania"
]

print(universities)

print("the 6th index is",universities[5])
print(universities)

universities[3]= "Harvard University"
print(universities)

del universities[8]
print("the last index is",universities[-1])