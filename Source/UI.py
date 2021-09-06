#Made By Ignas Mikolaitis
#ignuxas.com

import eel
import time
import requests
from bs4 import BeautifulSoup
import re
import os
from playsound import playsound

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
cls()

itemnum = 0
requested = 0
firstItem = ""

headers= {'User-Agent': 'Mozilla/5.0'}

#print("Started \n") #-------debug

eel.init('web')

@eel.expose
def searchpy(link, pages, notif):
	global firstItem
	splitlink = link.split("/")
	skipped = 0
	yeet1=0
	page = 1

	eel.CleanTable()
	for i in range(0, int(pages)):

		if len(splitlink) == 5:
			rlink = splitlink[0] +"/"+ splitlink[1] +"/"+ splitlink[2] +"/"+ splitlink[3] + "/" + str(page) + splitlink[4]
		else:
			rlink = splitlink[0] +"/"+ splitlink[1] +"/" + str(page) + splitlink[2]

		global itemnum

		source = requests.get(rlink, headers=headers).text
		soup = BeautifulSoup(source, "lxml")
		body = soup.find('body')
		content = body.findAll('li', class_=True, id=True)
		prices = body.findAll('div', class_="adsPrice")
		date = body.findAll('div', class_="adsDate")
		city = body.findAll('div', class_="adsCity")
		description = body.findAll('div', class_="adsTextReview")
		name = body.findAll('h3')
		status = body.findAll('div', class_="adsTextMoreDetails")

		for price in prices:
			try:
				rprice = prices[itemnum].find('span').text
				rname = " ".join(name[itemnum+1].text.split())
				rstatus = " ".join(status[itemnum].text.split())
				rdescription = " ".join(description[itemnum].text.split())
				#numprice = int(re.search(r'\d+', rprice.replace(" ", "")).group())
				url = content[itemnum+4].find('a', href=True)
				url = "https://www.skelbiu.lt" + url['href']
				eel.UpdateTable(str(url), rprice, " | " + date[itemnum].text + " | ", city[itemnum].text, " | " + rstatus, " | " + rname, " | " + rdescription, yeet1, skipped)
			except:
				skipped += 1
				pass
			if yeet1 == 0:
				# print("fist =", firstItem, "rname =", rname) #-------debug
				if firstItem == "":
					firstItem = rname
				if notif == True:
					if firstItem != rname:
						print('new')
						try:
							playsound('sound.mp3')
						except:
							try:
								playsound('sound.wav')
							except:
								pass
				firstItem = rname
			yeet1 += 1
			itemnum += 1

		itemnum = 0
		page += 1

eel.start('index.html', size=(1980, 1080), position=(0, 0))