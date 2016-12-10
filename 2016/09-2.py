import re

def expand(line):
	length = 0
	while True:
		m = re.search(r'\((\d+)x(\d+)\)', line)
		if m == None:
			return length + len(line)

		length += m.start()
		grouplen = int(m.group(1))
		grouprep = int(m.group(2))
		length += expand(line[m.end():m.end()+grouplen]) * grouprep
		line = line[m.end()+grouplen:]

line = open('09.in', 'r').read()
print expand(line)