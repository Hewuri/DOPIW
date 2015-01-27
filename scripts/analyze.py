from italian.italianChecker import isItalianWord
from italian.italianChecker import isPseudoItalianWord

def analyze(text):
	for word in text.split():
		word = word.lower()
		if isItalianWord(word):
			print("italian " + word)
		elif isPseudoItalianWord(word):
			print("pseudo " + word)	
			

