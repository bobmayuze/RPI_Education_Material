# Author: Yuze Bob Ma
# Date: Oct, 7th, 2016
# This code is written for RPI_CSCI_1100 HW4 Part 1

# Import modules
import sys


# define functions 
def is_alternating(word):
	word_test = word.lower()
	length = len(word)
	word_l = list(word_test)
	vowels = ['a', 'e', 'i', 'o', 'u']

	# test the length
	if length < 8:
		print('The word \'{}\' is not alternating'.format(word))
		sys.exit()
	# test if the word starts with an vowel	
	if word_l[0] not in vowels:
		print('The word \'{}\' is not alternating'.format(word))
		sys.exit()
	# test if has alternating consonants and vowels
	i = 0
	for charater in range(length-1):
		if word_l[i] not in vowels:
			print('The word \'{}\' is not alternating'.format(word))
			sys.exit()
		i += 1
		if word_l[i] in vowels:
			print('The word \'{}\' is not alternating'.format(word))
			sys.exit()
		i += 1
		if length % 2 == 0:
			if i > length-1:
				break
		else:
			if i > length-2:
				break
	# test if the consonants are increasing
	i = 1
	for charater in range(length-1):
		if not word_l[i] < word_l[i+2]:
			print('The word \'{}\' is not alternating'.format(word))
			sys.exit()
		i += 2
		if length % 2 == 0:
			if i > length-2:
				break
		else:
			if i > length-4:
				break

	print('The word \'{}\' is alternating'.format(word))

# main code
word = input('Enter a word => ')
print(word)
is_alternating(word)