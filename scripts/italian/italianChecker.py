import os

def readFile(file):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(location, file), "r")
    return set([x.lower() for x in set(f.read().splitlines())])

words = readFile("italianwords.txt")
suffixes = readFile("italiansuffixes.txt")
stopList = readFile("stoplist.txt")
phonems = ['gh', 'gn', 'ci', 'ce']

def isItalianWord(word):
	if word in words:
		if word in stopList:
			return False
		else:
			return True
	else:
		return False

def isPseudoItalianWord(word):
	if word in stopList:
		return False
		
	for phonem in phonems:
		if phonem in word:
			return True
	for suffix in suffixes:
		for gender in ['a', 'o', 'i', 'e']:
			if word.endswith(suffix[:-1] + gender):
				return True
