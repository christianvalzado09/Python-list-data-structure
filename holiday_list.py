# holiday_list.py

# Create a list of 12 holidays
holidays = [
    "New Year's Day",
    "Valentine's Day",
    "Easter",
    "Thanksgiving",
    "Independence Day",
    "Labor Day",
    "Halloween",
    "Memorial Day",
    "Veterans Day",
    "Hanukkah",
    "Diwali",
    "Midsummer"
]
print(holidays)

print("the 9th index is",holidays[8])
print(holidays)

holidays[2] = "Christmas"
print(holidays)

del holidays[10]

print(holidays[2:7])

print("the last index is ",holidays[-1])