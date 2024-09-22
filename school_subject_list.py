# school_subject_list.py

# Create a list of 12 school subjects
subjects = [
    "English",
    "Science",
    "History",
    "Geography",
    "Art",
    "Physical Education",
    "Music",
    "Computer Science",
    "Chemistry",  # Updated from Mathematics to Chemistry
    "Literature",
    "Economics",
    "Biology"
]
print(subjects)

print("the 6th index is",subjects[5])
print(subjects)

subjects[7]= "Mathematics"
print(subjects)

del subjects[3]

print(subjects[2:5])
print("the lst index is",subjects[-1])