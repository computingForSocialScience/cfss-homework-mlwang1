from io import open

def writeArtistsTable(artist_info_list):
    """Given a list of dictionries, each as returned from 
    fetchArtistInfo(), write a csv file 'artists.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY
    """
    f = open('artists.csv','w', encoding='utf-8')
    f.write(u'ARTIST_ID,ARTIST_NAME,ARTIST_FOLLOWERS,ARTIST_POPULARITY\n')
    for a in artist_info_list:
        string = a['id']+u',"'+a['name']+u'",'+unicode(a['followers'])+u','+unicode(a['popularity'])+u'\n'
        print string
        f.write(string)
    f.close()

def writeAlbumsTable(album_info_list):
    """
    Given list of dictionaries, each as returned
    from the function fetchAlbumInfo(), write a csv file
    'albums.csv'.

    The csv file should have a header line that looks like this:
    ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY
    """
    f = open('albums.csv','w', encoding='utf-8')
    f.write(u'ARTIST_ID,ALBUM_ID,ALBUM_NAME,ALBUM_YEAR,ALBUM_POPULARITY\n')
    for a in album_info_list:
        string = a['artist_id']+u','+a['album_id']+u',"'+a['name']+u'",'+a['year']+u','+unicode(a['popularity'])+u'\n'
        f.write(string)
    f.close()

