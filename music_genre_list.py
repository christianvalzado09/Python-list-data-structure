# music_genre_list.py

# Create a list of 15 music genres
music_genres = [
    "Pop",
    "Rock",
    "Hip Hop",
    "Country",
    "Classical",
    "Electronic",
    "Reggae",
    "Blues",
    "R&B",
    "Metal",
    "Funk",  # Updated from Jazz to Funk
    "Folk",
    "Indie",
    "Latin",
    "Punk",
    "Gospel"
]
print(music_genres)

print("the 10th index is",music_genres[9])
print(music_genres)

music_genres[4]= "Jazz"
print(music_genres)

del music_genres[6]

print(music_genres[3:8])
print("the last index is",music_genres[-1])