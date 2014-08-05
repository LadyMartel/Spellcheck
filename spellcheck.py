import sys 
from random import randint,uniform

''' Runtime analysis:
The average runtime for finding a suggestion for a word is O(m), 
where m is the number of characters in the word. For each node,
the lookup for the next node is amortized O(1) because the trie
is represented as a dictionary. For each of the characters in 
a word, we only branch out a constant amount of times. 
'''

vowels = ['a','e','i','o','u','A','E','I','O','U']

f = open("/usr/share/dict/words", 'r')
read_data = f.read() 
dictionary = read_data.split('\n')

def wordgenerator():
	# assuming entire dictionary file can fit into memory
	random_word = dictionary[randint(0,len(dictionary)-1)]
	wl = []
	# generate vowel change
	for c in random_word:
		r_vowel = uniform(0,1)
		r_case = uniform(0,1)
		r_repeat = uniform(0,1)

		if r_vowel < 0.8 and c in vowels:
			wl.append(vowels[randint(0,9)])
		if r_repeat < 0.8 :
			for i in range(randint(0,5)):
				wl.append(rand_chap(c))
		wl.append(c)
	return ''.join(wl)

def rand_chap(ch):
	r = uniform(0,1)
	if r < 0.5:
		if ch.isupper():
			return ch.lower()
		else:
			return ch.upper()
	return ch


# each level contains a tuple of a list and dictionary
# the list contains the characters of the word so far
class spellcheck_trie():
	def __init__(self):
		self.t = ([], {})
		self.parse_dictionary()

	def parse_dictionary(self):
		print "parsing dictionary. . . "
		for w in dictionary:
			self.add_word(w.strip()) 

	def add_word(self, word):
		cur = self.t
		for c in word:
			(chars_list, remaining_dict) = cur
			if not c in remaining_dict:
				nl = list(chars_list)
				nl.append(c)
				cur = remaining_dict.setdefault(c, (nl, {}))
			else:
				cur = remaining_dict[c]
		(chars_list , remaining_dict) = cur
		if not '.' in remaining_dict:
			nl = list(chars_list)
			cur = remaining_dict.setdefault('.', (nl, '.'))

	def get_suggestion(self, word):
		cur = self.t
		s = self.traverse(list(word), cur)
		if not s:
			return "NO SUGGESTION"
		return s

	def traverse(self, wl, cur):
		(chars_list, remaining_dict) = cur
		if len(wl) == 0 and '.' in remaining_dict:
			return "".join(chars_list)
		elif (len(wl) > 0 and remaining_dict == '.') or (len(wl) == 0 and remaining_dict != '.'):
			return None
		else:
			ch = wl.pop(0)
			tocheck = []
			# check this character
			tocheck.append(ch)

			# check its opposite case
			if ch.isupper():
				tocheck.append(ch.lower())
			else:
				tocheck.append(ch.upper())
			
			# possible vowels with upper/lower
			if ch in vowels:
				tocheck.extend(vowels)

			for c in tocheck:
				if c in remaining_dict: 
					s = self.traverse(list(wl),remaining_dict[c])
					if s:
						return s

			if len(chars_list) > 0 and ch.lower() == chars_list[len(chars_list) - 1].lower():
				s = self.traverse(list(wl), cur)
				if s:
					return s
		return None


if __name__ == "__main__":
	sc = spellcheck_trie()

	print "enter word below:"
	print "press ':q' to exit"
	print "type RAND to randomly generate many misspelled words."
	while True:
		word_input = raw_input("> ")
		if( word_input == ':q'):
			break
		if word_input == 'RAND':
			num = raw_input("please enter the number of words to generate: ")
			while True:
				try:
					num = int(num)
					break
				except:
					num = raw_input("please enter an int: ")
			for i in range(num):
				w = wordgenerator()
				ret = sc.get_suggestion(w)
				print "word: " + w + "suggestion: " + ret
				assert(ret != 'NO SUGGESTION'), "word %s failed" % ret
			print "all generated words had suggestions."
		else:
			print sc.get_suggestion(word_input.strip())
	print "bye bye"


 	