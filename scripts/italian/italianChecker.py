import os

def readFile(file):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    f = open(os.path.join(location, file), "r")
    return set([x.lower() for x in set(f.read().splitlines())])

words = readFile("italianwords.txt")
suffixes = readFile("italiansuffixes.txt")


def isItalianWord(word):
    return word in words


def isPseudoItalianWord(word):
	for suffix in suffixes:
		for gender in ['a', 'o', 'i', 'e']:
			if word.endswith(suffix[:-1] + gender):
				return True;
