import sys
from io import open
import requests as requests
import csv
import pandas as pd

def getRelatedArtists(artistID):
	url = 'https://api.spotify.com/v1/artists/'+artistID+'/related-artists'
	req = requests.get(url)
	src = req.json()
	ids = []
	if src.has_key('artists') == False:
		return ids
	#print src
	for i in src['artists']:
		ids.append(i['id'])
	return ids

def getDepthEdges(artistID, depth):
	related = getDepthRecurse(artistID, depth, [])
	return related
def getDepthRecurse(artistID, depth, biglist):
	if depth == 0:
		return biglist 
	else:
		#print artistID
		currentlist = getRelatedArtists(artistID)
		for id1 in currentlist:
			pair = (artistID, id1)
			if pair not in biglist:
				biglist.append(pair)	
			if depth-1 > 0:
				getDepthRecurse(id1, depth-1, biglist)
		return biglist

def getEdgeList(artistID,depth):
	return pd.DataFrame(getDepthEdges(artistID,depth))

def writeEdgeList(artistID, depth, filename):
	getEdgeList(artistID,depth).to_csv(filename, index=False, encoding='utf-8')
