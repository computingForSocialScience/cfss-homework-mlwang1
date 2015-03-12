import requests
from datetime import datetime
import sys

def fetchAlbumIds(artist_id):
    """Using the Spotify API, take an artist ID and 
    returns a list of album IDs in a list
    """
    url = 'https://api.spotify.com/v1/artists/'+artist_id+'/albums?market=US&album_type=album'
    req = requests.get(url)
    src = req.json()
    ids = []
    for i in src['items']:
    	ids.append(i['id'])
    return ids

def fetchAlbumInfo(album_id):
    """Using the Spotify API, take an album ID 
    and return a dictionary with keys 'artist_id', 'album_id' 'name', 'year', popularity'
    """
    url = 'https://api.spotify.com/v1/albums/'+album_id
    req = requests.get(url)
    src = req.json()
    if src.has_key('error'):
        return {'name':0}
    dictionary = {}
    dictionary['artist_id'] = src['artists'][0]['id']
    dictionary['album_id'] = album_id
    dictionary['name'] = src['name']
    dictionary['year'] = src['release_date'][:4]
    dictionary['popularity'] = src['popularity']
    return dictionary