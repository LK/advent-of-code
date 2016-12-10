val = 5

code = ''

line = raw_input()
while line != '':
	for char in line:
		if char == 'U' and val > 3:
			val -= 3
		elif char == 'L' and val % 3 != 1:
			val -= 1
		elif char == 'D' and val < 7:
			val += 3
		elif char == 'R' and val % 3 != 0:
			val += 1

	code += str(val)

	line = raw_input()

print code