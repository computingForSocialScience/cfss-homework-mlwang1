import sys
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *
import random
import requests
import pandas as pd

if __name__ == "__main__":
	an = sys.argv[1:]
	artist_names = []
	for name in an:
		name = fetchArtistId(name)
		artist_names.append(name)
	edgelists = getEdgeList(artist_names.pop(),2)
	for artists in artist_names:
		if getRelatedArtists(artists) == []:
			continue
		e2 = getEdgeList(artists,2)
		edgelists = combineEdgeLists(edgelists, e2)
	g = pandasToNetworkX(edgelists)
	art_list = []
	for i in range(30):
		r = randomCentralNode(g)
		art_list.append(r)
	data = []
	for a in art_list:
		name = fetchArtistInfo(a)['name'] #correct id but url not working
		if name == 0:
			continue
		album = random.choice(fetchAlbumIds(a))
		url = 'http://api.spotify.com/v1/albums/'+album+'/tracks'
		req = requests.get(url)
		src = req.json()
		song = random.choice(src['items'])['name']
		alb_name = fetchAlbumInfo(album)['name']
		data.append((name, alb_name, song))
		if len(data) == 30:
			break
	print data
	pd.DataFrame(data).to_csv('playlist.csv', index=False, encoding='utf-8')
			
