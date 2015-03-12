import sys
import requests
import csv

def fetchArtistId(name):
    """Using the Spotify API search method, take a string that is the artist's name, 
    and return a Spotify artist ID.
    """
    url = 'https://api.spotify.com/v1/search?q='+str(name)+'&type=artist'
    req = requests.get(url)
    src = req.json()
    if len(src['artists']['items']) > 0:
        return src['artists']['items'][0]['id']
    else:
        return None

def fetchArtistInfo(artist_id):
    """Using the Spotify API, takes a string representing the id and
`   returns a dictionary including the keys 'followers', 'genres', 
    'id', 'name', and 'popularity'.
    """
    url = 'https://api.spotify.com/v1/artists/'+artist_id
    req = requests.get(url)
    src = req.json()
    dictionary = {}
    #dictionary['followers'] = src['followers']['total']
    #dictionary['genres'] = src['genres']
    #dictionary['id'] = artist_id
    dictionary['n'] = src['name']
    #dictionary['popularity'] = src['popularity']
    return dictionary