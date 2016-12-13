import Queue

number = int(raw_input())

def is_wall(x, y):
	val = x*x + 3*x + 2*x*y + y + y*y + number
	ones = bin(val)[2:].count('1')

	return ones % 2 == 1

visited = set()

q = Queue.Queue()
q.put((1, 1, 0))

while True:
	x, y, steps = q.get(False)

	if steps > 50:
		print len(visited)
		break
		
	visited.add((x, y))

	if x - 1 >= 0 and not is_wall(x-1, y) and (x-1, y) not in visited:
		q.put((x-1, y, steps+1))
	if x + 1 >= 0 and not is_wall(x+1, y) and (x+1, y) not in visited:
		q.put((x+1, y, steps+1))
	if y - 1 >= 0 and not is_wall(x, y-1) and (x, y-1) not in visited:
		q.put((x, y-1, steps+1))
	if y + 1 >= 0 and not is_wall(x, y+1) and (x, y+1) not in visited:
		q.put((x, y+1, steps+1))