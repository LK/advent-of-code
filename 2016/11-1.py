import itertools
import Queue
from copy import deepcopy
import sys

#initial = (0, [set(['hc', 'lc']), set(['hg']), set(['lg']), set()], 0)
initial = (0, [set(['tg', 'tc', 'pg', 'sg']), set(['pc', 'sc']), set(['qg', 'qc', 'rg', 'rc']), set()], 0)

v = set()
q = Queue.Queue()
q.put(initial)

def done(s):
	return len(s[1][0]) == 0 and len(s[1][1]) == 0 and len(s[1][2]) == 0

def valid(floors):
	for floor in floors:
		gens = set()
		chips = set()
		for elem in floor:
			if elem[1] == 'g':
				gens.add(elem[0])
			else:
				chips.add(elem[0])

		for ch in chips:
			if ch not in gens and len(gens) > 0:
				#print 'Invalid: ' + str(floors) + ' on floor ' + str(floor)
				return False

	return True

def unique_tuple(s):
	floors = []
	mapping = {}
	i = 0
	for floor in s[1]:
		new_floor = set()
		for elem in floor:
			if elem[0] not in mapping:
				mapping[elem[0]] = i
				i += 1
			new_floor.add(str(mapping[elem[0]]) + elem[1])
		floors.append(frozenset(new_floor))
	return (s[0], tuple(floors), s[2])

while True:
	position, state, length = q.get(False)
	print '======= ' + str(length) + ' ======='
	#print state
	possible_positions = [x for x in [position-1, position+1] if x >= 0 and x <= 3]
	for new_position in possible_positions:
		x1 = [set(x) for x in itertools.combinations(state[position], 1)]
		x2 = [set(x) for x in itertools.combinations(state[position], 2)]
		possible_movements = x1 + x2

		for mov in possible_movements:
			new_state = deepcopy(state)
			new_state[position] = new_state[position] - mov
			new_state[new_position] = new_state[new_position] | mov
			new_s = (new_position, new_state, length+1)
			uniq = unique_tuple(new_s)

			if not valid(new_state) or uniq in v:
				#print 'Skipping: ' + str(new_state)
				continue

			if done(new_s):
				print length+1
				sys.exit(0)

			#print 'Adding: ' + str(new_state)
			v.add(uniq)
			q.put(new_s)