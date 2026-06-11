def make_album(artist, album_name, tracks=None):
    album = {'artist': artist, 'name': album_name}
    if tracks:
        album['tracks'] = tracks
    return album

new_album = make_album('craig david', 'born to do it')
print(new_album)
new_album = make_album('sam smith', 'in the lonely hour')
print(new_album)
new_album = make_album('onerepublic', 'native', 13)
print(new_album)

while True:
    print("\nProszę podać artystę i tytuł albumu:")
    print("(wpisz 'q', aby zakończyć pracę programu w dowolnym momencie)")
    artist_name = input("Artysta: ")
    if artist_name == 'q':
        break
    album_name = input("Tytuł albumu: ")
    if album_name == 'q':
        break

    new_album = make_album(artist_name, album_name)
    print(new_album)