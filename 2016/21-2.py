import re

password = [x for x in 'fbgdceah']

cmds = []
l = raw_input()
while l != '':
	cmds.append(l)
	l = raw_input()

for line in reversed(cmds):
	m = re.match(r'swap position (.*) with position (.*)', line)
	if m != None:
		x = int(m.group(1))
		y = int(m.group(2))
		tmp = password[x]
		password[x] = password[y]
		password[y] = tmp

	m = re.match(r'swap letter (.) with letter (.)', line)
	if m != None:
		x = m.group(1)
		y = m.group(2)
		password = [y if char == x else x if char == y else char for char in password]

	m = re.match(r'rotate (left|right) (.*) (step|steps)', line)
	if m != None:
		dir = m.group(1)
		steps = int(m.group(2))
		
		if dir == 'right':
			for i in range(steps):
				password.append(password.pop(0))
		else:
			for i in range(steps):
				password = [password.pop()] + password

	m = re.match(r'rotate based on position of letter (.)', line)
	if m != None:
		letter = m.group(1)
		password.append(password.pop(0))
		idx = password.index(letter)
		if idx % 2 == 1:
			idx += len(password)+1

		rots = idx/2
		
		for i in range(rots):
			password.append(password.pop(0))

	m = re.match(r'reverse positions (.*) through (.*)', line)
	if m != None:
		x = int(m.group(1))
		y = int(m.group(2))
		password = password[:x] + password[x:y+1][::-1] + password[y+1:]

	m = re.match(r'move position (.*) to position (.*)', line)
	if m != None:
		y = int(m.group(1))
		x = int(m.group(2))
		char = password.pop(x)
		password.insert(y, char)

print ''.join(password)