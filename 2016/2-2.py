keypad = [
	[None, None, '1', None, None],
	[None, '2',  '3', '4',  None],
	['5',  '6',  '7', '8',  '9'],
	[None, 'A',  'B', 'C',  None],
	[None, None, 'D', None, None]
]

pos = (2, 0)

code = ''

line = raw_input()
while line != '':
	for char in line:
		if char == 'U' and pos[0] > 0 and keypad[pos[0]-1][pos[1]] != None:
			pos = (pos[0]-1, pos[1])
		elif char == 'L' and pos[1] > 0 and keypad[pos[0]][pos[1]-1] != None:
			pos = (pos[0], pos[1]-1)
		elif char == 'D' and pos[0] < 4 and keypad[pos[0]+1][pos[1]] != None:
			pos = (pos[0]+1, pos[1])
		elif char == 'R' and pos[1] < 4 and keypad[pos[0]][pos[1]+1] != None:
			pos = (pos[0], pos[1]+1)

	code += str(keypad[pos[0]][pos[1]])

	line = raw_input()

print code