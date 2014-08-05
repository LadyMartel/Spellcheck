#Spellcheck

This program spellchecks an english word and gives a suggestion of the correctly spelled word. It uses the large list of english words from the unix system (/usr/share/dict/words). Run the program by typing the following:

	python spellcheck.py
	
Onscreen instructions will be outputted. 

###Suggestion will correct for the following cases:

-	wrong case:
	- 	""wRONg" --> "wrong"	
-	repeating letters:
	-	"wrrrrong"--> "wrong"
-	vowel swaps:
	-	"reght" --> "right"

###Terribly misspelled words

The program will not be able to suggest a word in the following case where words are misspelled beyond recognition. (Outside of the above rules)

-	"dasdf" --> "NO SUGGESTION"

### Testing

Typying "RAND" as an input will let you test the spellchecker with any number of automatically generated, wrongly spelled, words. 