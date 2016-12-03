lines = [raw_input(), raw_input(), raw_input()]
count = 0
while lines[0] != '':
	nums = [[int(num) for num in line.split(' ') if num != ''] for line in lines]
	for i in range(3):
		triplet = [nums[x][i] for x in range(3)]
		if 2 * max(triplet) - sum(triplet) < 0:
			count += 1
	lines = [raw_input(), raw_input(), raw_input()]

print str(count)