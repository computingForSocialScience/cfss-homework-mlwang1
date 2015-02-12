import unicodecsv as csv
import matplotlib.pyplot as plt

def getBarChartData():
    #opens both files
    f_artists = open('artists.csv') 
    f_albums = open('albums.csv')
    #creates csv reader
    artists_rows = csv.reader(f_artists)
    albums_rows = csv.reader(f_albums)
    #reads in the first row (header)
    artists_header = artists_rows.next()
    albums_header = albums_rows.next()

    artist_names = []
    
    decades = range(1900,2020, 10)
    decade_dict = {}
    for decade in decades: #initializes each decade key to equal 0
        decade_dict[decade] = 0
    
    for artist_row in artists_rows:
        if not artist_row:
            continue
        artist_id,name,followers, popularity = artist_row
        #adds artist name to list of artist names
        artist_names.append(name)

    for album_row  in albums_rows:
        if not album_row:
            continue
        artist_id, album_id, album_name, year, popularity = album_row
        for decade in decades:
            #if the year is within the decade, increment the count of the decade
            if (int(year) >= int(decade)) and (int(year) < (int(decade) + 10)):
                decade_dict[decade] += 1
                break

    x_values = decades
    y_values = [decade_dict[d] for d in decades]
    #returns decades, counts for decades, and list of artist names
    return x_values, y_values, artist_names

def plotBarChart():
    x_vals, y_vals, artist_names = getBarChartData()
    
    fig , ax = plt.subplots(1,1)
    ax.bar(x_vals, y_vals, width=10) #plot decades and counts for decades
    ax.set_xlabel('decades')
    ax.set_ylabel('number of albums')
    ax.set_title('Totals for ' + ', '.join(artist_names))
    plt.show()

