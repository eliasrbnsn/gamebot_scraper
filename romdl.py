#!/usr/bin/python
import urllib, urllib2
import zipfile
import requests
import StringIO
import cookielib
import os
import csv
import figlet

systems = ['gbc', 'sega32x', 'genesis', 'segacd', 'atari2600', 'n64', 'atari7800', 'gb', 'psp', \
			'snes', 'atarilynx', 'gba', 'nes', 'psx']
def printAvailableGames(file):

	with open(file, 'rb') as f:
		reader = csv.reader(f, delimiter="\t")
		row_count = sum(1 for row in f)
		j = 0
		for syst in systems:
			print str(j) +": "+ syst
			j+=1
		print (str(j) + ": Show All")
		system = raw_input("Select a system\n")
		rows, columns = os.popen('stty size', 'r').read().split()
		i = 0
		#currSystem = 0
		return showAll(file, int(rows), int(columns), int(row_count), int(system))

	
def showAll(file, rows, cols, total, system):
	currRow = 0
	while(currRow < total):	
		skip = showX(file, rows, currRow, system)
		temp = raw_input("Give me a game index to download. Enter 'n' to go to next page or 'p' to go to previous page")
		if temp == 'n':
			if (currRow+rows) < total:
				currRow += rows
				currRow -= skip
		elif temp == 'p':
			if(currRow >= (rows-skip)):
				currRow -= (rows-skip)
		else: 
			return temp

def showX(file, rows, start, system):
	with open(file, 'rb') as f:
		reader = csv.reader(f, delimiter="\t")
		firstTime = 0
		i = 0
		skip = 2
		if(system == 14):
			currSystem = 0
			for row in reader:
				if i < start:
					i+=1
					continue
				elif i >= start and i < start + rows-2:
					if currSystem != row[1]:
						printfiglets(row[1])
						currSystem = row[1]
						i+=5
						skip += 5
					print row[0] +": " + row[2]
					i+=1
		else:
			for row in reader:
				if i < start:
					i += 1
					continue
				elif row[1] == systems[int(system)] and i >= start and i < rows:
					print row[0]+": " + row[2]
					i+=1
		return skip
def printfiglets(system):
	if system == "gbc":
		figlet.gbc()
	elif system == "sega32x":
		figlet.sega32x()
	elif system == "genesis":
		figlet.genesis()
	elif system == "segacd":
		figlet.segacd()
	elif system == "atari2600":
		figlet.atari2600()
	elif system == "n64":
		figlet.n64()
	elif system == "atari7800":
		figlet.atari7800()
	elif system == "gb":
		figlet.gb()
	elif system == "psp":
		figlet.psp()
	elif system == "snes":
		figlet.snes()
	elif system == "atarilynx":
		figlet.atarilynx()
	elif system == "gba":
		figlet.gba()
	elif system == "nes":
		figlet.nes()
	elif system == "psx":
		figlet.psx()
	else:
		figlet.system()

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

index = printAvailableGames("games")
gamer = scannerThing("games", int(index))
destination = "/home/pi/RetroPie/roms/"+gamer[1]
#destination = "roms/"+gamer[1]
dlUnzipper(gamer, destination)
#downloadAll("games.txt", "roms/")
print gamer[2]+" Was Downloaded Successfully!"


