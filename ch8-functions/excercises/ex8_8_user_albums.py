# Start with your program from Exercise 8-7. Write a while
# loop that allows users to enter an album’s artist and title. Once you have that
# information, call make_album() with the user’s input and print the dictionary
# that’s created. Be sure to include a quit value in the while loop.

from ex_8_7_album import make_album

albums = []

print("Lets make a list of your favorites music albums!")
print("When you have entered all of them enter quit to exit")

while True:
    artist = input("Enter the name of the artist: ")
    if artist == "quit":
        break

    album = input("Enter the name of the album: ")
    if album == 'quit':
        break

    albums.append(make_album(artist, album))

print("Your favorites albums are:")
for i in range(len(albums)):
    artist = list(albums[i].keys())[0]
    album_name = albums[i][artist]
    print(f"{i + 1}. {album_name} by {artist}")
