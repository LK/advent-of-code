visited = set([(0,0)])

facing = 0
x_offset = 0
y_offset = 0
directions = raw_input('').split(', ')
for direction in directions:
	if direction[0] == 'L':
		facing = (facing - 1) % 4
	else:
		facing = (facing + 1) % 4

	new_positions = None

	blocks = int(direction[1:])
	if facing == 0:
		new_positions = {(x_offset, y_offset + e) for e in range(1, blocks + 1)}
		y_offset += blocks
	elif facing == 1:
		new_positions = {(x_offset + e, y_offset) for e in range(1, blocks + 1)}
		x_offset += blocks
	elif facing == 2:
		new_positions = {(x_offset, y_offset - e) for e in range(1, blocks + 1)}
		y_offset -= blocks
	elif facing == 3:
		new_positions = {(x_offset - e, y_offset) for e in range(1, blocks + 1)}
		x_offset -= blocks

	overlap = visited & new_positions
	if len(overlap) > 0:
		# This could break if we cross more than one path with one motion
		pos = overlap.pop()
		print abs(pos[0]) + abs(pos[1])

	visited.update(new_positions)