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

paramslist = []
firstItem = ""

headers= {'User-Agent': 'Mozilla/5.0'}

#print("Started \n") #-------debug

eel.init('web')

@eel.expose
def skelbiu(link, pages, notif):
	global firstItem
	yeet1 = 0
	itemnum = 0
	splitlink = link.split("/")

	eel.CleanTable()

	for page in range(int(pages)):

		rlpage = page+1

		if len(splitlink) == 5:
			rlink = splitlink[0] +"/"+ splitlink[1] +"/"+ splitlink[2] +"/"+ splitlink[3] + "/" + str(rlpage) + splitlink[4]
		else:
			rlink = splitlink[0] +"/"+ splitlink[1] +"/" + str(rlpage) + splitlink[2]


		source = requests.get(rlink, headers=headers).text
		soup = BeautifulSoup(source, "lxml")
		body = soup.find('body')

		adverts = body.findAll('li', class_='simpleAds')

		for advert in adverts:
			try:

				content = advert.find('div', class_='itemReview')

				pricediv = content.find('div', class_='adsPrice')
				price = pricediv.find('span').text

				name = content.find('a', class_='js-cfuser-link')
				url = 'https://www.skelbiu.lt/' + name['href']
				rlname = " ".join(name.text.split())

				date = advert.find('div', class_="adsDate").text
				city = advert.find('div', class_="adsCity").text

				description = content.find('div', class_="adsTextReview").text
				rldescription = " ".join(description.split())

				condition = content.find('div', class_="adsTextMoreDetails").text
				rlcondition = " ".join(condition.split())

				eel.UpdateTableSkelbiu(url, price + " | ", date + " | ", city + " | ", condition + " | ", rlname, " | " + description, itemnum)
				# print(price + " | " + rlname + " | " + city + " | " + date + " | " + rlcondition) ---- debug

				itemnum += 1
			except:
				pass
		
			if yeet1 == 0:
				# print("fist =", firstItem, "rname =", rname) #-------debug
				if firstItem == "":
					firstItem = rlname
				if notif == True:
					if firstItem != rlname:
						print('new')
						try:
							playsound('sound.mp3')
						except:
							try:
								playsound('sound.wav')
							except:
								pass
				firstItem = rlname
			yeet1 += 1

@eel.expose
def autoplius(link, pages, notif):
	global firstItem
	eel.CleanTable()
	yeet1 = 0
	itemnum = 0
	for page in range(int(pages)):
		rlpage = page+1

		if(link.find('page_nr') != -1):
			rlink = link.replace(link[-1], str(rlpage))
		else:
			rlink = " ".join((link, '&page_nr=' + str(rlpage)))

		source = requests.get(rlink).text
		soup = BeautifulSoup(source, "lxml")
		body = soup.find('body')

		adverts = body.findAll('a', class_='item-thumb js-announcement-list-item')
		announcments = body.findAll('a', class_='announcement-item')

		if(adverts != []):
			for advert in adverts:
				try:
					paramslist = []

					url = advert['href']

					price = advert.find('strong').text
					rlprice = " ".join(price.split())

					year = advert.find('div', class_='title-year').text
					rlyear = " ".join(year.split())

					title = advert.find('div', class_='line1').text
					rltitle = " ".join(title.split())

					params = advert.findAll('span')
					for param in params:
						rlparam = " ".join(param.text.split())
						paramslist.append(rlparam)

					parameters = str(paramslist)[0:-1].replace("'", '').replace(",", " |").replace("[", "")

					eel.UpdateTableAutoplius(url, rlprice + " | ", rlyear + " | ", rltitle, parameters, itemnum)
					#print(rlprice,"|",rlyear,"|",rltitle, parameters, url) -- debug
					itemnum += 1
				except:
					pass

		else:
			#print('announcment:', announcments) -- debug
			for announcment in announcments:
				try:
					paramslist = []

					url = announcment['href']

					price = announcment.find('strong').text
					rlprice = " ".join(price.split())

					year = announcment.find('span', title='Pagaminimo data').text
					rlyear = " ".join(year.split())

					title = announcment.find('div', class_='announcement-title').text
					rltitle = " ".join(title.split())

					params = announcment.findAll('span')
					for param in params:
						rlparam = " ".join(param.text.split())
						paramslist.append(rlparam)

					parameters = str(paramslist)[0:-1].replace("'", '').replace(",", " |").replace("[", "")

					eel.UpdateTableAutoplius(url, rlprice + " | ", rlyear + " | ", rltitle, " | " + parameters, itemnum)
					#print(rlprice,"|",rlyear,"|",rltitle, parameters, url) -- debug
					itemnum += 1
				except:
					pass

		if yeet1 == 0:
			# print("fist =", firstItem, "rname =", rname) #-------debug
			if firstItem == "":
				firstItem = rltitle
			if notif == True:
				if firstItem != rltitle:
					# print('new') -- debug
					try:
						playsound('sound.mp3')
					except:
						try:
							playsound('sound.wav')
						except:
							pass
			firstItem = rltitle
		yeet1 += 1


eel.start('index.html', size=(1980, 1080), position=(0, 0))
