import re
from copy import deepcopy

screen = [[0] * 50 for i in range(6)]

def show():
	print '\n'.join(''.join('X' if x else ' ' for x in row) for row in screen)

def rect(width, height):
	for w in range(width):
		for h in range(height):
			screen[h][w] = 1

def rotate_col(col, by):
	copy = deepcopy(screen)
	for i in range(6):
		screen[(i+by)%6][col] = copy[i][col]

def rotate_row(row, by):
	copy = deepcopy(screen)
	for i in range(50):
		screen[row][(i+by)%50] = copy[row][i]

line = raw_input()
while line != '':
	m = re.match(r'rect (\d*?)x(\d*)', line)
	if m != None:
		rect(int(m.group(1)), int(m.group(2)))

	m = re.match(r'rotate column x=(.*?) by (.*)', line)
	if m != None:
		rotate_col(int(m.group(1)), int(m.group(2)))

	m = re.match(r'rotate row y=(.*?) by (.*)', line)
	if m != None:
		rotate_row(int(m.group(1)), int(m.group(2)))

	line = raw_input()

count = 0
for row in range(6):
	for col in range(50):
		if screen[row][col] == 1:
			count += 1

print count