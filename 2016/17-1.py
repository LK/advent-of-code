import hashlib
import Queue

code = raw_input()

o = ['b', 'c', 'd', 'e', 'f']

initial = (0, 0, [])

visited = set()
q = Queue.Queue()
q.put(initial)

def options(s):
	retval = []
	hsh = hashlib.md5(code + ''.join(s[2])).hexdigest()
	if hsh[0] in o and s[1] > 0:
		retval.append('U')
	if hsh[1] in o and s[1] < 3:
		retval.append('D')
	if hsh[2] in o and s[0] > 0:
		retval.append('L')
	if hsh[3] in o and s[0] < 3:
		retval.append('R')

	return retval

while True:
	s = q.get(False)
	if s[0] == 3 and s[1] == 3:
		print ''.join(s[2])
		break

	for opt in options(s):
		if opt == 'U':
			q.put((s[0], s[1]-1, s[2] + [opt]))
		elif opt == 'D':
			q.put((s[0], s[1]+1, s[2] + [opt]))
		elif opt == 'L':
			q.put((s[0]-1, s[1], s[2] + [opt]))
		elif opt == 'R':
			q.put((s[0]+1, s[1], s[2] + [opt]))