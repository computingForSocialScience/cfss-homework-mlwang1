import csv
import sys
import matplotlib.pyplot as plt

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)


### enter your code below

def get_avg_latlng():
	data = readCSV('permits.csv')
	num_obs = len(data)-1
	total_lat = 0.0
	total_lon = 0.0
	for i in range(1,num_obs):
		if data[i][128] != "" and data[i][129] != "":
			total_lat += float(data[i][128])
			total_lon += float(data[i][129])
	print "Avg latitude: " + str(total_lat/num_obs)
	print "Avg longitude: " + str(total_lon/num_obs)

def zip_code_barchart():
	data = readCSV('permits.csv')
	zipcodes = []
	for i in range(1,len(data)-1):
		zipcode = data[i][28]
		if zipcode is not "":
			if len(zipcode) >= 5 and zipcode[4] == "-":
				zc = zipcode[:4]+zipcode[5:6]
				zipcodes.append(int(zc))
			elif len(zipcode) > 5:
				zipcodes.append(int(zipcode[:5]))
			elif len(zipcode) == 5 and zipcode[4] != "-":
				zipcodes.append(int(data[i][28]))
	plt.suptitle("Contractor Zip Codes")
	plt.ylim((0,10))
	plt.xlabel("Zip Code")
	plt.ylabel("Frequency")
	plt.hist(zipcodes, bins=10, range=(0000,9000))
	plt.savefig('barchart.jpg')

if sys.argv[1] == 'latlong':
	get_avg_latlng()
if sys.argv[1] == 'hist':
	zip_code_barchart()
