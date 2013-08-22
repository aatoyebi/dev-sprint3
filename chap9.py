# This is where the answers to Chapter 9 questions for the BSS Dev RampUp go
# Name: Amaka Atoyebi

#9.1
readFile = open('words.txt')
line = readFile.readline()
for line in readFile:
	if (len(line) > 20):
		word = line.strip()
		print word


#9.2

def has_no_e():
	counter = 0
	counter_all = 0
	for line in readFile:
		if 'e' in line:
			word = line.strip()
			counter += 1
			print word
		counter_all += 1
	num = counter * 100
	den = counter_all
	print num / den
	
	return True


has_no_e()


#9.3
def avoids():
	prompt = "Please enter your word:\n"
	my_input = raw_input(prompt)
	counter = 0
	for line in readFile:
		if my_input not in line:
			word = line.strip()
			counter += 1
			print word
	print counter
			
	return True

avoids()

#9.4
def uses_only(word, letters):
	for letters in word:
		if letters in word:
			return True

uses_only('Hello Ace Flo', 'aceflho')

