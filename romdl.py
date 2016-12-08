import urllib, urllib2
import zipfile
import requests
import StringIO
import cookielib
import os
import csv

systems = ['gbc', 'sega32x', 'genesis', 'segacd', 'atari2600', 'n64', 'atari7800', 'gb', 'psp', \
			'snes', 'atarilynx', 'gba', 'nes', 'psx']
def printAvailableGames(file):

	with open(file, 'rb') as f:
		reader = csv.reader(f, delimiter="\t")
		j = 0
		for syst in systems:
			print str(j) +": "+ syst
			j+=1
		system = raw_input("Select a system\n")
		i = 0
		for row in reader:
			if row[1] == systems[int(system)] and i < 4:
				print row[0]+": " + row[2]
				i+=1

		index = raw_input("Give me a game index to download. Enter 'n' to scroll down.\n")
		f.close()
		#print index, "this is the index"
	with open(file, 'rb') as f:
		reader = csv.reader(f, delimiter="\t")
		i = 0
		if(index == 'n'):
			
			for row in reader:
				if row[1] == systems[int(system)] and i >4:
					print row[0]+": " + row[2]
				i+=1
		index = raw_input("Give me a game index to download.\n")

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
				return row
		

def dlUnzipper(row, dest):
	#print row[3]
	opener = urllib2.build_opener()
	opener.addheaders.append(('Cookie', 'refexception=1'))
	opener.addheaders.append(('Cookie', 'downloadcaptcha=1'))
	download = row[3] 
	request = opener.open( download )
	#save
	#output = open("intasll.zip", "w")
	name = str(row[2])+".zip"
	output = open(name, "w")
	output.write(request.read())
	output.close()

	z = zipfile.ZipFile(name)
	z.extractall(dest)
	z.close()
	os.remove(name)

def downloadAll(file, dest):
	with open(file, 'rb') as f:
		reader = csv.reader(f, delimiter="\t")
		i = 0
		for row in reader:
			if i == 0:
				i+=1
				continue
			dlUnzipper(row, dest+row[1])

index = printAvailableGames("games.txt")
gamer = scannerThing("games.txt", int(index))
destination = "/home/pi/RetroPie/roms/"+gamer[1]
#destination = "roms/"+gamer[1]
dlUnzipper(gamer, destination)
#downloadAll("games.txt", "roms/")
print gamer[2]+" Was Downloaded Successfully!"


