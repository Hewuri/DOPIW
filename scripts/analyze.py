from italian.italianChecker import isItalianWord
from italian.italianChecker import isPseudoItalianWord
import codecs, operator
from lxml import etree

prodcount = {}
prodcount['teigwaren']= 1832
prodcount['suesswaren']=  9268
prodcount['reis']=  469
prodcount['pizza']=  571
prodcount['molkereiprodukte']=  9168
prodcount['konserven']=  5871
prodcount['kaffee']=  1362
prodcount['fruechte-gemuese']=  601
prodcount['fleisch-wurst-aufschnitt']=  5863
prodcount['essig-und-oele']=  1047
prodcount['eis']=  1280
prodcount['brotaufstriche']=  1953
prodcount['drogerie']=  12402
prodcount['backwaren']=  2009
prodcount['getränke']=  9237


parole = dict()

def analyze(xmlFile):
	xml_text = codecs.open(xmlFile, "r", "utf-8")
	xml = etree.parse(xml_text)
	
	for category in xml.iter("category"):
		for product in category.iter("product"):
			name = product.attrib["name"]
			hasItalianName(name)			
					

def hasItalianName(name):
	for word in name.split():
		word = word.lower()
		if isItalianWord(word) or isPseudoItalianWord(word):
			if word in parole:
				parole[word] += 1
			else:
				parole[word] = 1
            
def printTopWords(n):
	words_sorted = sorted(parole.items(), key=operator.itemgetter(1), reverse=True)
	print("Top " + str(n) + " words:")
	for i in range(0, n):
		pair = words_sorted[i]
		print(str(pair[1]) + " " + pair[0])
			
analyze('../corpus/products.xml')
printTopWords(100)
#analyze('../corpus/products.xml')
#print(words)
#target.write(words)
#target.close()		

