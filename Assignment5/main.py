import sys
from fetchArtist import fetchArtistId, fetchArtistInfo
from fetchAlbums import fetchAlbumIds, fetchAlbumInfo
from csvUtils import writeArtistsTable, writeAlbumsTable
from barChart import plotBarChart

if __name__ == '__main__':
    artist_names = sys.argv[1:]
    artists_ids = []
    artist_info = []
    print "input artists are ", artist_names
    for n in artist_names:
    	id = fetchArtistId(n)
    	artists_ids.append(id)
    	artist_info.append(fetchArtistInfo(id))

    album_info = []
    for ids in artists_ids:
    	album_id = fetchAlbumIds(ids)
    	for alb in album_id:
    		album_info.append(fetchAlbumInfo(alb))
    writeArtistsTable(artist_info)
    writeAlbumsTable(album_info)
    plotBarChart()


    

