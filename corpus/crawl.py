#!/usr/bin/env python3

from lxml import etree
import urllib.request
import os

def getSite(link):
	try:			
		site = etree.parse(link, parser = etree.HTMLParser())
		return site			
	except OSError:
		return None	


def getCategory(catname, pages):
	text = ""
	file = open(catname+".xml", 'w', encoding='utf-8')
	print(catname)
	
	for n in range(1, pages+1):
		if (n%100 == 0):
			backup = open(catname +"_backup.xml", 'w', encoding='utf-8')
			backup.write(text)
			backup.close()

		print('site ' + str(n))
		site = getSite("http://www.supermarktcheck.de/%s/produkte/page:%s" %(catname,n))
				
		for ul in site.iter('ul'):
			if (ul.attrib.has_key('class')) and (ul.attrib['class'] == "productList"):
				for li in ul.iter('li'):
					name = li.find('a').text 				
					price = etree.tostring(li, encoding = 'unicode')	
					price = price[price.find('Preis von ')+10 : price.find('€') - 1]
					if (len(price) < 7):
						element = "<product name='"+ str(name) +"' price='" + str(price) + "' />\n"
					else:
						element = "<product name='"+ str(name) +"' />\n"
					text += element					
	file.write(text)
	file.close()							


getCategory('fruechte-gemuese', 41)		 	
getCategory('fleisch-wurst-aufschnitt', 391)
getCategory('konserven', 392)
getCategory('molkereiprodukte', 612)
getCategory('kaffee', 91)
getCategory('brotaufstriche', 131)
getCategory('essig-und-oele', 70)
getCategory('teigwaren', 123)
getCategory('reis', 32)
getCategory('eis', 86)
getCategory('pizza-tiefkuehl', 39)
getCategory('suesswaren-knabberartikel', 618)	
