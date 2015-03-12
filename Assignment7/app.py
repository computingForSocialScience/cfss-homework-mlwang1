from flask import Flask, render_template, request, redirect, url_for
import pymysql

import sys
from artistNetworks import *
from analyzeNetworks import *
from fetchArtist import *
from fetchAlbums import *
import random
import requests
import pandas as pd

dbname="playlists"
host="localhost"
user="root"
passwd="MyNewPass"
db=pymysql.connect(db=dbname, host=host, user=user,passwd=passwd, charset='utf8')

app = Flask(__name__)

def createNewPlaylist(artistName):
    c=db.cursor()
    sql = '''CREATE TABLE IF NOT EXISTS playlists (id INTEGER PRIMARY KEY AUTO_INCREMENT,
                                                   rootArtist VARCHAR(255));'''
    c.execute(sql)
    sql = '''CREATE TABLE IF NOT EXISTS songs (playlistId INTEGER,
                                               songOrder INTEGER,
                                               artistName VARCHAR(255),
                                               albumName VARCHAR(255),
                                               trackName VARCHAR(255));'''
    c.execute(sql)
    edgelists = getEdgeList(fetchArtistId(artistName),2)
    g = pandasToNetworkX(edgelists)
    art_list = []
    for i in range(30):
        r = randomCentralNode(g)
        art_list.append(r)
    count = 0
    psql = "INSERT INTO playlists (rootArtist) VALUES ('%s');" % (artistName)
    c.execute(psql)
    idnum = c.lastrowid
    data = []
    for a in art_list:
        name = fetchArtistInfo(a)['n'] #correct id but url not working
        if name == 0:
            continue
        #sql = "INSERT INTO playlists (id, rootArtist) VALUES ('%i','%s')" % (count, name)
        #count = count+1
        try:
            album = random.choice(fetchAlbumIds(a))
        except IndexError:
            continue
        url = 'http://api.spotify.com/v1/albums/'+album+'/tracks'
        req = requests.get(url)
        src = req.json()
        song = random.choice(src['items'])['name']
        alb_name = fetchAlbumInfo(album)['name']
        data.append((idnum, count, name, alb_name, song))
        print (name, alb_name, song)
        #ssql = '''INSERT INTO songs (playlistId, songOrder, artistName, albumName, trackName) 
        #          VALUES (%s, %s, %s, %s, %s);''' % (c.lastrowid, count, name, alb_name, song)
        count = count+1
        #if count == 30:
        #    break
        #c.execute(ssql)
    c.executemany('''INSERT INTO songs (playlistId, songOrder, artistName, albumName, trackName) VALUES (%s, %s, %s, %s, %s);''', data)
    print len(data)
    db.commit()
    #c.close()
    #db.close()
    #pd.DataFrame(data).to_csv('playlist.csv', index=False, encoding='utf-8')


@app.route('/')
def make_index_resp():
    # this function just renders templates/index.html when
    # someone goes to http://127.0.0.1:5000/
    return(render_template('index.html'))


@app.route('/playlists/')
def make_playlists_resp():
    c = db.cursor()
    c.execute('SELECT * FROM playlists;')
    playlists = c.fetchall()
    #c.close()
    return render_template('playlists.html',playlists=playlists)


@app.route('/playlist/<playlistId>')
def make_playlist_resp(playlistId):
    c = db.cursor()
    c.execute('SELECT songOrder, artistName, albumName, trackName FROM songs WHERE playlistId = %s ORDER BY songOrder;', playlistId)
    songs = c.fetchall()
    #c.close()
    return render_template('playlist.html',songs=songs)


@app.route('/addPlaylist/',methods=['GET','POST'])
def add_playlist():
    if request.method == 'GET':
        # This code executes when someone visits the page.
        return(render_template('addPlaylist.html'))
    elif request.method == 'POST':
        # this code executes when someone fills out the form
        artistName = request.form['artistName']
        createNewPlaylist(artistName)
        return(redirect("/playlists/"))



if __name__ == '__main__':
    app.debug=True
    app.run()