# This is where the answers to Chapter 8 questions for the BSS Dev RampUp go
# Name: Amaka Atoyebi

#8.12
def rotate_word(string, integer):
	letters = string.split()
	for letters in string:
		letterToNum = ord(letters) + integer
		numToLetter = chr(letterToNum)
		print numToLetter

rotate_word('America', 13)	 