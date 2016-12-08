import urllib, urllib2
import zipfile
import requests
import StringIO
import cookielib
import os
import pandas as pd
import csv


def printAvailableGames(file):
	df = pd.read_csv(file, "\t")
	i = 1
	for name in df["title"]:
		print str(i)+": " + name
		i+=1
	index = raw_input("Give me a game index to download\n")
	print index
	return index

def scannerThing(file, index):	
	with open(file, 'rb') as f:
		reader = csv.reader(f, delimiter="\t")
		i = 0

		for row in reader:
			if i == 0:
				i+=1
				continue
			
			if(int(row[0]) == index):
				
				#print row
				return row
		

def dlUnzipper(url, dest):
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie', 'refexception=1'))
	opener.addheaders.append(('Cookie', 'downloadcaptcha=1'))
	download = url 
	request = opener.open( download )

	#save
	output = open("install.zip", "w")
	output.write(request.read())
	output.close()

	z = zipfile.ZipFile("install.zip")
	z.extractall(dest)
	z.close()
	os.remove("install.zip")

index = printAvailableGames("out.txt")
gamer = scannerThing("out.txt", int(index))
destination = "/home/pi/RetroPie/roms/"+gamer[1]
dlUnzipper(gamer[3], destination)



