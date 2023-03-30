def make_album(artist, title):
    album = {'artist': artist, 'title': title}
    return album

while True:
    print("\nPlease enter the album details:")
    print("Enter (q) at any time to quit.")
    a_artist = input("Enter the album artist name: ")
    if a_artist == 'q':
        break
    a_album = input("Enter the album name: ")
    if a_album == 'q':
        break
    album = make_album(artist = a_artist, title = a_album)
    
    print("\nAlbum Information")
    for name, title in album.items():
        print(f"{name.title()}: {title.title()}")
