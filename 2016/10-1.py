import re

class Bot(object):
	def __init__(self, id, start, low, high):
		self.id = id
		self.chips = start
		self.low = low
		self.high = high

	def give_chip(self, chip, bots):
		self.chips.append(chip)

		if len(self.chips) == 2:
			min_chip = min(self.chips)
			max_chip = max(self.chips)
			if min_chip == 17 and max_chip == 61:
				print self.id
			self.chips = []
			bots[self.low].give_chip(min_chip, bots)
			bots[self.high].give_chip(max_chip, bots)

class OutputBot(Bot):
	def give_chip(self, chip, bots):
		self.chips.append(chip)

def get_id(out, id):
	if out == 'bot':
		return id
	else:
		return -(id+1)

def create_bot(out, id):
	if out == 'bot':
		return Bot(get_id(out, id), [], 0, 0)
	else:
		return OutputBot(get_id(out, id), [], 0, 0)

line = raw_input()
starting = {}
bots = {}
while line != '':
	if line[:3] == 'bot':
		m = re.search(r'bot (\d*?) gives low to (bot|output) (\d*?) and high to (bot|output) (\d*)', line)
		origin_id = int(m.group(1))
		low_out = m.group(2)
		low_id = int(m.group(3))
		high_out = m.group(4)
		high_id = int(m.group(5))
		if origin_id not in bots:
			bots[origin_id] = Bot(origin_id, [], 0, 0)

		if get_id(low_out, low_id) not in bots:
			bots[get_id(low_out, low_id)] = create_bot(low_out, low_id)

		if get_id(high_out, high_id) not in bots:
			bots[get_id(high_out, high_id)] = create_bot(high_out, high_id)

		bots[origin_id].low = get_id(low_out, low_id)
		bots[origin_id].high = get_id(high_out, high_id)
	else:
		m = re.search(r'value (\d*?) goes to bot (\d*)', line)
		if int(m.group(2)) not in starting:
			starting[int(m.group(2))] = [int(m.group(1))]
		else:
			starting[int(m.group(2))].append(int(m.group(1)))

	line = raw_input()

for id, vals in starting.iteritems():
	for val in vals:
		bots[id].give_chip(val, bots)