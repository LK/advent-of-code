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

	c = collections.Counter(line)
	chars = sorted(c.items(), key=operator.itemgetter(1), reverse=True)
	bad = False
	for i in range(5):
		if chars[i][0] != checksum[i]:
			if c[checksum[i]] != chars[i][1]:
				bad = True

	if not bad:
		total += int(secid)

	line = raw_input()

print total