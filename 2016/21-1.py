import re

password = [x for x in 'abcdefgh']

line = raw_input()
while line != '':
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
		
		if dir == 'left':
			for i in range(steps):
				password.append(password.pop(0))
		else:
			for i in range(steps):
				password = [password.pop()] + password

	m = re.match(r'rotate based on position of letter (.)', line)
	if m != None:
		letter = m.group(1)
		idx = password.index(letter)
		password = [password.pop()] + password
		for i in range(idx):
			password = [password.pop()] + password
		if idx >= 4:
			password = [password.pop()] + password

	m = re.match(r'reverse positions (.*) through (.*)', line)
	if m != None:
		x = int(m.group(1))
		y = int(m.group(2))
		password = password[:x] + password[x:y+1][::-1] + password[y+1:]

	m = re.match(r'move position (.*) to position (.*)', line)
	if m != None:
		x = int(m.group(1))
		y = int(m.group(2))
		char = password.pop(x)
		password.insert(y, char)

	line = raw_input()

print ''.join(password)