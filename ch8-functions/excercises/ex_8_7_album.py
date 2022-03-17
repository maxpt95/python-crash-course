# Write a function called make_album() that builds a dictionary
# describing a music album. The function should take in an artist name and an
# album title, and it should return a dictionary containing these two pieces of
# information. Use the function to make three dictionaries representing different
# albums. Print each return value to show that the dictionaries are storing the
# album information correctly.
# Use None to add an optional parameter to make_album() that allows you to
# store the number of songs on an album. If the calling line includes a value for
# the number of songs, add that value to the album’s dictionary. Make at least
# one new function call that includes the number of songs on an album.

def make_album(artist_name, artist_title, song_num=""):
    album = {artist_name: artist_title}
    if song_num:
        album["Number of Songs"] = song_num
    return album


album_euphoria_ost = make_album("Labrinth", "Euphoria OST")
print(album_euphoria_ost)

album_the_slow_rush = make_album("Tame Impala", "The Slow Rush", 12)
print(album_the_slow_rush)

album_dawn_fm = make_album("The Weeknd", "Dawn FM", 16)
print(album_dawn_fm)
