import re

length = 0

line = open('09.in', 'r').read()

while True:
	m = re.search(r'\((\d+)x(\d+)\)', line)
	if m == None:
		length += len(line)
		break

	length += m.start()
	grouplen = int(m.group(1))
	grouprep = int(m.group(2))
	length += grouplen * grouprep
	line = line[m.end()+grouplen:]
	print line

print length