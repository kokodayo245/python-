# 8-6
def city(city_name='santiago', city_country='chile'):
    print('"' + city_name + ',' + city_country + '"')


city()


# 8-7
# def make_album(singer_name, album_name, songs=''):
#     album = {'sing': singer_name, 'album': album_name}
#     if songs:
#         album['songs'] = songs
#     return album
#
#
# album1 = make_album('周杰伦', 'Jay', '10')
# print(album1)


# 8-8
def make_album():
    while True:
        print("\nPlease enter your favorite singer and album")
        print("You can enter your favorite album's numbers of songs if you want")
        print("(enter 'q' at any time to quit)")

        singer_name = input("singer_name: ")
        if singer_name == 'q':
            break
        album_name = input("album_name: ")
        if album_name == 'q':
            break
        songs = input("songs: ")
        if songs == 'q':
            break
        flag = input("END ?")
        if flag == 'q':
            break

    album = {'sing': singer_name, 'album': album_name}
    if songs:
        album['songs'] = songs
    return album


my_album = make_album()
print(my_album)
