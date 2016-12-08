#    ______                                           ___         
#   / ____/___ ___  __  ______  ____ __________ _____/ (_)_______ 
#  / __/ / __ `__ \/ / / / __ \/ __ `/ ___/ __ `/ __  / / ___/ _ \
# / /___/ / / / / / /_/ / /_/ / /_/ / /  / /_/ / /_/ / (__  )  __/
#/_____/_/ /_/ /_/\__,_/ .___/\__,_/_/   \__,_/\__,_/_/____/\___/ 
#                     /_/                                         
#   _____                                
#  / ___/______________ _____  ___  _____
#  \__ \/ ___/ ___/ __ `/ __ \/ _ \/ ___/
# ___/ / /__/ /  / /_/ / /_/ /  __/ /    
#/____/\___/_/   \__,_/ .___/\___/_/     
#                    /_/                 
# 

#!/usr/bin/python

from bs4 import BeautifulSoup
import sys, re, urllib2


def get_html(url):
	"""Grab html code of a page given its URL"""
	try:
		usock = urllib2.urlopen(url)
		html = usock.read()
		usock.close()
		return html
	except:
		return "error"

def get_html_cap(url):
    """Grab html code of a page given its URL"""
    try:
    	opener = urllib2.build_opener()
    	opener.addheaders.append(('Cookie', 'downloadcaptcha=1'))
        usock = opener.open(url)
        html = usock.read()
        usock.close()
        return html
    except:
        return "error"


def make_soup(html_file):
	soup = BeautifulSoup(html_file, "html.parser")
	return soup

def get_name(i, table): 
	return soup.find('table')

# def get_link1(i, table):


# def get_link2(i, table):

class Console:
	def __init__(self):
		self.name = ''
		self.link = ''



class ROM:
	def __init__(self):
		self.sys = ''
		self.name = ''
		self.link1 = ''
		self.link2 = ''


def main():
	dirs = {'gbc':'http://www.emuparadise.me/Nintendo_Game_Boy_Color_ROMs/11',\
		'sega32x': "http://www.emuparadise.me/Sega_32X_ROMs/61",\
		'genesis': "http://www.emuparadise.me/Sega_Genesis_-_Sega_Megadrive_ROMs/6",\
		'segacd': "http://www.emuparadise.me/Sega_CD_ISOs/10",\
		'atari2600': "http://www.emuparadise.me/Atari_2600_ROMs/49",\
		'n64': "http://www.emuparadise.me/roms/n64/", \
		'atari7800': "http://www.emuparadise.me/Atari_7800_ROMs/47",\
		'gb': "http://www.emuparadise.me/Nintendo_Game_Boy_ROMs/12", \
		'psp': "http://www.emuparadise.me/PSX_on_PSP_ISOs/67", \
		'snes': "http://www.emuparadise.me/Super_Nintendo_Entertainment_System_(SNES)_ROMs/5", \
		'atarilynx': "http://www.emuparadise.me/Atari_Lynx_ROMs/28",\
		'gba': "http://www.emuparadise.me/Nintendo_Gameboy_Advance_ROMs/31", \
		'nes': "http://www.emuparadise.me/Nintendo_Entertainment_System_ROMs/13", \
		'psx': "http://www.emuparadise.me/roms/psx/"}


	emu = "http://www.emuparadise.me"


	gb_soup = BeautifulSoup(get_html("http://www.emuparadise.me/Nintendo_Game_Boy_ROMs/12"), "html.parser")
	gb_table = gb_soup.find('table')
	gb_list = []

	sys_soup = []
	game_list = []

	i = 0

	for k, v in dirs.iteritems():
		soup = BeautifulSoup(get_html(v), "html.parser")
		table = soup.find('table')
		if table != None:
			for x in table:
				game_list.append(ROM())
			 	game_list[i].sys = k
				game_list[i].name = x.contents[0].contents[0].contents[0]
				game_list[i].link1 = emu + x.contents[0].contents[0]['href'] + '-download'
			 # 	print('Sys: ')
				# print(game_list[i].sys)
				# print('Name: ')
				# print(game_list[i].name)
				# print('Link: ')
				# print(game_list[i].link1)
				# print('')
				i+=1
			print("done with" + str(i))


	i = 0
	for x in game_list:
		soup = BeautifulSoup(get_html_cap(x.link1), "html.parser")
		link = soup.find_all(id="download-link")
		if len(link) > 0:
			x.link2 = emu + link[0]['href']
		print ("got link" + str(i))
		i+=1




	try: 
		out = open('out.txt', 'w')
	except IOError: 
		print "cannot open file" "out"

	out.write("index\tsystem\ttitle\turl\n")

	i = 1
	for x in game_list:
		out.write(str(i) + '\t' + x.sys + '\t' + x.name + '\t' + x.link2 + '\n')
		i+=1

	out.close()















		#print soup1.prettify()
		# for b in a[0].children:
		# 	print str(z) + "QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ"
		#  	print(b)
		#  	z+=1

		#print (soup.prettify())

	# for x in dirs:
	# 	print x



	# for i in range(0,10): # Get most downloaded ROMS
	# 	gb_list.append(ROM())
	# 	gb_list[i].sys = 'gb'
	# 	if i < 10:
	# 		gb_list[i].name = table.contents[i].contents[0].contents[0].contents[0]
	# 		gb_list[i].link1 = emu + table.contents[i].contents[0].contents[0]['href']
	# 	if i >= 10:
	# 		gb_list[i].name = table.contents[i].contents[0].contents[0].contents[0]
	# 		gb_list[i].link1 = emu + table.contents[i].contents[0].contents[0]['href']


	# 	print('Sys: ')
	# 	print(gb_list[i].sys)
	# 	print('Name: ')
	# 	print(gb_list[i].name)
	# 	print('Link: ')
	# 	print(gb_list[i].link1)
	# 	print('')



	# one = ROM()
	# one.sys = 'gb'
	# one.name = table.contents[0].contents[0].contents[0].contents[0]
	# one.link1 = emu + table.contents[0].contents[0].contents[0]['href']
	# # print('GAMEGAMEGAME')
	# # print(table.contents[0].contents[0].contents[0]['href'])
	# # print("")

	# print('Sys: ')
	# print(one.sys)
	# print('Name: ')
	# print(one.name)
	# print('Link: ')
	# print(one.link1)



main()


