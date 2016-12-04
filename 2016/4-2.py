import collections
import operator

total = 0

line = raw_input()
while line != '':
	idx = line.index('[')
	checksum = line[idx+1:-1]
	secid = line[line.rfind('-')+1:idx]
	line = line[:line.rfind('-')]
	line = line.replace('-', '')

	newstring = ''
	for char in line:
		newstring += chr(((ord(char) - 97 + int(secid)) % 26) + 97)
	print newstring + ' ' + secid
	line = raw_input()

print total