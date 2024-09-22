# continent_country_list.py

# Create a list of 15 countries and the continents they belong to
countries = [
    "Canada",          # North America
    "Brazil",          # South America
    "United Kingdom",  # Europe
    "Germany",         # Europe
    "India",           # Asia
    "China",           # Asia
    "Phillipines",      # Asia
    "Nigeria",         # Africa
    "Russia",          # Europe
    "Japan",           # Asia
    "South Africa",    # Africa
    "Argentina",       # South America
    "Egypt",           # Africa
    "Mexico",          # North America
    "Italy"            # Europe
]
print(countries)

print("the 9th index is",countries[8])
print(countries)

countries[9]= "Australia"
print(countries)

del countries[11]

print(countries[4:8])
print("the last index is",countries[-1])