facing = 0
x_offset = 0
y_offset = 0
directions = raw_input('').split(', ')
for direction in directions:
	if direction[0] == 'L':
		facing = (facing - 1) % 4
	else:
		facing = (facing + 1) % 4

	blocks = int(direction[1:])
	if facing == 0:
		y_offset += blocks
	elif facing == 1:
		x_offset += blocks
	elif facing == 2:
		y_offset -= blocks
	elif facing == 3:
		x_offset -= blocks

print abs(x_offset) + abs(y_offset)